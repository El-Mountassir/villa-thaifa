# Expedia Partner Central — Policies and Settings Extraction

**Source URL:** https://apps.expediapartnercentral.com/onboarding/policiesAndSettings?htid=114807934
**Property ID:** 114807934 (Villa Thaifa)
**Extracted:** 2026-02-20
**Page:** Step 3 of 12 — Onboarding Wizard
**Status:** Read-only extraction. No fields modified.

---

## Onboarding Progress Context

This is step 3 of a 12-step onboarding wizard. Steps:

1. basicPropertyHotelier
2. contract
3. **policiesAndSettings** (current — extracted here)
4. modularAmenities
5. roomsAndRates
6. ratePlans
7. ratesAndAvailability
8. promotions
9. photos
10. taxes
11. regulatory
12. connectivitySettings

---

## Section 1: Languages Spoken at Property

**Field:** Which languages are spoken at your property?

**Currently selected:**

- Arabic (checked)
- Dutch (checked)
- English (checked)
- French (checked)

---

## Section 2: Payment Methods

**Field:** Which payment methods do you accept at your property?

### Credit / Debit Cards

- Credit / debit cards: **CHECKED (enabled)**

**Types of card you accept:**

| Card Type         | Accepted       |
| ----------------- | -------------- |
| Debit cards       | YES (checked)  |
| JCB International | NO (unchecked) |
| Visa              | YES (checked)  |
| Discover          | NO (unchecked) |
| Mastercard        | YES (checked)  |
| Carte Blanche     | NO (unchecked) |
| American Express  | NO (unchecked) |
| UnionPay          | NO (unchecked) |
| Diners Club       | NO (unchecked) |

### Other Settings

| Option                                                        | Value          |
| ------------------------------------------------------------- | -------------- |
| Installments payments offered at front desk (for locals only) | NO (unchecked) |
| Cash                                                          | YES (checked)  |

**Summary:** Property accepts Debit cards, Visa, Mastercard, and Cash.

---

## Section 3: Deposits

**Field:** Do you require any deposits?
**Value: NO** (the "No" button is selected)

---

## Section 4: Default Cancellation Policy

**Note:** "This will be your default while you're getting your property set up. You'll be able to add new policies or modify the policies for specific rooms or units later on."

### Property Time Zone

**Value: (GMT) Casablanca, Monrovia** (selected)

### Cancellation Policy Options

Cancellation cutoff time: **18:00** (local property time)

| Option                      | Selected       |
| --------------------------- | -------------- |
| 24-hour cancellation window | NO             |
| 48-hour cancellation window | NO             |
| 72-hour cancellation window | YES (selected) |
| Non-refundable              | NO             |

**Active policy: 72-hour cancellation window**

**Policy description:**

- Travelers who cancel 72 hours or more before 18:00 on the day of check-in are charged **no fee**.
- Travelers who cancel less than 72 hours before 18:00 on the day of check-in (including no-shows) are charged: **1st night + tax**

### Cancellation Fee (for late cancellations)

**Value: 1st night + tax** (selected from dropdown)

Other available options (not selected):

- 50% of booking amount
- 100% of booking amount

---

## Section 5: Taxes and Fees

**Field:** Will these taxes be included in your room rate?

**Applicable tax:** 10.00% VAT (Value Added Tax)

| Option                          | Selected       |
| ------------------------------- | -------------- |
| Yes, taxes are included in rate | NO             |
| No, add these taxes to the rate | YES (selected) |

**Current setting: Taxes are NOT included in the rate — they are added on top.**

Example (when tax is not included):

- Rate given to Expedia: 80 MAD
- Taxes/fees: 20 MAD
- Traveler pays: 100 MAD

### Taxes Collected from Guests at Property (not via Expedia)

| Tax                   | Amount |
| --------------------- | ------ |
| Taxe de Sejour        | 3 MAD  |
| Tourism Promotion Tax | 5 MAD  |

### Tax Team Assistance

**Field:** Request tax team assistance (checkbox)
**Value: CHECKED** — Tax team has been requested to contact the property before publishing.

---

## Section 6: Billing Currency (Payment to Expedia Group)

**Field:** What currency would you like to use to pay Expedia Group?

**Business model:** Expedia Traveler Preference — travelers can choose to pay property directly or via Expedia Group first.

**Billing currency:** Moroccan Dirhams (MAD) — selected

Available options:

- British Pounds Sterling (GBP)
- Euros (EUR)
- Moroccan Dirhams (MAD) ← **selected**
- US Dollars (USD)

---

## Notes and Observations

1. **Incomplete fields:** The "Default cancellation policy" section shows the timezone dropdown is set but the page was still partially loading when first captured. The final state shows Casablanca, Monrovia (GMT) timezone confirmed.

2. **Tax handling:** Property uses the "add taxes to rate" model. The 10% VAT is added on top. Additionally, 3 MAD Taxe de Sejour and 5 MAD Tourism Promotion Tax are collected directly from guests at the property.

3. **"Request tax team assistance" is checked** — this means Expedia's tax team is supposed to contact the property before the listing goes live. This may be a blocker or pending action.

4. **Billing currency = MAD** — consistent with the property being in Morocco.

5. **Languages: 4 set** — Arabic, Dutch, English, French. This is broader than typical; Dutch may have been added for European market coverage.

6. **Cancellation: 72h window with 1st night + tax penalty** — This is a moderately flexible policy. No-shows charged same as late cancellations.

7. **No deposits required** — guests are not required to pay a deposit.

8. **Page is Step 3 of 12** — this is an onboarding wizard, meaning the listing may not yet be fully published. Other steps (amenities, rooms/rates, photos, etc.) may also have data to extract.

---

## Screenshots

Screenshots were captured during extraction but not saved as files (browser-only capture). The page loaded successfully without any login required — the browser session was already authenticated as Said Thaifa / property owner.

---

_Extracted by browser-agent on 2026-02-20. Read-only. No changes made to any fields._
