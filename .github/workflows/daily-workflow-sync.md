---
on:
  schedule:
    - cron: "0 13 * * 1-5"  # Daily at 1 PM UTC, weekdays only
  workflow_dispatch:

permissions: read-all

timeout-minutes: 30

network:
  allowed:
    - node
    - raw.githubusercontent.com

steps:
  - name: Checkout repository
    uses: actions/checkout@v4
    with:
      fetch-depth: 0

  - name: Install gh-aw extension
    run: gh extension install githubnext/gh-aw || gh extension upgrade githubnext/gh-aw
    env:
      GH_TOKEN: ${{ github.token }}

tools:
  github:
    allowed:
      - search_pull_requests
      - pull_request_read
      - get_file_contents
      - list_commits
  edit:
  bash:
    - "*"

safe-outputs:
  create-pull-request:
    title-prefix: "[auto-update] "
    labels: [automation]
    draft: false
    if-no-changes: "warn"
  push-to-pull-request-branch:
    title-prefix: "[auto-update]"
    if-no-changes: "warn"
  add-comment:
    max: 1

engine: copilot
---

# Daily Workflow Sync from githubnext/gh-aw

You are an automated workflow synchronization agent. Your job is to keep the workflows in this repository (`${{ github.repository }}`) in sync with the latest workflows from the `githubnext/gh-aw` repository.

## Your Mission

Follow these steps carefully to synchronize workflows:

### 1. Check for existing pull request

Search for an open pull request with title starting with `[auto-update]`:
- Use the GitHub `search_pull_requests` tool with query: `repo:${{ github.repository }} is:pr is:open "[auto-update]" in:title`
- If found, note the PR number for later use
- This determines whether to use `create-pull-request` or `push-to-pull-request-branch`

### 2. Fetch workflows from githubnext/gh-aw

Get the list of workflow files from the upstream repository:
- Use GitHub tool to get contents of `githubnext/gh-aw` at path `.github/workflows/`
- Filter for files ending in `.md` (these are agentic workflow source files)
- Exclude any `.lock.yml` files (these are generated artifacts)
- Also check for the `.github/workflows/shared/` directory and list any shared workflows

### 3. Compare with local workflows

Check what's already in this repository:
- Use bash to list files in `workflows/` directory: `ls -1 workflows/*.md 2>/dev/null || true`
- Also list shared workflows: `ls -1 workflows/shared/*.md 2>/dev/null || true`
- Compare the lists to identify:
  - New workflows that exist in gh-aw but not locally
  - Existing workflows that might need updates

### 4. Fetch and write workflow content

For each workflow file you want to sync:
- Use GitHub tool `get_file_contents` to fetch from `githubnext/gh-aw` repository
- Path: `.github/workflows/<workflow-name>.md`
- Parse the frontmatter to check for any `imports:` field
- If imports are present, fetch those shared workflow files too from `.github/workflows/shared/`
- **Use the `edit` tool** to write or update files:
  - For new files: use `create` functionality
  - For existing files: use `edit` to update the entire content
  - Save to `workflows/<workflow-name>.md` (note: local paths use `workflows/` not `.github/workflows/`)
  - For shared workflows: save to `workflows/shared/<workflow-name>.md`

### 5. Create or update the pull request

Based on whether a PR exists:

**If no existing PR was found:**
- Use the `output.create-pull-request` safe output
- Provide:
  - **title**: "Sync workflows from gh-aw"
  - **body**: A description of what workflows were added/updated, with links to githubnext/gh-aw
  - Note that lock files are excluded and will be generated on merge
- The built-in safe output will automatically create the PR with your file changes

**If an existing PR was found:**
- Use the `output.push-to-pull-request-branch` safe output
- This will push your file changes to the existing PR branch
- Then use `output.add-comment` to add a comment like: "🔄 Updated with latest changes from githubnext/gh-aw"

## Important Guidelines

- **Use the `edit` tool for all file changes** - don't try to write files manually
- **DO NOT include .lock.yml files** - only sync .md source files
- Focus on workflow source files (`.md` files only)
- When fetching workflows, get them from `githubnext/gh-aw` repository's `.github/workflows/` directory
- When saving locally, save to `workflows/` directory (without the `.github/` prefix)
- Be selective - only sync workflows that are relevant for this repo
- Include shared workflow dependencies when needed

## Example Workflow Selection

Consider syncing workflows like:
- General-purpose automation workflows (triage, maintenance, etc.)
- Example workflows that demonstrate gh-aw features
- Shared workflow components that others might import

Skip workflows that are:
- Specific to the gh-aw repository itself
- For internal testing only
- Not applicable to general users

## Error Handling

- If a workflow fails to fetch, log it and continue with others
- If no workflows need syncing, that's success - just report it
- Let the safe outputs handle PR creation/update errors

## Context

- Current repository: `${{ github.repository }}`
- Date: Run at 1 PM UTC on weekdays
