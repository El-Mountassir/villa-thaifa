# Incident: WebFetch Access Errors During Sync Investigation

| Field     | Value                        |
| --------- | ---------------------------- |
| Date/Time | 2025-12-29 ~14:00            |
| Severity  | 🟡 Minor                     |
| Type      | HTTP Errors / Access Blocked |
| Status    | Open                         |

---

## Context

During investigation of HotelRunner ↔ Booking.com sync issues, attempted to fetch documentation from external sources to understand room mapping and channel manager configuration.

---

## Symptoms

### Error 1: HotelRunner Support (404)

```
URL: https://support.hotelrunner.com/en/knowledge-base/i-have-created-a-new-room-type-on-the-sales-channel-but-it-does-not-appear-on-the-hotelrunner-panel-what-should-i-do/
Error: Request failed with status code 404
```

### Error 2: Cloudbeds Documentation (403)

```
URL: https://myfrontdesk.cloudbeds.com/hc/en-us/articles/210935118-Room-mapping-guidelines
Error: Request failed with status code 403
```

### Error 3: HotelRunner Developers (Blocked)

```
URL: https://developers.hotelrunner.com/custom-apps/rest-api/inventory/get-room-list
Error: Unable to verify if domain developers.hotelrunner.com is safe to fetch
```

---

## Impact

- Could not access full API documentation
- Had to rely on WebSearch snippets instead of full pages
- Omar manually provided API documentation as workaround

---

## Action Taken

1. **Alternative found**: Used WebSearch to get summarized information
2. **Omar provided**: Full API documentation copy-pasted in chat
3. **Saved**: API reference to `data/specs/platform/hotelrunner/api-reference.md`

---

## Resolution

Partial - Omar provided the most critical documentation manually.

For future access to `developers.hotelrunner.com`:

- Enable Chrome extension
- Use Chrome as fallback for blocked domains

---

## Prevention

1. **Added to CLAUDE.md**: Web Access & Chrome priority rules
2. **Incident system**: Now properly tracking access issues
3. **Future**: Consider MCP for HotelRunner (Omar mentioned this is planned)

---

## Affected URLs for Future Reference

| URL                          | Status  | Alternative        |
| ---------------------------- | ------- | ------------------ |
| `support.hotelrunner.com`    | 404     | WebSearch + Chrome |
| `myfrontdesk.cloudbeds.com`  | 403     | WebSearch          |
| `developers.hotelrunner.com` | Blocked | Chrome required    |

---

_Incident logged: 2025-12-29_
