# 📚 Weekly Research

> For an overview of all available workflows, see the [main README](../README.md).

The [weekly research workflow](../workflows/weekly-research.md?plain=1) will run each Monday morning to collect research updates from the team and post them to a new issue in the repository. You can edit the workflow to adjust the topics, length and texture of the report. 

## Installation

```bash
gh aw add weekly-research -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run weekly-research
```

**Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

- No build steps required - works out of the box
- Edit the workflow file to customize output format, research topics, report length, focus areas or to adjust frequency or timing
- After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates new issues containing research reports
- Requires `issues: write` permission

## What web searches it performs

- Searches for latest trends and news from software industry sources
- Looks up information about related products and competitive analysis
- Searches for relevant research papers and academic content
- May search for market opportunities and business insights

## Human in the loop

- Review the research report issue created by the workflow
- Validate research findings and sources for accuracy
- Add additional context or follow-up questions as comments
- Close or update the issue once insights have been reviewed and acted upon
- Disable or uninstall the workflow if research reports are not useful or relevant

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering.
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
