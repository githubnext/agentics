# 📋 Plan Command

> For an overview of all available workflows, see the [main README](../README.md).

**Break down complex issues or discussions into manageable, actionable sub-tasks**

The [Plan workflow](../workflows/plan.md?plain=1) analyzes issue or discussion content and creates well-structured sub-issues that can be completed independently by GitHub Copilot agents.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/plan
```

This walks you through adding the workflow to your repository.

## How It Works

```mermaid
graph LR
    A[/plan Command] --> B[Analyze Issue/Discussion]
    B --> C[Break Down Work]
    C --> D[Create Sub-Issues]
    D --> E[Link to Parent]
    E --> F[Assign to Copilot]
```

Each sub-issue includes a clear title, objective, context, approach, specific files to modify, and acceptance criteria.

## Usage

Trigger on an issue or discussion:

```
/plan
```

- **In an Issue**: Breaks down the issue into sub-tasks
- **In a Discussion (Ideas category)**: Converts the discussion into actionable issues and closes it

### Configuration

The workflow is configured with max 5 sub-issues, 10-minute timeout, and automatically applies `task` and `ai-generated` labels.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## Learn More

- [Issue Triage](issue-triage.md) - For triaging incoming issues
- [Daily Plan](daily-plan.md) - For strategic project planning
- [Daily Progress](daily-progress.md) - For automated feature development
