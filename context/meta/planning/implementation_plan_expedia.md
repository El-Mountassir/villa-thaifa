# Implementation Plan: Expedia Onboarding (Browser Automation)

> **Goal**: Complete the Expedia room onboarding using the browser tool to automate the manual entry of verified data from `property.db`.
> **Status**: Pivoting back to Browser Automation (Confirmed: API is locked during onboarding).

## 1. Strategy: The "1-by-1 Flow" (Automated)

Since the property is still in the "12-step onboarding" phase, the API is not yet accessible. We will use the agent's browser capabilities to:

1.  Open Expedia Partner Central.
2.  Navigate to the Room/Unit setup section.
3.  Fill each field automatically using data from our SQLite database.

## 2. Mapping & Logic

The logic remains identical to the API mapping, but instead of JSON keys, we target DOM elements.

| DB Column          | UI Action (Browser)                    |
| :----------------- | :------------------------------------- |
| `expedia_type`     | Select from Dropdown                   |
| `internal_name`    | Type into "Room Name"                  |
| `occupancy_adults` | Type into "Max Occupancy"              |
| `beds`             | Select bed types and quantities        |
| `amenities`        | Check/Uncheck boxes in the "Amenities" |

## 3. Implementation Script (`scripts/auto_onboard_browser.ts`)

1.  **DB Reader**: Fetch all verification_status = 'VERIFIED' rooms.
2.  **Browser Flow**:
    - `login()`: (Manual/User assisted if MFA is active).
    - `navigateToRooms()`: Go to the room setup step.
    - `processRoom(room)`:
      - Navigate to "Add Room".
      - Fill details.
      - Take a screenshot for verification.
      - Save.
3.  **Validation**: Post-save verification check.

## 4. Verification Plan

### Automated Verification

- **Screenshot Proofs**: For every room added, the script will capture a final state screenshot and save it to `archive/onboarding/Rxx_final.png`.
- **DB Sync**: Update `property.db` with a new `onboarded_at` timestamp.

### Manual Verification

- **User Review (Room 12)**: I will perform the first room (R12) and pause for a user review of the screenshot before proceeding to R01-R11.
