# Decision: Room Pricing Confirmed

**Date:** 2026-02-19
**Source:** HotelRunner platform screenshot
**Status:** Confirmed — all 12 rooms priced and locked

## Confirmed Rates (EUR, per night)

| Room | Rate (EUR) | Category                    |
|------|------------|-----------------------------|
| R01  | 169€       | Chambre Triple De Luxe      |
| R02  | 149€       | Chambre Double De Luxe      |
| R03  | 169€       | Chambre Triple De Luxe      |
| R04  | 159€       | Chambre Double Superieure   |
| R05  | 159€       | Chambre Double Superieure   |
| R06  | 179€       | Suite Executive             |
| R07  | 329€       | Suite De Luxe King Size     |
| R08  | 169€       | Chambre Triple De Luxe      |
| R09  | 189€       | Suite Familiale             |
| R10  | 179€       | Suite                       |
| R11  | 189€       | Suite Familiale             |
| R12  | 449€       | Suite Presidentiel          |

## Notable

- R7 (329€) and R12 (449€) confirmed at premium pricing — these are the property's flagship suites.
- Previous file had stale/unverified rates for R02, R04, R05, R06 (marked `owner_pending`).

## Changes Applied

`data/finance/rates.json` updated:
- R02: 159€ → 149€
- R04: 149€ → 159€
- R05: 149€ → 159€
- R06: 169€ → 179€
- `data_confidence` upgraded from `owner_pending` to `confirmed`
- `last_updated` set to 2026-02-19
