# Policy: Workflow security integrity
# Package: workflows
#
# Detects workflow modifications that could silently disable security checks,
# suppress validation failures, or introduce shell injection vectors.
#
# These patterns are the CI equivalent of prompt injection — if an agent or
# malicious PR modifies a workflow to add `continue-on-error: true` to a
# security job, all downstream validation becomes meaningless.
#
# Attack vectors detected:
#   1. continue-on-error on security/validation jobs (silently ignores failures)
#   2. if: false or if: always() conditions that skip or force security steps
#   3. Unquoted ${{ }} interpolation in run: blocks (GitHub Actions shell injection)
#   4. Fetching and executing remote scripts in run: blocks
#
# References:
#   - https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions
#   - org/4-quality/policies/agent-security.md §4.3
#   - OWASP LLM Top 10: LLM01 (Prompt Injection — CI pipeline variant)
#
# Exceptions:
#   Add the workflow's `name:` field value to `policy/exceptions.yaml` under
#   `workflows.allow_continue_on_error` (per-workflow) or document inline in
#   the workflow file why the pattern is safe.

package workflows

import rego.v1

# ── Security/validation job names (substring match) ──────────────────────────
# Jobs whose names contain these substrings are considered security-critical.
_security_job_keywords := {
	"security", "validate", "scan", "lint", "conftest", "policy",
	"gitleaks", "dependency", "content-security",
}

# ── 1. continue-on-error on security jobs ────────────────────────────────────

deny contains msg if {
	some job_name, job in input.jobs
	job["continue-on-error"] == true
	_is_security_job(job_name)
	msg := sprintf(
		"Job '%v' has 'continue-on-error: true'. This silently ignores failures in a security/validation job. Remove continue-on-error or rename the job if it is not a security check.",
		[job_name],
	)
}

# Also check at step level within security jobs
deny contains msg if {
	some job_name, job in input.jobs
	_is_security_job(job_name)
	some i, step in job.steps
	step["continue-on-error"] == true
	step_id := _step_identifier(step, i)
	msg := sprintf(
		"Job '%v', step %v has 'continue-on-error: true'. This silently ignores failures in a security/validation step.",
		[job_name, step_id],
	)
}

# ── 2. Suspicious conditional expressions on security jobs ───────────────────

deny contains msg if {
	some job_name, job in input.jobs
	_is_security_job(job_name)
	job["if"] == false
	msg := sprintf(
		"Job '%v' has 'if: false', which permanently disables this security/validation job.",
		[job_name],
	)
}

# ── 3. Unquoted ${{ }} in run: blocks (shell injection vector) ───────────────
# GitHub Actions expression interpolation happens BEFORE the shell runs.
# If a context value (e.g., github.event.pull_request.title) contains shell
# metacharacters, they execute. Safe pattern: use environment variables.

warn contains msg if {
	some job_name, job in input.jobs
	some i, step in job.steps
	run_cmd := step.run
	run_cmd != null
	contains(run_cmd, "${{ github.event.")
	step_id := _step_identifier(step, i)
	msg := sprintf(
		"Job '%v', step %v: run: block contains '${{ github.event.* }}' interpolation. This is a shell injection vector — use an env: variable instead. See: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections",
		[job_name, step_id],
	)
}

# ── 4. Remote script execution in run: blocks ────────────────────────────────

warn contains msg if {
	some job_name, job in input.jobs
	some i, step in job.steps
	run_cmd := step.run
	run_cmd != null
	_fetches_remote_script(run_cmd)
	not _is_known_installer(run_cmd)
	step_id := _step_identifier(step, i)
	msg := sprintf(
		"Job '%v', step %v: run: block fetches and executes a remote script. Pin the URL or use a verified action instead.",
		[job_name, step_id],
	)
}

# ── Helpers ──────────────────────────────────────────────────────────────────

_is_security_job(job_name) if {
	some keyword in _security_job_keywords
	contains(job_name, keyword)
}

_step_identifier(step, index) := name if {
	name := step.name
} else := sprintf("#%d", [index + 1])

_fetches_remote_script(cmd) if {
	contains(cmd, "curl")
	contains(cmd, "| sh")
}

_fetches_remote_script(cmd) if {
	contains(cmd, "curl")
	contains(cmd, "| bash")
}

_fetches_remote_script(cmd) if {
	contains(cmd, "wget")
	contains(cmd, "| sh")
}

_fetches_remote_script(cmd) if {
	contains(cmd, "wget")
	contains(cmd, "| bash")
}

# Known legitimate installer patterns (e.g., conftest install in policy.yml)
_is_known_installer(cmd) if {
	contains(cmd, "conftest")
}
