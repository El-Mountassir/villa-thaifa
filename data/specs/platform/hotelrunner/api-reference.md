# HotelRunner Developer API Reference

> **Source**: Omar (shared 2025-12-29)
> **Full docs**: https://developers.hotelrunner.com
> **Base URL**: `https://app.hotelrunner.com/api/v2/apps`

---

## Authentication

All requests require:
- `token`: API token
- `hr_id`: HotelRunner property ID

**Location**: See `.env` file (root) for tokens. Reference: `.env.example`

---

## Endpoints

### 1. Get Room List

Retrieves all rooms/rates of the property.

```
GET /rooms?token={TOKEN}&hr_id={HR_ID}
```

**Response:**
```json
{
  "rooms": [
    {
      "rate_code": "HR:1",
      "inv_code": "HR:1",
      "availability_update": true,
      "restrictions_update": true,
      "price_update": true,
      "pricing_type": "guest_based",
      "name": "Standard Room",
      "description": "Standard Room Description",
      "policy": "Standard Room Policy",
      "room_capacity": 3,
      "adult_capacity": 2,
      "is_master": false,
      "shared": false,
      "channel_codes": ["bookingcom", "online", "hrs", "expedia"],
      "sales_currency": "EUR",
      "sell_online": true
    }
  ]
}
```

**Key Fields:**

| Field | Description | Sync Relevance |
|-------|-------------|----------------|
| `rate_code` | Rate code (`NR` = Non-refundable) | Rate identification |
| `inv_code` | Inventory group | Same group = shared availability |
| `availability_update` | Can update availability | **MUST be `true` for sync** |
| `restrictions_update` | Can update restrictions | Min-stay, stop-sale |
| `price_update` | Can update prices | Pricing sync |
| `channel_codes` | Connected channels | **MUST contain `bookingcom`** |
| `is_master` | Default/fallback room | If `true` = unmatched reservations go here |

---

### 2. Update Room

Updates availability, price, restrictions for a room type.

```
PUT /rooms/~
```

**Parameters:**

| Param | Required | Description |
|-------|----------|-------------|
| `inv_code` | Yes | Inventory code to update |
| `start_date` | Yes | Format: YYYY-MM-DD |
| `end_date` | Yes | Format: YYYY-MM-DD |
| `availability` | No | Number of rooms available |
| `price` | No | Room price |
| `stop_sale` | No | 1 = stop, 0 = open |
| `min_stay` | No | Minimum nights |
| `cta` | No | Close to arrival (1/0) |
| `ctd` | No | Close to departure (1/0) |
| `days` | No | Array [0-6], Sunday=0 |
| `channel_codes` | No | Array of channels to update |

**Response:**
```json
{
  "status": "ok",
  "transaction_id": "123456789"
}
```

---

### 3. Get Transaction Details

Check if an update succeeded or failed.

```
GET /infos/transaction_details?transaction_id={ID}&token={TOKEN}&hr_id={HR_ID}
```

**Response:**
```json
{
  "transaction": {
    "id": "883770514",
    "counts": {
      "failed": 1,
      "succeeded": 1,
      "in_progress": 0
    },
    "details": [
      {
        "id": 12529,
        "channel_code": "bookingcom",
        "state": "failed",
        "name": "Room Name",
        "code": "156754:8833301",
        "inv_code": "8833301",
        "created_at": "2025-05-16T08:01:29Z",
        "error_message": null
      }
    ]
  }
}
```

**Use Case**: After any update, check this endpoint to verify if Booking.com received the changes.

---

## Diagnostic Checklist

To diagnose sync issues, verify:

1. **Room has `availability_update: true`**
2. **Room has `bookingcom` in `channel_codes`**
3. **Room is NOT `is_master: true`** (master = fallback for unmapped)
4. **Transaction shows `state: succeeded`** for `bookingcom`

---

## Example: Check Villa Thaifa Room Config

```bash
curl "https://app.hotelrunner.com/api/v2/apps/rooms?token={TOKEN}&hr_id={HR_ID}"
```

Look for:
- "Double Room Superior" with 2 units
- `channel_codes` includes `bookingcom`
- `availability_update: true`

---

_API Reference — HotelRunner Developer Portal_
_Saved: 2025-12-29_
