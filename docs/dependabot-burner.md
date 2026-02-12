# :dependabot: Dependabot Burner

> For an overview of all available workflows, see the [main README](../README.md).

The [dependabot burner workflow](../workflows/dependabot-burner.md?plain=1) scans for open Dependabot pull requests and bundles them into issues by runtime and manifest file to reduce PR noise.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Dependabot Burner workflow to your repository
gh aw add-wizard githubnext/agentics/dependabot-burner
```

This walks you through adding the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run dependabot-burner
```

## Configuration

This workflow requires no configuration and works out of the box. You can edit it to adjust how updates are grouped and what goes into each bundle issue.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Pull requests and their metadata
- Repository contents and dependency files

## What it creates

- Creates bundle issues summarizing related Dependabot PRs

## Human in the loop

- Review bundle issues for accuracy and completeness
- Decide which PRs to merge or close based on the bundle
- Adjust bundling logic if it is too noisy or too coarse
