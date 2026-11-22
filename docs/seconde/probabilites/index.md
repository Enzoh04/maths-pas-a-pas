# Chapitre 9 — Probabilités

## Ce que tu vas apprendre

- Modéliser une expérience aléatoire : **univers**, **issues**, **événements**, **loi de probabilité**.
- Calculer des probabilités en situation d'**équiprobabilité**, avec des **tableaux** et des **arbres**.
- Utiliser l'**événement contraire**, la **réunion** et l'**intersection** : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- Découvrir les **probabilités conditionnelles** à partir d'un tableau croisé ou d'un arbre pondéré, et le vocabulaire des **tests de dépistage**.
- **Simuler** une expérience en Python et observer la **stabilisation des fréquences**.

## Prérequis

- [Chapitre 8](../statistiques/index.md) : fréquences, tableaux croisés.
- Collège : probabilités simples.

## Parcours conseillé

1. [Cours](cours.md) — environ 1 h 30 de lecture active.
2. [Méthodes](methodes.md) — les 5 savoir-faire du chapitre.
3. [Exercices corrigés](exercices.md) — 28 exercices classés en 5 thèmes, de ★ à ★★★.
4. [Évaluations type](bac.md) — 4 sujets d'entraînement.

## Versions imprimables (PDF)

[📄 Cours](pdf/cours.pdf){ .md-button }
[📄 Cours complet + toutes les démonstrations](pdf/cours-complet.pdf){ .md-button }
[📄 Fiches méthode](pdf/methodes.pdf){ .md-button }
[📄 Exercices — énoncés](pdf/exercices-enonces.pdf){ .md-button }
[📄 Exercices — corrigés](pdf/exercices-corriges.pdf){ .md-button }
[📄 Évaluations type — énoncés](pdf/bac-enonces.pdf){ .md-button }
[📄 Évaluations type — corrigés](pdf/bac-corriges.pdf){ .md-button }

!!! abstract "Les démonstrations de ce chapitre"
    **Au programme** : le programme officiel n'impose aucune démonstration dans ce chapitre.

    **Pour aller plus loin** : la probabilité de l'événement contraire, la formule $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, la formule du produit $P(A \cap B) = P(A) \times P_A(B)$ dans le cas équiprobable.

    **Admis** : la **loi des grands nombres** (la fréquence d'un événement se rapproche de sa probabilité quand on répète l'expérience) est seulement **observée** par simulation ; elle est démontrée en Terminale.
