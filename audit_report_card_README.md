# SOJA W04 Audit Report Card Generator

**Price:** $19.00 (one-time per report batch)  
**Format:** Professional HTML/PDF audit reports from W04 JSON output  
**Delivery:** Email or download link after purchase  

---

## What's Inside

This service converts your raw W04 verification results into professional, stakeholder-ready audit documentation that non-technical audiences can understand.

### Report Components

Each Audit Report Card includes:

#### 1. Executive Summary
- High-level VERIFIED/NOT_VERIFIED status with visual indicator
- One-sentence verdict explanation
- Confidence score as percentage and color-coded meter
- Total traces verified and rules evaluated

#### 2. Verification Details
- Chronological trace-by-trace breakdown
- Rule evaluation results per trace entry
- Failed checks highlighted with specific findings
- Timestamps preserved for audit trail integrity

#### 3. Technical Appendix
- Original W04 JSON output (machine-readable)
- Payment transaction reference (x402 hash)
- Verification timestamp and service version
- Schema validation status

#### 4. Trust Markers
- SOJA W04 branding and authentication
- QR code for independent verification
- Digital signature placeholder for enterprise use
- Merchant address proof of origin

---

## How It Works

### Step 1: Run Your W04 Verification
Execute your standard paid W04 invocation against your evidence manifest:

```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  -d @your-manifest.json \
  -H "x402-payment: <payment-proof>"
```

### Step 2: Capture the JSON Response
Save the W04 response (containing verdict, summary, failures, confidence_score).

### Step 3: Submit for Report Generation
Send your W04 result to the Audit Report Card service along with:
- Your email for delivery
- Optional: organization name, report ID, custom branding preferences

### Step 4: Receive Professional PDF/HTML
Within minutes, receive a professionally formatted audit document suitable for:
- Board presentations
- Compliance documentation  
- Client deliverables
- Internal security reviews
- Regulatory filings

---

## Sample Report Layout

```
┌─────────────────────────────────────────────────────┐
│              SOJA W04 AUDIT REPORT                  │
│         Bounded Trace-Integrity Verification        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  VERIFIED ✓                                         │
│                                                     │
│  Confidence: 98.5%                                  │
│  ━━━━━━━━━━━━━━━━━━█                               │
│                                                     │
│  Summary: All trace hash validations passed. No     │
│  integrity violations detected across 12 trace      │
│  entries evaluated against 6 bounded rules.         │
│                                                     │
│  ──────────────────────────────────────             │
│  Verification Details                              │
│                                                     │
│  [✓] Trace 001: User input validation              │
│  [✓] Trace 002: Tool execution check               │
│  [✓] Trace 003: Response integrity                 │
│  ...                                               │
│                                                     │
│  ──────────────────────────────────────             │
│  Technical Appendix                                │
│  • Transaction Hash: 0x4f2a...9b8c                 │
│  • Verification Time: 2026-08-30T12:34:56Z         │
│  • W04 Version: 1.3                                │
│                                                     │
│  [Verify Independently] [QR Code]                  │
└─────────────────────────────────────────────────────┘
```

---

## Use Cases

### Compliance Teams
Meet audit requirements with standardized, defensible verification documentation that regulators and auditors recognize.

### Client-Facing Agentic Services
Deliver professional proof of trace integrity to clients who need assurance beyond raw JSON outputs.

### Security Reviews
Document verification results for security audits, incident investigations, or penetration testing reports.

### Contract Validation
Provide immutable proof that AI-generated work products passed independent integrity checks before payment or delivery.

---

## Technical Specifications

**Input:** W04 v1 JSON response object  
**Output:** HTML document + PDF (A4 landscape or letter)  
**Processing Time:** <5 minutes standard, <30 minutes peak demand  
**Format Options:**
- Standard professional template (default)
- Brand-customized header/footer ($29 upgrade)
- Multi-report batch processing ($19 per 5 reports)

---

## Integration Options

### Option A: Manual Submission (Currently Available)
Send us your W04 JSON output via Telegram with payment confirmation. We deliver formatted reports manually.

**Best for:** One-time audits, proof-of-concept testing  
**Turnaround:** <24 hours  
**Price:** $19/report

### Option B: Automated API Pipeline (In Development)
Integrate the report generator into your workflow as a secondary paid endpoint following W04 invocation.

**Best for:** High-volume operations, embedded compliance  
**Status:** Planned, owner approval required for implementation

### Option C: Self-Hosted Template (Enterprise)
Purchase and deploy the report template engine on internal infrastructure for unlimited internal use.

**Best for:** Organizations requiring data sovereignty  
**Price:** Custom quote via Telegram

---

## Pricing

| Tier | Price | What You Get |
|------|-------|--------------|
| Single Report | $19 | One professional PDF/HTML audit report |
| Pack of 5 | $79 (~$16/report) | Five reports, batch discount |
| Enterprise Template | Custom | Unlimited internal use, self-hosted |

Payment accepted via USDC to merchant address or pending PayPal/Stripe integration.

---

## Delivery Method

**Current:** Manual delivery after payment verification (via Telegram or email)  
**Coming:** Automated encrypted download link system  

---

## About W04

W04 is SOJA's Bounded Trace-Integrity Verifier operating on Base mainnet with x402 v2 exact payments ($0.01 per verification call). No account required for the base service; audit reports add human-readable professional output layer.

More: [W04 Public Beta](https://soja-w04-public-beta.onrender.com) | [Template Pack](./EVIDENCE_MANIFEST_TEMPLATE_PACK_README.md)

---

## License

Single-report license included. For unlimited internal reprocessing or client-facing redistribution, contact for enterprise licensing via Telegram.

**Warranty:** Reports provided as-rendered from W04 output. SOJA does not warrant accuracy of underlying trace data submitted to W04.
