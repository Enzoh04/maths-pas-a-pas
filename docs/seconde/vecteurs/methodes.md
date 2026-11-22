# Méthodes — Vecteurs

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Simplifier une somme de vecteurs avec la relation de Chasles

**Les étapes**

1. Remplacer chaque différence par une somme : $-\overrightarrow{AB} = \overrightarrow{BA}$.
2. Réordonner les termes pour que la fin de chaque vecteur soit le début du suivant (la somme est commutative).
3. Appliquer Chasles : $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$.
4. Inversement, pour **décomposer** un vecteur, on intercale un point : $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC}$.

**Exemple.** $\vec{w} = \overrightarrow{AB} - \overrightarrow{CB} + \overrightarrow{CA} = \overrightarrow{AB} + \overrightarrow{BC} + \overrightarrow{CA} = \overrightarrow{AC} + \overrightarrow{CA} = \overrightarrow{AA} = \vec{0}$.

---

## Méthode 2 — Construire un point défini par une égalité vectorielle

**Les étapes**

1. Exprimer le vecteur qui « part » d'un point connu : écrire l'égalité sous la forme $\overrightarrow{AM} = \ldots$ (avec Chasles si besoin).
2. **Construire** : placer $M$ en reportant le vecteur à partir de $A$.
3. **Calculer** ses coordonnées : $x_M - x_A = \ldots$ et $y_M - y_A = \ldots$

**Exemple.** $A(1\,;\,2)$, $B(4\,;\,0)$, $C(-1\,;\,3)$. On cherche $M$ tel que $\overrightarrow{AM} = 2\overrightarrow{AB} - \overrightarrow{AC}$.

$\overrightarrow{AB}\begin{pmatrix} 3 \\ -2 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} -2 \\ 1 \end{pmatrix}$, donc $\overrightarrow{AM}\begin{pmatrix} 6 + 2 \\ -4 - 1 \end{pmatrix} = \begin{pmatrix} 8 \\ -5 \end{pmatrix}$, et $M(1 + 8\,;\,2 - 5) = (9\,;\,-3)$.

---

## Méthode 3 — Déterminer la nature d'un triangle ou d'un quadrilatère

**Les étapes**

1. Calculer les **longueurs** des côtés (repère orthonormé) : $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$. Souvent, comparer les **carrés** des longueurs suffit.
2. Triangle **isocèle** : deux côtés égaux ; **équilatéral** : trois côtés égaux ; **rectangle** : réciproque de Pythagore sur le plus grand côté.
3. Quadrilatère : **parallélogramme** si $\overrightarrow{AB} = \overrightarrow{DC}$ ; puis **losange** (deux côtés consécutifs égaux), **rectangle** (diagonales de même longueur), **carré** (les deux).

**Exemple.** $A(-1\,;\,1)$, $B(3\,;\,-1)$, $C(4\,;\,1)$. $AB^2 = 16 + 4 = 20$, $BC^2 = 1 + 4 = 5$, $AC^2 = 25 + 0 = 25$. Or $20 + 5 = 25$ : $AB^2 + BC^2 = AC^2$, le triangle est **rectangle en $B$**.

---

## Méthode 4 — Démontrer un alignement ou un parallélisme

**Les étapes**

1. Choisir deux vecteurs : $\overrightarrow{AB}$ et $\overrightarrow{AC}$ pour l'alignement de $A$, $B$, $C$ ; $\overrightarrow{AB}$ et $\overrightarrow{CD}$ pour le parallélisme de $(AB)$ et $(CD)$.
2. Calculer leurs coordonnées.
3. Calculer le déterminant $xy' - x'y$.
4. Conclure : déterminant nul $\iff$ colinéaires $\iff$ alignés (ou parallèles).

**Exemple.** $A(-2\,;\,1)$, $B(1\,;\,3)$, $C(4\,;\,-1)$, $D(10\,;\,3)$. $\overrightarrow{AB}\begin{pmatrix} 3 \\ 2 \end{pmatrix}$, $\overrightarrow{CD}\begin{pmatrix} 6 \\ 4 \end{pmatrix}$ : $3 \times 4 - 6 \times 2 = 0$. Les droites $(AB)$ et $(CD)$ sont parallèles.

!!! tip "Sans repère"
    On peut aussi prouver la colinéarité en exprimant les deux vecteurs en fonction de deux vecteurs de base ($\overrightarrow{AB}$ et $\overrightarrow{AC}$ par exemple), à l'aide de la relation de Chasles.

---

## Méthode 5 — Démontrer qu'un quadrilatère est un parallélogramme

**Les étapes**

1. Écrire les sommets **dans l'ordre** : $ABCD$.
2. Montrer que $\overrightarrow{AB} = \overrightarrow{DC}$ (attention à l'ordre des lettres), en comparant les coordonnées.
3. *Autre méthode* : montrer que les diagonales $[AC]$ et $[BD]$ ont le **même milieu**.
4. Pour trouver le quatrième sommet $D$ d'un parallélogramme $ABCD$, résoudre $\overrightarrow{AD} = \overrightarrow{BC}$.

**Exemple.** $A(1\,;\,1)$, $B(5\,;\,2)$, $C(6\,;\,5)$, $D(2\,;\,4)$. $\overrightarrow{AB}\begin{pmatrix} 4 \\ 1 \end{pmatrix}$ et $\overrightarrow{DC}\begin{pmatrix} 4 \\ 1 \end{pmatrix}$ : $\overrightarrow{AB} = \overrightarrow{DC}$, donc $ABCD$ est un parallélogramme.
