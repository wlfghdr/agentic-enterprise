# Missions

Active and completed missions. Each mission gets its own folder.

## How to Create a Mission

1. A signal must be validated through the Discover loop first
2. Use the template: `work/missions/_TEMPLATE-mission-brief.md`
3. Create a folder: `<mission-name>/`
4. Add `BRIEF.md` and `OUTCOME-CONTRACT.md` to the folder
5. Submit as a Pull Request for Strategy Layer approval

## Mission Structure

```
missions/
└── <mission-name>/
    ├── BRIEF.md                 # Mission brief (from template)
    ├── OUTCOME-CONTRACT.md    # Measurable success criteria
    ├── STATUS.md                # Progress updates (append-only, latest first)
    ├── OUTCOME-REPORT.md        # Final outcome measurement (mission closure)
    └── evaluations/             # Quality evaluation reports
        └── YYYY-MM-DD-<eval>.md # Individual quality evaluations
```

## Mission Statuses

| Status | Meaning |
|--------|---------|
| **proposed** | Brief created, awaiting approval |
| **approved** | Approved by Strategy Layer, ready for Build loop |
| **active** | Currently being executed |
| **paused** | Temporarily suspended |
| **completed** | Outcomes measured, mission closed |
