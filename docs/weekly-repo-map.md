# 🗺️ Weekly Repository Map

> For an overview of all available workflows, see the [main README](../README.md).

**Visualize your repository's file structure and size distribution with a weekly ASCII tree map**

The [Weekly Repository Map workflow](../workflows/weekly-repo-map.md?plain=1) analyzes your repository's structure every week using standard bash tools, then creates a GitHub issue containing an ASCII tree map visualization showing directory hierarchy, file sizes, and key statistics.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/weekly-repo-map.md
```

Then compile:

```bash
gh aw compile
```

> **Note**: This workflow creates GitHub Issues with the `documentation` label.

## What It Does

The Weekly Repository Map runs every Monday and:

1. **Collects Repository Statistics** — Counts files, measures sizes, and maps the directory structure using standard bash tools
2. **Generates ASCII Tree Map** — Creates a visual representation of the repository hierarchy with proportional size bars
3. **Summarizes Key Metrics** — Reports file type distribution, largest files, and directory sizes
4. **Creates an Issue** — Posts the complete visualization as a GitHub issue, closing the previous week's issue

## How It Works

````mermaid
graph LR
    A[Collect File Statistics] --> B[Compute Sizes & Counts]
    B --> C[Generate ASCII Tree Map]
    C --> D[Compute Key Statistics]
    D --> E[Create Issue Report]
````

### Output: GitHub Issues

Each run produces one issue containing:

- **Repository Overview** — Brief summary of the repository's structure and size
- **ASCII Tree Map** — Visual directory hierarchy with size bars using box-drawing characters
- **File Type Breakdown** — Count of files by extension
- **Largest Files** — Top 10 files by size
- **Directory Sizes** — Top directories ranked by total size

Example excerpt from an issue:

```
Repository Tree Map
===================

/ [1234 files, 45.2 MB]
│
├─ src/ [456 files, 28.5 MB] ██████████████████░░
│  ├─ core/ [78 files, 5.2 MB] ████░░
│  └─ utils/ [34 files, 3.1 MB] ███░░
│
├─ docs/ [234 files, 8.7 MB] ██████░░
│
└─ tests/ [78 files, 3.5 MB] ███░░
```

## Configuration

The workflow uses these default settings:

| Setting | Default | Description |
|---------|---------|-------------|
| Schedule | Weekly on Monday | When to run the analysis |
| Issue label | `documentation` | Label applied to created issues |
| Max issues per run | 1 | Prevents duplicate reports |
| Issue expiry | 7 days | Older issues are closed when a new one is posted |
| Timeout | 10 minutes | Per-run time limit |

## Customization

```bash
gh aw edit weekly-repo-map
```

Common customizations:
- **Change issue labels** — Set the `labels` field in `safe-outputs.create-issue` to labels that exist in your repository
- **Adjust the schedule** — Change to run more or less frequently (e.g., daily or monthly)
- **Customize exclusions** — Update the bash commands to exclude additional directories (e.g., `vendor/`, `dist/`)
- **Adjust tree depth** — Edit the prompt to change how deep the tree visualization goes (default max is 3–4 levels)

## Related Workflows

- [Repository Quality Improver](repository-quality-improver.md) — Daily analysis of quality dimensions across your repository
- [Daily File Diet](daily-file-diet.md) — Monitor for oversized source files and create targeted refactoring issues
- [Weekly Issue Summary](weekly-issue-summary.md) — Weekly issue activity report with trend charts
