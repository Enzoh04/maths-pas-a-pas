# Méthodes — Vecteurs, droites et plans de l'espace

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac. Les exemples utilisent le cube $ABCDEFGH$ du cours.

![Le cube ABCDEFGH](img/cube.png){ width="40%" }

---

## Méthode 1 — Déterminer la position relative de deux droites

**Les étapes**

1. Les droites sont-elles **parallèles** ? On compare leurs vecteurs directeurs (colinéaires ou non).
2. Sinon, sont-elles **dans un même plan** ? Si oui, elles sont sécantes ; si non, elles sont non coplanaires.
3. Pour justifier « non coplanaires », on raisonne souvent par l'absurde : si elles étaient dans un même plan, ce plan contiendrait trop de points.

**Exemple.** $(AB)$ et $(CG)$ : leurs vecteurs directeurs $\overrightarrow{AB}$ et $\overrightarrow{CG}$ ne sont pas colinéaires. Si elles étaient coplanaires, le plan contiendrait $A$, $B$ et $C$, donc ce serait le plan $(ABC)$, qui ne contient pas $G$. Elles sont donc non coplanaires.

---

## Méthode 2 — Exprimer un vecteur en fonction d'autres

**Les étapes**

1. Utiliser la **relation de Chasles** pour faire apparaître les vecteurs voulus.
2. Remplacer les vecteurs « égaux » (côtés opposés d'un parallélogramme, d'une face du cube…).
3. Utiliser les milieux : si $I$ est le milieu de $[AB]$, $\overrightarrow{AI} = \frac{1}{2}\overrightarrow{AB}$, et pour tout point $M$, $\overrightarrow{MI} = \frac{1}{2}\left(\overrightarrow{MA} + \overrightarrow{MB}\right)$.

**Exemple.** Soit $I$ le milieu de $[FG]$. Alors $\overrightarrow{AI} = \overrightarrow{AB} + \overrightarrow{BF} + \overrightarrow{FI} = \overrightarrow{AB} + \overrightarrow{AE} + \frac{1}{2}\overrightarrow{AD}$, car $\overrightarrow{BF} = \overrightarrow{AE}$ et $\overrightarrow{FG} = \overrightarrow{AD}$.

---

## Méthode 3 — Démontrer un alignement ou un parallélisme

**Les étapes**

1. Exprimer les deux vecteurs en jeu (par Chasles ou en coordonnées).
2. Trouver le réel $k$ tel que $\vec{v} = k\vec{u}$.
3. Conclure : points alignés (si les vecteurs ont un point commun), ou droites parallèles.

**Exemple en coordonnées.** $A(1, 2, 3)$, $B(2, 4, 7)$, $C(4, 8, 15)$ : $\overrightarrow{AB}(1, 2, 4)$ et $\overrightarrow{AC}(3, 6, 12) = 3\overrightarrow{AB}$. Les points sont alignés.

---

## Méthode 4 — Démontrer que des vecteurs ou des points sont coplanaires

**Les étapes**

1. Vérifier que $\vec{u}$ et $\vec{v}$ ne sont **pas colinéaires**.
2. Chercher $a$ et $b$ tels que $\vec{w} = a\vec{u} + b\vec{v}$ : on écrit le système à trois équations, on le **résout avec deux équations**, et l'on **vérifie la troisième**.
3. Si la troisième équation est vérifiée : coplanaires. Sinon : non coplanaires (et $(\vec{u}, \vec{v}, \vec{w})$ est une base).

**Exemple.** $\vec{u}(1, 0, 1)$, $\vec{v}(0, 1, 1)$, $\vec{w}(2, 3, 5)$. On cherche $a\vec{u} + b\vec{v} = (a, b, a + b) = (2, 3, 5)$. Les deux premières coordonnées donnent $a = 2$ et $b = 3$, et la troisième est vérifiée : $2 + 3 = 5$. Donc $\vec{w} = 2\vec{u} + 3\vec{v}$ : les vecteurs sont coplanaires.

---

## Méthode 5 — Choisir un repère et calculer

**Quand ?** Dans un cube, un pavé ou une pyramide, dès que le calcul vectoriel « à la main » devient compliqué.

**Les étapes**

1. Choisir un repère adapté, par exemple $\left(A \,;\, \overrightarrow{AB}, \overrightarrow{AD}, \overrightarrow{AE}\right)$ pour le cube.
2. Écrire les coordonnées de tous les points utiles (milieux, points définis par une égalité vectorielle).
3. Faire les calculs en coordonnées (méthodes 3 et 4).

**Exemple.** Dans ce repère, le milieu $I$ de $[FG]$ a pour coordonnées $\left(1, \frac{1}{2}, 1\right)$, et $\overrightarrow{AI}\left(1, \frac{1}{2}, 1\right)$ : on retrouve $\overrightarrow{AI} = \overrightarrow{AB} + \frac{1}{2}\overrightarrow{AD} + \overrightarrow{AE}$.

---

## Méthode 6 — Construire la section d'un solide par un plan

**Les outils**

1. Si deux points du plan de coupe sont sur une même face, on les relie : c'est un côté de la section.
2. Deux faces parallèles sont coupées selon des **segments parallèles**.
3. **Théorème du toit** : si le plan de coupe contient une droite parallèle à une arête, il coupe la face qui contient cette arête selon une parallèle à cette arête.
4. On prolonge des droites d'une même face pour trouver des points sur les arêtes voisines.

**Exemple.** La section du cube par le plan $(BDE)$ : $B$ et $D$ sont sur la face du bas, $B$ et $E$ sur la face avant, $D$ et $E$ sur la face de gauche. La section est le triangle $BDE$, équilatéral (ses côtés sont des diagonales de faces).
