# SOJA operator topology

Effective: 2026-09-07.

## Hermes/SOJA CLI — continuous execution plane

Owns local research, product creation, code, documents, QA, Git operations, release preparation, public HTTP checks, snapshots, metrics ledgers, Obsidian memory, opportunity ranking, local-model routing, and scheduled work. It operates every 45 minutes from the current controlling Soul and Growth Board with run-to-run prompt continuity disabled, preventing stale outputs from becoming instructions.

It uses the clean release workspace at `/Users/soja/Documents/Codex/SOJA_RELEASE/evidence-manifest-storefront`, never the dirty historical checkout, for production GitHub/Netlify work.

## Codex browser operator — authenticated UI plane

Owns authenticated visual verification and bounded browser-only actions for Netlify, Gumroad, GitHub, and other approved commercial services. It reads and updates `05_COMMERCIAL/SOJA_BROWSER_ACTION_QUEUE.md` on its recurring cycle.

The browser operator does not access or transfer credentials, cookies, tokens, payment data, customer personal information, banking/tax information, or session internals. It honors confirmation requirements for external side effects.

## Handoff rule

CLI work should never stop merely because a browser task exists. SOJA writes a decision-ready queue item, continues the next safe CLI action, and consumes the browser result from Obsidian on a later cycle.

Browser work should never alter the CLI source of truth silently. Every material result is recorded in the queue and operational memory.

## Model plane

- Primary operator: `qwen3.5:27b` until a challenger passes the local acceptance gate.
- Fast fallback/triage: `qwen3.5:9b`.
- Bounded drafting/implementation: `gemma4:26b`.
- Independent challenge: `qwen3.8:27b-q4_K_M`.
- Difficult, latency-tolerant secondary reasoning: `deepseek-r1:32b`.
- Nemotron 3 Nano 4B: installed and registered as a controlled lightweight worker for low-consequence extraction, classification, triage, candidate generation, and first-pass checks. Its initial decisions were correct, but strict-output testing exposed a verbose reasoning trace; deterministic validation remains mandatory. It does not become the primary operator until measured local results pass the gate.
- Nemotron 3 Nano 30B A3B Q4: later benchmark candidate, not installed; its approximately 24 GB artifact leaves limited headroom on the 32 GiB host.
