# Work Locks (Concurrency Control)

This folder defines a simple **pessimistic locking convention** for critical shared files.

The agentic-enterprise model prefers **additive artifacts** (new files) to avoid conflicts. For a small set of high-impact shared files, we use locks to prevent parallel edits.

## When to lock

Lock **before** modifying any of the following categories:
- Core operating model and company identity docs (e.g., `COMPANY.md`, `OPERATING-MODEL.md`, `AGENTS.md`, `CONFIG.yaml`)
- Quality policies (`org/4-quality/policies/*`)
- Global templates (`**/_TEMPLATE-*`), if the change affects multiple workflows
- Any other path your fork designates as protected

## Lock file format

A lock is a single Markdown file stored under:

`work/locks/<lock-id>.md`

Where `<lock-id>` is a stable slug derived from the protected path.

### Example
Locking `org/4-quality/policies/security.md`:

- Lock id: `org-4-quality-policies-security-md`
- Lock file: `work/locks/org-4-quality-policies-security-md.md`

## Lock file contents

Use this minimal structure:

- **Target:** the file/folder being locked
- **Owner:** GitHub handle (or agent id)
- **Reason:** why the lock is needed
- **Created:** timestamp
- **Expires:** timestamp (required) — locks must be time-bound
- **Related:** issue/PR links

## Acquire / release protocol

### Acquire
1. Create a branch.
2. Add the lock file.
3. Open a PR.
4. Merge the lock PR (or keep it as the first commit in a PR that includes the changes).
5. Only after the lock exists on `main`, proceed with the protected change.

### Release
- Remove the lock file in the same PR that completes the protected change, or in a follow-up PR.

## Stale locks

Locks must include an **Expires** timestamp.

- If a lock is expired, a new PR may remove it **with a short explanation** and proceed.
- If in doubt, escalate to `@wlfghdr` (or the repo owner).

## Notes

This convention is intentionally simple. If you need stronger enforcement, add a CI gate that:
- blocks PRs touching protected paths unless a corresponding lock file exists, or
- requires an exception record.
