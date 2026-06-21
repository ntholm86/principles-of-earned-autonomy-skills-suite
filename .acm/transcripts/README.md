# Transcript Artifacts

This directory stores verbatim transcript exports for high-fidelity runs.

- Use one file per run: `YYYY-MM-DD-<slug>.md`.
- Link each transcript from the corresponding audit entry using `transcript-file:`.
- Keep per-session summaries in `.acm/sessions/`.
- Do not replace summaries with transcript dumps; they serve different audit roles.

Required transcript metadata (inside each transcript file):

- `**Fidelity:** verbatim` or `**Fidelity:** verbatim-structural`
- source details for where the transcript was exported from
