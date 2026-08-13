# orientation.md - notification-policy-fixture

Last updated: 2026-07-02 (run: `orient-focus-first-policy`)

## Current claims

The target is a focus-first personal notification policy. Its main risk is interrupting individual users too often, so the next changes should continue reducing notification frequency while preserving identical email and mobile behavior.

## What the next runs should test

1. Check whether digest timing remains identical across delivery channels.
2. Look for repeated timing values that could drift independently.

## Active operational rules

- Preserve externally visible schedules unless focused tests support a change.
- Keep email and mobile defaults aligned.
