# Learning

Auto-generated from `.acm/audit-trail.md` by the `record.py learning --write` command in the autonomous-agent-skills install.
Do not edit by hand — re-run the command to refresh.

Compact chronological extract of the most recent `[!REALIZATION]` and `[!REVERSAL]` markers. The learning surface — what the loop has actually concluded across runs. Read this before reading `audit-trail.md` in full; reach for `audit-trail.md` only when an item here needs its surrounding context.

Showing the most recent 60 markers. 190 older marker(s) are in `.acm/learning-archive.md` — check there if the recent window doesn't cover what you're looking for.

## 2026-08-01 — fix-lens-count-miscount-three-vs-four

**[!REALIZATION]** This is a small but clean example of a pattern this session has now seen many times: a fragile, hardcoded specific (a count, a file list, a version number) drifting silently until something unrelated forces a direct look at the actual text. The fix this time explicitly avoided reproducing the same fragility (choosing "Several" over "Four") rather than just resolving the immediate symptom -- consistent with, and reinforcing, the systemic lesson from the REQUIRED_FILES/BOM arc earlier today.

## 2026-08-01 — fix-lens-count-miscount-three-vs-four

**[!REALIZATION]** The operator-explicitly-asked trigger firing here, combined with the "not fired" recurring-finding-class result, is worth noting precisely because it did NOT fire as recurring: this session has now seen the "fragile hardcoded specific drifts silently" root-cause shape at least three times (REQUIRED_FILES gap, ACM traversal file lists, and now this lens-count miscount) but each instance has been in different subject matter (file-scoping lists vs. prose counts), so the mechanical recurring-finding-class trigger (which tracks entry-to-entry repetition, not cross-session thematic repetition) correctly does not fire. This is itself worth naming as a limit of the trigger: it catches immediate repetition well but would not, on its own, surface "this is the third distinct instance of the same root-cause shape today" without a broader arc-level read -- exactly the kind of thing an Orient run is positioned to catch that a single Improve iteration structurally cannot.

## 2026-08-01 — fix-real-mojibake-corruption-and-extend-check-no-mojibake

**[!REALIZATION]** This session has now found three genuinely different classes of "a mechanical check exists but its actual coverage is narrower than its name/purpose implies": the H1-duplicate check missing PRINCIPLES.md and later POSITION.md/QUICKSTART.md, the BOM issue that no check covered at all, and now check_no_mojibake() itself -- a check whose entire job is "detect mojibake" but which only ever detected one specific corruption signature (U+FFFD) despite this repo's own documented history showing the OTHER signature (windows-1252 misdecoding) is the one that has actually caused real incidents twice. This is the same governing-variable-shaped pattern named in an earlier macro-Hansei today (no single canonical source of truth for what each check actually covers vs. what it claims to cover) showing up a fourth time, in the check most directly named for the exact problem it under-covered.

## 2026-08-01 — fix-real-mojibake-corruption-and-extend-check-no-mojibake

**[!REALIZATION]** This is the fourth occurrence today of the same governing-variable-shaped recurrence (checks whose real coverage is narrower than their stated purpose), and per the imagined-reader pushback above, the accumulation itself is now the more important signal than any individual instance. A systematic audit -- reading every verify.py check function's actual implementation against its docstring/comment claim, in one pass, rather than waiting for the next accidental discovery -- is now a well-evidenced, high-confidence candidate for either a dedicated Improve iteration or the next Orient run's "what next runs should test" section. Naming this explicitly rather than letting a fifth accidental discovery make the same point yet again.

## 2026-08-01 — trail-condensed-entry-format-for-non-decision-fixes

**[!REALIZATION]** This entry itself is a live demonstration of the distinction it creates: this decision involved multiple rejected alternatives, a re-derivation of which architectural layer the concern actually lived in, and a genuine judgment call about where to draw the condensed-format boundary -- exactly the profile that keeps the full template, not the condensed one, even though the *artifact it produces* (a new format for other, simpler future entries) is about reducing ceremony elsewhere. The decision to keep ceremony proportional to judgment, rather than uniformly reducing it, is validated by needing the full template to make this exact decision legible.

## 2026-08-01 — trail-condensed-entry-format-for-non-decision-fixes

**[!REALIZATION]** This is the first entry in this session where the operator explicitly handed over a governing-variable-level decision rather than picking from a ranked list or delegating a narrower, already-scoped choice (as with the BOM-grouping decision). Read against the arc as a whole: the operator-gate in this session has now been exercised in at least four distinct shapes -- ranked-candidate selection, narrow delegated autonomy (BOM grouping, operator unavailable), direct operator-initiated diagnostic questions (the Argyris-in-Orient gap), and now full delegation of an architectural-format decision with an explicit instruction to reason from destination and inferred intent. Each shape places different demands on the agent's judgment, and this is the first case testing whether the agent, given real latitude, converges on a *narrower* change than the destination-level revision the framing implied ("what should we do about ceremony overhead") -- which is what happened here: the decision made is smaller in destination-level footprint than the question as posed, because closer reading found the actual concern lived one layer down from where it was first framed.

## 2026-08-01 — citation-cff-currency-fix-surfaces-git-tag-drift

**[!REALIZATION]** This is the first time the new condensed-entry-format decision has actually been tested in practice, and it immediately produced the predicted failure mode from its own blind-spot note: a task selected specifically as a condensed-format candidate ("the smallest, most mechanical" backlog item) turned out to contain a real judgment call once actually investigated (what version number to use given the CHANGELOG/tag mismatch; whether to touch the tags at all). This is direct, fast evidence for the condensed format's own "when in doubt, use the full template" bias working as intended -- the format correctly escalated to full treatment once a real decision appeared, rather than the investigation being artificially truncated to fit a pre-chosen ceremony level.

## 2026-08-01 — citation-cff-currency-fix-surfaces-git-tag-drift

**[!REALIZATION]** Per the lighter-weight-pointer convention established earlier today: the governing-variable diagnosis stands unchanged from `confirm-bom-root-cause-and-fix-verifypy` and its subsequent restatements -- this entry is the fifth instance of the same shape, now extending beyond "verify.py checks" and "file lists" into "release/tag hygiene," which broadens the diagnosis's scope slightly (it is not just a verify.py-specific problem, it is a general pattern in how this repo tracks "what is the current true state" across several independent bookkeeping mechanisms -- CHANGELOG prose, git tags, verify.py's REQUIRED_FILES/STALE_PATH_DOCS/ACM_SCOPE_TRAVERSAL_FILES lists, and now CITATION.cff -- each maintained by hand, each capable of independently drifting from the others). This broadened framing is itself worth carrying into the still-pending "systematic verify.py audit" candidate move, which should now perhaps be reframed more broadly as a systematic audit of every hand-maintained "current state" claim in the repo, not only verify.py's checks specifically.

## 2026-08-01 — clarify-history-learning-optional-per-acm-spec-conformance

**[!REALIZATION]** This is the sixth distinct instance today of "a claim (this time, an operator-stated premise, not a mechanical check) turned out to be checkable and slightly inaccurate once actually verified against a primary source rather than accepted or inferred" -- following PRINCIPLES.md's H1 gap, the POSITION.md/QUICKSTART.md REQUIRED_FILES gap, the systemic BOM issue, check_no_mojibake's narrow coverage, and the git tag drift. This one is different in kind from the prior five: those were all mechanical artifacts within this repo; this one is a conceptual/architectural claim about this repo's relationship to an external spec. The same discipline (check the primary source directly, don't reason from memory or file-name pattern-matching) resolved it the same way.

## 2026-08-01 — clarify-history-learning-optional-per-acm-spec-conformance

**[!REALIZATION]** Per the lighter-weight-pointer convention: the core governing-variable diagnosis (no single source of truth for several categories of "current state" claims across this repo) stands as recorded in `confirm-bom-root-cause-and-fix-verifypy` and its restatements, now broadened a second time today (first to release/tag hygiene in the CITATION.cff entry, now to this repo's own claimed relationship to an external governing spec). Both broadenings share the same root shape and do not require a new diagnosis, only an acknowledgment that the pattern's scope keeps turning out to be wider than each individual instance suggested. Worth naming as a candidate for the still-pending systematic-audit candidate move: that audit should now explicitly include checking this repo's stated relationships to external repos (agent-context-memory, evo, ai-steward, llm-harness-proxy) against those repos' actual current content, not just this repo's own internal artifacts.

## 2026-08-01 — destination-note-skillsuite-as-acm-development-site

**[!REALIZATION]** This destination note is qualitatively different from every prior one: all previous notes described gaps *within* this repo's own self-conception (efficiency, reasoning-capability, action-gating). This is the first note describing a *relationship* to something outside the repo as a standing destination-level expectation. If this note holds up, it changes what "done" can mean for a future Improve/Orient run on this repo -- convergence would need to also ask "did this arc produce anything that belongs upstream, and if so, was it surfaced rather than absorbed silently," which is a genuinely new dimension the existing convergence framing (silence per named quality bar) does not yet explicitly cover.

## 2026-08-01 — destination-note-skillsuite-as-acm-development-site

**[!REALIZATION]** This entry is a live test of the destination note it just added: it recognized the Scale-gap/learning.md-pattern connection as evidence worth citing in a destination-level note, rather than only as conversational color. Whether that recognition generalizes to future, less operator-prompted instances -- the loop noticing a spec-level implication on its own initiative, the way this session has repeatedly tested whether the loop derives reasoning-capability gaps unprompted -- remains exactly as untested as every prior version of that same open question in this repo's trail.

## 2026-08-01 — implement-scale-gap-in-acm-spec-repo

**[!REALIZATION]** The destination note added earlier this session ("this repo is the site of ACM's own development") was tested within the same conversation that named it, and held: a concrete finding (the Scale gap, the learning.md pattern) was recognized as spec-relevant, surfaced explicitly rather than left as a local-only improvement, drafted as a candidate, and -- once authorized -- actually implemented in the correct upstream location. This is the fastest a destination note has gone from stated expectation to exercised instance in this repo's history.

## 2026-08-01 — implement-scale-gap-in-acm-spec-repo

**[!REALIZATION]** Per the lighter-weight-pointer convention: no new governing-variable diagnosis is introduced by this entry. It is the direct execution of the destination note added immediately before it in this same session, and the substantive precedent-checking and decision reasoning for the cross-repo action itself lives in agent-context-memory's own trail, not here. What is new is the confirmation that the destination note's own falsifiability test ("does a future entry actually surface and act on a spec-level finding, or does the note sit unused") has already been answered once, within the same conversation that posed it.

## 2026-08-01 — systematic-verifypy-audit-closes-stale-path-docs-gap

**[!REALIZATION]** This closes the loop the recurring-finding-class trigger has been naming all day: rather than a fifth accidental discovery of the same pattern, this entry performed the actual systematic pass and found the audit produces a much smaller yield than the accumulated anxiety about it suggested -- one dormant gap, not another BOM-scale issue. That is itself informative: the pattern recurred because each individual instance was found in a different subject area (file lists, encoding checks, version metadata, git tags), not because verify.py as a whole is unreliable. A single deliberate pass was sufficient to confirm the check suite is now in good shape, closing this as a standing concern rather than a permanently-open one.

## 2026-08-01 — orient-how-close-to-destination

**[!REALIZATION]** This window produced the first evidenced cross-repo contribution to ACM's own governing specification (agent-context-memory), completing recognition -> draft -> authorization -> implementation -> push within one conversation -- the strongest evidence yet for destination.md's "research success" condition.

## 2026-08-01 — orient-how-close-to-destination

**[!REALIZATION]** The clearest finding from reading the full window as one document: every entry this session was either internal self-consistency work or a contribution to a repo the same operator also controls. Nothing gathered or produced evidence of use by anyone who is not the operator. Destination.md names both research success and adoption success as necessary; this session, for all its real velocity, advanced only the former. Named plainly in orientation.md's direct answer, not softened.

## 2026-08-01 — orient-how-close-to-destination

**[!REALIZATION]** Read as the whole arc from the very first v3-redesign entry through today: the loop has repeatedly demonstrated it can find, diagnose, and fix genuine defects (mojibake, BOM corruption, file-scope gaps, version drift) and can even extend its own reasoning framework (double-loop learning in two skills) and contribute upstream to a different repo's specification. What it has not yet done, across the entire trail, not just this window, is produce or seek evidence that anyone other than the operator has picked this up. This is the single most load-bearing gap this repo's own destination names, and today's session -- despite being unusually productive -- did not close any distance on it. Naming this as the arc's actual state, not just this window's, since the pattern is consistent across the whole history, not new to today.

## 2026-08-01 — remove-vision-md-legacy-fallback

**[!REALIZATION]** This is a clean example of a compatibility shim being retired on schedule rather than accumulating indefinitely as unexamined insurance -- the original design (destination/SKILL.md, 2026-05-28) explicitly named the condition for its own removal ("the transition period... may be removed in a future major version") rather than leaving it open-ended, and this entry is that condition being checked and found satisfied, not assumed. This is a small but genuine instance of the suite's own design discipline (name the retirement condition, don't just add compatibility forever) paying off.

## 2026-08-01 — remove-vision-md-legacy-fallback

**[!REALIZATION]** No new governing-variable diagnosis needed here; this entry does not extend or contradict the day's other recurring-pattern diagnoses. It is worth noting as a distinct, positive category from those: this is the first entry today that closes a piece of the suite's OWN evolution (retiring a self-scoped temporary feature) rather than fixing a defect (encoding, file-scope, version drift). The suite's design discipline of naming removal conditions in advance, rather than leaving compatibility shims open-ended, is what made this decision fast and low-risk to make today.

## 2026-08-01 — confirm-push-and-record-trail-completeness-check

**[!REALIZATION]** Not every operator action needs its own trail entry the instant it happens, but a real, consequential action (publishing 13 commits to a public repo) sitting unrecorded across a conversational-compaction boundary is a genuine gap worth naming: the trail's completeness currently depends on someone (here, the operator) noticing the gap, since no mechanical check verifies that every git push event has a corresponding audit-trail.md entry.

## 2026-08-01 — deutero-learning-credited-and-closed-in-orient-step-4

**[!REALIZATION]** Naming something that already exists in substance as an explicit instance of cited theory closed a real gap - the missing routing instruction - but the larger, harder question the operator named (how a Purpose-driven loop derives gaps like this on its own, generically) is not solved by this single fix. This entry is evidence for the standing destination note's claim, not a refutation of the need for the broader Purpose-lens reframing still sitting unimplemented.

## 2026-08-01 — exclude-trigger-label-references-from-learning-markers

**[!REALIZATION]** The most-read memory artifact was mechanically fresh yet semantically contaminated by its own Trail template. This is concrete evidence for the destination's model-capability/fidelity concern: structured artifacts reduce error only when their parser distinguishes a claim from a reference to the syntax of a claim.

## 2026-08-01 — generalize-learning-marker-parser-from-context-exclusion-to-assertion-grammar

**[!REALIZATION]** The prior fix demonstrated exactly why expanding exception lists is the wrong abstraction for semantic parsing: it removed the dominant false-positive class while its own explanation immediately created another. Assertion boundaries generalize; phrase exclusions do not.

## 2026-08-01 — generalize-learning-marker-parser-from-context-exclusion-to-assertion-grammar

**[!REVERSAL]** Reversed v4.25.0's context-specific `TRIGGER_REALIZATION_REFERENCE` strategy after its own explanatory entry produced three new fake realizations. Replaced it with left-boundary assertion grammar and a double-quoted-example guard. The seven-case matrix passed. Full regeneration reduced the archive from 198 to 153 markers (45 more references removed), preserved the eight inspected genuine inline assertions, and `verify.py` passed. Prediction held.

## 2026-08-02 — align-installed-skill-docs-with-harness-tool-layout

**[!REALIZATION]** The verifier's stale-path coverage is semantically narrow: it catches obsolete trail filenames, but not documented executable paths that no longer exist. This installation defect survived a recent systematic verifier audit because command-path validity is a distinct quality bar from trail-path token consistency.

## 2026-08-02 — refresh-iteration-count-and-readme-totals

**[!REALIZATION]** This is the third distinct hand-maintained "current state" artifact this repo's trail has found stale and fixed individually (CITATION.cff version/tags, verify.py's own file-scope lists, now ITERATION-COUNT.md/README's iteration claim) - each discovered independently, each fixed the same way, none converted into a standing mechanical guarantee. The recurrence across three unrelated sessions, not just within one, is stronger evidence than any single instance that the governing variable is "this repo has no mechanism that prevents a hand-counted claim from drifting," not "this one document happened to go stale."

## 2026-08-02 — confirm-iteration-count-sync-scope-across-live-docs

**[!REALIZATION]** Not every unsynced number is the same defect. This repo's evidence-currency problem now has two named subclasses - stale-precise (fixed by resyncing) and vague-floor (a style choice, not a defect) - and treating them identically would have produced either a false fix (rewriting archival metadata on an inference) or an omission (leaving `INSTALLING.md` inconsistent with README's newly precise figure for no reason).

## 2026-08-02 — automatic-intent-trail-workflow

**[!REALIZATION]** Installer completion text is part of the product contract. The first full-doc pass still missed two lines that would have taught the old six-command model at the exact moment a user begins. The contradiction scan, rather than file taxonomy, exposed the real boundary.

## 2026-08-02 — automatic-intent-trail-workflow

**[!REALIZATION]** The suite's complexity problem was not six separate capabilities; it was exposing six capabilities as six operator responsibilities. Earlier iterations repeatedly simplified placement and wording while preserving evidence machinery underneath. This change applies the same pattern to runtime composition: keep distinct ownership boundaries, collapse the user's required control surface. The recurring drift risk now moves to any surface that enumerates skills without also naming their operating role.

## 2026-08-02 — destination-orientation-run-mindset

**[!REALIZATION]** The smallest honest description of the suite has three layers with different counts: three concepts for the user, five capabilities for operation, six capabilities for research. Previous descriptions kept collapsing these counts into one taxonomy, which forced either infrastructure or instrumentation into the user's mental model. Naming the layers separately resolves that tension without deleting functionality.

## 2026-08-02 — passive-evidence-triggered-orientation

**[!REALIZATION]** The arc's repeated simplifications reveal a stronger architecture than the earlier three/five/six count: capability count and operator action count are independent. Destination and Improve are the only deliberate control inputs; Intent, Trail, and Orientation are feedback infrastructure. Probe remains external instrumentation. The suite's public model should be organized by agency - what the operator decides versus what the system maintains - rather than by how many skill files exist.

## 2026-08-02 — passive-evidence-triggered-orientation

**[!REVERSAL]** Focused validation exposed that append-only ordering contradiction before documentation changed. Moved evaluation before Trail and kept only the actual Orient handoff after durability.

## 2026-08-02 — orient-passive-control-surface-arc

**[!REALIZATION]** Orientation's importance never implied operator agency. Treating every important capability as a command was the governing mistake behind the repeated taxonomy revisions. The architecture now separates authority from maintenance: the operator controls direction and action; the system maintains interpretation, evidence, and situational awareness.

## 2026-08-02 — orient-passive-control-surface-arc

**[!REVERSAL]** The run-204 model of "three concepts for the user" was a useful plateau but not the stable boundary. The arc shows that conceptual importance and operator responsibility were still conflated. Revised to two deliberate actions plus passive Orientation; retained the underlying capability rather than deleting or weakening it.

## 2026-08-02 — unify-readme-skill-roster-by-activation

**[!REALIZATION]** The prior README architecture accurately described internal composition but exposed too many valid taxonomies at once. A first-contact model should classify each capability by one question only: how does it activate? Roles, artifacts, and research status belong inside the row, not in competing rosters.

## 2026-08-02 — retire-memory-model-name-in-favor-of-acm

**[!REALIZATION]** Standardization changes what simplicity requires. Before ACM existed, The Memory Model gave the architecture a coherent name. After ACM became the separate standard, the same phrase became translation debt. A useful local concept can become waste when its underlying idea acquires a canonical shared name.

## 2026-08-02 — publish-activation-and-acm-simplification

**[!REALIZATION]** The operator's recent changes form a coherent onboarding simplification: expose one skill roster classified by activation, require only two routine actions, and name the persistent architecture once as ACM. The implementation history remains visible in the trail, while the newcomer surface presents the converged model rather than the sequence that produced it.

## 2026-08-02 — destination-coequal-research-and-unassisted-use

**[!REALIZATION]** The operator is not simplifying the suite to turn research into marketing. Adoption and research remain equal, and explanation quality is diagnostic rather than evidentiary. The sharper adoption claim is behavioral: can someone use the system successfully without the author, even before they can articulate its full theory?

## 2026-08-02 — orient-against-coequal-research-and-adoption

**[!REALIZATION]** The current plateau is not "the suite is now simple enough." It is "the suite now has a testable adoption bar and a separately bounded research bar." The next meaningful evidence must come from behavior against those bars, not from further confidence in the explanatory model itself.

## 2026-08-02 — orient-against-coequal-research-and-adoption

**[!REVERSAL]** The initial Destination hunch treated newcomer understanding and successful use as one combined destination and risked elevating adoption above research. Operator responses separated the claims: research remains co-equal, successful use is enough for adoption, and easier explanation is useful signal rather than research evidence.

## 2026-08-02 — destination-restore-reasoning-growth-and-token-viability

**[!REALIZATION]** Token efficiency and reasoning capability are not competing destination tracks. Efficiency is a viability constraint on every track: reduce resource use without reducing the capabilities that make delegation trustworthy. The target is better capability per unit of resource, not minimal tokens in isolation.

## 2026-08-02 — destination-restore-reasoning-growth-and-token-viability

**[!REVERSAL]** The preceding Destination/Orient pair over-corrected toward external behavioral evidence. External behavior remains necessary for adoption and research validation, but it is not the full immediate research program. The suite must also keep improving the reasoning system that generates that behavior, while making the system affordable enough to sustain.

## 2026-08-02 — orient-restore-reasoning-growth-and-token-viability

**[!REALIZATION]** The suite's viability equation has three inseparable terms: capability, trust, and cost. Optimizing any one by silently degrading another does not advance the destination. The useful unit is demonstrated capability and trust per resource spent, not raw feature count, explanation simplicity, or token reduction alone.

## 2026-08-02 — orient-restore-reasoning-growth-and-token-viability

**[!REVERSAL]** Run 213's claim that the next meaningful evidence must come from behavior was too exclusive. Behavioral evidence remains required for adoption and external validation, while internal reasoning-capability discovery and capability-preserving efficiency work are also immediate research paths.

## 2026-08-02 — bounded-current-destination-with-full-read-fallback

**[!REALIZATION]** The latest reasoning omission and the destination's token cost had a shared cause: active intent and historical provenance were stored together without an auditable completeness boundary. Separating their read paths can improve both carry-forward reliability and resource use, but only after reconciliation earns the boundary.

## 2026-08-02 — reconcile-complete-current-destination

**[!REALIZATION]** The engine's self-improvement mandate does not require a special self-targeting capability list. It follows recursively from the same generic operation used on every target: reason about purpose and intent, discover what most limits them, and improve that limitation. Fixing named capabilities would turn today's examples into tomorrow's ceiling.

## 2026-08-02 — reconcile-complete-current-destination

**[!REVERSAL]** The historical "irreducible human gate" over every implementation choice is no longer active. The operator owns and confirms the Destination; within it, implementation choice may be delegated. Direction changes and declared consequential actions remain gated.

## 2026-08-02 — orient-recursive-purpose-and-principles-boundary

**[!REALIZATION]** The strongest current reasoning evidence is mixed in a specific way: the engine applied prior learning well enough to protect intent structurally, while still needing operator correction to avoid creating a new conceptual ceiling. Improving learning carry-forward alone does not establish equally strong intent generalization.

## 2026-08-02 — surface-governance-accretion-redesign

**[!REALIZATION]** The previously unnamed limitation is governance accretion: the architecture has no mechanism for safeguards to expire, consolidate, or move out of routine context after they are added. As a result, successful learning monotonically increases the instruction burden that future reasoning must carry. This is distinct from example-to-checklist collapse; it is learning that protects against past failures while progressively consuming the attention needed to discover new ones.

## 2026-08-02 — orient-after-governance-accretion-finding

**[!REALIZATION]** The unseeded self-improvement test succeeded at discovery and exposed a new asymmetry: the suite has strong mechanisms for turning failures into permanent instructions, but weak mechanisms for turning accumulated instructions back into smaller abstractions without losing their protections.

## 2026-08-02 — prototype-layered-improve

**[!REALIZATION]** Conditional loading is architecturally feasible but composition is itself a load-bearing protocol: the kernel must expose trigger names, ownership, and mandatory routing even when protocol bodies move out. The experiment also reveals that governance accretion and evidence discipline are separable constraints; reducing the former does not automatically improve the latter.

## 2026-08-02 — prototype-layered-improve

**[!REVERSAL]** The initial kernel assumed "Apply Intent/Trail" and a link to conditional protocols were sufficient composition instructions. The first isolated evaluator treated siblings as manual and skipped conditional loading. Repaired the kernel by making automatic composition explicit and exposing the trigger index.

## 2026-08-02 — prototype-layered-improve

**[!REVERSAL]** The second evaluator identified Standalone Fallback but still declined to read it, invented mechanisms, and inferred Orientation staleness from absent context. Repaired the kernel by requiring matching-section loading, separating facts/inferences/proposals, and stating that missing Orientation evidence does not prove staleness.

## 2026-08-02 — replicate-layered-improve-grounding-test

**[!REALIZATION]** The replicated evidence separates operator control from evidence discipline. Both contracts reliably preserved the explicit consequential-action gate, while both failed to keep plausible causal stories and implementation details inside the boundary of known evidence. Adding more routine prohibitions is not yet justified; the next discriminating variable is execution context or independent classification, not contract length.

## 2026-08-02 — orient-after-replicated-layered-tests

**[!REALIZATION]** Compression can preserve visible structure and explicit authority gates without improving factual grounding. The next credible evidence must vary model/host context or evaluator independence; another kernel sentence would repeat governance accretion without isolating the cause.

## 2026-08-02 — orient-after-replicated-layered-tests

**[!REALIZATION]** Factual-grounding failures in natural-language instruction contracts are primarily execution-context effects. The same contracts that failed under one model version succeeded under another without modification. This bounds the value of adding more grounding instructions -- the return on additional prohibition text is limited by model capability, not instruction coverage.

## 2026-08-02 — orient-after-replicated-layered-tests

**[!REALIZATION]** The cross-model replication converted the layered-Improve arc from compression feasible but behaviorally unproven to compression feasible and not behaviorally worse, with grounding variation tracking model context. The productive next tests are routing (undertested), cross-vendor (untested), and adoption (unexercised).

## 2026-08-02 — orient-after-replicated-layered-tests

**[!REALIZATION]** Compression is not uniformly good or bad. In this run it coincided with BETTER factual grounding and WORSE across-run reflection depth. The prior finding that the layered arm was never worse on any dimension NO LONGER HOLDS. The likely mechanism is phrasing strength, not byte count: production mandates an explicit four-trigger evaluation with per-trigger evidence and got a double-loop reframe; the kernel asks more softly and got a one-sentence decline to escalate.

## 2026-08-02 — orient-after-replicated-layered-tests

**[!REALIZATION]** A contract repair generalized beyond the surface it was written for. The kernel sentence "missing Orientation context is not evidence that it is stale" was added as the iteration-2 repair during Case 1 and written about Orientation. A routing evaluator applied it correctly and unprompted to a DESTINATION gap. Repairs to this contract can transfer across surfaces rather than staying local to the case that produced them.

---

**60 markers — 51 realisations, 9 reversals**
