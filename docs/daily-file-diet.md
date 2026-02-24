# 🏋️ Daily File Diet

> For an overview of all available workflows, see the [main README](../README.md).

The [Daily File Diet workflow](../workflows/daily-file-diet.md?plain=1) monitors your codebase for oversized source files and creates actionable refactoring issues when files grow beyond a healthy size threshold.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/daily-file-diet.md
```

Then compile:

```bash
gh aw compile
```

## What It Does

The Daily File Diet workflow runs on weekdays and:

1. **Scans Source Files** - Finds all non-test source files in your repository, excluding generated directories like `node_modules`, `vendor`, `dist`, and `target`
2. **Identifies Oversized Files** - Detects files exceeding 500 lines (the healthy size threshold)
3. **Analyzes Structure** - Examines what the file contains: functions, classes, modules, and their relationships
4. **Creates Refactoring Issues** - Proposes concrete split strategies with specific file names, responsibilities, and implementation guidance
5. **Skips When Healthy** - If no file exceeds the threshold, reports all-clear with no issue created

## How It Works

````mermaid
graph LR
    A[Scan Source Files] --> B[Sort by Line Count]
    B --> C{Largest File<br/>≥ 500 lines?}
    C -->|No| D[Report: All Files Healthy]
    C -->|Yes| E[Analyze File Structure]
    E --> F[Propose File Splits]
    F --> G[Create Refactoring Issue]
````

The workflow focuses on **production source code only** — test files are excluded so the signal stays relevant. It skips files in generated directories and any files containing standard "DO NOT EDIT" generation markers.

### Why File Size Matters

Large files are a universal code smell that affects every programming language:

- **Hard to navigate**: Scrolling through 1000+ line files wastes developer time
- **Increases merge conflicts**: Multiple developers frequently change the same large file
- **Harder to test**: Large files tend to mix concerns, making isolated unit testing difficult
- **Obscures ownership**: It's unclear who is responsible for what in a large catch-all file

The 500-line threshold is a practical guideline. Files near the threshold may be fine; files well over it are worth examining.

## Example Issues

From the original gh-aw repository (79% merge rate):
- Targeting `add_interactive.go` (large file) → [PR refactored it into 6 domain-focused modules](https://github.com/github/gh-aw/pull/12545)
- Targeting `permissions.go` → [PR splitting into focused modules](https://github.com/github/gh-aw/pull/12363) (928 → 133 lines)

## Configuration

The workflow uses these default settings:

- **Schedule**: Weekdays at 1 PM UTC
- **Threshold**: 500 lines
- **Issue labels**: `refactoring`, `code-health`, `automated-analysis`
- **Max issues per run**: 1 (one file at a time to avoid overwhelming the backlog)
- **Issue expiry**: 2 days if not actioned
- **Skip condition**: Does not run if a `[file-diet]` issue is already open

## Customization

You can customize the workflow by editing the source file:

```bash
gh aw edit daily-file-diet
```

Common customizations:
- **Adjust the threshold** - Change the 500-line limit to suit your team's preferences
- **Focus on specific languages** - Restrict `find` commands to your repository's primary language
- **Add labels** - Apply team-specific labels to generated issues
- **Change the schedule** - Run less frequently if your codebase changes slowly

## Tips for Success

1. **Work the backlog gradually** - The workflow creates one issue at a time to keep the backlog manageable
2. **Split incrementally** - Refactor one module at a time to make review easier
3. **Update imports throughout** - After splitting a file, search the codebase for all import paths that need updating
4. **Trust the threshold** - Files just above 500 lines may not need splitting; focus on files that are significantly larger

## Source

This workflow is adapted from [Peli's Agent Factory](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-refactoring/), where it achieved a 79% merge rate with 26 merged PRs out of 33 proposed in the gh-aw repository.

## Related Workflows

- [Code Simplifier](code-simplifier.md) - Simplifies recently modified code
- [Duplicate Code Detector](duplicate-code-detector.md) - Finds and removes code duplication
- [Daily Performance Improver](daily-perf-improver.md) - Optimizes code performance
