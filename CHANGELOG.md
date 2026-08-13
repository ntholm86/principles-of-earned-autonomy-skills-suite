# Changelog

## v4.29.0 — 2026-08-13

- **Improve is now the suite's single normal entry point.** A user's prompt, visibly interpreted by automatic Intent, authorizes the current Improve run without requiring prior ACM or Destination setup. Improve explains each service handoff, records the run through Trail, and evaluates whether continued work now needs durable direction.
- **Destination is now evidence-triggered progressive disclosure.** Improve schedules it when accepted mandates reveal stable cross-run direction, future candidates depend on an unstated priority, mandates conflict or attract correction, a governing variable is uncertain, or widening autonomy would compound an assumption. Missing destination files and raw iteration counts never trigger it by themselves; durable direction still requires operator confirmation.
- **First-contact documentation and installer output now teach one action: `/improve`.** Intent and Trail remain automatic, Destination and Orient are triggered services with manual overrides, and Probe remains explicit research instrumentation. `intent/SKILL.md` 1.6.0 -> 1.7.0; `improve/SKILL.md` 3.16.0 -> 3.17.0; `destination/SKILL.md` 2.6.0 -> 2.7.0.

## v4.28.0 — 2026-08-02

- Added an explicit, fail-closed current-destination boundary: Destination may mark a self-contained active mandate only after reconciling every earlier commitment, while preserving prior layers as history.
- Intent, Improve, and Orient now read the bounded active mandate during routine work and widen to the full file for Destination work, ambiguity, conflicts, provenance, or any unmarked/malformed file.
- This makes destination reads scale without trading away operator intent: historical layers remain available, and cheap reads are enabled only by an auditable completeness claim.

## v4.27.2 — 2026-08-02

### Changed

- **Current documentation now uses Agent Context Memory (ACM) as the single name for the suite's memory architecture.** "The Memory Model" was the suite's term before ACM became a separate standard; presenting both names now implies two concepts where only one remains. The README section is now `Agent Context Memory (ACM)`, and all six skill contracts label their place in the architecture as `ACM role`. Historical trail and changelog references remain unchanged. `destination/SKILL.md` 2.5.0 -> 2.5.1; `improve/SKILL.md` 3.15.0 -> 3.15.1; `intent/SKILL.md` 1.5.0 -> 1.5.1; `orient/SKILL.md` 2.6.0 -> 2.6.1; `probe/SKILL.md` 3.4.1 -> 3.4.2; `trail/SKILL.md` 2.5.0 -> 2.5.1.

## v4.27.1 — 2026-08-02

### Changed

- **The README now presents all six skills in one icon-led roster classified by activation.** Active skills are deliberately invoked (Destination, Improve, and research-only Probe), Passive skills always surround substantive work (Intent and Trail), and Triggered skills fire when their conditions are met (Orient). This replaces three overlapping groupings that showed Orient twice and made readers reconcile conceptual roles with implementation services. The six existing inline glyphs from `pea-website` are now reusable SVG assets under `assets/skills/`.

## v4.27.0 — 2026-08-02

### Changed

- **Orientation is now a passive, automatically scheduled service.** A material Destination change schedules Orient after the destination Trail entry is durable. Every Improve run evaluates orientation freshness before recording, then schedules Orient after its Trail entry when meaningful arc evidence has accumulated, the current orientation no longer explains the trail, or convergence is approaching. Raw iteration count alone never triggers an arc-read. The normal operator workflow is now two actions — `/destination` and `/improve`; `/orient` remains a manual diagnostic override. README, QUICKSTART, INSTALLING, and installer output reflect the new boundary. `destination/SKILL.md` 2.4.0 -> 2.5.0; `improve/SKILL.md` 3.14.0 -> 3.15.0; `orient/SKILL.md` 2.5.0 -> 2.6.0.

## v4.26.2 — 2026-08-02

### Changed

- **Default installation now matches the operational command surface.** `install.sh` and `install.ps1` install the five operational capabilities by default, so Probe no longer appears in a normal user's slash-command list. Controlled ARF research explicitly opts in with `--research` or `-Research`, which adds Probe as the sixth skill. README, QUICKSTART, and INSTALLING document both modes. Executable PowerShell checks confirmed the default and research installs contain exactly five and six skill folders respectively.

## v4.26.1 — 2026-08-02

### Changed

- **The newcomer model is now Destination, Orientation, Run.** README, QUICKSTART, INSTALLING, and installer output teach only these three operating concepts: `/destination` establishes direction, `/orient` refreshes orientation, and `/improve` runs the work. Intent and Trail remain automatic implementation services. Probe is now explicitly optional scientific instrumentation for ARF research, is not required or invoked by the other five skills, and can be omitted from operational installs. `probe/SKILL.md` 3.4.0 -> 3.4.1.

## v4.26.0 — 2026-08-02

### Changed

- **Intent and Trail are now explicit automatic services around the three deliberate workflow skills.** Destination, Improve, Orient, and Probe automatically apply Intent before reasoning and Trail after substantive output; standalone installations retain local fallback behavior. README, QUICKSTART, and INSTALLING now teach one operating model: invoke Destination when work begins or direction changes, run Improve for the work, and run Orient periodically when accumulated evidence warrants an arc-read. Intent and Trail remain separately invokable for diagnostics, consequential work outside those workflows, missing-record repair, and independent-writer mode. `intent/SKILL.md` 1.4.0 -> 1.5.0; `destination/SKILL.md` 2.3.0 -> 2.4.0; `improve/SKILL.md` 3.13.1 -> 3.14.0; `trail/SKILL.md` 2.4.2 -> 2.5.0; `orient/SKILL.md` 2.4.0 -> 2.5.0; `probe/SKILL.md` 3.3.0 -> 3.4.0.

## v4.25.2 — 2026-08-02

### Fixed

- **Installation and maintainer commands now match the repository's `harness/tools/` layout.** The one-line installers copy only the six skill files plus `PRINCIPLES.md`, but README/INSTALLING/QUICKSTART and the Improve/Trail helper references still advertised `tools/` paths or implied that optional tooling was installed. Hook instructions now distinguish the target repo working directory from the cloned suite script path; maintainer and `record.py` references use `harness/tools/`; and the docs state explicitly that optional tooling remains in the clone. `improve/SKILL.md` 3.13.0 -> 3.13.1; `trail/SKILL.md` 2.4.1 -> 2.4.2.

## v4.25.1 — 2026-08-01

### Fixed
- **Correction: marker parsing now recognizes assertions by grammar instead of excluding one known false-positive context.** v4.25.0 excluded Trail's `Contradicts prior [!REALIZATION]` label, but its own explanatory trail entry immediately generated three new fake realizations by quoting marker syntax in prose. The parser now accepts a marker only when it begins a line/list item or follows a completed sentence, requires whitespace before the asserted text, supports the historical Markdown-wrapped forms, and rejects double-quoted examples. A seven-case executable matrix passes; full regeneration preserved genuine inline assertions and reduced the archive from 198 to 153 markers by removing 45 additional prose references.

## v4.25.0 — 2026-08-01

### Fixed
- **`record.py learning` no longer turns Trail's "Contradicts prior `[!REALIZATION]`" trigger label into a fake realization.** The parser intentionally uses a permissive mid-line marker search to preserve genuine historical markers, but that also captured the literal marker syntax inside every trigger-evaluation label. The compact learning surface was therefore polluted with synthetic entries beginning `:* not fired`. Added a narrow exclusion for that exact label context, preserving legitimate inline markers. Regeneration removed 88 synthetic archive markers while `verify.py` continued to pass.

## v4.24.0 — 2026-08-01

### Added
- **`intent/SKILL.md`'s Extract step gains a reader-side mirror of Principle 1's own writer-side test.** Principle 1 already tests instruction-*writers*: "if you removed the specific examples, would an intelligent agent still know what to do?" Nothing tested the *reader* side of the same failure — an agent collapsing a prompt's illustrative examples into an exhaustive checklist. Found live, in-session: the operator gave three spontaneous examples of "what understanding a target's purpose might involve," and the agent treated them as a menu to choose from rather than illustrations of a richer, unenumerated category — despite Intent being explicitly invoked by name moments earlier. Added one probe: strip the prompt's examples and check whether the underlying goal is still visible; if the interpretation only holds together because of the specific examples, illustration has been mistaken for enumeration. `intent/SKILL.md` 1.3.1 -> 1.4.0.

## v4.23.0 — 2026-08-01

### Added
- **Restored the OODA/PDCA/pre-mortem lineage citations dropped in the v1-to-v3 merge**, found earlier this session while investigating why self-targeting hadn't derived deutero-learning on its own. `archive/v2/v1_archive/kaizen.md` explicitly credited PDCA, Boyd's OODA loop, and pre-mortem analysis as inspirations; the citation was silently lost when v1/v2's Kaizen+Kaikaku+Hansei merged into v3's Improve. Restored: PDCA/OODA credited in `improve/SKILL.md`'s intro alongside the existing Kaizen/Kaikaku/Hansei lineage note; OODA credited again in `orient/SKILL.md`'s intro specifically (Boyd's insight that Orientation is the neglected, decisive phase — this skill's own namesake); pre-mortem (Klein, 2007) credited at Improve step 4a's pre-commit-prediction mechanic, which was already a pre-mortem in substance. `improve/SKILL.md` 3.12.4 -> 3.13.0; `orient/SKILL.md` 2.3.0 -> 2.4.0.

## v4.22.0 — 2026-08-01

### Added
- **Closed the Kaikaku/Purpose-lens thread with the minimal fix, not a new mechanism.** The operator's own suggestion ("maybe Purpose lens is what should do it") was correct: rather than adding separate incremental-vs-radical branching logic to Orient step 4's deutero-learning close, one clarifying sentence now points to the fact that acting on a routed finding is itself a subsequent Improve iteration on the implicated mechanism — whose existing Purpose lens and Kaikaku question (step 3) already decide incremental vs. redesign generically, for any target. If a redesign results, its validation is named explicitly as Convergence Is Silence, not the agent's own say-so. `orient/SKILL.md` 2.2.0 -> 2.3.0.

## v4.21.0 — 2026-08-01

### Added
- **`orient/SKILL.md` step 4 ("Evaluate loop effectiveness") now explicitly named as Argyris & Schon's deutero-learning** — the third level of their organizational-learning model, distinct from both single-loop (correct the action) and double-loop (correct the target's governing variable, already credited in step 3b). Step 4 already asked substantively deutero-learning-shaped questions ("is the silence earned," "what kind of finding would this loop structurally miss") but never named the lineage, and — unlike step 3b — never closed with an explicit routing instruction when it found something. Added a closing paragraph: when step 4 surfaces a structural blind spot in how the loop itself learns (an untested lens, a trigger that never fires, a trail format that hides evidence), that is named as a candidate revision to the loop's own mechanism and routed to the operator via Destination, mirroring step 3b's existing routing for governing-variable findings. Sourced from a `.acm/destination.md` note (2026-08-01) naming this exact gap, and the finding — while checking lineage — that `archive/v2/v1_archive/kaizen.md` had already cited OODA and pre-mortem analysis as inspirations, a citation silently dropped when v1/v2 Kaizen merged into v3 Improve; not restored in this entry, named as a separate candidate. `orient/SKILL.md` 2.1.1 -> 2.2.0.

## v4.20.0 — 2026-08-01

### Removed
- **`.acm/vision.md` legacy-fallback support removed entirely.** The Vision→Destination rename (v2.0.0, 2026-05-28) added a fallback so repos that hadn't migrated yet would still work — explicitly scoped as transition-period support ("may be removed in a future major version"). Two months later, the fleet migration is confirmed complete (the 8 operator repos migrated 2026-05-28) and no repo touched this session, including `agent-context-memory` and `work-skill`, references `vision.md` at all. Removed every "or legacy `.acm/vision.md`" mention and the migration-hint mechanism from `destination/SKILL.md` (which owned the fallback rule), and the corresponding read-instruction clauses in `improve/SKILL.md`, `intent/SKILL.md`, `orient/SKILL.md` (including its frontmatter description), and `trail/SKILL.md`'s directory listing. `.acm/destination.md` is now the only recognized filename — a repo with only an old `vision.md` will be treated as having no destination yet, the same as any repo that hasn't run Destination. `destination/SKILL.md` 2.2.0 -> 2.3.0; `improve/SKILL.md` 3.12.3 -> 3.12.4; `intent/SKILL.md` 1.3.0 -> 1.3.1; `orient/SKILL.md` 2.1.0 -> 2.1.1; `trail/SKILL.md` 2.4.0 -> 2.4.1.

## v4.19.0 — 2026-08-01

### Fixed
- **Systematic audit of every `verify.py` check's actual implementation against its docstring claim** (the recurring pattern named 4+ times earlier this session). 11 of 12 checks were correctly scoped. Found one real gap: `STALE_PATH_DOCS` (check #11) was missing `QUICKSTART.md` and `harness/BENCHMARKS.md`, both in `REQUIRED_FILES` but structurally uncovered by the stale-path-token check. Confirmed neither currently contains a stale path (no live corruption), so this closes a dormant gap rather than fixing an active defect. Added both to the list.

## v4.18.0 — 2026-08-01

### Fixed
- **`trail/SKILL.md` presented `history.md`, `learning.md`, and `learning-archive.md` as if they were part of the standard commit routine, without ever stating they are optional.** Checked against the actual authoritative spec this skillset implements ([agent-context-memory](https://github.com/ntholm86/agent-context-memory) SPEC.md) — its §6.1 required-files list and §6.3 minimal-conformance criteria name only `destination.md` and `audit-trail.md` as required; `orientation.md` is explicitly optional; `history.md`/`learning.md`/`learning-archive.md` aren't mentioned in either list at all — they're purely a reference-implementation convenience layer named in §1.3. The spec's own reference example (the `agent-context-memory` repo itself) uses exactly 3 files: `destination.md`, `audit-trail.md`, `orientation.md` — the same set another operator project (`work-skill`) independently uses. Updated the directory listing and surrounding prose in `trail/SKILL.md` to mark these three files as explicitly optional, explain when to adopt them (once a trail is long enough that reading it in full every run is wasteful) rather than as a default starting point, and clarify they are never hand-written — only generated by `record.py`, and skippable entirely for a leaner ACM-conformant target. `trail/SKILL.md` 2.3.0 -> 2.4.0.

## v4.17.0 — 2026-08-01

### Fixed
- **`CITATION.cff`'s `version`/`date-released` fields were stale** (3.19.0 / 2026-05-12, several months and ~4 major CHANGELOG versions behind). Synced to the version this fix itself produces (4.17.0), not the version at time of editing — otherwise the file would already be one version stale the moment this commit lands. While checking this, found a separate, more significant issue not fixed here: git tags have not been created for any v4.x release since `v4.0.0` (CHANGELOG has since moved through v4.1.0–v4.16.0 with no corresponding tags), and an existing tag named `v4.18.0` actually points to a commit whose message says "v3.18.0" — almost certainly a historical tagging typo, not a real v4.18.0 release. Neither the missing tags nor the mistagged `v4.18.0` were touched — creating/renaming/deleting tags is release-management territory and tag deletion rewrites shared history, both warranting explicit operator confirmation rather than a unilateral fix inside this entry's scope.

## v4.16.0 — 2026-08-01

### Added
- **`trail/SKILL.md` gains a condensed entry format for changes with no genuine judgment call** (a typo fix, a stale-count correction, a mechanical find-and-replace with an obviously correct outcome) — the full six-section template (Interpretation/Examination/Decision/Prediction/Action/Reflection) exists to make decisions legible, and forcing it onto changes with no decision either produces trivially-restated sections or ceremony padded to look substantive, itself a rationalization risk. The condensed format drops straight to a one-paragraph summary but **never drops the four-trigger evaluation or macro-Hansei** — deliberately, since that is the cheapest part of the template and the mechanism most likely to catch a pattern recurring across several small entries. The criterion is qualitative ("no genuine judgment call"), not a size/line-count threshold, consistent with this suite's own "state the goal, not the steps" principle — a size threshold would be exactly the kind of prescribed-route smuggling Principle 1 exists to prevent. `trail/SKILL.md` 2.2.0 -> 2.3.0. No change needed to `verify.py`'s trigger-evaluation check — it already parses generically by regex, not by section headings.

## v4.15.0 — 2026-08-01

### Fixed
- **`check_no_mojibake()` only ever detected U+FFFD (replacement character) corruption — it had no coverage for the more common windows-1252-misdecoded-UTF-8 corruption pattern (e.g. an em-dash or arrow byte-decoded as windows-1252 instead of UTF-8) that this repo's own memory notes document as having happened twice before via `Get-Content`/`Set-Content` round-trips.** Found during an unrelated hardcoded-count sweep: `INSTALLING.md` (3 instances) and `trail/SKILL.md` (2 instances) contained exactly this kind of corruption in an ASCII-arrow annotation, invisible in a normal editor view (a stray C1 control byte in the corrupted sequence suppressed rendering of the text after it in some tools). Fixed both files (replaced the corrupted 3-character sequence with the correct arrow character), then extended `check_no_mojibake()` with a new `MOJIBAKE_WIN1252` pattern so this class of corruption is caught mechanically going forward. `.acm/audit-trail.md` is exempted from only this new check (not the U+FFFD check) since its own narrative entries legitimately quote corrupted byte sequences as prose evidence — confirmed this exemption is not vacuous (the file genuinely contains one such quoted instance). Verified via positive/negative test: the clean live tree passes, and a synthetic corrupted string is correctly detected.

## v4.14.0 — 2026-08-01

### Fixed
- **`improve/SKILL.md` step 2 said "Three lenses are available" but listed four (Purpose, Inconsistency, Overburden, Waste)** — a stale count left over from when the "Purpose" lens was added after the original three (the Toyota 3M lenses, renamed to English during the v3 redesign: Mura→Inconsistency, Muri→Overburden, Muda→Waste). Fixed by removing the fragile count entirely ("Several lenses") rather than updating it to "Four," since a hardcoded number would just go stale again the next time a lens is added or removed — the same staleness class as several other fixes this session (`REQUIRED_FILES`, ACM traversal file lists). `improve/SKILL.md` 3.12.2 -> 3.12.3.

## v4.13.0 — 2026-08-01

### Added
- **Argyris 1977 double-loop learning was implemented in `improve/SKILL.md` step 6b but not in `orient/SKILL.md`, despite Orient being the skill best positioned to catch governing-variable-level recurrences (it reads the whole arc, not one iteration).** Added step 3b to `orient/SKILL.md`: when step 3 produces a claim describing a recurring pattern, explicitly ask whether the recurrence is a single-loop symptom or a double-loop signal, name the governing variable if so, and route it to the operator via Destination rather than resolving it unilaterally. The question can resolve to "no" — not automatically an escalation trigger. Mirrors step 6b's existing framing; applies the substitution test (no repo-specific nouns). `orient/SKILL.md` 2.0.1 -> 2.1.0.

## v4.12.0 — 2026-08-01

### Fixed
- **`POSITION.md` and `QUICKSTART.md` were both outside `verify.py`'s `REQUIRED_FILES`, leaving them uncovered by the duplicate-H1 check — the exact blind-spot class an old (now-archived) realization explicitly warned would recur ("docs not in `REQUIRED_FILES` should also be spot-checked... adding a broader check would close this blind spot permanently").** Added both files to `REQUIRED_FILES`. While verifying coverage, found `QUICKSTART.md` had a leading UTF-8 BOM silently making its H1 undetectable by the check (0 H1s "found" rather than 1) — stripped it; confirmed via direct byte inspection this was the only content change (no visible text difference). A related, wider finding — many other live files (`verify.py`, `orient/SKILL.md`, `probe/SKILL.md`, `trail/SKILL.md`, `harness/tools/record.py`, `INSTALLING.md`, `.acm/audit-trail.md`, `.acm/orientation.md`, and several `.acm/sessions/*.md` files) also carry a leading BOM — is named but deliberately **not** fixed in this same change; see the corresponding trail entry for why.

## v4.11.0 — 2026-08-01

### Changed
- **`learning.md` is now bounded to a recent window instead of growing unboundedly forever (`harness/tools/record.py`, `trail/SKILL.md` 2.1.0 → 2.2.0, `improve/SKILL.md` 3.12.1 → 3.12.2, `verify.py`).** `learning.md` is read at the start of every improve/orient/intent run (a mandatory step-1 read); before this change it accumulated every `[!REALIZATION]`/`[!REVERSAL]` marker from the entire trail with no ceiling — measured at 120,835 bytes / 282 markers before this change. `record.py learning --write` now keeps only the most recent `LEARNING_RECENT_COUNT` (60) markers in `learning.md` and moves the rest to `.acm/learning-archive.md`, read only when the recent window doesn't cover what's needed. After this change: `learning.md` is 33,880 bytes (60 markers), `learning-archive.md` holds the other 222. `verify.py`'s derived-artifact-freshness check now also validates `learning-archive.md` when it exists (its absence is not a failure — it's only created once the trail is long enough). This is the first dedicated response to the destination's 2026-08-01 note naming token/resource efficiency as a real constraint, not an optimization afterthought — the prior two responses to that note were about reasoning-capability, not efficiency.

## v4.10.0 — 2026-08-01

### Changed
- **`[!DECISION]` entries now require a precedent check against `learning.md`, not just a rationale and rejected alternative (`trail/SKILL.md` 2.0.0 → 2.1.0).** Sourced from a same-session, same-repo failure: a `learning.md` read at session start did not prevent a later decision in the same session from repeating a mistake `learning.md` had already recorded (the self-targeting genericity violation, reverted the same session). The fix is generic — it applies to any `[!DECISION]` on any target with a learning surface, not specific to this suite: state whether the target's `learning.md` was checked for anything directly relevant to *this* decision, and what was found. A single early read is evidence of good practice at session start; it is not sufficient insurance against contradicting a precedent recorded earlier in the same run once a new idea is in play.

## v4.9.1 — 2026-08-01 [correction]

### Reverted
- **`improve/SKILL.md`'s Self-targeting section reverted to its pre-v4.9.0 wording (3.12.0 → 3.12.1).** The v4.9.0 addition named "this suite," a dated destination note, and specific self-targeting behavior inside a skill file that must work generically across any target repo — a direct violation of this suite's own "Generic first" architectural constraint and an already-recorded lesson in `.acm/learning.md` ("remain target-agnostic enough that the self-targeting case falls out without special-casing," from the `reflect-step-hansei-rewrite` entry). Operator caught this immediately on review. The underlying concern (self-targeting runs should be able to surface reasoning-capability gaps, not only artifact-level ones) is not abandoned — it is left unresolved rather than solved with a special-cased instruction, per the same discipline that produced the original wording this change reverts to.

## v4.9.0 — 2026-08-01

### Changed
- **Destination (`.acm/destination.md`) gains a new note naming three gaps: genericity as an explicit self-claim, self-targeting deriving reasoning-capability improvement as a necessary instrument (not just architectural tidiness), and token/resource efficiency as a real constraint.** Operator-authored, per this suite's own rule that destination.md is never written by a skill. Not itself a skill change; recorded here because the improve change below is a direct response to it.
- **`improve/SKILL.md`'s Self-targeting section now names reasoning-capability gaps as a legitimate, distinct outcome from textual/mechanical fixes (3.11.0 → 3.12.0).** Previously the section only distinguished "nothing actionable" from "a list of fixes" or "an argument for redesign" — all three outcomes are artifact-level. Added an explicit self-check for self-targeting runs: is the highest-leverage gap actually in the agent's own reasoning/interpretive capability (intent decompression, governing-variable challenge, learning carry-forward) rather than in the skill files' wording? This is the first improve iteration to act directly on the destination note above, testing whether the loop can derive a reasoning-capability gap in itself rather than only a textual one.

## v4.8.0 — 2026-08-01

### Changed (BREAKING — removes a prior mandate)
- **Trail no longer requires the agent to author a `.acm/sessions/<date>-<slug>.md` session summary (`trail/SKILL.md` 1.19.0 → 2.0.0).** This mandate was added on 2026-05-02 (`trail-v1-10-0-sessions-mandatory`) specifically because no independent, non-agent-authored capture mechanism existed at the time — an agent-authored ("reconstructed") summary was the only available substrate for the "Full resolution" tier, despite the skill's own Fidelity section already ranking it as the weakest tier ("a summary written by the audited party is evidence, but it is not independent evidence"). Two independent capture mechanisms now exist: (1) `llm-harness-proxy`, a tamper-evident hash-chained ledger for harness-routed sessions; (2) the host product's own session/conversation history (e.g. VS Code Copilot Chat's session store, already queried independently by the `chronicle` skill). Requiring the agent to additionally author its own summary duplicates weaker evidence at real token cost. The mandatory artifact remains `.acm/audit-trail.md` — the structured Interpretation/Examination/Decision/Prediction/Action/Reflection entry, which neither raw capture source provides in compact form. The "Three resolutions" table's Full tier and the Fidelity section were both updated to point at independent capture rather than agent-authored files. `.acm/sessions/` is retained only as a legacy location for entries predating this change and as an optional destination if an operator wants a transcript linked manually.

## v4.7.0 — 2026-08-01

### Fixed
- **`PRINCIPLES.md` was silently excluded from `verify.py`'s duplicate-H1-heading check (check 7).** `PRINCIPLES.md` was never added to `REQUIRED_FILES`, so `check_required_markdown_docs()` never analyzed it at all — despite a comment inside that function explicitly (and vacuously) excluding it from a list it was never part of. This meant the exact check born from `PRINCIPLES.md`'s own 2026-04-23 duplicate-H1 splice defect (`v3-principles-copy-repair`) did not apply to `PRINCIPLES.md` itself. Added `PRINCIPLES.md` to `REQUIRED_FILES`; `check_required_markdown_docs()` now runs the duplicate-H1 check on it and only skips its broken-local-link check (its links intentionally point to the external manifesto repo, not local paths). Verified both that `PRINCIPLES.md` currently has exactly one H1 (passes) and that a synthetically spliced second H1 would now be caught (previously would not have been).

## v4.6.0 — 2026-08-01

### Changed
- **`orient/SKILL.md`'s ACM §4 stop-condition wording harmonized with `improve/SKILL.md`, `intent/SKILL.md`, and `destination/SKILL.md` (`orient/SKILL.md` 2.0.0 → 2.0.1).** `orient/SKILL.md` carried the original 2026-06-22 phrasing ("operator ceiling", no "(implementation ceiling)" label) while the other three had been refined since. Found by re-deriving the ACM §4 traversal audit's own selection criterion and applying it exhaustively — the four files needed to match, not just each independently contain some form of the rule.

### Added
- **`verify.py` check 15: ACM §4 scope-traversal wording consistency.** New `check_acm_scope_traversal_consistency()` fails if `improve/SKILL.md`, `orient/SKILL.md`, `intent/SKILL.md`, or `destination/SKILL.md` is missing the "ACM §4 Scoped Memory" paragraph, or if its stop-condition clause (filesystem root, `.acm-root` marker, 4-level ceiling) has drifted from the canonical wording. Mirrors the drift class this repo has already paid for three times (PRINCIPLES.md, CHANGELOG.md, trail/README.md splice defects, 2026-04-24) — here caught mechanically at commit time instead of requiring a fresh-session evaluator to notice by hand. Paired in the same session as the wording fix, per this repo's own operational rule that every spec change must ship with enforcement.

## v4.5.0 — 2026-07-31

### Changed
- **Destination skill now reads parent-scope destinations before forming hunches (`destination/SKILL.md` 2.1.0 → 2.2.0).** Added the ACM §4 Scoped Memory paragraph (parent-directory traversal, `.acm-root` stop marker, 4-level ceiling, higher-scope-wins) to step 1 ("Gather signal"), matching the instruction already present in `improve/SKILL.md`, `orient/SKILL.md`, and `intent/SKILL.md` (added earlier the same day). Found while auditing whether `probe/SKILL.md` and `trail/SKILL.md` also needed the paragraph — they do not (probe never reads destination.md; trail records decisions already made, it does not independently interpret destination) — but the audit surfaced a more consequential gap: Destination is the one skill that *authors* the repo-level `destination.md`, and it was the one skill not reading the workspace-level mandate first. A hunch formed, or a revision written, without the higher-scope destination risks proposing something already settled one level up, or duplicating a coordination constraint that belongs there instead.

## v4.4.0 — 2026-07-31

### Changed
- **Intent skill now reads parent-scope destinations before interpreting a prompt (`intent/SKILL.md` 1.2.1 → 1.3.0).** Added the ACM §4 Scoped Memory paragraph (parent-directory traversal, `.acm-root` stop marker, 4-level ceiling, higher-scope-wins) to the "Read the accumulated context" step, matching the instruction already present in `improve/SKILL.md` and `orient/SKILL.md`. This closes a gap named as the top candidate next move in this repo's own trail on 2026-06-22 (entry `acm-parent-scope-traversal-propagated`) and reconfirmed by the 2026-07-31 orient run — over five weeks between naming and fixing. Without this, an agent applying Intent inside a nested repo (such as this one, under `c:\git\pea\.acm-root`) could interpret a prompt without ever reading the workspace-level mandate that might reshape what the prompt means.

## v4.3.0 — 2026-07-31

### Changed
- **Improve skill's across-trail reflection now names Argyris double-loop learning explicitly (`improve/SKILL.md` 3.10.0 → 3.11.0).** Step 6b's macro-reflection prompts gain a fifth question: when the recurring-finding-class trigger fires, the agent must ask whether the recurrence is a single-loop symptom (the action keeps getting patched) or a double-loop signal (a governing variable in `.acm/destination.md`, or an unstated carried assumption, is the actual defect). When the latter, the entry must name the specific governing variable implicated and route it to the operator via the Destination skill rather than proposing another artifact-level patch. Sourced from operator direction (2026-07-31) to integrate Argyris 1977 double-loop learning into the skillset, captured first as a destination note (`.acm/destination.md`, entry `2026-07-31`) and then left to an Improve iteration to find the highest-leverage integration point. This is additive: no new skill, marker, or file was introduced; the question only surfaces when the existing recurring-finding-class trigger already fires.

## v4.2.0 — 2026-06-04

### Changed
- **Improve skill silence claims now require named boundaries (`improve/SKILL.md` 3.9.2 → 3.10.0).** Step 4a's Silence option now requires every silence claim to name the quality bar the iteration was testing against (internal text-layer consistency, comparative defensibility under hostile external review, comparator coverage, empirical replication, operational deployability), the surfaces in scope, and the bars *not* tested. Mirrors the `retrospect/SKILL.md` step 5a rule introduced in v4.1.0; both originate in the manifesto target's retro-v201 → retro-v202 transition (2026-06-04). The asymmetry between the two skills - retrospect declares silence on arc-level claims, improve declares silence on iteration-level claims - is preserved; both now share the same named-boundary discipline.
- **Destination skill now lists "Quality bar" as an inference shape (`destination/SKILL.md` 2.0.0 → 2.1.0).** Step 2 ("Form sourced inferences") gains a fifth shape: *Quality bar*. The destination skill surfaces the operator-held quality bars early, so a later Retrospect can declare silence against destination-named bars rather than infer them on its own. This closes the loop opened by the v4.1.0 retrospect rule: destinations name bars → retrospects test them → silence is declared against the destination-named set. Soft addition rather than a requirement, consistent with destination's posture of synthesising operator-held intent rather than producing agent-driven content.

Provenance for both changes: this repo's `.trail/audit-trail.md`, entry slug `improve-destination-named-boundary-symmetric`, originating from manifesto target's retro-v201 → retro-v202 transition.

## v4.1.0 — 2026-06-04

### Changed
- **Retrospect skill now requires every silence claim to name its quality bar and surfaces (`retrospect/SKILL.md` 1.8.0 → 1.9.0).** Added step 5a ("Bound every silence claim") requiring that any retrospect-declared silence, convergence, or readiness names which quality bar the silence applies to (internal text-layer consistency, comparative defensibility under hostile external review, comparator coverage, empirical replication, operational deployability, etc.) and which surfaces are in scope, plus an explicit list of bars not tested. Unbounded silence claims ("the target is in good shape", "text-layer silence is now earned") are forbidden because a bar the retrospect has never tested cannot be inside the silence claim. Also added a parallel question to step 4's loop-effectiveness checklist ("Which quality bars has the loop actually tested, and which has it never been challenged on?"). Provenance: promoted from the manifesto target's retro-v201 → retro-v202 transition (2026-06-04), where a retrospect-declared text-layer silence was overturned within the same day by an operator-initiated publication-rigour-review run testing a bar the prior retrospect had never been challenged on. Full provenance in this repo's `.trail/audit-trail.md` under entry slug `retro-named-boundary-rule-from-manifesto-arc`.

## v4.0.0 — 2026-05-28

### Changed (BREAKING — skill rename)
- **Vision skill renamed to Destination** (`destination/SKILL.md` v2.0.0). The skill's behaviour is unchanged; the name was changed because "vision" was reading as fluffy/aspirational while the skill's actual job is to produce a *definitive* operator-held destination. "Destination" carries that semantics directly. Slash command is now `/destination` (was `/vision`). Skill folder is `destination/` (was `vision/`). Internal cross-references in `intent/SKILL.md`, `improve/SKILL.md`, `retrospect/SKILL.md`, `trail/SKILL.md`, `de-ai/SKILL.md` updated accordingly. Top-level docs updated: `README.md`, `QUICKSTART.md`, `INSTALLING.md`, `POSITION.md`, `CITATION.cff`, `.zenodo.json`, `install.ps1`, `install.sh`, `harness/BENCHMARKS.md`, `verify.py` (`REQUIRED_FILES` and `STALE_PATH_DOCS`). Two alternative renames considered and rejected in the same session: retrospect→plan (rejected — retrospect is backward-looking synthesis, "plan" would mislead readers into expecting action items and erode Convergence Is Silence) and improve→execute (rejected — "execute" presupposes the decide-to-act decision that Improve is supposed to make, including the legitimate decision *not* to act).
- **Artifact filename renamed `.trail/vision.md` → `.trail/destination.md`** with a legacy fallback: every skill that reads the operator-held destination now reads `.trail/destination.md` first, falls back to `.trail/vision.md` if only the legacy name exists, and surfaces a one-line migration hint (`git mv .trail/vision.md .trail/destination.md`). The fallback exists for the transition period and may be removed in a future major version. This repo's own `.trail/vision.md` was renamed via `git mv` to preserve history; the H1 header and preamble were updated to match.

## v3.22.0 — 2026-05-23

### Changed
- **Trail harness boundary softened (`trail/SKILL.md` 1.18.0 → 1.19.0):** Removed the mandate that the agent must extract raw harness transcripts to satisfy fidelity. Reasoning capture is now required; verbatim harness extraction is optional. Added an explicit anti-rationalization discipline (write reasoning before action, mark `[!REVERSAL]`, name a rejected alternative, prefer literal quotes, mark fidelity honestly). Verbatim transcripts remain the highest-trust tier when available and link via `transcript-file:` / `transcript-fidelity:`.
- **Operator-held vision path fixed:** Updated `.trail/vision.md` reference to the canonical `.trail/audit-trail.md` (removed stale `.trail/log.md` token).
- **Historical-era policy made explicit:** Added a "Historical-Era Policy" section to `BENCHMARKS.md` and a clarifying comment on `SESSION_FIDELITY_CONTRACT_DATE` in `verify.py`. Pre-contract entries are grandfathered as historical evidence and do not count toward Replicated status on their own.
- **Benchmark publication surface upgraded:** `BENCHMARKS.md` now publishes a Results Matrix v0.1 with explicit per-evaluator-family columns (Claude, GPT, Gemini) and a Status legend (Seed / In progress / Replicated / Pending). B1–B3 are marked Seed pending replication; B4 is marked Replicated under the existing convergence chain.

### Added
- **`QUICKSTART.md`** — a 10-minute, copy-pasteable first-successful-run path. Linked from the README Quickstart section to reduce initial cognitive load.

## v3.21.0 — 2026-05-23

### Added
- **Benchmark publication surface:** Added `BENCHMARKS.md` with a small benchmark set (external improve, external learning carry-forward, cold-target vision, independent convergence check), explicit replication rules, and current evidence status.

### Changed
- **Onboarding wording alignment (fast win):**
  - `README.md`: "These five skills" → "These six skills".
  - `README.md`: Quickstart rewritten as "First Successful Run" with explicit Vision-first and evidence-check steps.
  - `INSTALLING.md`: pre-commit hook reference corrected to `.trail/audit-trail.md`.
  - `INSTALLING.md`: "Full install (all five skills)" → "all six skills" and includes `probe/` in the directory tree.
  - `vision/SKILL.md`: example question updated from five/six to six/seven for consistency.
- **Trail structural fidelity contract:** `trail/SKILL.md` (1.17.0 → 1.18.0) now distinguishes `.trail/sessions/` (summary artifacts) from `.trail/transcripts/` (verbatim exports), updates transcript linking examples, and clarifies fidelity metadata expectations.
- **Verifier hardening:** `verify.py` now enforces:
  - stale path token detection in live docs (`trail/log.md` / `.trail/log.md` → `.trail/audit-trail.md`),
  - session/transcript fidelity structure checks,
  - transcript-file reference existence checks,
  - reversal-cue honesty gate (reversal narration without `[!REVERSAL]` marker fails under contract),
  - local virtual environment exclusion in mojibake scans to avoid third-party package noise.
- **Session fidelity coverage:** Added explicit fidelity metadata to date-stamped summary files in `.trail/sessions/` where missing.

### Added (supporting artifact)
- `.trail/transcripts/README.md` — guidance for verbatim transcript exports and required metadata.

## v3.20.1 — 2026-05-23

### Added
- **Confidential field evidence statement (README):** Added a confidentiality-safe note that the skillset was used successfully in a professional enterprise delivery context with high architectural complexity (multi-tenant cloud, DDD boundaries across microservices, cross-platform requirements, automated CI/CD), including the reported delivery delta (large T-shirt-size scope to completion in 3 days).
- **Confidential field evidence context (POSITION):** Added the same deployment as private field evidence in "What the runs are showing," explicitly stating that the full trail cannot be published due to professional intellectual property and confidentiality obligations. Framed as high-signal evidence, not public proof of generality.

## v3.20.0 — 2026-05-22

### Changed
- **Vision Step 2 reframed:** "Form hunches" → "Form sourced inferences" (`vision/SKILL.md` 1.3.0 → 1.4.0). Adds an explicit acknowledgment that Step 2 superficially resembles the failure mode the framework prevents (agent narrating operator intent), and names the safeguard: every inference must be citable to a specific source, and the operator adjudicates evidence-reading and conclusion independently. Tightens the source requirement from "briefly state what gave you this vision" to a specific citation (quoted phrase, trail entry by date+slug, concrete exchange). Propagates vocabulary change through Step 5, Step 6, and "What this skill does not do."

## v3.19.0 — 2026-05-12

### Changed
- **Trail file renamed:** `.trail/log.md` → `.trail/audit-trail.md`. The new name names its skill (Trail) and its function (audit) explicitly, eliminating the ambiguity of the generic `log.md`. All spec surface updated: `trail/SKILL.md` (1.16.0 → 1.17.0), `improve/SKILL.md`, `intent/SKILL.md`, `probe/SKILL.md`, `retrospect/SKILL.md`, `vision/SKILL.md`, `README.md`, `INSTALLING.md`, `.zenodo.json`, `tools/record.py`, `verify.py`, and `tools/hooks/pre-commit`. Derived artifacts (`.trail/history.md`, `.trail/learning.md`) regenerate with the new header automatically.

### Migration (hard-cut, no legacy fallback)

Existing target repos must rename their file once:

```
git mv .trail/log.md .trail/audit-trail.md
python <skills>/tools/record.py history --write
python <skills>/tools/record.py learning --write
git add .trail/audit-trail.md .trail/history.md .trail/learning.md
git commit -m "trail: rename log.md → audit-trail.md"
```

`record.py` and `verify.py` no longer recognise the old `.trail/log.md` path — they will report it as missing.

## v3.18.0 — 2026-05-12

### Added
- **Structural Enforcement (CI):** New GitHub Actions workflow (`.github/workflows/verify.yml`) runs `verify.py` on every push and pull request to `main`, structurally enforcing trail integrity.
- **Structural Enforcement (Pre-commit Hook):** New cross-platform pre-commit hook (`tools/hooks/pre-commit`) rejects commits that modify substantive files without a corresponding `.trail/log.md` update.
- **One-line Installers:** New `install.sh` and `install.ps1` scripts at the repo root allow users to install all skills with a single command.
- **Hook Installers:** New `tools/install-hooks.sh` and `tools/install-hooks.ps1` scripts allow users to install the pre-commit hook into their own target repositories.

### Changed
- **README.md:** Added a subtitle and compatibility line to improve discoverability through keyword search. Quickstart now leads with the one-line installers.
- **INSTALLING.md:** Restructured to lead with the new one-line install scripts and added instructions for the optional pre-commit hook installation.

## v3.17.4 — 2026-05-04

### Changed
- `.zenodo.json` — full description rewrite. Problem-first structure: accountability under capability asymmetry, the two broken stances, the central question ("what does it take to safely delegate?"). Three principles stated as architectural constraints with their rationale, not as a feature list. Skills presented as the implementation of those constraints, not as a catalogue.

## v3.17.3 — 2026-05-03

### Changed
- `README.md` — added daily-use statement: "These are the skills I use in my daily work as a senior software engineer. I run them on real codebases — not as a showcase."
- `.trail/vision.md` — "revision cycles" corrected to "Retrospect cycles" for terminological precision.

### Fixed
- `.zenodo.json` — title and description updated from "Five" to "Six" skills; Vision added to the skill list and read-order.

## v3.17.2 — 2026-05-03

### Fixed — verify.py now enforces session-file: references

Added check 8 to `verify.py`: every `session-file:` reference in `.trail/log.md` must point to an existing file. Trail v1.10.0 made sessions/ mandatory but the mechanical check was missing — an entry could reference a non-existent session file and verify.py would pass. Named as a gap in three consecutive trail entries before being closed here.

## v3.17.1 — 2026-05-02

### Fixed — Intent now cross-references Vision in "What This Skill Is Not"

`intent/SKILL.md` (v1.2.0 → v1.2.1) — Vision already carried a symmetric note ("It does not replace Intent — Intent is per-prompt, Vision is per-direction") but Intent had no corresponding entry. A practitioner reading Intent alone had no pointer to Vision when direction-level questions arose. Added "Not Vision." item to "What This Skill Is Not", mirroring the existing cross-reference in Vision and making the distinction discoverable from either skill.

## v3.17.0 — 2026-05-02

### Fixed — Trail sessions/ writing is now mandatory with explicit format

`trail/SKILL.md` (v1.9.0 → v1.10.0) — `sessions/` was listed as "optional" in the directory structure and had no explicit write step anywhere in the skill. The agent had guidance about what session files should contain (three-resolution table) but no instruction to actually create one. Fixed: (1) `sessions/` is now mandatory, not optional; (2) a new "Writing the session file" section defines the exact filename convention (`YYYY-MM-DD-<slug>.md`), required content structure, fidelity labeling, the `session-file:` link in `log.md`, and the git commit sequence. Session files are part of every trail commit.

## v3.16.1 — 2026-05-02

### Added — Improve can bootstrap direction on underspecified asks (occasion-independence mechanism)

`improve/SKILL.md` (v3.6.0 → v3.7.0) — step 1 now includes an explicit rule for prompts like "continue"/"keep going"/"next": before examination, the agent must form 1-3 sourced hunches from vision+retrospect.md+recent trail, surface one prioritized falsifiable direction question, and proceed on an explicit highest-confidence assumption if no operator answer is available. This is a structural mechanism for reducing occasion-dependence without overriding operator intent.

## v3.16.0 — 2026-05-02

### Added — Retrospect step 0: read vision.md before arc analysis

`retrospect/SKILL.md` (v1.4.0 → v1.5.0) — vision.md was previously consulted only at the retrospect.md write step, meaning the arc analysis happened without the destination in view. A new step 0 "Read vision first" now precedes the scope statement and arc-read. This matches the pattern Intent already used. The redundant vision reference at the write step was removed.

### Added — all writing skills create `.trail/` directory before any write

`trail/SKILL.md` (v1.8.0 → v1.9.0), `vision/SKILL.md` (v1.2.0 → v1.3.0), `retrospect/SKILL.md` (v1.3.0 → v1.4.0), `improve/SKILL.md` (v3.5.0 → v3.6.0), `probe/SKILL.md` (v3.2.0 → v3.3.0) — no skill previously created the `.trail/` directory explicitly. On a fresh repo the write would silently fail or error. Every write point now carries an explicit instruction: "create the `.trail/` directory in the target repo root if it does not already exist — before any write, regardless of whether the skill runs alone, in a chain, or for the first time."

### Fixed — Vision writes vision.md automatically; operator commits to git

`vision/SKILL.md` (v1.1.0 → v1.2.0 → v1.3.0) — the skill previously instructed the agent to "propose the diff and let the operator commit it," which caused the agent to hand back file-creation work that should have been done automatically. Vision now writes `.trail/vision.md` as part of completing the run. The operator's job is to review and commit to git when it reads right, not to write the file.

### Fixed — POSITION.md signature

Corrected closing signature from hallucinated "— Lars" to "— Nils". Author throughout is **Nils Wendelboe Holmager** ([@ntholm86](https://github.com/ntholm86)).

### Trail — first real Retrospect arc-read

First Retrospect run on this repo with a populated trail (runs 55–71). Produced five arc-level claims: phase boundary crossed (doc-convergence to validated-capability); validation gap shifted from Vision to Retrospect; loop still has no occasion-independence; two-repo relationship not yet in any README; no harness-independent validation yet. retrospect.md updated from operator-seeded to evidence-derived.

## v3.15.0 — 2026-05-02

### Changed — all skills: explicit target-repo anchor for `.trail/` reads and writes

Every skill that reads or writes `.trail/` now explicitly states that `.trail/` is in the **target repo root** — never in the skills install directory. This closes a structural ambiguity: an agent running from the skills install directory could misinterpret bare `.trail/` references as relative to the install location rather than the target.

- `intent/SKILL.md` (v1.1.0 → v1.2.0) — "Read the accumulated context" now opens with the explicit anchor: "the target repo's `.trail/` folder (in the root of the repo being worked on — never in the skills install directory)".
- `improve/SKILL.md` (v3.4.0 → v3.5.0) — same anchor added to the trail-read step; fallback write step now says "`.trail/log.md` **in the target repo root**".
- `probe/SKILL.md` (v3.1.0 → v3.2.0) — fallback write step now says "`.trail/log.md` **in the target repo root**".
- `retrospect/SKILL.md` (v1.2.0 → v1.3.0) — arc-read step now says "`.trail/log.md` **in the target repo root**".
- `vision/SKILL.md` (v1.0.0 → v1.1.0) — signal-gather step now opens with the explicit anchor; vision write step now says "`.trail/vision.md` **in the target repo root**".

`trail/SKILL.md` was already explicit — it is the reference implementation. All other skills now match it.



### Changed
- `intent/SKILL.md` (v1.0.0 → v1.1.0) — "Read the accumulated context" section now explicitly lists `.trail/vision.md` and `.trail/retrospect.md` as the first two documents to read before interpreting any prompt. Vision (operator-held destination) and retrospect.md (Retrospect-derived orientation) are the most important context for intent interpretation; reading only `log.md` and sessions was insufficient. Adds note: if no `.trail/` exists yet, run Vision first.

### Added
- `README.md` — new "The recommended flow for a new codebase" section. Explains the Vision-first onboarding flow (establish vision before the loop starts), the Intent+Improve loop, Trail's role as the evidence record, and Retrospect's role as the arc reader. Includes a table showing which skills read and write to `.trail/`. Captures the operator's articulation of how the skills compose through shared `.trail/` state.



### Added
- `POSITION.md` (v0.1) — new top-level stance document. Names what this repo is betting on: **operation-time trustworthy delegation** — what it takes for a human to safely hand real work to an AI more capable than themselves on that work and remain the responsible party. Defines the area via four sub-claims (operation-time, delegation, evidence-while-driving, protocol-not-tool), maps it against adjacent fields (scalable oversight, agentic AI safety, human-AI collaboration, constitutional AI, SRE), states what the repo is **not** claiming, and lists five explicit falsification criteria. Marked v0.1 and provisional. Aimed at skeptical technical practitioners; signed work, not corporate-we (run 71).
- `.trail/vision.md` — added "What this work is, beyond a skillset" section framing the repo as research as much as development; introduces the trustworthy-delegation question and the dashboard-instruments framing for transparency-while-steering. Drafted from operator intent via Vision, not paraphrased from operator words (run 70).

## v3.13.0 — 2026-05-02

### Changed
- `trail/SKILL.md` (v1.7.0 → v1.8.0) — `history.md` generation is now **manual/on-demand only**. Removed mandatory `record.py history --write` post-session step. Commit step now only requires `log.md` (plus `retrospect.md` if Retrospect ran). `history.md` is a convenience file for humans, not part of the evidence chain — it should not be auto-generated after every session.

## v3.11.0 — 2026-05-01

### Added
- `vision/SKILL.md` (v1.0.0) — new sixth skill. Invoked on demand (not in the autonomous loop). The agent forms guesses about where the operator is heading from signal in conversation, the trail, and the operator's reactions, then surfaces them as short, falsifiable questions the operator can confirm, correct, or reject. Closes the gap between explicit vision (what the operator has written down) and implicit direction (what the agent has picked up but the operator has not articulated). Addresses the human-articulation bottleneck that vision alone cannot solve. Vision never writes to `.trail/vision.md` without operator approval (run 68).
- `README.md`, `CITATION.cff` — updated to describe the suite as six skills (run 68).

---

## v3.10.0 — 2026-05-01

### Added
- `.trail/vision.md` — new optional artifact: the **operator-held destination**. Stable across runs, never written by any skill, read by Improve at step 1 before retrospect.md and trail. Resolves the contract incoherence between Retrospect (which rewrites `.trail/retrospect.md` each run) and operator-written orientation that should not be overwritten. Vision is input to the loop; retrospect.md is output (run 67).

### Changed
- `improve/SKILL.md` (v3.3.0 → v3.4.0) — step 1 read order now: vision → retrospect.md → log. Vision is the destination, retrospect.md is the current location, trail is the path. Resolution rule on disagreement spelled out: vision wins over retrospect.md (operator holds destination); trail wins over retrospect.md (trail is evidence) (run 67).
- `retrospect/SKILL.md` (v1.1.0 → v1.2.0) — step 5 clarified: Retrospect reads vision but never writes to it. retrospect.md shape extended with explicit "What the next runs should test" section (previously implicit). Frontmatter description updated to name vision as input (run 67).
- `trail/SKILL.md` (v1.6.0 → v1.7.0) — directory listing includes `vision.md`; commit step clarifies vision is committed only when the operator changes it, not as a side effect of any agent run (run 67).
- `README.md` — "How it works" updated for the vision/retrospect.md/trail read order (run 67).

---

## v3.9.1 — 2026-05-01

### Added
- `retrospect/SKILL.md` (v1.0.0 → v1.1.0) — new step 5: write `.trail/retrospect.md`, the **retrospect.md** for the target. After each retrospect run the arc-claims are written to `.trail/retrospect.md` — a plain file that distills the current synthesized understanding of the target and orients future runs. Retrospect owns it; Improve reads it (run 65).
- `improve/SKILL.md` — step 1 updated: check for `.trail/retrospect.md` before examining the target; if present, read it first before reading the full trail (run 65).
- `trail/SKILL.md` — directory structure updated to include `retrospect.md`; commit step updated to include `retrospect.md` when Retrospect ran this session (run 65).

---

## v3.9.0 — 2026-05-01

### Added
- `retrospect/SKILL.md` (v1.0.0) — new standalone arc-reflection skill. Reads `.trail/log.md` as a single document about the target and forms falsifiable arc-level claims. Runs independently of Improve when a high-altitude view is needed rather than another incremental pass. Includes an optional loop-effectiveness step (step 4) for evaluating whether the loop is examining the right things — a question that Improve's step 6 explicitly defers (run 64).
- `improve/SKILL.md` — step 6 intro and step 6b updated to reference Retrospect for arc-reads that run outside an improve iteration (run 64).

---

## v3.8.1 — 2026-05-01

### Fixed
- `improve/SKILL.md` step 7 fallback bullet — "Any reflection on the loop itself" replaced with target-anchored prompt matching step 6a (run 55).
- `tools/record.py` STUB_TEMPLATE — bare `TODO` under `### Reflection` replaced with four-section scaffold (falsifiable claim, named blind spot, imagined pushback, conditional macro-Hansei) so agents are prompted with the required structure at stub generation time (run 57).

### Documentation
- `README.md` — "Reflect" step description updated from "Is the loop converging or drifting?" to match v3.8.0 target-anchored Hansei (run 56).
- `README.md` table + `improve/SKILL.md` subtitle — stale 5-word formula "Examine. Decide. Change. Verify. Record." replaced with accurate 7-step sequence matching actual SKILL.md headings (run 60).
- `improve/SKILL.md` frontmatter description — rewritten to name all seven steps accurately; "change it" and "verify" were wrong/absent step names (run 61).
- `.zenodo.json` description — Improve step summary updated to include all six enumerable steps (run 59).

---

## v3.8.0 — 2026-05-01

### Changed
- `improve/SKILL.md` step 6 — "Reflect on the loop itself" replaced with "Reflect", split into two operations:
  - **6a. Per-iteration reflection** runs every iteration. Forces a falsifiable target-model claim, a named blind spot, and a perspective-injection question (what would someone who knows the target push back on).
  - **6b. Across-trail reflection** is conditional. Triggers: recurring *class* of finding, about to declare silence, prior `[!REALIZATION]` contradicted, or operator asked. Reads the trail as one document about the target.
  - Reflection is reframed throughout to be *about the target*, not *about the loop* — addressing templated arc-counting reflections observed across runs 48–53. Storage is the existing `[!REALIZATION]` marker; no new markers, files, or tooling.
  - Skill version: 3.2.0 → 3.3.0.
- `trail/SKILL.md` entry-shape template — the "Reflection" section description rewritten to match the new two-part structure (target-model claim + blind spot + push-back; arc-claim when triggered). Skill version: 1.5.0 → 1.6.0.

---

## v3.7.4 — 2026-05-01

### Fixed
- `.trail/README.md` line 32: `trail/log.md` → `.trail/log.md` in the skill description bullet for Trail.
- `.zenodo.json`: two occurrences of `trail/log.md` → `.trail/log.md` in the Zenodo metadata description HTML (Trail skill description and "Read in this order" list). Published on next Zenodo release.
- `CITATION.cff`: version updated to reflect current HEAD.

---

## v3.7.3 — 2026-05-01

### Fixed
- `tools/record.py` module docstring, subcommand description, and `_parse_entries()` docstring: `trail/log.md` → `.trail/log.md`. Post-rename sweep complete — grep for `[^.]trail/log.` across all live non-CHANGELOG files now returns zero hits.
- `trail/SKILL.md` grep example command: `trail/` → `.trail/` — users copying this to search their evidence directory would have got zero results.
- `trail/SKILL.md` "The test" sentence: `trail/log.md` → `.trail/log.md` — the skill's own definition of what the trail file is now names the correct path.

---

## v3.7.2 — 2026-05-01

### Fixed
- `trail/SKILL.md` frontmatter `description:` field, two example git commands: `trail/log.md` → `.trail/log.md`.
- `README.md`: two references to `trail/log.md` in the "How it works" and "Evidence" sections corrected.
- `verify.py` `REQUIRED_FILES` list: `trail/log.md` → `.trail/log.md`, `trail/README.md` → `.trail/README.md`.

---

## v3.7.1 — 2026-05-01

### Fixed
- `tools/record.py`: added `sys.stdout.reconfigure(encoding='utf-8')` at the start of `main()`. Users on Windows with cp1252 or similar non-UTF-8 default code pages received a `UnicodeEncodeError` on any run that printed trail content containing em-dash or other non-ASCII characters.

---

## v3.7.0 — 2026-05-01

### Changed — Breaking
- Evidence directory renamed from `trail/` to `.trail/` in both the skills repo and the trail skill convention. The hidden-directory convention (`.trail/`) keeps the evidence in the repo without cluttering directory listings.

### Migration
Any target repo that has previously run the trail skill must be migrated:
```bash
git mv trail .trail
git commit -m "trail: rename trail/ to .trail/"
```
Update any CI scripts, `grep` commands, or external links that reference `trail/log.md` → `.trail/log.md` and `trail/history.md` → `.trail/history.md`. Set `$TRAIL_ROOT` if you cannot run `record.py` from the target repo root.

---

## v3.6.1 — 2026-04-30

### Fixed
- `INSTALLING.md`, `README.md`: added `tools/` to the full-install directory tree and quick-start step (missing since v3.5.0 moved `record.py` to the skills install).
- `trail/SKILL.md`, `improve/SKILL.md`, `README.md`: corrected `record.py` path prefix from `tools/record.py` to `<skills>/tools/record.py` — the script lives in the skills install, not the target repo root.
- `INSTALLING.md`, `improve/SKILL.md`: removed all references to `CONVERGENCE_SCOPE_PROTOCOL.md`, which no longer exists in the repo.
- `probe/SKILL.md`: removed unexplained v2 jargon "(Tier 1)" and replaced with a self-contained description of the failure mode being avoided.
- `INSTALLING.md`, `README.md`: removed `verify.py` from the exported `tools/` list; moved it to the repo root as an internal CI script. Users should not copy it to their target repos.

### Rationale
Five documentation-drift fixes found by the convergence loop running self-targeted after v3.6.0. Each finding had the same root cause: when an architectural decision is made, references in surrounding documentation don't get swept. All five are now resolved.

---

## v3.6.0 — 2026-04-30

### Changed
- `trail/SKILL.md` v1.5.0: added `### Multi-iteration runs` protocol under "When to write an entry". Each iteration is a separate trail entry appended and committed **before** the next iteration begins. A partial run must produce partial trail — batch writing at end-of-session is now an explicit violation.
- `improve/SKILL.md` v3.2.0: step 7 "Record" now opens with the multi-iteration requirement. A user who stops a 10-iteration run after iteration 4 must have 4 committed trail entries, not 0.

### Rationale
The per-iteration commit requirement was always implied by "write during the session, not after" but never stated as a structural rule. This session produced evidence that an agent will batch-write at the end unless the rule is explicit: three trail entries written in a single block at session end, rather than one per iteration. The fix makes the checkpoint sequence (`iteration → append entry → record.py history --write → commit`) a first-class part of both skills.

---

## v3.5.0 — 2026-04-30

### Changed
- `tools/record.py` now resolves the trail root from `$TRAIL_ROOT` or current working directory — no longer from its own file location. The script stays in the skills install and writes to whatever target repo invokes it. **No more copying `record.py` into target repos.**
- `trail/SKILL.md`: removed the "copy `record.py` into target repo" init step. Init now creates only `trail/log.md`. Documentation shows invoking `python <skills>/tools/record.py ...` from the target repo root.
- `INSTALLING.md`: same simplification.

### Rationale
A `record.py` showing up in someone else's repo trail folder is noise that creates confusion ("what is this script doing in my repo?"). The skill should leave a minimum, legible footprint in the target repo: `log.md` and `history.md`, both human-readable, both committed. The tool that produces them belongs in the skills install.

### Migration
If an existing target repo has `trail/record.py`, simply `git rm` it — stop committing it going forward. Existing `trail/log.md` and `trail/history.md` are unaffected; regenerate `history.md` by invoking the skills-install copy from the target repo root.

---

## v3.4.0 — 2026-04-30

### Added
- `tools/record.py history --write`: writes `trail/history.md` as committed markdown — a readable, GitHub-renderable summary of all runs. Closes the actual proof-of-improvement gap from v3.0.0: `record.py history` produced terminal output only, not a committed artifact a colleague could read.
- `trail/SKILL.md`: standard workflow now includes regenerating `trail/history.md` after every session. Documented in the directory tree.

### Changed
- `cmd_history` refactored: rendering split into `_render_history(entries, markdown=...)` so the same parser drives both terminal and markdown outputs.

---

## v3.3.4 — 2026-04-30

### Fixed
- `INSTALLING.md`: fully rewritten to match current truth.
  - Trail section corrected: trail lives in target repo root, not in `.copilot/skills/`. Documents `record.py` and `python trail/record.py history` usage.
  - Removed `PRINCIPLES.md` and `CONVERGENCE_SCOPE_PROTOCOL.md` from required files (they have been optional since v3.3.1).
  - "What each skill needs" table updated to "optional" sibling files only.
  - Minimum install simplified: no sibling files needed.
  - Full install directory tree no longer shows `trail/log.md` and `trail/README.md` inside `.copilot/skills/`.

---

## v3.3.3 — 2026-04-30

### Fixed
- `trail/SKILL.md`: trail initialisation now includes copying `record.py` into `trail/record.py` in the target repo. The history viewer is self-contained per project — no dependency on the global skills install path. Usage: `python trail/record.py history` from the repo root.

---

## v3.3.2 — 2026-04-30

### Fixed
- `trail/SKILL.md`: made trail location explicit — the `trail/` folder lives in the **root of the target repo**, not in the skills install directory. Previous wording was ambiguous and agents defaulted to writing the trail relative to themselves (the skills folder). Each repo now gets its own trail.

---

## v3.3.1 — 2026-04-29

### Changed
- `improve/SKILL.md`: principles inlined; `PRINCIPLES.md` and `CONVERGENCE_SCOPE_PROTOCOL.md` references changed to "if available".
- `probe/SKILL.md`: ARF definition inlined; `PRINCIPLES.md` reference changed to "if available".
- `trail/SKILL.md`: added self-init instruction — create `trail/log.md` if it does not exist.

All four skills now operate correctly with only their own `SKILL.md` present — no required sibling files.

---

## v3.3.0 — 2026-04-29

### Added
- `tools/record.py history` subcommand: renders a per-run timeline from `trail/log.md` — date, slug, outcome, delta, decisions. `▸` for change runs, `·` for silence. Closes the proof-of-improvement gap left when the v2 scorecard was removed.
- `INSTALLING.md`: installation guide explaining Copilot's one-level-deep skill discovery rule, minimum vs full install, sibling file requirements, and trail initialisation.

### Changed
- `README.md` opening rewritten to lead with "autonomous self-improving loop" — the first sentence now communicates what this system is, not just what files it contains.
- `README.md` "Using the skills" section links to INSTALLING.md.

---

## v3.2.0 — 2026-04-28

### Added
- `intent/SKILL.md` — Intent as a standalone first-class skill.
- `trail/SKILL.md` — Trail as a standalone first-class skill.

### Changed
- `improve/SKILL.md` — step 1 delegates to Intent when installed; step 7 delegates to Trail when installed.
- `probe/SKILL.md` — step 5 delegates to Trail when installed.
- `README.md` — four-skill description; composable installation progression documented.

---

## v3.1.0 — 2026-04-24

### Changed
- README.md "Versioning and convergence" section updated to reflect convergence achieved.
- CITATION.cff bumped to v3.1.0.

### Evidence
- Skills convergence: 3/3 silence (Anthropic, xAI/Grok, Google/Gemini). Trail slugs: `v3-silence-1`, `v3-silence-2`, `v3-silence-3`.
- Cross-layer coherence: silence. Trail slug: `cross-layer-coherence`.
- All four entries in `trail/log.md`. Verified by `tools/verify.py` (0 failures, 0 warnings).

---

## v3.0.1 — 2026-04-24

### Changed
- trail/README.md corrected to reflect the v3 trail structure and remove the v2 splice tail.

## v3.0.0 — 2026-04-23 (branch `v3-redesign`)

Radical redesign. See [.trail/audit-trail.md](./.acm/audit-trail.md) for the rationale and decision trail.

### Changed
- Skill count reduced from 6 to 2: `improve` (Kaizen + Kaikaku + Hansei + Intent + Kata) and `probe` (Shiken).
- Vocabulary changed from Japanese/TPS terms to plain English. Repo name `kata` retained as a historical codename.
- Trail unified from three files (`TRAIL/`, `GENBA.md`, `SCORECARD.md`) into one append-only `trail/log.md`.
- Scripts ported from PowerShell (~66 KB across 5 files) to Python 3 (`tools/verify.py` + `tools/record.py`, no third-party deps).
- `PRINCIPLES.md` is now an explicit copy of the canonical version in the [autonomous-agent-principles](https://github.com/ntholm86/autonomous-agent-principles) repo.

### Removed
- The Tier 1 self-scoring rubric (10 weighted dimensions). Convergence (Principle 3) is now the only honest measure of done.
- `SCORECARD.md`, `METRICS_HISTORY.md`, `INTEGRITY.json`, `STANDARDS.md`, `PATTERNS.md`, `DESIGN_BACKLOG.md` from the live tree (preserved under `archive/v2/`).
- The `kata`, `kaizen`, `kaikaku`, `hansei`, `shiken`, `intent`, `kiroku` skill directories from the live tree (preserved under `archive/v2/`).
- All `.ps1` scripts from the live tree (preserved under `archive/v2/`).

### Convergence chain
- v2's in-progress 2/3 chain (Gemini 3.1 Pro + Grok Code Fast 1 at score 8.83) is invalidated by Principle 3, condition 2 (material change resets the counter). v3 must converge from zero on its own merits.

---

For history prior to v3, see [archive/v2/CHANGELOG.md](./archive/v2/CHANGELOG.md).
