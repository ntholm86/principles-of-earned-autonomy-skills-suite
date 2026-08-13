# Unassisted Newcomer Observation Protocol

Status: preregistered 2026-08-13; awaiting an eligible consenting participant

## Question

Can a developer who did not co-author or previously use the suite encounter its public materials, decide whether it is relevant, install it, complete a useful first Improve run on a real target, and recognize enough of the resulting evidence to continue without author assistance or prior Destination setup?

This protocol tests human recognition and adoption. It does not retest model-route availability, prove workflow reliability, or treat conceptual fluency as a prerequisite for successful use.

## Authorization boundary

This document authorizes one observation only after it is committed and an eligible participant gives informed consent. It does not authorize impersonating a newcomer, recruiting or contacting anyone without operator action, recording without consent, exposing private work, or replacing an incomplete observation after its outcome is known.

The observation begins when the participant receives the frozen first-contact message. Eligibility, consent, environment, and capture choices are recorded before that message. Any technical assistance after first contact changes the observation from unassisted to assisted and must be timestamped; the session may continue for diagnosis, but it cannot be classified as an unassisted Pass.

## Participant eligibility

An eligible participant:

- is a developer who did not author or review this suite;
- has not previously installed or invoked it;
- has not read this experiment protocol or been coached on the expected workflow;
- has a development environment in which they ordinarily use VS Code and GitHub Copilot;
- chooses a public, disposable, or participant-owned target that may be observed without confidentiality or ownership violations;
- gives explicit consent for the agreed capture before first contact.

Record prior familiarity with AI coding tools and approximate development experience as participant-provided context, not as selection criteria or identifying biography. Use a study-local participant ID. Do not commit names, contact details, account identifiers, credentials, screen content outside the agreed target, or private repository material.

## Frozen first contact

Give the participant only the public repository URL and this message:

> Please evaluate whether this project is useful for improving a codebase you can safely modify. Work as you normally would. You may stop at any time. I will observe without technical guidance and ask about your experience afterward.

Do not mention Improve, the installer command, ACM, Intent, Trail, Destination, expected success criteria, prior experiment results, or where to click or read. The repository's own public materials are the product surface under observation.

The participant may use documentation, search, GitHub Copilot, terminals, and other tools as they normally would. Observer-supplied technical instructions are assistance. Answers limited to consent, privacy, safety, capture, or the right to stop are not technical assistance.

## Observation boundary

Before first contact, capture:

- study-local participant ID and signed or recorded consent state;
- date, operating system, VS Code and Copilot surfaces available, and whether required software was already present;
- target ownership/public status, baseline commit or snapshot, test command if known, and pre-existing ACM state;
- capture modes the participant accepted;
- observer identity and confirmation that no suite coaching occurred.

From first contact until the participant stops or reaches useful continuation, record timestamps for observable events without prompting them toward those events:

- first repository surface opened;
- first statement or action indicating recognition, confusion, rejection, or interest;
- documentation path followed;
- installation attempt and outcome;
- first autonomous invocation, including the participant's own prompt;
- automatic-service explanations shown to the participant;
- target change, verification, and resulting Trail evidence;
- participant inspection or use of that evidence;
- any fresh-session or different-model continuation attempt;
- every observer intervention and participant request for help;
- stop point and participant-stated reason.

Preserve exact commands and machine-generated outputs when consent permits. Distinguish direct observation, participant report, and evaluator inference in every note. Never reconstruct missing chronology from the final interview as if it were observed.

## Useful continuation

The first run is useful when all of these are evidenced:

- the participant chose to invoke Improve without observer instruction;
- the run produced a material change or a bounded Silence conclusion relevant to the participant's target;
- applicable verification passed or the run honestly exposed why it could not;
- Trail evidence was left in the target without requiring prior Destination setup;
- the participant judged the outcome worth keeping or acting on.

Continuation is demonstrated when, after the first run, the participant starts a fresh Copilot session or uses a different available model on the same target and asks it to continue in their own words. The later agent must locate and use the durable evidence coherently without the observer describing ACM or naming files. Continuation may be observed in the same sitting, but it is a distinct stage from first-run completion.

## Post-observation interview

After the participant stops, ask these questions in order without teaching the framework first:

1. What did you think this project was for when you first encountered it?
2. What made you continue, hesitate, or stop?
3. What did you expect Improve to do before you ran it?
4. What evidence did the run leave, and what would you use it for?
5. Did any automatic handoff or explanation feel useful, confusing, or ceremonial?
6. Would you use this again on your own work? Why or why not?
7. What was the first point where help would have changed your outcome?

Record answers as participant report. Do not score vocabulary or correct misunderstandings until capture is complete.

## Staged classification

Classify the earliest terminal stage reached:

- **Pass - useful continuation:** all useful-first-run conditions hold and a fresh session or different model uses the durable evidence coherently without observer guidance.
- **Partial - useful first run:** all useful-first-run conditions hold, but continuation was declined, not attempted, or not completed.
- **Fail - recognition:** the participant does not identify a reason to try the suite from the public materials.
- **Fail - installation:** the participant chooses to try it but cannot install it from the public instructions without technical help.
- **Fail - invocation:** installation succeeds but the participant cannot identify or complete a first Improve invocation without technical help.
- **Fail - outcome:** Improve runs, but the result is not useful, verified, trustworthy, or worth keeping to the participant.
- **Fail - evidence or continuation:** the first run is useful, but its evidence is absent, misleading, or insufficient for coherent continuation.
- **Inconclusive:** consent or capture failure, unrelated host outage, unsafe target state, or another external condition prevents classification.

A participant's voluntary refusal is evidence, not Inconclusive, when the public materials or perceived relevance caused the refusal. An observer intervention never becomes invisible: classify the unassisted stage immediately before it, then report any assisted diagnostic outcome separately.

## Evidence package

Before interpretation, preserve an access-controlled raw package outside the public repository when it contains personal or private data. Commit only consent-compatible, de-identified evidence:

- eligibility and environment record;
- frozen first-contact message and its timestamp;
- chronological event log with source labels;
- intervention log, including an explicit none if no intervention occurred;
- documentation path and exact commands;
- consent-compatible terminal or Copilot transcript;
- baseline and post-run target state, verification output, and ACM files when the target is publishable;
- post-observation answers;
- staged classification and earliest failure point;
- a SHA-256 and byte-size manifest.

Publish redactions as redactions, not as absent events. State what raw evidence exists, who can access it, and which claims depend on participant report rather than direct capture.

## Claim boundary and next decision

One Pass establishes one observed newcomer journey, not adoption rate, population reliability, cross-platform behavior, or causal proof that any specific explanation produced success. One failure identifies the earliest observed boundary for a later Improve iteration; it does not justify rewriting multiple onboarding surfaces at once.

Publish the result and limitations before changing production skills or documentation. Any proposed change must target the earliest evidenced failure and preserve the already-established simulated workflow behavior. A deliberate reduction in reasoning, memory, learning, or evidence capability remains operator-gated.
