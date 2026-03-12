<!-- AUTOLOOP:UNCONFIGURED -->
<!-- ⚠️  REMOVE the line above once you've filled in your program. -->
<!-- Autoloop will NOT run until you do. -->

<!--
  Optional: control how often THIS program runs and its timeout.
  Remove the comment markers to activate. If omitted, the program
  runs on every workflow trigger with no per-program timeout.

---
schedule: every 6h
timeout-minutes: 30
---

-->

# Autoloop Program

<!--
  This file tells Autoloop what to optimize, what it can change, and how to
  measure success. Edit each section below, then remove the UNCONFIGURED
  sentinel at the top. Commit and push — the loop will start on the next
  scheduled run.

  Rename this file to something meaningful — the filename (minus .md) becomes
  the program name used in issues, PRs, and slash commands.

  Want multiple loops? Just add more .md files to this directory.

  Need inspiration? See the examples at the bottom of this file.
-->

## Goal

<!-- TODO: Describe what you want to optimize in plain language. Be specific
     about what "better" means. One or two paragraphs is plenty. -->

REPLACE THIS with your optimization goal. For example:
- "Minimize validation loss on CIFAR-10 within a 5-minute training budget"
- "Maximize test coverage percentage across the project"
- "Reduce production Docker image size"

## Target

<!-- TODO: List the files Autoloop is allowed to modify. Be explicit —
     anything not listed here is off-limits. -->

Only modify these files:
- `REPLACE_WITH_FILE_1` — (describe what this file does)
- `REPLACE_WITH_FILE_2` — (describe what this file does)

Do NOT modify:
- (list files that should never be touched, e.g., evaluation scripts, data files)

## Evaluation

<!-- TODO: Provide the command(s) to run and the metric to extract.
     The command should produce a measurable result that Autoloop can parse. -->

Run the following command to evaluate:

```bash
REPLACE_WITH_YOUR_EVALUATION_COMMAND
```

The metric is `REPLACE_WITH_METRIC_NAME` from the output. **Lower/Higher is better.** (pick one)

A change is accepted if the metric strictly improves over the previous best.
The first run establishes the baseline.

---

<!--
  ============================================================
  EXAMPLES — delete everything below this line once configured
  ============================================================

  ── Example 1: ML Training ──────────────────────────────────

  ## Goal
  Optimize the neural network training script to achieve the lowest
  possible validation loss on CIFAR-10 within a 5-minute training budget.

  ## Target
  Only modify these files:
  - `train.py` (hyperparameters, architecture, training loop)
  - `config.yaml` (configuration values)

  Do NOT modify:
  - `data.py` (data loading)
  - `evaluate.py` (evaluation script)

  ## Evaluation
  ```bash
  python train.py --epochs 5 && python evaluate.py --output-json results.json
  ```
  The metric is `validation_loss` from `results.json`. **Lower is better.**


  ── Example 2: Test Coverage ────────────────────────────────

  ## Goal
  Increase test coverage across the project by adding meaningful tests
  to under-covered modules. Focus on business logic, not boilerplate.

  ## Target
  Only modify these files:
  - `tests/**/*.test.ts` (test files)
  - `jest.config.js` (test configuration)

  Do NOT modify:
  - `src/**/*` (source code — we're only adding tests)

  ## Evaluation
  ```bash
  npm test -- --coverage --coverageReporters=json-summary 2>/dev/null
  ```
  The metric is `total.lines.pct` from `coverage/coverage-summary.json`.
  **Higher is better.**


  ── Example 3: Build Performance ────────────────────────────

  ## Goal
  Reduce production build time by optimizing the webpack configuration,
  removing unnecessary plugins, and improving code splitting.

  ## Target
  Only modify these files:
  - `webpack.config.js`
  - `tsconfig.json`
  - `.babelrc`

  Do NOT modify:
  - `src/**/*` (application source code)

  ## Evaluation
  ```bash
  time npm run build 2>&1 | tail -1
  ```
  The metric is wall-clock build time in seconds. **Lower is better.**
-->
