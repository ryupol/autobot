---
name: update-readme-on-change
description: Keep README.md in sync whenever user-facing code in this project changes. Use after any edit to gamebots/ or other source files that affects behavior, setup, config, or usage. Does not apply to tests/.
---

README.md is a user guide, not test docs. Code changes under `gamebots/` (or any user-facing source) that affect behavior, setup, config, or usage require a README.md update in the same task, before finishing.

`tests/` changes are exempt — README is not about test coverage or test internals.

Steps:

1. After making code changes, diff what changed (`git diff` / `git status`).
2. Skip if changes are only under `tests/`.
3. Check if README.md documents the affected area (setup instructions, usage, file/module list, config options, features).
4. Update README.md to match: add new sections for new features, fix stale instructions, remove docs for deleted code.
5. If change is purely internal (refactor, no behavior/interface/setup change), skip — no README update needed.
6. Include README.md changes in the same commit as the code change, not a separate follow-up.

Do not skip this because it seems minor. Small drift compounds into a stale README fast.
