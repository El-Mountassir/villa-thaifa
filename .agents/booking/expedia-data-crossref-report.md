# Expedia Partner Central — Cross-Reference Report

**Source:** `expedia-partner-central-extraction.md` (extracted 2026-02-20)
**Cross-referenced against:**

- `data/admin/said-data-validation-checklist.md`
- `data/finance/billing.json`
- `data/finance/rates.json`
- `data/operations/channels.json`
- `data/property/property-config.json`

**Generated:** 2026-02-20

---

## Table of Contents

- [Section A: Checklist Items Now Answerable](#section-a-checklist-items-now-answerable)
- [Section B: Data Mismatches](#section-b-data-mismatches)
- [Section C: New Data to Integrate](#section-c-new-data-to-integrate)
- [Section D: Critical Flag — VAT Configuration](#section-d-critical-flag--vat-configuration)

---

## Section A: Checklist Items Now Answerable

The Expedia extraction covers Step 3 (policiesAndSettings) of a 12-step onboarding wizard. It does NOT contain room-level data (that will be in Steps 4–7). All answerable items below are from the "Property-Wide: Policies and Services" section of the checklist.

### Cancellation Policy — ANSWERED

**Checklist question:** "What is the cancellation policy?"

**Expedia answer:**

- Free cancellation if cancelled 72+ hours before 18:00 on arrival day.
- Fee for cancellations within 72 hours: 1st night + tax.
- No-shows: same fee as late cancellation (1st night + tax).
- Policy cutoff time: 18:00 local (Casablanca/Marrakech timezone, GMT).

**Confidence:** HIGH — set directly in Expedia onboarding by Said.

---

### Payment Methods — PARTIALLY ANSWERED

**Checklist question:** "What payment methods are accepted?"

**Expedia answer:** Debit cards, Visa, Mastercard, and Cash.

**Note:** Card acceptance is now confirmed for Expedia bookings. The channels.json and billing.json currently list only cash and bank_transfer. Expedia confirms card (Visa/MC/Debit) is accepted.

**Confidence:** HIGH for Expedia channel. Unclear whether card acceptance applies at the physical property front desk too, or only via Expedia's payment processing.

**Action needed:** Ask Said: "Card payments — is this only through Expedia, or do you accept Visa/Mastercard at the property directly?"

---

### Deposits — ANSWERED

**Checklist:** No explicit question about deposits, but the property-config.json `todo` list includes "Said to fill: payment methods."

**Expedia answer:** No deposit required.

**Confidence:** HIGH — explicitly set to "No" in Expedia.

---

### Languages Spoken — ANSWERED (not in checklist, new data)

Not in the Said checklist, but now known: Arabic, Dutch, English, French.

**Note:** Dutch is unexpected. Worth confirming with Said whether this is accurate or a default selection.

---

### Timezone — ANSWERED (implicit)

Property timezone confirmed as GMT (Casablanca/Monrovia). This is consistent with Marrakech. Not explicitly asked in checklist but useful for check-in time policies.

---

### Billing Currency — CONFIRMED

Expedia billing currency = MAD. Consistent with `billing.json` `currency.secondary = "MAD"` and `currency.primary = "EUR"`. No conflict.

---

## Section B: Data Mismatches

### MISMATCH 1: Payment Methods — billing.json vs Expedia

| Field            | billing.json                                | Expedia (confirmed)      |
| ---------------- | ------------------------------------------- | ------------------------ |
| Cash             | YES                                         | YES                      |
| Bank transfer    | YES                                         | NOT listed               |
| Visa             | NOT listed (only in notes as "legacy data") | YES                      |
| Mastercard       | NOT listed (only in notes as "legacy data") | YES                      |
| Debit cards      | NOT listed                                  | YES                      |
| American Express | NOT listed                                  | NO (explicitly declined) |

**Impact:** billing.json `payment_methods.accepted` is `["cash", "bank_transfer"]`. Expedia confirms Visa/Mastercard/Debit are accepted. Bank transfer is not mentioned in Expedia (though it may still be offered directly by the property).

**Resolution needed:** Update billing.json to reflect card acceptance. Clarify whether bank transfer applies to direct bookings only.

---

### MISMATCH 2: VAT in billing.json — null vs Expedia's 10%

| Field                           | billing.json | Expedia (confirmed)                                    |
| ------------------------------- | ------------ | ------------------------------------------------------ |
| `tax.vat_rate`                  | `null`       | 10% VAT                                                |
| `tax.tourist_tax_per_night_mad` | `null`       | 3 MAD (Taxe de Sejour) + 5 MAD (Tourism Promotion Tax) |

**This is the critical mismatch.** See Section D for full analysis.

---

### MISMATCH 3: Cancellation policy — property-config.json vs Expedia

| Field                   | property-config.json | Expedia (confirmed)                     |
| ----------------------- | -------------------- | --------------------------------------- |
| `policies.cancellation` | `"TODO"`             | 72-hour window, 1st night + tax penalty |

**Impact:** The cancellation policy was unknown in our system. Expedia now gives us the authoritative value. This is now answerable — not a conflict, but a gap now filled.

---

### MISMATCH 4: Check-out time — destinia OTA vs property-config.json

This is a pre-existing mismatch flagged in property-config.json `todo`:

- Internal check-in-out.json: 11:00
- Destinia OTA: 13:30

Expedia extraction does not cover check-in/check-out times (those are likely in a later step of the onboarding wizard). This mismatch remains unresolved.

---

## Section C: New Data to Integrate

The following data points from Expedia do not exist anywhere in our data files and should be added.

### 1. VAT Rate: 10%

- **Source:** Expedia Step 3, Section 5 — Taxes and Fees
- **Target file:** `data/finance/billing.json` → `tax.vat_rate`
- **Value:** `0.10` (10%)
- **Critical caveat:** See Section D before integrating. The treatment of this rate (gross vs net) is not yet determined.

### 2. Taxe de Sejour: 3 MAD/night

- **Source:** Expedia Step 3, Section 5 — collected at property, not via Expedia
- **Target file:** `data/finance/billing.json` → `tax.tourist_tax_per_night_mad`
- **Value:** `3` (MAD per night)

### 3. Tourism Promotion Tax: 5 MAD/night

- **Source:** Expedia Step 3, Section 5 — collected at property, not via Expedia
- **Target file:** `data/finance/billing.json` → `tax.city_tax` (or new field)
- **Value:** `5` (MAD per night)
- **Note:** This is a separate tax from Taxe de Sejour. billing.json currently has only one tax field. A new field may be needed.

### 4. Cancellation Policy (full text)

- **Source:** Expedia Step 3, Section 4
- **Target file:** `data/property/property-config.json` → `policies.cancellation`
- **Value:** "Free cancellation up to 72 hours before 18:00 on check-in day. Late cancellation or no-show: 1st night + tax charged."

### 5. Card Payment Methods Confirmed

- **Source:** Expedia Step 3, Section 2
- **Target file:** `data/finance/billing.json` → `payment_methods.accepted`
- **Add:** `"visa"`, `"mastercard"`, `"debit_card"`

### 6. Deposit Policy: None

- **Source:** Expedia Step 3, Section 3
- **Target file:** `data/property/property-config.json` → `policies` (new field `deposit_required: false`)

### 7. Languages Spoken

- **Source:** Expedia Step 3, Section 1
- **Target file:** `data/property/property-config.json` → new field `languages_spoken`
- **Value:** `["Arabic", "Dutch", "English", "French"]`

### 8. Expedia Property ID

- **Source:** Expedia URL — `htid=114807934`
- **Target file:** `data/operations/channels.json` — add Expedia channel with `property_id: "114807934"`

### 9. Tax Team Assistance Pending

- **Source:** Expedia Step 3 — "Request tax team assistance" is CHECKED
- **Implication:** Expedia's tax team is supposed to contact the property before the listing goes live. This may be a blocker on the Expedia channel going live.
- **Target:** Create a Linear issue or note in `ops/status/` — this is an open action item.

---

## Section D: Critical Flag — VAT Configuration

**Severity: HIGH. Omar must review and decide before rates are loaded into Expedia.**

### The Problem

Expedia is configured with: **"No, add these taxes to the rate"** — meaning the 10% VAT is added ON TOP of whatever rate Said enters.

Our `rates.json` contains the following confirmed rates (locked until Dec 2026):

| Room                      | EUR/night |
| ------------------------- | --------- |
| R02 Deluxe Double         | 149       |
| R04/R05 Double Superior   | 159       |
| R06 Executive Suite       | 179       |
| R07 Deluxe King Suite     | 329       |
| R09/R11 Family Suite      | 189       |
| R12 Presidential Suite    | 449       |
| R01/R03/R08 Deluxe Triple | 169       |
| R10 Suite                 | 179       |

### The Risk

If Said locked these rates as **gross prices** (what the guest pays), but Expedia adds 10% VAT on top, guests will be overcharged:

- Example: R02 locked at 149 EUR. If entered as-is into Expedia, guest sees 149 + 14.9 = **163.9 EUR**. That is NOT what Said intended.

If Said locked these rates as **net prices** (before tax), then the 149 EUR becomes 163.9 EUR to the guest — this may or may not be intended.

### What We Don't Know

The lock source (`data/finance/rates.json`) says: "Said Thaifa via HotelRunner, confirmed by WhatsApp (Jan 2026)." We do not know whether those rates are:

- **Option A: Gross (tax-inclusive)** — guest pays exactly this amount. Expedia would need to be reconfigured to "Yes, taxes included in rate" OR Said must enter tax-exclusive amounts into Expedia.
- **Option B: Net (tax-exclusive)** — Said intends these as base prices, VAT added on top. The current Expedia setting is correct, and guests pay +10%.

### Check Against HotelRunner

HotelRunner is the PMS where Said originally set these rates. The Expedia setting was configured separately. If HotelRunner rates are gross (inclusive), the two systems may be configured inconsistently.

### What Omar Must Decide

1. **Are the rates.json values gross or net?** Ask Said: "The rates you set — 149 EUR for R02, 329 EUR for R07, etc. — is that what the guest pays in total, or is that before taxes?"

2. **Should Expedia add VAT on top, or include it?** Once Omar knows the answer to #1, update Expedia accordingly before the listing goes live.

3. **Additional taxes collected at property:** 3 MAD Taxe de Sejour + 5 MAD Tourism Promotion Tax are collected directly — not through Expedia. These need to be disclosed in our check-in procedures so the guest is not surprised.

### Financial Impact Illustration

| Scenario                          | R07 rate in Expedia           | Guest pays | Difference |
| --------------------------------- | ----------------------------- | ---------: | ---------- |
| Current config (VAT added on top) | 329 EUR                       |  361.9 EUR | +32.9 EUR  |
| If Said meant gross rate          | 299 EUR (to make total = 329) |  328.9 EUR | ~correct   |

If the listing goes live with the wrong configuration, every booking is either overcharging guests (damaging trust and reviews) or undercharging (reducing revenue). This must be resolved before Expedia goes live.

---

## Summary Table

| Data Point                                | Source  | In Our Files?        | Action                            |
| ----------------------------------------- | ------- | -------------------- | --------------------------------- |
| Cancellation: 72h window, 1st night + tax | Expedia | NO (was TODO)        | Integrate to property-config.json |
| Payment: Visa, Mastercard, Debit          | Expedia | Partial (notes only) | Update billing.json               |
| Payment: No deposit required              | Expedia | NO                   | Add to property-config.json       |
| VAT: 10%, added to rate                   | Expedia | null in billing.json | CRITICAL — resolve before go-live |
| Taxe de Sejour: 3 MAD/night               | Expedia | null in billing.json | Integrate after VAT decision      |
| Tourism Promotion Tax: 5 MAD/night        | Expedia | null in billing.json | Integrate after VAT decision      |
| Languages: Arabic, Dutch, English, French | Expedia | NO                   | Add to property-config.json       |
| Property ID: 114807934                    | Expedia | NO                   | Add to channels.json              |
| Expedia tax team pending                  | Expedia | NO                   | Create tracking item              |
| Timezone: GMT (Casablanca)                | Expedia | Implicit             | No action needed                  |
| Billing currency: MAD                     | Expedia | YES (matches)        | No action needed                  |

---

## Remaining Gaps (not addressable from this extraction)

The Expedia extraction covers Step 3 of 12. The following are still unknown and not covered:

- **Steps 4–7:** Room-level amenities, room configurations, specific rates loaded into Expedia, rate plans, availability calendar
- **Step 9:** Photos loaded into Expedia (may differ from our data/rooms/)
- **Step 10:** Tax step (may reveal additional configuration)
- **Step 11:** Regulatory information

These steps should be extracted in a follow-up browser-agent session.

---

_Report generated 2026-02-20 | Source data: expedia-partner-central-extraction.md (step 3 of 12)_
_Cross-referenced against: billing.json, rates.json, channels.json, property-config.json, said-data-validation-checklist.md_
