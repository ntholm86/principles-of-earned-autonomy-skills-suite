# orientation.md - autonomous-agent-skills

Last updated: 2026-08-02 (run: `orient-after-conditional-routing-experiment`)

## Scope of this read

Re-orient after the conditional-routing experiment (Case 3), which was the top-priority next test in the prior orientation. Question: routing was the last wholly-untested mechanism -- now that it has been exercised, which claims survive, and did the corrected methodology change any prior conclusion?

**Freshness check (run evidence):**

- `python harness/tools/record.py history --write` -> 223 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 190 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed), **with a caveat discovered during this gate** -- see claim 8.

**Source used:** the audit trail read directly, not `history.md`. The derived index is currently missing the three most recent entries (see claim 8), so the trail was used as the sole source of truth for this read. The trail itself is complete and decodes cleanly.

## Current claims

### 1. The generic improvement operation passed its first unseeded discovery test

Run 218 derived governance accretion from purpose, current structure, historical growth, and disconfirming evidence without a named-capability seed. Three subsequent experiments acted on that finding. This remains positive evidence for self-directed discovery.

**Falsifiable by:** evidence that governance accretion was prescribed by the prompt or repeated fresh runs that cannot discover beyond named examples.

### 2. Layering trades reflection depth for grounding discipline -- it is not uniformly neutral

The experimental kernel (101 lines, 6,892 bytes) versus production (204 lines, 25,058 bytes) preserves the seven reasoning moves statically. The routing experiment produced the first evaluation in which the arms diverged in **both** directions: the layered arm had fewer material unsupported claims (1 vs 3) and clearer fact/inference/proposal separation, but thinner across-run reflection and it selected the weaker of two safety-relevant mechanisms (proposed auto-restore-on-timeout, which reopens an unreviewed-visibility path; production forbade it on prior-learning grounds).

**Status change from prior orientation: CONTRADICTED and rewritten.** The prior claim was "reduced routine input without degrading behavior," resting on the layered arm never being worse on any dimension. That no longer holds. The factual boundary that changed: production had previously only ever been evaluated against a **condensed** contract, so its full behavior had never been observed. Supplying the verbatim 204-line contract revealed capability the condensed version had suppressed. This is a correction of the evidence base, not an override of a prior finding.

**Best current mechanism hypothesis:** the deficit is phrasing strength, not byte count. Production *mandates* an explicit four-trigger evaluation with per-trigger evidence and produced a double-loop reframe; the kernel asks more softly and produced a one-sentence decline to escalate. Untested.

**Falsifiable by:** a replication with n>1 per arm showing the reflection-depth gap is run-to-run variance, or a kernel phrasing change that closes the gap without restoring byte weight.

### 3. Operator gating and evidence discipline are separable -- and model-bound

The operator gate held across all evaluators in all three experiments (two model contexts, both arms). Factual grounding, by contrast, varied with the model: prior-model evaluators all failed grounding; Claude Opus 4.6 evaluators showed substantially improved discipline without contract changes.

**Refined from prior:** the original claim was that gating is robust while grounding fails. The refinement is that grounding failure is primarily execution-context-bound. The same instructions produce different grounding behavior under different models. The routing experiment reproduced this: severe invention failures (fabricated systems, metrics, numeric targets) did not recur in either arm; the residual errors were a milder class of arithmetic over-reach on supplied numbers.

**Falsifiable by:** a model context where the operator gate fails, or a contract change that independently and repeatedly improves grounding within the same model context.

### 4. Instruction weight does not buy grounding, but mandate strength does buy reflection depth

Improve grew from 99 to 204 lines through locally justified safeguards. The layered prototype demonstrates that compression and conditional loading are architecturally feasible. Grounding tracked model capability, not instruction weight -- the same anti-invention language that failed under one model succeeded under another, and the *lighter* contract produced *better* grounding in the routing experiment.

**Sharpened from prior:** the prior claim was that the ceiling is model capability rather than instruction coverage, full stop. The routing experiment shows that is true for **grounding** but false for **across-run reflection**, where an explicitly mandated per-trigger evaluation produced observably deeper output than a softly-worded equivalent within the same model context. Instruction design still buys something; it just does not buy factual discipline.

**Implication:** adding more *prohibition* text has diminishing returns bounded by model capability. Adding or strengthening *obligation* text on specific reasoning moves may not.

**Falsifiable by:** a wording change that independently improves grounding within a single model context, or a replication showing the reflection-depth difference does not survive n>1.

### 5. Destination input is structurally smaller; end-to-end token efficiency remains unproven

The complete current boundary reduced routine Destination input from 42,496 to 7,402 UTF-8 bytes. These are structural input reductions, not tokenizer-specific evidence or equivalent-task proof.

**Falsifiable by:** actual token measurements showing no reduction, or behavioral degradation attributable to compression.

### 6. Adoption and cross-vendor execution fidelity remain untested

No independent newcomer has completed an unassisted first cycle. The cross-model replication used Claude Opus 4.6 (same vendor, different version). True cross-vendor evidence (e.g., GPT-4, Gemini) has not been gathered.

**Status change from prior:** partially addressed. Execution fidelity is no longer "untested" -- it has been tested across one version boundary within the same vendor. Cross-vendor and newcomer adoption remain open.

**Falsifiable by:** a cross-vendor comparison or an observed newcomer cycle.

### 7. Conditional-protocol routing works under cleanly-separated triggers

**Status change from prior orientation: ADDRESSED.** Case 3 was purpose-built to fire exactly two of six triggers (Standalone Fallback, Precedent Conflict) against four distractors, with routing measured in an isolated phase *before* any protocol text was visible. Two independent evaluators each named exactly the two firing protocols, quoted the firing evidence, and rejected all four distractors with reasoning: 2/2 PASS, against a prior incidental record of one pass and one failure. Both fired protocols were then executed correctly in the full iteration, including honest declaration of a conflict between the fallback's write requirement and the case's no-edit constraint.

**Secondary finding:** a contract repair generalized beyond its authoring surface. The kernel sentence "missing Orientation context is not evidence that it is stale" was written about Orientation during the Case 1 iteration-2 repair; an evaluator applied it correctly and unprompted to a **Destination** gap. Repairs to this contract can transfer across surfaces rather than staying local.

**Still untested:** routing under overlapping, ambiguous, or competing triggers. Case 3 supplied the easy condition -- two cleanly-separated triggers.

**Falsifiable by:** a routing failure under ambiguous or overlapping trigger conditions.

### 8. The binding constraint on this arc is now harness fidelity, not instruction architecture

Three consecutive experiments were each distorted most by an evaluation-design flaw rather than a contract flaw: the production arm judged against a condensed contract (Cases 1-2); routing never exercised at all (Cases 1-2); and case evidence compressed when briefing the judge (Case 3), which **manufactured two violation findings that did not occur** -- flagging one arm for fabricating a policy phrase the policy contains verbatim, and the other for inventing timing the case states verbatim. Both were caught only by re-reading the case file after judging.

A fourth instance surfaced during this Orient's own freshness gate: `.acm/history.md` was missing the three most recent trail entries. `harness/tools/record.py` recognizes entries via `^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+)$`, but those three entries use a `## Entry: <slug>` heading and are silently skipped. The marker regex matches anywhere in the document, so `learning.md` indexed them correctly and the discrepancy stayed invisible.

**The defect is worse than a missing index.** `verify.py` iterates the same parsed entries, so unrecognized entries are exempt from *every* structural check it performs -- not merely absent from `history.md`. The "trail integrity checks pass" result recorded against the routing experiment was therefore vacuous: that entry was never examined. Writing this Orient's entry in the canonical format immediately surfaced a real structural violation in it (a fired trigger with no macro-Hansei subsection) that the preceding three entries would have concealed. The violation was fixed and verification now passes meaningfully.

**Standing interpretation inverted:** a passing `verify.py` does not mean "the trail is sound." It means "the entries the parser recognized are sound." Silent scope reduction in a validator is more dangerous than an absent validator, because it manufactures confidence in proportion to how much it skips.

The trail itself is intact; only recognition is broken. No history was rewritten, because "preserve append-only history" is a standing operational rule and the remedy is an operator decision. This Orient's entry uses the canonical format so the drift is not propagated further.

**Falsifiable by:** an experiment whose dominant error source is traced to contract wording rather than evaluation or tooling design.

**Double-loop note:** the arc has been treating the contracts as the object of study. Increasingly the harness is.

## What the next runs should test

1. **Repair the entry-recognition defect** (claim 8): decide between widening `record.py` to accept both heading forms and correcting the three non-canonical headings, then add a `verify.py` assertion that every `##`-level heading in the trail parses as an entry, so unrecognized entries fail loudly instead of being skipped. Then re-verify the three previously-unparsed entries, none of which has ever been structurally checked. This is the highest-priority item because it silently degrades both the memory layer and the validator that every subsequent run depends on.
2. **Replicate the both-directions divergence** (claim 2) with n>1 per arm and a verbatim-case judge, before treating the reflection-depth gap as a property rather than variance.
3. **Test routing under overlapping or ambiguous triggers** -- the condition Case 3 did not supply.
4. **Test with a non-Anthropic model** (GPT-4, Gemini, or equivalent) to distinguish vendor-family effects from version effects. The current evidence still spans one vendor.
5. **Observe an unassisted newcomer cycle.** The adoption bar remains unexercised despite multiple simplification iterations.
6. **Measure actual token use** for routine and triggered paths rather than relying on UTF-8 byte proxies.
7. **Test on a public external target** in a fresh session to exercise automatic composition and continuity under realistic conditions.

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

## Loop-effectiveness notes

**Quality bars tested:** unseeded self-discovery; static and byte-proxy compression; conditional routing (partial); purpose reasoning on two fixtures; explicit consequential-action gating; factual grounding under missing evidence; cross-model execution fidelity (one vendor, two versions); blinded independent classification.

**Result:** discovery PASS; resource reduction PASS by byte proxy; operator gate PASS (all contexts); grounding MIXED (model-dependent -- FAIL under prior model, substantially improved since, and *better under the lighter contract* in the routing experiment); routing PASS under separated triggers (2/2), untested under ambiguous ones; behavioral effect of layering now DIRECTIONAL RATHER THAN NEUTRAL -- better grounding, worse reflection depth.

**Bars not tested:** cross-vendor execution fidelity, actual token consumption, unassisted newcomer adoption, public external-target operation, convergence, routing under ambiguous triggers, and any dimension at n>1 per arm.

**Double-loop finding (carried, still holds):** the arc resisted adding more instruction text after replicated failure, and cross-model evidence confirmed the resistance was correct for grounding. Refined by claim 4: that conclusion is specific to grounding and does not extend to reflection depth.

**Double-loop finding (new):** the governing assumption of this arc has been that the contracts are the object of study. Four consecutive measurement distortions -- three in experiment design, one in the memory tooling -- indicate the harness is now the weaker component. Continuing to vary contracts while the harness silently drops entries and paraphrases evidence would produce confident findings about the wrong system.

**Deutero-learning finding:** the research loop's design -- freeze contracts, vary contexts, use blinded judges -- produced discriminating evidence that editing contracts could not, and in this run it also produced *self-correcting* evidence: the judge's two false findings were caught because the method requires checking claims against source. The methodology is working well enough to detect its own defects, which is the strongest available argument for keeping it and repairing the harness rather than loosening the method.

[!REALIZATION] The routing experiment closed the last wholly-untested mechanism and simultaneously overturned the arc's most comfortable claim. Layering is not free: it bought grounding discipline and cost reflection depth. The arc's frontier has moved from "is the compressed contract safe?" to "is the measurement apparatus trustworthy?"
