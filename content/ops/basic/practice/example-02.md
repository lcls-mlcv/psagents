# Wrap a CLI in a shell function

**Goal:** Isolate environment and arguments for a command you run often.

## Steps (local)

1. Pick any CLI you use repeatedly (e.g. `python`, `kubectl`, a facility wrapper).
2. Add a shell function or alias that sets `PATH` or fixed flags.
3. Open a new terminal and confirm the wrapper behaves the same every time.

## What you are practicing

- Moving “how to run this safely” into **tooling** instead of memory.
- A pattern that transfers directly to agents that shell out to the same CLI.

Dummy exercise; adapt names to your environment.
