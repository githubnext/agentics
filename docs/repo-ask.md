# 🔍 Repo Ask

> For an overview of all available workflows, see the [main README](../README.md).

**Intelligent research assistant for your repository**

The [Repo Ask workflow](../workflows/repo-ask.md?plain=1) provides accurate, well-researched answers to questions about your codebase, features, documentation, or any repository-related topics by leveraging web search, repository analysis, and bash commands.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/repo-ask
```

This walks you through adding the workflow to your repository.

## How It Works

```mermaid
graph LR
    A[/repo-ask Question] --> B[Analyze Repository]
    B --> C[Search Codebase]
    C --> D[Research Online]
    D --> E[Compose Answer]
    E --> F[Post Comment]
```

The workflow searches for relevant documentation online, looks up technical information, and runs repository analysis commands to answer questions.

## Usage

This workflow triggers from issue or PR comments - you cannot start it manually.

### Usage as a General-Purpose Assistant

Trigger on any issue or PR:

```
/repo-ask How does the authentication system work in this project?
```

Example commands:

```
/repo-ask Has anyone reported similar issues in the past?
/repo-ask What are the testing requirements for this type of change?
/repo-ask How does this PR affect the existing authentication flow?
/repo-ask What's the best way to test this feature locally?
```

### Configuration

This workflow requires no configuration and works out of the box. You can customize research behavior and response format.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

### Human in the Loop

- Review research findings and answers provided
- Ask follow-up questions or request clarification
- Validate technical recommendations before implementing
