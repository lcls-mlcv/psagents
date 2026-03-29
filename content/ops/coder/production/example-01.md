# Read-only probe on S3DF

**Context:** Code that will host an agent should be validated where it will run.

## On S3DF (illustrative)

1. SSH to your S3DF environment per site instructions.
2. Confirm interpreter version and that a read-only CLI you need is on `PATH`.
3. Run a one-liner that prints environment markers only (hostname, cwd)—no secrets.

## Take-away

“Works on my laptop” ≠ “works on S3DF”; bake environment checks into your harness.

> **Dummy:** Follow authentication and data-handling policies for your lab.
