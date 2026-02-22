# 🔥 Daily Backlog Burner

> For an overview of all available workflows, see the [main README](../README.md).

The [daily backlog burner workflow](../workflows/daily-backlog-burner.md?plain=1) performs systematic backlog management by working through issues and pull requests. It operates in two phases: first researching the entire backlog to categorize and prioritize items, then systematically closing, resolving, or advancing selected items. It uses repo-memory to maintain a backlog cursor across runs, ensuring steady progress through the full issue list without repeating work. Creates discussions to track progress and gather maintainer feedback, helping reduce technical debt.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-backlog-burner
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-backlog-burner
```

## How It Works

````mermaid
graph LR
    A[Research Backlog] --> B[Categorize Items]
    B --> C[Prioritize]
    C --> D{Action Needed?}
    D -->|Close| E[Close Stale Items]
    D -->|Fix| F[Create Draft PR]
    D -->|Discuss| G[Create Discussion]
````

## Configuration

This workflow requires no configuration and works out of the box. It uses repo-memory to track a backlog cursor and work history across runs, allowing it to systematically advance through issues and PRs without repeating work. You can edit it to customize prioritization criteria and decision-making logic.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- All open issues, pull requests, and their metadata
- Issue and PR comments, labels, and activity history
- Repository policies and contribution guidelines
- Discussions and community feedback
- Its own memory from previous runs (stored in a repo-memory branch)

## What it creates

- Creates discussions in the "Ideas" category to propose backlog cleanup strategies
- Adds comments to issues and PRs explaining proposed actions
- Creates draft pull requests to address backlog items
- Requires `issues: write`, `pull-requests: write`, and `discussions: write` permissions

## Human in the loop

- Review discussions created by the workflow to validate backlog cleanup proposals
- Provide feedback on prioritization decisions and item categorization
- Approve or reject proposed closures or resolutions through discussion comments
- Monitor the workflow's progress and adjust its strategy as needed
- Disable or uninstall the workflow if backlog management becomes too aggressive
