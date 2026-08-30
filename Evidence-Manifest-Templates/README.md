# W04 Evidence Manifest Template Pack

**Purpose**: Sample evidence manifest files to help developers and buyers test the W04 Bounded Trace-Integrity Verifier.

## About These Templates

These JSON templates demonstrate three verification scenarios:

1. **clean-trace.json** - All traces pass verification (expected result: `VERIFIED`)
2. **tampered-output.json** - Output has been modified after generation (expected result: `NOT_VERIFIED`)  
3. **corrupted-data.json** - Hash mismatches indicating data corruption (expected result: `NOT_VERIFIED`)

## How to Use

### Step 1: Download a Template
```bash
# Example download command (URLs will be provided)
curl -o clean-test.json "https://example.com/w04-templates/clean-trace.json"
```

### Step 2: Prepare Your x402 Payment Request
W04 requires an x402 v2 exact-match payment on Base mainnet (USDC, $0.01).

See the [x402 specification](https://x402.org) for payment request construction.

### Step 3: Invoke W04 Verification
```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  --data-binary @clean-test.json \
  [INCLUDE_X402_PAYMENT_HEADER_OR_BODY]
```

### Step 4: Parse the Response
```json
{
  "status": "VERIFIED",
  "trace_count": 3,
  "rules_checked": ["hash_integrity", "model_consistency", "prompts_unchanged"],
  "failures": [],
  "evidence_hash": "sha256:...",
  "verified_at": "2026-08-30T..."
}
```

## Template Structure Reference

Each evidence manifest contains:

```json
{
  "metadata": {
    "version": "1.0",
    "description": "What this template demonstrates",
    "use_case": "Scenario description",
    "expected_result": "VERIFIED | NOT_VERIFIED"
  },
  "rules": {
    "check_hash_integrity": true,
    "check_model_consistency": true,
    "check_prompts_unchanged": true
  },
  "traces": [
    {
      "id": "trace-unique-id",
      "timestamp": "ISO8601 timestamp",
      "model": "model-identifier",
      "prompt_sent": "input to the model",
      "output_received": "model response",
      "input_hash": "sha256:...",
      "output_hash": "sha256:..."
    }
  ]
}
```

## Creating Your Own Manifest

1. **Collect traces**: Record prompt/output pairs with their original hashes
2. **Apply rules**: Decide which integrity checks you need
3. **Format correctly**: Ensure all required fields are present
4. **Test locally**: Validate JSON structure before paying for W04 verification
5. **Submit to W04**: POST to `/v1/verify` with x402 payment

## Notes

- Maximum 500 traces per request
- Maximum 50 custom rules per request
- Maximum body size: 1 MB
- Current price: $0.01 USDC per verification on Base mainnet

## Support & Documentation

- **Health Check**: `https://soja-w04-public-beta.onrender.com/health`
- **Live Offer**: `https://soja-w04-public-beta.onrender.com/`
- **Landing Page**: See `W04-Landing-Page.md`
- **Issues**: Contact SOJA once distribution channel is established

---

*These templates are provided as-is for testing and educational purposes.*  
*Actual W04 verification results depend on live execution against real data.*
