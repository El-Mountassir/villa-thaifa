# Property Database Migration Summary

This document summarizes the database migration state for Villa Thaifa, based on the extraction from `property.db`.

## Metadata

- **Source File**: `property.db` (SQLite)
- **Extraction Date**: 2026-02-13
- **Objective**: Full data extraction for system redesign.

### Tables Overview

| Table Name  | Record Count |
| ----------- | ------------ |
| `rooms`     | 12           |
| `beds`      | 22           |
| `amenities` | 94           |

---

## Database Schema

### 🏠 Rooms Table

- **Primary Key**: `id`
- **Fields**:
  - `id`: TEXT (e.g., R01-R12)
  - `expedia_type`: TEXT
  - `internal_name`: TEXT
  - `floor`: TEXT
  - `occupancy_adults`: INTEGER
  - `size_m2`: REAL
  - `is_smoking`: BOOLEAN
  - `has_kitchen`: BOOLEAN
  - `base_rate_mad`: REAL
  - `verification_status`: TEXT (DRAFT | PENDING_SAID | VERIFIED)

### 🛏️ Beds Table

- **Primary Key**: `id`
- **Foreign Key**: `room_id` -> `rooms.id`
- **Fields**:
  - `id`: INTEGER
  - `room_id`: TEXT
  - `type`: TEXT (King, Sofa Bed)
  - `width_cm`: INTEGER
  - `count`: INTEGER

### ✨ Amenities Table

- **Primary Key**: `id`
- **Foreign Key**: `room_id` -> `rooms.id`
- **Fields**:
  - `id`: INTEGER
  - `room_id`: TEXT
  - `category`: TEXT (View, Outdoor, Bathroom, Climate, Layout, Hardware)
  - `name`: TEXT
  - `value`: BOOLEAN

---

## Statistics & Summary

### Room Types

- **Triple Room**: 3
- **Double Room**: 3
- **Executive Suite**: 1
- **Suite**: 2
- **Family Suite**: 2
- **Presidential Suite**: 1

### Floor Distribution

- **Rez-de-chaussée**: 4
- **Ground Floor**: 2
- **1er étage**: 5
- **Unknown**: 1

### Bed Inventory

- **King**: 12
- **Sofa Bed**: 10

### Amenity Categories

- **View**: 16
- **Outdoor**: 12
- **Bathroom**: 24
- **Climate**: 24
- **Layout**: 18
