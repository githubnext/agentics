# 📦 Daily Dependency Updater

> For an overview of all available workflows, see the [main README](../README.md).

The [daily dependency updater workflow](../workflows/daily-dependency-updates.md?plain=1) will check for Dependabot alerts in the repository and update dependencies to the latest versions, creating pull requests as necessary.

## Installation

```bash
gh aw add daily-dependency-updates -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-dependency-updates
```

## Configuration

- Edit the workflow to specify dependency management tools (npm, pip, maven, etc.), customize dependency update strategies and version constraints
- Configure which dependencies to include/exclude from automated updates
- After editing run `gh aw compile` to update the workflow.

## What it reads from GitHub

- Repository contents and dependency files
- Issues and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information
- Security events and Dependabot alerts

## What it creates

- Creates pull requests with dependency updates
- Creates new branches for the dependency changes
- Makes file changes to update dependency versions
- Requires `contents: write` and `pull-requests: write` permissions

## Human in the loop

- Review dependency update pull requests for breaking changes
- Test updated dependencies to ensure compatibility
- Merge approved pull requests after validation
- Monitor for any issues after dependency updates are deployed
- Disable or uninstall the workflow if dependency updates cause more problems than benefits

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

⚠️ See notes on coding tasks in the [main README](../README.md).
