# 📊 Repository Quality Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [Repository Quality Improver workflow](../workflows/repository-quality-improver.md?plain=1) analyzes your repository from a different quality angle every day, producing a discussion with findings and actionable improvement tasks.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/repository-quality-improver.md
```

Then compile:

```bash
gh aw compile
```

> **Note**: This workflow posts results as GitHub Discussions. Make sure Discussions are enabled in your repository settings, and update the `category` field in the workflow to match an existing discussion category in your repo.

## What It Does

The Repository Quality Improver runs on weekdays and:

1. **Selects a Focus Area** — Picks a different quality dimension each run, using a rotating strategy to ensure broad, diverse coverage over time
2. **Analyzes the Repository** — Examines source code, configuration, tests, and documentation from the chosen angle
3. **Produces a Discussion** — Posts a structured report with findings, metrics, and 3–5 actionable improvement tasks
4. **Tracks History** — Remembers previous focus areas (using cache memory) to avoid repetition and maximize coverage

## How It Works

````mermaid
graph LR
    A[Load Focus History] --> B[Select Focus Area]
    B --> C{Strategy?}
    C -->|60%| D[Custom: Repo-specific area]
    C -->|30%| E[Standard: Code/Docs/Tests/Security...]
    C -->|10%| F[Reuse: Most impactful recent area]
    D --> G[Analyze Repository]
    E --> G
    F --> G
    G --> H[Generate Discussion Report]
    H --> I[Update Cache Memory]
````

### Focus Area Strategy

The workflow follows a deliberate diversity strategy across runs:

- **60% Custom areas** — Repository-specific issues the agent discovers by inspecting the codebase: e.g., "Error Message Clarity", "Contributor Onboarding Experience", "API Consistency"
- **30% Standard categories** — Established quality dimensions: Code Quality, Documentation, Testing, Security, Performance, CI/CD, Dependencies, Code Organization, Accessibility, Usability
- **10% Revisits** — Revisit the most impactful area from recent history for follow-up

Over ten runs, the agent will typically explore 6–7+ unique quality dimensions.

### Output: GitHub Discussions

Each run produces one discussion containing:

- **Executive Summary** — 2–3 paragraphs of key findings
- **Full Analysis** — Detailed metrics, strengths, and areas for improvement (collapsed)
- **Improvement Tasks** — 3–5 concrete, prioritized tasks with file-level specificity
- **Historical Context** — Table of previous focus areas for reference

You can use the `/plan` command on the discussion to automatically break the tasks into trackable GitHub issues.

## Example Reports

From the original gh-aw use (62% merge rate via causal chain):
- [CI/CD Optimization report](https://github.com/github/gh-aw/discussions/6863) — identified pipeline inefficiencies leading to multiple PRs
- [Performance report](https://github.com/github/gh-aw/discussions/13280) — surfaced bottlenecks addressed by downstream agents

## Configuration

The workflow uses these default settings:

| Setting | Default | Description |
|---------|---------|-------------|
| Schedule | Weekdays at 1 PM UTC | When to run the analysis |
| Discussion category | `General` | Category for posted discussions |
| Max discussions per run | 1 | Prevents duplicate reports |
| Discussion expiry | 2 days | Older discussions are closed when a new one is posted |
| Timeout | 20 minutes | Per-run time limit |

## Customization

```bash
gh aw edit repository-quality-improver
```

Common customizations:
- **Change discussion category** — Set the `category` field in `safe-outputs.create-discussion` to a category that exists in your repo's Discussions settings
- **Adjust the schedule** — Change the cron to run less frequently if your codebase changes slowly
- **Add custom standard areas** — Extend the standard categories list with areas relevant to your project

## Tips for Success

1. **Enable GitHub Discussions** — The workflow requires Discussions to be turned on in your repository settings
2. **Use `/plan` on reports** — Pair this workflow with the [Plan Command](plan.md) to automatically turn discussion tasks into trackable issues
3. **Let the diversity algorithm work** — Avoid overriding the focus area too frequently; the rotating strategy ensures broad coverage over time
4. **Review weekly** — Check the weekly discussion thread to pick up any quick wins

## Source

This workflow is adapted from [Peli's Agent Factory](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-improvement/), where it achieved a 62% merge rate (25 merged PRs out of 40 proposed) via a causal discussion → issue → PR chain.

## Related Workflows

- [Plan Command](plan.md) — Turn discussion tasks into actionable sub-issues with `/plan`
- [Daily File Diet](daily-file-diet.md) — Targeted refactoring for oversized files
- [Code Simplifier](code-simplifier.md) — Simplify recently modified code
- [Duplicate Code Detector](duplicate-code-detector.md) — Find and remove code duplication
