# 🏨 HotelRunner API

REST API integration for Villa Thaifa's property management system.

## Quick Reference

| Info | Value |
|------|-------|
| **Type** | REST API (HR-v1) |
| **Status** | ⏳ Credentials Pending |
| **Base URL** | `https://am.hotelrunner.com/custom-apps/rest-api` |
| **Rate Limit** | 250/day, 5/min |
| **Docs** | [developers.hotelrunner.com](https://developers.hotelrunner.com/custom-apps/rest-api) |

## Authentication

```bash
# Environment variables (.env.local)
HOTELRUNNER_TOKEN=<pending>
HOTELRUNNER_HR_ID=<pending>
```

## Capabilities

✅ **Rooms**: Get room list, manage inventory
✅ **Reservations**: Retrieve bookings, real-time updates
✅ **Calendar**: Update rates and availability
✅ **Webhooks**: Push notifications for booking changes

## Setup Status

- [x] App configuration form filled
- [ ] App created in HotelRunner dashboard
- [ ] Credentials copied to `.env.local`
- [ ] Connection tested
- [ ] Source enabled

## Next Step

**Complete app creation in HotelRunner dashboard** and copy TOKEN + HR_ID to `.env.local`.

See [guide.md](./guide.md) for detailed instructions.
