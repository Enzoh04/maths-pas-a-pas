# Sujets type bac — Limites de fonctions

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Étude d'une fonction avec exponentielle | croissances comparées, dérivée, asymptote, tangente |
| 2 | Fraction rationnelle et asymptote oblique | limites en un réel, position relative, variations |
| 3 | QCM | limites variées |
| 4 | Modélisation : croissance d'une population | limite et interprétation, dérivée, Python |

## Sujet 1 — Une fonction avec exponentielle

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = (2x + 1)e^{-x}$, et on note $\mathcal{C}$ sa courbe représentative.

1. Déterminer la limite de $f$ en $-\infty$.
2. Déterminer la limite de $f$ en $+\infty$. Interpréter graphiquement ce résultat.
3. Montrer que pour tout réel $x$ : $f'(x) = (1 - 2x)e^{-x}$. Dresser le tableau de variations complet de $f$.
4. Résoudre l'équation $f(x) = 0$, puis étudier le signe de $f(x)$ selon les valeurs de $x$.
5. Déterminer une équation de la tangente $T$ à $\mathcal{C}$ au point d'abscisse $0$.

??? success "Correction"
    **1.** En $-\infty$ : $2x + 1 \to -\infty$ et $-x \to +\infty$, donc $e^{-x} \to +\infty$. Par produit, $\displaystyle\lim_{x\to-\infty} f(x) = -\infty$.

    **2.** En $+\infty$, on a une forme $\infty \times 0$. On développe : $f(x) = 2xe^{-x} + e^{-x} = 2\dfrac{x}{e^x} + e^{-x}$.

    Par croissance comparée, $\dfrac{x}{e^x} \to 0$, et $e^{-x} \to 0$. Donc $\displaystyle\lim_{x\to+\infty} f(x) = 0$ : l'axe des abscisses (droite $y = 0$) est asymptote horizontale à $\mathcal{C}$ en $+\infty$.

    **3.** $f = uv$ avec $u(x) = 2x + 1$, $u'(x) = 2$, $v(x) = e^{-x}$, $v'(x) = -e^{-x}$ :

    $$f'(x) = 2e^{-x} - (2x + 1)e^{-x} = (2 - 2x - 1)e^{-x} = (1 - 2x)e^{-x}.$$

    Comme $e^{-x} > 0$, $f'(x)$ a le signe de $1 - 2x$, positif pour $x < \frac{1}{2}$. On calcule $f\left(\frac{1}{2}\right) = 2e^{-1/2} = \dfrac{2}{\sqrt{e}} \approx 1{,}21$.

    | $x$ | $-\infty$ | | $\frac{1}{2}$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $-\infty$ | $\nearrow$ | $\frac{2}{\sqrt{e}}$ | $\searrow$ | $0$ |

    **4.** $e^{-x} > 0$, donc $f(x) = 0 \iff 2x + 1 = 0 \iff x = -\frac{1}{2}$. De même, $f(x)$ a le signe de $2x + 1$ : $f(x) < 0$ sur $\left]-\infty \,;\, -\frac{1}{2}\right[$ et $f(x) > 0$ sur $\left]-\frac{1}{2} \,;\, +\infty\right[$.

    **5.** $f(0) = 1$ et $f'(0) = 1$. La tangente a pour équation $y = f'(0)(x - 0) + f(0)$, soit $y = x + 1$.

---

## Sujet 2 — Asymptote oblique

On considère la fonction $f$ définie sur $]1 \,;\, +\infty[$ par $f(x) = \dfrac{x^2 - 3x + 6}{x - 1}$.

**Partie A — Limites et asymptotes**

1. Déterminer la limite de $f$ en $1$. Interpréter graphiquement.
2. Déterminer la limite de $f$ en $+\infty$.
3. Montrer que pour tout $x > 1$ : $f(x) = x - 2 + \dfrac{4}{x - 1}$.
4. En déduire que la droite $D$ d'équation $y = x - 2$ est asymptote à la courbe $\mathcal{C}_f$ en $+\infty$, c'est-à-dire que $\displaystyle\lim_{x\to+\infty} \big(f(x) - (x - 2)\big) = 0$. Étudier la position de $\mathcal{C}_f$ par rapport à $D$.

**Partie B — Variations**

5. Montrer que pour tout $x > 1$ : $f'(x) = \dfrac{(x - 3)(x + 1)}{(x - 1)^2}$.
6. Dresser le tableau de variations de $f$.
7. En déduire que pour tout $x > 1$, $f(x) \geq 3$.

??? success "Correction"
    **1.** Le numérateur tend vers $1 - 3 + 6 = 4 > 0$, et pour $x > 1$, $x - 1 \to 0^+$. Donc $\displaystyle\lim_{x\to 1^+} f(x) = +\infty$ : la droite $x = 1$ est asymptote verticale.

    **2.** En $+\infty$, par la règle des termes dominants : $\dfrac{x^2}{x} = x \to +\infty$.

    **3.** $(x - 2)(x - 1) + 4 = x^2 - 3x + 2 + 4 = x^2 - 3x + 6$. On divise par $x - 1 \neq 0$.

    **4.** $f(x) - (x - 2) = \dfrac{4}{x - 1} \to 0$ en $+\infty$ : $D$ est asymptote oblique. Comme $\dfrac{4}{x - 1} > 0$ pour $x > 1$, la courbe est **au-dessus** de $D$.

    **5.** Avec l'écriture de la question 3 : $f'(x) = 1 - \dfrac{4}{(x - 1)^2} = \dfrac{(x - 1)^2 - 4}{(x - 1)^2}$.

    Or $(x - 1)^2 - 4 = (x - 1 - 2)(x - 1 + 2) = (x - 3)(x + 1)$.

    **6.** Pour $x > 1$, $(x - 1)^2 > 0$ et $x + 1 > 0$ : $f'(x)$ a le signe de $x - 3$. On calcule $f(3) = \dfrac{9 - 9 + 6}{2} = 3$.

    | $x$ | $1$ | | $3$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | |
    | $f(x)$ | $+\infty$ | $\searrow$ | $3$ | $\nearrow$ | $+\infty$ |

    **7.** D'après le tableau, $f$ admet un minimum égal à $3$, atteint en $x = 3$. Donc $f(x) \geq 3$ pour tout $x > 1$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** $\displaystyle\lim_{x\to+\infty} \frac{3x^2 - x}{1 - 2x^2}$ vaut :

a) $-\frac{3}{2}$ — b) $\frac{3}{2}$ — c) $-\infty$ — d) $3$

**Question 2.** $\displaystyle\lim_{\substack{x\to 2 \\ x < 2}} \frac{1}{x^2 - 4}$ vaut :

a) $+\infty$ — b) $-\infty$ — c) $0$ — d) $\frac{1}{4}$

**Question 3.** $\displaystyle\lim_{x\to-\infty} x^2 e^x$ vaut :

a) $+\infty$ — b) $-\infty$ — c) $0$ — d) $1$

**Question 4.** $\displaystyle\lim_{x\to+\infty} \left(\sqrt{x^2 + 4x} - x\right)$ vaut :

a) $0$ — b) $2$ — c) $4$ — d) $+\infty$

**Question 5.** $\displaystyle\lim_{x\to 0} \frac{e^{3x} - 1}{x}$ vaut :

a) $0$ — b) $1$ — c) $3$ — d) $\frac{1}{3}$

??? success "Correction"
    **Question 1 : a).** Par les termes dominants : $\dfrac{3x^2}{-2x^2} = -\dfrac{3}{2}$.

    **Question 2 : b).** Pour $x$ proche de $2$ avec $x < 2$ (par exemple $1 < x < 2$), on a $x^2 < 4$, donc $x^2 - 4 \to 0^-$. Le quotient tend vers $-\infty$.

    **Question 3 : c).** Croissance comparée : $\displaystyle\lim_{x\to-\infty} x^n e^x = 0$ avec $n = 2$.

    **Question 4 : b).** Avec la quantité conjuguée : $\sqrt{x^2 + 4x} - x = \dfrac{4x}{\sqrt{x^2 + 4x} + x} = \dfrac{4}{\sqrt{1 + \frac{4}{x}} + 1} \to \dfrac{4}{2} = 2$.

    **Question 5 : c).** On pose $X = 3x \to 0$ : $\dfrac{e^{3x} - 1}{x} = 3 \times \dfrac{e^X - 1}{X} \to 3$.

---

## Sujet 4 — Croissance d'une population

Dans une réserve naturelle, on introduit 100 animaux d'une espèce protégée. Leur nombre est modélisé, $t$ années après l'introduction, par :

$$N(t) = \frac{1000}{1 + 9e^{-0{,}4t}}, \qquad t \geq 0.$$

1. Vérifier que $N(0) = 100$.
2. Déterminer $\displaystyle\lim_{t\to+\infty} N(t)$. Interpréter ce résultat dans le contexte.
3. Montrer que pour tout $t \geq 0$ : $N'(t) = \dfrac{3600\,e^{-0{,}4t}}{\left(1 + 9e^{-0{,}4t}\right)^2}$. En déduire le sens de variation de $N$.
4. Montrer que pour tout $t \geq 0$ : $N(t) = \dfrac{1000\,e^{0{,}4t}}{e^{0{,}4t} + 9}$.
5. Les gestionnaires veulent savoir au bout de combien d'années entières la population dépassera 900 animaux. Écrire une fonction Python qui répond à cette question, et donner le résultat à l'aide de la calculatrice.

??? success "Correction"
    **1.** $N(0) = \dfrac{1000}{1 + 9e^0} = \dfrac{1000}{10} = 100$.

    **2.** $-0{,}4t \to -\infty$, donc $e^{-0{,}4t} \to 0$ (composition), et $1 + 9e^{-0{,}4t} \to 1$. Ainsi $\displaystyle\lim_{t\to+\infty} N(t) = 1000$.

    À long terme, la population se stabilise autour de 1 000 animaux. C'est la capacité d'accueil de la réserve.

    **3.** $N = \dfrac{1000}{w}$ avec $w(t) = 1 + 9e^{-0{,}4t}$ et $w'(t) = 9 \times (-0{,}4)e^{-0{,}4t} = -3{,}6\,e^{-0{,}4t}$. Donc

    $$N'(t) = -\frac{1000\,w'(t)}{w(t)^2} = \frac{3600\,e^{-0{,}4t}}{\left(1 + 9e^{-0{,}4t}\right)^2}.$$

    Le numérateur et le dénominateur sont strictement positifs : $N'(t) > 0$ et $N$ est strictement croissante sur $[0 \,;\, +\infty[$.

    **4.** On multiplie le numérateur et le dénominateur par $e^{0{,}4t} > 0$ :

    $$N(t) = \frac{1000\,e^{0{,}4t}}{e^{0{,}4t} + 9e^{-0{,}4t}e^{0{,}4t}} = \frac{1000\,e^{0{,}4t}}{e^{0{,}4t} + 9}.$$

    **5.**

    ```python
    from math import exp

    def annees():
        t = 0
        while 1000 / (1 + 9 * exp(-0.4 * t)) <= 900:
            t = t + 1
        return t
    ```

    À la calculatrice : $N(10) \approx 858{,}5$ et $N(11) \approx 900{,}5$. Comme $N$ est croissante, la fonction renvoie **11** : la population dépasse 900 animaux au bout de 11 ans.

    *Au chapitre 5, le logarithme permettra de résoudre exactement l'inéquation $N(t) > 900$.*
