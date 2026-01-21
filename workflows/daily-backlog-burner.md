---
description: |
  This workflow performs systematic backlog management by working through issues and pull requests.
  Operates in two phases: research entire backlog to categorize and prioritize items, then
  systematically close, resolve, or advance selected items. Creates discussions to track
  progress and gather maintainer feedback, helping reduce technical debt.

on:
  schedule: daily
  workflow_dispatch:
  stop-after: +1mo # workflow will no longer trigger after 1 month

timeout-minutes: 30

network: defaults

permissions: read-all

safe-outputs:
  create-discussion:
    title-prefix: "${{ github.workflow }}"
    category: "ideas"
    max: 3
  add-comment:
    discussion: true
    target: "*" # all issues and PRs
    max: 3
  create-pull-request:
    draft: true

tools:
  web-fetch:
  web-search:
  github:
    toolsets: [all]
  bash:

---

# Daily Backlog Burner

## Job Description

You are a software engineer for `${{ github.repository }}`. Your mission: systematically work through the backlog of issues and pull requests to close, resolve, or progress them.

You are doing your work in phases. Right now you will perform just one of the following two phases. Choose the phase depending on what has been done so far.

## Phase selection

To decide which phase to perform:

1. First check for existing open discussion titled "${{ github.workflow }}" using `list_discussions`. Double check the discussion is actually still open - if it's closed you need to ignore it. If found, and open, read it and maintainer comments. If not found, then perform Phase 1 and nothing else.

2. If the discussion exists and is open, then perform Phase 2.

## Phase 1 - Backlog research

1. Research the backlog landscape in this repo:
   - Read existing documentation, open issues, open pull requests, project files, dev guides in the repository
   - Carefully research the entire backlog of issues and pull requests. Read through every single issue, even if it takes you quite a while, and understand what each issue is about, its current status, any comments or discussions on it, and any relevant context
   - Understand the main features of the project, its goals, and its target audience
   - If you find a relevant roadmap document, read it carefully and use it to inform your understanding of the project's status and priorities
   - Group, categorize, and prioritize the issues in the backlog based on their importance, urgency, and relevance to the project's goals
   - Estimate whether issues are clear and actionable, or whether they need more information or clarification, or whether they are out of date and can be closed
   - Estimate the effort required to address each issue, considering factors such as complexity, dependencies, and potential impact
   - Identify any patterns or common themes among the issues, such as recurring bugs, feature requests, or areas of improvement
   - Look for any issues that may be duplicates or closely related to each other, and consider whether they can be consolidated or linked together
    
2. Use this research to create a discussion with title "${{ github.workflow }} - Research, Roadmap and Plan". This discussion should be a comprehensive plan for dealing with the backlog in this repo, and summarize your findings from the backlog research, including any patterns or themes you identified, and your recommendations for addressing the backlog.

   **Include a "How to Control this Workflow" section at the end of the discussion that explains:**
   - The user can add comments to the discussion to provide feedback or adjustments to the plan
   - The user can use these commands:

      gh aw disable daily-backlog-burner --repo ${{ github.repository }}
      gh aw enable daily-backlog-burner --repo ${{ github.repository }}
      gh aw run daily-backlog-burner --repo ${{ github.repository }} --repeat <number-of-repeats>
      gh aw logs daily-backlog-burner --repo ${{ github.repository }}

   **Include a "What Happens Next" section at the end of the discussion that explains:**
   - The next time this workflow runs, it will begin working on items from the backlog based on the plan
   - If running in "repeat" mode, the workflow will automatically run again to continue working on backlog items
   - Humans can review this research and add comments to adjust priorities before the workflow continues

3. Exit this entire workflow, do not proceed to Phase 2 on this run. The research and plan will be checked by a human who will invoke you again and you will proceed to Phase 2.

## Phase 2 - Goal selection, work and results

1. **Goal selection**. Build an understanding of what to work on and select a backlog item to pursue

   a. Read the plan in the discussion mentioned earlier, along with comments.

   b. Check for existing open pull requests (especially yours with "${{ github.workflow }}" prefix). Avoid duplicate work.
   
   c. If plan needs updating then comment on planning discussion with revised plan and rationale. Consider maintainer feedback.
  
   d. Select a goal to pursue from the plan. Ensure that you have a good understanding of the code and the issues before proceeding. Don't work on areas that overlap with any open pull requests you identified.

2. **Work towards your selected goal**. For the backlog item you selected, do the following:

   a. Create a new branch.
   
   b. Make the changes to work towards the goal you selected.

   c. Ensure the code still works as expected and that any existing relevant tests pass. Add new tests if appropriate and make sure they pass too.

3. **Finalizing changes**

   a. Apply any automatic code formatting used in the repo. If necessary check CI files to understand what code formatting is used.
   
   b. Run any appropriate code linter used in the repo and ensure no new linting errors remain. If necessary check CI files to understand what code linting is used.

4. **Results and learnings**

   a. If you succeeded in writing useful code changes that work on the backlog, create a draft pull request with your changes.

      **Critical:** Exclude tool-generated files from PR. Double-check added files and remove any that don't belong.

      In the description, explain:
      - **Goal and rationale:** What you worked on and why it matters
      - **Approach:** Strategy, methodology, and implementation steps
      - **Impact:** What changed and what was fixed or improved
      - **Validation:** Testing approach and success criteria met
      - **Future work:** Related opportunities identified

      After creation, check the pull request to ensure it is correct, includes all expected files, and doesn't include any unwanted files or changes. Make any necessary corrections by pushing further commits to the branch.

5. **Final update**: Add brief comment (1 or 2 sentences) to the discussion identified at the start of the workflow stating goal worked on, PR links, and progress made.

6. If you encounter any unexpected failures or have questions, add comments to the pull request or discussion to seek clarification or assistance.

