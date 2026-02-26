# 🔒 Sub-Issue Closer

> For an overview of all available workflows, see the [main README](../README.md).

The [Sub-Issue Closer workflow](../workflows/sub-issue-closer.md?plain=1) automatically closes parent issues when all of their sub-issues have been completed, keeping your issue tracker clean and organized.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/sub-issue-closer
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run sub-issue-closer
```

## What It Does

The Sub-Issue Closer workflow runs daily and:

1. **Scans Open Parent Issues** - Finds all open issues that have sub-issues (tracked issues)
2. **Checks Completion** - Verifies whether all sub-issues are in a closed state
3. **Closes Completed Parents** - Closes parent issues where every sub-issue is done
4. **Recurses Up the Tree** - If closing a parent reveals its own parent is now complete, that parent is closed too
5. **Adds Explanatory Comments** - Posts a comment on each closed issue explaining the automatic closure

## How It Works

````mermaid
graph LR
    A[Find Open Parent Issues] --> B[Check Sub-Issue Status]
    B --> C{All Sub-Issues Closed?}
    C -->|Yes| D[Close Parent Issue]
    D --> E[Add Closure Comment]
    E --> F{Parent Has Its Own Parent?}
    F -->|Yes| B
    F -->|No| G[Done]
    C -->|No| H[Skip - Keep Open]
````

### Recursive Closure

The workflow processes issue trees bottom-up. If you have a hierarchy like:

```
Epic #1: "Launch v2.0"
  ├── Feature #2: "User auth" (all sub-issues closed)
  │     ├── #3: "Login page" [CLOSED]
  │     └── #4: "Logout" [CLOSED]
  └── Feature #5: "Dashboard" (sub-issue still open)
        └── #6: "Chart widget" [OPEN]
```

The workflow would close Feature #2 (all sub-issues done), then check if Epic #1 can be closed too (it cannot, because Feature #5 is still open).

## What It Reads from GitHub

- Open issues and their sub-issue relationships
- Sub-issue states (open/closed)

## What It Creates

- Closes parent issues via the `update-issue` safe output
- Adds closure comments via the `add-comment` safe output

## When It Runs

- **Daily** (automatic fuzzy scheduling)
- **Manually** via workflow_dispatch

## Permissions Required

- `contents: read` - To read repository contents
- `issues: read` - To query issue and sub-issue status

## Configuration

The workflow works out of the box for any repository using GitHub's sub-issues feature. You can edit it to customize:
- Maximum issues closed per run (default: 20)
- The closure comment message
- Whether to process recursively up the tree

After editing, run `gh aw compile` to apply your changes.

## Benefits

1. **Automatic housekeeping** - Issue trackers stay clean without manual intervention
2. **Works recursively** - Cascades up through multi-level issue hierarchies
3. **Transparent** - Always explains why an issue was closed with a comment
4. **Conservative** - Only closes when 100% of sub-issues are done; skips on any doubt
5. **Complements event-driven workflows** - Catches cases that may have been missed by real-time triggers

## Example Output

When the workflow closes a parent issue, it posts a comment like:

> 🎉 **Automatically closed by Sub-Issue Closer**
>
> All sub-issues have been completed. This parent issue is now closed automatically.
>
> **Sub-issues status:** 4/4 closed (100%)

## Source

This workflow is adapted from Peli's Agent Factory. Read more: [Meet the Workflows: Organization](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-organization/)
