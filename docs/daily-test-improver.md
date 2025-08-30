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

**Checklist**

* [ ] See notes on coding tasks in the [main README](../README.md). 

* [ ] Enable "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] Recommend enabling  "Always suggest updating pull request branches" in the repository settings

* [ ] If in a fork, enable "GitHub Actions" and "GitHub Issues" in the fork project settings

* [ ] When a pull request is created, you must review the changes carefully. 

* [ ] Understand that your GitHub Actions runs will **not** trigger on pull requests created by this workflow, or indeed any Actions-created PRs. You must open/close the PR or push a new commit to trigger CI checks. This is not indicated in the GitHub UI. It's just something you need to be aware of.

## Configuration

1. The first run of the workflow will produce a pull request with inferred action pre-steps that need approval.

2. The first run of the workflow will also create an issue in the repository with a plan for improving test coverage. You can comment on this issue to provide feedback or adjustments to the plan. Comments will not be picked up until the next run.

3. Use local configuation or comment on the plan to specify test generation strategies, high-priority areas and coverage targets. Local configuration can be done in `.github/workflows/agentics/daily-test-improver.config.md`.

4. Build tool configuration for build tools shared across all workflows installed from this pack can be done in `.github/workflows/agentics/build-tools.md`.

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

## YOLO

- If you're sufficiently isolated (e.g. operating in a fresh fork of an open source project, with Actions and Issues enabled ), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

