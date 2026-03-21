# GitHub Issue Backend Setup Checklist

Use this checklist when instantiating the GitHub issue backend in a company fork.

It covers both supported shapes:

- same-repo issue backend
- dedicated work-repo issue backend

For the full operating model, combine this checklist with [`../github-issues.md`](../github-issues.md), [`../required-github-settings.md`](../required-github-settings.md), and [`../work-backends.md`](../work-backends.md).

---

## 1. Decide The Repo Shape

Choose one of these profiles:

### Profile A: Same Repo

Use the operating-model repository itself for GitHub Issues.

- `work_backend.github_issues.repo: ""`
- issue forms live in the main repo
- Project, labels, and issue coordination all happen in the main repo
- best when you want the simplest setup

### Profile B: Dedicated Work Repo

Use a separate repository such as `acme/operating-work` only for issue-backed coordination.

- `work_backend.github_issues.repo: "acme/operating-work"`
- issue forms, labels, and Project live in the work repo
- the full framework and governance backbone stay in the main operating-model repo
- best when you want a cleaner human-facing work surface

---

## 2. Configure `CONFIG.yaml`

Set:

```yaml
work_backend:
  type: "github-issues"

  github_issues:
    repo: ""
    use_projects: true
    project_owner: ""
    project_number: 0
    use_label_prefixes: true
```

If you use a dedicated work repo, set `repo` to that repository.

---

## 3. Copy The Template Assets

Copy these files into the repository that will host the issues:

- `docs/github/issue-templates/config.sample.yml` -> `.github/ISSUE_TEMPLATE/config.yml`
- `docs/github/issue-templates/forms/*.sample.yml` -> `.github/ISSUE_TEMPLATE/*.yml`

Optional but recommended:

- `docs/github/labels/labels.sample.yml` -> your label bootstrap process
- `docs/github/workflows/validate-issue-templates.yml` -> `.github/workflows/validate-issue-templates.yml`
- `docs/github/workflows/sync-issue-form-labels.yml` -> `.github/workflows/sync-issue-form-labels.yml`

---

## 4. Enable GitHub Features

In the issue-hosting repository:

- enable `Issues`
- enable `Issue Forms`

If branch protection is used there too, require only the checks that repo actually runs.

---

## 5. Create The Labels

Minimum required label families:

- `artifact:*`
- `layer:*`
- `loop:*`
- `priority:*`

Recommended additional label families:

- `urgency:*`
- `category:*`
- `confidence:*`
- `division:*` based on your configured divisions

Do not create `status:*` labels.
Status belongs in the GitHub Project `Status` field.

---

## 6. Create The Project

Create a GitHub Project v2 and define a single-select `Status` field with:

- `Backlog`
- `Triage`
- `Approved`
- `Planning`
- `In Progress`
- `Blocked`
- `Done`

Then add the issue-hosting repository to that Project and set:

- `project_owner`
- `project_number`

in `CONFIG.yaml`.

---

## 7. Understand What Templates Do And Do Not Enforce

Issue Forms enforce:

- issue structure
- required fields
- base labels defined statically in the form file

Issue Forms do not automatically enforce:

- dynamic labels such as `priority:*`, `category:*`, `confidence:*`, `urgency:*`
- Project `Status`
- division-specific labels

To close that gap:

- create labels up front
- use the Project `Status` field for workflow state
- optionally install `sync-issue-form-labels.yml` to map form answers to labels

---

## 8. CI Guidance

### Main operating-model repo

Keep the full framework validation there:

- structure checks
- markdown/link checks
- schema/config checks
- policy/security checks

### Dedicated work repo

Keep CI intentionally slim.
Usually enough:

- validate issue-template YAML
- validate repo-local GitHub automation

Do not copy the full framework CI into the work repo unless that repo actually stores the framework files those checks validate.
