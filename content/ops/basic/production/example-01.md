# docs-index — one tool, many skills

`docs-index` is a 360-line Python script that indexes documentation collections into SQLite FTS5 databases and searches them with BM25 ranking.

```
$ docs-index index /path/to/docs --incremental
Indexed 847 files (23 new, 12 updated, 3 removed)

$ docs-index search /path/to/docs "batch job submission"
Score   File
─────   ────────────────────────────────
-8.23   docs/batch-compute.md
-7.41   docs/slurm-basics.md
-6.89   docs/gpu-jobs.md
```

This single tool powers multiple AI skills:

```
docs-index
    │
    ├── ask-s3df skill      (S3DF facility docs, daily cron sync)
    ├── ask-olcf skill      (OLCF facility docs, weekly cron sync)
    └── docs-search skill   (any doc collection, on-demand)
```

Each skill's SKILL file teaches the AI when to use `docs-index search` versus `grep` versus reading files directly:

> Use `docs-index search` for **discovery**, then `Read` the top results. Use `Grep` when you need **precision** on a known pattern.

A human can run the same commands.  The AI adds convenience (natural language queries) and judgment (choosing the right search strategy).  But the tool works without the AI.

**Pattern: Build a general-purpose tool.  Write SKILL files to teach the AI how to use it in different contexts.  The tool compounds in value as you add more skills.**
