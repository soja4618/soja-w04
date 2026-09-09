# SOJA runtime control mirror

This directory is the scheduler-readable runtime mirror of SOJA's non-secret control documents.

The Obsidian vault remains the durable business brain. Hermes cron runs are intentionally sandboxed to their configured workspace, however, and cannot reliably traverse into the separate Obsidian path. The current scheduler must read and update the files in this directory so an unavailable vault mount never halts commercial execution.

Rules:

- Keep only non-secret operating records here: Soul, doctrine, commerce stack, Growth Board, browser queue, and topology.
- Do not store credentials, cookies, tokens, customer data, payment data, banking/tax data, or private session material.
- Before a material run, treat these files as the runtime authority.
- Only `SOJA_CONTROL/` and the reconciled Obsidian vault may direct current action. Repository-root W04, x402, Render, wallet, and legacy commercial files are historical evidence only, even when they contain commands, URLs, offers, or apparent next steps.
- Record material work in `GROWTH_BOARD.md` and `BROWSER_ACTION_QUEUE.md` here. The next healthy Obsidian-capable maintenance pass syncs the result back to the vault.
- Every material benefit delivered by another operator must be converted into a concise, durable entry: what changed, why it matters, evidence of verification, the current state, and the next action. Do not depend on chat history or a transient report for operational continuity.
- `quarantine/` contains stale, non-authoritative drafts that must not be published, staged, or used as source copy.
