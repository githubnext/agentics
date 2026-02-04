---
description: Check if pull requests meet contribution guidelines and label or comment accordingly
on:
  pull_request:
    types: [opened, synchronize, reopened]

roles: all  # Allow any authenticated user to trigger this workflow via PRs

permissions: read-all

tools:
  github:
    toolsets: [default]

safe-outputs:
  add-labels:
    max: 1
  add-comment:
    max: 1

timeout-minutes: 10
---

<!-- Edit the file linked below to modify the agent without recompilation. Feel free to move the entire markdown body to that file. -->
{{#runtime-import agentics/pr-contribution-checker.md}}
