# SOJA Distribution Decision Request

**Date:** 2026-08-30 10:17 EDT  
**Cycle ID:** d4964b1e961c (current run)  
**Urgency:** Medium — Products complete, revenue blocked  

---

## EXECUTIVE SUMMARY

All commercial assets are built and ready. Cannot generate revenue without publishing to buyers through a distribution channel. Need owner decision on which approved path(s) to enable.

### Revenue Objective Status
- **Target:** $10,000 minimum → $250,000 stretch in <30 days  
- **Current Verified Revenue:** $0.00  
- **Blocking Factor:** Distribution channel access  

---

## READY COMMERCIAL ASSETS (No Additional Build Time Needed)

| Asset | Type | Price | Status | Owner Action Required |
|-------|------|-------|--------|----------------------|
| W04 Agent-to-Agent Service | x402 verification | $0.01/invocation | ✅ LIVE | None — endpoint operational |
| Evidence Manifest Template Pack | Human product | $9 | ✅ COMPLETE | Publication channel |
| Audit Report Card | Human product | $19 | ✅ COMPLETE | Publication channel |
| Service Catalog (Machine-Readable) | Discovery/free | Free | ✅ COMPLETE | Owner approval to publish |

---

## DISTRIBUTION CHANNEL OPTIONS (Ranked by Speed + Effort)

### Option 1: Manual USDC Payment Flow (IMMEDIATE — RECOMMENDED AS FIRST TEST)

**What:** Announce via a single public post that buyers can send USDC to the known merchant address, receive products/reports manually.

**Process:**
- Buyer sends $9 or $19 USDC to `0x59faea25627eda8bb2be8feda62bde961a665a1d` on Base mainnet
- Buyer includes product name in transaction memo (if supported) or follows up via Telegram
- Owner manually delivers template/report files

**Pros:**
- Zero external account/approval needed
- Tests real payment intent immediately
- Works within existing authorization boundaries

**Cons:**
- High friction for buyers
- Manual fulfillment (scales poorly beyond first few sales)
- No checkout automation or delivery confirmation

**Time to Execute:** Immediate, once approved

---

### Option 2: GitHub Repository Update (LOW EFFORT)

**What:** Update `soja4618/soja-w04` repository with product information, template pack download links, and purchase instructions.

**Process:**
- Update README with Evidence Manifest Templates + Audit Report Card descriptions
- Add `/COMMERCIAL/` folder containing downloadable templates
- Include manual USDC payment instructions (as above) or Gumroad links once created

**Pros:**
- Permanent discovery surface for technical audience
- SEO signal, credibility with agent developers
- Low ownership/account risk (existing repo)

**Cons:**
- Requires `gh` CLI token or owner manual update
- Not discoverable by autonomous agents yet

**Owner Action Required:**
- Option A: Enable Hermes to write to the repo via GitHub CLI token
- Option B: Owner updates repository manually with provided content

**Time to Execute:** <30 minutes after access granted

---

### Option 3: Gumroad/Lemon Squeezy Account (FULL AUTOMATION)

**What:** Create account on one platform, publish Evidence Manifest Template Pack ($9) and Audit Report Card ($19).

**Pros:**
- Professional checkout experience
- Automated delivery, payments, refunds handled
- Analytics, email collection, discount codes available

**Cons:**
- New account creation requires owner permission
- ~1 hour setup + platform review time
- Platform fees (~5% + processing)

**Owner Action Required:** Approve account creation on Gumroad or Lemon Squeezy for SOJA commercial use

**Time to Execute:** ~1-2 hours after approval

---

### Option 4: x402-list.com Directory Submission (AGENT DISCOVERY)

**What:** Submit W04 service listing to x402-compatible directories.

**Pros:**
- Direct agent-to-agent discovery audience
- Free submission for compute-hosted services
- Credible within x402 ecosystem

**Cons:**
- Listing may require verification step
- Uncertainty about directory traffic/demand

**Owner Action Required:** Verify Render listing eligibility, approve optional $1 fee if needed

**Time to Execute:** <1 hour after verification

---

## DECISION REQUESTED

Please approve one of the following:

### A. APPROVE IMMEDIATE TEST (RECOMMENDED)
✅ **Allow manual USDC payment flow announcement via [one existing public channel]**  
- Post to x402 Slack if access enabled, or prepare post for owner to publish
- Tests real demand before investing in automation

### B. ENABLE GITHUB REPOSITORY UPDATE
✅ **Enable Hermes to update `soja4618/soja-w04` repository with product assets**  
- Or: Owner manually updates repo with provided README/content changes

### C. APPROVE STOREFRONT ACCOUNT CREATION
✅ **Create Gumroad or Lemon Squeezy account for SOJA commercial products**  
- Enable full automation for Evidence Manifest Template Pack + Audit Report Card

### D. COMBINE MULTIPLE PATHS
Specify which combination (e.g., A+B, or B+C) to execute in sequence

### E. APPROVE x402-list.com SUBMISSION ONLY — IMMEDIATE ZERO-COST ACTION (NEW OPTION)

**What:** List W04 service on x402-list.com directory for agent discovery

**Prepared Data Ready Now:**
| Field | Value |
|-------|-------|
| Service name | SOJA W04 — Bounded Trace-Integrity Verifier |
| Base URL | https://soja-w04-public-beta.onrender.com |
| Website URL | https://soja-w04-public-beta.onrender.com (or GitHub) |
| Category | Data / Verification / Agent Tools |
| Description | x402 v2 exact trace-integrity verifier for AI agents. Validate bounded execution traces with deterministic rule engines. Base mainnet, $0.01/invocation USDC. Machine-ready health + offer at service root. |
| Endpoint paths | POST /v1/verify |
| Network | eip155:8453 (Base) |

**Owner Action Required: Confirm email address for submission**
- Submitting on behalf of SOJA to x402-list directory
- No cost (verified: "submit yours, free")
- Enables machine-readable discovery by autonomous agents
Directory stats verified: 575 services, $199K USD settlement volume last 30 days

**Execution Time:** <10 minutes after email confirmation
**Risk:** Zero (reversible via owner contact if needed)
**Upside:** W04 discoverable by agent ecosystem without human distribution friction

---

## NEXT STEPS AFTER APPROVAL

1. Execute first approved distribution action
2. Track: impressions → clicks → payment attempts → successful deliveries → verified revenue  
3. Record conversion event (even if zero sales initially proves demand channel works)  
4. Iterate based on real signal or scale to next highest channel  

---

## ROLLBACK / SAFETY NOTES

- No wallet secrets exposed in any option
- Merchant address already public at W04 endpoint
- Slice 35 quarantine never accessed
- All product assets verified before this request
- Manual delivery flow keeps full owner control

---

**Prepared by:** Hermes Agent (SOJA commercial operator)  
**Waiting on:** Owner decision via Telegram channel  
