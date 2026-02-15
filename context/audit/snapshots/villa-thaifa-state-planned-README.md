# Etat Planifie

> **Propositions en attente de validation avant execution.**

---

## Objectif

Ce repertoire contient les changements planifies qui necessitent la validation d'Omar avant execution. Les fichiers ici sont modifiables jusqu'a leur approbation et execution.

---

## Fichiers

| Fichier      | Statut              | Decision Bloquante                       |
| ------------ | ------------------- | ---------------------------------------- |
| `pricing.md` | En attente de validation | Tarification premium pour Chambres 7 & 12 |

---

## Flux de Travail

```
1. BROUILLON  → Creer la proposition dans planned/
2. REVISION   → Omar revise et valide les decisions
3. EXECUTION  → Suivre la methode d'execution dans le fichier
4. JOURNAL    → Documenter dans ../execution/YYYY-MM-DD/
5. ARCHIVAGE  → Deplacer le fichier de planned/ vers execution/
```

---

## Liste de Controle de Validation

Avant d'executer un changement planifie :

- [ ] Toutes les cases de decision remplies par Omar
- [ ] Proposition verifiee contre [`configs/hotel/`](../../configs/hotel/)
- [ ] Methode d'execution clairement definie
- [ ] Etapes de verification post-execution identifiees

---

## Associes

- **Configuration** → [`../../configs/hotel/`](../../configs/hotel/)
- **Etat actuel** → [`../current/`](../current/)
- **Journaux d'execution** → [`../execution/`](../execution/)

---

_Standard : `shared/standards/state-management.md`_
