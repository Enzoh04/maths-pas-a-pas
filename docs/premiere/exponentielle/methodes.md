# Méthodes — Fonction exponentielle

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Simplifier une expression

**Les étapes**

1. Utiliser les règles : $e^a e^b = e^{a + b}$, $\dfrac{e^a}{e^b} = e^{a - b}$, $(e^a)^n = e^{na}$, $e^{-a} = \dfrac{1}{e^a}$.
2. Pour un quotient de sommes, **factoriser** par une exponentielle, ou multiplier numérateur et dénominateur par $e^x$.

**Exemple.** $\dfrac{e^{2x + 1} \times e^{-x}}{e^{x - 2}} = e^{2x + 1 - x - (x - 2)} = e^3$.

**Exemple.** $\dfrac{1 + e^{-x}}{1 - e^{-x}} = \dfrac{e^x(1 + e^{-x})}{e^x(1 - e^{-x})} = \dfrac{e^x + 1}{e^x - 1}$ (pour $x \neq 0$).

---

## Méthode 2 — Résoudre une équation ou une inéquation

**Les étapes**

1. Se ramener à la forme $e^A = e^B$ ou $e^A < e^B$, puis écrire $A = B$ ou $A < B$.
2. Penser que $1 = e^0$ et $e = e^1$.
3. Si l'expression contient $e^{2x}$ et $e^x$, poser $X = e^x$ (avec $X > 0$), ce qui donne une équation du second degré.
4. Pour un produit comme $(x - 2)e^x \geq 0$ : comme $e^x > 0$, c'est équivalent à $x - 2 \geq 0$.

**Exemple.** $e^{x^2} = e^{4x - 3} \iff x^2 - 4x + 3 = 0 \iff x = 1$ ou $x = 3$.

**Exemple.** $e^{2x} - (1 + e)e^x + e = 0$. Avec $X = e^x$ : $X^2 - (1 + e)X + e = 0$, de racines $1$ et $e$ (somme $1 + e$, produit $e$). Donc $e^x = 1$ ou $e^x = e$, soit $x = 0$ ou $x = 1$.

---

## Méthode 3 — Dériver une fonction avec l'exponentielle

**Les étapes**

1. Repérer la structure : produit $u \times e^{v}$, quotient, ou $e^{ax + b}$.
2. Utiliser $(e^x)' = e^x$ et $\left(e^{ax + b}\right)' = a\,e^{ax + b}$.
3. **Factoriser** le résultat par l'exponentielle.

**Exemple.** $f(x) = x\,e^{-x}$ : $f'(x) = 1 \times e^{-x} + x \times (-e^{-x}) = (1 - x)\,e^{-x}$.

---

## Méthode 4 — Étudier une fonction

**Les étapes**

1. Dériver et factoriser par l'exponentielle (méthode 3).
2. Comme $e^{\ldots} > 0$, le signe de $f'$ est celui de l'autre facteur.
3. Dresser le tableau de variations ; calculer les extremums (les laisser sous forme exacte, comme $\frac{1}{e}$ ou $-e$).

**Exemple.** Avec $f(x) = x\,e^{-x}$ : $f'(x)$ a le signe de $1 - x$. $f$ est croissante sur $]-\infty\,;\,1]$, décroissante sur $[1\,;\,+\infty[$, de maximum $f(1) = e^{-1} = \dfrac{1}{e}$.

---

## Méthode 5 — Modéliser une évolution exponentielle

**Les étapes**

1. Repérer une évolution à **taux constant** : en temps discret, suite géométrique ; en temps continu, fonction $C\,e^{kt}$.
2. Déterminer les constantes avec les données (valeur initiale, valeur à un instant donné).
3. Utiliser la croissance de l'exponentielle pour comparer, ou la dérivée pour étudier la vitesse d'évolution.

**Exemple.** Une tasse de café est à $80$ °C dans une pièce à $20$ °C. Sa température après $t$ minutes est $T(t) = 20 + 60\,e^{-0{,}1t}$. Alors $T(0) = 80$ et $T'(t) = -6\,e^{-0{,}1t} < 0$ : la température diminue. Comme $e^{-0{,}1t} > 0$, $T(t) > 20$ : le café ne descend jamais en dessous de la température de la pièce.
