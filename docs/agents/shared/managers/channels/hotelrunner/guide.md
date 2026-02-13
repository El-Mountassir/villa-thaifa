# HotelRunner API Guide

## Overview

HotelRunner REST API (HR-v1) provides programmatic access to Villa Thaifa's property management system.

**Base URL**: `https://am.hotelrunner.com/custom-apps/rest-api`
**Documentation**: `https://developers.hotelrunner.com/custom-apps/rest-api`
**Rate Limit**: 250 requests/day, 5 requests/minute

## Authentication

The API uses TOKEN and HR_ID for authentication via headers.

### Credentials Location

**Environment Variables** (`.env.local`):

```bash
HOTELRUNNER_TOKEN=your_token_here
HOTELRUNNER_HR_ID=your_hr_id_here
```

### How to Get Credentials

1. Login to HotelRunner dashboard: `https://app.hotelrunner.com`
2. Navigate to **Custom Apps** (in main menu)
3. Click **"Créez votre app"** (Create your app)
4. Fill the form:
   - **Type**: PMS
   - **Integration Type**: HR-v1
   - **Permissions**: Check all boxes
5. After creation, go to **"Identifiants"** tab
6. Copy TOKEN and HR_ID to `.env.local`

## App Configuration

**Current App Details** (created 2026-01-24):

- **Name**: Villa Thaifa AI Automation (or Villa Thaifa PMS)
- **Type**: PMS (Property Management System)
- **Integration**: HR-v1 (REST API)
- **Contact Email**: omar@el-mountassir.com
- **Callback URL**: `https://localhost/hotelrunner/callback`
- **SSL Enforced**: Yes

### Permissions Enabled

✅ All permissions:

- Get room list
- Retrieve reservations
- Receive real-time reservation push updates (Confirmed, Modified, Cancelled)
- Update room calendar (rates & availability)

## API Capabilities

### 1. Inventory Management

**Get Room List**

```bash
# Retrieve all room types and their details
GET /inventory/rooms
```

**Update Calendar**

```bash
# Update rates and availability for specific dates
POST /inventory/calendar
```

### 2. Reservations

**Retrieve Reservations**

```bash
# Get reservation history and current bookings
GET /reservations
```

**Push Notifications** (Real-time webhooks):

- New reservation confirmed
- Existing reservation modified
- Reservation cancelled

### 3. Rate Limiting

⚠️ **Important**:

- **250 requests per day** maximum
- **5 requests per minute** maximum
- Plan your automation carefully to stay within limits

## Usage Examples

### Example 1: Fetch Today's Reservations

```python
import os
import requests

TOKEN = os.getenv('HOTELRUNNER_TOKEN')
HR_ID = os.getenv('HOTELRUNNER_HR_ID')

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'HR-ID': HR_ID
}

response = requests.get(
    'https://am.hotelrunner.com/custom-apps/rest-api/reservations',
    headers=headers,
    params={'date': '2026-01-24'}
)

reservations = response.json()
```

### Example 2: Update Room Availability

```python
import os
import requests

TOKEN = os.getenv('HOTELRUNNER_TOKEN')
HR_ID = os.getenv('HOTELRUNNER_HR_ID')

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'HR-ID': HR_ID,
    'Content-Type': 'application/json'
}

data = {
    'room_id': 'ROOM_001',
    'date': '2026-01-25',
    'available': 1,
    'rate': 150.00
}

response = requests.post(
    'https://am.hotelrunner.com/custom-apps/rest-api/inventory/calendar',
    headers=headers,
    json=data
)
```

## Webhook Configuration

For real-time reservation updates, HotelRunner will POST to your callback URL:

**Callback URL**: `https://localhost/hotelrunner/callback`

⚠️ **Note**: Update this URL when you deploy a production endpoint.

### Webhook Events

- `reservation.confirmed` - New booking received
- `reservation.modified` - Booking details changed
- `reservation.cancelled` - Booking cancelled

## Best Practices

1. **Cache Smartly**: Store room and rate data locally to minimize API calls
2. **Batch Operations**: Group multiple updates when possible
3. **Error Handling**: Implement retry logic with exponential backoff
4. **Monitor Rate Limits**: Track your daily/minute usage
5. **Secure Credentials**: Never commit TOKEN/HR_ID to git

## Troubleshooting

### Common Issues

**401 Unauthorized**

- Check TOKEN and HR_ID are correct in `.env.local`
- Verify credentials haven't expired

**429 Too Many Requests**

- You've hit rate limit (250/day or 5/min)
- Wait before retrying

**500 Server Error**

- Check HotelRunner API status
- Contact integrations@hotelrunner.com

## Support

**Technical Contact**: omar@el-mountassir.com
**HotelRunner Support**: integrations@hotelrunner.com
**API Documentation**: https://developers.hotelrunner.com/custom-apps/rest-api

## Next Steps

1. ⏳ **Waiting**: Complete app creation in HotelRunner dashboard
2. 📋 **Copy Credentials**: Get TOKEN and HR_ID from "Identifiants" tab
3. 💾 **Save to .env.local**: Add credentials to environment file
4. ✅ **Test Connection**: Run a simple API call to verify
5. 🚀 **Enable Source**: Set `"enabled": true` in config.json
