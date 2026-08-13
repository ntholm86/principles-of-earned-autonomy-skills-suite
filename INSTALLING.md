# Installing the skills

## One-line install (recommended)

From a clone of this repo:

```
bash install.sh                                                       # macOS / Linux  → installs to ~/.copilot/skills
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1     # Windows        → installs to $HOME\.copilot\skills
```

The default install copies the five operational skills plus PRINCIPLES.md. Probe is omitted so normal users see only the operational command surface.

To install into a project instead of user-global:

```
bash install.sh ./my-repo/.copilot/skills
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Target .\my-repo\.copilot\skills
```

To include Probe for controlled ARF research:

```
bash install.sh --research
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Research

# Project-local research install
bash install.sh ./my-repo/.copilot/skills --research
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Target .\my-repo\.copilot\skills -Research
```

Nothing else is installed and nothing is executed at runtime.

### Optional: enforce trail discipline with a git hook

The one-line installer does not copy optional tooling. From the target repo where you'll be running the skills, invoke the hook installer by its path in your cloned skills suite:

```
bash /path/to/autonomous-agent-skills/harness/tools/install-hooks.sh
powershell -NoProfile -ExecutionPolicy Bypass -File C:\path\to\autonomous-agent-skills\harness\tools\install-hooks.ps1
```

This installs a pre-commit hook that rejects commits which touch substantive files without a corresponding `.acm/audit-trail.md` entry. Override with `git commit --no-verify` — the override itself is auditable.

---

## How VS Code Copilot discovers skills

Copilot looks for skills at exactly **one level deep** under `.copilot/skills/`:

```
.copilot/
  skills/
    intent/
      SKILL.md     ← found
    improve/
      SKILL.md     ← found
    some-folder/
      subfolder/
        SKILL.md   ← NOT found (too deep)
```

**This means: do not drop the entire repo folder into your skills directory.** That adds an extra nesting level and Copilot finds nothing. Copy the individual skill folders directly.

---

## Operational install (recommended)

The normal operating model uses five installed skills but only one deliberate operator action: **Run Improve**. Intent and Trail are automatic services; Destination and Orient activate when Improve detects that accumulated evidence needs durable direction or a refreshed map.

```
your-repo/
  .copilot/
    skills/
      destination/
        SKILL.md
      orient/
        SKILL.md
      improve/
        SKILL.md
      intent/
        SKILL.md
      trail/
        SKILL.md
```

Invoke `/improve`. Do not add routine `/intent`, `/destination`, `/trail`, or `/orient` steps; manual `/destination` and `/orient` remain available as overrides.

---

## Research install (adds Probe)

```
your-repo/
  .copilot/
    skills/
      intent/
        SKILL.md
      destination/
        SKILL.md
      improve/
        SKILL.md
      trail/
        SKILL.md
      orient/
        SKILL.md
      probe/
        SKILL.md
```

This is what the installer copies only when research mode is enabled. The skills are plain markdown files — no scripts, no dependencies, nothing to execute at runtime.

Optionally copy `PRINCIPLES.md` next to the skill folders — the skills reference it but work fully without it (the principles are inlined in each SKILL.md).

### Probe is optional scientific instrumentation

`probe/SKILL.md` measures [Autonomous Reasoning Fidelity](https://github.com/ntholm86/autonomous-agent-principles/blob/v1.0.0/PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition). It exists so controlled ARF experiments can be reproduced. Destination, Orient, Improve, Intent, and Trail neither require nor invoke it. Install it with `--research` or `-Research` only when conducting that research; the default installer leaves it out.

---

## What each skill needs at runtime

All skills work with only their own `SKILL.md`. No required sibling files.

| Skill | Optional sibling files |
|---|---|
| **intent** | `PRINCIPLES.md` (cross-reference link; content is inlined) |
| **destination** | `PRINCIPLES.md` |
| **improve** | `PRINCIPLES.md` |
| **trail** | nothing — creates `.acm/audit-trail.md` on first use |
| **orient** | nothing — reads `.acm/audit-trail.md` written by trail |

---

## The trail — where it lives

The trail is **per project**. The AI writes it automatically — no scripts required.

When the trail skill runs for the first time on a project it creates:
`<repo-root>/.acm/audit-trail.md` (the append-only evidence log)

Commit `.acm/audit-trail.md` after each session. That's the full workflow.

---

## For maintainers: experiment tooling

*This section is for people running the improvement loop on the skills repo itself. If you're adopting the skills for your own project, you don't need any of this.*

`harness/tools/record.py` and `verify.py` exist to support the experiment that produced this suite — running the loop 280+ times and proving the trail is intact. They remain in the cloned repository and are not copied by the one-line installer.

**`harness/tools/record.py`** — generates a human-readable `history.md` from the trail log. Run from the repo root:
```
python harness/tools/record.py history --write    # writes .acm/history.md
python harness/tools/record.py summary            # prints the latest entry
```
It only writes into `.acm/`. No network calls.

**`verify.py`** — read-only integrity check. Confirms the trail is well-formed, dates are in order, required files exist, and referenced session files are present. Writes nothing.
```
python verify.py
```
Exit 0 = all checks pass, exit 1 = something is wrong.

---

## Using a skill

Once installed, remember one action:

- **Run** (`/improve`) — interpret this prompt, advance the work, and coordinate the suite.

Intent runs automatically before substantive work. Trail runs automatically afterward. Improve triggers Destination when broader direction needs operator confirmation and Orient when the evidence-based freshness check fires. Manual `/destination` and `/orient` remain available as overrides, but are not routine workflow steps. Probe is outside this operating model; `/probe` is only for controlled ARF research.

Example:
```
/improve review the checkout module for waste and overburden
```

---

## Updating

Skills are just markdown files. Replace the SKILL.md files with newer versions to update. The trail log is separate from the skills and does not change when you update.
