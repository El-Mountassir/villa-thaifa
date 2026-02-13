.PHONY: sync verify-rooms verify-contracts verify-unique verify-domain test

sync:
	uv sync

verify-contracts:
	uv run python scripts/validate_contracts.py

verify-unique:
	uv run python scripts/check_unique_info.py --source data/core/property/inventory/rooms/rooms-4.md --canonical data/core/property/inventory/rooms/rooms.md

verify-domain:
	uv run python scripts/domain_verify.py

verify-rooms: verify-contracts verify-domain

test:
	uv run pytest
