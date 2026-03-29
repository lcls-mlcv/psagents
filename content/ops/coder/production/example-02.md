# Dry-run integration vs S3DF paths

**Context:** Tool code often hard-codes roots; production uses shared filesystems and quotas.

## On S3DF (illustrative)

1. Locate a canonical read-only path your workflow is allowed to list (e.g. a public doc root).
2. Run `ls` or a language `os.listdir` against that path from the same account the agent will use.
3. Adjust your config so the tool takes that root as an explicit parameter.

## Take-away

Explicit parameters beat hidden globals when agents (or humans) must reproduce runs.

> **Dummy:** Do not scan arbitrary user directories; stay in allowed trees.
