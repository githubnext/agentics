# Autoloop

> For an overview of all available workflows, see the [main README](../README.md).

**Iterative optimization agent inspired by [Autoresearch](https://github.com/karpathy/autoresearch) and Claude Code's `/loop`**

The [Autoloop workflow](../workflows/autoloop.md?plain=1) runs on a schedule to autonomously improve target artifacts toward measurable goals. Each iteration proposes a change, evaluates it against a metric, and keeps only improvements. Supports **multiple independent loops** in the same repository.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/autoloop
```

This walks you through adding the workflow to your repository.

## How It Works

```mermaid
graph LR
    A[Scheduled Run] --> B[Discover Programs]
    B --> C[For Each Program]
    C --> D[Review History]
    D --> E[Propose Change]
    E --> F[Implement on Branch]
    F --> G[Run Evaluation]
    G --> H{Metric Improved?}
    H -->|Yes| I[Create Draft PR]
    H -->|No| J[Record & Reject]
    I --> K[Update Experiment Log]
    J --> K
```

## Getting Started

When you install Autoloop, a **template program file** is added at `.github/autoloop/programs/example.md`. This template has placeholder sections you must fill in — the workflow **will not run** until you do.

### Setup flow

```mermaid
graph LR
    A[Install Workflow] --> B[Rename & Edit Program]
    B --> C[Define Goal, Targets, Evaluation]
    C --> D[Remove UNCONFIGURED sentinel]
    D --> E[Commit & Push]
    E --> F[Loop Begins]
```

1. **Install** — `gh aw add-wizard githubnext/agentics/autoloop`
2. **Rename** — Rename `.github/autoloop/programs/example.md` to something meaningful (e.g., `training.md`, `coverage.md`). The filename becomes the program name.
3. **Edit** — Replace the placeholders with your project's goal, target files, and evaluation command. The template includes three complete examples for inspiration.
4. **Activate** — Remove the `<!-- AUTOLOOP:UNCONFIGURED -->` line at the top.
5. **Compile & push** — `gh aw compile && git add . && git commit -m "Configure autoloop" && git push`

If you forget to edit the template, the first scheduled run will create a GitHub issue reminding you, with a direct link to edit the file.

### Adding more loops

To run multiple optimization loops in parallel, just add more `.md` files to `.github/autoloop/programs/`:

```
.github/autoloop/programs/
├── training.md      ← optimize model training loss
├── coverage.md      ← maximize test coverage
└── build-perf.md    ← minimize build time
```

Each program runs independently with its own metric tracking, experiment log issue, and PR namespace. Copy the template, fill it in, and push — the next scheduled run picks it up automatically.

## Configuration

Each program file in `.github/autoloop/programs/` has three sections:

### 1. Goal — What to optimize

Describe the objective in natural language. Be specific about what "better" means.

### 2. Target — What files can be changed

List the files the agent is allowed to modify. Everything else is off-limits.

### 3. Evaluation — How to measure success

Provide a command to run and a metric to extract. Specify whether higher or lower is better.

### Example program file

````markdown
# Autoloop Program

## Goal

Optimize the training script to minimize validation loss on CIFAR-10
within a 5-minute training budget.

## Target

Only modify these files:
- `train.py`
- `config.yaml`

## Evaluation

```bash
python train.py --epochs 5 && python evaluate.py --output-json results.json
```

Metric: `validation_loss` from `results.json`. Lower is better.
````

### Customizing the Schedule

Edit the workflow's `schedule` field. Examples:
- `every 6h` — 4 times a day (default)
- `every 1h` — hourly iterations
- `daily` — once a day
- `0 */2 * * *` — every 2 hours (cron syntax)

After editing, run `gh aw compile` to update the workflow.

Note: The schedule applies to the workflow as a whole — all programs iterate on the same schedule. To run programs at different frequencies, you can install the workflow multiple times with different schedules, each pointing to a subset of programs.

## Usage

### Automatic mode

Once at least one configured program exists, iterations run automatically on schedule. Each run processes every configured program:

1. Reads the program definition and past history
2. Proposes a single targeted change
3. Runs the evaluation command
4. Accepts (creates draft PR) or rejects (logs the attempt)

### Manual trigger

```bash
# Run all programs now
gh aw run autoloop

# Target a specific program
gh aw run autoloop -- "training: try using cosine annealing"

# If only one program exists, no prefix needed
gh aw run autoloop -- "try batch size 64 instead of 32"
```

### Slash command

Comment on any issue or PR:
```
/autoloop training: try batch size 64 instead of 32
```

## Experiment Tracking

Each program gets its own monthly experiment log issue titled `[Autoloop: {program-name}] Experiment Log {YYYY-MM}`. The issue tracks:

- Current best metric value
- Full iteration history with accept/reject status
- Links to PRs for accepted changes
- Links to GitHub Actions runs

## Human in the Loop

- **Review draft PRs** — accepted improvements appear as draft PRs for human review
- **Merge or close** — you decide which optimizations to keep
- **Adjust programs** — edit any program file to change the goal, targets, or evaluation
- **Add/remove loops** — add or delete files in `.github/autoloop/programs/`
- **Steer via slash command** — use `/autoloop {program}: {instructions}` to direct experiments
- **Pause** — disable the workflow schedule to stop all loops, or add the sentinel back to a single program file to pause just that loop

## Security

- Runs with read-only GitHub permissions
- Only modifies files listed in each program's Target section
- Never modifies evaluation scripts
- All changes go through draft PRs requiring human approval
- Uses "safe outputs" to constrain what the agent can create
