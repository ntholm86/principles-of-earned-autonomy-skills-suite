# orientation.md - autonomous-agent-skills

Last updated: 2026-08-02 (run: `orient-after-replication-n2`)

## Scope of this read

Re-orient after the n>1 replication of claim 2, which was the prior orientation's top-priority next move and its stated gate on any kernel wording change. Question: does the both-directions divergence survive replication, and what does the answer unlock?

**Freshness check (run evidence):**

- `python harness/tools/record.py history --write` -> 230 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 194 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed). Unlike the previous two Orient runs, this gate is **not** vacuous: the entry-recognition repair means the newest entry is confirmed present in the derived index, and the count incremented as expected.

**Source used:** `learning.md` plus the two most recent entries read directly. The derived surfaces are now trustworthy for the first time in three Orient runs.

## Current claims

### 1. The generic improvement operation passed its first unseeded discovery test

Run 218 derived governance accretion from purpose, current structure, historical growth, and disconfirming evidence without a named-capability seed. Three subsequent experiments acted on that finding. This remains positive evidence for self-directed discovery.

**Falsifiable by:** evidence that governance accretion was prescribed by the prompt or repeated fresh runs that cannot discover beyond named examples.

### 2. Layering costs reflection depth categorically and buys grounding only on average

The experimental kernel (101 lines, 6,892 bytes) versus production (204 lines, 25,058 bytes) preserves the seven reasoning moves statically.

**Status change: REPLICATED at n=2 per arm, and NARROWED.** The claim was tested against its own pre-registered falsifier with four fresh isolated evaluators and a blinded verbatim-case judge.

- **Reflection half: confirmed and strengthened.** Production took both top slots on reflection depth, layered both bottom slots. Clean arm separation, not variance.
- **Grounding half: narrowed from categorical to on-average.** Material unsupported claims came to layered 2, production 6, reproducing the n=1 ratio of 1:3. But the judge's holistic grounding rank *interleaved* the arms. Layering produced the single best-grounded output and the only output with zero material unsupported claims, without producing categorical separation.

**The deficit now has a nameable mechanism, not a diffuse one.** Two countable, judge-independent behaviours separated the arms perfectly, and both sit exactly where production carries an explicit imperative and the kernel carries soft prose:

- within-iteration `[!REVERSAL]` marked: production 2/2, layered 0/2
- retrospective across-run reflection performed: production 2/2, layered 1/2

This is the strongest available support for the standing hypothesis that the deficit is **phrasing strength, not byte count** -- and it means the deficit is plausibly recoverable for a small number of bytes of stronger obligation wording.

**Gate status: DISCHARGED.** The prior orientation blocked any kernel reflection-wording change pending this replication. That block is lifted. The change is authorised by evidence and deliberately not yet made, so that it is measured against this baseline rather than folded into the run that justified it.

**Falsifiable by:** strengthening the kernel's reflection obligations and finding the gap persists, which would relocate the cause from wording to something structural about conditional loading itself.

### 3. Operator gating and evidence discipline are separable -- and model-bound

The operator gate held across all evaluators in all three experiments (two model contexts, both arms). Factual grounding, by contrast, varied with the model: prior-model evaluators all failed grounding; Claude Opus 4.6 evaluators showed substantially improved discipline without contract changes.

**Refined from prior:** the original claim was that gating is robust while grounding fails. The refinement is that grounding failure is primarily execution-context-bound. The same instructions produce different grounding behavior under different models. The routing experiment reproduced this: severe invention failures (fabricated systems, metrics, numeric targets) did not recur in either arm; the residual errors were a milder class of arithmetic over-reach on supplied numbers.

**Falsifiable by:** a model context where the operator gate fails, or a contract change that independently and repeatedly improves grounding within the same model context.

### 4. Instruction weight does not buy grounding, but mandate strength does buy reflection depth

Improve grew from 99 to 204 lines through locally justified safeguards. The layered prototype demonstrates that compression and conditional loading are architecturally feasible. Grounding tracked model capability, not instruction weight -- the same anti-invention language that failed under one model succeeded under another, and the *lighter* contract produced *better* grounding in the routing experiment.

**Sharpened from prior:** the prior claim was that the ceiling is model capability rather than instruction coverage, full stop. The routing experiment shows that is true for **grounding** but false for **across-run reflection**, where an explicitly mandated per-trigger evaluation produced observably deeper output than a softly-worded equivalent within the same model context. Instruction design still buys something; it just does not buy factual discipline.

**Implication:** adding more *prohibition* text has diminishing returns bounded by model capability. Adding or strengthening *obligation* text on specific reasoning moves may not.

**Strengthened by the n=2 replication.** The two behaviours that separated the arms perfectly were precisely the two that production states as imperatives and the kernel states as prose. Obligation wording bought an observable, countable act -- a marked reversal -- in 2/2 production runs and 0/2 layered runs, within one model context.

**Falsifiable by:** a wording change that independently improves grounding within a single model context, or a strengthened obligation that fails to produce the mandated act.

### 5. Destination input is structurally smaller; end-to-end token efficiency remains unproven

The complete current boundary reduced routine Destination input from 42,496 to 7,402 UTF-8 bytes. These are structural input reductions, not tokenizer-specific evidence or equivalent-task proof.

**Falsifiable by:** actual token measurements showing no reduction, or behavioral degradation attributable to compression.

### 6. Adoption and cross-vendor execution fidelity remain untested

No independent newcomer has completed an unassisted first cycle. The cross-model replication used Claude Opus 4.6 (same vendor, different version). True cross-vendor evidence (e.g., GPT-4, Gemini) has not been gathered.

**Status change from prior:** partially addressed. Execution fidelity is no longer "untested" -- it has been tested across one version boundary within the same vendor. Cross-vendor and newcomer adoption remain open.

**Falsifiable by:** a cross-vendor comparison or an observed newcomer cycle.

### 7. Conditional-protocol routing works under cleanly-separated triggers

**Status: ADDRESSED, now 4/4 cumulative.** Case 3 was purpose-built to fire exactly two of six triggers (Standalone Fallback, Precedent Conflict) against four distractors, with routing measured in an isolated phase *before* any protocol text was visible. Across two experiments, four independent evaluators each named exactly the two firing protocols, quoted the firing evidence, and rejected all four distractors with reasoning. All four refused the discriminating distractor (Destination Boundary Failure) on the correct ground that an *absent* surface is a different condition from an *invalid* completeness marker. Both fired protocols were executed correctly in every full iteration, including honest declaration of a conflict between the fallback's write requirement and the case's no-edit constraint -- 4/4 on that too.

**Secondary finding:** a contract repair generalized beyond its authoring surface. The kernel sentence "missing Orientation context is not evidence that it is stale" was written about Orientation during the Case 1 iteration-2 repair; an evaluator applied it correctly and unprompted to a **Destination** gap. Repairs to this contract can transfer across surfaces rather than staying local.

**Still untested:** routing under overlapping, ambiguous, or competing triggers. Case 3 supplied the easy condition -- two cleanly-separated triggers.

**Falsifiable by:** a routing failure under ambiguous or overlapping trigger conditions.

### 7b. The kernel's staleness repair is directionally incomplete

The sentence "missing Orientation context is not evidence that it is stale" blocks over-claiming in one direction only. In the replication, one layered evaluator converted the same absence into a *positive* conclusion -- "Orientation is not stale, so no refresh is owed" -- while the other handled it correctly and both production runs declared it undetermined or unevaluable.

The repair prevents asserting stale and permits asserting not-stale from identical evidence. This is a precision defect in the kernel's own wording, found incidentally by a run not looking for it, and it is independent of the reflection-depth question.

**Falsifiable by:** a symmetric rewording that still produces a positive not-stale conclusion from an absent surface.

### 8. The binding constraint on this arc is now harness fidelity, not instruction architecture

Three consecutive experiments were each distorted most by an evaluation-design flaw rather than a contract flaw: the production arm judged against a condensed contract (Cases 1-2); routing never exercised at all (Cases 1-2); and case evidence compressed when briefing the judge (Case 3), which **manufactured two violation findings that did not occur** -- flagging one arm for fabricating a policy phrase the policy contains verbatim, and the other for inventing timing the case states verbatim. Both were caught only by re-reading the case file after judging.

A fourth instance surfaced during this Orient's own freshness gate: `.acm/history.md` was missing the three most recent trail entries. `harness/tools/record.py` recognizes entries via `^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+)$`, but those three entries use a `## Entry: <slug>` heading and are silently skipped. The marker regex matches anywhere in the document, so `learning.md` indexed them correctly and the discrepancy stayed invisible.

**The defect was worse than a missing index.** A heading matching neither the canonical pattern nor the date-leading malformed pattern fell through to the body-accumulator, so its content was appended to the **previous** entry. The three orphaned entries' `[!DECISION]` and `[!REALIZATION]` markers were therefore filed under `orient-after-replicated-layered-tests` -- a different run from an earlier session. This is provenance corruption of the learning record, not merely an absent index. `verify.py` iterated the same parsed entries, so those entries were also exempt from every structural check while still printing `OK`. The "trail integrity checks pass" result recorded against the routing experiment was vacuous: that entry was never examined.

**Repaired 2026-08-02.** `record.py` now treats any level-2 heading as an unconditional entry boundary, salvaging date and slug best-effort, so drifted headings can never again absorb a neighbour's content. `verify.py` now fails on any level-2 heading that is not a canonical entry heading, with the four historical exceptions listed as explicit auditable exemptions. Entry count recovered from 224 to 228; the routing markers now resolve to `conditional-routing-experiment-case-3`. Verified by injecting a drifted heading and confirming a hard failure.

**Standing interpretation inverted:** a passing `verify.py` does not mean "the trail is sound." It means "the entries the parser recognized are sound." Silent scope reduction in a validator is more dangerous than an absent validator, because it manufactures confidence in proportion to how much it skips.

No history was rewritten. "Observable Autonomy" is a fixed boundary -- evidence the agent cannot retroactively rewrite -- so the reader was widened rather than the record corrected. The three drifted entries remain structurally unchecked and are grandfathered.

**Falsifiable by:** an experiment whose dominant error source is traced to contract wording rather than evaluation or tooling design.

**First contrary evidence, 2026-08-02.** The n=2 replication is the first run since this claim was raised whose harness *held*: isolation was genuine, the verbatim-case rule produced zero findings requiring annulment, the derived index incremented correctly, and the freshness gate was non-vacuous. The claim is not retired -- one clean run does not undo five -- but the repairs are landing, and instrument quality is no longer automatically the binding constraint.

**Double-loop note:** the arc has been treating the contracts as the object of study. For five entries the harness was. This may now be reverting.

### 9. Grounding, reflection depth, and decision quality are dissociable

The replication separated all three dimensions in a single run. The arm that ranked best on grounding ranked third on reflection depth and produced the decision the blinded judge assessed as best-supported in the set. The output with the worst grounding produced the second-deepest reflection. The judge, blind to arms, reached the same conclusion unprompted: "the output that was most careful about what it could claim was not the output that was most searching about its own reasoning, and vice versa."

**Implication for this arc's vocabulary:** any claim that one contract "reasons better" than another is under-specified until it names which of the three dimensions it means. Several earlier claims in this trail are weaker than they read because they did not make that distinction.

**Falsifiable by:** an evaluation where the three dimensions rank identically across a set of outputs large enough that coincidence is implausible.

## What the next runs should test

1. **Strengthen the kernel's reflection obligations** -- mandate `[!REVERSAL]` marking and per-trigger evidence in imperative form -- then re-run against the n=2 baseline. This is the change the whole comparison was built to justify, the gate is discharged, and the hypothesis is specific enough to be refuted cheaply. If it works, most of the 72.7% routine byte reduction survives with the reflection deficit closed.
2. **Repair the kernel's staleness sentence** so it blocks over-claiming in both directions (claim 7b). Independent of item 1 and cheaper.
3. **Test routing under overlapping or ambiguous triggers** -- the last untested condition for a mechanism now at 4/4 under separated ones.
4. **Structurally check the four grandfathered entries** by some means that does not rewrite them, since none has ever been verified.
5. **Make verifier output state its coverage** (entries examined versus exempted) so vacuous passes are visible rather than inferred after the fact.
6. **Test with a non-Anthropic model** (GPT-4, Gemini, or equivalent) to distinguish vendor-family effects from version effects. The current evidence still spans one vendor.
7. **Measure actual token use** for routine and triggered paths rather than relying on UTF-8 byte proxies.
8. **Observe an unassisted newcomer cycle.** The adoption bar remains unexercised despite multiple simplification iterations.
9. **Test on a public external target** in a fresh session to exercise automatic composition and continuity under realistic conditions.

## Active operational rules

- Derive candidate changes from target purpose and operator intent; never treat named capabilities or mechanisms as an exhaustive search space.
- Hold only the three principles fixed. Require every other mechanism to justify itself against purpose and evidence.
- Do not make a new safeguard permanently resident in routine instructions without considering consolidation, conditional loading, or an expiry condition.
- When the same failure persists across contract variants despite explicit instructions, vary execution context or evaluation method before adding more wording.
- Test operator gating and factual grounding independently; success on one does not imply success on the other.
- Let the engine choose implementation within a confirmed Destination; stop for direction changes and operator-declared consequential actions.
- Treat research and adoption as co-equal priorities.
- Optimize trustworthy capability per resource; require preservation checks before claiming efficiency.
- Use only the bounded current Destination for routine work when its ordered completeness markers are valid; widen to history for Destination changes, ambiguity, conflict, or provenance.
- Count adoption only from successful unassisted use and keep explanation, efficiency, adoption, and research evidence distinct.
- Preserve append-only history and regenerate derived evidence after every Trail append.
- Evaluate Orientation freshness before an Improve entry becomes durable; run scheduled Orient only after the triggering entry is durable.
- Grounding improvement should be pursued through model selection and evaluation design, not instruction expansion, until evidence shows otherwise.
- When briefing an independent judge, supply the case or evidence file **verbatim**. Never paraphrase material that will be used to score fabrication, because the paraphrase becomes the fabrication.
- Compare contract variants only at equal fidelity. A summarized contract measures the summary, not the contract.
- Measure a mechanism before showing the evaluator the artifacts that mechanism selects; inclusion is itself a signal.
- Treat `verify.py` passing as necessary, not sufficient. A validator that iterates parsed entries only certifies what it recognized; confirm the newest entry actually appears in the derived index before trusting a freshness gate.
- Append trail entries with an explicit UTF-8 writer; PowerShell `Add-Content` corrupts non-ASCII punctuation in this repo.
- Name which dimension a capability comparison refers to -- grounding, reflection depth, or decision quality. They dissociate, so an unqualified "reasons better" is not a claim.
- Write a claim's falsifier into `orientation.md` before running the experiment that tests it, and do not adjust it afterwards. The one claim in this arc treated that way is the only one that can be said to have survived a genuine attempt to kill it.
- Prefer countable, judge-independent measures over holistic rankings when a conclusion will unlock a contract change. Use the holistic read for interpretation, not for load-bearing evidence.
- Do not fold a change into the run that justified it. The baseline a change needs to be measured against is destroyed by making it in the same iteration.

## Loop-effectiveness notes

**Quality bars tested:** unseeded self-discovery; static and byte-proxy compression; conditional routing; purpose reasoning on two fixtures; explicit consequential-action gating; factual grounding under missing evidence; cross-model execution fidelity (one vendor, two versions); blinded independent classification; **replication at n=2 per arm against a pre-registered falsifier**.

**Result:** discovery PASS; resource reduction PASS by byte proxy; operator gate PASS (all contexts, 4/4 in the replication); grounding MIXED (model-dependent, and better under the lighter contract on count but not on holistic rank); routing PASS under separated triggers (4/4 cumulative), untested under ambiguous ones; reflection depth FAIL for the layered kernel, replicated with clean arm separation and traced to two specific unmandated behaviours.

**Bars not tested:** cross-vendor execution fidelity, actual token consumption, unassisted newcomer adoption, public external-target operation, convergence, routing under ambiguous triggers, and any dimension at n>2 per arm or with more than one judge.

**Double-loop finding (carried, still holds):** the arc resisted adding more instruction text after replicated failure, and cross-model evidence confirmed the resistance was correct for grounding. Refined by claim 4: that conclusion is specific to grounding and does not extend to reflection depth, where obligation wording buys an observable act.

**Double-loop finding (updated):** the governing assumption that the contracts are the object of study was suspended for five entries while the harness proved the weaker component. The replication is the first evidence that the repairs have landed. The assumption is provisionally restored, on the condition that every future experiment states what its instruments actually covered.

**Deutero-learning finding:** the research loop's design -- freeze contracts, vary contexts, use blinded judges, quote before accusing, compare only at equal fidelity -- has now produced a result strong enough to unlock a contract change that n=1 could not justify. Every rule in that list was born from a failure of the previous experiment. The method's value is not that it avoids mistakes but that each mistake becomes a standing constraint, and this run is the first where none of the accumulated constraints was violated.

[!REALIZATION] The arc has reached the point where its most comfortable claim was stated with a pre-registered refutation condition, tested at n>1, and survived in one half while being narrowed in the other. The frontier has moved again: from "is the measurement apparatus trustworthy?" to "can the deficit the apparatus found be closed without giving back the saving that motivated it?" That is the first question in this arc whose answer would change what gets shipped rather than what gets believed.
