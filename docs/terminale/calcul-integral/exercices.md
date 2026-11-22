# Exercices corrigés — Calcul intégral

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Calculs d'intégrales | 1 à 6 |
| 2. Propriétés et encadrements | 7 à 11 |
| 3. Calculs d'aires | 12 à 16 |
| 4. Intégration par parties | 17 à 20 |
| 5. Valeur moyenne et suites d'intégrales | 21 à 25 |
| 6. Approfondissement | 26 à 28 |

---

## Thème 1 — Calculs d'intégrales

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-une-integrale-avec-une-primitive).*

### Exercice 1 — Primitives usuelles <span class="etoiles">★</span>

Calculer :

1. $\displaystyle\int_0^1 (3x^2 - 2x + 1)\,\mathrm{d}x$
2. $\displaystyle\int_1^e \frac{1}{x}\,\mathrm{d}x$
3. $\displaystyle\int_0^{\ln 2} e^x\,\mathrm{d}x$
4. $\displaystyle\int_0^\pi \sin x\,\mathrm{d}x$

??? success "Correction"
    1. $\big[x^3 - x^2 + x\big]_0^1 = 1$.
    2. $\big[\ln x\big]_1^e = 1 - 0 = 1$.
    3. $\big[e^x\big]_0^{\ln 2} = 2 - 1 = 1$.
    4. $\big[-\cos x\big]_0^\pi = 1 - (-1) = 2$.

### Exercice 2 — Formes composées <span class="etoiles">★</span>

Calculer :

1. $\displaystyle\int_0^1 e^{2x}\,\mathrm{d}x$
2. $\displaystyle\int_0^1 xe^{x^2}\,\mathrm{d}x$
3. $\displaystyle\int_0^1 \frac{2x}{x^2 + 1}\,\mathrm{d}x$

??? success "Correction"
    1. $\left[\frac{1}{2}e^{2x}\right]_0^1 = \dfrac{e^2 - 1}{2}$.
    2. $\left[\frac{1}{2}e^{x^2}\right]_0^1 = \dfrac{e - 1}{2}$.
    3. $\big[\ln(x^2 + 1)\big]_0^1 = \ln 2$.

### Exercice 3 — Formes $u'u^n$ et $\frac{u'}{\sqrt{u}}$ <span class="etoiles">★★</span>

Calculer :

1. $\displaystyle\int_0^1 (2x + 1)(x^2 + x)^2\,\mathrm{d}x$
2. $\displaystyle\int_0^{\pi/2} \cos x\,\sin^2 x\,\mathrm{d}x$
3. $\displaystyle\int_0^2 \frac{x}{\sqrt{x^2 + 5}}\,\mathrm{d}x$

??? success "Correction"
    1. $\left[\dfrac{(x^2 + x)^3}{3}\right]_0^1 = \dfrac{8}{3}$.
    2. $\left[\dfrac{\sin^3 x}{3}\right]_0^{\pi/2} = \dfrac{1}{3}$.
    3. $\Big[\sqrt{x^2 + 5}\Big]_0^2 = 3 - \sqrt{5}$.

### Exercice 4 — Parité <span class="etoiles">★★</span>

1. Calculer $\displaystyle\int_{-1}^1 x^3\,\mathrm{d}x$. Interpréter graphiquement.
2. Calculer $\displaystyle\int_{-1}^1 |x|\,\mathrm{d}x$ à l'aide de la relation de Chasles.

??? success "Correction"
    **1.** $\left[\frac{x^4}{4}\right]_{-1}^1 = \frac{1}{4} - \frac{1}{4} = 0$. La fonction cube est impaire : l'aire au-dessus de l'axe sur $[0 \,;\, 1]$ compense exactement l'aire en dessous sur $[-1 \,;\, 0]$.

    **2.** $\int_{-1}^1 |x|\,\mathrm{d}x = \int_{-1}^0 (-x)\,\mathrm{d}x + \int_0^1 x\,\mathrm{d}x = \frac{1}{2} + \frac{1}{2} = 1$.

### Exercice 5 — Valeur absolue <span class="etoiles">★★</span>

Calculer $\displaystyle\int_0^2 |x - 1|\,\mathrm{d}x$.

??? success "Correction"
    $|x - 1| = 1 - x$ sur $[0 \,;\, 1]$ et $x - 1$ sur $[1 \,;\, 2]$. Par Chasles :

    $$\int_0^1 (1 - x)\,\mathrm{d}x + \int_1^2 (x - 1)\,\mathrm{d}x = \frac{1}{2} + \frac{1}{2} = 1.$$

    *Ce sont deux triangles d'aire $\frac{1}{2}$.*

### Exercice 6 — Somme de fonctions <span class="etoiles">★★</span>

Calculer $\displaystyle\int_1^2 \left(\frac{1}{x} + \frac{1}{x^2}\right)\mathrm{d}x$.

??? success "Correction"
    $\left[\ln x - \frac{1}{x}\right]_1^2 = \left(\ln 2 - \frac{1}{2}\right) - (0 - 1) = \ln 2 + \frac{1}{2}$.

---

## Thème 2 — Propriétés et encadrements

*Méthode associée : [Méthode 4](methodes.md#methode-4-encadrer-une-integrale-sans-la-calculer).*

### Exercice 7 — Linéarité <span class="etoiles">★</span>

On sait que $\displaystyle\int_0^1 f(x)\,\mathrm{d}x = 3$ et $\displaystyle\int_0^1 g(x)\,\mathrm{d}x = -1$. Calculer $\displaystyle\int_0^1 \big(2f(x) - 3g(x)\big)\,\mathrm{d}x$ et $\displaystyle\int_1^0 f(x)\,\mathrm{d}x$.

??? success "Correction"
    Par linéarité : $2 \times 3 - 3 \times (-1) = 9$. Et $\int_1^0 f = -\int_0^1 f = -3$.

### Exercice 8 — Fonction définie par morceaux <span class="etoiles">★★</span>

Soit $f$ définie sur $[0 \,;\, 3]$ par $f(x) = x$ si $x \leq 1$ et $f(x) = 1$ si $x > 1$. Justifier que $f$ est continue, puis calculer $\displaystyle\int_0^3 f(x)\,\mathrm{d}x$.

??? success "Correction"
    En $1$, les limites à gauche et à droite valent $1 = f(1)$ : $f$ est continue. Par Chasles :

    $$\int_0^3 f = \int_0^1 x\,\mathrm{d}x + \int_1^3 1\,\mathrm{d}x = \frac{1}{2} + 2 = \frac{5}{2}.$$

### Exercice 9 — Signe et comparaison sans calcul <span class="etoiles">★★</span>

Sans calculer d'intégrale :

1. Déterminer le signe de $\displaystyle\int_1^2 \ln x\,\mathrm{d}x$ et de $\displaystyle\int_0^1 (x^2 - x)\,\mathrm{d}x$.
2. Comparer $\displaystyle\int_0^1 x^2\,\mathrm{d}x$ et $\displaystyle\int_0^1 x^3\,\mathrm{d}x$.

??? success "Correction"
    **1.** Sur $[1 \,;\, 2]$, $\ln x \geq 0$, et $1 \leq 2$ : la première intégrale est positive. Sur $[0 \,;\, 1]$, $x^2 - x = x(x - 1) \leq 0$ : la seconde est négative.

    **2.** Sur $[0 \,;\, 1]$, $x^3 = x \times x^2 \leq x^2$ (car $0 \leq x \leq 1$). Par la propriété d'ordre, $\int_0^1 x^3 \leq \int_0^1 x^2$. *(Les valeurs sont $\frac{1}{4}$ et $\frac{1}{3}$.)*

### Exercice 10 — Encadrement simple <span class="etoiles">★★</span>

Montrer que $\dfrac{1}{2} \leq \displaystyle\int_0^1 \frac{\mathrm{d}x}{1 + x^2} \leq 1$.

??? success "Correction"
    Pour $x \in [0 \,;\, 1]$, $1 \leq 1 + x^2 \leq 2$, donc $\frac{1}{2} \leq \frac{1}{1 + x^2} \leq 1$. On intègre sur $[0 \,;\, 1]$, de longueur $1$ (inégalité de la moyenne).

    *Dans le supérieur, on montre que cette intégrale vaut $\frac{\pi}{4} \approx 0{,}785$.*

### Exercice 11 — Encadrer l'intégrale de la gaussienne <span class="etoiles">★★★</span>

On pose $I = \displaystyle\int_0^1 e^{-x^2}\,\mathrm{d}x$. On ne connaît pas de primitive de $x \mapsto e^{-x^2}$.

1. Montrer que pour tout $u \geq 0$ : $1 - u \leq e^{-u} \leq 1 - u + \dfrac{u^2}{2}$.
2. En déduire que $\dfrac{2}{3} \leq I \leq \dfrac{23}{30}$.

??? success "Correction"
    **1.** La minoration est $e^X \geq 1 + X$ avec $X = -u$. Pour la majoration, soit $g(u) = 1 - u + \frac{u^2}{2} - e^{-u}$ : $g'(u) = -1 + u + e^{-u} \geq 0$ (encore $e^{-u} \geq 1 - u$), et $g(0) = 0$. Donc $g(u) \geq 0$ pour $u \geq 0$.

    **2.** Avec $u = x^2$ : $1 - x^2 \leq e^{-x^2} \leq 1 - x^2 + \frac{x^4}{2}$ sur $[0 \,;\, 1]$. On intègre :

    $$\int_0^1 (1 - x^2)\,\mathrm{d}x = 1 - \frac{1}{3} = \frac{2}{3}, \qquad \int_0^1 \left(1 - x^2 + \frac{x^4}{2}\right)\mathrm{d}x = 1 - \frac{1}{3} + \frac{1}{10} = \frac{23}{30}.$$

    *La valeur exacte est $I \approx 0{,}7468$, et $\frac{23}{30} \approx 0{,}7667$.*

---

## Thème 3 — Calculs d'aires

*Méthode associée : [Méthode 2](methodes.md#methode-2-calculer-une-aire).*

### Exercice 12 — Sous une parabole <span class="etoiles">★</span>

Calculer l'aire du domaine compris entre la parabole $y = x^2$, l'axe des abscisses et les droites $x = 0$ et $x = 2$.

??? success "Correction"
    $x^2 \geq 0$, donc $\mathcal{A} = \displaystyle\int_0^2 x^2\,\mathrm{d}x = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}$ u.a.

### Exercice 13 — Entre une droite et une parabole <span class="etoiles">★★</span>

Calculer l'aire du domaine compris entre la droite $y = x$ et la parabole $y = x^2$.

??? success "Correction"
    Les courbes se coupent quand $x = x^2$, soit en $0$ et $1$. Sur $[0 \,;\, 1]$, $x - x^2 \geq 0$ :

    $$\mathcal{A} = \int_0^1 (x - x^2)\,\mathrm{d}x = \frac{1}{2} - \frac{1}{3} = \frac{1}{6} \text{ u.a.}$$

### Exercice 14 — Exponentielle et tangente <span class="etoiles">★★</span>

Calculer l'aire du domaine compris entre la courbe de l'exponentielle, sa tangente en $0$ (d'équation $y = x + 1$), et les droites $x = 0$ et $x = 1$.

??? success "Correction"
    On sait que $e^x \geq x + 1$ (convexité). Donc

    $$\mathcal{A} = \int_0^1 (e^x - x - 1)\,\mathrm{d}x = \left[e^x - \frac{x^2}{2} - x\right]_0^1 = \left(e - \frac{3}{2}\right) - 1 = e - \frac{5}{2} \approx 0{,}218 \text{ u.a.}$$

### Exercice 15 — Une fonction négative <span class="etoiles">★★</span>

Calculer l'aire du domaine compris entre la courbe de $f(x) = x^2 - 4$ et l'axe des abscisses.

??? success "Correction"
    $f$ s'annule en $\pm 2$ et est négative entre. L'aire vaut

    $$\mathcal{A} = -\int_{-2}^2 (x^2 - 4)\,\mathrm{d}x = -\left[\frac{x^3}{3} - 4x\right]_{-2}^2 = -\left(\left(\frac{8}{3} - 8\right) - \left(-\frac{8}{3} + 8\right)\right) = \frac{32}{3} \text{ u.a.}$$

### Exercice 16 — Entre sinus et cosinus <span class="etoiles">★★★</span>

Calculer l'aire du domaine compris entre les courbes de $\sin$ et de $\cos$ sur $\left[\frac{\pi}{4} \,;\, \frac{5\pi}{4}\right]$.

??? success "Correction"
    Les courbes se coupent en $\frac{\pi}{4}$ et $\frac{5\pi}{4}$, et le sinus est au-dessus entre ces valeurs (par exemple en $\frac{\pi}{2}$, $\sin = 1 > 0 = \cos$). Donc

    $$\mathcal{A} = \int_{\pi/4}^{5\pi/4} (\sin x - \cos x)\,\mathrm{d}x = \big[-\cos x - \sin x\big]_{\pi/4}^{5\pi/4} = \left(\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}\right) - \left(-\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\right) = 2\sqrt{2} \text{ u.a.}$$

---

## Thème 4 — Intégration par parties

*Méthode associée : [Méthode 3](methodes.md#methode-3-integrer-par-parties).*

### Exercice 17 — $\int x e^x$ <span class="etoiles">★★</span>

Calculer $\displaystyle\int_0^1 xe^x\,\mathrm{d}x$ par une intégration par parties.

??? success "Correction"
    $u = x$, $v' = e^x$, $u' = 1$, $v = e^x$ : $\big[xe^x\big]_0^1 - \int_0^1 e^x\,\mathrm{d}x = e - (e - 1) = 1$.

### Exercice 18 — $\int \ln x$ <span class="etoiles">★★</span>

Calculer $\displaystyle\int_1^e \ln x\,\mathrm{d}x$, puis l'aire sous la courbe de $\ln$ entre $1$ et $e$.

??? success "Correction"
    $u = \ln x$, $v' = 1$, $u' = \frac{1}{x}$, $v = x$ : $\big[x\ln x\big]_1^e - \int_1^e 1\,\mathrm{d}x = e - (e - 1) = 1$. Comme $\ln \geq 0$ sur $[1 \,;\, e]$, l'aire vaut $1$ u.a.

### Exercice 19 — $\int x\sin x$ <span class="etoiles">★★</span>

Calculer $\displaystyle\int_0^\pi x\sin x\,\mathrm{d}x$.

??? success "Correction"
    $u = x$, $v' = \sin x$, $u' = 1$, $v = -\cos x$ :

    $$\big[-x\cos x\big]_0^\pi + \int_0^\pi \cos x\,\mathrm{d}x = \pi + \big[\sin x\big]_0^\pi = \pi.$$

### Exercice 20 — Deux intégrations par parties <span class="etoiles">★★★</span>

Calculer $\displaystyle\int_0^1 x^2e^x\,\mathrm{d}x$.

??? success "Correction"
    $u = x^2$, $v' = e^x$, $u' = 2x$, $v = e^x$ :

    $$\int_0^1 x^2e^x\,\mathrm{d}x = \big[x^2e^x\big]_0^1 - 2\int_0^1 xe^x\,\mathrm{d}x = e - 2 \times 1 = e - 2,$$

    en utilisant l'exercice 17.

---

## Thème 5 — Valeur moyenne et suites d'intégrales

*Méthodes associées : [Méthode 5](methodes.md#methode-5-etudier-une-suite-dintegrales) et [Méthode 6](methodes.md#methode-6-valeur-moyenne-et-methode-des-rectangles).*

### Exercice 21 — Une valeur moyenne <span class="etoiles">★</span>

Calculer la valeur moyenne de $x \mapsto x^2$ sur $[0 \,;\, 3]$.

??? success "Correction"
    $\mu = \dfrac{1}{3}\displaystyle\int_0^3 x^2\,\mathrm{d}x = \dfrac{1}{3} \times 9 = 3$.

### Exercice 22 — Moyenne du sinus <span class="etoiles">★★</span>

Calculer la valeur moyenne de $\sin$ sur $[0 \,;\, \pi]$, puis sur $[0 \,;\, 2\pi]$. Interpréter.

??? success "Correction"
    Sur $[0 \,;\, \pi]$ : $\frac{1}{\pi} \times 2 = \frac{2}{\pi} \approx 0{,}64$. Sur $[0 \,;\, 2\pi]$ : $\frac{1}{2\pi} \times 0 = 0$, car les deux arches se compensent.

    *En électricité, c'est pour cela qu'on utilise la valeur « efficace » plutôt que la valeur moyenne d'une tension alternative, qui est nulle.*

### Exercice 23 — Température moyenne <span class="etoiles">★★</span>

La température d'une boisson est $T(t) = 20 + 70e^{-0{,}1t}$ (en °C, $t$ en minutes). Calculer sa température moyenne pendant les 10 premières minutes.

??? success "Correction"
    $$\mu = \frac{1}{10}\int_0^{10} \left(20 + 70e^{-0{,}1t}\right)\mathrm{d}t = \frac{1}{10}\Big[20t - 700e^{-0{,}1t}\Big]_0^{10} = \frac{1}{10}\left(200 - 700e^{-1} + 700\right) = 90 - 70e^{-1} \approx 64{,}2 \text{ °C}.$$

### Exercice 24 — Une suite d'intégrales <span class="etoiles">★★★</span>

Pour $n \in \mathbb{N}$, on pose $I_n = \displaystyle\int_0^1 x^n e^{-x}\,\mathrm{d}x$.

1. Calculer $I_0$.
2. Montrer que $(I_n)$ est positive et décroissante.
3. Montrer que $0 \leq I_n \leq \dfrac{1}{n + 1}$ et en déduire la limite de $(I_n)$.
4. Montrer, par une intégration par parties, que $I_{n+1} = (n + 1)I_n - \dfrac{1}{e}$. En déduire $I_1$.

??? success "Correction"
    **1.** $I_0 = \big[-e^{-x}\big]_0^1 = 1 - \frac{1}{e}$.

    **2.** Sur $[0 \,;\, 1]$, $x^ne^{-x} \geq 0$, donc $I_n \geq 0$. Et $I_{n+1} - I_n = \int_0^1 x^n(x - 1)e^{-x}\,\mathrm{d}x \leq 0$, car $x - 1 \leq 0$.

    **3.** $e^{-x} \leq 1$ sur $[0 \,;\, 1]$, donc $x^ne^{-x} \leq x^n$, et $I_n \leq \int_0^1 x^n\,\mathrm{d}x = \frac{1}{n + 1}$. Par les gendarmes, $I_n \to 0$.

    **4.** $u = x^{n+1}$, $v' = e^{-x}$, $u' = (n + 1)x^n$, $v = -e^{-x}$ :

    $$I_{n+1} = \big[-x^{n+1}e^{-x}\big]_0^1 + (n + 1)\int_0^1 x^ne^{-x}\,\mathrm{d}x = -\frac{1}{e} + (n + 1)I_n.$$

    $I_1 = I_0 - \frac{1}{e} = 1 - \frac{2}{e}$.

### Exercice 25 — Une limite d'intégrales <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $J_n = \displaystyle\int_0^1 \frac{\mathrm{d}x}{1 + x^n}$. Montrer que $0 \leq 1 - J_n \leq \dfrac{1}{n + 1}$ et en déduire la limite de $(J_n)$.

??? success "Correction"
    $1 - J_n = \int_0^1 \left(1 - \frac{1}{1 + x^n}\right)\mathrm{d}x = \int_0^1 \frac{x^n}{1 + x^n}\,\mathrm{d}x$. Sur $[0 \,;\, 1]$ : $0 \leq \frac{x^n}{1 + x^n} \leq x^n$, donc $0 \leq 1 - J_n \leq \frac{1}{n + 1}$. Par les gendarmes, $1 - J_n \to 0$, donc $J_n \to 1$.

---

## Thème 6 — Approfondissement

### Exercice 26 — Méthode des rectangles <span class="etoiles">★★</span>

On approche $I = \displaystyle\int_0^1 x^2\,\mathrm{d}x$ par la méthode des rectangles avec $n = 4$.

1. Calculer la somme $s_4$ des rectangles à gauche et la somme $S_4$ des rectangles à droite. Comparer avec $I$.
2. Combien faut-il de rectangles pour que $S_n - s_n \leq 10^{-3}$ ?
3. Écrire une fonction Python qui renvoie $s_n$ et $S_n$.

??? success "Correction"
    **1.** $h = \frac{1}{4}$. $s_4 = \frac{1}{4}\left(0 + \frac{1}{16} + \frac{4}{16} + \frac{9}{16}\right) = \frac{14}{64} \approx 0{,}219$ et $S_4 = \frac{1}{4}\left(\frac{1}{16} + \frac{4}{16} + \frac{9}{16} + 1\right) = \frac{30}{64} \approx 0{,}469$. On a bien $s_4 \leq \frac{1}{3} \leq S_4$, car $x \mapsto x^2$ est croissante sur $[0 \,;\, 1]$.

    **2.** $S_n - s_n = \frac{(1 - 0)(1 - 0)}{n} = \frac{1}{n} \leq 10^{-3} \iff n \geq 1000$.

    **3.**

    ```python
    def sommes(n):
        h = 1 / n
        s = sum((k * h)**2 for k in range(n))         # à gauche
        S = sum((k * h)**2 for k in range(1, n + 1))  # à droite
        return h * s, h * S
    ```

### Exercice 27 — Le logarithme comme intégrale <span class="etoiles">★★★</span>

Pour $x > 0$, on pose $L(x) = \displaystyle\int_1^x \frac{\mathrm{d}t}{t}$.

1. Justifier que $L$ est dérivable sur $]0 \,;\, +\infty[$ et calculer $L'$. En déduire que $L = \ln$.
2. En encadrant $\frac{1}{t}$ sur $[1 \,;\, 2]$, montrer que $\frac{1}{2} \leq \ln 2 \leq 1$.
3. Interpréter $\ln 2$ comme une aire.

??? success "Correction"
    **1.** $t \mapsto \frac{1}{t}$ est continue sur $]0 \,;\, +\infty[$, et $L$ est la primitive de cette fonction qui s'annule en $1$ (cours, § 2). Donc $L'(x) = \frac{1}{x}$. Comme $\ln$ est aussi une primitive de $\frac{1}{x}$ qui s'annule en $1$, on a $L = \ln$.

    **2.** Pour $t \in [1 \,;\, 2]$, $\frac{1}{2} \leq \frac{1}{t} \leq 1$. En intégrant sur un intervalle de longueur $1$ : $\frac{1}{2} \leq \ln 2 \leq 1$.

    **3.** $\ln 2$ est l'aire sous l'hyperbole $y = \frac{1}{t}$ entre $t = 1$ et $t = 2$.

### Exercice 28 — La série harmonique <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $H_n = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}$.

1. Montrer que pour tout entier $k \geq 1$ : $\displaystyle\int_k^{k+1} \frac{\mathrm{d}t}{t} \leq \frac{1}{k}$.
2. En déduire que $H_n \geq \ln(n + 1)$, puis la limite de $(H_n)$.
3. Montrer de même que $H_n \leq 1 + \ln n$.

??? success "Correction"
    **1.** Sur $[k \,;\, k + 1]$, $\frac{1}{t} \leq \frac{1}{k}$. On intègre sur un intervalle de longueur $1$.

    **2.** On additionne pour $k$ de $1$ à $n$, avec la relation de Chasles :

    $$H_n \geq \int_1^{n+1} \frac{\mathrm{d}t}{t} = \ln(n + 1).$$

    Comme $\ln(n + 1) \to +\infty$, par comparaison $H_n \to +\infty$.

    **3.** Pour $k \geq 2$, sur $[k - 1 \,;\, k]$, $\frac{1}{t} \geq \frac{1}{k}$, donc $\frac{1}{k} \leq \int_{k-1}^k \frac{\mathrm{d}t}{t}$. En additionnant pour $k$ de $2$ à $n$ : $H_n - 1 \leq \int_1^n \frac{\mathrm{d}t}{t} = \ln n$.

    *Ainsi $\ln(n + 1) \leq H_n \leq 1 + \ln n$ : la somme des inverses tend vers $+\infty$, mais très lentement. Il faut environ $1{,}5 \times 10^{43}$ termes pour qu'elle dépasse $100$ !*
