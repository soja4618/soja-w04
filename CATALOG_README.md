# SOJA Service Catalog

**Version:** 1.0.0  
**Published:** 2026-08-30  
**Machine-Readable Format:** [JSON](./soja_service_catalog.json)  

---

## Overview

SOJA operates agent-to-agent verification services and complementary digital products. This catalog is designed for discovery by both:
- **Autonomous agents** seeking programmable, x402-payable verification services
- **Human buyers** evaluating trace-integrity solutions or operator tooling

---

## Active Services

### W04 — Bounded Trace-Integrity Verifier

**Status:** ✅ Active | **Network:** Base Mainnet (eip155:8453)  

A deterministic verification service for LLM traces, agentic workflows, and x402 transaction records using 6 bounded validation rules:

1. **Rule Correctness** — Validation rules match stated requirements
2. **Determinism** — Same input produces same output  
3. **Hallucination-Free Execution** — No fabricated trace entries or claims
4. **Context Sufficiency** — All required evidence present in input
5. **Provenance Chain** — Complete, verifiable history of transformations
6. **Bounded Output Integrity** — Response size and structure within limits

#### Commercial Profile (Fixed)

| Parameter | Value |
|-----------|-------|
| Price | **$0.01** per invocation |
| Protocol | x402 v2 exact |
| Network | Base Mainnet (eip155:8453) |
| Settlement Currency | USDC (Circle, 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913) |
| Pay-to Address | 0x59faea25627eda8bb2be8feda62bde961a665a1d |

#### Technical Specs

- **Endpoint:** `POST https://soja-w04-public-beta.onrender.com/v1/verify`
- **Authentication:** x402 v2 payment proof in request headers
- **Max Request Size:** 1 MB
- **Max Rules per Call:** 50
- **Max Trace Entries:** 500
- **Concurrent Execution Limit:** 4

#### Input Example

```json
{
  "trace": [
    {"timestamp": "2026-08-30T05:00:00Z", "role": "user", "tool": "execute_code", "content": "python script"},
    {"timestamp": "2026-08-30T05:01:00Z", "role": "assistant", "tool": null, "content": "Result explanation"}
  ],
  "rules": [
    "Verify tool execution produced deterministic output",
    "Check for hallucinated trace entries not in input"
  ]
}
```

#### Output Schema

```json
{
  "verdict": true|false,
  "summary": "Brief verdict explanation",
  "failures": ["list of failed checks if verdict=false"],
  "confidence_score": 0.0-1.0
}
```

---

## Upcoming Products (Human-Facing)

These are planned for near-term launch pending demand validation:

| Product | Target Price | Description |
|---------|--------------|-------------|
| Evidence Manifest Template Pack | $9 | Notion/Obsidian templates for documenting trace integrity evidence |
| Human-Readable Audit Report Card | $19 | Convertible W04 output into shareable HTML/PDF reports |

---

## Discovery & Integration

### For Autonomous Agents

This catalog is x402-compatible. Agents can:
1. Parse this JSON to discover `W04` service metadata
2. Follow the `offer_available_at` URL for complete payment profile
3. Invoke with standard x402 v2 exact payment flow on Base mainnet

### For Human Developers

- **Test invocation:** Requires live USDC funds and x402-compatible client
- **Documentation:** Full spec available at service root URL
- **Support:** Telegram channel only (no DM)

---

## Machine Discovery Metadata

```json
{
  "x402_compatible": true,
  "accepts_x402_payments": true,
  "payment_routing": "direct-to-merchant",
  "circuit_breaker": "owner-controlled"
}
```

---

## Contact & Inquiries

**Business inquiries only via:** Telegram (configured channel)  
No DM. No unsolicited outreach. Owner-operated only.

---

## License & Usage

This catalog and its metadata are published for discovery purposes.  
Service invocation requires payment per commercial profile.
