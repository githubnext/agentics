# ⚡ Daily Performance Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily performance improver workflow](../workflows/daily-perf-improver.md?plain=1) will analyze code performance, identify bottlenecks, and implement optimizations through benchmarking and code improvements.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily Performance Improver workflow to your repository
gh aw add githubnext/agentics/daily-perf-improver
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

**Mandatory Checklist**

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] I will review all pull requests very carefully, and carefully monitor the repository. 

## Configuration

1. The first run of the workflow will produce a pull request with inferred action pre-steps that need approval

2. The first run of the workflow will also create an issue in the repository with a plan for improving performance. You can comment on this issue to provide feedback or adjustments to the plan. Comments will not be picked up until the next run.

3. Use local configuration to specify performance testing tools and benchmarking frameworks, optimization targets, performance metrics, and profiling strategies. Local configuration can be done in `.github/workflows/agentics/daily-perf-improver.config.md`.

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
- Requires `contents: write`, `issues: write`, and `pull-requests: write` permissions

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

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

