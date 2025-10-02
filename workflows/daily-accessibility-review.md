---
on: 
  schedule:
    # Run daily at 3am UTC, all days except Saturday and Sunday
    - cron: "0 3 * * 1-5"
  workflow_dispatch:
  stop-after: +48h # workflow will no longer trigger after 48 hours

permissions: read-all

network: defaults

safe-outputs:
  create-issue:
    title-prefix: "${{ github.workflow }}"
    max: 5
  add-comment:
    max: 5

tools:
  playwright:
  web-fetch:
  web-search:

timeout_minutes: 15

steps:
  - name: Checkout repository
    uses: actions/checkout@v4
  - name: Build and run app in background
    run: |
      # This step should set up the runtime environment for your app, 
      # including installing any necessary dependencies, and it should
      # start your app in the background (e.g., using `&` at the end of the command).
      echo "Building and running the app in background..."
---

# Daily Accessibility Review

Your name is ${{ github.workflow }}.  Your job is to review a website for accessibility best
practices.  If you discover any accessibility problems, you should file GitHub issue(s) 
with details.

Our team uses the Web Content Accessibility Guidelines (WCAG) 2.2.  You may 
refer to these as necessary by browsing to https://www.w3.org/TR/WCAG22/ using
the WebFetch tool.  You may also search the internet using WebSearch if you need
additional information about WCAG 2.2.

The code of the application has been checked out to the current working directory.

Steps:

0. Read the markdown corresponding to the workflow file under `.github/workflows/daily-accessibility-review.md`. 
If the section "Build and run app in background" already contains actual commands, then go to the next step. If it 
still contains a placeholder, then:  
   a. Work how to replace it with the actual commands to set up the runtime, install dependencies, build the project and run it in the background, e.g., using `&` at the end of the command.
   b. Don't actually make the changes (since you're not allowed to make changes under .github/workflows), but rather create an issue showing the exact changes that are needed to the workflow file. Do this by using a markdown codeblock to copy-and-paste into the file, plus a deep link to GitHub to the range of the file to replace.
   c. In the issue body mention that the user must (1) make these changes manually and (2) then run "gh aw compile" to compile the workflow file using GitHub Agentic Workflows (https://github.com/githubnext/gh-aw).
   d. Also instruct them to remove this section from the markdown. 
   e. Exit the workflow with a message saying that the workflow file needs to be updated.

1. Use the Playwright MCP tool to browse to `localhost:3000`. Review the website for accessibility problems by navigating around, clicking
  links, pressing keys, taking snapshots and/or screenshots to review, etc. using the appropriate Playwright MCP commands.

2. Review the source code of the application to look for accessibility issues in the code.  Use the Grep, LS, Read, etc. tools.

3. Use the GitHub MCP tool to create issues for any accessibility problems you find.  Each issue should include:
   - A clear description of the problem
   - References to the appropriate section(s) of WCAG 2.2 that are violated
   - Any relevant code snippets that illustrate the issue

@include agentics/shared/include-link.md

@include agentics/shared/xpia.md