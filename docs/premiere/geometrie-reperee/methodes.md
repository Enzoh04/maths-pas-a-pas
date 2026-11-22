# Méthodes — Géométrie repérée

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice. Le repère est orthonormé.

---

## Méthode 1 — Déterminer une équation de droite

**Les étapes**

1. Trouver soit un **vecteur normal** $\vec{n}(a\,;\,b)$, soit un **vecteur directeur** $\vec{u}(-b\,;\,a)$ de la droite.
   - Droite **perpendiculaire** à $(BC)$ : $\overrightarrow{BC}$ est normal.
   - Droite **parallèle** à $(BC)$ : $\overrightarrow{BC}$ est directeur.
2. Écrire $ax + by + c = 0$ avec le vecteur normal $(a\,;\,b)$.
3. Trouver $c$ en écrivant qu'un point connu de la droite vérifie l'équation.

**Exemple.** $A(3\,;\,-1)$, $B(1\,;\,2)$, $C(4\,;\,4)$. Droite passant par $A$ et perpendiculaire à $(BC)$ : $\overrightarrow{BC}(3\,;\,2)$ est normal, donc $3x + 2y + c = 0$ ; avec $A$ : $9 - 2 + c = 0$, soit $c = -7$. Équation : $3x + 2y - 7 = 0$.

Droite passant par $A$ et parallèle à $(BC)$ : $\overrightarrow{BC}(3\,;\,2)$ est directeur, donc $(2\,;\,-3)$ est normal : $2x - 3y + c = 0$ avec $6 + 3 + c = 0$. Équation : $2x - 3y - 9 = 0$.

---

## Méthode 2 — Calculer le projeté orthogonal d'un point et une distance

**Les étapes**

1. Écrire l'équation de la perpendiculaire $\Delta$ à $d$ passant par $M$ : un vecteur normal de $d$ est un vecteur **directeur** de $\Delta$.
2. Le projeté $H$ est l'intersection de $d$ et $\Delta$ : résoudre le système des deux équations.
3. La distance de $M$ à $d$ est $MH$. Pour vérifier : $\dfrac{|ax_M + by_M + c|}{\sqrt{a^2 + b^2}}$.

**Exemple.** Projeté de $M(5\,;\,5)$ sur $d : x + 2y - 4 = 0$.

$\vec{n}(1\,;\,2)$ dirige $\Delta$, donc $(2\,;\,-1)$ est normal à $\Delta$ : $2x - y + c = 0$ avec $10 - 5 + c = 0$, soit $\Delta : 2x - y - 5 = 0$.

Système : $y = 2x - 5$, puis $x + 2(2x - 5) = 4$, donc $5x = 14$ : $H\left(\frac{14}{5}\,;\,\frac{3}{5}\right)$.

Distance : $\overrightarrow{HM}\left(\frac{11}{5}\,;\,\frac{22}{5}\right)$, donc $MH = \frac{11}{5}\sqrt{1 + 4} = \frac{11\sqrt{5}}{5}$. Vérification : $\frac{|5 + 10 - 4|}{\sqrt{5}} = \frac{11}{\sqrt{5}} = \frac{11\sqrt{5}}{5}$.

---

## Méthode 3 — Trouver le centre et le rayon d'un cercle

**Les étapes**

1. Regrouper les termes en $x$ et en $y$.
2. Écrire les formes canoniques : $x^2 + \alpha x = \left(x + \frac{\alpha}{2}\right)^2 - \frac{\alpha^2}{4}$.
3. Mettre l'équation sous la forme $(x - x_0)^2 + (y - y_0)^2 = k$ et conclure selon le signe de $k$.

**Exemple.** $x^2 + y^2 + 6x - 4y - 12 = 0$.
$$(x + 3)^2 - 9 + (y - 2)^2 - 4 - 12 = 0 \iff (x + 3)^2 + (y - 2)^2 = 25.$$
C'est le cercle de centre $\Omega(-3\,;\,2)$ et de rayon $5$.

!!! warning "Attention aux signes"
    $(x + 3)^2$ correspond à $x_0 = -3$, pas à $3$.

---

## Méthode 4 — Étudier l'intersection d'une droite et d'un cercle

**Les étapes**

1. Exprimer $y$ en fonction de $x$ (ou l'inverse) avec l'équation de la droite.
2. Remplacer dans l'équation du cercle : on obtient une équation du second degré.
3. Le discriminant donne le nombre de points communs ($2$, $1$ : tangente, ou $0$). Calculer les coordonnées des points.
4. *Autre méthode* : comparer la distance du centre à la droite avec le rayon.

**Exemple.** Cercle $\mathcal{C} : x^2 + y^2 = 5$ et droite $d : y = x + 1$.
$$x^2 + (x + 1)^2 = 5 \iff 2x^2 + 2x - 4 = 0 \iff x^2 + x - 2 = 0 \iff (x - 1)(x + 2) = 0.$$
Deux points communs : $(1\,;\,2)$ et $(-2\,;\,-1)$.

---

## Méthode 5 — Étudier une parabole

**Les étapes**

1. Calculer $\alpha = -\frac{b}{2a}$ et $\beta = f(\alpha)$ : sommet $S(\alpha\,;\,\beta)$, axe de symétrie $x = \alpha$.
2. Le signe de $a$ donne l'orientation (vers le haut si $a > 0$).
3. Intersections avec l'axe des abscisses : résoudre $f(x) = 0$ ; avec une droite $y = mx + p$ : résoudre $f(x) = mx + p$.

**Exemple.** $f(x) = -2x^2 + 8x - 6$. $\alpha = -\frac{8}{-4} = 2$ et $\beta = -8 + 16 - 6 = 2$ : sommet $S(2\,;\,2)$, axe $x = 2$, parabole tournée vers le bas. Racines : $-2(x^2 - 4x + 3) = -2(x - 1)(x - 3)$, donc $1$ et $3$.

Intersection avec $y = 2x - 6$ : $-2x^2 + 8x - 6 = 2x - 6 \iff -2x^2 + 6x = 0 \iff -2x(x - 3) = 0$. Points $(0\,;\,-6)$ et $(3\,;\,0)$.
