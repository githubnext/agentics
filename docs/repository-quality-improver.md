# 📊 Repository Quality Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [Repository Quality Improver workflow](../workflows/repository-quality-improver.md?plain=1) analyzes your repository from a different quality angle every weekday, producing an issue with findings and actionable improvement tasks.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/repository-quality-improver.md
```

Then compile:

```bash
gh aw compile
```

> **Note**: This workflow creates GitHub Issues with the `quality` and `automated-analysis` labels.

## What It Does

The Repository Quality Improver runs on weekdays and:

1. **Selects a Focus Area** — Picks a different quality dimension each run, using a rotating strategy to ensure broad, diverse coverage over time
2. **Analyzes the Repository** — Examines source code, configuration, tests, and documentation from the chosen angle
3. **Creates an Issue** — Posts a structured report with findings, metrics, and 3–5 actionable improvement tasks
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
    G --> H[Create Issue Report]
    H --> I[Update Cache Memory]
````

### Focus Area Strategy

The workflow follows a deliberate diversity strategy across runs:

- **60% Custom areas** — Repository-specific issues the agent discovers by inspecting the codebase: e.g., "Error Message Clarity", "Contributor Onboarding Experience", "API Consistency"
- **30% Standard categories** — Established quality dimensions: Code Quality, Documentation, Testing, Security, Performance, CI/CD, Dependencies, Code Organization, Accessibility, Usability
- **10% Revisits** — Revisit the most impactful area from recent history for follow-up

Over ten runs, the agent will typically explore 6–7+ unique quality dimensions.

### Output: GitHub Issues

Each run produces one issue containing:

- **Executive Summary** — 2–3 paragraphs of key findings
- **Full Analysis** — Detailed metrics, strengths, and areas for improvement (collapsed)
- **Improvement Tasks** — 3–5 concrete, prioritized tasks with file-level specificity
- **Historical Context** — Table of previous focus areas for reference

You can comment on the issue to request follow-up actions or add it to a project board for tracking.

## Example Reports

From the original gh-aw use (62% merge rate via causal chain):
- [CI/CD Optimization report](https://github.com/github/gh-aw/discussions/6863) — identified pipeline inefficiencies leading to multiple PRs
- [Performance report](https://github.com/github/gh-aw/discussions/13280) — surfaced bottlenecks addressed by downstream agents

## Configuration

The workflow uses these default settings:

| Setting | Default | Description |
|---------|---------|-------------|
| Schedule | Daily on weekdays | When to run the analysis |
| Issue labels | `quality`, `automated-analysis` | Labels applied to created issues |
| Max issues per run | 1 | Prevents duplicate reports |
| Issue expiry | 2 days | Older issues are closed when a new one is posted |
| Timeout | 20 minutes | Per-run time limit |

## Customization

```bash
gh aw edit repository-quality-improver
```

Common customizations:
- **Change issue labels** — Set the `labels` field in `safe-outputs.create-issue` to labels that exist in your repository
- **Adjust the schedule** — Change the cron to run less frequently if your codebase changes slowly
- **Add custom standard areas** — Extend the standard categories list with areas relevant to your project

## Tips for Success

1. **Review open issues** — Check the labeled issues regularly to pick up quick wins
2. **Add issues to a project board** — Track improvement tasks using GitHub Projects for visibility
3. **Let the diversity algorithm work** — Avoid overriding the focus area too frequently; the rotating strategy ensures broad coverage over time
4. **Review weekly** — Check recent issues to pick up any quick wins

## Source

This workflow is adapted from [Peli's Agent Factory](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-improvement/), where it achieved a 62% merge rate (25 merged PRs out of 40 proposed) via a causal discussion → issue → PR chain.

## Related Workflows

- [Daily File Diet](daily-file-diet.md) — Targeted refactoring for oversized files
- [Code Simplifier](code-simplifier.md) — Simplify recently modified code
- [Duplicate Code Detector](duplicate-code-detector.md) — Find and remove code duplication
