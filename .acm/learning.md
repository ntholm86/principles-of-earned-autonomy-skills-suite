# Learning

Auto-generated from `.acm/audit-trail.md` by the `record.py learning --write` command in the autonomous-agent-skills install.
Do not edit by hand — re-run the command to refresh.

Compact chronological extract of the most recent `[!REALIZATION]` and `[!REVERSAL]` markers. The learning surface — what the loop has actually concluded across runs. Read this before reading `audit-trail.md` in full; reach for `audit-trail.md` only when an item here needs its surrounding context.

Showing the most recent 60 markers. 168 older marker(s) are in `.acm/learning-archive.md` — check there if the recent window doesn't cover what you're looking for.

## 2026-08-01 — orient-post-genericity-reversal

**[!REALIZATION]** The operator-gate caught what the loop's own process did not, immediately, in the same session -- a new form of gate-effectiveness evidence distinct from prior "which next move to pick" evidence: this is the gate catching a bad implementation of an agreed destination-level concern.

## 2026-08-01 — orient-post-genericity-reversal

**[!REALIZATION]** Read as one document, this window is the clearest evidence this repo's trail has produced on the destination's own oldest named gap (Learning: "the most underdeveloped of the three"). A destination note asking the loop to derive that improving its own reasoning matters did not, by itself, make the loop apply its own already-recorded learning more carefully in the very next action -- if anything, the new framing appears to have competed with, rather than reinforced, the older and more mundane precedent. The operator-gate closed the gap this time. Whether it needs to every time, or whether a structural re-trigger point for learning.md is worth adding, is now the single most concrete open design question this repo's trail has surfaced.

## 2026-08-01 — trail-decision-precedent-check-requirement

**[!REALIZATION]** This entry is itself the first live test of the new requirement -- and it passed, because the precedent check was performed deliberately and stated explicitly before the Decision was finalized, not added afterward as decoration. That is a meaningfully different discipline than what happened in the withdrawn entry, where a directly relevant precedent existed in learning.md and was not re-checked before the contradicting edit was written. The difference this time was not a smarter mechanism -- it was choosing to grep learning.md for specific terms before deciding, the same action any future agent following this new marker definition would be asked to take.

## 2026-08-01 — learning-md-bounded-recent-window-plus-archive

**[!REALIZATION]** This is the first entry in this whole multi-turn arc that responds to destination note item 3 (token/resource efficiency) as its own dedicated concern, rather than as a side effect of an unrelated instruction (the earlier trail sessions-mandate removal was efficiency-motivated but operator-directed, not self-derived from the destination text). Unlike the reasoning-capability attempts, this one did not require touching a skill file's *behavioral* instructions at all -- it is a change to tooling (record.py) and a description update (trail/SKILL.md, improve/SKILL.md), with no risk of the genericity violation that tripped up the earlier attempt, because record.py and the .acm/ file structure are already generic (they apply identically to any target using these skills, not just this repo).

## 2026-08-01 — audit-learning-precedent-surfaces-position-quickstart-h1-gap-and-systemic-bom

**[!REALIZATION]** This is the first entry in this arc where the new precedent-check discipline (added two entries ago) directly produced a finding neither the operator nor I had already surfaced -- the POSITION.md/QUICKSTART.md coverage gap was sitting, fully documented, in an archived realization from months earlier, and would not have been found without deliberately going back to check learning-archive.md for this session's other changes rather than continuing to defer that audit a fourth time. This is a genuinely positive data point for whether the precedent-check requirement can do real work, distinct from the earlier failure where the same kind of check was skipped.

## 2026-08-01 — audit-learning-precedent-surfaces-position-quickstart-h1-gap-and-systemic-bom

**[!REALIZATION]** Reading this session as one arc: the recurring pattern named above (checks with silent scope gaps) has now appeared three times in one day, each time found by actually re-reading the file/list in question rather than trusting that a prior fix generalized further than it did. The PRINCIPLES.md fix from earlier today explicitly named "audit STALE_PATH_DOCS and ACM_SCOPE_TRAVERSAL_FILES for the same silent-exclusion pattern" as a candidate next move -- that audit still has not been done, and this entry's finding (POSITION.md/QUICKSTART.md missing from REQUIRED_FILES) is arguably the same class of gap that audit was meant to catch, just in a different list (REQUIRED_FILES itself, not the other two). The governing pattern is: whenever this repo adds a new live doc (POSITION.md, QUICKSTART.md were both added well after the original REQUIRED_FILES list was written), nothing currently prompts a check of whether it needs to join every file-scoping list verify.py maintains. Fixing three individual instances of this pattern is not the same as fixing the pattern -- a genuinely systemic answer would be enumerating all of verify.py's file-scoping lists in one place and checking each new live doc against the full set, not discovering each one independently when something happens to force a look.

## 2026-08-01 — confirm-bom-root-cause-and-fix-verifypy

**[!REALIZATION]** The append-safety test (BOM is only written at file-creation/full-overwrite time, never reintroduced by a later append to an already-BOM-less file) is the load-bearing fact for how this cleanup can proceed safely: it means `.acm/audit-trail.md`'s BOM, once eventually stripped, would not silently reappear from this session's own continued use of `Add-Content -Encoding UTF8` for future entries -- the risk is entirely in the one-time strip operation itself, not in ongoing use. This changes the shape of the remaining work: it is a one-time, per-file migration, not a recurring maintenance burden, provided future *new* files in this repo are created via a BOM-safe path (`create_file`, or PowerShell's `-Encoding utf8NoBOM` where available, or `[System.IO.File]::WriteAllText` with an explicit `UTF8Encoding(false)`) rather than plain `-Encoding utf8`/`UTF8` in Windows PowerShell 5.1.

## 2026-08-01 — confirm-bom-root-cause-and-fix-verifypy

**[!REALIZATION]** The recurring-finding-class trigger fired, but the macro-Hansei for this specific pattern was already performed in the immediately prior entry (governing-variable diagnosis: no single canonical file-scope list in verify.py -- REQUIRED_FILES, STALE_PATH_DOCS, and ACM_SCOPE_TRAVERSAL_FILES each independently go stale). This entry does not change that diagnosis; it is a direct continuation of acting on it (root-cause confirmation, then one more fix in the already-agreed "one at a time" sequence), not a new instance requiring a fresh governing-variable read. Repeating the full macro reflection verbatim here would be ceremony without new signal -- the honest record is that the check was made, the same governing variable still applies, and no revision to it is warranted from this entry's evidence.

## 2026-08-01 — close-create-file-bom-blind-spot-and-fix-installing-md

**[!REALIZATION]** With create_file confirmed BOM-safe and three files now successfully migrated with the identical byte-verified mechanism, the remaining risk in this cleanup is concentrated almost entirely in the two deliberately-deferred files (.acm/audit-trail.md, .acm/orientation.md) rather than spread across the whole remaining list. The plain-file fixes (SKILL.md files, record.py, session files) are now low-uncertainty, repetitive work with a proven-safe mechanism -- the interesting remaining decision is specifically how to handle the two high-risk files, not whether the mechanism generalizes to the rest.

## 2026-08-01 — close-create-file-bom-blind-spot-and-fix-installing-md

**[!REALIZATION]** Continuing to fire the recurring-finding-class trigger on every file-by-file BOM fix, while correct per the letter of the rule, is starting to produce repetitive trail entries whose macro-Hansei content is identical to the last one ("no new diagnosis, continuation of agreed plan"). This is itself worth naming as a pattern: the trigger was designed to catch *drift* across a recurring finding-class, but a deliberately-sequenced, already-diagnosed cleanup (like this BOM migration) will keep firing it every time with nothing new to say. That is not a flaw in this entry's evidence -- it is the honest, correct evaluation -- but it suggests the *next* time this trigger fires with "same diagnosis as last entry," the macro-Hansei content itself could be a single-sentence pointer to the entry where the diagnosis was actually made, rather than re-stating the reasoning. Not changing the format now (that would be a new mid-migration process change, and this entry is not the place for it); naming it as a candidate for the next dedicated verify.py/trail process discussion instead.

## 2026-08-01 — fix-recordpy-bom

**[!REALIZATION]** Four files into this migration (QUICKSTART.md, verify.py, INSTALLING.md, record.py), the pattern is now fully mechanical and has produced zero surprises since the QUICKSTART.md entry's original discovery -- the interesting content of this cleanup arc was front-loaded into the root-cause investigation two entries ago, not spread evenly across the remaining fixes. This matches the macro-Hansei observation from the immediately prior entry almost exactly: the remaining work is low-uncertainty repetition, and the only files where real uncertainty still exists are the two deliberately-deferred ones.

## 2026-08-01 — fix-recordpy-bom

**[!REALIZATION]** Per the process observation named in the immediately prior entry's macro-Hansei (that repeated firings of this trigger with "same diagnosis as last entry" could use a lighter-weight pointer format), this entry's macro-Hansei is intentionally kept to a single pointer rather than re-deriving the diagnosis: the governing-variable finding stands as stated in the `confirm-bom-root-cause-and-fix-verifypy` entry (no single canonical file-scope list in verify.py) and the process-format question stands as named in `close-create-file-bom-blind-spot-and-fix-installing-md`. Neither is re-argued here. This is the first entry to actually apply the lighter-weight-pointer idea rather than only naming it as a future candidate -- worth watching whether this format holds up over the remaining fixes or whether it turns out to lose information a fuller restatement would have preserved.

## 2026-08-01 — orient-post-bom-cleanup-and-efficiency-check

**[!REALIZATION]** "One change per run, no batching" has not yet been examined against the evidence this window produced about how uniform and low-risk byte-identical BOM fixes are -- a live tension between two destination-level concerns (rigor via no-batching, efficiency via destination note item 3) that four consecutive entries had the evidence for and did not name as a tension. This is the double-loop gap from the 2026-07-31 destination note showing up in a new, quieter place than the genericity violation.

## 2026-08-01 — orient-post-bom-cleanup-and-efficiency-check

**[!REALIZATION]** Claim 5 is itself the macro-Hansei output of this run, arrived at only by reading the six-entry arc as one document rather than entry-by-entry -- no single one of the four BOM-fix entries had enough surface area on its own to surface the no-batching/efficiency tension; it only became visible by comparing the sequence's cumulative ceremony cost against the destination's efficiency note as a whole. This is the kind of finding Orient exists to produce that Improve's step 6b, running inside a single iteration, structurally cannot.

## 2026-08-01 — route-batching-tension-to-operator-then-fix-three-skillmd-boms

**[!REALIZATION]** This entry is the first direct test of whether the operator-gate can function even when the operator is not present to answer in real time -- the "work autonomously and make good decisions" instruction is a delegated form of the gate, not an absence of it. The decision made here (a scoped middle path, not either extreme) is falsifiable: if the operator reviews this later and says "no, I wanted strict one-per-entry" or "no, you should have batched everything," that would be direct evidence about how well an autonomous best-guess under real delegation matches what a present operator would have chosen. This is more informative than any of the four prior BOM-fix entries, because it is the first one testing something the arc's own orient run identified as actually uncertain, rather than repeating an already-settled mechanism.

## 2026-08-01 — route-batching-tension-to-operator-then-fix-three-skillmd-boms

**[!REALIZATION]** Both the recurring-finding-class and operator-explicitly-asked triggers fired simultaneously for the first time this session. Read together, they mark a transition point in this sub-arc: the prior four entries were the loop executing an already-settled mechanism repeatedly; this entry is the loop's own accumulated pattern-recognition (via Orient) producing a genuine governing-variable question, escalating it correctly instead of quietly deciding alone, and then exercising real judgment when the operator delegated the decision back. Whether "grouped, per-file-verified" turns out to be the granularity the operator actually wants remains open until reviewed -- this is not a closed loop yet, only a well-reasoned, clearly-flagged one.

## 2026-08-01 — orient-step3b-argyris-double-loop-check

**[!REALIZATION]** This closes the loop on something this session's own arc had already produced evidence for without naming it as a gap: the most recent orient run (two entries ago) exhibited double-loop reasoning in its claim 5 without any instruction to do so, and an even earlier session (`orient-post-argyris-window`) had informally borrowed step 6b's exact question into an orient run twice. The gap was never "Orient can't do this" -- it demonstrably already had, twice, in different sessions -- the gap was that the capability lived in ad hoc borrowing rather than in Orient's own spec, meaning a fresh agent reading only orient/SKILL.md (not the trail) would have no reason to know to ask this question. Codifying it turns a pattern that depended on an agent happening to remember or rediscover it into one the spec itself teaches.

## 2026-08-01 — orient-step3b-argyris-double-loop-check

**[!REALIZATION]** The operator-explicitly-asked trigger firing here is a clean case, distinct from the deeper double-loop candidates named in recent entries: the operator did not just approve a self-directed hunch, they asked the diagnostic question themselves ("is this also implemented in Orient?") that this entry's own answer depended on. Read against this session's arc as a whole, this is the second time in a row (after the delegated no-batching decision) that the operator-gate has functioned in a form other than "pick from a ranked candidate list" -- first as delegated autonomy under an explicit standing instruction, now as a direct diagnostic question the agent had not itself surfaced as a gap until asked. Both are healthy variants of the gate, not degraded ones, and worth naming together: the gate is not a single mechanism but a family of interaction shapes, and this session has now exercised three of them (ranked-candidate selection, delegated autonomy, direct operator-initiated diagnosis).

## 2026-08-01 — resolve-sessions-fingerprint-blind-spot-and-fix-six-boms

**[!REALIZATION]** This closes the last open item blocking the BOM cleanup before the two deliberately-highest-risk files (.acm/orientation.md, .acm/audit-trail.md). All 10 lower-risk live files are now fixed (verify.py, QUICKSTART.md, INSTALLING.md, record.py, three SKILL.md files, six session files -- note: nine, not ten; the count from two entries ago said "five" session files when the actual figure, confirmed by direct listing this run, is six -- a small factual correction to the running count, worth naming rather than silently absorbing). The blind-spot investigation itself was fast and conclusive specifically because the question was answerable by reading code directly rather than reasoning abstractly about what "might" depend on file content -- consistent with this session's own recurring lesson (from the QUICKSTART.md/PRINCIPLES.md arc) that direct verification beats inference every time it's available.

## 2026-08-01 — resolve-sessions-fingerprint-blind-spot-and-fix-six-boms

**[!REALIZATION]** Per the lighter-weight-pointer precedent: no new governing-variable diagnosis is introduced by this entry: the pattern-family diagnosis stands as recorded in `confirm-bom-root-cause-and-fix-verifypy`, and the granularity precedent stands as recorded in the delegated-autonomy entry two runs ago. This entry is a clean application of both, plus one small self-correction (the six-vs-five count) surfaced honestly rather than absorbed.

## 2026-08-01 — fix-orientation-and-audit-trail-boms-closes-cleanup-arc

**[!REALIZATION]** This closes the entire systemic BOM cleanup arc that began four entries ago as an unplanned discovery inside a REQUIRED_FILES coverage fix. Twelve files total were fixed across this arc (verify.py, QUICKSTART.md, INSTALLING.md, record.py, three SKILL.md files, six session files, orientation.md, and now audit-trail.md), zero of which suffered any content loss or corruption beyond the intended 3-byte BOM removal, each independently verified. The arc's own governing-variable question (raised via the delegated no-batching-vs-efficiency decision) was itself resolved in practice, not just in principle: this final entry groups two files of genuinely different risk profiles under one entry, but gives each the level of individual scrutiny its risk actually warrants -- a quick standard check for orientation.md, a deliberately designed and reconfirmed check for audit-trail.md. That asymmetry within a single entry is arguably the correct resolution of the tension named two entries ago: grouping should track marginal information value, not treat every file identically regardless of risk.

## 2026-08-01 — fix-orientation-and-audit-trail-boms-closes-cleanup-arc

**[!REALIZATION]** Per the established lighter-weight-pointer convention: no new governing-variable diagnosis is introduced here. The pattern-family diagnosis stands as recorded in `confirm-bom-root-cause-and-fix-verifypy`; the grouping-vs-risk resolution is this entry's own contribution, noted above, and does not contradict the delegated decision two entries ago -- it is the natural completion of applying that decision with risk-appropriate rigor rather than a uniform template.

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

---

**60 markers — 57 realisations, 3 reversals**
