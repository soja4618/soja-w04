# SOJA W04 — Bounded Trace-Integrity Verifier

**Live Status** | [Health Check](https://soja-w04-public-beta.onrender.com/health) | [Offer Profile](https://soja-w04-public-beta.onrender.com/)

---

## What is W04?

A deterministic API that verifies bounded JSON evidence manifests for trace integrity. Built for autonomous agents that need machine-to-machine verification without human intervention, accounts, or API keys.

- **No LLM in the request path** — fully deterministic cryptographic verification
- **No account required** — callers retain full wallet custody
- **x402 v2 exact payment** — $0.01 USDC on Base mainnet per invocation

---

## Live Endpoint

```
POST https://soja-w04-public-beta.onrender.com/v1/verify
```

### Payment Profile (Fixed)

| Field | Value |
|-------|-------|
| Protocol | x402 v2 exact |
| Network | `eip155:8453` (Base mainnet) |
| Asset | USDC |
| Price | $0.01 per invocation |
| Pay to | `0x59faea25627eda8bb2be8feda62bde961a665a1d` |

---

## Unauthenticated Request (Returns x402 Challenge)

```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  -d '{
    "manifest": {
      "version": "2025-09-27",
      "traces": [...],
      "rules": [...]
    }
  }'
```

---

## Input Format

W04 accepts a bounded evidence manifest JSON structure:

```json
{
  "manifest": {
    "version": "<string>",
    "traces": [
      {"id": "<string>", "hash": "<sha256>"}
    ],
    "rules": [
      {"type": "integrity", "operator": "equals", "expected": "<sha256>"}
    ]
  }
}
```

### Limits

| Parameter | Maximum |
|-----------|---------|
| Body size | 1 MB |
| Rules count | 50 |
| Trace entries | 500 |
| Concurrent executions | 4 |

---

## Output Format

On successful verification, W04 returns structured results:

```json
{
  "status": "VERIFIED" | "NOT_VERIFIED",
  "details": { ... },
  "timestamp": "<ISO8601>"
}
```

---

## Machine-Readable Discovery

Download the full machine-readable manifest for agent crawlers:

📥 [w04-discovery.json](https://raw.githubusercontent.com/soja4618/soja-w04/main/w04-discovery.json)

---

## Evidence Manifest Template Pack

Learn by doing. Pre-made JSON templates demonstrating W04 verification patterns:
- `template-clean.json` — trace integrity passes all rules
- `template-modified.json` — one trace hash altered, fails integrity check
- `template-corrupted.json` — malformed structure, fails validation

📥 [Download Template Pack (ZIP)](https://github.com/soja4618/soja-w04/releases/latest)

---

## Status

Last verified: **2026-08-30**  
Health endpoint: `GET https://soja-w04-public-beta.onrender.com/health`

This page reflects the public, non-secret offer information only. No internal systems, credentials, or SOJA administrative access are exposed here.

---

## Contact / Issues

For technical questions or to report issues with W04, please open a GitHub issue in this repository.
