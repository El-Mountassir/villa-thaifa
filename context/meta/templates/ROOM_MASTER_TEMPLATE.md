# Room Master Data Template (LOCKED GLOBALS V2)

> **Instructions**: Use this file to define the "Golden Record" for one room.
> **Strict Compliance**: All values MUST match the provided lists exactly.
> **Source**: Expedia Onboarding Form 2026 (Verified + User Inputs).

## 1. Room Type & Class

* **Room Type**: [SELECT from List]
* **Room Class**: [SELECT from List]

## 2. Basic Configuration

| Field | Value | Notes |
| :--- | :--- | :--- |
| **Smoking Policy** | [x] Non-smoking | **LOCKED** (Global) |
| **No. Bedrooms** | [Integer] | |
| **No. Living Spaces** | [Integer] | |

## 3. Sleeping Spaces

* **King Bed**: 180-210cm (Standard: 200cm checked).
* **Sofa Bed**: For Canapés.

## 4. Occupancy

| Field | Value |
| :--- | :--- |
| **Room Occupancy** | [Integer] |

## 5. Amenities: Bathroom

### Bathroom Type

* [x] Private bathroom | **LOCKED** (Global)
* **Number of Bathrooms**: 1

### Bath or Shower

* **Default**: [ ] Shower/tub combination (Combiné)
* **Exception (R12)**: [ ] Shower only (Douche Italienne)

### Essentials (ALL LOCKED - YES)

* [x] Free toiletries
* [x] Soap
* [x] Shampoo
* [x] Toilet paper
* [x] Towels
* [x] Hair dryer (**Available**)

## 6. Amenities: Kitchen

* **Has Kitchen?**: [x] No (**LOCKED GLOBAL**)
* **Kitchen Amenities**: None.

## 7. Amenities: Climate Control

* [x] Air conditioning (**Independent, Hot/Cold, Regulator**)
* [x] Heating (**In-room control**)

## 8. Amenities: Room View

**Does this room have a view?**: [x] Yes

* [ ] Garden view
* [ ] Pool view
* [ ] Mountain view

## 9. Amenities: Outdoor Space

**Does this room have an outdoor space?**: [x] Yes

* [ ] Furnished patio (RDC / Ground Floor)
* [ ] Furnished balcony (Etage / Upper Floor)

## 10. Amenities: Room Layout & Luxuries

* **Desk**: [ ] No (**LOCKED GLOBAL**)
* **Laptop friendly workspace**: [x] Yes (**LOCKED - All Rooms**)
* **Separate sitting area**: Only R07 & R12.
* **Separate dining area**: Only R07 & R12.
* **Private spa tub**: Pending.

## 11. Room Size

| Field | Value | Unit |
| :--- | :--- | :--- |
| **Size** | [Float] | Square meters |

## 12. Base Rate

| Field | Value | Currency |
| :--- | :--- | :--- |
| **Base Rate** | [Amount] | MAD |
