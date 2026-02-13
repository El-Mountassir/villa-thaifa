# Pattern Extraction

**Date**: 2025-12-20

---

## Extracted Patterns

### Pattern 1: Executive Snapshot First

- **Observed In**: Source 1 (existant partiellement), Source 3 (CRM best practice)
- **Underlying Principle**: Les décideurs scannent en 5 secondes — KPIs clés en haut
- **Generalization Test**: Appliquerait-on à un autre profil client? → **Oui**
- **Confidence**: **High**

**Implementation**:
```markdown
> **Status:** Lead (RDV planifié)
> **Priority:** HIGH
> **Next:** RDV découverte 22 déc 10h
> **KPIs:** 12 chambres | 9.3/10 Booking | HotelRunner actif
```

---

### Pattern 2: Contact + Communication Protocol

- **Observed In**: Source 1 (lessons-learned.md)
- **Underlying Principle**: Les coordonnées sans le "comment" sont insuffisantes
- **Generalization Test**: Tout client senior nécessite ce pattern → **Oui**
- **Confidence**: **High**

**Implementation**:
- Intégrer le pattern Scout → Rapport → Questions → Action
- Rappeler le vouvoiement obligatoire
- Référencer lessons-learned.md

---

### Pattern 3: Faits ✅ vs Hypothèses ⏳

- **Observed In**: Source 1 (besoin identifié)
- **Underlying Principle**: Mélanger confirmé et supposé crée de la confusion
- **Generalization Test**: Applicable à tout profil client en phase discovery → **Oui**
- **Confidence**: **High**

**Implementation**:
```
4.1 FAITS CONFIRMÉS ✅
    - PMS: Aucun
    - Channel Manager: HotelRunner
    - Note: 9.3/10

4.2 HYPOTHÈSES À VALIDER ⏳
    - Besoin principal: [liste]
    - Budget: À déterminer
```

---

### Pattern 4: SSOT Links (Single Source of Truth)

- **Observed In**: Source 1 (state/ existe), Source 2 & 3 (intégration PMS/CRM)
- **Underlying Principle**: Dupliquer les données crée des incohérences
- **Generalization Test**: Applicable à tout dossier client → **Oui**
- **Confidence**: **High**

**Implementation**:
```markdown
### État Opérationnel
→ Voir `state/current/rooms.md`
→ Voir `state/current/reservations.md`
```

---

## Anti-Patterns Identified

| Anti-Pattern | Problème | Solution |
|--------------|----------|----------|
| Infos éparpillées | Données dans PROFILE + state + lessons = redondance | Pointer vers SSOT |
| Faits/Hypothèses mélangés | Confusion sur ce qui est confirmé | Sections séparées |
| Profil statique | Pas de date de MAJ visible | Ajouter "Last Updated" en haut |
| Vocabulaire informel | "Dure à estimer" au lieu de "À déterminer" | Corrections orthographe + ton |

---

_Output de Phase 2 — Pipeline /elevate_
