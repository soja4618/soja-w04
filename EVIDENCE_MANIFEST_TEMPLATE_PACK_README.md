# SOJA W04 Evidence Manifest Template Pack

**Price:** $9.00 (one-time)  
**Format:** 3 ready-to-use JSON templates + documentation  
**Delivery:** Immediate download link after purchase  

---

## What's Inside

This pack contains three carefully crafted evidence manifest templates designed to demonstrate the full range of W04 verification outcomes:

### `template-clean.json`
A perfectly valid manifest where all trace hashes match their expected values. Passes every rule check, demonstrating successful integrity verification.

**Use case:** Verify your implementation correctly accepts valid manifests; test happy paths in your agent workflows.

### `template-modified.json`
A manifest with one deliberately altered trace hash that fails the integrity check. Demonstrates tamper detection — exactly what W04 is built to catch.

**Use case:** Test that your system properly rejects compromised traces; validate error handling and failure responses.

### `template-corrupted.json`
A manifest with malformed structure (extra fields, missing required properties). Fails schema validation before rule execution even begins.

**Use case:** Ensure robust JSON parsing; test input validation edge cases; understand W04's bounded acceptance criteria.

---

## How to Use

1. **Download** all three template files
2. **Review** each template structure and comments
3. **Test** against your local W04 mock or the live endpoint (requires $0.01 per invocation)
4. **Adapt** patterns for your own evidence manifest needs

### Quick Test Command

```bash
# Save a template as manifest.json, then:
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  --data-binary @manifest.json
```

Note: Live invocations require x402 v2 exact payment of $0.01 USDC on Base mainnet. See the [W04 README](./README.md) for full documentation.

---

## What You Learn

- Correct evidence manifest structure per W04 spec v2025-09-27
- How trace-hash mismatches trigger failure responses
- Schema validation boundaries and error modes
- Real-world patterns for agent-to-agent verification workflows
- How to build your own manifests for production use

---

## Who This Is For

- **Agent developers** building x402-compatible workflows
- **Base network developers** exploring payment-gated APIs  
- **Verifier implementers** needing test coverage across success/failure modes
- **Learning labs** teaching trace integrity concepts
- **Integration teams** prototyping SOJA W04 connections

---

## Pricing & Payment

**$9.00 USD, one-time purchase.**

Payment options (currently being configured):
- Direct USDC transfer to merchant address
- Alternative payment methods coming soon

Contact through Telegram for bulk/enterprise licensing or custom manifest creation services.

---

## License

Single-user commercial use license included. Redistribution of templates requires explicit written permission from SOJA. Templates are provided as-is with no warranty; W04 service availability subject to hosting terms.

---

## About W04

W04 is SOJA's Bounded Trace-Integrity Verifier — a deterministic, no-LLM-in-path API for autonomous agent-to-agent verification via x402 v2 payments on Base mainnet. No account required; callers retain full wallet custody.

Learn more: [W04 Public Beta](https://soja-w04-public-beta.onrender.com) | [README](./README.md)
