# Booking.com — Browser Agent Context

> **Last Updated:** 2026-02-21
> **Source:** Admin extranet scout session

## Access

- **Public listing**: https://www.booking.com/hotel/ma/riad-salim-amp-spa.html
- **Admin URL**: https://admin.booking.com
- **Credentials**: `.secrets/.env` (BOOKING_ADMIN_EMAIL + BOOKING_ADMIN_PASSWORD)
- **Hotel ID**: 5446847
- **Property**: Villa Thaifa (Riad Salim & Spa)

## Authentication Flow

1. Navigate to admin.booking.com
2. Enter email, then password
3. **2FA required**: SMS code sent to Said's phone (+21******0409)
4. Enter 6-digit OTP and click Verify
5. **AWS WAF CAPTCHA** may trigger after 2-3 page navigations (image puzzle, e.g. "Choose all the clocks")

## Session Persistence

- Sessions expire after hours (not days)
- Use `--user-data-dir=tmp/booking-profile` with Playwright to preserve session
- `storageState` JSON is alternative (save after login, reload next time)
- Re-authentication needed periodically — always plan for it
- Details: `context/meta/knowledge/booking-session-persistence.md`

## Extracted Pages (2026-02-21)

| Page | Status | Data |
|------|--------|------|
| Dashboard | Done | Finance summary, review score |
| Policies | Done | Check-in/out, children, pets, events, quiet hours |
| Amenities | Done | Room sizes, floors, equipment per room type |
| Facilities | BLOCKED (CAPTCHA) | Parking, spa, pool, garden details |
| Description | BLOCKED (CAPTCHA) | Official property description text |
| Reservations | Not attempted | Booking history, occupancy |

## Room Size Data (confirmed from admin)

| Booking.com Room Type | Size | Floor | Internal Rooms |
|---|---|---|---|
| Chambre Triple de Luxe | 44 m² | Ground | R01, R03, R08 |
| Chambre Double De luxe | 41 m² | Ground | R02 |
| Chambre Double Superieur | 24 m² | Ground | R04, R05 |
| Suite Executive | 40 m² | Upper | R06 |
| Suite De Luxe King Size | 61 m² | Upper | R07 |
| Suite Familiale | 41 m² | Ground | R09, R11 |
| Suite 10 | 41 m² | Ground | R10 |
| Suite Presidentiel | 82 m² | Ground | R12 |

## Key Learnings

- Playwright CLI can access both public and admin (with credentials)
- Use `--headed` flag to show the visible browser during automation
- CAPTCHA triggers are unpredictable — save progress frequently
- Always use `browser-agent` (not general-purpose) for any browser-related task

## Related Files

- Terrain map: `context/meta/knowledge/booking-admin-terrain-map.md`
- Extraction data: `context/meta/knowledge/booking-admin-extraction.md`
- Session research: `context/meta/knowledge/booking-session-persistence.md`
- Public scrape: `context/meta/knowledge/booking-com-data.md`

## Next Steps (for future sessions)

1. Solve CAPTCHA manually → extract facilities.html + request_change.html
2. Apply room sizes to canonical profiles (work-overview task #160)
3. Explore reservations page for occupancy data
