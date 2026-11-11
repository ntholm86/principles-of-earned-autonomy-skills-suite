import assert from 'node:assert/strict';
import test from 'node:test';
import { calculateTotal } from './cart.mjs';

test('empty cart has no shipping', () => {
  assert.deepEqual(calculateTotal([]), { subtotalCents: 0, shippingCents: 0, totalCents: 0 });
});
test('quantities and shipping use integer cents', () => {
  assert.deepEqual(calculateTotal([{ priceCents: 1200, quantity: 2 }]),
    { subtotalCents: 2400, shippingCents: 500, totalCents: 2900 });
});
test('free shipping includes the exact threshold', () => {
  assert.equal(calculateTotal([{ priceCents: 5000, quantity: 1 }]).shippingCents, 0);
});
test('custom shipping is supported', () => {
  assert.equal(calculateTotal([{ priceCents: 100, quantity: 1 }],
    { shippingCents: 200, freeShippingAtCents: 1000 }).totalCents, 300);
});
test('invalid input is rejected', () => {
  for (const items of [null, {}, [{ priceCents: -1, quantity: 1 }], [{ priceCents: 1, quantity: 0 }]]) {
    assert.throws(() => calculateTotal(items), TypeError);
  }
});
test('overflow is rejected', () => {
  assert.throws(() => calculateTotal([{ priceCents: Number.MAX_SAFE_INTEGER, quantity: 2 }]), RangeError);
});
