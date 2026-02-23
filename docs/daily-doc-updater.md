# 📖 Daily Documentation Updater

> For an overview of all available workflows, see the [main README](../README.md).

The [Daily Documentation Updater workflow](../workflows/daily-doc-updater.md?plain=1) automatically reviews and updates documentation based on recent code changes and merged pull requests. It scans for changes in the last 24 hours and updates documentation to reflect new features, modifications, or deprecations.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-doc-updater
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-doc-updater
```

## How It Works

````mermaid
graph LR
    A[Scan Recent PRs] --> B[Find Code Changes]
    B --> C[Identify Doc Gaps]
    C --> D{Updates Needed?}
    D -->|Yes| E[Update Documentation]
    E --> F[Create PR]
    D -->|No| G[Report: Docs Current]
````

## Configuration

This workflow requires no configuration and works out of the box. It automatically:
- Scans for merged PRs from the last 24 hours
- Identifies documentation gaps
- Follows your repository's existing documentation structure and style
- Creates pull requests with documentation updates

You can edit the workflow to customize:
- The time range for scanning changes
- Which types of changes to document
- The documentation update criteria
- PR title prefix and labels

After editing, run `gh aw compile` to apply your changes.

## What it reads from GitHub

- Merged pull requests from the last 24 hours
- Recent commits and their details
- Pull request descriptions and comments
- Code changes and diffs

## What it creates

- Pull requests with documentation updates
- Updated markdown documentation files

## Triggering CI on Pull Requests

By default, pull requests created by this workflow do not trigger CI workflow runs. This is a GitHub Actions feature to prevent event cascades.

To trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

## Human in the loop

- **Pull Request Review**: All documentation changes are submitted as pull requests for review before merging
- **Manual Approval**: A human reviewer can verify accuracy, completeness, and appropriateness of documentation updates
- **Draft PRs**: Configure `draft: true` in the workflow to require explicit promotion to ready-for-review

## Use Cases

1. **Continuous Documentation**: Keep documentation synchronized with code changes automatically
2. **Feature Release Documentation**: Ensure new features are documented when they're merged
3. **API Changes**: Document API modifications, deprecations, and breaking changes
4. **Changelog Maintenance**: Help maintain up-to-date changelogs or release notes
5. **Developer Onboarding**: Ensure new developers always have current documentation

## Why It's Valuable

- **Reduces Documentation Debt**: Catches documentation gaps before they accumulate
- **Maintains Documentation Quality**: Keeps docs synchronized with code changes
- **Saves Developer Time**: Automates the tedious task of documentation maintenance
- **Improves User Experience**: Ensures users have access to current, accurate documentation
- **High Success Rate**: With a 96% merge rate in production use, this workflow consistently produces valuable documentation updates

## Activity Duration

Typical workflow execution takes 10-20 minutes depending on:
- Number of recent pull requests
- Size of the repository
- Complexity of documentation updates

## Example Workflow Run

A typical run might:
1. Scan the last 24 hours and find 3 merged PRs
2. Identify that PR #123 added a new command-line flag
3. Locate the CLI documentation file
4. Add documentation for the new flag with usage examples
5. Create a PR titled "[docs] Update documentation for features from 2026-02-15"
6. Include links to the original PR that added the feature

The resulting PR would be reviewed and merged, keeping documentation current.
