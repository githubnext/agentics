# 🔍 Daily Adhoc QA

> For an overview of all available workflows, see the [main README](../README.md).

The [daily Adhoc QA workflow](../workflows/daily-qa.md?plain=1) will perform adhoc quality assurance tasks in the repository, such as following the instructions in the README.md, tutorials and walkthroughs to check that the code builds and runs, and that the getting started process is simple and works well. You can edit and configure the workflow to describe more tasks. 

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily QA workflow to your repository
gh aw add-wizard githubnext/agentics/daily-qa
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-qa
```

## Configuration

This workflow requires no configuration and works out of the box. You can edit it to specify QA tasks, testing scenarios, reporting format, and frequency.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and source code
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates new issues for problems found during QA
- Updates existing issues with QA findings
- Adds comments to issues with QA results
- Requires `issues: write` permission

## Human in the loop

- Review QA issues to validate reported problems
- Reproduce and confirm issues identified by the workflow
- Prioritize QA findings and assign them for resolution
- Close issues once problems have been addressed
- Disable or uninstall the workflow if QA findings are not actionable or valuable

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
