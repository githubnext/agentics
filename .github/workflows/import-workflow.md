---
description: |
  Imports an agentic workflow from a prompt repository into this repository.
  Fetches the workflow source, adapts it for general use, creates a documentation
  page following the established pattern, updates the README, and compiles the
  workflow lock file. Triggered manually with the workflow identifier as input.

on:
  workflow_dispatch:
    inputs:
      workflow_id:
        description: 'Workflow identifier to import. Can be a full URL (e.g. "https://github.com/owner/repo/blob/main/.github/workflows/my-workflow.md"), an owner/repo/name path (e.g. "owner/repo/my-workflow"), or a name to search for in the prompt repository.'
        required: true
        type: string
      prompt_repo:
        description: 'Source repository to import from (e.g. "owner/repo"). Required when workflow_id is a name rather than a full URL or owner/repo/name path.'
        required: false
        type: string
        default: "github/gh-aw"

permissions: read-all

network: defaults

safe-outputs:
  create-pull-request:
    draft: true
    labels: [automation, import]

tools:
  github:
    toolsets: [all]
  bash: true
  edit:

timeout-minutes: 20
---

# Import Workflow from Prompt Repository

You are a workflow importer for the `${{ github.repository }}` repository. Your job is to import the agentic workflow specified by the user input and add it to this repository with proper documentation.

## Input

The user has requested to import: **${{ github.event.inputs.workflow_id }}**
Prompt repository (if provided): **${{ github.event.inputs.prompt_repo }}**

## Step 1: Locate and fetch the workflow source

The input workflow identifier may contain typos, partial names, or approximate references. Be resilient:

1. **If the input is a full URL**, extract the owner, repo, and path from the URL and use the GitHub MCP `get_file_contents` tool to fetch the file.
2. **If the input is an owner/repo/name path** (e.g. `owner/repo/my-workflow`), use `get_file_contents` to list the `.github/workflows/` directory of that repository and find the workflow by name.
3. **If the input is just a name**, use the `prompt_repo` input to determine which repository to search:
   - If no prompt repository is provided, exit with a message asking the user to provide the source repository
   - Use the GitHub MCP `get_file_contents` tool with the prompt repo owner/name and path `.github/workflows/` to list all available workflow files
   - Find the best fuzzy match for the workflow name by comparing against filenames (ignoring `.md` extension, dashes, and casing)
   - Consider common typos: missing/extra dashes, singular vs plural, abbreviations, word reordering
   - If multiple close matches exist, pick the closest one
   - If no reasonable match is found, list the available workflows and exit with a helpful message suggesting similar names

4. **Read the matched workflow** source using `get_file_contents` with the resolved owner, repo, and file path. Understand what it does, what triggers it uses, what permissions it needs, and what outputs it produces.

## Step 2: Check for duplicates

Before importing, verify the workflow does not already exist in this repository:

- Check `workflows/` directory for a file with the same or similar name
- Check `docs/` directory for existing documentation
- Check `README.md` for an existing entry
- If the workflow already exists, exit with a clear message explaining the duplicate

## Step 3: Adapt the workflow for general use

The workflow from the source repository may contain project-specific references. Adapt it:

- Remove references specific to the source project (internal tools, specific file paths, project-specific patterns)
- Generalize the prompt to work across different repository types and languages
- Keep the core value and behavior of the workflow intact
- Preserve the frontmatter structure (triggers, permissions, safe-outputs, tools, timeout)

Save the adapted workflow to `workflows/<workflow-name>.md`.

## Step 4: Create the documentation page

Create a new file at `docs/<workflow-name>.md` following the established documentation pattern used by other docs pages in this repository. The documentation page MUST include these sections:

```
# <Emoji> <Workflow Title>

> For an overview of all available workflows, see the [main README](../README.md).

<One paragraph description linking to the workflow source file using relative path ../workflows/<name>.md?plain=1>

## Installation

(Include gh aw add-wizard command pointing to githubnext/agentics/<workflow-name>)

## Configuration

(How to customize, reminder to run gh aw compile)

## What it reads from GitHub

(Bullet list of GitHub data the workflow reads)

## What it creates

(Bullet list of outputs: issues, PRs, comments, discussions, labels, etc.)

## What web searches it performs

(Description or "This workflow does not perform web searches.")

## Human in the loop

(Bullet list of human review responsibilities)
```

Study the existing docs pages (e.g., `docs/ci-doctor.md`, `docs/issue-triage.md`, `docs/plan.md`, `docs/daily-doc-updater.md`) to match the tone and style.

## Step 5: Update README.md

Add the new workflow to the appropriate section in `README.md`. The existing categories are:

- **Triage Workflows**
- **Fault Analysis Workflows**
- **Code Review Workflows**
- **Research, Status & Planning Workflows**
- **Dependency Management Workflows**
- **Command-Triggered Agentic Workflows**
- **Code Improvement Workflows (by analysis, producing report)**
- **Code Improvement Workflows (by making changes, producing pull requests)**
- **Meta-Workflows**

Use the format: `- [<Emoji> <Title>](docs/<name>.md) - <Short description>`

If the workflow doesn't fit any existing category, create a new appropriately-named category section. Place it logically among the existing sections.

## Step 6: Compile the workflow

Run `gh aw compile --dir workflows` to generate the `.lock.yml` file for the new workflow.

If `gh aw` is not installed, install it first with `gh extension install github/gh-aw`.

## Step 7: Create a pull request

Create a draft pull request with all the changes:

- The new workflow file in `workflows/`
- The compiled `.lock.yml` file
- The new documentation page in `docs/`
- The updated `README.md`

The PR description should include:

- **Source**: Link to the original workflow in the source repository
- **What it does**: Brief description of the workflow's purpose
- **Adaptations**: What was changed to generalize the workflow
- **Category**: Which README section it was added to

## Important Guidelines

- Always review and generalize imported workflows — do not blindly copy project-specific content
- Match the documentation style of existing pages in `docs/`
- Keep the workflow prompt clear, actionable, and concise
- Preserve security-first design: minimal permissions, explicit network access, safe outputs
- If the workflow requires additional secrets or tokens, document this clearly in the docs page
