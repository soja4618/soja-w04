# 🛠️ W04 Developer Starter Kit
**Version:** 1.0 | **Status:** Ready for Distribution
**Product:** SOJA W04 — Bounded Trace-Integrity Verifier

---

## 📖 Overview
The **W04 Starter Kit** is designed for developers building autonomous agent-to-agent commerce pipelines. It provides the necessary tools to test, validate, and implement deterministic trace-integrity verification using the **x402 v2 exact payment protocol**.

## 🚀 Quick Start: Testing Your First Manifest

W04 allows you to verify that a JSON "evidence manifest" (a log of an agent's actions) has not been tampered with by using cryptographic hash rules.

### 1. Environment Setup
Ensure you have `curl` and `jq` installed on your system.

### 2. Grab the Test Templates
These templates allow you to see exactly how W04 responds to different integrity scenarios.

```bash
# Create a directory for your tests
mkdir w04-tests && cd w04-tests

# Download the three core test cases
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-clean.json
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-modified.json
curl -O https://raw.githubusercontent.com/soja4618/soja-w04/main/COMMERCIAL/template-corrupted.json
```

### 3. Run the Verification
Each invocation costs **$0.01 USDC** on **Base Mainnet** via the x402 protocol.

#### **Test Case #1: The "Happy Path" (Clean Trace)**
Verifies a perfectly intact manifest.
```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json" \
  --data-binary @template-clean.json
```
**Expected Result:** `{"status": "VERIFIED", ...}`

#### **Test Case #2: The "Tamper Alert" (Modified Trace)**
Verifies how W04 detects a single changed hash.
```bash
curl -X POST https://soja-w04-public-beta.onrender.com/v1/verify \
  -H "Content-Type: application/json\" \
  --data-binary @template-modified.json
```
**Expected Result:** `{"status": "NOT_VERIFIED", "details": {"failure": "trace-002"}}`

---

## 📐 Manifest Schema Reference
When building your own agent-to-agent verification logic, your JSON payloads must follow this strict schema:

```json
{
  "version": "1.0",
  "description": "Your manifest description",
  "traces": [
    {
      "id": "unique-trace-id-001",
      "hash": "sha256-hash-of-action-1"
    }
  ],
  "rules": [
    {
      "type": "integrity",
      "operator": "equals",
      "expected": "sha256-expected-hash-1"
    }
  ]
}
```

## 💰 Payment & Integration Details
* **Protocol:** x402 v2 (Exact)
* **Network:** Base Mainnet (`eip155:8453`)
* **Asset:** USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
* **Merchant:** `0x59faea25627eda8bb2be8feda62bde961a665a1d`
* **Facilitator:** `https://facilitator.payai.network`

---
*© 2026 SOJA. Empowering autonomous agent integrity.*
