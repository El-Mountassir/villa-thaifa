# 🏨 HotelRunner API Knowledge Base

> **Last updated**: January 12, 2026
> **Source**: https://developers.hotelrunner.com/

## 🔐 Authentication

- **Method**: HTTP Headers
- **Required Parameters**:
  - `HR_ID`: Property identifier code.
  - `TOKEN`: Secret key.
- **Acquisition**:
  - Directly in the "My Property" panel (admin) of the HotelRunner dashboard.
  - **Verdict**: Available for Villa Thaifa (Owner Access).

## 🚀 Capabilities

### 1. Inventory (Rooms & Rates)

- **Read**: `Get Room List` (`inv_code` codes for room types).
- **Update**: Availability, Rates, Stop Sell.
- **Utility**: Allows updating rates/availability from a central file (e.g., Markdown or future Excel).

### 2. Channels (OTAs)

- **Read**: List of connected channels.
- **Update**: Enable/Disable a channel.
- **Limitations**: Doesn't necessarily allow _configuring_ a channel for the first time (often requires OAuth UI), but useful for monitoring.

### 3. Reservations

- **Read**: History.
- **Push**: Webhooks for new reservations (JSON/XML).

## ⚠️ Limits

- **Rate Limit**: 250 requests/day (5/min).
- **Usage**: Sufficient for periodic synchronization, not for high-frequency real-time.

## ✅ API Action Plan

1.  Retrieve `HR_ID` and `TOKEN` in the dashboard (Manually or Browser Agent).
2.  Store in `.env.local` (e.g., `HOTELRUNNER_TOKEN`).
3.  Create tools (Node Scripts or MCP) to read inventory without a browser.

![API Auth Details](hr_api_auth_details.png)
