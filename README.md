# 🛡️ SOJA W04 — Bounded Trace-Integrity Verifier

**Deterministic verification of agent-to-agent payment trace integrity.**

---

## 🤖 Machine-Readable Offer (Agent Discovery)
*For autonomous agents and x402-compliant discovery engines.*

```json
{
  "name": "SOJA W04 \u2014 Bounded Trace-Integrity Verifier",
  "version": "1.3",
  "description": "Deterministic verification of bounded JSON evidence manifests for autonomous agent-to-agent payment trace integrity. Validates that x402-invoked API calls delivered their claimed results.",
  "type": "agent_api_service",
  "category": "verification",
  "endpoints": [
    {
      "name": "verify",
      "method": "POST",
      "path": "/v1/verify",
      "description": "Submit an evidence manifest for deterministic trace-integrity verification.",
      "authentication": "x402_v2_exact_payment_required"
    },
    {
      "name": "health",
      "method": "GET",
      "path": "/health",
      "description": "Service health check (no authentication required)",
      "status": "free"
    },
    {
      "name": "offer",
      "method": "GET",
      "path": "/",
      "description": "Machine-readable offer profile (no authentication required)",
      "status": "free"
    }
  ],
  "payment": {
    "protocol": "x402",
    "version": "2.0",
    "scheme": "exact",
    "network": "eip155:8453",
    "network_name": "Base mainnet",
    "asset": "USDC",
    "asset_contract": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    "merchant_address": "0x59faea25627eda8bb2be8feda62bde961a665a1d",
    "price_per_invocation_usd": "0.01",
    "price_atomic_units": "10000",
    "facilitator": "https://facilitator.payai.network"
  },
  "limits": {
    "max_request_body_bytes": 1048576,
    "max_rules_count": 50,
    "max_trace_entries": 500,
    "max_concurrent_executions": 4
  },
  "input_schema": {
    "type": "object",
    "required": [
      "manifest"
    ],
    "properties": {
      "manifest": {
        "type": "object",
        "required": [
          "traces",
          "rules"
        ],
        "properties": {
          "version": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "traces": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "id",
                "hash"
              ],
              "properties": {
                "id": {
                  "type": "string"
                },
                "hash": {
                  "type": "string"
                }
              },
              "additionalProperties": false
            }
          },
          "rules": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "type",
                "operator",
                "expected"
              ],
              "properties": {
                "type": {
                  "type": "string"
                },
                "operator": {
                  "type": "string"
                },
                "expected": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "status": {
        "type": "string",
        "enum": [
          "VERIFIED",
          "NOT_VERIFIED"
        ]
      },
      "details": {
        "type": "object",
        "description": "Structured evaluation results"
      },
      "timestamp": {
        "type": "string",
        "format": "date-time"
      }
    }
  },
  "capabilities": [
    "deterministic_verification",
    "no_llm_in_path",
    "machine_readable_offers",
    "x402_v2_payment",
    "account_not_required",
    "trace_integrity_validation"
  ],
  "target_buyer": {
    "primary": "autonomous_agents",
    "secondary": [
      "agent_developers",
      "x402_implementers",
      "base_developers"
    ]
  },
  "use_cases": [
    "Verify x402 payment \u2192 result chain integrity for agent API invocations",
    "Detect tampering in trace hash chains",
    "Validate evidence manifests with bounded cryptographic rules",
    "Agent-to-agent verification without human sales interaction"
  ],
  "links": {
    "service_url": "https://soja-w04-public-beta.onrender.com",
    "health_endpoint": "https://soja-w04-public-beta.onrender.com/health",
    "offer_endpoint": "https://soja-w04-public-beta.onrender.com/",
    "verification_endpoint": "https://soja-w04-public-beta.onrender.com/v1/verify"
  },
  "created": "2026-08-25",
  "updated": "2026-08-30",
  "status": "live_beta"
}
```

---

## 🚀 Quick Start for Developers
**Verify your agent-to-agent traces for just $0.01 per invocation.**

W04 allows you to confirm that an API call delivered the claimed result using cryptographic hash rules. 

### 1. Get the Test Templates
Use our pre-made JSON manifests to test success and failure patterns:
[Download Starter Kit Gist](https://gist.github.com/soja4618/1e5ff0899548b13e99516f700fccd42f)

### 2. Run a Test Verification
```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  --data-binary @template-clean.json
```

### 3. Integration Details
- **Protocol:** x402 v2 (Exact)
- **Network:** Base Mainnet (`eip155:8453`)
- **Asset:** USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
- **Merchant:** `0x59faea25627eda8bb2be8feda62bde961a665a1d`

---

## 📊 Commercial Status
- **Status:** Live Beta
- **Pricing:** $0.01 per request
- **Contact:** [SOJA Commercial Operations]
