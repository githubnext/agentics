# 🏷️ Issue Triage

> For an overview of all available workflows, see the [main README](../README.md).

The [issue triage workflow](../workflows/issue-triage.md?plain=1) will when issues are created or reopened to triage issues in the repository.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Issue Triage workflow to your repository
gh aw add-wizard githubnext/agentics/issue-triage
```

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can't start a run of this workflow directly as it is triggered in the context of an issue.

## Configuration

This workflow requires no configuration and works out of the box. You can edit it to customize triage criteria, labeling logic, customize issue categorization, modify automated responses.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- The specific issue being triaged and its details
- Repository contents and file structure
- Pull requests and their metadata
- Actions workflow runs and results
- Checks and status information

## What it creates

- Adds comments to issues with triage information
- Updates issue labels, assignees, or other metadata
- Requires `issues: write` permission

## What web searches it performs

- Searches for relevant information to assist with issue triage
- May look up documentation, error messages, or similar issues

## Human in the loop

- Review triage comments added to issues for accuracy
- Validate label assignments and priority assessments
- Override or adjust triage decisions when needed
- Monitor triaged issues to ensure proper follow-up and resolution
- Disable or uninstall the workflow if triage automation is not accurate or helpful

