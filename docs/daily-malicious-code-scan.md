# 🔍 Daily Malicious Code Scan

> For an overview of all available workflows, see the [main README](../README.md).

The **Daily Malicious Code Scan** workflow automatically reviews recent code changes for suspicious patterns that could indicate malicious activity, supply chain attacks, or unintended security regressions.

## What It Does

This workflow runs daily to analyze all code changes from the last three days:

- **Scans Recent Commits**: Examines every file changed in the past 72 hours
- **Detects Suspicious Patterns**: Searches for secret exfiltration, suspicious network calls, obfuscated code, out-of-context additions, and privilege escalation attempts
- **Creates Code Scanning Alerts**: Reports findings directly in GitHub's Security tab using native code-scanning alerts — visible to the whole team without cluttering the issue tracker
- **Assigns Threat Scores**: Rates each finding from 1–10 so teams can prioritize remediation

## Why It's Valuable

As AI-assisted code generation and automated commits become common, new attack surfaces emerge:

- A compromised dependency or agent could silently inject credential-harvesting code
- A supply chain attack could add out-of-context code (e.g., a crypto miner in a CLI tool)
- Obfuscated payloads can be missed in manual code review

The Daily Malicious Code Scan provides an automated second layer of defence that:

- **Catches subtle threats** that human reviewers may miss in fast-moving repositories
- **Integrates with GitHub Security** so findings appear alongside Dependabot and CodeQL alerts
- **Provides actionable context** — each alert explains *why* the code is suspicious and recommends next steps
- **Minimizes false positives** by looking for converging patterns rather than individual signals

## How It Works

1. **Daily Schedule**: Runs every day automatically
2. **History Fetch**: Retrieves the full git history to enable accurate diff analysis
3. **Change Identification**: Lists all files modified, added, or removed in the last 3 days
4. **Pattern Scanning**: Searches for:
   - Credentials accessed alongside external network calls (exfiltration)
   - Executable files or base64 payloads added to source directories
   - Access to sensitive system paths or privilege escalation primitives
   - Code obfuscation (hex/base64 strings, deliberately obscure variable names)
   - New dependencies or imports inconsistent with the project's purpose
5. **Contextual Analysis**: Cross-references findings with commit authors, PR descriptions, and repository purpose to reduce noise
6. **Alert Creation**: Publishes findings as GitHub code-scanning alerts with detailed descriptions and remediation steps

## Categories of Findings

| Category | Description |
|---|---|
| `secret-exfiltration` | Environment variable or credential access combined with outbound network calls |
| `out-of-context` | Files or dependencies that don't fit the project's established purpose |
| `suspicious-network` | Unusual or unauthorized network activity patterns |
| `system-access` | Suspicious system operations, sensitive file access, or privilege escalation |
| `obfuscation` | Base64/hex payloads, deliberately obscure naming, or encoded strings |
| `supply-chain` | Signs of dependency or toolchain compromise |

## Severity Levels

Findings are classified using GitHub's native code-scanning severity model:

- **error** (threat score 7–10): Requires immediate investigation
- **warning** (threat score 3–6): Warrants review before the next release
- **note** (threat score 1–2): Informational — review at your convenience

## What It Does Not Do

- It does **not** execute any code it finds — analysis only
- It does **not** modify the repository
- It does **not** block PRs or CI runs (findings are advisory)
- It does **not** replace dedicated SAST tools like CodeQL, but complements them with change-focused, context-aware analysis

## Getting Started

This workflow works out of the box with any repository and any programming language. No additional configuration is required.

Once enabled, findings appear in **Security → Code scanning alerts** in your repository.

## Learn More

- [GitHub Agentic Workflows Documentation](https://github.github.io/gh-aw/)
- [Blog: Security-related Workflows](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-security-compliance/)
- [GitHub Code Scanning Documentation](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)
