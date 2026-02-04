---
description: Check if PRs meet contribution guidelines and label or comment accordingly
on:
  pull_request:
    types: [opened, synchronize, reopened, edited]

permissions:
  contents: read
  pull-requests: read
  issues: read

tools:
  github:
    toolsets: [default]

safe-outputs:
  add-labels:
    allowed: [contribution-guidelines-met]
    max: 1
    target: triggering
  add-comment:
    max: 1
    target: triggering
---

<!-- Edit the file linked below to modify the agent without recompilation. Feel free to move the entire markdown body to that file. -->
{{#runtime-import agentics/pr-contribution-check.md}}
