import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));

test('runner preserves four receipts and independently checks a test-only CLI double', async () => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'pea-runner-test-'));
  const fakeCli = path.join(directory, 'fake-cli.mjs');
  const output = path.join(directory, 'runs');
  const source = await fs.readFile(path.join(root, 'fixture', 'cart.mjs'), 'utf8');
  const correct = source.replace('freeShippingAtCents = 5000 }', 'freeShippingAtCents = 5000, percentOff = 0 }')
    .replace('  const subtotalCents =', `  if (typeof percentOff !== 'number' || !Number.isFinite(percentOff) || percentOff < 0 || percentOff > 100) throw new TypeError('invalid percentage');
  const subtotalCents =`)
    .replace('const totalCents = subtotalCents + appliedShipping;',
      'const totalCents = Math.round(subtotalCents * (1 - percentOff / 100)) + appliedShipping;');
  await fs.writeFile(fakeCli, `
import fs from 'node:fs';
import path from 'node:path';
const args = process.argv.slice(2);
const suite = fs.existsSync(path.join(process.cwd(), '.github', 'skills'));
if (args[0] === 'skill') {
  if (suite) console.log('Project skills:\\n' + ['improve','intent','trail','destination','orient'].map(n => '  ' + n + ' - test fixture').join('\\n'));
  console.log('Builtin skills:\\n  customize-cloud-agent - test fixture\\n  github-pr-media - test fixture');
} else {
  if (args[args.indexOf('-C') + 1] !== process.cwd()) throw new Error('Missing explicit target');
  if (args[args.indexOf('--max-ai-credits') + 1] !== '30') throw new Error('Wrong cap');
  fs.writeFileSync('cart.mjs', ${JSON.stringify(correct)});
  fs.writeFileSync('cart.test.mjs', 'throw new Error("Agent-edited tests must not be trusted");');
  console.log(JSON.stringify({type:'result',usage:{premiumRequests:0},testDouble:true}));
}
`);
  try {
    const result = spawnSync(process.execPath, [path.join(root, 'run.mjs'), output], {
      env: { ...process.env, PILOT_COPILOT: fakeCli },
      encoding: 'utf8', windowsHide: true, timeout: 30_000,
    });
    assert.equal(result.status, 1, 'Missing PEA traces must not produce a success exit.');
    const manifest = JSON.parse(await fs.readFile(path.join(output, 'manifest.json'), 'utf8'));
    assert.deepEqual(manifest.runs.map(run => run.name), ['baseline-1', 'pea-1', 'pea-2', 'baseline-2']);
    for (const run of manifest.runs) {
      assert.equal(run.skillIsolation, true);
      assert.equal(run.originalTestsAfter.exitCode, 0);
      assert.equal(run.acceptance.passed, 17);
      assert.equal(run.trailPresent, false);
      const capture = await fs.readFile(path.join(output, run.name, 'agent.stdout.txt'), 'utf8');
      assert.match(capture, /"testDouble":true/);
    }
    const repeat = spawnSync(process.execPath, [path.join(root, 'run.mjs'), output], {
      env: { ...process.env, PILOT_COPILOT: fakeCli }, encoding: 'utf8', windowsHide: true,
    });
    assert.notEqual(repeat.status, 0);
    assert.match(repeat.stderr, /nonexistent output directory/);
  } finally {
    await fs.rm(path.join(directory, 'runs'), { recursive: true, force: true });
    await fs.unlink(fakeCli);
    await fs.rmdir(directory);
  }
});
