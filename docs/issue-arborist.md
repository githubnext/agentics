# 🌳 Issue Arborist

> For an overview of all available workflows, see the [main README](../README.md).

The [Issue Arborist workflow](../workflows/issue-arborist.md?plain=1) automatically organizes your issue tracker by identifying related issues and linking them as parent-child sub-issues. It keeps your issue garden tidy by building structured hierarchies from unorganized issue clusters.

## What It Does

This workflow runs daily to analyze open issues and create meaningful organization:

- **Fetches Open Issues**: Downloads the last 100 open issues that don't already have a parent
- **Identifies Relationships**: Finds natural parent-child relationships between issues through semantic analysis
- **Links Sub-Issues**: Creates parent-child links for clearly related issue pairs
- **Creates Parent Issues**: When it finds clusters of 5+ related orphan issues, it creates a new parent issue to group them
- **Reports Findings**: Creates a daily discussion report summarizing what was analyzed and linked

## Why It's Valuable

Issue trackers tend to grow organically and become hard to navigate. Related issues accumulate without structure, making it difficult to understand the overall scope of work. The Issue Arborist helps by:

- **Building structure automatically** — links related issues without requiring manual triage
- **Grouping orphan clusters** — identifies themes across unrelated-looking issues and creates parent issues for cohesive groupings
- **Improving traceability** — makes it easier to see which issues are part of broader efforts
- **Being conservative** — only links when the relationship is clear and unambiguous, avoiding false positives

## How It Works

````mermaid
graph LR
    A[Fetch Open Issues] --> B[Analyze Relationships]
    B --> C{Orphan Cluster?}
    C -->|5+ related| D[Create Parent Issue]
    D --> E[Link as Sub-Issues]
    C -->|Clear hierarchy| F[Link Existing Issues]
    E --> G[Report]
    F --> G
    B --> H{Nothing clear?}
    H --> I[Noop Report]
````

1. **Daily Schedule**: Runs automatically every day
2. **Issue Fetch**: Downloads up to 100 open issues (excluding those already linked as sub-issues)
3. **Relationship Analysis**: Examines issue titles, descriptions, and labels to find:
   - Feature requests with related implementation tasks
   - Epics with component issues
   - Bug symptoms related to a common root cause
   - Tracking issues covering multiple work items
   - Clusters of semantically related issues without a parent
4. **Linking**: Creates parent-child links for confirmed relationships (max 50 per run)
5. **Parent Creation**: For clusters of 5+ related orphans, creates a new "[Parent]" issue (max 5 per run)
6. **Discussion Report**: Publishes a daily summary with all links created and potential relationships for manual review

## Example Output

When the workflow finds and links related issues, it creates a discussion like:

```markdown
## 🌳 Issue Arborist Daily Report

**Date**: 2026-02-22
**Issues Analyzed**: 87

### Parent Issues Created

| Parent Issue | Title | Related Issues | Reasoning |
|--------------|-------|----------------|-----------|
| #234 | [Parent] Authentication Improvements | #189, #201, #215, #222, #228 | All 5 issues relate to auth flows |

### Links Created

| Parent Issue | Sub-Issue | Reasoning |
|-------------|-----------|-----------|
| #120: Epic: Docs Overhaul | #183: Update CLI docs | Clear sub-task of the epic |

### Potential Relationships (For Manual Review)

- #95 and #167 may be related (both about performance), but not confident enough to link
```

## Getting Started

This workflow works out of the box with any GitHub repository that uses issues. No configuration is required.

The workflow uses only standard GitHub CLI tools and JSON processing, making it language-agnostic and applicable to any project type.

> **Note**: For the discussion report to appear, your repository needs a GitHub Discussions category named "audits". You can update the `category` field in the workflow frontmatter to use any existing discussion category in your repository.

## Learn More

- [GitHub Agentic Workflows Documentation](https://github.github.io/gh-aw/)
- [Blog: Issue & PR Management Workflows](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-issue-management/)
