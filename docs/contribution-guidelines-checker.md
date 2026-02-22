# ✅ Contribution Guidelines Checker

> For an overview of all available workflows, see the [main README](../README.md).

The [contribution guidelines checker workflow](../workflows/contribution-guidelines-checker.md?plain=1) reviews incoming pull requests to verify they comply with the repository's contribution guidelines. It checks CONTRIBUTING.md and similar documentation, then either labels the PR as ready or provides constructive feedback on what needs to be improved to meet the guidelines.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/contribution-guidelines-checker
```

This walks you through adding the workflow to your repository.

The workflow automatically runs on pull requests. You can also trigger it with a 👀 (eyes) reaction on any pull request.

## How It Works

````mermaid
graph LR
    A[PR Created/Updated] --> B[Read CONTRIBUTING.md]
    B --> C[Review PR Content]
    C --> D{Guidelines Met?}
    D -->|Yes| E[Add contribution-ready Label]
    D -->|No| F[Comment with Feedback]
````

## Configuration

This workflow requires no configuration and works out of the box. It will automatically review contribution guidelines documents in your repository and check PRs against them.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Pull request content and metadata
- CONTRIBUTING.md and contribution guidelines documents
- Repository policies and documentation
- Previous PR comments and feedback

## What it creates

- Adds the `contribution-ready` label to compliant PRs
- Adds comments with constructive feedback on what needs improvement
- Requires `pull-requests: write` permission

## Human in the loop

- Review feedback provided by the workflow to validate accuracy
- Follow up on PRs that need improvements with additional guidance
- Update contribution guidelines based on common patterns
- Manually apply the label if the workflow's assessment needs adjustment
- Disable or uninstall the workflow if automated checks are not helpful
