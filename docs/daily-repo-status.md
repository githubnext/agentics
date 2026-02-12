# 👥 Daily Repo Status

> For an overview of all available workflows, see the [main README](../README.md).

The [daily repo status workflow](../workflows/daily-repo-status.md?plain=1) will assess activity in the repository and create a status report issue. You can edit the workflow to adjust the topics and texture of the report. 

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily Repo Status workflow to your repository
gh aw add-wizard githubnext/agentics/daily-repo-status
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-repo-status
```

## Configuration

This workflow requires no configuration and works out of the box. You can use edit the workflow to customize triage criteria, labeling logic, customize issue categorization, modify automated responses.

## What it reads from GitHub

- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates new daily status report issues with the `[team-status]` prefix
- Automatically closes older status report issues to prevent clutter
- Labels new issues with `report` and `daily-status` tags
- Requires `issues: write` permission

## Human in the loop

- Review daily status report issues for accuracy and completeness
- Validate team activity assessments and metrics
- Comment on issues to provide additional context or corrections
- Use status reports to inform team meetings and planning decisions
- Disable or uninstall the workflow if status reports don't provide valuable insights
