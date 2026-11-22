# Méthodes — Variations et courbes représentatives

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Étudier la parité d'une fonction

**Les étapes**

1. Vérifier que l'ensemble de définition est **symétrique par rapport à $0$**.
2. Calculer $f(-x)$ en remplaçant $x$ par $(-x)$, **avec des parenthèses**.
3. Comparer à $f(x)$ et à $-f(x)$.
4. Pour montrer qu'elle n'est ni paire ni impaire, donner un contre-exemple numérique.

**Exemple.** $f(x) = \dfrac{x}{x^2 + 1}$, définie sur $\mathbb{R}$ (symétrique). $f(-x) = \dfrac{-x}{(-x)^2 + 1} = -\dfrac{x}{x^2 + 1} = -f(x)$ : $f$ est impaire.

**Exemple.** $g(x) = x^2 - x$ : $g(1) = 0$ et $g(-1) = 2$. Comme $g(-1) \neq g(1)$, $g$ n'est pas paire ; comme $g(-1) \neq -g(1)$, elle n'est pas impaire.

---

## Méthode 2 — Étudier les variations d'une fonction

**Les étapes**

1. Préciser l'intervalle d'étude et justifier la dérivabilité.
2. Calculer $f'(x)$, puis le **factoriser** (ou le mettre sous la forme d'un seul quotient).
3. Étudier le **signe** de $f'(x)$ : trinôme, tableau de signes, ou terme évidemment positif.
4. Dresser le tableau de variations, en calculant les valeurs aux points remarquables.

**Exemple.** $f(x) = x + \dfrac{1}{x}$ sur $]0\,;\,+\infty[$. $f'(x) = 1 - \dfrac{1}{x^2} = \dfrac{x^2 - 1}{x^2} = \dfrac{(x - 1)(x + 1)}{x^2}$. Sur $]0\,;\,+\infty[$, $x + 1 > 0$ et $x^2 > 0$, donc $f'(x)$ a le signe de $x - 1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f$ | ‖ | $\searrow$ | $2$ | $\nearrow$ | |

---

## Méthode 3 — Déterminer les extremums

**Les étapes**

1. Résoudre $f'(x) = 0$ pour trouver les candidats.
2. Garder ceux où $f'$ **change de signe** (lu dans le tableau).
3. Calculer les valeurs de $f$ en ces points, et aussi **aux bornes** si l'intervalle est fermé.
4. Distinguer extremum **local** et extremum **sur l'intervalle** (global).

**Exemple.** Avec la méthode 2, $f(x) = x + \frac{1}{x}$ admet sur $]0\,;\,+\infty[$ un minimum égal à $2$, atteint en $1$. On en déduit que $x + \frac{1}{x} \geq 2$ pour tout $x > 0$.

---

## Méthode 4 — Démontrer une inégalité, comparer deux courbes

**Les étapes**

1. Tout passer dans un membre : poser $h(x) = f(x) - g(x)$.
2. Si l'on sait **factoriser** $h(x)$, étudier directement son signe.
3. Sinon, étudier les **variations** de $h$ et montrer que son minimum est positif (ou son maximum négatif).
4. Conclure sur l'inégalité, ou sur la position des courbes.

**Exemple.** Comparer les courbes de $f(x) = x^3$ et $g(x) = x$. $h(x) = x^3 - x = x(x - 1)(x + 1)$.

| $x$ | $-\infty$ | | $-1$ | | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|---|---|
| $h(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ | |

La courbe de $x^3$ est au-dessus de la droite $y = x$ sur $]-1\,;\,0[$ et sur $]1\,;\,+\infty[$, en dessous ailleurs.

---

## Méthode 5 — Résoudre un problème d'optimisation

**Les étapes**

1. Faire un schéma, choisir la variable $x$ et son intervalle.
2. Exprimer la grandeur à optimiser en fonction de $x$ (utiliser les contraintes pour éliminer les autres variables).
3. Étudier les variations sur l'intervalle.
4. Conclure en répondant à la question (valeur de $x$, valeur optimale, unités).

**Exemple.** Une entreprise produit $q$ tonnes ($0 \leq q \leq 9$) d'un produit, vendu $30$ milliers d'euros la tonne. Le coût de production est $C(q) = q^3 - 9q^2 + 30q$ milliers d'euros. Le bénéfice vaut $B(q) = 30q - C(q) = -q^3 + 9q^2$.

$B'(q) = -3q^2 + 18q = -3q(q - 6)$, positif sur $]0\,;\,6[$ et négatif sur $]6\,;\,9[$. Le bénéfice est maximal pour $q = 6$ tonnes, et vaut $B(6) = -216 + 324 = 108$ milliers d'euros.
