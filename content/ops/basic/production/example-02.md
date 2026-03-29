# elog-copilot — cron pipeline meets AI

LCLS experiment metadata -- runs, detectors, sample configurations, logbook entries -- lives behind a Kerberos-authenticated web API. Scientists need to query it, but the API is not designed for ad-hoc analysis.

The tooling solution:

```
Confluence/eLog API                     AI skill
       │                                    │
  ┌────▼────┐    every 6 hours    ┌─────────▼─────────┐
  │ elogfetch├───────────────────►│  SQLite database   │
  │ (cron)   │                    │  (~1.3 GB)         │
  └──────────┘                    │                    │
                                  │  9 tables:         │
                                  │  Experiment        │
                                  │  Run               │
                                  │  Detector          │
                                  │  Logbook           │
                                  │  Questionnaire     │
                                  │  ...               │
                                  └─────────┬──────────┘
                                            │
                                       sqlite3 CLI
                                            │
                                     ┌──────▼──────┐
                                     │ Human    or │
                                     │ AI agent    │
                                     └─────────────┘
```

The SKILL file teaches the AI the schema, domain conventions (LCLS run numbers, experiment naming, questionnaire categories), and safety rules (never SELECT full logbook content with inline base64 images -- use `LENGTH()` and `SUBSTR()` to inspect first).

A human can query the same database directly:

```
$ sqlite3 /path/to/elog-copilot.db \
    "SELECT experiment_id, instrument, pi FROM Experiment
     WHERE instrument = 'mfx' ORDER BY start_time DESC LIMIT 5"
```

The AI adds the ability to ask "What detectors were used in recent MFX experiments with protein crystallography samples?" and get back a well-formed SQL query, executed and interpreted.  But the database, the cron job, and the CLI tool exist independently of the AI.

**Pattern: Build a data pipeline (cron + database) that makes information queryable.  The AI becomes a natural language interface to data that humans can also query directly.**
