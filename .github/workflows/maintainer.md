---
on:
  workflow_dispatch:
  repository_dispatch:
    types: [maintainer]

permissions: read-all

network: defaults
engine: claude
safe-outputs:
  create-pull-request:
  create-issue:

tools:
  github:
    toolsets: [repos, issues, pull_requests]
  bash:
    - "*"

timeout-minutes: 30

steps:
  - name: Checkout repository
    uses: actions/checkout@v4
    with:
      fetch-depth: 0
      persist-credentials: false

  - name: Install gh-aw extension
    run: |
      gh extension install github/gh-aw
    env:
      GH_TOKEN: ${{ github.token }}

  - name: Verify gh-aw installation
    run: gh aw version
    env:
      GH_TOKEN: ${{ github.token }}

---

# Agentic Workflow Maintainer

Your name is "${{ github.workflow }}". Your job is to upgrade the workflows in the GitHub repository `${{ github.repository }}` to the latest version of gh-aw.

## Instructions

1. **Fetch the latest gh-aw changes**: 
   - Use the GitHub tools to fetch the CHANGELOG.md or release notes from the `github/gh-aw` repository
   - Review and understand the interesting changes, breaking changes, and new features in the latest version
   - Pay special attention to any migration guides or upgrade instructions

2. **Apply automatic fixes with codemods**:
   - Run `gh aw fix --write` to apply all available codemods that automatically fix deprecated fields and migrate to new syntax
   - This will update workflow files with changes like:
     - Replacing 'timeout_minutes' with 'timeout-minutes'
     - Replacing 'network.firewall' with 'sandbox.agent: false'
     - Removing deprecated 'safe-inputs.mode' field
   - Review the output to see what changes were made

3. **Attempt to recompile the workflows**:
   - Clean up any existing `.lock.yml` files: `find workflows -name "*.lock.yml" -type f -delete`
   - Run `gh aw compile --validate` on each workflow file in the `workflows/` directory
   - Note any compilation errors or warnings

4. **Fix compilation errors if they occur**:
   - If there are compilation errors, analyze them carefully
   - Review the gh-aw changelog and new documentation you fetched earlier
   - Identify what changes are needed in the workflow files to make them compatible with the new version
   - Make the necessary changes to the workflow markdown files to fix the errors
   - Re-run `gh aw compile --validate` to verify the fixes work
   - Iterate until all workflows compile successfully or you've exhausted reasonable fix attempts

5. **Create appropriate outputs**:
   - **If all workflows compile successfully**: Create a pull request with the title "Upgrade workflows to latest gh-aw version" containing:
     - All updated workflow files (including any codemod changes from `gh aw fix`)
     - Any generated `.lock.yml` files
     - A detailed description of what changed, referencing the gh-aw changelog
     - A summary of any automatic fixes applied by codemods
     - A summary of any manual fixes that were needed
   
   - **If there are compilation errors you cannot fix**: Create an issue with the title "Failed to upgrade workflows to latest gh-aw version" containing:
     - The specific compilation errors you encountered
     - What you tried to fix them
     - Links to relevant sections of the gh-aw changelog or documentation
     - The version of gh-aw you were trying to upgrade to

## Important notes
- The gh-aw CLI extension has already been installed and is available for use
- Always check the gh-aw changelog first to understand breaking changes
- Test each fix by running `gh aw compile --validate` before moving to the next error
- Include context and reasoning in your PR or issue descriptions

