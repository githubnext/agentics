# Copilot Instructions for gh-aw Agents Repository

This repository defines autonomous GitHub agents using the [gh-aw](https://github.com/githubnext/gh-aw) framework. Each agent is a specialized workflow that can perform specific tasks in GitHub repositories.

## Repository Structure

- `workflows/` - Agent definitions in markdown format
- `workflows/shared/` - Reusable components for agent outputs and reporting

## Agent Definition Format

Agents are defined as markdown files with YAML frontmatter specifying:

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

### Components System
Use `@include` directives to incorporate reusable components:
```markdown
@include shared/shared-team-issue.md
```

## Agent Patterns

### 1. Agentic Coder (`agentic-coder.md`)
- **Purpose**: Implements features and fixes bugs
- **Workflow**: Find unlabeled issues → claim with label → implement → create PR → remove label
- **Key constraints**: No direct main branch pushes, must resolve merge conflicts
- **Tools**: Full GitHub access + unrestricted Bash

### 2. Agentic Planner (`agentic-planner.md`)
- **Purpose**: Creates and maintains project plans
- **Workflow**: Analyze repo state → create dependency graph → update "agentic-plan" issue
- **Output**: JSON plan graph with issue dependencies in collapsed section
- **Tools**: Limited to planning-focused GitHub operations

### 3. Agentic QA (`agentic-qa.md`)
- **Purpose**: Reviews pull requests and ensures quality
- **Tools**: Full GitHub access for comprehensive testing

### 4. Agentic Researcher (`agentic-researcher.md`)
- **Purpose**: Gathers information and creates research reports
- **Schedule**: Weekly execution (Monday 9AM UTC)
- **Tools**: Read-only GitHub access + limited Bash commands

### 5. Agentic Triage (`agentic-triage.md`)
- **Purpose**: Organizes and prioritizes issues

## Output Conventions

All agents must include AI attribution in generated content:
```markdown
> AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
```

### Shared Team Issue Pattern
Agents coordinate through a daily "Team Status DD/MM/YYYY" issue for progress reporting and communication.

## Development Workflow

### Adding a New Agent

1. **Create agent file** - Add a new `.md` file in `workflows/` directory
2. **Define YAML frontmatter** - Configure timeout, permissions, and tools
3. **Write job description** - Numbered steps with clear exit conditions
4. **Include components** - Use `@include shared/shared-team-issue.md` for coordination
5. **Test and compile** - Run `gh aw compile` to validate syntax

### Agent Development Process

1. **Define agent purpose** - Clear, specific role with well-defined boundaries
2. **Configure permissions** - Minimal required GitHub permissions
3. **Specify tools** - Only tools needed for the agent's specific tasks
4. **Write job description** - Numbered steps with clear exit conditions
5. **Handle edge cases** - Permission errors, conflicts, stale labels
6. **Test iteratively** - Use `gh aw compile` after edits

### Compilation and Testing

- **Compile agents**: Run `gh aw compile` after any changes to validate YAML and markdown syntax
- **Deploy agents**: Compilation transforms markdown definitions into GitHub Actions workflows
- **Debug issues**: Check compilation output for syntax errors or permission conflicts

## Key Conventions

- **Label management**: Agents claim work with their workflow name as label
- **Issue dependencies**: Use `depends_on`/`required_by` arrays in plan graphs
- **Error handling**: Always document permission failures and tool access needs
- **Branch protection**: Never push directly to main, always use pull requests
- **Cleanup**: Remove claiming labels when work is complete or abandoned

When creating new agents, model them on existing patterns but tailor tools and permissions to the specific use case. Each agent should be autonomous but coordinate through the shared issue system.
