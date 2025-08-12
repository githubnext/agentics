---
on: 
  schedule:
    # Every day at 9am UTC
    - cron: "0 9 * * *"
  workflow_dispatch:

timeout_minutes: 15

max-runs: 1

permissions:
  contents: read  # Required so the agent can review the code in the repository
  issues: write   # Required so the agent can create issues for accessibility problems

tools:
  mcps:
    playwright:
      command: npx
      args: ["@playwright/mcp@0.0.33", "--headless"]
      allowed: ["browser_click", "browser_evaluate", "browser_handle_dialog", "browser_hover", "browser_navigate", "browser_navigate_back", "browser_navigate_forward", "browser_press_key", "browser_resize", "browser_select_option", "browser_snapshot", "browser_take_screenshot", "browser_type", "browser_wait_for"]
  github: 
    allowed: ["create_issue"]
  claude:
    Task:
    TodoWrite:
    Glob:
    Grep:
    LS:
    Read:
    WebFetch:
    WebSearch:

steps:
  - name: Checkout repository
    uses: actions/checkout@v4

  - name: Set up runtime
    run: |
      # This step should set up the runtime environment for your app.
      # For example, if your app is a Node.js app, you should install Node
      # and any other necessary tools.
      echo "ERROR: No runtime specified. Please update the workflow file to include the necessary setup steps."
      exit 1

  - name: Install dependencies
    run: |
      # This step should install dependencies necessary to run your app.
      # For example, if your app is a Node.js app, you should run `npm ci`.
      echo "ERROR: No dependencies specified. Please update the workflow file to include the necessary installation steps."
      exit 1

  - name: Build app
    run: |
      # This step should build your app if necessary.
      # For example, if your app is a Node.js app, you might run `npm run build`.
      echo "ERROR: No build steps specified. Please update the workflow file to include the necessary build steps."
      exit 1

  - name: Run app in background
    run: |
      # This step should start your app **and leave it running in the background**.
      # For example, if your app is a Node.js app, you might run `npm start &`.
      echo "ERROR: No app specified. Please update the workflow file to include the command to run your app."
      exit 1
---

# Agentic Accessibility Reviewer

You are an accessibility reviewer.  Your job is to review a website for accessibility best
practices.  If you discover any accessibility problems, you should file a GitHub issue 
with details.

Here are more specifics:

* Our team uses the Web Content Accessibility Guidelines (WCAG) 2.2.  You may 
  refer to these as necessary by browsing to https://www.w3.org/TR/WCAG22/ using
  the WebFetch tool.
* I have started the site running on this machine.  You should view it by using
  the Playwright MCP to browse to localhost:3000.  Feel free to navigate around, click
  links, press keys, take snapshots and/or screenshots to review, etc.
* You may also want to review the source code of the application.  Use tools like Grep, LS, 
  Read, etc. to review the code.
* Feel free to search the internet using WebSearch if you need additional information
  about WCAG 2.2.
* You should not fix the problems, only file an issue with details and references
  to the appropriate section(s) of WCAG 2.2.

@include shared/include-link.md

@include shared/job-summary.md

@include shared/tool-refused.md