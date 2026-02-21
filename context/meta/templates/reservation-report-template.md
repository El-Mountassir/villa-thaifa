---
title: 'Reservation Exploration Report'
author: '[AI Agent / Omar]'
date: 'YYYY-MM-DD'
lang: en
---

## Template: Reservation Exploration Report

> **Version**: 0.1.0-alpha.0 | **Based on**: Hotelogix, Cloudbeds, Smartsheet (3 sources triangulation)
> **Usage**: Villa Thaifa operational reports

---

## Instructions for use

1. Copy this template to `~/Templates/ai/agents/clis/{ai-agent-cli}/output/YYYY/QQ/reports/{description}.md`
2. Fill each section with current data
3. Remove non-applicable sections
4. Add custom sections if necessary

---

## [REPORT TITLE]

**Exploration Date**: YYYY-MM-DD HH:MM
**Platform**: HotelRunner
**Explorer**: [AI Agent / Omar]
**Status**: 🟢 Completed | 🟡 Partial | 🔴 Blocked

---

## 1. Executive Summary

### 1.1 Key Figures

| Metric               | Value | Trend |
| -------------------- | ----- | ----- |
| Pending reservations | X     | ↑↓→   |
| Check-ins today      | X     |       |
| Check-outs today     | X     |       |
| Occupied rooms       | X/12  |       |
| Occupancy rate       | X%    |       |

### 1.2 Urgent Alerts

| Priority | Alert         | Action Required | Deadline    |
| -------- | ------------- | --------------- | ----------- |
| 🔴 P0    | [Description] | [Action]        | [Date/Time] |
| 🟠 P1    | [Description] | [Action]        | [Date]      |

### 1.3 3-Point Summary

1. **Key point 1**: [Major discovery]
2. **Key point 2**: [Major discovery]
3. **Key point 3**: [Major discovery]

---

## 2. Pending Reservations

### 2.1 Overview

| Total Pending | Urgent (< 24h) | This week | This month |
| ------------- | -------------- | --------- | ---------- |
| X             | X              | X         | X          |

### 2.2 Reservation Details

| #   | Ref.   | Guest Name | Room | Type   | Check-in | Check-out | Nights | Source       | Amount  | Status   | Action        |
| --- | ------ | ---------- | ---- | ------ | -------- | --------- | ------ | ------------ | ------- | -------- | ------------- |
| 1   | HR-XXX | [Name]     | [N°] | [Type] | DD/MM    | DD/MM     | X      | [OTA/Direct] | XXX MAD | [Status] | [Action req.] |
| 2   |        |            |      |        |          |           |        |              |         |          |               |

### 2.3 Status Legend

| Status       | Meaning               | Action Type            |
| ------------ | --------------------- | ---------------------- |
| `PENDING`    | Awaiting confirmation | Confirm or cancel      |
| `HOLD`       | Temporarily blocked   | Check expiration delay |
| `WAITLIST`   | Waitlist              | Propose alternative    |
| `INCOMPLETE` | Missing info          | Contact guest          |

---

## 3. Confirmed Reservations (Upcoming)

### 3.1 Expected Arrivals

| Date  | Ref. | Guest Name | Room | Type | Nights | Source | Amount | Notes |
| ----- | ---- | ---------- | ---- | ---- | ------ | ------ | ------ | ----- |
| DD/MM |      |            |      |      |        |        |        |       |

### 3.2 Expected Departures

| Date  | Ref. | Guest Name | Room | Balance Due | Notes |
| ----- | ---- | ---------- | ---- | ----------- | ----- |
| DD/MM |      |            |      |             |       |

---

## 4. Room Occupancy

### 4.1 Status by Room

| Room | Type               | Status      | Occupant          | Check-out | Notes |
| ---- | ------------------ | ----------- | ----------------- | --------- | ----- |
| 1    | Deluxe Triple      | 🟢 Free     | -                 | -         |       |
| 2    | Deluxe Double      | 🔵 Occupied | [Name]            | DD/MM     |       |
| 3    | Deluxe Triple      | 🟢 Free     | -                 | -         |       |
| 4    | Superior Double    | 🟡 Pending  | [Name?]           | DD/MM     |       |
| 5    | Superior Double    | 🟢 Free     | -                 | -         |       |
| 6    | Executive Suite    | 🟢 Free     | -                 | -         |       |
| 7    | King Suite         | 🟢 Free     | -                 | -         |       |
| 8    | Deluxe Triple      | 🟢 Free     | -                 | -         |       |
| 9    | Family Suite       | 🟢 Free     | -                 | -         |       |
| 10   | Suite              | 🟢 Free     | -                 | -         |       |
| 11   | Family Suite       | 🟡 Pending  | [Current mission] | 21/12     |       |
| 12   | Presidential Suite | 🟢 Free     | -                 | -         |       |

### 4.2 Legend

| Code | Meaning                    |
| ---- | -------------------------- |
| 🟢   | Free / Available           |
| 🔵   | Occupied                   |
| 🟡   | Pending reservation        |
| 🔴   | Out of order / Maintenance |
| ⚪   | Blocked (house use)        |

---

## 5. Analysis

### 5.1 Reservation Sources

| Source           | Quantity | % Total | Trend |
| ---------------- | -------- | ------- | ----- |
| Direct (Walk-in) | X        | X%      |       |
| Website          | X        | X%      |       |
| Booking.com      | X        | X%      |       |
| Expedia          | X        | X%      |       |
| Other OTAs       | X        | X%      |       |

### 5.2 Observed Patterns

- **Pattern 1**: [Description and implications]
- **Pattern 2**: [Description and implications]

### 5.3 Identified Risks

| Risk     | Probability     | Impact                   | Mitigation |
| -------- | --------------- | ------------------------ | ---------- |
| [Risk 1] | High/Medium/Low | Critical/Important/Minor | [Action]   |

---

## 6. Recommended Actions

### 6.1 Immediate Actions (P0-P1)

| #   | Action   | Owner | Deadline | Dependency |
| --- | -------- | ----- | -------- | ---------- |
| 1   | [Action] | [Who] | [When]   | [Blocker?] |

### 6.2 Actions This Week (P2-P3)

| #   | Action   | Owner | Deadline |
| --- | -------- | ----- | -------- |
| 1   | [Action] | [Who] | [When]   |

### 6.3 Backlog (P4-P5)

- [ ] [Future action 1]
- [ ] [Future action 2]

---

## 7. Appendices

### 7.1 Navigation Logs

```text
[HH:MM] Action performed
[HH:MM] Page visited
[HH:MM] Extracted data
```

### 7.2 Screenshots

> Reference captured screenshots if relevant
> Format: `assets/screenshots/YYYY-MM-DD-description.png`

### 7.3 Technical Notes

- [Observations on the platform]
- [Bugs or unexpected behaviors]
- [Improvement suggestions]

---

## 8. Metadata

| Field                | Value                 |
| -------------------- | --------------------- |
| **Created by**       | [Agent/Omar]          |
| **Creation Date**    | YYYY-MM-DD HH:MM      |
| **Last Update**      | YYYY-MM-DD HH:MM      |
| **Version**          | 1.0                   |
| **Exploration Time** | X min                 |
| **Linked Files**     | [Links to other docs] |

---

## Template Sources

- [Hotelogix - 8 Must-Have Hotel PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Cloudbeds - 13 Hotel Audit Reports](https://www.cloudbeds.com/articles/6-reports-your-hotel-should-run-every-night/)
- [Smartsheet - Hotel Management Templates](https://www.smartsheet.com/content/hotel-management-templates)
- [DashThis - The Perfect Hotel Report](https://dashthis.com/blog/the-perfect-hotel-report/)
