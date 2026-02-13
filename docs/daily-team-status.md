# 👥 Daily Team Status

> For an overview of all available workflows, see the [main README](../README.md).

The [daily team status workflow](../workflows/daily-team-status.md?plain=1) creates daily team status reports with upbeat activity summaries. It gathers recent repository activity (issues, PRs, discussions, releases, code changes) and generates engaging GitHub issues with productivity insights, community highlights, and project recommendations. Uses a positive, encouraging tone with moderate emoji usage to boost team morale.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-team-status
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-team-status
```

## Configuration

This workflow requires no configuration and works out of the box. It will automatically gather repository activity and create daily status reports. You can edit it to customize the tone, included metrics, and reporting frequency.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Recent issues, pull requests, and discussions
- Repository commits and code changes
- Release information and milestones
- Contributor activity and community engagement
- Project boards and task progress

## What it creates

- Creates issues with the `[team-status]` prefix for daily activity reports
- Automatically labels reports with `report` and `daily-status` tags
- Requires `issues: write` permission

## Human in the loop

- Review daily status reports for team awareness and planning
- Use insights from reports to identify trends and bottlenecks
- Celebrate team achievements highlighted in status updates
- Close or archive older status reports to keep the issue list clean
- Adjust workflow tone or metrics based on team preferences
- Disable or uninstall the workflow if daily reports are not valuable
