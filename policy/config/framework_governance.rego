# Policy: Template config governance invariants
# Package: config
#
# Enforces structural CONFIG.yaml invariants that define how the template itself
# is governed. These rules are safe at template level because they should hold in
# both the public framework and serious downstream forks.

package config

import rego.v1

_valid_work_backends := {"git-files", "github-issues"}
_required_git_overrides := {"technical-design", "governance-exception", "asset-registry"}

deny contains msg if {
	not regex.match("^[0-9]+\\.[0-9]+\\.[0-9]+$", object.get(input, "framework_version", ""))
	msg := "CONFIG.yaml framework_version must use semantic versioning (MAJOR.MINOR.PATCH)."
}

deny contains msg if {
	backend := object.get(object.get(input, "work_backend", {}), "type", "")
	not _valid_work_backends[backend]
	msg := sprintf(
		"CONFIG.yaml work_backend.type %q is invalid. Allowed values: git-files, github-issues.",
		[backend],
	)
}

deny contains msg if {
	some key in _required_git_overrides
	overrides := object.get(object.get(input, "work_backend", {}), "overrides", {})
	object.get(overrides, key, "") != "git-files"
	msg := sprintf(
		"CONFIG.yaml work_backend.overrides.%s must be 'git-files' because that artifact remains governance-critical.",
		[key],
	)
}
