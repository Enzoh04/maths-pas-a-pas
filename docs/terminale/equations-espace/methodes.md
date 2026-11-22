# Méthodes — Représentations paramétriques et équations cartésiennes

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé** comme on l'attend au bac. Le repère est orthonormé.

---

## Méthode 1 — Écrire et utiliser une représentation paramétrique

**Les étapes**

1. Trouver **un point** $A$ et **un vecteur directeur** $\vec{u}$ (pour la droite $(AB)$, on prend $\vec{u} = \overrightarrow{AB}$).
2. Écrire $x = x_A + ta$, $y = y_A + tb$, $z = z_A + tc$, $t \in \mathbb{R}$.
3. Pour tester si un point est sur la droite : trouver $t$ avec une équation, puis vérifier les deux autres **avec la même valeur**.

**Exemple.** Droite $(AB)$ avec $A(2, 0, -1)$ et $B(3, 2, 1)$. On a $\overrightarrow{AB}(1, 2, 2)$, d'où la représentation
$$\begin{cases} x = 2 + t \\ y = 2t \\ z = -1 + 2t \end{cases} \quad t \in \mathbb{R}.$$
Le point $C(5, 6, 5)$ : la première équation donne $t = 3$, et alors $y = 6$, $z = 5$. Donc $C \in (AB)$.

---

## Méthode 2 — Déterminer une équation cartésienne d'un plan

**Si l'on connaît un vecteur normal $\vec{n}(a, b, c)$ et un point $A$ :**

1. Écrire $ax + by + cz + d = 0$.
2. Remplacer par les coordonnées de $A$ pour trouver $d$.

**Si l'on connaît trois points non alignés $A$, $B$, $C$ :**

1. Calculer $\overrightarrow{AB}$ et $\overrightarrow{AC}$, vérifier qu'ils ne sont pas colinéaires.
2. Chercher un vecteur normal $\vec{n}(a, b, c)$ : $\vec{n} \cdot \overrightarrow{AB} = 0$ et $\vec{n} \cdot \overrightarrow{AC} = 0$, en fixant une coordonnée.
3. Conclure comme ci-dessus, puis **vérifier** que $B$ et $C$ satisfont l'équation.

**Exemple.** Plan $(ABC)$ avec $A(1, 1, 0)$, $B(2, 1, 1)$, $C(1, 3, 1)$. $\overrightarrow{AB}(1, 0, 1)$ et $\overrightarrow{AC}(0, 2, 1)$ ne sont pas colinéaires. On veut $a + c = 0$ et $2b + c = 0$ ; avec $c = -2$ : $a = 2$, $b = 1$, donc $\vec{n}(2, 1, -2)$. Équation $2x + y - 2z + d = 0$ ; avec $A$ : $3 + d = 0$, donc $2x + y - 2z - 3 = 0$. Vérification : $B$ donne $4 + 1 - 2 - 3 = 0$ et $C$ donne $2 + 3 - 2 - 3 = 0$.

---

## Méthode 3 — Intersection d'une droite et d'un plan

**Les étapes**

1. Remplacer $x$, $y$, $z$ de la représentation paramétrique dans l'équation du plan.
2. Résoudre l'équation en $t$ :
   - une solution : la droite coupe le plan ; on remplace $t$ pour obtenir le point ;
   - aucune solution : la droite est strictement parallèle au plan ;
   - une infinité ($0 = 0$) : la droite est contenue dans le plan.

**Exemple.** $d$ : $x = 2 + t$, $y = 2t$, $z = -1 + 2t$ et $\mathcal{P}$ : $x + y + z - 7 = 0$. On obtient $(2 + t) + 2t + (-1 + 2t) - 7 = 0$, soit $5t - 6 = 0$, donc $t = \dfrac{6}{5}$. Le point d'intersection est $\left(\dfrac{16}{5}, \dfrac{12}{5}, \dfrac{7}{5}\right)$. Vérification : $\dfrac{16 + 12 + 7}{5} = 7$.

---

## Méthode 4 — Intersection de deux plans

**Les étapes**

1. Vérifier que les vecteurs normaux ne sont pas colinéaires : les plans sont sécants.
2. Choisir une coordonnée comme paramètre (par exemple $z = t$).
3. Résoudre le système des deux équations en les deux autres coordonnées, en fonction de $t$.
4. On obtient une représentation paramétrique de la droite d'intersection. **Vérifier** avec un point.

**Exemple.** $\mathcal{P}$ : $x + y - z - 1 = 0$ et $\mathcal{Q}$ : $x - y + z - 3 = 0$. Les vecteurs normaux $(1, 1, -1)$ et $(1, -1, 1)$ ne sont pas colinéaires. On pose $z = t$ :
$$\begin{cases} x + y = 1 + t \\ x - y = 3 - t \end{cases} \iff \begin{cases} x = 2 \\ y = -1 + t \end{cases}$$
La droite d'intersection est $x = 2$, $y = -1 + t$, $z = t$, $t \in \mathbb{R}$. Vérification avec $t = 0$, point $(2, -1, 0)$ : $2 - 1 - 0 - 1 = 0$ et $2 + 1 + 0 - 3 = 0$.

---

## Méthode 5 — Projeté orthogonal et distance à un plan

**Les étapes**

1. Écrire une représentation paramétrique de la droite $\Delta$ passant par $M$ et dirigée par le vecteur normal $\vec{n}$ du plan.
2. Chercher l'intersection de $\Delta$ et du plan (méthode 3) : c'est le projeté $H$.
3. La distance est $MH$. On peut contrôler avec la formule $\dfrac{|ax_M + by_M + cz_M + d|}{\sqrt{a^2 + b^2 + c^2}}$.

**Exemple.** $M(3, 1, 2)$ et $\mathcal{P}$ : $x + y + z = 0$. La droite $\Delta$ : $x = 3 + t$, $y = 1 + t$, $z = 2 + t$. En remplaçant : $6 + 3t = 0$, donc $t = -2$ et $H(1, -1, 0)$. Alors $MH = \sqrt{4 + 4 + 4} = 2\sqrt{3}$, et la formule donne bien $\dfrac{|3 + 1 + 2|}{\sqrt{3}} = \dfrac{6}{\sqrt{3}} = 2\sqrt{3}$.

---

## Méthode 6 — Position relative de deux droites

**Les étapes**

1. Comparer les vecteurs directeurs. S'ils sont colinéaires, les droites sont parallèles : tester si un point de l'une est sur l'autre.
2. Sinon, écrire les deux représentations avec **deux paramètres différents** $t$ et $s$, et égaler les coordonnées : trois équations, deux inconnues.
3. Résoudre avec deux des équations, puis **tester la troisième** :
   - elle est vérifiée : les droites sont sécantes ; on calcule le point ;
   - elle ne l'est pas : les droites sont non coplanaires.

**Exemple.** $d$ : $x = 1 + t$, $y = 2t$, $z = 3 - t$ et $d'$ : $x = 2 + s$, $y = 2 - s$, $z = 2 + 3s$. Les vecteurs $(1, 2, -1)$ et $(1, -1, 3)$ ne sont pas colinéaires. On résout :
$$\begin{cases} 1 + t = 2 + s \\ 2t = 2 - s \\ 3 - t = 2 + 3s \end{cases}$$
Les deux premières donnent $s = t - 1$, puis $2t = 3 - t$, donc $t = 1$ et $s = 0$. La troisième : $3 - 1 = 2 + 0$, vraie. Les droites sont sécantes au point $(2, 2, 2)$.
