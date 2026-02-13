# 📋 Daily Plan

> For an overview of all available workflows, see the [main README](../README.md).

The [daily plan workflow](../workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team. This planning issue can be used by other workflows as a reference for what the team is working on and what the current priorities are. You can edit the workflow to adjust the planning and report. 

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-plan
```

This walks you through adding the workflow to your repository and running the workflow for the first time.

## Configuration

This workflow requires no configuration and works out of the box. 

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and file structure
- Pull requests and their metadata

## What it creates

- Creates new planning issues for the team
- Updates existing planning issues with current information
- Requires `issues: write` permission

## What web searches it performs

- Searches for additional planning information and best practices
- May look up industry trends or project management insights

## Human in the loop

- Review and validate planning issues created or updated by the workflow
- Adjust priorities and tasks based on team feedback
- Add missing context or clarifications to planning issues
- Use planning issues as input for team coordination and sprint planning
- Disable or uninstall the workflow if planning automation is not helpful

