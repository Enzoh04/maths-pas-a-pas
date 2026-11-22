# Sujets type bac — Continuité

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Fonction auxiliaire | TVI sur deux intervalles, signe, variations |
| 2 | Suite récurrente et point fixe | récurrence, convergence monotone, point fixe, Python |
| 3 | QCM | continuité, TVI, dichotomie |
| 4 | Modélisation : refroidissement d'une boisson | TVI, interprétation, dichotomie en Python |

## Sujet 1 — Fonction auxiliaire

**Partie A.** Soit $g$ la fonction définie sur $\mathbb{R}$ par $g(x) = e^x - x - 2$.

1. Déterminer les limites de $g$ en $-\infty$ et en $+\infty$.
2. Étudier les variations de $g$ et dresser son tableau de variations.
3. Montrer que l'équation $g(x) = 0$ admet exactement deux solutions $\beta < 0 < \alpha$.
4. Montrer que $1 < \alpha < 2$ et $-2 < \beta < -1$. Donner une valeur approchée de $\alpha$ à $10^{-2}$ près.
5. En déduire le signe de $g(x)$ selon les valeurs de $x$.

**Partie B.** Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = e^x - \dfrac{x^2}{2} - 2x$.

6. Calculer $f'(x)$ et en déduire les variations de $f$.

??? success "Correction"
    **1.** En $-\infty$ : $e^x \to 0$ et $-x - 2 \to +\infty$, donc $g \to +\infty$. En $+\infty$ : $g(x) = e^x\left(1 - \frac{x}{e^x} - \frac{2}{e^x}\right)$ ; par croissance comparée, la parenthèse tend vers $1$, donc $g \to +\infty$.

    **2.** $g'(x) = e^x - 1$, négatif sur $]-\infty \,;\, 0]$, positif sur $[0 \,;\, +\infty[$. $g(0) = 1 - 2 = -1$.

    | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $g'(x)$ | | $-$ | $0$ | $+$ | |
    | $g(x)$ | $+\infty$ | $\searrow$ | $-1$ | $\nearrow$ | $+\infty$ |

    **3.** Sur $]-\infty \,;\, 0]$, $g$ est continue, strictement décroissante, de $+\infty$ à $-1$, et $0 \in \,]-1 \,;\, +\infty[$ : une unique solution $\beta < 0$. Sur $[0 \,;\, +\infty[$, $g$ est continue, strictement croissante, de $-1$ à $+\infty$ : une unique solution $\alpha > 0$. Il y a exactement deux solutions.

    **4.** $g(1) = e - 3 \approx -0{,}28 < 0$ et $g(2) = e^2 - 4 \approx 3{,}39 > 0$, donc $1 < \alpha < 2$. $g(-2) = e^{-2} \approx 0{,}14 > 0$ et $g(-1) = e^{-1} - 1 \approx -0{,}63 < 0$, donc $-2 < \beta < -1$.

    À la calculatrice, $\alpha \approx 1{,}15$ (plus précisément $1{,}146$).

    **5.** D'après le tableau : $g(x) > 0$ sur $]-\infty \,;\, \beta[$ et sur $]\alpha \,;\, +\infty[$, $g(x) < 0$ sur $]\beta \,;\, \alpha[$, et $g$ s'annule en $\beta$ et en $\alpha$.

    **6.** $f'(x) = e^x - x - 2 = g(x)$. Donc $f$ est croissante sur $]-\infty \,;\, \beta]$, décroissante sur $[\beta \,;\, \alpha]$, et croissante sur $[\alpha \,;\, +\infty[$.

---

## Sujet 2 — Suite récurrente et point fixe

Soit $f$ la fonction définie sur $[0 \,;\, +\infty[$ par $f(x) = \dfrac{4x + 2}{x + 3}$, et la suite $(u_n)$ définie par $u_0 = 0$ et $u_{n+1} = f(u_n)$.

1. Montrer que $f$ est strictement croissante sur $[0 \,;\, +\infty[$ et calculer $f(2)$.
2. Calculer $u_1$ et $u_2$.
3. Démontrer par récurrence que pour tout entier $n$ : $0 \leq u_n \leq u_{n+1} \leq 2$.
4. En déduire que $(u_n)$ converge, et déterminer sa limite.
5. Écrire une fonction Python qui renvoie le plus petit entier $n$ tel que $2 - u_n < 10^{-3}$. On admet qu'elle renvoie $10$. Interpréter.

??? success "Correction"
    **1.** $f'(x) = \dfrac{4(x + 3) - (4x + 2)}{(x + 3)^2} = \dfrac{10}{(x + 3)^2} > 0$. $f(2) = \dfrac{10}{5} = 2$.

    **2.** $u_1 = f(0) = \frac{2}{3}$ et $u_2 = f\left(\frac{2}{3}\right) = \dfrac{\frac{8}{3} + 2}{\frac{2}{3} + 3} = \dfrac{14/3}{11/3} = \dfrac{14}{11}$.

    **3.** Soit $\mathcal{P}(n)$ : « $0 \leq u_n \leq u_{n+1} \leq 2$ ».

    - Initialisation : $u_0 = 0$, $u_1 = \frac{2}{3}$, et $0 \leq 0 \leq \frac{2}{3} \leq 2$.
    - Hérédité : si $0 \leq u_n \leq u_{n+1} \leq 2$, comme $f$ est croissante sur $[0 \,;\, +\infty[$ : $f(0) \leq f(u_n) \leq f(u_{n+1}) \leq f(2)$, soit $\frac{2}{3} \leq u_{n+1} \leq u_{n+2} \leq 2$, donc en particulier $0 \leq u_{n+1}$.
    - Conclusion : $\mathcal{P}(n)$ est vraie pour tout $n$.

    **4.** $(u_n)$ est croissante et majorée par $2$ : elle converge vers $\ell \in [0 \,;\, 2]$. $f$ est continue sur $[0 \,;\, +\infty[$ (fraction rationnelle de dénominateur non nul), donc $f(\ell) = \ell$ :

    $$\frac{4\ell + 2}{\ell + 3} = \ell \iff 4\ell + 2 = \ell^2 + 3\ell \iff \ell^2 - \ell - 2 = 0 \iff (\ell - 2)(\ell + 1) = 0.$$

    Comme $\ell \geq 0$, on obtient $\ell = 2$.

    **5.**

    ```python
    def seuil():
        n, u = 0, 0
        while 2 - u >= 0.001:
            u = (4 * u + 2) / (u + 3)
            n = n + 1
        return n
    ```

    À partir du rang $10$, $u_n$ est une approximation de la limite $2$ à moins de $10^{-3}$ près (la suite étant croissante, elle s'en rapproche par en dessous).

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** Soit $f$ définie par $f(x) = x^2$ si $x < 1$ et $f(x) = ax + 1$ si $x \geq 1$. $f$ est continue sur $\mathbb{R}$ si et seulement si :

a) $a = 1$ — b) $a = 0$ — c) $a = 2$ — d) pour tout $a$

**Question 2.** La suite définie par $u_0 = 0$ et $u_{n+1} = 0{,}5\,u_n + 1$ converge. Sa limite est :

a) $0$ — b) $1$ — c) $2$ — d) $0{,}5$

**Question 3.** Le nombre de solutions réelles de l'équation $x^3 + 2x - 5 = 0$ est :

a) $0$ — b) $1$ — c) $2$ — d) $3$

**Question 4.** On applique la dichotomie sur $[0 \,;\, 1]$. Le nombre minimal d'étapes pour obtenir un encadrement d'amplitude strictement inférieure à $0{,}01$ est :

a) $5$ — b) $6$ — c) $7$ — d) $100$

**Question 5.** Soit $f$ continue sur $[0 \,;\, 2]$ avec $f(0) = 3$ et $f(2) = -1$. Alors :

a) l'équation $f(x) = 0$ a exactement une solution dans $[0 \,;\, 2]$
b) l'équation $f(x) = 0$ a au moins une solution dans $[0 \,;\, 2]$
c) $f$ est décroissante sur $[0 \,;\, 2]$
d) l'équation $f(x) = 4$ n'a pas de solution dans $[0 \,;\, 2]$

??? success "Correction"
    **Question 1 : b).** En $1$ : la limite à gauche vaut $1$ et $f(1) = a + 1$. Il faut $a + 1 = 1$, soit $a = 0$.

    **Question 2 : c).** $x \mapsto 0{,}5x + 1$ est continue ; la limite vérifie $\ell = 0{,}5\ell + 1$, soit $\ell = 2$.

    **Question 3 : b).** $f(x) = x^3 + 2x - 5$ est continue, $f'(x) = 3x^2 + 2 > 0$, et ses limites sont $-\infty$ et $+\infty$ : exactement une solution.

    **Question 4 : c).** Il faut $\frac{1}{2^n} < 0{,}01$, soit $2^n > 100$. $2^6 = 64$ et $2^7 = 128$ : $n = 7$.

    **Question 5 : b).** C'est le TVI ($0$ est entre $-1$ et $3$). La réponse a) est fausse car $f$ peut changer de sens de variation et s'annuler plusieurs fois ; c) n'est pas garanti ; d) n'est pas garanti non plus, car $f$ peut dépasser $3$ entre $0$ et $2$.

---

## Sujet 4 — Refroidissement d'une boisson

On sert une boisson chaude à 90 °C dans une pièce à 20 °C. Sa température, en °C, $t$ minutes après avoir été servie, est modélisée par :

$$T(t) = 20 + 70\,e^{-0{,}1t}, \qquad t \geq 0.$$

1. Vérifier que $T(0) = 90$, puis déterminer $\displaystyle\lim_{t\to+\infty} T(t)$. Interpréter.
2. Étudier les variations de $T$.
3. Montrer qu'il existe un unique instant $t_1$ où la boisson est à 60 °C, et un unique instant $t_2$ où elle est à 50 °C. Comparer $t_1$ et $t_2$.
4. On souhaite déterminer $t_2$ à $0{,}01$ minute près. Compléter la fonction Python suivante, qui applique la dichotomie sur $[0 \,;\, 20]$.

    ```python
    from math import exp

    def T(t):
        return 20 + 70 * exp(-0.1 * t)

    def instant(temp):
        a, b = 0, 20
        while b - a > 0.01:
            m = (a + b) / 2
            if T(m) > temp:
                ......
            else:
                ......
        return a, b
    ```

5. Que renvoie `instant(50)`, approximativement ? On admet que la boisson est agréable à boire entre 50 °C et 60 °C : pendant combien de temps environ ?

??? success "Correction"
    **1.** $T(0) = 20 + 70 = 90$. $-0{,}1t \to -\infty$ donc $e^{-0{,}1t} \to 0$ et $T(t) \to 20$. À long terme, la boisson atteint la température de la pièce.

    **2.** $T'(t) = 70 \times (-0{,}1)e^{-0{,}1t} = -7e^{-0{,}1t} < 0$ : $T$ est strictement décroissante sur $[0 \,;\, +\infty[$.

    **3.** $T$ est continue et strictement décroissante sur $[0 \,;\, +\infty[$, de $90$ vers $20$. Comme $60$ et $50$ appartiennent à $]20 \,;\, 90]$, le corollaire du TVI (version avec limite) donne l'existence et l'unicité de $t_1$ et $t_2$. Comme $T$ est décroissante et $T(t_1) = 60 > 50 = T(t_2)$, on a $t_1 < t_2$.

    **4.** Si $T(m) > temp$, la boisson est encore trop chaude en $m$ : l'instant cherché est après $m$, donc on pose `a = m`. Sinon, on pose `b = m`.

    ```python
            if T(m) > temp:
                a = m
            else:
                b = m
    ```

    **5.** La fonction renvoie un intervalle d'amplitude inférieure à $0{,}01$ autour de $t_2 \approx 8{,}47$ min. De même, $t_1 \approx 5{,}60$ min. La boisson est agréable pendant environ $8{,}47 - 5{,}60 \approx 2{,}9$ minutes, soit à peu près 3 minutes.

    *Au chapitre 5, le logarithme donnera les valeurs exactes : $t_2 = 10\ln\frac{7}{3}$ et $t_1 = 10\ln\frac{7}{4}$.*
