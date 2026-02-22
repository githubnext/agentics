# 📖 Glossary Maintainer

> For an overview of all available workflows, see the [main README](../README.md).

The [Glossary Maintainer workflow](../workflows/glossary-maintainer.md?plain=1) automatically maintains project glossary or terminology documentation by scanning code changes and keeping technical terms up-to-date.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/glossary-maintainer
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run glossary-maintainer
```

## What It Does

The Glossary Maintainer workflow runs daily on weekdays and:

1. **Scans Recent Changes** - Reviews commits and PRs from the last 24 hours (daily) or 7 days (weekly on Mondays)
2. **Identifies New Terms** - Finds technical terminology, configuration options, and project-specific concepts
3. **Updates Definitions** - Adds new terms or updates existing definitions based on code changes
4. **Maintains Consistency** - Ensures glossary follows existing structure and style
5. **Creates Pull Requests** - Proposes glossary updates for review when new terms are found

## How It Works

## How It Works

````mermaid
graph LR
    A[Scan Recent Changes] --> B[Identify New Terms]
    B --> C[Check Glossary]
    C --> D{Updates Needed?}
    D -->|Yes| E[Add/Update Definitions]
    E --> F[Create PR]
    D -->|No| G[Report: Glossary Current]
````

### Incremental vs Full Scans

- **Daily (Mon-Fri)**: Incremental scan of last 24 hours
- **Monday**: Full scan of last 7 days for comprehensive review

### What Gets Added

The workflow identifies terms that are:
- Used in user-facing documentation or code
- Project-specific or domain-specific
- Technical terms requiring explanation
- Newly introduced in recent changes

### What Gets Skipped

The workflow avoids adding:
- Generic programming terms
- Self-evident terminology
- Internal implementation details
- Terms only in code comments

## Configuration

This workflow works out of the box and automatically:
- Locates your glossary file (common paths: `docs/glossary.md`, `docs/reference/glossary.md`, `GLOSSARY.md`)
- Follows your existing glossary structure and style
- Maintains alphabetical or categorical organization
- Uses cache memory to avoid duplicate work

You can edit the workflow to customize:
- The glossary file path if it's in a non-standard location
- The scanning timeframe (daily vs weekly)
- The PR title prefix and labels

After editing, run `gh aw compile` to apply your changes.

## What it reads from GitHub

- Recent commits and their diffs
- Merged pull requests from the specified timeframe
- PR descriptions and comments
- Code changes that introduce new terminology

## What it creates

- Pull requests with glossary updates
- Cache memory of processed commits to avoid duplicates

## When it runs

- **Daily on weekdays** (incremental scan of last 24 hours)
- **Mondays** (full scan of last 7 days)
- **Manually** via workflow_dispatch

## Permissions required

- `contents: read` - To read repository files
- `issues: read` - To review issue discussions
- `pull-requests: read` - To analyze PR descriptions
- `actions: read` - To check workflow runs

## Benefits

1. **Automatic maintenance**: Keeps terminology documentation current without manual tracking
2. **Consistency**: Ensures definitions stay aligned with code changes
3. **Accessibility**: Helps new contributors understand project-specific terms
4. **Time savings**: Eliminates manual glossary updates
5. **Historical context**: Uses cache memory to track what's been processed

## Example Output

When the workflow finds new terms, it creates a PR like:

**Title:** `[docs] Update glossary - daily scan`

**Body:**
```markdown
### Glossary Updates

**Scan Type**: Incremental (daily)

**Terms Added**:
- **Safe Outputs**: Security mechanism for controlling workflow write operations
- **Cache Memory**: Persistent storage for workflow state across runs

**Terms Updated**:
- **Frontmatter**: Updated to include new engine configuration options

**Changes Analyzed**:
- Reviewed 5 commits from last 24 hours
- Analyzed 2 merged PRs
- Processed 1 new feature (cache-memory tool)

**Related Changes**:
- abc1234: Add cache-memory tool support
- PR #123: Implement safe-outputs validation
```

## Source

This workflow is adapted from Peli's Agent Factory. Read more: [Meet the Workflows: Continuous Documentation](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/)

## Use Cases

This workflow is valuable for:

- **Open source projects** with growing terminology
- **Technical documentation** that needs to stay synchronized with code
- **API projects** with evolving configuration options
- **Developer tools** with CLI commands and options
- **Frameworks** with specialized concepts and patterns

## Future Enhancements

Possible improvements:
- Suggest related terms when adding new definitions
- Detect inconsistent terminology usage across documentation
- Generate glossary if one doesn't exist
- Link term usage to specific code locations
- Track term popularity and usage frequency
