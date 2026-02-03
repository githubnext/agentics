# 🔍 Daily Adhoc QA

> For an overview of all available workflows, see the [main README](../README.md).

The [daily Adhoc QA workflow](../workflows/daily-qa.md?plain=1) will perform adhoc quality assurance tasks in the repository, such as following the instructions in the README.md, tutorials and walkthroughs to check that the code builds and runs, and that the getting started process is simple and works well. You can edit and configure the workflow to describe more tasks. 

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily QA workflow to your repository
gh aw add githubnext/agentics/daily-qa --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-qa
```

**Mandatory Checklist**

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. You can use local configuration to specify QA tasks, testing scenarios, reporting format, and frequency. Local configuration can be done in `.github/workflows/agentics/daily-qa.config.md`.



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
