# orientation.md - autonomous-agent-skills

Last updated: 2026-08-02 (run: `orient-after-cross-model-replication`)

## Scope of this read

Re-orient after three layered-Improve experiments spanning two model contexts (prior model + Claude Opus 4.6). Question: now that cross-model evidence exists, which claims still hold, which are refined, and what is the next discriminating test?

**Freshness check (run evidence):**

- `python harness/tools/record.py history --write` -> 223 entries.
- `python harness/tools/record.py learning --write` -> 60 recent + 187 archived markers.
- `python verify.py` -> OK, trail integrity checks pass.
- Gate: PASS (arc-claims allowed).

## Current claims

### 1. The generic improvement operation passed its first unseeded discovery test

Run 218 derived governance accretion from purpose, current structure, historical growth, and disconfirming evidence without a named-capability seed. Three subsequent experiments acted on that finding. This remains positive evidence for self-directed discovery.

**Falsifiable by:** evidence that governance accretion was prescribed by the prompt or repeated fresh runs that cannot discover beyond named examples.

### 2. Layering reduced routine instruction input without degrading behavior

The experimental kernel (101 lines, 6,892 bytes) versus production (204 lines, 25,058 bytes) preserves the seven reasoning moves statically. Across three experiments and two model contexts, the layered arm never performed worse than production on any measured dimension. Under Claude Opus 4.6, it showed marginally better fact/inference/proposal separation on Case 1.

**Status change from prior orientation:** upgraded from "not establishing behavioral improvement" to "not degrading behavior." The cross-model replication found no case where the layered contract was worse.

**Falsifiable by:** a fresh evaluation where the layered arm clearly degrades relative to production on grounding, gating, or routing.

### 3. Operator gating and evidence discipline are separable -- and model-bound

The operator gate held across all evaluators in all three experiments (two model contexts, both arms). Factual grounding, by contrast, varied with the model: prior-model evaluators all failed grounding; Claude Opus 4.6 evaluators showed substantially improved discipline without contract changes.

**Refined from prior:** the original claim was that gating is robust while grounding fails. The refinement is that grounding failure is primarily execution-context-bound. The same instructions produce different grounding behavior under different models.

**Falsifiable by:** a model context where the operator gate fails, or a contract change that independently and repeatedly improves grounding within the same model context.

### 4. Governance accretion remains real; its ceiling is model capability, not instruction coverage

Improve grew from 99 to 204 lines through locally justified safeguards. The layered prototype demonstrates that compression and conditional loading are architecturally feasible. The cross-model replication shows that the grounding failure tracked model capability, not instruction weight -- the same anti-invention language that failed under one model succeeded under another.

**Implication:** adding more prohibition text has diminishing returns bounded by model capability. The productive intervention for grounding is model selection or training, not instruction expansion.

**Falsifiable by:** a wording change that independently improves grounding within a single model context, or evidence that the Opus 4.6 improvement came from the contract difference rather than the model difference.

### 5. Destination input is structurally smaller; end-to-end token efficiency remains unproven

The complete current boundary reduced routine Destination input from 42,496 to 7,402 UTF-8 bytes. These are structural input reductions, not tokenizer-specific evidence or equivalent-task proof.

**Falsifiable by:** actual token measurements showing no reduction, or behavioral degradation attributable to compression.

### 6. Adoption and cross-vendor execution fidelity remain untested

No independent newcomer has completed an unassisted first cycle. The cross-model replication used Claude Opus 4.6 (same vendor, different version). True cross-vendor evidence (e.g., GPT-4, Gemini) has not been gathered.

**Status change from prior:** partially addressed. Execution fidelity is no longer "untested" -- it has been tested across one version boundary within the same vendor. Cross-vendor and newcomer adoption remain open.

**Falsifiable by:** a cross-vendor comparison or an observed newcomer cycle.

### 7. Conditional-protocol routing remains undertested

Neither novelty case in the cross-model replication triggered conditional protocols (no unavailable siblings, no convergence asks in the isolated evaluator context). The prior experiment showed one routing pass and one routing failure. This dimension needs a purpose-built test case.

**Falsifiable by:** a test case designed to force trigger evaluation, producing either reliable routing or a reproducible failure.

## What the next runs should test

1. **Design a routing-specific test case** that forces conditional-protocol trigger evaluation. This is the most undertested dimension across three experiments.
2. **Test with a non-Anthropic model** (GPT-4, Gemini, or equivalent) to distinguish vendor-family effects from version effects. The current evidence only spans one vendor.
3. **Observe an unassisted newcomer cycle.** The adoption bar remains unexercised despite multiple simplification iterations.
4. **Measure actual token use** for routine and triggered paths rather than relying on UTF-8 byte proxies.
5. **Test on a public external target** in a fresh session to exercise automatic composition and continuity under realistic conditions.

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

## Loop-effectiveness notes

**Quality bars tested:** unseeded self-discovery; static and byte-proxy compression; conditional routing (partial); purpose reasoning on two fixtures; explicit consequential-action gating; factual grounding under missing evidence; cross-model execution fidelity (one vendor, two versions); blinded independent classification.

**Result:** discovery PASS; resource reduction PASS by byte proxy; operator gate PASS (all contexts); grounding MIXED (model-dependent -- FAIL under prior model, substantially improved under Opus 4.6); routing MIXED (one pass, one fail, two untested); behavioral improvement from layering NOT DISPROVEN but not positively established.

**Bars not tested:** cross-vendor execution fidelity, actual token consumption, unassisted newcomer adoption, public external-target operation, convergence, and forced conditional-routing evaluation.

**Double-loop finding:** the arc successfully resisted adding more instruction text after replicated failure, then confirmed via cross-model evidence that the resistance was correct. The governing variable for grounding is model capability, not instruction coverage. This is the strongest double-loop result in the layered-improve arc.

**Deutero-learning finding:** the research loop's design -- freeze contracts, vary contexts, use blinded judges -- produced the discriminating evidence that editing contracts could not. This validates the methodology and suggests it should be applied to the remaining undertested dimensions (routing, adoption, token measurement).

[!REALIZATION] The cross-model replication converted the layered-Improve arc from "compression feasible but behaviorally unproven" to "compression feasible and not behaviorally worse, with grounding variation tracking model context." The productive next tests are routing (undertested), cross-vendor (untested), and adoption (unexercised).
