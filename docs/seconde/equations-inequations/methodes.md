# Méthodes — Équations et inéquations

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Résoudre une équation en se ramenant à un produit nul

**Les étapes**

1. Si l'équation est du premier degré (pas de $x^2$ après développement), isoler $x$.
2. Sinon, **tout passer dans le membre de gauche** pour obtenir $\ldots = 0$.
3. **Factoriser** (facteur commun, identité remarquable).
4. Appliquer la règle du produit nul et conclure par l'ensemble $S$.

**Exemple.** Résoudre $(x + 2)^2 = 4(x + 2)$.
$$(x + 2)^2 - 4(x + 2) = 0 \iff (x + 2)(x + 2 - 4) = 0 \iff (x + 2)(x - 2) = 0.$$
$S = \{-2\,;\,2\}$.

**Exemple.** Résoudre $(3x - 1)^2 = 25$ : $3x - 1 = 5$ ou $3x - 1 = -5$, donc $x = 2$ ou $x = -\frac{4}{3}$.

---

## Méthode 2 — Résoudre une équation quotient

**Les étapes**

1. Chercher les **valeurs interdites** (celles qui annulent un dénominateur).
2. Se ramener à $\frac{A(x)}{B(x)} = 0$ : tout passer à gauche et réduire au même dénominateur.
3. Résoudre $A(x) = 0$, puis **éliminer** les valeurs interdites.

**Exemple.** Résoudre $\dfrac{2x + 1}{x - 1} = 3$. Valeur interdite : $1$.
$$\frac{2x + 1}{x - 1} - 3 = 0 \iff \frac{2x + 1 - 3(x - 1)}{x - 1} = 0 \iff \frac{-x + 4}{x - 1} = 0.$$
$-x + 4 = 0 \iff x = 4$, qui n'est pas interdit. $S = \{4\}$.

---

## Méthode 3 — Résoudre une inéquation du premier degré

**Les étapes**

1. Développer et réduire chaque membre.
2. Regrouper les termes en $x$ d'un côté, les constantes de l'autre.
3. Diviser par le coefficient de $x$ : **changer le sens** s'il est **négatif**.
4. Écrire l'ensemble des solutions sous forme d'**intervalle**.

**Exemple.** $2(x - 3) > 5x + 3 \iff 2x - 6 > 5x + 3 \iff -3x > 9 \iff x < -3$. $S = ]-\infty\,;\,-3[$.

---

## Méthode 4 — Dresser un tableau de signes

**Les étapes**

1. Écrire l'expression sous forme d'un **produit** ou d'un **quotient** de facteurs affines (factoriser si besoin).
2. Pour chaque facteur $ax + b$ : trouver la valeur qui l'annule, $-\frac{b}{a}$, et appliquer la règle « **signe de $a$ à droite du zéro** ».
3. Placer toutes les valeurs remarquables **dans l'ordre croissant** sur la première ligne.
4. Une ligne par facteur, puis la dernière ligne avec la **règle des signes** ; une **double barre** pour les valeurs interdites.

**Exemple.** Signe de $Q(x) = \dfrac{3 - x}{2x + 4}$. $3 - x$ s'annule en $3$ ($a = -1$) ; $2x + 4$ s'annule en $-2$ ($a = 2$), valeur interdite.

| $x$ | $-\infty$ | | $-2$ | | $3$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $3 - x$ | | $+$ | | $+$ | $0$ | $-$ | |
| $2x + 4$ | | $-$ | $0$ | $+$ | | $+$ | |
| $Q(x)$ | | $-$ | $\parallel$ | $+$ | $0$ | $-$ | |

---

## Méthode 5 — Résoudre une inéquation produit ou quotient

**Les étapes**

1. Tout passer à gauche pour obtenir « $\ldots \geq 0$ » (ou $>$, $\leq$, $<$). Ne **jamais** multiplier les deux membres par une expression contenant $x$.
2. Factoriser, ou réduire au même dénominateur.
3. Dresser le tableau de signes.
4. Lire les intervalles où l'expression a le signe voulu ; inclure les zéros pour $\geq$ ou $\leq$, **jamais** les valeurs interdites.

**Exemple.** Résoudre $x^2 \leq 2x$. $x^2 - 2x \leq 0 \iff x(x - 2) \leq 0$. Les facteurs s'annulent en $0$ et $2$ ; le produit est négatif entre ces deux valeurs. $S = [0\,;\,2]$.

**Exemple.** Résoudre $\dfrac{1}{x} < 2$. Valeur interdite $0$. $\frac{1}{x} - 2 < 0 \iff \frac{1 - 2x}{x} < 0$. Zéros : $\frac{1}{2}$ pour le numérateur, $0$ (interdite) pour le dénominateur.

| $x$ | $-\infty$ | | $0$ | | $\frac{1}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $1 - 2x$ | | $+$ | | $+$ | $0$ | $-$ | |
| $x$ | | $-$ | $0$ | $+$ | | $+$ | |
| quotient | | $-$ | $\parallel$ | $+$ | $0$ | $-$ | |

$S = ]-\infty\,;\,0[ \cup \left]\frac{1}{2}\,;\,+\infty\right[$.
