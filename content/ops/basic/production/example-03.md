# ask-slurm-s3df — wrapping existing system tools

S3DF runs Slurm 24.11.3 across 200+ nodes with 7 partition types. Scientists struggle with job submission, pending reasons, GPU allocation, and fairshare.  The commands exist (`sinfo`, `squeue`, `sacctmgr`) -- but the output requires interpretation.

The tooling here is Slurm itself.  The SKILL file teaches the AI:

- Which commands always work vs. which need `slurmdbd` (and may fail):

  ```
  Always works          Needs slurmdbd (may fail)
  ────────────          ─────────────────────────
  sinfo                 sacctmgr
  squeue                sacct
  scontrol show         sshare
  sprio                 sreport
  ```

- What the output means (e.g., `AssocGrpNodeLimit` means the user's account has hit its allocation cap, not that the cluster is full)

- Partition specifications (7 partitions, their CPU/GPU models, memory, GRES names)

- Priority formula: `Priority = (QOS * 100K) + (FairShare * 10K) + (JobSize * 1K) + (Age * 100)`

A human can run `sinfo -p ampere -o "%N %G %T"` to check GPU availability.  The AI adds interpretation: it explains *why* your job is pending, suggests the right partition for your workload, and falls back gracefully when `slurmdbd` is temporarily down.

**Pattern: You don't always need to build new tools.  Sometimes the tools already exist -- you just need to write a man page that teaches the AI how to use them and interpret the output.**
