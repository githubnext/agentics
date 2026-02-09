# 🔍 Repo Ask

> For an overview of all available workflows, see the [main README](../README.md).

The [repo-ask workflow](../workflows/repo-ask.md?plain=1) is a command-triggered workflow that acts as an intelligent research assistant for your repository. When invoked with the `repo-ask` command, it provides accurate, well-researched answers to questions about your codebase, features, documentation, or any repository-related topics by leveraging web search, repository analysis, and bash commands.

You can trigger the workflow by adding a comment to any issue or pull request with the command:

```text
/repo-ask
```

or by writing a comment with a specific question:

```text
/repo-ask How does the authentication system work in this project?
```

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Repo Ask workflow to your repository
gh aw add-wizard githubnext/agentics/repo-ask
```

This walks you through adding the workflow to your repository.

You can't start a run of this workflow directly as it is triggered in the context of an issue or pull request comment.

To trigger the workflow on a specific issue or pull request, add a comment with the command:

```
/repo-ask [your question here]
```

## Configuration

This workflow requires no configuration and works out of the box. You can customize research behavior, response format, and allowed tools if needed by editing the workflow file.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and file structure
- Issue or pull request context where the command was triggered
- Pull requests and their metadata
- Actions workflow runs and results
- Repository documentation and code files
- Project configuration files

## What it creates

- Adds detailed research-based comments to issues or pull requests
- Requires `issues: write` permission

## What web searches it performs

- Searches for relevant documentation and resources online
- Looks up technical information related to the repository's technologies
- Researches best practices and solutions for specific questions
- May search for community discussions and expert opinions

## What bash commands it runs

- Repository analysis commands (e.g., `find`, `grep`, `ls`)
- Code inspection commands to understand project structure
- Test execution to verify functionality
- Build commands to understand the development workflow
- Any other repository exploration commands needed to answer questions

## Use Cases

- **Documentation Research**: Ask about how specific features work or are implemented
- **Code Analysis**: Get explanations of complex code patterns or architectures  
- **Troubleshooting**: Research solutions for build issues or configuration problems
- **Best Practices**: Get recommendations for improving code or project structure
- **Feature Investigation**: Understand what features exist and how they're used
- **Dependency Analysis**: Learn about project dependencies and their purposes

## Example Commands

```
/repo-ask Has anyone reported similar issues in the past?
/repo-ask Is this bug related to any known issues in the codebase?
/repo-ask What are the testing requirements for this type of change?
/repo-ask How does this PR affect the existing authentication flow?
/repo-ask Are there similar implementations I should look at for reference?
/repo-ask What's the best way to test this feature locally?
/repo-ask Does this change require any documentation updates?
/repo-ask What are the performance implications of this approach?
```

## Human in the loop

- Review research findings and answers provided by the workflow
- Ask follow-up questions or request clarification as needed
- Validate technical recommendations before implementing them