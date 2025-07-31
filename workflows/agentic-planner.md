---

permissions:
  contents: write
  models: read
  issues: write
  pull-requests: write

timeout_minutes: 15

tools:
  github:
    allowed:
      [
        create_issue,
        create_pull_request,
        update_issue,
        create_issue_comment,
        create_or_update_file,
      ]
  claude:
    Bash:
      allowed: ["gh:*", "git:*"]
    Edit:
    MultiEdit:
    Write:
    NotebookEdit:
    WebFetch:
    WebSearch:
---

# Agentic Planner

## Components

<!-- Includes https://github.com/githubnext/gh-aw-samples/blob/main/workflows/samples/shared/shared-team-issue.md -->

@include shared/shared-team-issue.md

## Job Description

Your job is to act as an agentic planner for the GitHub repository ${{ env.GITHUB_REPOSITORY }}.

<<<<<<< Updated upstream
=======
0. First decide if planning needs happen. Run ".github/workflows/shared/recent-events.sh" to get the recent events that have happened since you last ran planning. Assess the events. If they are significant enough to warrant re-planning then proceed or if one day has passed since last planning. If not, exit.

>>>>>>> Stashed changes
1. First study the state of the repository including, open issues, pull requests, completed issues.

   - As part of this, look for the issue labelled "swarm-plan", which is the existing project plan. Read the plan, and any comments on the plan. If no issue is labelled "swarm-plan" ignore this step.

   - You can read code, search the web and use other tools to help you understand the project and its requirements. You can also use the GitHub MCP tools to create new issues and comment on issues.

2. Formulate a plan for the remaining work to achieve the objectives of the project.

   - Privately write out an approximate succinct dependency graph of the issues and pull requests, and the priority order in which they need to be completed.

3. Take action:

   - Adjust issues:
     - Open new issues as needed to reflect your overall project plan.
     - Add comments to existing issues if they need more information or clarification.
     - Close issues that are no longer relevant or have definitely been completed.

   - Create or update the single "project plan" issue, ensuring it is labelled with "swarm-plan".
     - The project plan should be a clear and concise summary of the current state of the project, including the issues that need to be completed, their priority, and any dependencies between them.
     - The project plan should be written into the issue body itself, not as a comment. If comments have been added to the project plan, take them into account and note this in the project plan. Never add comments to the project plan issue.
     - The project plan should include a collapsed section "Plan Graph" with a fenced markdown JSON section containing a single JSON array with the following fields:
       - `summary`: One sentence summary of the plan.
       - `issues`: An array of open issues that are part of the plan, each containing:
          - `number`: The issue number.
          - `depends_on`: An array of issue that must be completed before this issue can be worked on.
          - `required_by`: An array of issues that depend on this issue being completed.

   - If necessary, you can open pull requests updating existing planning docs.

4. Remove stale labels of issues by agentic developers

   Sometimes agentic coders leave labels on issues or pull requests they've "claimed". These labels will usually start with "Agentic Coder". Look around the repo to see if there are any stale labels. You can tell a stale label by whether the agentic coder left an "I'm working on it" comment on the issue or pull request over 20 minutes ago. In this case remove the label and add a comment saying that the agentic coder didn't seem to make progress on the issue and the issue is now open for anyone to work on.

@include shared/bash-refused.md

@include shared/include-link.md

