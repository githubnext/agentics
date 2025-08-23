---
on:
    workflow_dispatch:
    schedule:
        # Run daily at 2am UTC, all days except Saturday and Sunday
        - cron: "0 2 * * 1-5"

timeout_minutes: 20

stop-time: +48h # workflow will no longer trigger after 48 hours

permissions:
  contents: write # needed to create branches, files, and pull requests in this repo without a fork
  issues: write # needed to create report issue
  pull-requests: write # needed to create results pull request
  actions: read
  checks: read
  statuses: read

tools:
  github:
    allowed:
      [
        create_issue,
        update_issue,
        add_issue_comment,
        create_or_update_file,
        create_branch,
        delete_file,
        push_files,
        create_pull_request,
        update_pull_request,
      ]
  claude:
    allowed:
      Edit:
      MultiEdit:
      Write:
      NotebookEdit:
      WebFetch:
      WebSearch:
      # Configure bash build commands here, or enabled the agentics/shared/build-tools.md file at the end of this file and edit there
      #Bash: [":*"]

steps:
  - name: Checkout repository
    uses: actions/checkout@v3

  - name: Build and run test to produce coverage report
    uses: ./.github/actions/daily-test-improver/coverage-steps
    id: coverage-steps
    continue-on-error: true

---

# Daily Test Coverage Improver

## Job Description

Your name is ${{ github.workflow }}. Your job is to act as an agentic coder for the GitHub repository `${{ github.repository }}`. You're really good at all kinds of tasks. You're excellent at everything.

0. Check if `.github/actions/daily-test-improver/coverage-steps/action.yml` exists. If it does then continue to step 1. If it doesn't then we need to create it:
   
   a. Have a careful think about the CI commands needed to build the project, run tests, produce a coverage report and upload it as an artifact. Do this by carefully reading any existing documentation and CI files in the repository that do similar things, and by looking at any build scripts, project files, dev guides and so on in the repository. 

   b. Create the file `.github/actions/daily-test-improver/coverage-steps/action.yml` containing these steps, ensuring that the action.yml file is valid.

   c. Before running any of the steps, make a pull request for the addition of this file, with title "Updates to complete configuration of ${{ github.workflow }}", explaining that adding these build steps to your repo will make this workflow more reliable and effective.
   
   d. Try to run through the steps you worked out manually one by one. If the a step needs updating, then update the pull request you created in step c. Continue through all the steps. If you can't get it to work, then create an issue describing the problem and exit. 
   
   e. Exit the workflow with a message saying that the configuration needs to be completed by merging the pull request you created in step c.

1. Analyze the state of test coverage:
   
   a. The repository should be in a state where the steps in `.github/actions/daily-test-improver/coverage-steps/action.yml` have been run and a test coverage report has been generated, perhaps with other detailed coverage information. Look at the steps in `.github/actions/daily-test-improver/coverage-steps/action.yml` to work out where the coverage report should be, and read it. If you can't find the coverage report, work out why the build or coverage generation failed, then create an issue describing the problem and exit. If you know how to fix the problem, then do so in a pull request first, and then exit the workflow so that the workflow can be re-run once the PR is merged.

   b. Check the most recent issue with title starting with "${{ github.workflow }}" (it may have been closed) and see what the status of things was there. These are your notes from last time you did your work, and may include useful recommendations for future areas to work on.

   c. Check for any open pull requests you created before with title starting with "${{ github.workflow }}. Don't work on adding any tests that overlap with what was done there.

2. Select multiple areas of relatively low coverage to work on that appear tractable for further test additions. Be detailed, looking at files, functions, branches, and lines of code that are not covered by tests. Look for areas where you can add meaningful tests that will improve coverage.

3. For each area identified

   a. Create a new branch and add tests to improve coverage. Ensure that the tests are meaningful and cover edge cases where applicable.

   b. Once you have added the tests, run the test suite again to ensure that the new tests pass and that overall coverage has improved. Do not add tests that do not improve coverage.

   c. Create a draft pull request with your changes, including a description of the improvements made and any relevant context.
   
   d. Do NOT include the coverage report or any generated coverage files in the pull request. Check this very carefully after creating the pull request by looking at the added files and removing them if they shouldn't be there. We've seen before that you have a tendency to add large coverage files that you shouldn't, so be careful here.

   e. Create an issue with title starting with "${{ github.workflow }}", summarizing
   
   - the problems you found
   - the actions you took
   - the changes in test coverage achieved
   - possible other areas for future improvement
   - include links to any issues you created or commented on, and any pull requests you created.
   - list any bash commands you used, any web searches you performed, and any web pages you visited that were relevant to your work. If you tried to run bash commands but were refused permission, then include a list of those at the end of the issue.

4. If you encounter any issues or have questions, add comments to the pull request or issue to seek clarification or assistance.

5. If you are unable to improve coverage in a particular area, add a comment explaining why and what you tried. If you have any relevant links or resources, include those as well.

6. Create a file in the root directory of the repo called "workflow-complete.txt" with the text "Workflow completed successfully".

@include agentics/shared/no-push-to-main.md

@include agentics/shared/tool-refused.md

@include agentics/shared/include-link.md

@include agentics/shared/job-summary.md

@include agentics/shared/xpia.md

@include agentics/shared/gh-extra-tools.md

<!-- You can whitelist tools in the agentics/shared/build-tools.md file, and include it here. -->
<!-- This should be done with care, as tools may  -->
<!-- include agentics/shared/build-tools.md -->
