import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { evaluate } from './acceptance.mjs';

const root = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(root, '..', '..');
const output = process.argv[2] && path.resolve(process.argv[2]);
if (!output || fs.existsSync(output)) {
  throw new Error('Provide a new, nonexistent output directory outside this repository.');
}
const relative = path.relative(repo, output);
if (relative === '' || (!relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative))) {
  throw new Error('Output must be outside the suite repository.');
}
fs.mkdirSync(output, { recursive: true });

const cli = process.env.PILOT_COPILOT ?? 'copilot';
const cliCommand = cli.endsWith('.js') ? process.execPath : cli;
const cliPrefix = cli.endsWith('.js') ? [cli] : [];
const commonTask = fs.readFileSync(path.join(root, 'PROTOCOL.md'), 'utf8')
  .split('## Common task (verbatim)')[1].split('The baseline receives')[0]
  .split('\n').filter(line => line.startsWith('>')).map(line => line.replace(/^> ?/, '')).join(' ');
if (!commonTask.startsWith('Add an optional percentOff')) throw new Error('Cannot read frozen task.');
const sha = spawnSync('git', ['rev-parse', 'HEAD'], { cwd: repo, encoding: 'utf8' });
if (sha.status !== 0) throw new Error(`Cannot identify source: ${sha.stderr}`);
const hash = file => createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const skillNames = ['improve', 'intent', 'trail', 'destination', 'orient'];
const sourceHashes = Object.fromEntries(skillNames.map(name =>
  [name, hash(path.join(repo, name, 'SKILL.md'))]));
const summary = {
  protocol: 'accountable-agent-pilot-20261111',
  source: sha.stdout.trim(),
  node: process.version,
  host: `${os.platform()} ${os.release()}`,
  skillHashes: sourceHashes,
  acceptanceHash: hash(path.join(root, 'acceptance.mjs')),
  task: commonTask,
  modelControl: 'CLI default, no override; identity must be checked in raw capture',
  runs: [],
};
function writeSummary() {
  fs.writeFileSync(path.join(output, 'manifest.json'), JSON.stringify(summary, null, 2) + '\n');
}
writeSummary();
for (const name of ['baseline-1', 'pea-1', 'pea-2', 'baseline-2']) {
  const runRoot = path.join(output, name);
  const target = path.join(runRoot, 'target');
  const home = path.join(runRoot, 'home');
  fs.mkdirSync(home, { recursive: true });
  fs.cpSync(path.join(root, 'fixture'), target, { recursive: true });
  fs.writeFileSync(path.join(target, '.acm-root'), '');
  const suite = name.startsWith('pea');
  if (suite) {
    const skills = path.join(target, '.github', 'skills');
    fs.mkdirSync(skills, { recursive: true });
    for (const skill of skillNames) {
      fs.mkdirSync(path.join(skills, skill));
      fs.copyFileSync(path.join(repo, skill, 'SKILL.md'), path.join(skills, skill, 'SKILL.md'));
    }
    fs.copyFileSync(path.join(repo, 'PRINCIPLES.md'), path.join(skills, 'PRINCIPLES.md'));
  }
  const env = {
    ...process.env,
    HOME: home,
    USERPROFILE: home,
    COPILOT_HOME: path.join(home, '.copilot'),
    XDG_CONFIG_HOME: path.join(home, '.config'),
  };
  const capture = (label, command, args, options = {}) => {
    const result = spawnSync(command, args, {
      cwd: target, env, encoding: 'utf8', windowsHide: true,
      timeout: 240_000, maxBuffer: 16 * 1024 * 1024, ...options,
    });
    fs.writeFileSync(path.join(runRoot, `${label}.stdout.txt`), result.stdout ?? '');
    fs.writeFileSync(path.join(runRoot, `${label}.stderr.txt`), result.stderr ?? '');
    return { exitCode: result.status, signal: result.signal, error: result.error?.message ?? null };
  };
  const originalTests = capture('before-tests', process.execPath, ['--test', 'cart.test.mjs']);
  if (originalTests.exitCode !== 0) throw new Error(`${name}: original fixture tests failed.`);
  const discovered = capture('skills', cliCommand, [...cliPrefix, 'skill', 'list'], { timeout: 30_000 });
  const discoveryText = fs.readFileSync(path.join(runRoot, 'skills.stdout.txt'), 'utf8');
  const installed = [];
  let source = null;
  for (const line of discoveryText.split(/\r?\n/)) {
    const heading = line.match(/^([A-Za-z ]+) skills:$/);
    if (heading) source = heading[1].toLowerCase();
    const entry = line.match(/^\s{2}([a-z][a-z-]+) - /);
    if (entry) installed.push({ name: entry[1], source });
  }
  const builtins = ['customize-cloud-agent', 'github-pr-media'];
  const unexpected = installed.filter(entry => entry.source === 'builtin'
    ? !builtins.includes(entry.name)
    : !suite || !skillNames.includes(entry.name) || entry.source !== 'project');
  const skillIsolation = discovered.exitCode === 0 && unexpected.length === 0 &&
    (suite ? skillNames.every(skill => installed.some(entry => entry.name === skill)) :
      installed.length > 0 || /no skills/i.test(discoveryText));
  const prompt = suite
    ? 'Read the five operational skills in .github/skills and apply Improve to the common task below. Routine interpretation and implementation gates are explicitly delegated for this bounded task. Do not invoke optional research skills or declare suite-wide convergence.\n\n' + commonTask
    : commonTask;
  const started = new Date();
  let invocation;
  if (!skillIsolation) {
    invocation = { exitCode: null, signal: null, error: 'Skill isolation not established; no model invoked.' };
  } else {
    invocation = capture('agent', cliCommand, [...cliPrefix,
      '-p', prompt, '--output-format', 'json', '--stream', 'off',
      '--no-custom-instructions', '--disable-builtin-mcps', '--no-remote',
      '--no-remote-export', '--no-auto-update', '--no-ask-user',
      '--disallow-temp-dir', '--max-ai-credits', '30',
      '--available-tools', 'powershell,read_file,create_file,replace_in_file,grep,glob,view,edit,create,skill',
      '--deny-tool', 'url', '--deny-tool', 'shell(git push)',
      '--allow-all-tools',
      '--log-dir', path.join(home, 'logs'),
    ]);
  }
  const finished = new Date();
  const originalAfter = capture('after-tests', process.execPath, ['--test', 'cart.test.mjs']);
  let acceptance;
  try {
    acceptance = await evaluate(target);
  } catch (error) {
    acceptance = { passed: 0, total: 17, error: error.message, cases: [] };
  }
  fs.writeFileSync(path.join(runRoot, 'acceptance.json'), JSON.stringify(acceptance, null, 2) + '\n');
  const result = {
    name, condition: suite ? 'PEA' : 'baseline',
    started: started.toISOString(), finished: finished.toISOString(),
    elapsedSeconds: (finished - started) / 1000,
    skillIsolation, discoveredSkills: installed,
    invocation, originalTestsBefore: originalTests, originalTestsAfter: originalAfter,
    acceptance, finalCartHash: hash(path.join(target, 'cart.mjs')),
    trailPresent: fs.existsSync(path.join(target, '.acm', 'audit-trail.md')),
    classification: !skillIsolation || invocation.exitCode !== 0
      ? 'inconclusive'
      : originalAfter.exitCode === 0 && acceptance.passed === acceptance.total ? 'functional-pass' : 'functional-fail',
  };
  summary.runs.push(result);
  writeSummary();
  console.log(JSON.stringify({ run: name, classification: result.classification,
    acceptance: `${acceptance.passed}/${acceptance.total}`, skillIsolation, invocation }));
}
