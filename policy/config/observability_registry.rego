# Policy: Observability registry structure
# Package: config
#
# Enforces the minimum structure of the observability integration registry in
# CONFIG.yaml. This does not prove runtime telemetry exists; it ensures the
# registry shape is compatible with the framework's observability-first stance.

package config

import rego.v1

_entries := object.get(object.get(input, "integrations", {}), "observability", [])
_valid_connections := {"opentelemetry", "native-agent", "api"}
_required_otel_capabilities := {"metrics", "traces", "logs"}

deny contains msg if {
	count(_entries) == 0
	msg := "CONFIG.yaml must declare at least one observability integration entry."
}

deny contains msg if {
	some i
	entry := _entries[i]
	object.get(entry, "id", "") == ""
	msg := sprintf(
		"CONFIG.yaml integrations.observability[%d] must declare a non-empty id.",
		[i],
	)
}

deny contains msg if {
	ids := [object.get(entry, "id", "") |
		some i
		entry := _entries[i]
		object.get(entry, "id", "") != ""
	]
	count(ids) != count({id | id := ids[_]})
	msg := "CONFIG.yaml observability integration ids must be unique."
}

deny contains msg if {
	some i
	entry := _entries[i]
	connection := object.get(entry, "connection", "")
	not _valid_connections[connection]
	msg := sprintf(
		"CONFIG.yaml integrations.observability[%d].connection %q is invalid. Allowed values: opentelemetry, native-agent, api.",
		[i, connection],
	)
}

deny contains msg if {
	some i
	entry := _entries[i]
	object.get(entry, "connection", "") == "opentelemetry"
	capabilities := {cap |
		some j
		cap := object.get(entry, "capabilities", [])[j]
	}
	missing := _required_otel_capabilities - capabilities
	count(missing) > 0
	msg := sprintf(
		"CONFIG.yaml integrations.observability[%d] uses 'opentelemetry' and must declare metrics, traces, and logs capabilities.",
		[i],
	)
}
