# 📋 Plan Command

The Plan Command is an agentic workflow that helps break down complex issues or discussions into manageable, actionable sub-tasks for GitHub Copilot agents.

> [!WARNING]
> GitHub Agentic Workflows are a research demonstrator, and these workflows are demonstrator samples only. They are not intended for production use. Use at your own risk.

## Overview

When you comment `/plan` on an issue or discussion, this workflow analyzes the content and automatically creates a series of well-structured sub-issues that:
- Break down complex work into smaller, focused tasks
- Provide clear context and acceptance criteria
- Are properly sequenced with dependencies considered
- Can be completed independently by GitHub Copilot agents

## How It Works

````mermaid
graph LR
    A[/plan Command] --> B[Analyze Issue/Discussion]
    B --> C[Break Down Work]
    C --> D[Create Sub-Issues]
    D --> E[Link to Parent]
    E --> F[Assign to Copilot]
````

## How to Use

1. **In an Issue**: Comment `/plan` to break down the issue into sub-tasks
2. **In a Discussion**: Comment `/plan` in the "Ideas" category to convert the discussion into actionable issues

The workflow will:
- Analyze the issue/discussion and its comments
- Create up to 5 focused sub-issues with clear objectives
- Link each sub-issue back to the parent
- (For Ideas discussions) Close the discussion with a summary

## What It Creates

Each sub-issue includes:
- **Clear Title**: Descriptive and action-oriented
- **Objective**: What needs to be done
- **Context**: Why this work is needed
- **Approach**: Suggested implementation steps
- **Files**: Specific files to modify or create
- **Acceptance Criteria**: How to verify completion

## Example Usage

### Issue Planning
```
Original Issue: "Implement user authentication system"

Comment: /plan

Creates sub-issues like:
1. [task] Add JWT authentication middleware
2. [task] Create user login endpoint
3. [task] Implement password hashing
4. [task] Add authentication tests
5. [task] Update API documentation
```

### Discussion to Tasks
```
Discussion (Ideas category): "Should we add real-time notifications?"

Comment: /plan

Creates actionable issues and closes the discussion as "RESOLVED"
```

## Configuration

The workflow is configured with:
- **Maximum sub-issues**: 5 (to keep tasks focused)
- **Timeout**: 10 minutes
- **Labels**: Automatically applies `task` and `ai-generated` labels
- **Title prefix**: `[task]` for easy identification
- **Safe outputs**: Creates issues in a controlled manner

## Best Practices

1. **Use descriptive issues**: The better the original issue/discussion is written, the better the breakdown
2. **Include context**: Add relevant technical details, constraints, and requirements
3. **Comment on the plan**: You can add comments on generated sub-issues to refine them
4. **Iterate if needed**: You can use `/plan` again if the breakdown needs adjustment

## When to Use

✅ **Good use cases:**
- Breaking down large features into smaller tasks
- Converting high-level ideas into concrete work items
- Planning multi-step implementations
- Creating structured task lists for team coordination

❌ **Not ideal for:**
- Simple, single-action tasks
- Issues that are already well-broken down
- Emergency bug fixes (just fix them directly)

## Limitations

- Creates a maximum of 5 sub-issues per invocation
- Requires clear, well-written parent issues/discussions
- Best suited for technical implementation tasks
- AI-generated plans may need human review and adjustment

## Permissions

This workflow requires:
- `contents: read` - To read repository files
- `discussions: read` - To read discussion content
- `issues: read` - To read issue content
- `pull-requests: read` - To read PR content

It can also:
- Create issues (with specific labels and title prefix)
- Close discussions (only in "Ideas" category)

## See Also

- [Issue Triage](issue-triage.md) - For triaging incoming issues
- [Daily Plan](daily-plan.md) - For strategic project planning
- [Daily Progress](daily-progress.md) - For automated feature development
