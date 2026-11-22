# Chapitre 10 — Variables aléatoires réelles

## Ce que tu vas apprendre

- Définir une **variable aléatoire** et déterminer sa **loi de probabilité**.
- Calculer l'**espérance**, la **variance** et l'**écart-type** d'une variable aléatoire, et les interpréter.
- Utiliser la **linéarité** : $E(aX + b) = aE(X) + b$ et $V(aX + b) = a^2V(X)$.
- Utiliser la formule de **König-Huygens** : $V(X) = E(X^2) - E(X)^2$.
- Étudier une **variable de Bernoulli** et le nombre de succès dans une répétition d'épreuves.
- **Simuler** une variable aléatoire en Python et comparer moyenne observée et espérance.

## Prérequis

- [Chapitre 9](../probabilites-conditionnelles/index.md) : arbres pondérés, épreuves indépendantes.
- Seconde : statistiques (moyenne, écart-type), probabilités.

## Parcours conseillé

1. [Cours](cours.md) — environ 1 h 15 de lecture active.
2. [Méthodes](methodes.md) — les 5 savoir-faire du chapitre.
3. [Exercices corrigés](exercices.md) — 28 exercices classés en 5 thèmes, de ★ à ★★★.
4. [Sujets type épreuve anticipée](bac.md) — 4 sujets sans calculatrice.

## Versions imprimables (PDF)

[📄 Cours](pdf/cours.pdf){ .md-button }
[📄 Cours complet + toutes les démonstrations](pdf/cours-complet.pdf){ .md-button }
[📄 Fiches méthode](pdf/methodes.pdf){ .md-button }
[📄 Exercices — énoncés](pdf/exercices-enonces.pdf){ .md-button }
[📄 Exercices — corrigés](pdf/exercices-corriges.pdf){ .md-button }
[📄 Sujets type épreuve anticipée — énoncés](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets type épreuve anticipée — corrigés](pdf/bac-corriges.pdf){ .md-button }

!!! abstract "Les démonstrations de ce chapitre"
    **Au programme** : le programme officiel n'impose aucune démonstration dans ce chapitre.

    **Pour aller plus loin** : la linéarité de l'espérance, la formule $V(aX + b) = a^2V(X)$, la formule de König-Huygens, l'espérance et la variance d'une variable de Bernoulli.

    **Admis** : le rapprochement entre la moyenne d'un grand échantillon et l'espérance est seulement **observé** par simulation ; il sera démontré en Terminale (**loi des grands nombres**, avec l'inégalité de Bienaymé-Tchebychev).
