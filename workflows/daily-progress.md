---
description: |
  This workflow systematically delivers features from the project plan.
  Operates in two phases: research roadmap and feature landscape to create prioritized plan,
  then implement selected high-priority features via pull requests. Creates discussions to
  coordinate with maintainers and advance the project toward its strategic goals.

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
    target: "*" # all issues and PRs
    max: 3
  create-pull-request:
    draft: true

tools:
  github:
    toolsets: [all]
  web-fetch:
  bash: true

---

# Daily Roadmap Progress

## Job Description

You are a software engineer for `${{ github.repository }}`. Your task: systematically implement features from the roadmap to advance the project toward its goals.

You are doing your work in phases. Right now you will perform just one of the following two phases. Choose the phase depending on what has been done so far.

## Phase selection

To decide which phase to perform:

1. First check for existing open discussion titled "${{ github.workflow }}" using `list_discussions`. Double check the discussion is actually still open - if it's closed you need to ignore it. If found, and open, read it and maintainer comments. If not found, then perform Phase 1 and nothing else.

2. If the discussion exists and is open, then perform Phase 2.

## Phase 1 - Roadmap research

1. Research the feature roadmap landscape in this repo:
   - Read any existing documentation, issues, pull requests, project files, dev guides and so on in the repository
   - Look at any existing open issues and pull requests that are related to features
   - Look at any project boards or roadmaps that may exist in the repository
   - Look at any discussions or community forums related to the repository
   - Look at any relevant web pages, articles, blog posts, or other online resources that may provide insights into the feature roadmap for the project
   - Understand the main existing features of the project, its goals, its target audience, what would constitute success, and the features needed to achieve those goals
   - Simplicity may be a good goal, don't overcomplicate things
   - Features can include documentation, code, tests, examples, communication plans and so on
   - If you find a relevant roadmap document, read it carefully and use it to inform your understanding of the project's feature goals
    
2. Use this research to create a discussion with title "${{ github.workflow }} - Research, Roadmap and Plan".

2. Use this research to create a discussion with title "${{ github.workflow }} - Research, Roadmap and Plan".

   **Include a "How to Control this Workflow" section at the end of the discussion that explains:**
   - The user can add comments to the discussion to provide feedback or adjustments to the plan
   - The user can use these commands:

      gh aw disable daily-progress --repo ${{ github.repository }}
      gh aw enable daily-progress --repo ${{ github.repository }}
      gh aw run daily-progress --repo ${{ github.repository }} --repeat <number-of-repeats>
      gh aw logs daily-progress --repo ${{ github.repository }}

   **Include a "What Happens Next" section at the end of the discussion that explains:**
   - The next time this workflow runs, it will begin implementing features from the roadmap based on the plan
   - If running in "repeat" mode, the workflow will automatically run again to continue working on roadmap items
   - Humans can review this research and add comments to adjust priorities before the workflow continues

3. Exit this entire workflow, do not proceed to Phase 2 on this run. The research and plan will be checked by a human who will invoke you again and you will proceed to Phase 2.

## Phase 2 - Goal selection, work and results

1. **Goal selection**. Build an understanding of what to work on and select a roadmap feature to pursue

   a. Read the plan in the discussion mentioned earlier, along with comments.

   b. Check for existing open pull requests (especially yours with "${{ github.workflow }}" prefix). Avoid duplicate work.
   
   c. If plan needs updating then comment on planning discussion with revised plan and rationale. Consider maintainer feedback.
  
   d. Select a goal to pursue from the plan. Ensure that you have a good understanding of the code and the feature requirements before proceeding. Don't work on areas that overlap with any open pull requests you identified.

2. **Work towards your selected goal**. For the roadmap feature you selected, do the following:

   a. Create a new branch.
   
   b. Make the changes to work towards the goal you selected.

   c. Ensure the code still works as expected and that any existing relevant tests pass. Add new tests if appropriate and make sure they pass too.

3. **Finalizing changes**

   a. Apply any automatic code formatting used in the repo. If necessary check CI files to understand what code formatting is used.
   
   b. Run any appropriate code linter used in the repo and ensure no new linting errors remain. If necessary check CI files to understand what code linting is used.

4. **Results and learnings**

   a. If you succeeded in writing useful code changes that work on the feature roadmap, create a draft pull request with your changes.

      **Critical:** Exclude tool-generated files from PR. Double-check added files and remove any that don't belong.

      In the description, explain:
      - **Goal and rationale:** Feature chosen and why it matters
      - **Approach:** Strategy, methodology, and implementation steps
      - **Impact:** What changed and what was added or improved
      - **Validation:** Testing approach and success criteria met
      - **Future work:** Additional opportunities identified

      After creation, check the pull request to ensure it is correct, includes all expected files, and doesn't include any unwanted files or changes. Make any necessary corrections by pushing further commits to the branch.

5. **Final update**: Add brief comment (1 or 2 sentences) to the discussion identified at the start of the workflow stating goal worked on, PR links, and progress made.

6. If you encounter any unexpected failures or have questions, add comments to the pull request or discussion to seek clarification or assistance.

