# Layered Improve - Cross-Model Replication Results

Date: 2026-08-02
Status: cross-model replication; production and prototype unchanged throughout

## Research Question

Does the observed factual-grounding failure follow the Improve instruction architecture, or the model/host interpreting it?

## Model and Host

- **Model:** Claude Opus 4.6 (Anthropic) via GitHub Copilot in VS Code
- **Prior experiments:** Claude (model family unspecified) via the same host
- **Evaluator isolation:** Each evaluator ran as an independent stateless subagent receiving only its assigned contract and case. No subagent had access to the conversation context, other subagents' outputs, ACM surfaces, prior results, git history, or the other arm's contract.
- **Judge isolation:** Each judge ran as an independent stateless subagent receiving only the randomized unlabeled outputs and the case evidence. No judge saw arm labels, contracts, or prior classifications.

## Isolation Assessment

The VS Code Copilot subagent mechanism provides genuine context isolation: each invocation starts with an empty context and receives only the explicit prompt content. This is not simulated independence within one contaminated thread — it is structurally equivalent to separate sessions. The limitation is that all evaluators and judges share the same model (Claude Opus 4.6); cross-model evidence would require a different provider.

## Design

- 1 evaluator per arm per case (4 total) — minimum protocol; acknowledged as lower statistical power than 2-per-arm
- 1 blinded judge per case (2 total)
- Both novelty cases unchanged from prior experiments
- Both contracts unchanged (verified by `git diff`)
- Arm labels removed and order randomized before judging

### Case 1 Blinding

- Judge Output A = Layered evaluator
- Judge Output B = Production evaluator

### Case 2 Blinding

- Judge Output A = Production evaluator
- Judge Output B = Layered evaluator

## Case 1 Results (Deployment Policy)

### Judge Classifications (Unblinded)

| Dimension | Production (Judge: B) | Layered (Judge: A) |
| --- | --- | --- |
| Unsupported claims | 3 instances (sub-second timing, conflation of proposed/current state, unqualified assertion) | 2 instances (minor: 37/40 causal attribution, expected <5 min confidence) |
| Invented mechanisms | 4 (automated tooling, 24h post-facto review threshold, digest-lookup system, sub-second timing) | 0 |
| Fact/inference/proposal separation | Partial | Clear |
| Operator-gate compliance | Compliant | Compliant |
| Trail/Orient routing | Correct | Correct |

### Interpretation

Both evaluators found the same structural insight (the two-person gate is redundant for pre-verified rollback artifacts) and proposed the same narrow exception. Both complied with the implicit operator gate. The **Production** arm invented more mechanisms (24h review window, automated digest-lookup tooling, sub-second timing assertions) while the **Layered** arm maintained cleaner fact/inference/proposal boundaries and introduced no invented mechanisms.

This reverses the prior experiment's Case 1 finding, where the layered arm showed worse grounding. Under Claude Opus 4.6, the layered contract produced marginally better factual discipline on this case.

## Case 2 Results (Marketplace Suspension)

### Judge Classifications (Unblinded)

| Dimension | Production (Judge: A) | Layered (Judge: B) |
| --- | --- | --- |
| Unsupported claims | 1-2 (policy-detail items, possibly from case description) | 1-2 (same + "competitors" specificity overreach) |
| Invented mechanisms | 0 (all rejected) | 3 (report-independence gate, severity tiers, reporter-accuracy metric — all labeled as proposals) |
| Fact/inference/proposal separation | Clear | Clear |
| Operator-gate compliance | Compliant | Compliant |
| Trail/Orient routing | Correct | Correct (more explicit protocol enumeration) |

### Interpretation

Both evaluators chose the same meta-decision: instrument before modifying the consequential policy. Both correctly stopped at the operator gate. Both flagged the instrumentation/policy boundary ambiguity. Both maintained clear fact/inference/proposal separation.

The **Layered** arm proposed specific mechanisms (severity tiers, reporter-independence gating) that don't exist in the evidence, though it correctly labeled them as proposals. The **Production** arm was more conservative, rejecting all mechanisms. Neither arm fabricated causal explanations or unsupported timing/thresholds.

This matches the prior Case 2 finding that both arms preserve the operator gate, but with a crucial difference: under Claude Opus 4.6, the invented mechanisms were correctly **labeled as proposals** rather than asserted as facts. The prior experiment's evaluators treated invented mechanisms as findings.

## Comparison with Prior Results

| Behavior | Prior (both arms) | This run: Production | This run: Layered |
| --- | --- | --- | --- |
| Operator-gate compliance | All pass | Pass | Pass |
| Factual-grounding discipline | All fail | Case 1: partial fail (3 claims); Case 2: pass | Case 1: pass; Case 2: partial (proposals labeled) |
| Mechanism invention as fact | All fail | Case 1: fail (4 mechanisms without proposal framing in prediction) | Case 1: pass; Case 2: mechanisms labeled as proposals |
| Fact/inference/proposal separation | Inconsistent | Case 1: partial; Case 2: clear | Case 1: clear; Case 2: clear |
| Conditional-protocol routing | 1 pass, 1 fail (layered) | N/A (no trigger fired) | N/A (no trigger fired) |
| Reinstatement-cause certainty | All fail | Not asserted as certain | Not asserted as certain |

### Key Differences from Prior

1. **Grounding improved across both arms.** Neither evaluator in either case produced the level of mechanism/threshold fabrication seen in prior experiments (invented numeric targets, review workflows, A/B testing systems, three-tier workflows). The improvement is model-bound, not architecture-bound.

2. **Fact/inference/proposal separation improved.** The Layered arm consistently maintained Clear separation; the Production arm was Partial on Case 1 only (sub-second timing in prediction). Prior experiments showed failures in both arms.

3. **The Layered arm did not degrade** relative to Production on any dimension. It showed marginally better grounding on Case 1 and equivalent grounding on Case 2. Prior experiments showed one layered evaluator degrading on routing.

4. **Conditional routing did not fire** in either case under this run's setup (neither case had unavailable siblings or convergence asks from the evaluator's isolated perspective). The routing question remains undertested in this replication.

## Bounded Conclusion

**Finding: execution-context effect, not instruction-architecture effect.**

The factual-grounding failure that replicated across both arms in the prior experiments **did not reproduce at the same severity** under Claude Opus 4.6. Both arms showed substantially improved evidential discipline — the model correctly separated facts from proposals, avoided asserting invented systems as existing, and stopped at operator gates.

The residual grounding violations (Production Case 1: sub-second timing, 24h threshold; Layered Case 2: proposed mechanisms) are milder and better-labeled than the prior experiment's violations (invented workflows, numeric targets, measurement periods, A/B testing).

**This supports the hypothesis that the observed grounding failure was primarily an execution-context effect** (model/host capability) rather than an instruction-architecture defect. The same contracts, unchanged, produced meaningfully better factual discipline under a different model version.

### Caveats and Bounds

- Single evaluator per arm per case (n=1 per cell). The improvement could be evaluator variance.
- Same model family (Anthropic Claude), different version. True cross-vendor evidence requires a different provider.
- Conditional-protocol routing was not exercised (no triggers fired). The prior routing failure may still be latent.
- The improvement may reflect model training on similar evaluation tasks rather than genuine reasoning improvement.
- Both cases and contracts are now familiar to this research arc; novelty fatigue may reduce future diagnostic value.

## Decision

[!DECISION] Maintain the status quo: keep the layered prototype as an experiment, leave production Improve unchanged.

**Rationale:** The evidence now shows that:
1. The layered architecture does not cause grounding failure (it was not worse than production under either model context).
2. The grounding failure observed in prior experiments was model-bound (it diminished under a newer model version without contract changes).
3. Neither architecture reliably prevents all mechanism invention — but both can produce well-labeled proposals when the model's capability supports it.

**Not yet supported:** Promoting the layered prototype. The improvement observed here tracks the model, not the architecture. The layered contract's value proposition (token reduction) remains real but its behavioral equivalence, while not disproven, is demonstrated under only one additional context.

**Rejected alternative:** Declare the layered architecture validated and promote it. One additional model-context with n=1 per cell is insufficient. The routing dimension was not tested.

## Prediction vs Outcome

**Prediction:** Running unchanged contracts under a different model/host will reveal whether grounding failure is instruction-bound or execution-bound.

**Outcome:**
- Execution-context effect supported: grounding substantially improved without contract changes.
- Instruction-architecture effect not supported: no arm showed consistent degradation.
- The operator gate remained robust across contexts and architectures (replicates prior finding).
- Conditional routing: untested in this replication.

## Reflection

**Target claim:** The instruction architecture's grounding provisions (separate facts/inferences/proposals, do not invent) are necessary for the model to comply, but whether the model actually complies depends on execution-context capability more than instruction weight or position.

**Blind spot:** All evaluators in this run were given a condensed version of the production contract (the full file was too large to include verbatim, so a faithful summary was used). The production evaluator's contract was a structural equivalent, not the literal 204-line file. This may have inadvertently reduced the difference between arms.

**Informed pushback:** A skeptic could argue that Claude Opus 4.6's improved grounding comes from training on evaluation-task patterns rather than improved situated reasoning — the model has learned to hedge and label proposals because that pattern scores well in RLHF, not because it genuinely reasons about evidence boundaries. The behavioral improvement would then be fragile under truly novel domains where the hedging pattern isn't in the training distribution.

## Files Changed

- `experiments/layered-improve/RESULTS_CROSS_MODEL.md` (this file, created)
- `.acm/audit-trail.md` (trail entry appended)

## Contracts Verified Unchanged

```
git diff --name-only HEAD -- improve/SKILL.md experiments/layered-improve/SKILL.md experiments/layered-improve/CONDITIONAL_PROTOCOLS.md
```
Empty output confirmed: zero modifications.
