# Artifacts Summary

**Status**: Automated workflow analyzer  
**Trigger**: Weekly schedule or manual dispatch  
**Output**: GitHub Discussion with comprehensive artifacts usage report

## Overview

The Artifacts Summary workflow analyzes GitHub Actions artifacts across all workflows in your repository, providing insights into storage usage, costs, and optimization opportunities. It generates a comprehensive report that helps teams understand which workflows are consuming the most storage and provides actionable recommendations for reducing costs.

## What it does

1. **Scans all workflows** in the repository to identify artifact-generating workflows
2. **Collects artifact data** from recent workflow runs (typically last 30 days)
3. **Calculates statistics** including total count, total size, average size per artifact
4. **Generates a summary table** with workflow-by-workflow breakdown
5. **Provides insights** on storage trends and optimization opportunities
6. **Creates a discussion** with the full report for team review

## When to use this

- **Cost Management**: Monitor GitHub Actions storage costs and identify optimization opportunities
- **Storage Planning**: Understand artifact usage patterns before hitting storage limits
- **Workflow Optimization**: Identify workflows that generate excessive artifacts
- **Compliance**: Track artifact retention and ensure compliance with data policies
- **Trend Analysis**: Compare reports over time to see if optimization efforts are working

## Sample output

The workflow creates a discussion with a table like:

| Workflow Name | Artifacts Count | Total Size | Avg Size | Latest Run | Status |
|---------------|-----------------|------------|----------|------------|--------|
| CI Tests      | 45             | 2.3 GB     | 52 MB    | 2024-01-15 | Active |
| Build         | 12             | 456 MB     | 38 MB    | 2024-01-10 | Active |
| Deploy        | 8              | 120 MB     | 15 MB    | 2024-01-12 | Active |

Along with insights such as:
- Which workflows generate the most artifacts
- Total storage consumption
- Recommendations for optimization (e.g., reducing artifact retention, compressing artifacts)
- Trends compared to previous reports

## What it writes to GitHub

- **Creates one discussion** in the Q&A category with the artifacts usage report
- Updates existing discussion if run multiple times

## What it reads from GitHub

- Workflow configurations and metadata
- Workflow run history (last 30 days typically)
- Artifact metadata (names, sizes, dates)
- Workflow run status and completion information

## How it works

The workflow uses the GitHub Actions API to:
1. List all workflows in the repository
2. Retrieve recent workflow runs for each workflow
3. Fetch artifact information for each run
4. Aggregate statistics and calculate totals
5. Generate human-readable size formats (MB, GB)
6. Create insights and recommendations based on the data

## Configuration

This workflow requires no configuration and works out of the box. It runs weekly by default, but can be triggered manually via workflow dispatch.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## Permissions required

- `contents: read` - Read repository configuration
- `actions: read` - Access workflow runs and artifacts data

## Why this is useful

**Cost Awareness**: GitHub Actions storage costs can add up quickly, especially for repositories with many workflows generating large artifacts. This workflow provides visibility into storage consumption.

**Optimization**: By identifying which workflows use the most storage, teams can prioritize optimization efforts where they'll have the biggest impact.

**Trend Tracking**: Regular reports allow teams to track whether optimization efforts are working and catch storage growth early.

**Team Communication**: The discussion format makes it easy for teams to review and discuss artifact usage patterns together.

## Example use cases

1. **Pre-budget planning**: Run before quarterly planning to estimate storage costs
2. **Post-migration analysis**: After migrating to GitHub Actions, verify artifact usage is reasonable
3. **Continuous monitoring**: Weekly runs to catch storage spikes early
4. **Optimization campaigns**: Generate baseline report, optimize, then compare to see improvements
