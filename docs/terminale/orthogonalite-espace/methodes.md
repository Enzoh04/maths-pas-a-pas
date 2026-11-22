# Méthodes — Orthogonalité et distances dans l'espace

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé** comme on l'attend au bac. Les exemples utilisent le cube $ABCDEFGH$ d'arête $1$ et le repère orthonormé $\left(A \,;\, \overrightarrow{AB}, \overrightarrow{AD}, \overrightarrow{AE}\right)$.

![Le cube ABCDEFGH](img/cube.png){ width="40%" }

---

## Méthode 1 — Calculer un produit scalaire dans l'espace

**Les étapes.** Choisir l'outil le plus adapté :

1. **Projection** : si l'on voit un angle droit, on projette un vecteur sur l'autre.
2. **Décomposition** : on écrit les vecteurs avec la relation de Chasles à l'aide de vecteurs dont on connaît les produits scalaires (souvent orthogonaux), puis on développe.
3. **Coordonnées** : dans un repère **orthonormé**, $\vec{u} \cdot \vec{v} = xx' + yy' + zz'$.

**Exemple.** Calculer $\overrightarrow{AE} \cdot \overrightarrow{BG}$.

- Par décomposition : $\overrightarrow{BG} = \overrightarrow{BC} + \overrightarrow{CG} = \overrightarrow{AD} + \overrightarrow{AE}$, donc $\overrightarrow{AE} \cdot \overrightarrow{BG} = \overrightarrow{AE} \cdot \overrightarrow{AD} + \overrightarrow{AE} \cdot \overrightarrow{AE} = 0 + 1 = 1$.
- Par coordonnées : $\overrightarrow{AE}(0, 0, 1)$ et $\overrightarrow{BG}(0, 1, 1)$, donc le produit vaut $0 + 0 + 1 = 1$.

---

## Méthode 2 — Démontrer que deux droites sont orthogonales

**Les étapes**

1. Choisir un vecteur directeur de chaque droite.
2. Montrer que leur produit scalaire est nul (méthode 1).
3. Autre voie : montrer que l'une des droites est orthogonale à un plan qui contient l'autre.

**Exemple.** Montrer que $(BD)$ et $(AG)$ sont orthogonales.

$\overrightarrow{BD}(-1, 1, 0)$ et $\overrightarrow{AG}(1, 1, 1)$ : $\overrightarrow{BD} \cdot \overrightarrow{AG} = -1 + 1 + 0 = 0$. Les droites sont orthogonales.

*Sans coordonnées : $(BD)$ est orthogonale à $(AC)$ (diagonales d'un carré) et à $(CG)$ (orthogonale au plan $(ABC)$). Ces deux droites sont sécantes en $C$, donc $(BD)$ est orthogonale au plan $(ACG)$, qui contient $(AG)$.*

---

## Méthode 3 — Démontrer qu'une droite est orthogonale à un plan

**Les étapes**

1. Trouver deux vecteurs **non colinéaires** du plan (souvent $\overrightarrow{AB}$ et $\overrightarrow{AC}$ si le plan est $(ABC)$).
2. Montrer qu'un vecteur directeur de la droite est orthogonal à chacun d'eux.
3. Conclure : la droite est orthogonale au plan, et son vecteur directeur est **normal** au plan.

**Exemple.** Montrer que $(AG)$ est orthogonale au plan $(BDE)$.

$\overrightarrow{BD}(-1, 1, 0)$ et $\overrightarrow{BE}(-1, 0, 1)$ ne sont pas colinéaires. Or $\overrightarrow{AG} \cdot \overrightarrow{BD} = -1 + 1 + 0 = 0$ et $\overrightarrow{AG} \cdot \overrightarrow{BE} = -1 + 0 + 1 = 0$. Donc $(AG)$ est orthogonale à deux droites sécantes du plan $(BDE)$ : elle est orthogonale à ce plan, et $\overrightarrow{AG}$ est un vecteur normal à $(BDE)$.

---

## Méthode 4 — Trouver un vecteur normal à un plan

**Les étapes**

1. Calculer deux vecteurs non colinéaires $\vec{u}$ et $\vec{v}$ du plan.
2. Chercher $\vec{n}(a, b, c)$ tel que $\vec{n} \cdot \vec{u} = 0$ et $\vec{n} \cdot \vec{v} = 0$ : deux équations, trois inconnues.
3. Le vecteur normal n'est défini qu'à un coefficient près : **fixer** une coordonnée (par exemple $c = 1$, ou la valeur qui évite les fractions) et calculer les deux autres.
4. **Vérifier** les deux produits scalaires.

**Exemple.** Trouver un vecteur normal au plan $(ABC)$ avec $A(1, 0, 2)$, $B(2, 1, 2)$, $C(1, 2, 3)$.

$\overrightarrow{AB}(1, 1, 0)$ et $\overrightarrow{AC}(0, 2, 1)$ ne sont pas colinéaires. On veut $a + b = 0$ et $2b + c = 0$. Avec $b = -1$ : $a = 1$ et $c = 2$. Donc $\vec{n}(1, -1, 2)$. Vérification : $1 - 1 + 0 = 0$ et $0 - 2 + 2 = 0$.

---

## Méthode 5 — Déterminer le projeté orthogonal d'un point

**Sur un plan $\mathcal{P}$ de vecteur normal $\vec{n}$**

1. Écrire que $H$ vérifie $\overrightarrow{MH} = k\vec{n}$ : les coordonnées de $H$ s'expriment en fonction de $k$.
2. Écrire que $H \in \mathcal{P}$ : $\overrightarrow{AH} \cdot \vec{n} = 0$ pour un point $A$ du plan. On obtient une équation du premier degré en $k$.
3. Remplacer $k$ pour obtenir $H$.

**Sur une droite $d$ passant par $A$, de vecteur directeur $\vec{u}$**

1. Écrire $\overrightarrow{AH} = t\vec{u}$.
2. Écrire $\overrightarrow{MH} \cdot \vec{u} = 0$ : on trouve $t$.

**Exemple.** Projeté de $A$ sur le plan $(BDE)$.

D'après la méthode 3, $\overrightarrow{AG}(1, 1, 1)$ est normal à $(BDE)$. On écrit $\overrightarrow{AH} = k\overrightarrow{AG}$, soit $H(k, k, k)$. Puis $H \in (BDE)$ si et seulement si $\overrightarrow{BH} \cdot \overrightarrow{AG} = 0$, c'est-à-dire $(k - 1) + k + k = 0$, soit $k = \dfrac{1}{3}$. Donc $H\left(\dfrac{1}{3}, \dfrac{1}{3}, \dfrac{1}{3}\right)$.

---

## Méthode 6 — Calculer une distance ou un volume

**Les étapes**

1. Déterminer le projeté orthogonal $H$ (méthode 5).
2. Calculer $MH$ avec la formule de la distance en repère orthonormé.
3. Pour un volume de tétraèdre ou de pyramide : $V = \dfrac{1}{3} \times \mathcal{B} \times h$, où $h$ est la distance du sommet au plan de la base. On peut aussi calculer le volume de deux façons pour en déduire une distance.

**Exemple.** Distance de $A$ au plan $(BDE)$.

Avec $H\left(\dfrac{1}{3}, \dfrac{1}{3}, \dfrac{1}{3}\right)$ : $AH = \sqrt{\dfrac{1}{9} + \dfrac{1}{9} + \dfrac{1}{9}} = \dfrac{\sqrt{3}}{3}$.

*Vérification par les volumes. Le tétraèdre $ABDE$ a pour volume $\dfrac{1}{3} \times \mathcal{A}(ABD) \times AE = \dfrac{1}{3} \times \dfrac{1}{2} \times 1 = \dfrac{1}{6}$. Le triangle $BDE$ est équilatéral de côté $\sqrt{2}$, d'aire $\dfrac{\sqrt{3}}{4} \times 2 = \dfrac{\sqrt{3}}{2}$. Donc $\dfrac{1}{6} = \dfrac{1}{3} \times \dfrac{\sqrt{3}}{2} \times h$, d'où $h = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}$.*
