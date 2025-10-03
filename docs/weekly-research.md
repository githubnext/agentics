# 📚 Weekly Research

> For an overview of all available workflows, see the [main README](../README.md).

The [weekly research workflow](../workflows/weekly-research.md?plain=1) will run each Monday morning to collect research updates from the team and post them to a new issue in the repository. You can edit the workflow to adjust the topics, length and texture of the report. 

## Installation

```bash
gh aw add githubnext/agentics/weekly-research --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run weekly-research
```

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. You can use local configuation to customize output format, research topics, report length, focus areas or to adjust frequency or timing. Local configuration can be done in `.github/workflows/agentics/daily-plan.config.md`.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates a new issue containing a research report

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

## Security

- This workflow uses "safe outputs" to create a new issue containing a research report. The overall workflow has `issues: write` permission, but the agentic step doing the research only has `issues: read` permission and runs with no GitHub write permissions
- This workflow has no access to secrets
- This workflow does not modify existing issues or other repository content
- This workflow does web searches and fetches content from the web

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering.
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
