# Trace one workflow on S3DF

**Context:** Builders need to see how a pipeline behaves with real paths and permissions.

## On S3DF (illustrative)

1. Identify one automation or script your group runs on S3DF (read-only inspection).
2. Map its steps to Intake / Retrieve / Decide / Execute / Verify.
3. Note one failure mode (e.g. missing file) and what the script does today.

## Take-away

Production workflows already encode policy; your job is to **preserve** that policy when adding agents.

> **Dummy:** Do not modify production cron or shared pipelines without owners.
