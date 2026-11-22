# Méthodes — Équations, fonctions polynômes du second degré

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**. Les exemples se font sans calculatrice, comme à l'épreuve anticipée.

---

## Méthode 1 — Mettre un trinôme sous forme canonique

**Les étapes**

1. Factoriser par $a$ les termes en $x^2$ et en $x$ : $a\left(x^2 + \frac{b}{a}x\right) + c$.
2. Écrire $x^2 + px = \left(x + \frac{p}{2}\right)^2 - \frac{p^2}{4}$.
3. Développer le crochet et réduire les constantes.
4. **Vérifier** : $\alpha = -\frac{b}{2a}$ et $\beta = f(\alpha)$.

**Exemple.** $f(x) = -2x^2 + 12x - 10$.
$$f(x) = -2(x^2 - 6x) - 10 = -2\left[(x - 3)^2 - 9\right] - 10 = -2(x - 3)^2 + 18 - 10 = -2(x - 3)^2 + 8.$$
Vérification : $\alpha = -\frac{12}{-4} = 3$ et $f(3) = -18 + 36 - 10 = 8$.

---

## Méthode 2 — Trouver un extremum, résoudre un problème d'optimisation

**Les étapes**

1. Exprimer la grandeur à optimiser par une fonction $f$ d'une variable $x$, et préciser l'intervalle où $x$ varie.
2. Calculer $\alpha = -\frac{b}{2a}$ et $\beta = f(\alpha)$.
3. Si $a < 0$, $\beta$ est un **maximum** ; si $a > 0$, c'est un **minimum** (à condition que $\alpha$ soit dans l'intervalle).
4. Conclure **dans le contexte** du problème.

**Exemple.** Un rectangle a un périmètre de $20$ cm. Quelle est son aire maximale ?

Si l'une des dimensions est $x$ (avec $0 < x < 10$), l'autre vaut $10 - x$, et l'aire est $A(x) = x(10 - x) = -x^2 + 10x$. Ici $a = -1 < 0$, $\alpha = 5$ et $A(5) = 25$. L'aire est maximale, égale à $25$ cm², pour un **carré** de côté $5$ cm.

---

## Méthode 3 — Résoudre une équation du second degré

**Les étapes**

1. Tout ramener dans un membre : $ax^2 + bx + c = 0$.
2. Chercher d'abord une **méthode rapide** : factorisation évidente ($c = 0$), carré isolé ($b = 0$), identité remarquable, racine évidente.
3. Sinon, calculer $\Delta = b^2 - 4ac$ et appliquer le théorème.
4. Donner l'**ensemble des solutions** $S$.

**Exemple.** $2x^2 + x - 1 = 0$. $\Delta = 1 + 8 = 9$, $\sqrt{\Delta} = 3$. Solutions $\frac{-1 - 3}{4} = -1$ et $\frac{-1 + 3}{4} = \frac{1}{2}$. $S = \left\{-1\,;\,\frac{1}{2}\right\}$.

**Exemple.** $4x^2 = 9 \iff x^2 = \frac{9}{4} \iff x = \frac{3}{2}$ ou $x = -\frac{3}{2}$ : pas besoin de $\Delta$.

---

## Méthode 4 — Factoriser un trinôme

**Les étapes**

1. Trouver les racines (méthode 3), en cherchant d'abord une racine évidente.
2. Écrire $a(x - x_1)(x - x_2)$ — **sans oublier le coefficient $a$**.
3. Vérifier en développant, ou en calculant une valeur.

**Exemple.** $3x^2 - 5x + 2$ : $1$ est racine évidente ($3 - 5 + 2 = 0$). Le produit des racines vaut $\frac{c}{a} = \frac{2}{3}$, donc l'autre racine est $\frac{2}{3}$. D'où $3x^2 - 5x + 2 = 3(x - 1)\left(x - \frac{2}{3}\right) = (x - 1)(3x - 2)$.

---

## Méthode 5 — Étudier un signe, résoudre une inéquation

**Les étapes**

1. Tout ramener dans un membre, comparé à $0$.
2. Pour un trinôme : racines, puis règle « **signe de $a$ à l'extérieur des racines** ».
3. Pour un produit ou un quotient : un **tableau de signes**, avec une ligne par facteur, et une double barre aux valeurs interdites.
4. Lire l'ensemble des solutions, en faisant attention aux bornes (crochets ouverts ou fermés, valeurs interdites exclues).

**Exemple.** Résoudre $\dfrac{x^2 - 4}{x - 1} \geq 0$.

| $x$ | $-\infty$ | | $-2$ | | $1$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|---|---|
| $x^2 - 4$ | | $+$ | $0$ | $-$ | | $-$ | $0$ | $+$ | |
| $x - 1$ | | $-$ | | $-$ | $0$ | $+$ | | $+$ | |
| quotient | | $-$ | $0$ | $+$ | ‖ | $-$ | $0$ | $+$ | |

$S = [-2\,;\,1[\, \cup \,[2\,;\,+\infty[$.

---

## Méthode 6 — Étudier la position de deux courbes

**Les étapes**

1. Pour les **points d'intersection** des courbes de $f$ et $g$ : résoudre $f(x) = g(x)$, puis calculer les ordonnées.
2. Pour la **position relative** : étudier le signe de $f(x) - g(x)$. Là où il est positif, la courbe de $f$ est au-dessus de celle de $g$.

**Exemple.** $f(x) = x^2$ et $g(x) = 2x + 3$. $f(x) - g(x) = x^2 - 2x - 3 = (x + 1)(x - 3)$. Les courbes se coupent aux points $(-1\,;\,1)$ et $(3\,;\,9)$. La parabole est au-dessus de la droite sur $]-\infty\,;\,-1[$ et sur $]3\,;\,+\infty[$, en dessous sur $]-1\,;\,3[$.
