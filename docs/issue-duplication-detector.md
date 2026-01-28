1. # 🔁 Issue Duplication Detector
2. 
3. > For an overview of all available workflows, see the [main README](../README.md).
4. 
5. The [Issue Duplication Detector workflow](../.github/workflows/issue-duplication-detector.md?plain=1) automatically scans for newly created or recently updated issues every 5 minutes and flags likely duplicates with a helpful comment.
6. 
7. ## Installation
8. 
9. ```bash
10. # Install the 'gh aw' extension
11. gh extension install githubnext/gh-aw
12. 
13. # Add the Issue Duplication Detector workflow to your repository
14. gh aw add githubnext/agentics/issue-duplication-detector --pr
15. ```
16. 
17. This creates a pull request to add the workflow to your repository.
18. 
19. You must also [choose a coding agent](https://githubnext.github.io/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.
20. 
21. After merging the PR and syncing to main, you can run the workflow manually if desired:
22. 
23. ```bash
24. gh aw run issue-duplication-detector
25. ```
26. 
27. ## Configuration
28. 
29. This workflow works out of the box. You can customize detection strictness, comment tone, or batching window via a local config file at `.github/workflows/agentics/issue-duplication-detector.config.md`.
30. 
31. After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.
32. 
33. ## What it reads from GitHub
34. 
35. - Repository issues (open and closed)
36. - Recent issues created or updated in the last 10 minutes
37. 
38. ## What it creates
39. 
40. - Adds comments to issues that appear to be duplicates, including links to the matching issues
41. - Requires `issues: write` permission
42. 
43. ## Human in the loop
44. 
45. - Review duplicate comments for accuracy and tone
46. - Close or link issues as appropriate
47. - Disable or uninstall the workflow if it is not valuable
48. 
49. ## Activity duration
50. 
51. - By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
52. - This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
