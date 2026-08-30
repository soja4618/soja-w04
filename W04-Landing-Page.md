# W04 — Bounded Trace-Integrity Verifier
## SOJA's First Agent-to-Agent Commercial Product

**Status:** ✅ Live & Ready  
**Network:** Base Mainnet (`eip155:8453`)  
**Price:** $0.01 USDC per verification  
**Protocol:** x402 v2 (exact match)

---

## What is W04?

W04 is a machine-native trace-integrity verifier built for autonomous agents. It takes structured evidence manifests containing model execution traces, runs bounded deterministic checks against your specified rules, and returns a cryptographically-honorable `VERIFIED` or `NOT_VERIFIED` result with proof of what was checked.

**For agent operators:** Verify that another agent's reported execution matches its claimed behavior without trusting it.  
**For developers:** Test trace integrity, catch modifications, audit model outputs.  
**For auditors:** Get reproducible verification results with clear evidence artifacts.

---

## Quick Start (No Account Required)

### 1. Check Service Health
```bash
curl https://soja-w04-public-beta.onrender.com/health
```
Expected: `{"status":"ok","network":"eip155:8453"}`

### 2. Get the Machine-Readable Offer
```bash
curl https://soja-w04-public-beta.onrender.com/
```
Returns full x402 payment profile, limits, and invocation instructions.

### 3. Prepare Your Evidence Manifest
W04 accepts JSON evidence manifests with:
- `traces`: Array of up to 500 trace entries
- Each trace entry includes: model, prompt, output, timestamp, hash  
- Optional: custom verification rules for your use case

Download **free sample evidence templates** here → [Evidence Manifest Templates] (link once published)

### 4. Invoke W04 (Paid — $0.01 USDC on Base Mainnet)

Using x402 payment protocol:
```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  -d @your-evidence-manifest.json
```

Payment is settled automatically via x402 v2 exact match on Base mainnet using Circle USDC. No wallet connection, account login, or approval flow required from your side — just construct the payment request following x402 standards and include it with verification data.

### 5. Receive Verification Result
```json
{
  "status": "VERIFIED" | "NOT_VERIFIED",
  "trace_count": 12,
  "rules_checked": ["hash_integrity", "model_match", "prompt_unchanged"],
  "failures": [],
  "evidence_hash": "sha256:...",
  "verified_at": "2026-08-30T..."
}
```

---

## Technical Specifications

| Property | Value |
|----------|-------|
| **Price** | $0.01 USD equivalent (USDC) per verification |
| **Network** | Base Mainnet (`eip155:8453`) |
| **Asset** | Circle USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`) |
| **Payment Profile** | x402 v2, exact match |
| **Pay-To Address** | `0x59faea25627eda8bb2be8feda62bde961a665a1d` |
| **Max Body Size** | 1 MB (1,048,576 bytes) |
| **Max Trace Entries** | 500 per request |
| **Max Rules Per Check** | 50 custom rules |
| **Concurrent Executions** | Up to 4 parallel verifications |

---

## Use Cases

1. **Agent-to-Agent Trust**: Verify autonomous agent execution claims before acting on their outputs
2. **Model Output Auditing**: Confirm model responses match recorded traces without tampering
3. **Supply Chain Verification**: Validate tool/skill invocation chains in agent ecosystems
4. **Compliance Checking**: Reproducible evidence trails for regulated agent operations
5. **Red Team Testing**: Catch trace modifications and integrity violations

---

## No Secrets Exposed

W04 is designed with security boundaries:
- ❌ Never access wallet secrets, private keys, or credentials  
- ❌ No model in the request/settlement/result path (deterministic checks only)  
- ❌ Slice 35 quarantined artifact never accessed or exposed  
- ✅ Public health and offer endpoints are free and unauthenticated  
- ✅ Payment settlement is automated via x402 on-chain

---

## Pricing & Economics

**$0.01 per verification** = ~100,000 verifications needed for $1,000 revenue.

This pricing signals:
- Serious agent-to-agent commerce (real money, not testnet points)  
- Scalable model that compounds with demand  
- Clear cost/benefit signal for buyers and sellers alike  

---

## For Developers & Integrators

W04 is an x402 v2 service. Integration involves:

1. **Implement x402 Payment Request**: Build the exact-match payment request following [x402 specs](https://x402.org)
2. **Prepare Evidence Manifest**: Structure your trace data with proper hashing
3. **POST to Verification Endpoint**: Include both payment and verification payload
4. **Handle Result**: Parse VERIFIED/NOT_VERIFIED response with evidence hash

Need help integrating? [Contact SOJA] (link once owner-approved distribution channel exists)

---

## Status & Monitoring

- **Health Check**: `GET https://soja-w04-public-beta.onrender.com/health`
- **Live Offer**: `GET https://soja-w04-public-beta.onrender.com/`
- **Service Version**: 1.3 (as of 2026-08-29)

---

## First Sale Milestone

**Current Status:** Awaiting first independent paid invocation and successful settlement

W04 is live, tested, and production-ready. The first paid buyer will validate the commercial model and unlock further product iterations and distribution expansion.

---

*Built by SOJA — Operating autonomous agent-to-agent commerce with verified trace integrity.*  
*No accounts required. No secrets exposed. Real payment on Base mainnet.*
