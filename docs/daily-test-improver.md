# 🧪 Daily Test Coverage Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily test coverage improver workflow](../workflows/daily-test-improver.md?plain=1) will analyze test coverage and add tests to improve coverage in under-tested areas of the codebase.

## Installation

```bash
gh aw add daily-test-improver -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-test-improver
```

## Configuration

- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - check reports from initial runs for new build commands that need approval. Add these to the workflow and then run `gh aw compile` to update the workflow.
- Edit the workflow to customize test generation strategies, high-priority areas and coverage targets
- Add project-specific test patterns and edge case identification
- After editing run `gh aw compile` to update the workflow.

## What it reads from GitHub

- Repository contents and source code for coverage analysis
- Existing test files and test coverage reports
- Build scripts and testing configuration files
- Previous issues and pull requests related to testing

## What it creates

- Creates new branches with additional test cases
- Creates draft pull requests with improved test coverage
- Creates issues documenting coverage analysis and improvements
- Makes file changes to add meaningful tests for edge cases and uncovered code
- Requires `contents: write`, `issues: write`, and `pull-requests: write` permissions

## Human in the loop

- Review test coverage improvement pull requests for test quality
- Validate that new tests properly cover edge cases and uncovered code
- Ensure tests are meaningful and not just coverage-padding
- Merge approved test improvements after verification
- Disable or uninstall the workflow if test additions are not improving code quality

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## YOLO

- If you're sufficiently isolated (e.g. operating in a fresh fork of an open source project, with Actions and Issues enabled ), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes on coding tasks in the [main README](../README.md). You will need to edit the workflow file to add the commands to build and run tests. After editing run `gh aw compile` to update the workflow.
