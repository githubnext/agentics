# 🚀 CI Coach

**Automated CI/CD optimization expert that analyzes your GitHub Actions workflows and proposes efficiency improvements**

## What It Does

CI Coach is your personal CI/CD optimization consultant. It runs daily to:

1. **Analyzes all GitHub Actions workflows** in your repository
2. **Collects performance metrics** from recent workflow runs
3. **Identifies optimization opportunities** using proven patterns
4. **Proposes concrete improvements** through pull requests
5. **Estimates time and cost savings** for each optimization

Think of it as a tireless performance engineer who reviews your CI pipelines every day, looking for ways to make them faster and cheaper.

## Why It's Valuable

### Universal Problem, Universal Solution

Every repository with GitHub Actions can benefit from CI optimization:

- **Faster feedback loops** → Developers get test results sooner
- **Lower costs** → Reduced GitHub Actions minutes consumption
- **Better resource utilization** → Optimal use of runner resources
- **Improved developer experience** → Less time waiting for CI

### Proven Track Record

From Peli's Agent Factory:
> "CI Optimization Coach has contributed **9 merged PRs out of 9 proposed (100% merge rate)**, optimizing CI pipelines for speed and efficiency with perfect execution."

Examples of improvements made:
- [Removing unnecessary test dependencies](https://github.com/github/gh-aw/pull/13925)
- [Fixing duplicate test execution](https://github.com/github/gh-aw/pull/8176)

## How It Works

### Daily Analysis Cycle

````mermaid
graph LR
    A[Find Workflows] --> B[Collect Metrics]
    B --> C[Analyze Performance]
    C --> D{Improvements<br/>Found?}
    D -->|Yes| E[Create PR]
    D -->|No| F[Report: All Good]
````

### What It Analyzes

1. **Job Parallelization**
   - Are independent jobs running in parallel?
   - Can the critical path be shortened?
   - Are matrix jobs balanced?

2. **Caching Strategy**
   - Are dependencies cached effectively?
   - What's the cache hit rate?
   - Can cache keys be optimized?

3. **Test Distribution**
   - Is test execution balanced?
   - Can tests run in parallel?
   - Are slow tests identified?

4. **Resource Allocation**
   - Are timeouts appropriate?
   - Are runner types optimal?
   - Are jobs sized correctly?

5. **Artifact Management**
   - Are artifacts necessary?
   - Can sizes be reduced?
   - Are retention periods optimal?

6. **Conditional Execution**
   - Can jobs skip when not needed?
   - Are path filters used effectively?

### Sample Optimizations

**Before: Sequential Execution**
```yaml
test:
  needs: [build]
  runs-on: ubuntu-latest
  
lint:
  needs: [test]  # Waits for test to finish
  runs-on: ubuntu-latest
```

**After: Parallel Execution**
```yaml
test:
  needs: [build]
  runs-on: ubuntu-latest
  
lint:
  needs: [build]  # Runs in parallel with test
  runs-on: ubuntu-latest
```

**Impact**: 5 minutes saved per run (if lint takes 5 minutes)

## What You Get

### Pull Requests with Clear Value

Each PR includes:

- **Summary** of what's being optimized
- **Detailed analysis** with metrics and data
- **Expected impact** (time savings, cost reduction)
- **Risk assessment** (low/medium/high)
- **Testing recommendations**

### Evidence-Based Recommendations

All suggestions are backed by:
- Actual workflow run data
- Performance metrics
- Before/after comparisons
- Cost/benefit analysis

### Safe, Surgical Changes

CI Coach follows strict quality standards:
- ✅ Minimal, focused changes
- ✅ Low-risk optimizations prioritized
- ✅ Clear documentation
- ✅ Easy to review and rollback
- ❌ Never breaks test integrity
- ❌ Never sacrifices correctness for speed

## Configuration

### Basic Setup

The workflow runs daily by default:

```yaml
on:
  schedule:
    - cron: daily
```

### Customization

You can customize the behavior by editing the workflow file:

1. **Change schedule**: Modify the `cron` expression
2. **Adjust timeout**: Change `timeout-minutes` if analysis takes longer
3. **Modify PR expiration**: Adjust `expires` in safe-outputs

### Manual Trigger

You can also trigger the analysis manually:

```bash
gh workflow run ci-coach.md
```

## Use Cases

### 1. Growing Repositories

As your codebase grows, CI times naturally increase. CI Coach continuously monitors and optimizes to keep pipelines fast.

**Example**: Split monolithic test job into parallel matrix jobs as test count grows.

### 2. Cost-Conscious Teams

GitHub Actions minutes cost money. CI Coach finds opportunities to reduce runtime and save costs.

**Example**: Add dependency caching to eliminate repeated downloads (5-10 minute savings per run).

### 3. Fast-Moving Teams

Frequent commits mean CI runs constantly. Every minute saved multiplies across hundreds of runs.

**Example**: Enable parallel job execution to reduce critical path by 40%.

### 4. Multi-Language Projects

Different languages have different CI optimization patterns. CI Coach learns from your specific setup.

**Example**: Optimize build caching for npm, pip, and maven in the same repository.

## What It Won't Do

### Maintains Quality

CI Coach has strict rules to protect test integrity:

- ❌ Never modifies test code to hide failures
- ❌ Never suppresses error output
- ❌ Never makes failing tests appear to pass
- ❌ Never sacrifices correctness for speed

### Respects Your Decisions

CI Coach is advisory only:

- It **proposes** optimizations via PR
- You **review and approve** before merging
- All changes are **documented and reversible**
- You remain **in full control**

### Focuses on High-Value Work

CI Coach won't create noise:

- Only proposes changes with significant impact (>2% improvement)
- Skips if no meaningful optimizations found
- Prioritizes low-risk, high-value changes
- Creates at most one PR per run

## Real-World Impact

### Time Savings Example

A typical repository might see:
- **5-10 minutes** per CI run saved
- **50+ runs** per month
- **250-500 minutes** saved monthly
- **~8 hours** of developer waiting time eliminated

### Cost Savings Example

For a repository running CI 200 times/month:
- **Before**: 15 minutes/run = 3,000 minutes/month
- **After**: 10 minutes/run = 2,000 minutes/month
- **Savings**: 1,000 minutes/month

At GitHub Actions pricing, this saves real money while improving developer experience.

## Getting Started

1. **Add the workflow** to your repository (already done if you're reading this!)

2. **Wait for the first run** (runs daily automatically)

3. **Review any PRs** created by CI Coach

4. **Merge if beneficial**, or close with feedback

5. **Monitor impact** by comparing workflow run times before/after

## Tips for Best Results

### Provide Context

If CI Coach suggests something that doesn't fit your use case, close the PR with a comment explaining why. The agent learns from feedback.

### Review Thoroughly

While CI Coach has a perfect merge rate in its home repository, every repo is different. Always review proposed changes carefully.

### Start Small

Merge one optimization at a time, monitor the impact, then proceed with the next one.

### Share Feedback

If CI Coach misses an optimization opportunity or suggests something inappropriate, that's valuable feedback for improving the system.

## Comparison to Other Approaches

### vs. Manual Optimization

- **Manual**: Requires dedicated time, easily forgotten
- **CI Coach**: Continuous monitoring, never forgets

### vs. Third-Party CI Tools

- **Third-party**: Additional service, data leaves GitHub
- **CI Coach**: Native GitHub Actions, all data stays in your repo

### vs. Static Analysis

- **Static**: One-time snapshot
- **CI Coach**: Adapts as your repository evolves

## Troubleshooting

### No PRs Created

This is normal! It means your CI is already well-optimized. CI Coach only creates PRs when it finds significant improvements.

### PR Suggests Unwanted Change

Close the PR with a comment explaining why the change isn't appropriate. This helps document your CI design decisions.

### Analysis Timeout

If the workflow times out, increase `timeout-minutes` in the workflow configuration.

## Learn More

- [CI Coach source workflow](https://github.com/github/gh-aw/blob/main/.github/workflows/ci-coach.md)
- [GitHub Actions best practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Optimizing GitHub Actions workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)

---

**Remember**: CI Coach is your optimization consultant, not a mandate. Review its suggestions, merge what makes sense, and enjoy faster, cheaper CI pipelines!
