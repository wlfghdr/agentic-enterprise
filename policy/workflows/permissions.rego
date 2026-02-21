# Policy: Workflow top-level permissions
# Package: workflows
#
# All GitHub Actions workflow files must declare a top-level `permissions` block.
# Explicit permissions limit the GITHUB_TOKEN scope and prevent privilege escalation
# if a workflow step or dependency is compromised.
#
# References:
#   https://docs.github.com/en/actions/security-guides/automatic-token-authentication
#   https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions
#
# Exceptions:
#   Add the workflow's `name:` field value to `policy/exceptions.yaml` under
#   `workflows.allow_missing_permissions`.

package workflows

import rego.v1

# Load exception list from policy/exceptions.yaml (via --data flag)
_permission_exceptions := data.exceptions.workflows.allow_missing_permissions

deny contains msg if {
	not input.permissions
	not _permission_exception_applies
	msg := sprintf(
		"Workflow '%v' is missing a top-level 'permissions' block. Add 'permissions: {}' for least-privilege read-only access, or declare specific permissions. See: https://docs.github.com/en/actions/security-guides/automatic-token-authentication",
		[input["name"]],
	)
}

_permission_exception_applies if {
	some exception in _permission_exceptions
	exception == input["name"]
}
