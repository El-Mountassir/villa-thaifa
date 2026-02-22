# Room Profile Template — Canonical Schema

> SCHEMA CONTRACT — Read before editing any room profile
>
> This template defines the canonical schema for ALL room profiles (data/rooms/R01-R12/profile.md).
>
> **MANDATORY**: Any new field or structural change MUST be applied to this template FIRST,
> then cascaded to all 12 room profiles in one operation. Never edit room profiles
> without first updating this template.
>
> Reference: AGENTS.md § Room Schema Change Protocol

---

# {RXX}: {Room Class} {Room Type} (Golden Record)

<!-- Header fields: quick-reference summary at the top of every profile.
     These duplicate key YAML values for human readability.
     Sync with the Structured Data YAML block below — no drift allowed. -->

- **Type**: {Room Type}
  <!-- e.g. Double Room, Triple Room, Suite. Must match expedia_type in YAML. -->
- **Class**: {Room Class}
  <!-- e.g. Standard, Deluxe, Superior, Junior Suite. Must match category_code in YAML. -->
- **Floor**: {Floor}
  <!-- e.g. Ground Floor (Rez-de-chaussée), First Floor (Étage). -->
- **Occupancy**: {N} Adults
  <!-- Maximum adult occupancy. Must match max_occupancy in YAML. -->
- **Size**: {N} m²
  <!-- Floor area in square meters. If disputed, add inline NOTE comment citing source and discrepancy. -->
- **Sleeping**:
  <!-- List every bed in the room. One bullet per bed type. -->
  - {Bed type} ({size in cm if applicable})
  <!-- e.g. 1 King Bed (200cm), 1 Sofa Bed, 2 Twin Beds -->
- **View**: {[x] View type | [ ] No view}
  <!-- Check all that apply: Garden view, Pool view, Mountain view, No view. -->
- **Outdoor**: {[x] Outdoor space description | [ ] No outdoor space}
  <!-- e.g. [x] Furnished patio (RDC), [x] Furnished balcony (Étage), [ ] No -->
- **Bathroom**: {[x] Bath/shower type, [x] amenities}
  <!-- e.g. [x] Shower/tub combination, [x] Hair dryer. R12 exception: Shower only. -->
- **Kitchen**: {[x] Yes | [ ] No}
  <!-- All rooms are [ ] No — LOCKED GLOBAL. Only change if property adds a kitchenette room. -->
- **Climate**: {[x] Climate features}
  <!-- e.g. [x] Air conditioning (Independent), [x] Heating (Control). Both are LOCKED GLOBAL. -->
- **Layout**: {[x] Layout features}
  <!-- e.g. [x] Laptop friendly workspace, [ ] Desk (No), [x] Separate sitting area (R07/R12 only). -->
- **Features**: {Feature list}
  <!-- Room-specific features not covered above. e.g. Safe (Coffre fort). Append [assumed] if not on-site verified. -->
- **Mini bar**: {YES | NO | owner_pending} <!-- Confirmed presence of in-room mini bar. Source required. -->
- **Pricing**: {N} EUR
  <!-- Base nightly rate in EUR. Must match base_rate_eur in YAML. Add inline note if rate has an expiry date. -->

---

### {RXX} — {Room Class} {Room Type}

#### Identity

<!-- Canonical naming used internally and on French-language OTA listings. -->

- **FR Name**: {French room name}
  <!-- French display name. e.g. Triple Deluxe, Suite Junior. Used on Booking.com FR. -->
- **Internal Code**: {CATEGORY_CODE}
  <!-- Snake_case uppercase code. e.g. DELUXE_TRIPLE, JUNIOR_SUITE. Must match category_code in YAML. -->

---

#### Narrative

<!-- Human-readable descriptions. Used by agents for OTA copy, guest comms, and marketing.
     EN and FR must be semantically equivalent — not literal translations. -->

- **Description (EN)**: {English description}
  <!-- 1-2 sentences. Mention: room type, key bed(s), standout feature, floor/location within villa. -->
- **Description (FR)**: {French description}
  <!-- 1-2 sentences. Equivalent content to EN. Written for French-speaking OTA guests. -->
- **Tagline**: {Short tagline}
  <!-- Max 10 words. Positioning line for the room. e.g. Spacious garden retreat perfect for small families. -->

---

#### Marketing Hooks

<!-- Used by agents when drafting promotions, channel copy, or response templates. -->

- **Target Persona**: {Persona description}
  <!-- Who this room is best for. e.g. Couples with child, small families, value-conscious travelers. -->
- **Highlights**:
  <!-- 3 bullet points. Each = one concrete, guest-relevant selling point. -->
  - {Highlight 1}
  - {Highlight 2}
  - {Highlight 3}

---

#### OTA Fields

<!-- OTA-specific titles and short descriptions. Character counts are limits enforced by each platform.
     Titles must be in the platform's required language. Short descriptions must fit within char limits. -->

- **Expedia Title**: {Title} ({N} chars)
  <!-- English. Max ~60 chars. Format: {Class} {Type}, {View}. e.g. Deluxe Triple Room, Garden View -->
- **Booking.com Title**: {Title} ({N} chars)
  <!-- French for FR listings. Max ~50 chars. e.g. Chambre Triple de Luxe -->
- **Short Description (EN)**: {Description} ({N} chars)
  <!-- English. Max ~150 chars. Lead with size, key beds, standout feature. End with access/view detail. -->
- **Short Description (FR)**: {Description} ({N} chars)
  <!-- French. Same content as EN, adapted for FR readers. -->

---

#### Structured Data (YAML)

<!-- Machine-readable record. This is the authoritative queryable form of all room data.
     ALL header fields above must be derivable from this block.
     Keep in sync — if a header field changes, the YAML must change too (and vice versa). -->

```yaml
room_id: {RXX}
  # Canonical room identifier. Format: R + zero-padded number (R01, R02, ... R12).
room_number: '{NN}'
  # Zero-padded string. e.g. '01', '12'.
category_code: {CATEGORY_CODE}
  # Matches Internal Code above. e.g. DELUXE_TRIPLE.
internal_name: {Internal room name in English}
  # English display name. e.g. Deluxe Triple Room.
expedia_type: {Expedia room type string}
  # Must match Expedia platform room type. e.g. Triple Room.
booking_label: {Booking.com English label}
  # English label as shown on Booking.com. e.g. Deluxe Triple Room.
booking_label_fr: {Booking.com French label}
  # French label. e.g. Chambre Triple de Luxe.
floor: {Floor name in English}
  # e.g. Ground Floor, First Floor.
capacity: '{N} adults'
  # Human-readable string. e.g. '3 adults'.
max_occupancy: {N}
  # Integer. Maximum total adult occupancy.
smoking_allowed: false
  # LOCKED GLOBAL — always false.
has_kitchen: false
  # LOCKED GLOBAL — always false unless a kitchenette room is added.
size_m2: {N}
  # Integer or float. Floor area in square meters.
base_rate_mad: {N}
  # Base nightly rate in MAD (Moroccan Dirham). Integer.
base_rate_eur: {N}
  # Base nightly rate in EUR. Integer. Sync with Pricing header field above.
beds:
  # List all beds. One entry per bed type.
  - type: {bed_type}
      # Snake_case. e.g. king, queen, twin, sofa_bed, double.
    size_cm: {N}
      # Optional. Omit for beds without a standard size (e.g. sofa_bed).
    count: {N}
      # Number of beds of this type in the room.
views:
  # List of view types as strings. e.g. [garden], [pool], [mountain], [garden, pool].
  - {view_type}
access: {access type or null}
  # Outdoor access type. e.g. patio, balcony, null.
access_notes: {notes or null}
  # Free-text clarification. e.g. Ground floor direct garden access. or null.
outdoor: {Outdoor space description or null}
  # Human-readable. e.g. Furnished patio (Ground Floor), Furnished balcony (Upper Floor), null.
bathroom: {Bathroom description}
  # Semicolon-separated. e.g. Shower/tub combination; Hair dryer.
climate: {Climate description}
  # Semicolon-separated. e.g. Independent air conditioning; Heating control.
layout: {Layout description}
  # Semicolon-separated. e.g. Laptop-friendly workspace; Safe (Coffre fort) [assumed].
mini_bar: {confirmed | absent | owner_pending} # confirmed=verified present, absent=verified absent, owner_pending=awaiting Said
data_confidence: {owner_pending | verified | assumed}
  # owner_pending = needs Said/owner confirmation.
  # verified = confirmed on-site or by trusted source.
  # assumed = inferred from context, not explicitly confirmed.
status: {VERIFIED | DRAFT | NEEDS_REVIEW}
  # VERIFIED = fully reconciled and confirmed.
  # DRAFT = created but not yet checked against source.
  # NEEDS_REVIEW = flagged for correction.
```

---

#### Provenance

<!-- Traceability: where did this data come from? Required for auditability. -->

- **Legacy Features (Alias)**: {Alias list or "-"}
  <!-- Former names or tags used in legacy data sources. e.g. Jardin, Rez-de-chaussée. Use "-" if none. -->
- **Legacy Amenities (Alias)**: {Alias list or "-"}
  <!-- Amenity labels from legacy imports that map to current fields. Use "-" if none. -->
- **Profile Source**: {Source file(s)}
  <!-- Which legacy files were used to build this profile. e.g. rooms-2.md + rooms-4.md (alias enrichment). -->
- **Last Verified**: {YYYY-MM-DD}
  <!-- Date this profile was last confirmed against on-site reality or a trusted authority. -->

---

<!-- End of room profile template -->
