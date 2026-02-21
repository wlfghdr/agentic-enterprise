# Policy: Pinned external action references
# Package: workflows
#
# External GitHub Actions (uses: owner/repo@ref) must be pinned to a specific
# version tag or commit SHA. Using floating refs like @main, @master, or @latest
# allows arbitrary code changes to be silently pulled into CI — a supply-chain
# attack vector.
#
# Good:  uses: actions/checkout@v4
# Good:  uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  (SHA pin)
# Bad:   uses: actions/checkout@main
# Bad:   uses: actions/checkout@latest
#
# Local composite actions (uses: ./...) are exempt.
#
# Exceptions:
#   Add the full action ref (e.g., "myorg/myaction@main") to
#   `policy/exceptions.yaml` under `workflows.allow_unpinned_actions`.

package workflows

import rego.v1

_unpinned_suffixes := {"@main", "@master", "@latest"}

_pinned_exceptions := data.exceptions.workflows.allow_unpinned_actions

deny contains msg if {
	some job_name, job in input.jobs
	some step in job.steps
	uses := step.uses
	not startswith(uses, "./") # local composite actions are exempt
	some suffix in _unpinned_suffixes
	endswith(uses, suffix)
	not _pinned_exception_applies(uses)
	msg := sprintf(
		"Job '%v': action '%v' uses a floating ref ('%v'). Pin to a specific tag (e.g., @v4) or a full commit SHA to prevent supply-chain attacks.",
		[job_name, uses, suffix],
	)
}

_pinned_exception_applies(uses) if {
	some exception in _pinned_exceptions
	exception == uses
}
