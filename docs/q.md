# 🔧 Q - Agentic Workflow Optimizer

> For an overview of all available workflows, see the [main README](../README.md).

The [Q workflow](../workflows/q.md?plain=1) is a command-triggered workflow that acts as an expert system for optimizing and fixing agentic workflows. It provides agents with the best tools and configurations for their tasks. When invoked with the `q` command, it analyzes workflow performance, identifies missing tools, detects inefficiencies, and creates pull requests with optimized configurations.

You can trigger the workflow by adding a comment to any issue or pull request with the command:

```
/q
```

or by writing a comment with a specific request:

```
/q Analyze and optimize all workflows in this repository
```

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Q workflow to your repository
gh aw add githubnext/agentics/q --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can't start a run of this workflow directly as it is triggered in the context of an issue or pull request comment.

To trigger the workflow on a specific issue or pull request, add a comment with the command:

```
/q [your optimization request here]
```

**Mandatory Checklist**

* [ ] I have read the notes on coding tasks in the [main README](../README.md) and understand the implications.

* [ ] I understand that this workflow will analyze workflows and create pull requests with optimizations.

* [ ] I am a repository admin, maintainer, or have write permissions to trigger this workflow.

* [ ] If in a fork, I have enabled "GitHub Actions" and "GitHub Issues" in the fork repository settings.

## Configuration

This workflow requires no configuration and works out of the box. You can customize optimization behavior and analysis scope if needed.

After editing the workflow file, recompile and commit all changes to the default branch.

## What it reads from GitHub

- Workflow files and configurations in `workflows/` directory
- Actions workflow runs, logs, and audit information
- Issue or pull request context where the command was triggered
- Repository structure and shared workflow configurations
- Workflow execution history and performance metrics

## What it creates

- Pull requests with workflow optimizations (if changes are needed)
- Comments with analysis findings and recommendations
- Requires `contents: write`, `pull-requests: write`, and `issues: write` permissions

## What web searches it performs

- Searches for GitHub Actions agentic workflow best practices
- Looks up tool documentation for missing or misconfigured tools
- Researches performance optimization strategies
- Finds solutions for identified error patterns

## What bash commands it runs

- File inspection commands to analyze workflow files
- Directory traversal to find workflow configurations
- Text processing to identify patterns and issues
- Any other commands needed to analyze workflow structure

## Use Cases

- **Performance Optimization**: Identify and fix workflows with high token usage or excessive turns
- **Missing Tools**: Detect and add missing tools that workflows attempt to use
- **Permission Issues**: Fix workflows with insufficient permissions
- **Pattern Extraction**: Create shared configurations for common workflow patterns
- **Error Analysis**: Investigate recurring workflow failures and propose fixes
- **Configuration Improvements**: Add timeouts, stop-after limits, and other best practice settings

## Example Commands

```
/q Analyze all workflows and suggest optimizations
/q Fix the missing tools in the daily-progress workflow
/q Investigate why the CI doctor workflow is failing
/q Extract common patterns from coding workflows into a shared config
/q Add missing permissions to workflows that have errors
/q Optimize workflows with high token usage
/q Review and improve workflow timeout settings
```

## How It Works

1. **Context Analysis**: Parses the triggering comment to understand what needs optimization
2. **Data Gathering**: Downloads recent workflow logs and audit information using the agentic-workflows tool
3. **Code Analysis**: Examines workflow files to identify issues and patterns
4. **Research**: Uses web search to find solutions and best practices
5. **Improvements**: Makes targeted changes to workflow files
6. **Validation**: Validates changes using the compile tool
7. **Pull Request**: Creates a PR with optimizations (or comments if no changes needed)

## Human in the loop

- Review the analysis and findings before accepting optimizations
- Validate that suggested changes align with your workflow requirements
- Test workflow changes in a development environment before merging
- Provide feedback on optimization recommendations
