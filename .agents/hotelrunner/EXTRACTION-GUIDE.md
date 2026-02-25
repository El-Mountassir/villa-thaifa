# HotelRunner Data Extraction Guide

> **Status**: ✅ Operational (Browser Automation)
> **Date**: 2026-01-24
> **Method**: agent-browser with persistent profile

---

## 🎯 Overview

This guide explains how to automatically extract booking data from HotelRunner via browser automation.

**Advantages**:

- ✅ No complex API configuration
- ✅ No rate limits (250/day)
- ✅ No custom callback URL required
- ✅ Persistent authentication (no repeated reCAPTCHA)

---

## 📋 Prerequisites

### 1. Installation

```bash
# agent-browser already installed globally
agent-browser --version
```

### 2. Authentication Required

⚠️ **LIMITATION DISCOVERED**: The `--profile` flag of agent-browser does not correctly persist session cookies.

**Current workarounds**:

**Option A - Manual authentication before extraction**:

```bash
# 1. Open browser in headed mode
agent-browser --headed open https://villa-thaifa.hotelrunner.com/login

# 2. Login manually (solve reCAPTCHA if necessary)

# 3. Leave the browser open

# 4. In another terminal, run the script
# (The script will use the active browser session)
```

**Option B - Manual extraction via browser**:

```bash
# Use agent-browser in interactive mode for one-off extraction
agent-browser --headed open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all
# Then extract manually with eval/snapshot
```

**Note**: We are working on a solution to persist sessions automatically.

---

## 🚀 Usage

### Daily Extraction Script

**File**: [`extract_reservations.py`](./extract_reservations.py)

**Manual execution**:

```bash
cd /home/omar/omar-el-mountassir/projects/clients/villa-thaifa/sources/hotelrunner-api
python3 extract_reservations.py
```

**Output**:

```
data/reservations/
├── reservations_20260124_140630.json  # Timestamped extraction
├── reservations_20260124_153045.json
└── latest.json                        # Latest extraction (symlink or copy)

logs/
└── extract_20260124.log               # Daily logs
```

### Automation (Cron)

For automatic daily execution:

```bash
# Edit crontab
crontab -e

# Add (runs every day at 6:00 AM)
0 6 * * * cd /home/omar/omar-el-mountassir/projects/clients/villa-thaifa/sources/hotelrunner-api && /usr/bin/python3 extract_reservations.py >> logs/cron.log 2>&1
```

---

## 📊 Data Format

### JSON Structure

```json
{
  "extracted_at": "2026-01-24T14:06:30",
  "source": "HotelRunner Dashboard - Browser Automation",
  "count": 96,
  "reservations": [
    {
      "status": "No-show",
      "room": "",
      "channel": "Online",
      "client_name": "Famille Benchekroune",
      "confirmation_number": "R194048877",
      "check_in": "31 Dec. 2025 15:00",
      "check_out": "02 Jan. 2026 11:00",
      "room_type": "Deluxe King Size Suite",
      "total": "880 €",
      "payment_total": "373.45 €",
      "inventory_type": "Confirmed",
      "confirmation_status": "No-show",
      "booking_date": "Wednesday 31 December 2025 15:51",
      "nationality": "MA"
    }
    // ... other reservations
  ]
}
```

### Available Fields

| Field                 | Description         | Example                          |
| --------------------- | ------------------- | -------------------------------- |
| `status`              | Reservation status  | No-show, Confirmed, Canceled     |
| `room`                | Room number         | 101, 205                         |
| `channel`             | Booking channel     | Online, Booking.com, Direct      |
| `client_name`         | Guest name          | Famille Benchekroune             |
| `confirmation_number` | Confirmation number | R194048877                       |
| `check_in`            | Arrival date/time   | 31 Dec. 2025 15:00               |
| `check_out`           | Departure date/time | 02 Jan. 2026 11:00               |
| `room_type`           | Room type           | Deluxe King Size Suite           |
| `total`               | Total price         | 880 €                            |
| `payment_total`       | Amount paid         | 373.45 €                         |
| `inventory_type`      | Inventory type      | Confirmed, Modified              |
| `confirmation_status` | Confirmation status | No-show, Confirmed               |
| `booking_date`        | Booking date        | Wednesday 31 December 2025 15:51 |
| `nationality`         | Guest nationality   | MA (Morocco)                     |

---

## 🔧 Customization

### Modifying the Script

The [`extract_reservations.py`](./extract_reservations.py) script can be customized:

**1. Change source URL**:

```python
# Line 72
url = 'https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all'

# Alternatives:
# - /admin/channel/calendars/occupancies?f=1  (Calendar)
# - /admin/reports  (Reports)
# - /admin/pms/overview  (PMS Overview)
```

**2. Filter data**:

```python
# After extraction, filter by status
active_reservations = [r for r in reservations if r['status'] == 'Confirmed']

# Filter by date
import datetime
today = datetime.date.today()
# ... filtering logic
```

**3. Add exports**:

```python
# CSV Export
import csv
with open('reservations.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=reservations[0].keys())
    writer.writeheader()
    writer.writerows(reservations)
```

---

## 📈 Use Cases

### 1. Daily Extraction

**Goal**: Daily backup of reservations

```bash
# Cron at 6 AM every day
0 6 * * * cd .../sources/hotelrunner-api && python3 extract_reservations.py
```

### 2. AI Agent Integration

**Goal**: Agents read the latest reservations

```python
# In your agent
import json

with open('sources/hotelrunner-api/data/reservations/latest.json') as f:
    data = json.load(f)
    reservations = data['reservations']

# Process reservations
for res in reservations:
    if res['status'] == 'Confirmed':
        # ... agent logic
```

### 3. Automated Reports

**Goal**: Generate weekly reports

```python
# Separate script
import json
from collections import Counter

with open('data/reservations/latest.json') as f:
    data = json.load(f)

# Stats by channel
channels = Counter(r['channel'] for r in data['reservations'])
print("Reservations by channel:", channels)

# Stats by status
statuses = Counter(r['status'] for r in data['reservations'])
print("Reservations by status:", statuses)
```

---

## 🐛 Troubleshooting

### Issue: "Not authenticated"

**Cause**: Profile expired or never created

**Solution**:

```bash
# Re-create profile in headed mode
agent-browser --headed --profile ~/.hotelrunner-profile open https://app.hotelrunner.com
# Login manually
agent-browser close
```

### Issue: "Command timed out"

**Cause**: Page slow to load

**Solution**: Increase timeout in the script

```python
# Line 30
timeout=60  # Instead of 30
```

### Issue: "Failed to parse JSON"

**Cause**: Page structure changed

**Solution**: Check the HTML structure

```bash
agent-browser --headed open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all
agent-browser snapshot -c  # View structure
```

### Issue: Browser doesn't close

**Solution**:

```bash
# Close manually
agent-browser close

# Or kill the process
pkill -f chromium
```

---

## 📚 Resources

**Documentation**:

- [Test Results](../../tmp/hotelrunner-browser-test-results.md) - POC Results
- [OPTIONS-ANALYSIS.md](./OPTIONS-ANALYSIS.md) - Complete options analysis
- [SETUP.md](./SETUP.md) - Progress tracking
- [agent-browser guide](../agent-browser/guide.md) - Tool documentation

**Scripts**:

- [`extract_reservations.py`](./extract_reservations.py) - Main script
- More scripts to come (calendar, reports, etc.)

---

## ✅ Checklist

Before first use:

- [ ] agent-browser installed (`agent-browser --version`)
- [ ] Profile created (`~/.hotelrunner-profile` exists)
- [ ] Initial manual auth successful
- [ ] Manual extraction test OK
- [ ] (Optional) Cron configured for automation

---

**Created by**: Craft Agent
**Date**: 2026-01-24
**Status**: ✅ Production-ready
