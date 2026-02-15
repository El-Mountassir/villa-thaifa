# Canonical

Active canonical assets that should be used as source of truth.

| Domain               | Canonical Path                                                   | Verification                                                                 | Notes                                              |
| -------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------- |
| rooms                | `data/core/property/inventory/rooms/rooms.md`                    | `python3 scripts/domain_verify.py` + `python3 scripts/validate_contracts.py` | Includes 12-row table and 12 multilingual profiles |
| rooms_reconciliation | `data/core/property/inventory/rooms/rooms-reconciliation-log.md` | manual + script-assisted checks                                              | Full audit trail for room consolidation            |
