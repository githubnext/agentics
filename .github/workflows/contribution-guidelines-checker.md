---
description: |
  Checks incoming PRs against the repository's contribution guidelines.
  Labels PRs that meet guidelines, and provides helpful feedback for those that don't.

on:
  pull_request:
    types: [opened, synchronize, reopened]
    forks: ["*"]

permissions: read-all

network: defaults

roles: [read]

tools:
  github:
    toolsets: [default]
  bash:
    - "cat *"
    - "ls *"

safe-outputs:
  add-labels:
    allowed: [contribution-guidelines-met]
    max: 1
  add-comment:
    max: 1
    hide-older-comments: true

timeout-minutes: 10
---

<!-- Edit the file linked below to modify the agent without recompilation. Feel free to move the entire markdown body to that file. -->
{{#runtime-import agentics/contribution-guidelines-checker.md}}
