# 🔒 Sub-Issue Closer

> For an overview of all available workflows, see the [main README](../README.md).

The [Sub-Issue Closer workflow](../workflows/sub-issue-closer.md?plain=1) automatically closes parent issues when all their sub-issues are 100% complete. This helps keep your issue tracker organized and reduces manual maintenance overhead when working with issue hierarchies.

## What It Does

1. Scans all open parent issues in the repository
2. Checks the completion status of all sub-issues
3. Recursively closes parent issues when all sub-issues are closed
4. Adds explanatory comments to closed issues
5. Provides a summary report of actions taken

## Why It's Useful

- **Reduces Manual Overhead**: No need to manually close parent issues after completing all sub-tasks
- **Maintains Clean Issue Tracker**: Automatically keeps your issue list organized
- **Recursive Processing**: Handles multi-level issue hierarchies intelligently
- **Transparent Operations**: Adds clear comments explaining why issues were closed
- **Conservative Approach**: Only closes when absolutely certain all sub-issues are complete

## Installation

```bash
# Install the 'gh aw' extension
gh extensions install github/gh-aw

# Add the workflow
gh aw add githubnext/agentics/sub-issue-closer

# Compile to generate the GitHub Actions workflow
gh aw compile
```

## Customization

Edit `.github/workflows/sub-issue-closer.md` to adjust:

- **Schedule**: Change from `daily` to a specific cron schedule
- **Limits**: Modify `max: 20` to process more or fewer issues per run
- **Timeout**: Adjust `timeout-minutes` based on your repository size
- **Comment format**: Customize the closure comment template

## How It Works

The workflow uses GitHub's issue tracking relationships to identify parent issues and their sub-issues. It processes the issue hierarchy bottom-up, ensuring that sub-issues are evaluated before their parents. This enables recursive closure up the tree as each level reaches 100% completion.

### Example Scenario

You have this issue hierarchy:

```
Issue #10: "Major Feature Release" (OPEN)
├─ Issue #11: "Backend changes" (OPEN)
│  ├─ Issue #12: "API updates" (CLOSED)
│  └─ Issue #13: "Database migration" (CLOSED)
└─ Issue #14: "Frontend changes" (CLOSED)
```

When you close Issue #13 (the last sub-issue of #11), the workflow will:
1. Detect Issue #11 is now 100% complete → Close #11
2. Check if Issue #10's sub-issues are complete → Detect #14 (closed) and #11 (now closed)
3. Close Issue #10 since all its sub-issues are complete

## Safe Outputs

The workflow uses these safe output actions:

- **update-issue**: Closes parent issues (max 20 per run)
- **add-comment**: Adds explanatory comments (max 20 per run)

All actions are logged and visible in the workflow run output.

## Permissions

Requires these permissions:
- `contents: read` - To access repository structure
- `issues: read` - To query issue relationships

## Best Practices

1. **Use clear issue hierarchies**: Structure issues with explicit parent-child relationships
2. **Review closure comments**: Check the automated comments to ensure correct operation
3. **Start with manual testing**: Run via workflow_dispatch first to observe behavior
4. **Adjust limits as needed**: Increase max values if you have large issue hierarchies
5. **Combine with event-driven workflows**: Consider adding a complementary workflow that runs when individual issues close

## Related Workflows

- [Issue Triage](issue-triage.md) - Automated issue categorization and labeling
- [Daily Plan](daily-plan.md) - Update planning issues for team coordination
