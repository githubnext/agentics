# 📊 Weekly Issue Summary

> For an overview of all available workflows, see the [main README](../README.md).

The [Weekly Issue Summary workflow](../workflows/weekly-issue-summary.md?plain=1) generates a comprehensive weekly report on issue activity, including trend charts, resolution time analysis, and actionable recommendations. It runs automatically every Monday, giving maintainers a clear snapshot of repository health over the past week and the past 30 days.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/weekly-issue-summary.md
```

Then compile:

```bash
gh aw compile
```

## How It Works

````mermaid
graph LR
    A[Monday Schedule] --> B[Collect Issue Data]
    B --> C[Generate Trend Charts]
    C --> D[Upload Charts]
    D --> E[Create Weekly Discussion]
````

Each Monday at 3 PM UTC, the workflow:

1. **Collects issue data** — Queries issues opened and closed over the past 30 days, computing daily counts and resolution times
2. **Generates trend charts** — Uses Python (pandas + matplotlib + seaborn) to produce two high-quality charts:
   - **Issue Activity Trends** — Weekly opened vs. closed counts and running open total
   - **Resolution Time Trends** — Average and median days-to-close over time
3. **Uploads charts** — Stores charts as GitHub assets and collects their URLs
4. **Creates a discussion** — Posts a `[Weekly Summary]` discussion in the **Audits** category with embedded charts, statistics, and recommendations

Older `[Weekly Summary]` discussions are automatically closed when a new one is created, keeping the discussions list clean.

## What You Get

Each weekly discussion includes:

- **Overview paragraph** comparing this week to last week
- **Two embedded trend charts** showing activity and resolution patterns
- **Key trends** highlighting common issue types, label distributions, and notable patterns
- **Summary statistics table** with week-over-week comparisons
- **Full issue list** in a collapsible section
- **Recommendations** for the upcoming week

## Configuration

The workflow runs every Monday at 3 PM UTC. To change the schedule, edit the `cron` expression in the workflow frontmatter:

```yaml
on:
  schedule:
    - cron: "0 15 * * 1"  # Monday 3 PM UTC
```

## Requirements

The workflow requires:

- A **GitHub Discussions** category named `audits` (create it in your repository's Discussions settings)
- Python 3 available on the Actions runner (standard on GitHub-hosted runners)
- Network access to install Python packages (`pandas`, `matplotlib`, `seaborn`)

## Permissions

The workflow uses `issues: read` permission only — it reads issue data but never modifies issues.
