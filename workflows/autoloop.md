---
description: |
  An iterative optimization loop inspired by Karpathy's Autoresearch and Claude Code's /loop.
  Runs on a configurable schedule to autonomously improve a target artifact toward a measurable goal.
  Each iteration: reads the program definition, proposes a change, evaluates against a metric,
  and accepts or rejects the change. Tracks all iterations in a rolling GitHub issue.
  - User defines the optimization goal and evaluation criteria in a program.md file
  - Accepts changes only when they improve the metric (ratchet pattern)
  - Persists state between runs via repo memory
  - Creates draft PRs for accepted improvements
  - Maintains a living experiment log as a GitHub issue

on:
  schedule: every 6h
  workflow_dispatch:
  slash_command:
    name: autoloop

permissions: read-all

timeout-minutes: 45

network:
  allowed:
  - defaults
  - node
  - python
  - rust
  - java
  - dotnet

safe-outputs:
  add-comment:
    max: 5
    target: "*"
    hide-older-comments: false
  create-pull-request:
    draft: true
    title-prefix: "[Autoloop] "
    labels: [automation, autoloop]
    protected-files: fallback-to-issue
    max: 2
  push-to-pull-request-branch:
    target: "*"
    title-prefix: "[Autoloop] "
    max: 2
  create-issue:
    title-prefix: "[Autoloop] "
    labels: [automation, autoloop]
    max: 2
  update-issue:
    target: "*"
    title-prefix: "[Autoloop] "
    max: 1

tools:
  web-fetch:
  github:
    toolsets: [all]
  bash: true
  repo-memory: true

imports:
  - shared/reporting.md

---

# Autoloop

An iterative optimization agent that proposes changes, evaluates them against a metric, and keeps only improvements — running autonomously on a schedule.

## Command Mode

Take heed of **instructions**: "${{ steps.sanitized.outputs.text }}"

If these are non-empty (not ""), then you have been triggered via `/autoloop <instructions>`. The instructions may be:
- **A one-off directive**: e.g., `/autoloop try a different approach to the loss function`. Execute it as a single iteration using the program.md context, then report results.
- **A configuration change**: e.g., `/autoloop set metric to accuracy instead of loss`. Update the relevant program.md section and confirm.

Then exit — do not run the normal loop after completing the instructions.

## Program Definition

The user configures the optimization loop by editing **`.github/autoloop/program.md`** — a template file installed alongside this workflow. This file defines three things:

1. **Goal**: What the agent is trying to optimize (natural language description)
2. **Target**: Which files the agent is allowed to modify
3. **Evaluation**: How to measure whether a change is an improvement

### Setup Guard

**The workflow will not run until the user has edited the template.** The installed template contains a sentinel line:

```
<!-- AUTOLOOP:UNCONFIGURED -->
```

At the start of every run, check for this sentinel. If it is present:

1. **Do not run any iterations.**
2. Create a single GitHub issue (if one doesn't already exist) titled `[Autoloop] Action required: configure your program.md` with:
   - A clear explanation that the workflow is installed but paused until `program.md` is configured.
   - A direct link to the file: `${{ github.server_url }}/${{ github.repository }}/edit/${{ github.ref_name }}/.github/autoloop/program.md`
   - A brief guide: "Open the file, replace the placeholder sections with your project's goal, target files, and evaluation command, then remove the `<!-- AUTOLOOP:UNCONFIGURED -->` line."
   - Two or three example programs for inspiration (ML training, test coverage, build performance).
3. Exit.

If the sentinel is absent, proceed with the iteration loop.

### Reading the Program

At the start of every run:

1. Read `.github/autoloop/program.md` (or `program.md` in the repo root as a fallback).
2. Check for the `<!-- AUTOLOOP:UNCONFIGURED -->` sentinel — if present, run the **Setup Guard** flow above.
3. Parse the three sections: Goal, Target, Evaluation.
4. Validate that all three sections have non-placeholder content. If any section still contains `TODO` or `REPLACE` markers, treat it as unconfigured — create/update the setup issue and exit.
5. Read the current state of all target files.
6. Read repo memory for the current best metric value and iteration history.

## Iteration Loop

Each run executes **one iteration** of the optimization loop:

### Step 1: Read State

1. Read `program.md` to understand the goal, targets, and evaluation method.
2. Read repo memory to get:
   - `best_metric`: The current best metric value (null if first run).
   - `iteration_count`: How many iterations have been completed.
   - `history`: Summary of recent iterations (last 20).
   - `current_branch`: Any in-progress branch from a previous run.
   - `rejected_approaches`: Approaches that were tried and failed (to avoid repeating).

### Step 2: Analyze and Propose

1. Read the target files and understand the current state.
2. Review the history of previous iterations — what worked, what didn't.
3. **Think carefully** about what change is most likely to improve the metric. Consider:
   - What has been tried before and rejected (don't repeat failures).
   - What the evaluation criteria reward.
   - Small, targeted changes are more likely to succeed than large rewrites.
   - If many small optimizations have been exhausted, consider a larger architectural change.
4. Describe the proposed change in your reasoning before implementing it.

### Step 3: Implement

1. Create a fresh branch: `autoloop/iteration-<N>-<short-desc>` from the default branch.
2. Make the proposed changes to the target files only.
3. **Respect the program constraints**: do not modify files outside the target list.

### Step 4: Evaluate

1. Run the evaluation command specified in `program.md`.
2. Parse the metric from the output.
3. Compare against `best_metric` from memory.

### Step 5: Accept or Reject

**If the metric improved** (or this is the first run establishing a baseline):
1. Record the new `best_metric` in repo memory.
2. Create a draft PR with:
   - Title: `[Autoloop] Iteration <N>: <short description of change>`
   - Body includes: what was changed, why, the old metric, the new metric, and the improvement delta.
   - AI disclosure: `🤖 *This change was proposed and validated by Autoloop.*`
3. Add an entry to the experiment log issue.
4. Update memory: add to `history`, increment `iteration_count`, clear `current_branch`.

**If the metric did not improve** (or evaluation failed):
1. Do NOT create a PR.
2. Record the attempt in `rejected_approaches` in memory with: what was tried, the resulting metric, and why it likely didn't work.
3. Add a "rejected" entry to the experiment log issue.
4. Update memory: increment `iteration_count`, clear `current_branch`.

**If evaluation could not run** (build failure, missing dependencies, etc.):
1. Do NOT create a PR.
2. Record the error in memory.
3. Add an "error" entry to the experiment log issue.
4. If this is a recurring error (3+ times), create an issue describing the problem and pause further iterations until resolved.

## Experiment Log Issue

Maintain a single open issue titled `[Autoloop] Experiment Log {YYYY}-{MM}` as a rolling record of all iterations.

### Issue Body Format

```markdown
🤖 *Autoloop — an iterative optimization agent for this repository.*

## Program

**Goal**: {one-line summary from program.md}
**Target files**: {list of target files}
**Metric**: {metric name} ({higher/lower} is better)
**Current best**: {best_metric} (established in iteration {N})

## Iteration History

### Iteration {N} — {YYYY-MM-DD HH:MM UTC} — [Run]({run_url})
- **Status**: ✅ Accepted / ❌ Rejected / ⚠️ Error
- **Change**: {one-line description}
- **Metric**: {value} (previous best: {previous_best}, delta: {delta})
- **PR**: #{number} (if accepted)

### Iteration {N-1} — {YYYY-MM-DD HH:MM UTC} — [Run]({run_url})
- **Status**: ❌ Rejected
- **Change**: {one-line description}
- **Metric**: {value} (previous best: {previous_best}, delta: {delta})
- **Reason**: {why it was rejected}
```

### Format Rules

- Iterations in **reverse chronological order** (newest first).
- Each iteration heading links to its GitHub Actions run.
- Use `${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}` for the current run URL.
- Close the previous month's issue and create a new one at month boundaries.
- Maximum 50 iterations per issue; create a continuation issue if exceeded.

## Memory Schema

Store the following in repo memory:

```json
{
  "best_metric": 0.0234,
  "metric_name": "validation_loss",
  "metric_direction": "lower",
  "iteration_count": 17,
  "current_branch": null,
  "last_run": "2025-01-15T12:00:00Z",
  "history": [
    {
      "iteration": 17,
      "status": "accepted",
      "description": "Reduced learning rate warmup from 5 to 3 epochs",
      "metric": 0.0234,
      "previous_best": 0.0241,
      "pr": 42
    }
  ],
  "rejected_approaches": [
    {
      "iteration": 16,
      "description": "Switched from Adam to SGD with momentum",
      "metric": 0.0298,
      "reason": "SGD converges slower within the 5-minute budget"
    }
  ],
  "consecutive_errors": 0,
  "paused": false,
  "pause_reason": null
}
```

## Guidelines

- **One change per iteration.** Keep changes small and targeted. A single hyperparameter tweak, a minor architectural modification, or a focused code optimization. This makes it clear what caused metric changes.
- **No breaking changes.** Target files must remain functional even if the iteration is rejected.
- **Respect the evaluation budget.** If the evaluation command has a time constraint (e.g., 5-minute training), respect it. Do not modify evaluation scripts or timeout settings.
- **Learn from history.** The rejected_approaches list exists to prevent repeating failures. Read it carefully before proposing changes.
- **Diminishing returns.** If the last 5 consecutive iterations were rejected, post a comment on the experiment log suggesting the user review the program definition — the optimization may have plateaued.
- **Transparency.** Every PR and comment must include AI disclosure with 🤖.
- **Safety.** Never modify files outside the target list. Never modify the evaluation script. Never modify program.md (except via `/autoloop` command mode).
- **Read AGENTS.md first**: before starting work, read the repository's `AGENTS.md` file (if present) to understand project-specific conventions.
- **Build and test**: run any build/test commands before creating PRs. If your changes break the build, reject the iteration.
