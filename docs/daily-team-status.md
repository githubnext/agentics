# 👥 Daily Team Status

> For an overview of all available workflows, see the [main README](../README.md).

The [daily team status workflow](../workflows/daily-team-status.md?plain=1) will assess activity in the repository and create a status report issue. You can edit the workflow to adjust the topics and texture of the report. 

## Installation

```bash
gh aw add daily-team-status -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-team-status
```

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. However, you can customize it as follows:

1. Use local configuation to customize triage criteria, labeling logic, customize issue categorization, modify automated responses. Local configuration can be done in `.github/workflows/agentics/daily-team-status.config.md`.

2. Add MCPs to integrate with project management tools

## What it reads from GitHub

- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates new status report issues
- Updates existing status issues with new information
- Requires `issues: write` permission

## Human in the loop

- Review daily status report issues for accuracy and completeness
- Validate team activity assessments and metrics
- Comment on issues to provide additional context or corrections
- Use status reports to inform team meetings and planning decisions
- Disable or uninstall the workflow if status reports don't provide valuable insights

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
