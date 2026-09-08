# SOJA runtime control mirror

This directory is the scheduler-readable runtime mirror of SOJA's non-secret control documents.

The Obsidian vault remains the durable business brain. Hermes cron runs are intentionally sandboxed to their configured workspace, however, and cannot reliably traverse into the separate Obsidian path. The current scheduler must read and update the files in this directory so an unavailable vault mount never halts commercial execution.

Rules:

- Keep only non-secret operating records here: Soul, doctrine, commerce stack, Growth Board, browser queue, and topology.
- Do not store credentials, cookies, tokens, customer data, payment data, banking/tax data, or private session material.
- Before a material run, treat these files as the runtime authority.
- Record material work in `GROWTH_BOARD.md` and `BROWSER_ACTION_QUEUE.md` here. The next healthy Obsidian-capable maintenance pass syncs the result back to the vault.
- `quarantine/` contains stale, non-authoritative drafts that must not be published, staged, or used as source copy.
