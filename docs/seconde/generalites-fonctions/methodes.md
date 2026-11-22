# Méthodes — Généralités sur les fonctions

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Calculer une image, chercher des antécédents

**Les étapes**

1. **Image de $a$** : remplacer $x$ par $a$ dans l'expression (avec des parenthèses autour des nombres négatifs), puis calculer.
2. **Antécédents de $b$** : résoudre l'équation $f(x) = b$, en vérifiant que les solutions sont dans l'ensemble de définition.
3. Pour savoir si un point $M(a\,;\,b)$ est sur la courbe : calculer $f(a)$ et comparer à $b$.

**Exemple.** $f(x) = 2x^2 - 3$. $f(-2) = 2 \times (-2)^2 - 3 = 5$. Antécédents de $15$ : $2x^2 - 3 = 15 \iff x^2 = 9 \iff x = 3$ ou $x = -3$. Le point $(1\,;\,0)$ n'est pas sur la courbe car $f(1) = -1 \neq 0$.

---

## Méthode 2 — Déterminer un ensemble de définition

**Les étapes**

1. Repérer les **dénominateurs** : ils doivent être **non nuls** (on résout « dénominateur $= 0$ » et on exclut les solutions).
2. Repérer les **racines carrées** : l'expression sous la racine doit être **positive ou nulle** (on résout une inéquation).
3. Combiner les conditions et écrire l'ensemble avec des intervalles.

**Exemple.** $f(x) = \dfrac{\sqrt{x + 1}}{x - 3}$. Conditions : $x + 1 \geq 0$, soit $x \geq -1$, et $x \neq 3$. $D = [-1\,;\,3[ \cup ]3\,;\,+\infty[$.

---

## Méthode 3 — Résoudre graphiquement

**Les étapes**

1. **$f(x) = k$** : tracer la droite horizontale $y = k$ et lire les abscisses des points d'intersection.
2. **$f(x) > k$** : lire les abscisses des points de la courbe **au-dessus** de cette droite (exclure les intersections pour une inégalité stricte).
3. **$f(x) = g(x)$**, **$f(x) \geq g(x)$** : même chose avec la courbe de $g$ à la place de la droite.
4. Donner les solutions sous forme d'ensemble ou d'intervalles, en précisant qu'il s'agit de **valeurs lues** (approchées).

**Exemple.** Avec la courbe du cours (fonction définie sur $[-3\,;\,5]$) : $f(x) \geq 2$ pour $x \in [-1{,}85\,;\,0] \cup [4{,}85\,;\,5]$ environ.

---

## Méthode 4 — Dresser et exploiter un tableau de variations

**Les étapes**

1. Sur le graphique, repérer les abscisses où la courbe **change de sens**, ainsi que les **bornes** de l'ensemble de définition.
2. Dresser le tableau : première ligne les abscisses, deuxième ligne les flèches et les valeurs de $f$.
3. **Extremums** : comparer les valeurs aux sommets des flèches (maximum) et aux creux (minimum), **bornes comprises**.
4. **Comparer des images** sans les calculer : si $a$ et $b$ sont dans un même intervalle où $f$ est monotone, on applique la définition.

**Exemple.** $f$ est croissante sur $[0\,;\,4]$ et décroissante sur $[4\,;\,10]$, avec $f(0) = 1$, $f(4) = 6$, $f(10) = -2$.

| $x$ | $0$ | | $4$ | | $10$ |
|---|---|---|---|---|---|
| $f(x)$ | $1$ | $\nearrow$ | $6$ | $\searrow$ | $-2$ |

Maximum $6$ en $4$, minimum $-2$ en $10$. Comme $5 < 8$ sont dans $[4\,;\,10]$ où $f$ décroît, $f(5) \geq f(8)$. On **ne peut pas** comparer $f(2)$ et $f(7)$ avec le seul tableau.

---

## Méthode 5 — Démontrer qu'une fonction admet un maximum (ou un minimum)

**Les étapes**

1. Conjecturer la valeur $M$ et l'endroit $a$ où elle est atteinte (graphique, tableau de valeurs).
2. Montrer que $f(x) - M \leq 0$ pour tout $x$ (souvent en faisant apparaître un carré).
3. Vérifier que $f(a) = M$.

**Exemple.** $f(x) = -x^2 + 6x - 5$. On conjecture un maximum $4$ en $3$. $f(x) - 4 = -x^2 + 6x - 9 = -(x - 3)^2 \leq 0$, et $f(3) = -9 + 18 - 5 = 4$. Le maximum de $f$ est $4$, atteint en $3$.
