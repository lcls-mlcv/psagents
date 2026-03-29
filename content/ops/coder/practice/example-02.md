# Logging around tool calls

**Goal:** Every tool invocation should leave an audit line.

## Steps (local)

1. Wrap one function so it logs timestamp, tool name, and argument **keys** (not secrets).
2. Force one failure (bad input) and confirm the log line still appears.
3. Redact one field that must never appear in logs.

## What you are practicing

Patterns you will need before giving an agent write access anywhere.
