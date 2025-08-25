# ⚡ Daily Performance Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily performance improver workflow](../workflows/daily-perf-improver.md?plain=1) will analyze code performance, identify bottlenecks, and implement optimizations through benchmarking and code improvements.

## Installation

```bash
gh aw add daily-perf-improver -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-perf-improver
```

## Configuration

- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify performance testing tools and benchmarking frameworks
- Customize optimization targets, performance metrics, and profiling strategies
- Add project-specific bottleneck identification and performance validation steps

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

## YOLO

- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes on coding tasks in the [main README](../README.md). You will need to edit the workflow file to add the commands to build, test and profile. After editing run `gh aw compile` to update the workflow.
