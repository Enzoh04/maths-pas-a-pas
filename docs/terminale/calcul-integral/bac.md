# Sujets type bac — Calcul intégral

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Aire sous une courbe et limite | primitive, intégration par parties, croissance comparée |
| 2 | Suite d'intégrales | relation de récurrence, monotonie, encadrement, limite |
| 3 | QCM | calculs, propriétés, fonction définie par une intégrale |
| 4 | Modélisation : distance parcourue par un véhicule | intégrale d'une vitesse, valeur moyenne, rectangles |

## Sujet 1 — Aire sous une courbe

Soit $f$ la fonction définie sur $[0 \,;\, +\infty[$ par $f(x) = xe^{-x}$. Pour tout réel $a > 0$, on note $\mathcal{A}(a)$ l'aire, en unités d'aire, du domaine compris entre la courbe de $f$, l'axe des abscisses et les droites d'équations $x = 0$ et $x = a$.

1. Justifier que $f$ est positive sur $[0 \,;\, +\infty[$, et que $\mathcal{A}(a) = \displaystyle\int_0^a xe^{-x}\,\mathrm{d}x$.
2. À l'aide d'une intégration par parties, montrer que $\mathcal{A}(a) = 1 - (a + 1)e^{-a}$.
3. Retrouver ce résultat en vérifiant que $F(x) = -(x + 1)e^{-x}$ est une primitive de $f$.
4. Déterminer $\displaystyle\lim_{a\to+\infty} \mathcal{A}(a)$. Interpréter.
5. Déterminer, à l'aide de la calculatrice, une valeur de $a$ pour laquelle $\mathcal{A}(a) > 0{,}99$.

??? success "Correction"
    **1.** $x \geq 0$ et $e^{-x} > 0$. L'intégrale d'une fonction continue et positive est l'aire sous la courbe.

    **2.** $u = x$, $v' = e^{-x}$, $u' = 1$, $v = -e^{-x}$ :

    $$\mathcal{A}(a) = \big[-xe^{-x}\big]_0^a + \int_0^a e^{-x}\,\mathrm{d}x = -ae^{-a} + \big[-e^{-x}\big]_0^a = -ae^{-a} - e^{-a} + 1 = 1 - (a + 1)e^{-a}.$$

    **3.** $F'(x) = -e^{-x} + (x + 1)e^{-x} = xe^{-x}$. Donc $\mathcal{A}(a) = F(a) - F(0) = -(a + 1)e^{-a} + 1$.

    **4.** $(a + 1)e^{-a} = \frac{a}{e^a} + e^{-a} \to 0$ par croissance comparée. Donc $\mathcal{A}(a) \to 1$ : le domaine sous la courbe, bien qu'il s'étende à l'infini, a une aire finie, égale à $1$ u.a.

    **5.** $\mathcal{A}(6) = 1 - 7e^{-6} \approx 0{,}9827$ et $\mathcal{A}(7) = 1 - 8e^{-7} \approx 0{,}9927 > 0{,}99$. Par exemple, $a = 7$ convient.

---

## Sujet 2 — Une suite d'intégrales

Pour tout entier naturel $n$, on pose $I_n = \displaystyle\int_0^1 \frac{x^n}{1 + x}\,\mathrm{d}x$.

1. Calculer $I_0$.
2. Montrer que pour tout $n$ : $I_n + I_{n+1} = \dfrac{1}{n + 1}$. En déduire $I_1$ et $I_2$.
3. Montrer que la suite $(I_n)$ est décroissante et positive.
4. Montrer que pour tout $n$ : $0 \leq I_n \leq \dfrac{1}{n + 1}$. En déduire la limite de $(I_n)$.
5. En utilisant les questions 2 et 3, montrer que $\dfrac{1}{2(n + 1)} \leq I_n \leq \dfrac{1}{2n}$ pour $n \geq 1$.

??? success "Correction"
    **1.** $I_0 = \big[\ln(1 + x)\big]_0^1 = \ln 2$.

    **2.** Par linéarité : $I_n + I_{n+1} = \displaystyle\int_0^1 \frac{x^n(1 + x)}{1 + x}\,\mathrm{d}x = \int_0^1 x^n\,\mathrm{d}x = \frac{1}{n + 1}$.

    $I_1 = 1 - I_0 = 1 - \ln 2$, puis $I_2 = \frac{1}{2} - I_1 = \ln 2 - \frac{1}{2}$.

    **3.** L'intégrande est positive sur $[0 \,;\, 1]$, donc $I_n \geq 0$. Et $I_{n+1} - I_n = \displaystyle\int_0^1 \frac{x^n(x - 1)}{1 + x}\,\mathrm{d}x \leq 0$, car $x - 1 \leq 0$ sur $[0 \,;\, 1]$.

    **4.** $1 + x \geq 1$ donc $\frac{x^n}{1 + x} \leq x^n$, et $I_n \leq \frac{1}{n + 1}$. Par les gendarmes, $I_n \to 0$.

    **5.** La suite étant décroissante, $I_{n+1} \leq I_n$, donc $\frac{1}{n + 1} = I_n + I_{n+1} \leq 2I_n$, soit $I_n \geq \frac{1}{2(n + 1)}$.

    De même, pour $n \geq 1$, $I_n \leq I_{n-1}$, donc $2I_n \leq I_{n-1} + I_n = \frac{1}{n}$, soit $I_n \leq \frac{1}{2n}$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** $\displaystyle\int_0^1 e^{2x}\,\mathrm{d}x$ vaut :

a) $e^2 - 1$ — b) $\dfrac{e^2 - 1}{2}$ — c) $2e^2 - 2$ — d) $\dfrac{e^2}{2}$

**Question 2.** $\displaystyle\int_{-2}^{2} x^3\,\mathrm{d}x$ vaut :

a) $0$ — b) $4$ — c) $8$ — d) $16$

**Question 3.** La valeur moyenne de $x \mapsto x$ sur $[0 \,;\, 4]$ est :

a) $1$ — b) $2$ — c) $4$ — d) $8$

**Question 4.** $\displaystyle\int_1^e \ln x\,\mathrm{d}x$ vaut :

a) $0$ — b) $1$ — c) $e$ — d) $e - 1$

**Question 5.** Soit $F(x) = \displaystyle\int_0^x e^{-t^2}\,\mathrm{d}t$. Alors :

a) $F'(x) = -2xe^{-x^2}$ — b) $F'(x) = e^{-x^2}$ — c) $F$ est décroissante — d) $F(0) = 1$

??? success "Correction"
    **Question 1 : b).** $\left[\frac{1}{2}e^{2x}\right]_0^1$.

    **Question 2 : a).** $\left[\frac{x^4}{4}\right]_{-2}^2 = 4 - 4 = 0$ (fonction impaire).

    **Question 3 : b).** $\frac{1}{4}\int_0^4 x\,\mathrm{d}x = \frac{1}{4} \times 8 = 2$.

    **Question 4 : b).** Par intégration par parties (cours, méthode 3).

    **Question 5 : b).** $F$ est la primitive de la fonction continue $t \mapsto e^{-t^2}$ qui s'annule en $0$. Elle est croissante (dérivée positive) et $F(0) = 0$.

---

## Sujet 4 — Distance parcourue par un véhicule

Un véhicule démarre à l'instant $t = 0$. Sa vitesse, en m/s, est modélisée pour $t \in [0 \,;\, 10]$ (en secondes) par :

$$v(t) = 20\left(1 - e^{-0{,}5t}\right).$$

On admet que la distance parcourue entre les instants $0$ et $T$ est $d(T) = \displaystyle\int_0^T v(t)\,\mathrm{d}t$.

1. Étudier les variations de $v$ sur $[0 \,;\, 10]$. Quelle vitesse le véhicule approche-t-il ?
2. Déterminer une primitive de $v$ sur $[0 \,;\, 10]$.
3. Calculer la distance parcourue pendant les 10 premières secondes, à 0,1 m près.
4. En déduire la vitesse moyenne du véhicule sur ces 10 secondes, en m/s puis en km/h.
5. On approche $d(10)$ par la méthode des rectangles à gauche avec $n$ rectangles. Expliquer pourquoi on obtient une valeur par défaut, et écrire une fonction Python qui calcule cette approximation.

??? success "Correction"
    **1.** $v'(t) = 20 \times 0{,}5e^{-0{,}5t} = 10e^{-0{,}5t} > 0$ : $v$ est croissante. Quand $t$ augmente, $e^{-0{,}5t}$ tend vers $0$ et la vitesse s'approche de $20$ m/s (72 km/h).

    **2.** $V(t) = 20\left(t + 2e^{-0{,}5t}\right)$, car $\left(2e^{-0{,}5t}\right)' = -e^{-0{,}5t}$.

    **3.** $d(10) = V(10) - V(0) = 20\left(10 + 2e^{-5}\right) - 20 \times 2 = 160 + 40e^{-5} \approx 160{,}3$ m.

    **4.** $\mu = \frac{d(10)}{10} \approx 16{,}03$ m/s, soit environ $57{,}7$ km/h.

    **5.** $v$ est croissante, donc sur chaque petit intervalle, la hauteur du rectangle à gauche est inférieure à la vitesse : la somme est une valeur par défaut.

    ```python
    from math import exp

    def distance(n):
        h = 10 / n
        s = 0
        for k in range(n):
            s = s + 20 * (1 - exp(-0.5 * k * h))
        return h * s
    ```
