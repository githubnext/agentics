# 📦 Dependabot Issue Bundler

> For an overview of all available workflows, see the [main README](../README.md).

The [Dependabot Issue Bundler workflow](../workflows/dependabot-issue-bundler.md?plain=1) will check for Dependabot alerts in the repository and manage a set of issues that group together the updates by runtime/ecosystem (Go, Java etc.)

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/dependabot-issue-bundler
```

This walks you through adding the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run dependabot-issue-bundler
```

## How It Works

````mermaid
graph LR
    A[Check Dependabot Alerts] --> B[Group by Ecosystem]
    B --> C{Alerts Found?}
    C -->|Yes| D[Create/Update Issues]
    C -->|No| E[Report: All Clear]
````

## Configuration

This workflow requires no configuration and works out of the box. Configure the workflow by editing it.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and dependency files
- Issues and their metadata
- Security events and Dependabot alerts

## What it creates

- Creates pull requests with dependency updates
- Creates new branches for the dependency changes
- Makes file changes to update dependency versions

## Human in the loop

- Review dependency update pull requests for breaking changes
- Test updated dependencies to ensure compatibility
- Merge approved pull requests after validation
- Monitor for any issues after dependency updates are deployed
- Disable or uninstall the workflow if dependency updates cause more problems than benefits
