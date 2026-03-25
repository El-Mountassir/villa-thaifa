# Source Triangulation

**Date**: 2025-12-20

---

## Sources

### Source 1: Exploration Dossier Villa Thaifa

- **Type**: Practitioner (données internes réelles)
- **Evidence Quality**: Strong

**Key Claims**:
- Âge client = **78 ans** (pas "60+")
- 12 chambres, 9 types HotelRunner
- Commission Booking.com = **25%** (vs 15% standard — élevée)
- Note client = **9.3/10** Booking
- HotelRunner = Channel Manager actif
- PMS = **Aucun** (tout dans la tête de M. Thaifa)
- Lessons-learned documentées (ton, pattern Scout→Rapport→Action)

**Fichiers clés**:
- `state/current/rooms.md` — 12 chambres, pricing
- `docs/lessons-learned.md` — 3 leçons communication
- `projects/2025-12_booking-hotelrunner/` — Mission active

---

### Source 2: Hotelogix Blog — Hotel Reservation Reports

- **URL**: https://blog.hotelogix.com/hotel-reservation-report/
- **Type**: Practitioner (blog industrie)
- **Evidence Quality**: Moderate

**Key Claims**:
- KPIs essentiels: ADR, Occupancy, RevPAR
- Réservations par source (walk-in, OTAs, travel agents, corporate, website)
- Comparaisons MTD/YTD pour tendances
- Trial balance (guest ledger, AR, deposits)
- Forecasting 30 jours

**Application**:
- Enrichir le profil avec terminologie standard
- Préparer les questions discovery (KPIs manquants)

---

### Source 3: Cloudbeds — Hotel CRM System Guide

- **URL**: https://www.cloudbeds.com/articles/hotel-crm-system/
- **Type**: Official docs (vendor)
- **Evidence Quality**: Strong

**Key Claims**:
- Profil CRM = contact + historique + préférences + comportement
- Segmentation par: type de groupe, caractéristiques, comportements
- Intégration PMS/POS essentielle
- Seulement 21% des hôtels utilisent un CRM

**Application**:
- Structure profil multi-sections
- Catégories de segmentation à considérer

---

## Convergence Analysis

| Pattern | Source 1 | Source 2 | Source 3 | Confidence |
|---------|----------|----------|----------|------------|
| Structure profil multi-sections | ✓ Existant | — | ✓ Best practice | **High** |
| Séparation faits/hypothèses | ✓ Nécessaire | — | — | **Medium** |
| KPIs sectoriels | ✓ Manquants | ✓ Définis | ✓ Essentiels | **High** |
| Liens vers données opérationnelles | ✓ state/ existe | ✓ Intégration | ✓ PMS/POS | **High** |
| Communication protocol | ✓ lessons-learned | — | — | **High** |

---

## Decision Points

Aucun conflit majeur entre sources. Convergence sur:
- Profil structuré en sections
- KPIs sectoriels à intégrer
- Liens vers données opérationnelles

---

_Output de Phase 1 — Pipeline /elevate_
