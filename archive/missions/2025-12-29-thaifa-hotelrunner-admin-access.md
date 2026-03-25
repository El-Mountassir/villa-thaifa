<!-- Security: Credentials redacted 2026-02-22. Original contained plaintext credentials for HotelRunner. -->
---
id: 2025-12-29-hotelrunner-admin-access
type: mission
status: queued
priority: P1
title: "Obtain HotelRunner Admin Access for Omar"
description: "Contact HotelRunner support to request/configure admin access for omar@el-mountassir.com"
client: Villa Thaifa
requested-by: Omar
date-created: 2025-12-29
tags:
  - thaifa
  - hotelrunner
  - admin
  - credentials
---

# Obtain HotelRunner Admin Access for Omar

## Context

In the `.env` file, we have configured:

```text
HOTELRUNNER_ADMIN_EMAIL=omar@el-mountassir.com
HOTELRUNNER_ADMIN_PASSWORD=[REDACTED — see secure credential storage]
```

However, this admin access is **not yet active**. HotelRunner support must be contacted to configure it.

## Objective

Contact HotelRunner support to:

1. Ask how to add an additional admin (omar@el-mountassir.com)
2. Or ask if there is a specific procedure
3. Obtain instructions/confirmation

## Required Actions

- [x] Contact Ikram (HWS support) — see `data/admin/client/CONTACT.md`
- [ ] Explain the need: add an admin account for Omar
- [ ] Obtain instructions or confirmation
- [ ] Update `.env` if credentials change
- [ ] Test the connection

## Resources

- Support contact: see `data/admin/client/CONTACT.md`
- Current credentials: see `.env`
- HotelRunner documentation: see `data/operations/hotelrunner/`

## Notes

This mission is **blocking** for automated operations on HotelRunner with the Omar account. In the meantime, Mr. Thaifa's account can be used if necessary.

---

_Created: 2025-12-29_
