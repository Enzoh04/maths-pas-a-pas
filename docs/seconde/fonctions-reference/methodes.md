# Méthodes — Fonctions de référence

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Comparer des images à l'aide des variations

**Les étapes**

1. Identifier la fonction de référence en jeu et l'intervalle où se trouvent les deux nombres.
2. Vérifier que les deux nombres sont dans un **même intervalle** où la fonction est monotone.
3. Conclure : une fonction **croissante** conserve l'ordre, une fonction **décroissante** le renverse.

**Exemples.**

- Comparer $(-3{,}2)^2$ et $(-2{,}9)^2$ : $-3{,}2 < -2{,}9 \leq 0$ et la fonction carré est décroissante sur $]-\infty\,;\,0]$, donc $(-3{,}2)^2 > (-2{,}9)^2$.
- Comparer $\frac{1}{\pi}$ et $\frac{1}{3}$ : $0 < 3 < \pi$ et la fonction inverse est décroissante sur $]0\,;\,+\infty[$, donc $\frac{1}{\pi} < \frac{1}{3}$.
- Comparer $\sqrt{7}$ et $\sqrt{6{,}9}$ : la racine est croissante, donc $\sqrt{6{,}9} < \sqrt{7}$.

---

## Méthode 2 — Encadrer $f(x)$ à partir d'un encadrement de $x$

**Les étapes**

1. Repérer si l'intervalle de $x$ contient un **changement de sens** de variation (le $0$ pour le carré et la valeur absolue ; le $0$ interdit pour l'inverse).
2. Si la fonction est monotone sur l'intervalle, appliquer la fonction aux bornes (en inversant l'ordre si elle est décroissante).
3. Sinon, découper l'intervalle, ou utiliser le tableau de variations.

**Exemples.**

- Si $1 \leq x \leq 4$ : $1 \leq x^2 \leq 16$ ; $\frac{1}{4} \leq \frac{1}{x} \leq 1$ ; $1 \leq \sqrt{x} \leq 2$.
- Si $-3 \leq x \leq 2$ : la fonction carré change de sens en $0$. Son minimum sur l'intervalle est $0$, son maximum est $(-3)^2 = 9$. Donc $0 \leq x^2 \leq 9$ (et **non** $4 \leq x^2 \leq 9$).

---

## Méthode 3 — Résoudre $x^2 = k$, $x^2 < k$, $x^2 > k$

**Les étapes**

1. Isoler $x^2$.
2. Selon le signe de $k$ : si $k < 0$, $x^2 = k$ et $x^2 < k$ n'ont pas de solution, $x^2 > k$ est vraie pour tout $x$ ; si $k = 0$, $x^2 = 0 \iff x = 0$.
3. Si $k > 0$ : $x^2 = k \iff x = \pm\sqrt{k}$ ; $x^2 < k \iff x \in \left]-\sqrt{k}\,;\,\sqrt{k}\right[$ ; $x^2 > k$ : à l'**extérieur**.
4. Vérifier avec la courbe de la fonction carré et la droite $y = k$.

**Exemple.** $2x^2 - 5 \geq 3 \iff x^2 \geq 4 \iff x \in ]-\infty\,;\,-2] \cup [2\,;\,+\infty[$.

---

## Méthode 4 — Résoudre $\frac{1}{x} = k$, $\frac{1}{x} < k$

**Les étapes**

1. Exclure $x = 0$.
2. $\frac{1}{x} = k$ : si $k \neq 0$, $x = \frac{1}{k}$ ; si $k = 0$, pas de solution.
3. Pour une inéquation, s'aider de la **courbe** (hyperbole) et de la droite $y = k$ : attention aux **deux branches**. Ou bien se ramener à un quotient : $\frac{1}{x} - k < 0 \iff \frac{1 - kx}{x} < 0$, puis tableau de signes.

**Exemple.** $\frac{1}{x} < 2$. Pour $x < 0$, $\frac{1}{x} < 0 < 2$ : toujours vrai. Pour $x > 0$, la fonction inverse étant décroissante, $\frac{1}{x} < 2 = \frac{1}{0{,}5} \iff x > 0{,}5$. $S = ]-\infty\,;\,0[ \cup ]0{,}5\,;\,+\infty[$.

---

## Méthode 5 — Démontrer un sens de variation

**Les étapes**

1. Prendre deux réels $a < b$ dans l'intervalle étudié.
2. Calculer $f(b) - f(a)$ et le **factoriser** (souvent par $b - a$).
3. Étudier le **signe** de chaque facteur sur l'intervalle.
4. Conclure : $f(b) - f(a) > 0$ pour tout $a < b$ : croissante ; $< 0$ : décroissante.

**Exemple.** $f(x) = (x - 1)^2$ sur $[1\,;\,+\infty[$. Pour $1 \leq a < b$ :
$$f(b) - f(a) = (b - 1)^2 - (a - 1)^2 = (b - a)(b + a - 2).$$
$b - a > 0$ et $b + a - 2 > 0$ (car $a \geq 1$ et $b > 1$) : $f$ est strictement croissante sur $[1\,;\,+\infty[$.
