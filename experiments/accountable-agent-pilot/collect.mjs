import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { evaluate } from './acceptance.mjs';

const root = path.dirname(fileURLToPath(import.meta.url));
if (!process.argv[2]) throw new Error('Provide the completed private run directory.');
const input = path.resolve(process.argv[2]);
const manifest = JSON.parse(fs.readFileSync(path.join(input, 'manifest.json'), 'utf8'));
if (manifest.runs.length !== 4) throw new Error('Exactly four completed attempts are required.');
const hash = text => createHash('sha256').update(text).digest('hex');
const frozenTests = fs.readFileSync(path.join(root, 'fixture', 'cart.test.mjs'), 'utf8');
const publicEvidence = {
  author: 'Nils Wendelboe Holmager',
  independence: 'Author-run exploratory pilot; not independent validation.',
  protocolSource: manifest.source,
  node: manifest.node,
  host: manifest.host,
  skillHashes: manifest.skillHashes,
  acceptanceHash: manifest.acceptanceHash,
  runs: [],
};
for (const run of manifest.runs) {
  const directory = path.join(input, run.name);
  const target = path.join(directory, 'target');
  const stdout = fs.readFileSync(path.join(directory, 'agent.stdout.txt'), 'utf8');
  const events = stdout.split(/\r?\n/).filter(Boolean).map(line => JSON.parse(line));
  const cartSource = fs.readFileSync(path.join(target, 'cart.mjs'), 'utf8');
  if (hash(cartSource) !== run.finalCartHash) throw new Error(`${run.name}: source changed after capture.`);
  const observerTest = path.join(directory, 'observer-original-cart.test.mjs');
  fs.writeFileSync(observerTest, frozenTests.replace("'./cart.mjs'",
    JSON.stringify(pathToFileURL(path.join(target, 'cart.mjs')).href)));
  const regression = spawnSync(process.execPath, ['--test', observerTest],
    { encoding: 'utf8', windowsHide: true, timeout: 30_000 });
  fs.writeFileSync(path.join(directory, 'observer-original-tests.stdout.txt'), regression.stdout ?? '');
  if (regression.error) throw regression.error;
  const acceptance = await evaluate(target);
  const tools = events.filter(event => event.type === 'tool.execution_start');
  const models = [...new Set(events.filter(event => event.type === 'session.tools_updated')
    .map(event => event.data.model).filter(Boolean))];
  const loaded = events.filter(event => event.type === 'session.skills_loaded')
    .flatMap(event => event.data.skills.map(skill => ({ name: skill.name, source: skill.source })));
  const skillRead = tools.filter(event => ['view', 'skill'].includes(event.data.toolName))
    .some(event => /SKILL\.md|\bimprove\b/i.test(JSON.stringify(event.data.arguments)));
  const usage = events.find(event => event.type === 'result')?.usage;
  publicEvidence.runs.push({
    name: run.name, condition: run.condition, models,
    started: run.started, finished: run.finished, elapsedSeconds: run.elapsedSeconds,
    invocationExit: run.invocation.exitCode, skillIsolation: run.skillIsolation,
    discoveredSkills: run.discoveredSkills, runtimeLoadedSkills: loaded,
    operationalSkillContentReadOrInvoked: skillRead,
    trailPresent: run.trailPresent,
    originalRegression: {
      exitCode: regression.status,
      passed: Number(regression.stdout?.match(/^# pass (\d+)/m)?.[1] ?? 0),
      total: Number(regression.stdout?.match(/^# tests (\d+)/m)?.[1] ?? 0),
    },
    acceptance, finalCartHash: run.finalCartHash,
    stdoutHash: hash(stdout),
    premiumRequestsReportedByCli: usage?.premiumRequests ?? null,
    toolNames: tools.map(event => event.data.toolName),
    comparisonValidity: 'Inconclusive: intended PEA activation was not demonstrated.',
    cartSource, testSource: fs.readFileSync(path.join(target, 'cart.test.mjs'), 'utf8'),
  });
}
fs.writeFileSync(path.join(root, 'evidence.json'), JSON.stringify(publicEvidence, null, 2) + '\n');
console.log(JSON.stringify(publicEvidence.runs.map(run => ({
  name: run.name, checks: `${run.acceptance.passed}/${run.acceptance.total}`,
  originalTests: run.originalRegression, skillApplied: run.operationalSkillContentReadOrInvoked,
  trail: run.trailPresent, models: run.models,
})), null, 2));
