# ⚡ Daily Performance Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily performance improver workflow](../workflows/daily-perf-improver.md?plain=1) will analyze code performance, identify bottlenecks, and implement optimizations through benchmarking and code improvements.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-perf-improver
```

This walks you through adding the workflow to your repository and running the workflow for the first time.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-perf-improver
```

To run repeatedly (at most one instance running at a time and sending a trigger every 3 minutes), use:

```bash
gh aw run daily-perf-improver --repeat 180
```

## Configuration

1. The first run of the workflow will produce a pull request with inferred action pre-steps that need approval

2. The first run of the workflow will also create an issue in the repository with a plan for improving performance. You can comment on this issue to provide feedback or adjustments to the plan. Comments will not be picked up until the next run.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and source code for performance analysis
- Existing issues and pull requests related to performance
- Build scripts and project configuration files
- CI/CD configurations and workflow results

## What it creates

- Creates new branches with performance improvements
- Creates draft pull requests with optimized code and benchmark results
- Creates issues documenting performance analysis and improvements
- Makes file changes to optimize algorithms and data structures

## What web searches it performs

- Searches for performance optimization techniques and best practices
- Looks up benchmarking tools and methodologies
- May search for algorithm optimizations and data structure improvements

## Human in the loop

- Review performance improvement pull requests and benchmark results
- Validate performance gains through independent testing
- Assess code quality and maintainability of optimizations
- Merge approved performance improvements after thorough testing
- Disable or uninstall the workflow if performance optimizations are not effective or introduce bugs

