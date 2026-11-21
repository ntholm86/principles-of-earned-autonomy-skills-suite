---
name: trail
version: 2.9.0
description: 'Automatic egress service for substantive work. Record a structured entry in the bound memory scope of the shared ACM (a new file in records/; legacy in-repo .acm/audit-trail.md is appended) — recording the interpretation, examination, decisions, actions, and reflection. Destination, Improve, Orient, and Probe apply Trail automatically; the operator should never need to invoke it separately. Direct use remains available for consequential work outside those workflows and independent-writer mode.'
argument-hint: 'The target being worked on (repo, file, system) — used to populate the log entry header'
---

# Trail

*The record of what actually happened.*

*ACM role: Writes the core of the memory layer — the records every other skill reads — and defines where memory lives.*

> **Governing principle:** [Observable Autonomy](../PRINCIPLES.md#principle-2-observable-autonomy) — *The degree of autonomy a system deserves is bounded by the degree of transparency it provides.* This skill is how that transparency is produced.

Autonomy without evidence is abdication. When an agent does work autonomously, the question is never "did it do something?" but "can someone who wasn't there reconstruct what happened, why, and whether to trust it?"

A trail that answers this earns the right to more autonomy. A trail that doesn't — or doesn't exist — means autonomy must be constrained regardless of how competent the work was.

**Automatic composition contract:** In the full suite, Destination, Improve, Orient, and Probe apply Trail automatically whenever they produce a substantive result. The operator should never have to remember or be told to invoke `/trail`. Direct invocation remains available for consequential conversations or manual work outside those workflows, repairing a missing record, and High-Fidelity Mode where the recorder must be independent from the agent that acted.

```
Evidence → Trust → Autonomy
```

---

## Where memory lives

This is the suite's one definition of where memory lives, how it is resolved and how records are written; the other skills refer here. It implements the shared-ACM memory-repository model (ACM SPEC v0.5.0 §3.3, §4, §8).

**Memory repository.** Memory lives in a repository of its own, the shared ACM — never in the skills install and never as a new `.acm/` in a repository of work. Clone it once and add its absolute path as one line of the user-level registry `~/.acm/memories` (Windows: `%USERPROFILE%\.acm\memories`). Nothing is configured per prompt.

```text
destination.md / orientation.md / records/   memory-wide scope (.acm-root marks the top; nothing above it is read)
repositories/<id>/                         repository scope: the same three, plus
  repository.json                          the binding: {"id", "root_commits": [...], "locators": [...]}
  audit-trail.md                           legacy single-file trail, read-only (migrated scopes only)
  tasks/<task>/                            task scope: the same three
  paths/<code/path>/                       path scope: the same three, and its own tasks/
```

One rule: a scope is a folder, and every scope folder has the same three entries — `destination.md` (the operator's mandate; written only by Destination after confirmation), `orientation.md` (Orient's derived synthesis) and `records/` (one file per record; closed months sealed). All are optional until used.

**Resolve before reading or writing.** The work repository's identity is its root commits (`git rev-list --max-parents=0 HEAD`). Across the registered memory repositories, each of which must contain `.acm-root`, exactly one `repositories/*/repository.json` whose `root_commits` intersect is the **bound** scope. Folder names and remote URLs never decide identity, so a renamed clone keeps its memory and two same-named repositories are never conflated. No match is **unbound**; more than one is **ambiguous**; an unreadable registry, memory repository or binding is **unavailable**. `record.py resolve` performs this check.

**When not bound.** Say exactly which case applies. Read and write no guessed memory and never create an `.acm/` in the work repository. Continue only the work the prompt independently authorises, and state that it is not ACM-recorded. Offer to register the repository — create `repositories/<id>/repository.json` with its root commit in a named memory repository — only with the operator's confirmation.

**Legacy in-repo memory.** If the repository is unbound and already has an `.acm/` from an earlier ACM version, that is legacy memory: say so, read it, record in its existing single-file format, create nothing new, and recommend migration.

**Governing chain.** Memory-wide `destination.md` → repository → path → task `destination.md`. Read broadest first and label each ("memory mandate", "repo mandate", "path mandate", "task mandate"); the higher scope wins, and a lower one may narrow but never contradict it. Never read above `.acm-root` and never walk up the code tree for mandates. A required higher mandate that cannot be read blocks the governed work it covers. In legacy memory the chain is the in-repo `.acm/destination.md` and its task scopes.

**Task scopes.** One repository often carries several unrelated tasks, and a single trail then mixes arcs that share nothing but a directory. A task gets a named scope — `tasks/<task>/` in a bound scope, `.acm/<task>/` in legacy memory — with its own trail and optional `orientation.md` and `destination.md`. The active scope is the narrowest that applies: the task scope when the confirmed mandate names a task, else the path scope the work is inside (when one exists), else the repository scope; Intent selects it and names it in its narration (see [intent/SKILL.md](../intent/SKILL.md)). Every skill reads the parent scopes first and reads and writes only the active scope. A task scope is created only when a confirmed mandate names it, never as a side effect of guessing a task boundary; entries are never merged or moved between scopes, and a finished task scope stays as evidence.

**Recording in a bound scope.** Each entry is one new file `records/<UTC yyyyMMddTHHmmssZ>-<slug>.md`; its content is never changed or lost. An existing identifier with identical content is already accepted; with different content it is a collision and gets a new identifier, never an overwrite. A correction is a new record that references the old one. A legacy `audit-trail.md` in a bound scope is read before `records/` and never appended to. Besides the entry fields below, each record states `record` (its identifier), `time` (UTC), `scope`, `repository` (id @ root commit), `authority` (the prompt, destination or delegation acted under) and `mandate` (memory repository commit or destination hash); `agent` is `unknown` when not known, never invented. Ordinary writers do not regenerate and commit derived views in a shared scope: history and learning are generated locally on demand, `orientation.md` is refreshed only by Orient, and each is labelled derived with its source revision. Committing and pushing memory records follows the memory-wide destination's policy; without one, leave them for the operator and say so.

**Sealing.** So the number of files grows with months, not with records, each closed UTC month is sealed. Before writing a record, if the scope's `records/` still holds records from an earlier month, seal that month first as its own commit: create `records/<yyyy-MM>.md` with each of that month's records in file-name order, each preceded by a line `<!-- record: <file name> sha256:<hash> -->` and followed by its content unchanged; remove exactly those records; commit both together. If the sealed file already exists or the push conflicts, someone else sealed it: drop yours and pull. Never edit a sealed file. Sealing needs only git and a SHA-256 tool. Read `records/` in file-name order; sealed months sort first.

**Recording in legacy memory.** One file per scope, `.acm/audit-trail.md` or `.acm/<task>/audit-trail.md`: append-only, one `##` entry per session, newest at the bottom, with `history.md` and `learning.md` regenerated and committed alongside it.

### Helper and commit routine

The skills repository's optional `<skills-repo>/harness/tools/record.py` applies these rules from the work repository's directory (or `$TRAIL_ROOT`); the one-line installer does not copy it and it is never committed to a target. `resolve` prints the bound scope or the reason there is none; `new --slug=<slug>` creates a bound record (`--body-file <file>` accepts a finished entry create-only; a stub created without it is a local draft until committed) or appends a legacy stub; `history`, `learning` and `summary` read a legacy `audit-trail.md` first, then the `records/` records in filename order; `--scope <task>` addresses a task scope and `--path <code/path>` a path scope; together they address a task inside a path scope.

In a bound scope, commit the work in the work repository and the record in the memory repository per its policy, subject `trail: <slug>`. In legacy memory, regenerate the derived files and commit them with the entry:

```
python <skills-repo>/harness/tools/record.py history --write
python <skills-repo>/harness/tools/record.py learning --write
git add .acm/audit-trail.md .acm/history.md .acm/learning.md .acm/learning-archive.md  # learning-archive.md only if it exists; .acm/<task>/... with --scope <task>
git commit -m "trail: <slug>"
```

When the entry records a silence verdict, put the verdict and the evaluator in the commit subject — `git commit -m "trail: <slug> - bounded silence, <model family and version>"` — so the lease state is readable from `git log` without opening the trail.

If Orient ran this session and updated `orientation.md`, include it in the same commit. `destination.md` is operator-managed and is committed only when the operator changes it — never as a side effect of an agent run.

### What a scope holds

Only the trail is required: per the Agent Context Memory specification this skillset implements ([agent-context-memory](https://github.com/ntholm86/agent-context-memory)), minimal conformance is about properties — append-only or create-only source records, author separation, mandate read first, interpretation visible — not about derived files. Everything else is optional:

- `history.md`, `learning.md`, `learning-archive.md` — derived reading aids, never hand-written, generated only by `record.py history --write` / `learning --write`. Adopt them when the trail is long enough that reading it in full every run is wasteful. `learning.md` holds the most recent `[!REALIZATION]` and `[!REVERSAL]` markers with date+slug context, bounded to a recent window; older markers move to `learning-archive.md`, read only when the window does not cover what is needed. Improve, Orient and Intent read them conditionally, before the full trail. In legacy memory they are regenerated at every commit so they never lag the source; in a bound scope they are local views as above.
- `orientation.md` — Orient-derived current orientation; recommended once arc-level synthesis earns its cost. The destination is the goal the operator holds and rarely changes; the orientation is the agent's current synthesis of where the target is, rewritten each Orient run. The destination is input to the loop; the orientation is output.
- `transcripts/` — verbatim transcript exports (see "Independent capture"). `sessions/` — legacy pre-v2.0.0 agent-authored summaries, not written routinely.

Trail does not routinely create agent-authored session summaries.

The `agent:` field names the model family and version as precisely as the host exposes or the operator states (mark operator-stated identity as such, e.g. `Claude Fable 5.1; model identified by the operator`). The host product alone — `GitHub Copilot`, `Cursor` — is not a model family. Principle 3 counts same-family evaluators as one and needs fresh sessions on an unchanged artifact, so a silence entry whose `agent:` names only the host cannot be counted toward convergence.

Each entry — a bound record or a legacy `##` section — follows this shape (a bound record adds the attribution fields above after the heading; `record.py new` writes them):

```markdown
## YYYY-MM-DD — <slug>

- target: <what was worked on>
- operator: <who initiated>
- agent: <model / provider>
- skill: <which skill was applied>
- outcome: <what resulted>
- delta: <version before → after, or a one-line summary of change>

### Interpretation of the ask

<What was asked for, verbatim or as close as possible. What the agent understood it to mean.
If Intent was applied, paste its narration here.>

### Examination

<What was looked at. What each lens revealed — including "nothing actionable.">

### Decision

[!DECISION] <choice made, rationale, alternatives rejected, precedent check>

### Prediction

<Falsifiable statement of what the change will achieve and what it will NOT achieve, committed to BEFORE the action.>

### Action

<What was done. Reasoning shown, not just the diff. Include the actual outcome compared to the prediction.>

### Reflection

<Reflection is about the target, not about the loop. At minimum: an updated
model of the target as a falsifiable claim a future run could disagree with, a
named blind spot in this iteration, and what someone who knows the target
better would push back on.

Then, **every entry must record an across-trail trigger evaluation** — one
short evidence-bearing line per trigger, drawn from the trail. Bare "N/A" is
not allowed; the audit value is showing the check was made, not skipped. The
four triggers are: recurring finding-class, about to declare silence, prior
[!REALIZATION] contradicted, operator explicitly asked for an arc-level
reflection (a request to run the work is not this trigger).

If any trigger fired, also include an across-trail macro-Hansei: an arc-claim
about the target read from the trail as a whole. Mark material insights with
[!REALIZATION].>

### Candidate Next Moves

<Optional. A short ranked list of candidate next moves visible from this
iteration's own examination — blind spots named, follow-ups implied, structural
questions surfaced but deferred. Top-ranked first, one sentence each. Omit if
convergence was declared. The operator may pick, redirect, or ignore; the
ranking exists as arc-level evidence of how the operator-gate steers the work,
not as a step the operator must engage with.>
```

---

## Condensed entries (when there is no decision to record)

The full template exists to make judgment calls legible — decisions, tradeoffs, rejected alternatives — to an observer who wasn't there. Not every entry contains one. A typo fix, a stale-count correction, or a mechanical find-and-replace with an obviously correct outcome carries no real Decision to justify, no alternative worth rejecting, no prediction worth stating beyond "this will fix X." Forcing the full six-section template onto this class of change adds ceremony without adding observability — the sections would either be trivially restated or padded to look substantive, which is itself a rationalization risk (Principle 2 is concerned with fabricated ceremony as much as with hidden reasoning).

Use the condensed format only when the change involves **no genuine judgment call**: nothing was weighed against an alternative, no precedent needed checking because there was no decision to check it against, and the outcome was obviously correct once the defect was seen. This is a qualitative test, not a size threshold — a one-line change that involved a real tradeoff still gets the full template, and a multi-file mechanical fix with no judgment call can use the condensed one. If there is any real tradeoff, any rejected alternative worth naming, or any claim a future run might disagree with, use the full template. When in doubt, use the full template — the condensed format is for the absence of a decision, not a way to avoid documenting one that exists.

The condensed shape:

```markdown
## YYYY-MM-DD — <slug>

- target: <what was worked on>
- operator: <who initiated>
- agent: <model / provider>
- skill: <which skill was applied>
- outcome: <what resulted>
- delta: <version before → after, or a one-line summary of change>

<One paragraph: what was found, what was changed, and how it was verified.
No Decision block — there was no judgment call to record.>

**Across-trail trigger evaluation:**

- *Recurring finding-class:* ...
- *About to declare silence:* ...
- *Contradicts prior [!REALIZATION]:* ...
- *Operator explicitly asked:* ...

<Macro-Hansei only if a trigger fired, per the same rule as the full template.>
```

The four-trigger evaluation and any resulting macro-Hansei are never skipped, even in condensed form — they are the cheapest part of the template and the mechanism most likely to catch a pattern recurring *across* several small, otherwise-unrelated entries (a worked example: a repo's own trail once found the same "a check's coverage is narrower than its stated purpose" defect four separate times across small, individually-unremarkable fixes in one session — only the trigger evaluation, not any single entry's own reflection, had a chance to name that as a pattern rather than four isolated notes).

---

## Three markers

Insert these inline wherever they occur — inside any section, not only Decision:

**`[!DECISION]`** — A choice that could have gone differently. Always include rationale and at least one rejected alternative. Also state a precedent check: whether `learning.md` (or the equivalent memory-of-realizations artifact) was checked for anything directly relevant to *this specific* decision, and what was found (or that nothing relevant was found). A read of `learning.md` at the start of a session is not sufficient insurance against contradicting a precedent recorded earlier in that same session, once a new idea or framing is in play — the check has to happen again, at the point of deciding, not only once at the start.

**`[!REALIZATION]`** — Something discovered during the work that changed understanding.

**`[!REVERSAL]`** — A decision made and then undone. **Both kinds count:** reversing a prior run's decision, *and* backing out of a step planned earlier in the same iteration ("attempted X, then removed it after Y"). Reversals are more valuable than decisions — they show the reasoning evolved. A healthy trail demonstrates consistent reversal density: a long run of entries lacking `[!REVERSAL]`, `[!REALIZATION]`, or outcome-mismatches should be treated as suspect (likely post-hoc rationalization) rather than celebrated as perfection. If your Action and Outcome section narrates "I tried X then removed it," mark it.

```markdown
[!DECISION] Collapsed six skills to two.
Rationale: the framework's mechanism contradicted its own first principle.
Alternative: keep all six, add cross-references — rejected, complexity without payoff.
Precedent check: learning.md had no prior realization about skill count or collapsing; nothing relevant found.

[!REALIZATION] The debug log captures zero conversation content — only session_start metadata.

[!REVERSAL] Initially planned to keep the PowerShell scripts. Reversed after confirming
they bind the suite to one OS for no reason a few hundred lines of Python won't satisfy.

[!REVERSAL] Within this iteration: added a check_non_canonical_markers() function to verify.py.
Reversed after running it produced 46 false positives from entries that mention marker syntax in prose.
The data-loss problem is solved at the source by the regex fix; the style check needs a better heuristic.
```

To find every load-bearing decision across all sessions:

```sh
grep -rn '\[!DECISION\]\|\[!REALIZATION\]\|\[!REVERSAL\]' <scope>/   # the bound scope, or .acm/ in legacy memory
```

---

## Independent capture

Trail serves three observer resolutions:

| Resolution | Source | Answers |
|---|---|---|
| **Digest** | `outcome` and `delta` in the trail | What happened? |
| **Indexed** | `[!DECISION]`, `[!REALIZATION]`, and `[!REVERSAL]` markers | What changed in the reasoning? |
| **Full** | A harness ledger or the host's session history | What was the complete interaction, including dead ends? |

The Full source must be captured independently of the audited agent. Trail does not routinely create a second, agent-authored session summary; structured reasoning belongs in the trail, while full-fidelity telemetry belongs in the harness or host that observed the session.

For every entry:

1. Record the prediction before acting.
2. Mark within-iteration reversals with `[!REVERSAL]`.
3. Name and reject at least one alternative when a decision exists.
4. Prefer literal operator text and tool evidence over paraphrase.

Independent capture is optional for ordinary Trail validity. When the operator wants it surfaced in memory, link or copy it at `transcripts/<date>-<slug>.md` in the active scope and add `transcript-file:` plus `transcript-fidelity:`:

- `verbatim` - exact export from an independent source.
- `verbatim-structural` - independent export produced through a structural capture workflow.
- `reconstructed` - legacy self-authored reconstruction; weakest fidelity and never independent.

Never label reconstructed material as verbatim.

---

## When to write an entry

Every session that produces a decision, realization, or finding. This includes conversations. **There is no such thing as "just conversation" if a decision was made in it.**

The distinction between "doing work" and "having a conversation" is false. A conversation that names a threat, approves a design direction, or rejects an approach is work. If it isn't logged, the next session cannot inherit it. ACM breaks at exactly that boundary.

Write during the session, not after. A trail written from memory compresses and rationalises. The markers belong in context, at the moment the decision or reversal occurs.

If you are unsure whether this session warrants an entry: if a decision was made that the next agent session would need to know about, write the entry. If nothing was decided and nothing was learned, silence is correct.

### Multi-iteration runs

**Each iteration is a separate trail entry. Record it immediately after that iteration completes — before beginning the next iteration.**

Do not buffer entries to write at the end of all iterations. The trail is the checkpoint: if the agent crashes, times out, or the user stops the run after iteration 3 of 10, the first 3 entries must already be recorded.

The mandatory sequence per iteration:

```
iteration N:
  1. record the entry
       bound scope:   create records/<UTC>-<slug>-N.md (record.py new --body-file)
       legacy memory: append to .acm/audit-trail.md, then record.py history --write and learning --write
  2. commit per the "Helper and commit routine" above   ("trail: <slug>-N")
  ↓ only now begin iteration N+1
```

Do not begin the next iteration until both steps are complete. Each record is a checkpoint — if the agent crashes or the user stops after iteration 3 of 10, the first 3 entries already exist. Batching at the end defeats this.

---

## What this skill is not

**Not a log of events.** A log records what happened. A trail records why — the reasoning that made the action the right choice. Without the why, an observer can see the diff but cannot judge whether it was correct.

**Not a post-hoc summary.** Better than nothing. Not the same as a trail written in real time.

**Not overhead.** The three markers take seconds. The cost of skipping them is discovering months later that no one can reconstruct why a critical decision was made.

---

## The test

Can someone who was not present reconstruct what was done, why each significant decision was made, and whether the work achieved what was asked for — using the scope's trail alone, or with it plus an independent capture source (harness ledger, host product history, or a linked transcript) when one exists?

If yes, the trail is sufficient. If no, something is missing.

---

## Composing with other skills

Trail is the automatic egress service for the full suite. Destination, Improve, Orient, and Probe invoke it without operator orchestration. When Intent is active, paste its narration verbatim into the "Interpretation of the ask" section of the same entry — Intent and Trail form the ingress/egress envelope around one substantive operation, not two separate records.

Trail also works standalone for consequential conversations, manual operations, or decisions outside another skill's workflow, and as the independent writer in Improve's High-Fidelity Mode.

The optional `<skills-repo>/harness/tools/record.py` helper can stub a new entry for you:

```sh
python <skills-repo>/harness/tools/record.py new --slug=<slug> --target=<target> --skill=trail
```
