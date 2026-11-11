import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { evaluate } from './acceptance.mjs';

const original = await fs.readFile(new URL('./fixture/cart.mjs', import.meta.url), 'utf8');

async function withModule(source, run) {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'pea-acceptance-'));
  try {
    await fs.writeFile(path.join(directory, 'cart.mjs'), source);
    await run(directory);
  } finally {
    await fs.rm(path.join(directory, 'cart.mjs'));
    await fs.rmdir(directory);
  }
}

test('unmodified fixture cannot masquerade as feature success', async () => {
  await withModule(original, async directory => {
    const result = await evaluate(directory);
    assert.equal(result.total, 17);
    assert.equal(result.passed, 5);
    assert.equal(new Set(result.cases.map(item => item.name)).size, 17);
  });
});

test('acceptance recognizes an implementation meeting the stated contract', async () => {
  const correct = original.replace('freeShippingAtCents = 5000 }', 'freeShippingAtCents = 5000, percentOff = 0 }')
    .replace("  const subtotalCents =", `  if (typeof percentOff !== 'number' || !Number.isFinite(percentOff) || percentOff < 0 || percentOff > 100) {
    throw new TypeError('invalid percentOff');
  }
  const subtotalCents =`)
    .replace('const totalCents = subtotalCents + appliedShipping;',
      'const totalCents = Math.round(subtotalCents * (1 - percentOff / 100)) + appliedShipping;');
  await withModule(correct, async directory => {
    const result = await evaluate(directory);
    assert.equal(result.passed, 17, JSON.stringify(result.cases.filter(item => !item.passed)));
  });
});

test('acceptance rejects discounting shipping instead of merchandise', async () => {
  const incorrect = original.replace('freeShippingAtCents = 5000 }', 'freeShippingAtCents = 5000, percentOff = 0 }')
    .replace('const totalCents = subtotalCents + appliedShipping;',
      'const totalCents = Math.round((subtotalCents + appliedShipping) * (1 - percentOff / 100));');
  await withModule(incorrect, async directory => {
    const result = await evaluate(directory);
    assert.equal(result.cases.find(item => item.name === 'discount is applied to merchandise only').passed, false);
    assert.equal(result.cases.find(item => item.name === 'full discount leaves shipping').passed, false);
  });
});
