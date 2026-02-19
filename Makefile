.PHONY: sync test verify-contracts verify-domain verify-rooms
.PHONY: structure-cards structure-filtered structure-update

sync:
	uv sync

verify-contracts:
	uv run python scripts/validate_contracts.py

verify-domain:
	uv run python scripts/domain_verify.py

verify-rooms: verify-contracts verify-domain

test:
	uv run pytest

# ===========================================
# Structure Documentation Targets
# ===========================================

# Generate role-based structure cards
structure-cards:
	@echo "Generating structure cards..."
	@uv run python scripts/structure/generate_structure_cards.py --all

# Generate filtered tree output (excludes binary/cache files)
structure-filtered:
	@echo "Generating filtered structure tree..."
	@tree -I "$$(cat .structureignore | grep -v '^#' | grep -v '^$$' | tr '\n' '|')" --dirsfirst -L 3 > docs/core/STRUCTURE-filtered.txt

# Update all structure documentation
structure-update: structure-filtered structure-cards
	@echo "Structure documentation updated."
