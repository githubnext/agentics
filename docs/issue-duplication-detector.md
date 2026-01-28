# 🔁 Issue Duplication Detector

> For an overview of all available workflows, see the [main README](../README.md).

The [Issue Duplication Detector workflow](../workflows/issue-duplication-detector.md?plain=1) automatically scans for newly created or recently updated issues every 5 minutes and flags likely duplicates with a helpful comment.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install githubnext/gh-aw

# Add the Issue Duplication Detector workflow to your repository
gh aw add githubnext/agentics/issue-duplication-detector --pr
```

This creates a pull request to add the workflow to your repository.

You must also [choose a coding agent](https://githubnext.github.io/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

After merging the PR and syncing to main, you can run the workflow manually if desired:

```bash
gh aw run issue-duplication-detector
```

## Configuration

This workflow works out of the box. You can customize detection strictness, comment tone, or batching window via a local config file at `.github/workflows/agentics/issue-duplication-detector.config.md`.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository issues (open and closed)
- Recent issues created or updated in the last 10 minutes

## What it creates

- Adds comments to issues that appear to be duplicates, including links to the matching issues
- Requires `issues: write` permission

## Human in the loop

- Review duplicate comments for accuracy and tone
- Close or link issues as appropriate
- Disable or uninstall the workflow if it is not valuable

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
