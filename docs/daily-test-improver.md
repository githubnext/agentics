# 🧪 Daily Test Coverage Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily test coverage improver workflow](../workflows/daily-test-improver.md?plain=1) will analyze test coverage and add tests to improve coverage in under-tested areas of the codebase.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily Test Coverage Improver workflow to your repository
gh aw add githubnext/agentics/daily-test-improver --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-test-improver
```

❗IMPORTANT: GitHub Actions runs will **not** trigger on commits pushed by this workflow and will **not** tell you that CI has not been run unless you have enabled a specific custom check for this condition. **You must open/close the PR or hit "Update branch" if offered to trigger CI.Yes it's painful and yes it's just something you need to be aware of.

**Mandatory Checklist**

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] I have read the notes on coding tasks in the [main README](../README.md) and understand the implications.

* [ ] I am a repository admin or have sufficient permissions, and am happy for the safe-outputs portion of this workflow to push new branches to the repository.

* [ ] I have enabled "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] I have considered enabling "Always suggest updating pull request branches" in the repository settings

* [ ] If in a fork, I have enabled "GitHub Actions" and "GitHub Issues" in the fork repository settings

* [ ] I will review all pull requests very carefully, and carefully monitor the repository. 

* [ ] I will operate this demonstrator for a time-limited period only (the default is 48h). 

* [ ] I understand that GitHub Actions runs will **not** trigger on pull requests created by this workflow, see above.

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
