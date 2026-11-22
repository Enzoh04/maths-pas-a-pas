# Sujets type bac — Fonction logarithme népérien

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Étude de $x^2 - 2\ln x$ | limites, variations, convexité, TVI |
| 2 | Suite arithmético-géométrique | suite auxiliaire, seuil exact avec $\ln$, Python |
| 3 | QCM | propriétés, équations, dérivée, limites |
| 4 | Modélisation : niveau sonore en décibels | logarithme décimal, interprétation |

## Sujet 1 — Étude d'une fonction

Soit $f$ la fonction définie sur $]0 \,;\, +\infty[$ par $f(x) = x^2 - 2\ln x$, et $\mathcal{C}$ sa courbe.

1. Déterminer la limite de $f$ en $0$.
2. Montrer que pour tout $x > 0$, $f(x) = x^2\left(1 - \dfrac{2\ln x}{x^2}\right)$, et en déduire la limite de $f$ en $+\infty$.
3. Montrer que $f'(x) = \dfrac{2(x - 1)(x + 1)}{x}$ et dresser le tableau de variations de $f$.
4. Étudier la convexité de $f$.
5. Montrer que l'équation $f(x) = 2$ admet exactement deux solutions $\alpha < 1 < \beta$. Donner un encadrement de $\beta$ d'amplitude $10^{-1}$.

??? success "Correction"
    **1.** En $0^+$ : $x^2 \to 0$ et $-2\ln x \to +\infty$, donc $f \to +\infty$.

    **2.** Pour $x > 0$, en développant : $x^2\left(1 - \frac{2\ln x}{x^2}\right) = x^2 - 2\ln x$. Par croissance comparée, $\frac{\ln x}{x^2} \to 0$, donc la parenthèse tend vers $1$, et $f \to +\infty$.

    **3.** $f'(x) = 2x - \dfrac{2}{x} = \dfrac{2x^2 - 2}{x} = \dfrac{2(x - 1)(x + 1)}{x}$. Sur $]0 \,;\, +\infty[$, $x > 0$ et $x + 1 > 0$ : $f'(x)$ a le signe de $x - 1$. Minimum : $f(1) = 1$.

    | $x$ | $0$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | |
    | $f(x)$ | $+\infty$ | $\searrow$ | $1$ | $\nearrow$ | $+\infty$ |

    **4.** $f''(x) = 2 + \dfrac{2}{x^2} > 0$ : $f$ est convexe sur $]0 \,;\, +\infty[$.

    **5.** Sur $]0 \,;\, 1]$, $f$ est continue, strictement décroissante, de $+\infty$ à $1$, et $2 \in [1 \,;\, +\infty[$ : une unique solution $\alpha$, avec $\alpha < 1$ puisque $f(1) = 1 \neq 2$. Sur $[1 \,;\, +\infty[$, de même, une unique solution $\beta > 1$.

    À la calculatrice : $f(1{,}7) = 2{,}89 - 2\ln 1{,}7 \approx 1{,}83 < 2$ et $f(1{,}8) = 3{,}24 - 2\ln 1{,}8 \approx 2{,}06 > 2$. Donc $1{,}7 < \beta < 1{,}8$.

---

## Sujet 2 — Suite arithmético-géométrique

Un étang contient 2 tonnes de poissons. Chaque année, 10 % des poissons disparaissent (pêche, prédateurs) et l'on réintroduit 2 tonnes de poissons. On note $u_n$ la masse de poissons, en tonnes, au bout de $n$ années. Ainsi $u_0 = 2$ et $u_{n+1} = 0{,}9\,u_n + 2$.

1. Calculer $u_1$ et $u_2$.
2. On pose $v_n = u_n - 20$. Montrer que $(v_n)$ est géométrique.
3. En déduire que $u_n = 20 - 18 \times 0{,}9^n$, puis la limite de $(u_n)$. Interpréter.
4. Déterminer **par le calcul** à partir de quelle année la masse de poissons dépassera 19 tonnes.
5. Écrire une fonction Python qui permet de vérifier ce résultat.

??? success "Correction"
    **1.** $u_1 = 0{,}9 \times 2 + 2 = 3{,}8$ et $u_2 = 0{,}9 \times 3{,}8 + 2 = 5{,}42$.

    **2.** $v_{n+1} = u_{n+1} - 20 = 0{,}9u_n - 18 = 0{,}9(u_n - 20) = 0{,}9v_n$. $(v_n)$ est géométrique de raison $0{,}9$, de premier terme $v_0 = -18$.

    **3.** $v_n = -18 \times 0{,}9^n$, donc $u_n = 20 - 18 \times 0{,}9^n$. Comme $0 < 0{,}9 < 1$, $0{,}9^n \to 0$ et $u_n \to 20$ : à long terme, la masse se stabilise à 20 tonnes.

    **4.** $u_n > 19 \iff 18 \times 0{,}9^n < 1 \iff 0{,}9^n < \frac{1}{18} \iff n\ln 0{,}9 < -\ln 18$.

    Comme $\ln 0{,}9 < 0$ : $n > \dfrac{-\ln 18}{\ln 0{,}9} \approx 27{,}4$. La masse dépasse 19 tonnes à partir de la **28ᵉ année**.

    **5.**

    ```python
    def annee():
        n, u = 0, 2
        while u <= 19:
            u = 0.9 * u + 2
            n = n + 1
        return n
    ```

    Elle renvoie $28$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** $\ln(e^2) - \ln\sqrt{e}$ est égal à :

a) $\frac{3}{2}$ — b) $2 - \sqrt{e}$ — c) $\frac{5}{2}$ — d) $1$

**Question 2.** L'ensemble des solutions de l'équation $\ln(x + 3) = \ln(2x)$ est :

a) $\varnothing$ — b) $\{3\}$ — c) $\{-3 \,;\, 3\}$ — d) $]0 \,;\, +\infty[$

**Question 3.** La dérivée de $x \mapsto \ln(3x^2 + 1)$ est :

a) $\dfrac{1}{3x^2 + 1}$ — b) $\dfrac{6x}{3x^2 + 1}$ — c) $\dfrac{6x}{\ln(3x^2 + 1)}$ — d) $6x\ln(3x^2 + 1)$

**Question 4.** $\displaystyle\lim_{x\to 0^+} x\ln x$ vaut :

a) $-\infty$ — b) $0$ — c) $1$ — d) elle n'existe pas

**Question 5.** Le plus petit entier $n$ tel que $0{,}5^n < 10^{-3}$ est :

a) $3$ — b) $9$ — c) $10$ — d) $1000$

??? success "Correction"
    **Question 1 : a).** $2 - \frac{1}{2} = \frac{3}{2}$.

    **Question 2 : b).** Il faut $x > 0$. Alors $x + 3 = 2x \iff x = 3$, qui convient.

    **Question 3 : b).** $(\ln u)' = \frac{u'}{u}$ avec $u' = 6x$.

    **Question 4 : b).** Croissance comparée (démonstration au programme).

    **Question 5 : c).** $n > \dfrac{\ln 1000}{\ln 2} \approx 9{,}97$, donc $n = 10$. *Vérification : $2^{10} = 1024 > 1000$.*

---

## Sujet 4 — Niveau sonore en décibels

Le **logarithme décimal** est la fonction définie sur $]0 \,;\, +\infty[$ par $\log x = \dfrac{\ln x}{\ln 10}$.

Le niveau sonore $L$, en décibels (dB), d'un son d'intensité $I$ (en W/m²) est $L = 10\log\left(\dfrac{I}{I_0}\right)$, où $I_0 = 10^{-12}$ W/m² est le seuil d'audibilité.

1. Montrer que $\log(10^n) = n$ pour tout entier $n$, et que $\log(ab) = \log a + \log b$ pour tous $a, b > 0$.
2. Quel est le niveau sonore d'un son d'intensité $I_0$ ? d'intensité $10^{-6}$ W/m² ?
3. Montrer que lorsque l'intensité **double**, le niveau sonore augmente d'environ 3 dB.
4. Une conversation produit 60 dB, un concert 90 dB. Combien de fois l'intensité du concert est-elle plus grande ?
5. Une machine produit 70 dB. Combien faut-il, au minimum, de machines identiques fonctionnant ensemble (les intensités s'additionnent) pour dépasser 85 dB, seuil de danger pour l'audition ?

??? success "Correction"
    **1.** $\log(10^n) = \dfrac{n\ln 10}{\ln 10} = n$. Et $\log(ab) = \dfrac{\ln a + \ln b}{\ln 10} = \log a + \log b$.

    **2.** $L(I_0) = 10\log 1 = 0$ dB. $L(10^{-6}) = 10\log(10^{6}) = 60$ dB.

    **3.** $L(2I) = 10\log\left(2\frac{I}{I_0}\right) = 10\log 2 + L(I)$, et $10\log 2 = \dfrac{10\ln 2}{\ln 10} \approx 3{,}01$.

    **4.** $90 - 60 = 30 = 10\log\dfrac{I_2}{I_1}$, donc $\log\dfrac{I_2}{I_1} = 3$ et $\dfrac{I_2}{I_1} = 10^3 = 1000$. Le concert est **1 000 fois** plus intense.

    **5.** Avec $n$ machines, l'intensité est multipliée par $n$ : $L_n = 70 + 10\log n$. On veut $70 + 10\log n > 85$, soit $\log n > 1{,}5$, c'est-à-dire $\ln n > 1{,}5\ln 10$, donc $n > 10^{1{,}5} \approx 31{,}6$. Il faut **32 machines**.

    *Le logarithme « écrase » les grandes intensités : multiplier le bruit par 32 n'ajoute que 15 dB. C'est pour cela que l'échelle des décibels est adaptée à l'oreille humaine, qui perçoit des intensités allant de 1 à 1 000 milliards.*
