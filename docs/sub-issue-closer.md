# Sub-Issue Closer

**Automatically closes parent issues when all their sub-issues are completed**

## Overview

The Sub-Issue Closer is an automated workflow that maintains a clean and organized issue tracker by automatically closing parent issues when all of their sub-issues have been completed. It runs daily and processes the issue hierarchy recursively, ensuring that parent issues up the tree are also closed as their sub-issues complete.

## How It Works

1. **Scans for Parent Issues**: The workflow searches for open issues that have sub-issues (tracked issues)
2. **Checks Completion Status**: For each parent issue, it verifies that ALL sub-issues are closed
3. **Closes Completed Parents**: When a parent issue has 100% of its sub-issues closed, it automatically closes the parent
4. **Processes Recursively**: After closing a parent, it checks if that parent is itself a sub-issue of another parent, and repeats the process up the tree
5. **Adds Transparency**: Each closure includes an explanatory comment showing the sub-issue completion status

## Why This Is Valuable

- **Keeps Issue Tracker Clean**: Automatically closes parent issues that are implicitly complete
- **Saves Manual Work**: Eliminates the need to manually track and close parent issues
- **Provides Clarity**: Team members can see at a glance which initiatives are fully complete
- **Recursive Processing**: Handles nested issue hierarchies automatically
- **Conservative Approach**: Only closes when absolutely certain all sub-issues are done

## When It Runs

- **Daily**: Automatically runs once per day on a fuzzy schedule
- **On-Demand**: Can be manually triggered via workflow_dispatch

## Example Scenario

Imagine you have a parent issue tracking a new feature with 5 sub-issues:

``````
Issue #100: "Feature: Add User Profile"
├── #101: "Design profile page" [CLOSED]
├── #102: "Implement backend API" [CLOSED]
├── #103: "Create frontend UI" [CLOSED]
├── #104: "Write tests" [CLOSED]
└── #105: "Update documentation" [CLOSED]
``````

When the last sub-issue (#105) is closed, the next time Sub-Issue Closer runs, it will:
1. Detect that issue #100 has all 5 sub-issues closed (100%)
2. Automatically close issue #100
3. Add a comment: "🎉 Automatically closed by Sub-Issue Closer - All sub-issues completed (5/5)"
4. Check if #100 is itself a sub-issue of a higher-level parent and repeat

## Configuration

The workflow is configured with conservative limits:
- **Maximum 20 issues closed per run**: Prevents accidental mass closures
- **Maximum 20 comments added per run**: Respects API rate limits
- **Daily schedule**: Provides regular cleanup without overwhelming noise
- **Read-only GitHub permissions**: Cannot modify code, only issue status

## Best Practices

- **Use Sub-Issues**: Create parent issues with sub-issues to track multi-part work
- **Keep Sub-Issues Updated**: Close sub-issues promptly when completed
- **Trust the Automation**: The workflow is conservative and only closes when 100% certain
- **Review Closure Comments**: Each automated closure includes a transparent explanation

## What Makes This Workflow Special

- **Simple and Focused**: Does one thing well - closes completed parent issues
- **Language-Agnostic**: Works with any repository that uses GitHub Issues
- **Zero Configuration**: Works out-of-the-box with standard GitHub issue tracking
- **Recursive Logic**: Handles complex nested issue hierarchies automatically
- **Transparent Operation**: Every action is logged and explained in comments

## Merge Rate

While this workflow doesn't create pull requests (it manages issues directly), its sister workflow in the gh-aw repository has been deployed successfully and operates automatically without intervention, demonstrating its reliability and effectiveness in production use.

## Adding to Your Repository

``````bash
gh aw add workflows/sub-issue-closer.md
gh aw compile
``````

Then commit and push the compiled workflow to your repository.

## Related Workflows

- [Issue Triage](issue-triage.md) - Automatically labels and organizes new issues
- [Daily Plan](daily-plan.md) - Creates and updates planning issues with sub-tasks

## Learn More

- [GitHub Issues Documentation](https://docs.github.com/en/issues)
- [Sub-Issues and Task Lists](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists)
- [GitHub Agentic Workflows](https://github.github.io/gh-aw/)
