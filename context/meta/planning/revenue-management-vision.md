# Villa Thaifa — Revenue Management Vision

## Why

Villa Thaifa currently operates with fixed pricing deployed through a single OTA, leaving significant revenue on the table. Three structural problems drive this:

1. **Fixed pricing in a dynamic market.** Rates are locked until December 2026, meaning Villa Thaifa cannot respond to demand spikes, local events, competitor moves, or seasonal shifts. A room priced the same on a quiet Tuesday and a holiday weekend is a room under-priced half the time.

2. **Single-channel dependency.** 100% of distribution runs through Booking.com at a 25% commission rate. No leverage, no fallback, no direct booking channel. Every reservation costs a quarter of its value before operations begin.

3. **No market intelligence.** There is no system to monitor how Villa Thaifa is positioned against comparable properties in the Marrakech Palmeraie. Pricing decisions are made in the dark.

The opportunity cost compounds daily. The goal of this vision is to close that gap systematically.

---

## Current State (2026)

- **Rates:** Fixed pricing across all 12 rooms, locked in `data/finance/rates.json` through December 2026
- **Distribution:** Single OTA (Booking.com), 25% commission, managed via HotelRunner channel manager
- **Rooms:** Data cleanup in progress — not all 12 rooms are fully documented
- **Revenue intelligence:** None. No RevPAR tracking, no ADR benchmarking, no occupancy analytics
- **Competitive monitoring:** None

---

## Vision: What We Want to Achieve

A dynamic, data-driven revenue management system that:

- **Prices rooms based on real demand** — not static tables. Rates adjust to occupancy trends, local events, competitor positioning, and seasonal patterns.
- **Distributes across multiple OTAs** with optimized rates per channel, reducing Booking.com dependency and overall commission burden.
- **Positions Villa Thaifa competitively** in the Marrakech Palmeraie boutique market — neither the cheapest nor arbitrarily expensive, but correctly valued.
- **Maximizes RevPAR** (revenue per available room), the true measure of pricing effectiveness for a property of this size.
- **Grows direct booking share** over time, reducing OTA commission drag.

The system should be largely autonomous — AI agents monitoring, recommending, and (eventually) executing pricing decisions within parameters Said approves.

---

## Strategic Pillars

### 1. Complete Data Foundation _(prerequisite — in progress)_

Accurate room data is the baseline for everything else. Pricing cannot be differentiated or justified without complete, verified room profiles, amenity data, and accurate inventory. This phase is underway.

### 2. Competitive Intelligence

Automated monitoring of comparable properties in the Palmeraie — rates, availability, positioning. The goal is to know where Villa Thaifa sits in the market at any given moment without manual research.

### 3. Dynamic Pricing Engine

Demand-based rate adjustments driven by: occupancy levels, booking lead time, local events, seasonal patterns, and competitor rate signals. Pricing should respond to the market, not lag it by months.

### 4. Channel Optimization

Multi-OTA distribution with a deliberate channel strategy. This includes: rate parity decisions (where required by contract), channel-specific differentiation (where permitted), and a direct booking channel to capture commission-free reservations.

### 5. Performance Analytics

Real-time and historical tracking of RevPAR, ADR (average daily rate), occupancy rate, direct booking share, and commission cost per channel. These metrics are the feedback loop — without them, there is no way to know if the system is working.

---

## Prerequisites Before Implementation

The following must be true before building any revenue management system:

- [ ] All 12 rooms fully documented with verified, accurate data
- [ ] Multi-OTA distribution live (Expedia, Airbnb, Trip.com alongside Booking.com)
- [ ] Minimum 3–6 months of historical booking data collected
- [ ] Said's explicit approval on pricing flexibility parameters (floor rates, ceiling rates, blackout periods)
- [ ] Direct booking channel established (even minimal)

None of these are negotiable. A pricing engine built on incomplete data or a single-channel distribution system is not a revenue management system — it is noise.

---

## Success Metrics

| Metric                   | Direction        | What It Measures                             |
| ------------------------ | ---------------- | -------------------------------------------- |
| RevPAR                   | Increase         | Overall revenue efficiency per room          |
| ADR (Average Daily Rate) | Optimize         | Rate quality, not just volume                |
| Occupancy rate           | Balance with ADR | Avoid over-discounting to fill rooms         |
| OTA commission cost      | Decrease         | Channel mix improvement                      |
| Direct booking share     | Increase         | Long-term margin health                      |
| Booking lead time        | Monitor          | Demand signal and pricing flexibility window |

---

## Status

**Phase:** Vision captured. Research pending.

**Current constraint:** Fixed rates until December 2026. No action on dynamic pricing until prerequisites are met.

**Next:** Deep research on best-in-class revenue management approaches for boutique hotels (5–20 rooms) in the North African/Marrakech market. Research to cover: tooling options, channel manager integrations, competitive intelligence sources, and AI agent patterns for pricing automation.
