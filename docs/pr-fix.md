# 🔧 PR Fix

> For an overview of all available workflows, see the [main README](../README.md).

**Analyze and fix failing CI checks in pull requests**

The [PR Fix workflow](../workflows/pr-fix.md?plain=1) analyzes failing CI checks, identifies root causes, implements fixes, and pushes them to the PR branch.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/pr-fix
```

This walks you through adding the workflow to your repository.

## How It Works

```mermaid
graph LR
    A[/pr-fix Command] --> B[Analyze CI Failures]
    B --> C[Identify Root Cause]
    C --> D[Implement Fix]
    D --> E[Push to Branch]
    E --> F[Comment on PR]
```

The workflow searches for error message documentation and solutions online, and can create issues for complex problems requiring human intervention.

## Usage

Trigger on any pull request:

```
/pr-fix
```

Or with specific instructions:

```
/pr-fix Please add more tests.
```

### Configuration

This workflow requires no configuration and works out of the box. You can customize build commands, testing procedures, and linting rules, or configure AGENTS.md for all agents.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

### Triggering CI on Pull Requests

To automatically trigger CI checks on PRs updated by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

### Human in the Loop

- Review all changes pushed before merging
- Validate fixes actually resolve the intended issues
- Monitor for unintended side effects
- Provide additional context via PR comments when needed

The workflow runs for up to 48 hours after being triggered. Re-trigger by commenting with the alias again if needed.
