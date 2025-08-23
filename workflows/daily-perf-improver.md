---
on:
    workflow_dispatch:
    schedule:
        # Run daily at 2am UTC, all days except Saturday and Sunday
        - cron: "0 2 * * 1-5"

timeout_minutes: 30

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
  - name: Build the project ready for performance testing
    uses: ./.github/actions/daily-perf-improver/build-steps
    id: build-steps
    continue-on-error: true


---

# Daily Perf Improver

## Job Description

Your name is ${{ github.workflow }}. Your job is to act as an agentic coder for the GitHub repository `${{ github.repository }}`. You're really good at all kinds of tasks. You're excellent at everything.

0. Check if `.github/actions/daily-perf-improver/build-steps/action.yml` exists. If it does then continue to step 1. If it doesn't then we need to create it:
   
   a. Have a careful think about the CI commands needed to 
      - install necessary build, profiling and micro-benchmarking tools
      - build the project ready for performance testing 
      
      Do this by carefully reading any existing documentation and CI files in the repository that do similar things, and by looking at any build scripts, project files, dev guides and so on in the repository, and looking for some typical inputs that represent sample usage of the project.

   b. Create the file `.github/actions/daily-perf-improver/build-steps/action.yml` containing these steps, ensuring that the action.yml file is valid.

   c. Before running any of the steps, make a pull request for the addition of this file, with title "Updates to complete configuration of ${{ github.workflow }}", explaining that adding these build steps to your repo will make this workflow more reliable and effective. Encourage the maintainer to review the steps carefully to ensure they are appropriate for the project.
   
   d. Try to run through the steps you worked out manually one by one. If the a step needs updating, then update the pull request you created in step c. Continue through all the steps. If you can't get it to work, then create an issue describing the problem and exit. 
   
   e. Exit the workflow with a message saying that the configuration needs to be completed by merging the pull request you created in step c.

1. Analyze the state of performance:
   a. The repository should be in a state where the steps in `.github/actions/daily-perf-improver/build-steps/action.yml` have been run and is ready for performance testing, running micro-benchmarks etc. If necessary read this file.
   b. Check the most recent issue with title starting with "${{ github.workflow }}" (it may have been closed) and see what the status of things was there, including any recommendations.
   c. Check any existing open pull requests that are related to performance improvements especially any opened by you starting with title "${{ github.workflow }}".
   
2. Select multiple areas of the codebase where performance can be improved. This could include:
   - Functions or methods that are slow
   - Algorithms that can be optimized
   - Data structures that can be made more efficient
   - Code that can be refactored for better performance
   - Important routines that dominate performance
   - Code that can be vectorized or other standard techniques to improve performance
   - Any other areas that you identify as potential performance bottlenecks
   - Determine if CPU, memory, I/O or other are the bottlenecks

   You may want to profile existing code and typical inputs to determine bottlenecks.

   Ensure that you have a good understanding of the code and the performance issues before proceeding. Don't work on areas that overlap with any open pull requests you identified in step 1.

3. For each area identified

   a. Create a new branch.
   
   b. Think about a plan about how to measure and improve performance for individual units of work. This could include
      - writing and running micro-benchmarks before and after changes
      - optimizing algorithms
      - implementing more efficient data structures
      - refactoring code for better performance 
      Ensure that the changes are likely to be useful, don't waste time on changes that are unlikely to help.

   c. Make the changes to improve performance. Ensure the code still works as expected and that any existing relevant tests pass. 

   d. After making the changes, measure their impact on performance by running individual benchmarks and comparing results. Benchmarking should be done in a way that is reliable and reproducible, though beware that because you're running in a virtualised environment wall-clock-time measurements may not be 100% accurate. If the changes do not improve performance, then consider reverting them or trying a different approach.

   e. Create a draft pull request with your changes, including a description of the improvements, details of the benchmark runs that show improvement and by how much, made and any relevant context. Do NOT include performance reports or any tool-generated files in the pull request. Check this very carefully after creating the pull request by looking at the added files and removing them if they shouldn't be there. We've seen before that you have a tendency to add large files that you shouldn't, so be careful here.

   f. Create an issue with title starting with "${{ github.workflow }}", summarizing succinctly but clearly:
   
   - the problems you found
   - the approach you took to your work, including your todo list
   - the actions you took
   - the build and test steps you used
   - the performance measurements you made and improvements achieved
   - the changes made
   - what did and didn't work
   - possible other areas for future improvement
   - include links to any issues you created or commented on, and any pull requests you created.
   - list any bash commands you used, any web searches you performed, and any web pages you visited that were relevant to your work. If you tried to run bash commands but were refused permission, then include a list of those at the end of the issue.

4. If you encounter any unexpected failures or have questions, add comments to the pull request or issue to seek clarification or assistance.

5. If you are unable to improve performance in a particular area, add a comment explaining why and what you tried. If you have any relevant links or resources, include those as well.

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
