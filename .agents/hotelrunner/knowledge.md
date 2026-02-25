# 🏨 HotelRunner Knowledge Base

> **Last updated**: January 12, 2026
> **Status**: Discovery in progress

## 🔐 Access & Security

- **Login URL**: `https://app.hotelrunner.com`
- **Mechanism**: Email + Password.
- **Protection**:
  - **Google reCAPTCHA** (Motorcycle/bus images etc.) active on every login attempt.
  - Prevents full automation of login.
- **PROD Credentials**:
  - Owner Email: [See .secrets/.env]
  - Admin Email (Omar): [Not yet active]

## ⚠️ Constraints

- AI cannot pass the Captcha.
- **Solution**: The user must log in manually or HotelRunner Support must configure the connection.

## 🔗 OTA Connectivity

- **Current Status** (01/11/2026):
  - ✅ **Booking.com**: ACTIVE.
  - ❌ **Expedia**: Not connected.
  - ❌ **Airbnb**: Not connected.

![Channels Status](hr_channels_status.png)

### Connection Prerequisites (Discovered 01/12)

#### Airbnb

- **Type**: API / OAuth.
- **Action**: Click on "Connect". Requires being logged into the Airbnb Host account.
- **Difficulty**: Low (Just login).
  ![Airbnb Reqs](hr_airbnb_reqs.png)

#### Expedia

- **Type**: Form + Extranet Action.
- **Required Data**: `Hotel ID`.
- **Extranet Action**: Go to Expedia Partner Central -> Connectivity Settings -> Authorize "HotelRunner" for Rates & Inventory.
- **Difficulty**: Medium (Requires coordination).
  ![Expedia Reqs](hr_expedia_reqs.png)

## 🛏️ Room Inventory (Room Types)

List of the 8 room types configured in HotelRunner:

| Room Name                | Capacity |
| :----------------------- | :------- |
| **Double Room Superior** | 2        |
| **Deluxe Double Room**   | 2        |
| **Deluxe Triple Room**   | 3        |
| **Suite**                | 2        |
| **Deluxe King Suite**    | 3        |
| **Family Suite**         | 4        |
| **Executive Suite**      | 2        |
| **Presidential Suite**   | 4        |

![Rooms List](hr_rooms_list.png)
