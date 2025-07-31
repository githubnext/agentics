# Copilot Instructions for gh-aw Workflows Repository

This repository defines autonomous GitHub Agentic Workflows using the [gh-aw](https://github.com/githubnext/gh-aw) framework. Each workflow is a specialized workflow that can perform specific tasks in GitHub repositories.

## Repository Structure

- `workflows/` - Workflow definitions in markdown format
- `workflows/shared/` - Reusable components for workflow outputs and reporting

## Workflow Definition Format

Workflows are defined as markdown files with YAML frontmatter specifying:

### Core Configuration
- `timeout_minutes` - Maximum execution time (typically 15 minutes)
- `permissions` - GitHub permissions required (contents, models, issues, pull-requests, etc.)
- `tools` - Available tools with specific allowed operations

### Tool Categories
- **github** - GitHub API operations (list_files, create_issue, get_pull_request, etc.)
- **Bash** - Shell commands (use `:*` for unrestricted or specific prefixes like `gh:*`)
- **File operations** - Read, Edit, MultiEdit, Write, LS, Glob, Grep
- **Web** - WebFetch, WebSearch for external research
- **Notebook** - NotebookRead, NotebookEdit for Jupyter integration

## Output Conventions

All workflows must include AI attribution in generated content:
```markdown
> AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
```

## Development Workflow

### Adding a New Workflow

1. **Create workflow file** - Add a new `.md` file in `workflows/` directory
2. **Define YAML frontmatter** - Configure timeout, permissions, and tools
3. **Write job description** - Numbered steps with clear exit conditions

### Workflow Development Process

1. **Define workflow purpose** - Clear, specific role with well-defined boundaries
2. **Configure permissions** - Minimal required GitHub permissions
3. **Specify tools** - Only tools needed for the workflow's specific tasks
4. **Write job description** - Numbered steps with clear exit conditions
5. **Handle edge cases** - Permission errors, conflicts

When creating new workflows, model them on existing patterns but tailor tools and permissions to the specific use case. Each workflow should be autonomous but coordinate through the shared issue system.
