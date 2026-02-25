# 🏨 HotelRunner API

REST API integration for Villa Thaifa's property management system.

## Quick Reference

| Info           | Value                                                                                 |
| -------------- | ------------------------------------------------------------------------------------- |
| **Type**       | REST API (HR-v1)                                                                      |
| **Status**     | ⏸️ **On Hold - Analysis Required**                                                    |
| **Base URL**   | `https://am.hotelrunner.com/custom-apps/rest-api`                                     |
| **Rate Limit** | 250/day, 5/min                                                                        |
| **Docs**       | [developers.hotelrunner.com](https://developers.hotelrunner.com/custom-apps/rest-api) |

⚠️ **Project Paused**: Professional analysis of integration options required before proceeding.
See [OPTIONS-ANALYSIS.md](./OPTIONS-ANALYSIS.md) for details.

## Authentication

```bash
# Environment variables (.secrets/.env)
HOTELRUNNER_TOKEN=<pending>
HOTELRUNNER_HR_ID=<pending>
```

## Capabilities

✅ **Rooms**: Get room list, manage inventory
✅ **Reservations**: Retrieve bookings, real-time updates
✅ **Calendar**: Update rates and availability
✅ **Webhooks**: Push notifications for booking changes

## Setup Status

- [x] Research completed - API location found
- [x] Integration options identified (HR-v1 vs OTA-2015b)
- [x] Documentation structure created
- [x] Form requirements understood
- [ ] ⏸️ **PAUSED**: Options analysis in progress
- [ ] Decision on integration approach
- [ ] App created in HotelRunner dashboard
- [ ] Credentials obtained
- [ ] Connection tested
- [ ] Source enabled

## Next Steps

1. **Complete options analysis** - See [OPTIONS-ANALYSIS.md](./OPTIONS-ANALYSIS.md)
2. **Decide on integration approach** (API vs browser automation vs other)
3. **Only then**: Proceed with implementation

**Rationale**: Professional approach requires evaluating all alternatives before committing to a solution.

See [SETUP.md](./SETUP.md) for detailed progress tracking.
