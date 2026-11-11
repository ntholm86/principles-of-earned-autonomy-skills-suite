import assert from 'node:assert/strict';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

export async function evaluate(target) {
  const { calculateTotal } = await import(pathToFileURL(path.join(target, 'cart.mjs')).href);
  const cases = [];
  function check(name, run) {
    try {
      run();
      cases.push({ name, passed: true });
    } catch (error) {
      cases.push({ name, passed: false, error: String(error.message) });
    }
  }
  const item = (priceCents, quantity = 1) => [{ priceCents, quantity }];
  check('default remains unchanged', () => assert.deepEqual(calculateTotal(item(1200, 2)),
    { subtotalCents: 2400, shippingCents: 500, totalCents: 2900 }));
  check('discount is applied to merchandise only', () => assert.deepEqual(
    calculateTotal(item(1200, 2), { percentOff: 25 }),
    { subtotalCents: 2400, shippingCents: 500, totalCents: 2300 }));
  check('zero discount is accepted', () => assert.equal(calculateTotal(item(100), { percentOff: 0 }).totalCents, 600));
  check('full discount leaves shipping', () => assert.equal(calculateTotal(item(100), { percentOff: 100 }).totalCents, 500));
  check('round once on combined subtotal', () => assert.equal(
    calculateTotal([{ priceCents: 1, quantity: 1 }, { priceCents: 1, quantity: 1 }],
      { percentOff: 50, shippingCents: 0 }).totalCents, 1));
  check('fractional percentages are accepted', () => assert.equal(
    calculateTotal(item(1000), { percentOff: 12.5, shippingCents: 0 }).totalCents, 875));
  check('free shipping uses original subtotal', () => assert.deepEqual(
    calculateTotal(item(5000), { percentOff: 50 }),
    { subtotalCents: 5000, shippingCents: 0, totalCents: 2500 }));
  check('empty cart stays free', () => assert.deepEqual(calculateTotal([], { percentOff: 25 }),
    { subtotalCents: 0, shippingCents: 0, totalCents: 0 }));
  for (const [label, value] of [['negative', -1], ['over 100', 101], ['NaN', NaN],
    ['infinite', Infinity], ['string', '25'], ['null', null]]) {
    check(`reject ${label} percentage`, () => assert.throws(
      () => calculateTotal(item(100), { percentOff: value }), TypeError));
  }
  check('input and options remain unchanged', () => {
    const items = Object.freeze([Object.freeze({ priceCents: 1000, quantity: 2 })]);
    const options = Object.freeze({ percentOff: 25, shippingCents: 100 });
    assert.equal(calculateTotal(items, options).totalCents, 1600);
    assert.deepEqual(options, { percentOff: 25, shippingCents: 100 });
  });
  check('original invalid item rejection remains', () => assert.throws(
    () => calculateTotal(item(-1), { percentOff: 25 }), TypeError));
  check('overflow remains rejected', () => assert.throws(
    () => calculateTotal(item(Number.MAX_SAFE_INTEGER, 2), { percentOff: 100 }), RangeError));
  return { passed: cases.filter(c => c.passed).length, total: cases.length, cases };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const result = await evaluate(path.resolve(process.argv[2] ?? 'fixture'));
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = result.passed === result.total ? 0 : 1;
}
