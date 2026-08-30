# W04 Evidence Manifest Template Pack — User Guide

**Version:** 1.0  
**Last Updated:** 2026-08-30  
**Purpose:** Learn W04 verification patterns through hands-on testing

---

## What is this?

The Evidence Manifest Template Pack contains pre-made JSON templates demonstrating how W04 (SOJA's Bounded Trace-Integrity Verifier) processes different trace integrity scenarios. Each template shows one distinct verification pattern:

| Template | Description | Expected W04 Result |
|----------|-------------|---------------------|
| `template-clean.json` | All hash values match expected rules | `VERIFIED` — passes all integrity checks |
| `template-modified.json` | One trace hash altered from expected value | `NOT_VERIFIED` — integrity check fails on trace-002 |
| `template-corrupted.json` | Invalid structure (unexpected fields, missing required keys) | `INVALID_INPUT` — structural validation error |

---

## How to Use These Templates

### 1. Download the Template Pack

Get all three templates from the W04 Commercial repo:

```bash
# Individual files
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-clean.json
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-modified.json
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-corrupted.json
```

### 2. Test with W04 (Paid Invocation Required)

Each W04 verification costs **$0.01 USDC on Base mainnet** via x402 v2 exact payment protocol.

#### Example: Testing the Clean Template

```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  --data-binary @template-clean.json
```

**Expected Response (after payment):**
```json
{
  "status": "VERIFIED",
  "details": {
    "all_traces_integrity_confirmed": true,
    "rule_evaluation_results": [...]
  },
  "timestamp": "2026-08-30T..."
}
```

### 3. Understand the Results

Each template demonstrates a different verification outcome:

#### ✅ `template-clean.json` — Verification Success Pattern

**What's tested:** All trace hashes match their corresponding integrity rules exactly.

**W04 behavior:** Returns `VERIFIED` status with no errors.

**Use case:** Learn what a successful verification response looks like when parsing agent-to-agent responses.

---

#### ❌ `template-modified.json` — Integrity Failure Pattern

**What's tested:** The hash value for `trace-002` has been changed from its expected value in the rules array.

**Specific difference:**
- Template trace: `"MODIFIED_HASH_TO_TRIGGER_FAILURE_..."`
- Rule expects: `"b2c3d4e5f67890123456789012345678901bcdef..."`

**W04 behavior:** Returns `NOT_VERIFIED` with details showing which trace failed integrity check.

**Use case:** Handle verification failures in your agent code; learn what error output looks like.

---

#### ⚠️ `template-corrupted.json` — Structural Error Pattern

**What's tested:** Intentionally malformed JSON structure:
- Extra field `extra_field` on trace-001 (triggers `UNEXPECTED_FIELD`)
- Missing required `id` key on trace-003 (triggers validation error)

**W04 behavior:** Returns `INVALID_INPUT` indicating structural validation failed before rule evaluation.

**Use case:** Validate client input before sending to W04; understand W04's strict schema enforcement.

---

## Template Structure Reference

All templates use this JSON schema:

```json
{
  "version": "<string>",
  "description": "<string>",
  "traces": [
    {
      "id": "<string>",          // Required unique identifier
      "hash": "<sha256>"         // Required hash value
    }
  ],
  "rules": [
    {
      "type": "integrity",       // Rule type
      "operator": "equals",      // Comparison operator
      "expected": "<sha256>"     // Expected hash value
    }
  ]
}
```

### Validation Rules

W04 enforces strict structural validation:

1. **No duplicate keys** in any JSON object → `DUPLICATE_KEY` error
2. **No extra fields** in `traces[]` beyond `id`, `hash` → `UNEXPECTED_FIELD` error  
3. **All traces must have required keys** (`id`, `hash`) → structural validation error
4. **Rules array must match trace count** otherwise some rules may be unapplied

---

## Real-World Use Cases

### 1. Testing Agent-to-Agent Verification Pipelines

Before deploying autonomous verification logic, test your agents' ability to:
- Parse W04 responses correctly
- Handle both success and failure cases  
- Implement retry logic for invalid inputs

### 2. Demonstrating W04 Behavior to Stakeholders

The template pack provides concrete examples when explaining:
- How deterministic trace verification works
- What kinds of tampering W04 detects
- The difference between structural errors vs integrity failures

### 3. Building Client Libraries

Use these templates as test fixtures for your own W04 client SDK implementations in any language.

---

## Cost Guide

Each template invocation costs **$0.01 USDC** on Base mainnet:

| Activity | Cost |
|----------|------|
| Download templates | $0 (free) |
| Test template-clean.json | $0.01 |
| Test template-modified.json | $0.01 |
| Test template-corrupted.json | $0.01 |
| **Total for all 3** | **$0.03** |

---

## Troubleshooting

### "x402 challenge" response

If you see an x402 challenge (not a verification result), your request is missing proper authentication/payment headers. W04 requires:
- x402 v2 exact payment protocol
- Base mainnet (`eip155:8453`)
- USDC asset
- $0.01 payment to merchant address

### "Invalid JSON" errors

Ensure your client properly parses JSON responses. W04 only accepts valid JSON input — test with the templates first to see correct formatting.

---

## Reporting Template Issues

If a template produces unexpected results, or you find bugs in this guide:
- Open an issue on the W04 GitHub repository
- Include the template name and observed vs expected behavior
- Note your client library/language version if applicable

---

## Next Steps

After testing with templates:
1. **Create your own manifests** following the schema above
2. **Test edge cases** (missing fields, extra data types, boundary values)
3. **Build verification logic** into your autonomous agents
4. **Consider bulk verification patterns** for production traces

---

*This guide is free to use and distribute. W04 verification service requires payment per invocation as stated above.*
