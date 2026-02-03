# 🧪 Daily Test Coverage Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily test coverage improver workflow](../workflows/daily-test-improver.md?plain=1) will analyze test coverage and add tests to improve coverage in under-tested areas of the codebase.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily Test Coverage Improver workflow to your repository
gh aw add githubnext/agentics/daily-test-improver
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-test-improver
```

**Mandatory Checklist**

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] I will review all pull requests very carefully, and carefully monitor the repository. 

## Configuration

1. The first run of the workflow will produce a pull request with inferred action pre-steps that need approval.

2. The first run of the workflow will also create an issue in the repository with a plan for improving test coverage. You can comment on this issue to provide feedback or adjustments to the plan. Comments will not be picked up until the next run.

3. Use local configuration or comment on the plan to specify test generation strategies, high-priority areas and coverage targets. Local configuration can be done in `.github/workflows/agentics/daily-test-improver.config.md`.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

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
