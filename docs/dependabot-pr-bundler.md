# 📦 Dependabot PR Bundler

> For an overview of all available workflows, see the [main README](../README.md).

The [dependency PR bundler workflow](../workflows/dependabot-pr-bundler.md?plain=1) will check for Dependabot alerts in the repository and create pull requests that group together updates and fully update the dependencies to the latest versions. It will attempt to test the updates and ensure they are compatible, but human review and testing is required before merging.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/dependabot-pr-bundler
```

This walks you through adding the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run dependabot-pr-bundler
```

## How It Works

````mermaid
graph LR
    A[Check Dependabot Alerts] --> B[Group Updates]
    B --> C[Update Dependencies]
    C --> D[Run Tests]
    D --> E{Tests Pass?}
    E -->|Yes| F[Create Bundled PR]
    E -->|No| G[Report Issues]
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

## Triggering CI on Pull Requests

By default, pull requests created by this workflow do not trigger CI workflow runs. This is a GitHub Actions feature to prevent event cascades.

To trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

## Human in the loop

- Review dependency update pull requests for breaking changes
- Test updated dependencies to ensure compatibility
- Merge approved pull requests after validation
- Monitor for any issues after dependency updates are deployed
- Disable or uninstall the workflow if dependency updates cause more problems than benefits
