# Exercices corrigés — Fonction logarithme népérien

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Propriétés algébriques | 1 à 5 |
| 2. Équations et inéquations | 6 à 11 |
| 3. Dérivées et études de fonctions | 12 à 17 |
| 4. Limites et croissances comparées | 18 à 22 |
| 5. Suites et modélisation | 23 à 26 |
| 6. Approfondissement | 27 et 28 |

---

## Thème 1 — Propriétés algébriques

*Méthode associée : [Méthode 1](methodes.md#methode-1-simplifier-une-expression).*

### Exercice 1 — Calculs simples <span class="etoiles">★</span>

Simplifier :

1. $A = \ln 8 - \ln 2$
2. $B = \ln(e^3) - \ln\left(\dfrac{1}{e}\right)$
3. $C = e^{2\ln 3}$
4. $D = \ln\sqrt{e}$

??? success "Correction"
    1. $A = \ln\frac{8}{2} = \ln 4 = 2\ln 2$.
    2. $B = 3 - (-1) = 4$.
    3. $C = \left(e^{\ln 3}\right)^2 = 3^2 = 9$.
    4. $D = \frac{1}{2}\ln e = \frac{1}{2}$.

### Exercice 2 — En fonction de $\ln 2$ et $\ln 3$ <span class="etoiles">★</span>

Exprimer en fonction de $\ln 2$ et $\ln 3$ :

1. $\ln 6$
2. $\ln 12$
3. $\ln\dfrac{9}{8}$
4. $\ln\sqrt{18}$

??? success "Correction"
    1. $\ln 6 = \ln(2 \times 3) = \ln 2 + \ln 3$.
    2. $\ln 12 = \ln(2^2 \times 3) = 2\ln 2 + \ln 3$.
    3. $\ln\frac{9}{8} = \ln(3^2) - \ln(2^3) = 2\ln 3 - 3\ln 2$.
    4. $\ln\sqrt{18} = \frac{1}{2}\ln(2 \times 3^2) = \frac{1}{2}\ln 2 + \ln 3$.

### Exercice 3 — Attention au domaine <span class="etoiles">★★</span>

1. Pour $x > 0$, simplifier $\ln(x^2) - 2\ln x$.
2. L'égalité $\ln(x^2) = 2\ln x$ est-elle vraie pour $x = -3$ ? Quelle est la formule correcte pour tout $x \neq 0$ ?

??? success "Correction"
    **1.** Pour $x > 0$, $\ln(x^2) = 2\ln x$, donc l'expression vaut $0$.

    **2.** Pour $x = -3$, $\ln(x^2) = \ln 9$ existe, mais $\ln(-3)$ n'existe pas : l'égalité n'a pas de sens. Pour tout $x \neq 0$, $x^2 = |x|^2$ avec $|x| > 0$, donc $\ln(x^2) = 2\ln|x|$.

### Exercice 4 — Une identité utile <span class="etoiles">★★</span>

Montrer que pour tout réel $x$ : $\ln(1 + e^x) - x = \ln(1 + e^{-x})$.

??? success "Correction"
    $x = \ln(e^x)$, donc

    $$\ln(1 + e^x) - x = \ln(1 + e^x) - \ln(e^x) = \ln\frac{1 + e^x}{e^x} = \ln\left(e^{-x} + 1\right).$$

### Exercice 5 — Démontrer $\ln(a^n) = n\ln a$ <span class="etoiles">★★★</span>

Soit $a > 0$.

1. Démontrer par récurrence que pour tout entier $n \geq 0$ : $\ln(a^n) = n\ln a$.
2. En déduire la formule pour les entiers $n < 0$.

??? success "Correction"
    **1.** Initialisation : $\ln(a^0) = \ln 1 = 0 = 0 \times \ln a$. Hérédité : si $\ln(a^n) = n\ln a$, alors $\ln(a^{n+1}) = \ln(a^n \times a) = \ln(a^n) + \ln a = n\ln a + \ln a = (n + 1)\ln a$.

    **2.** Si $n < 0$, on pose $m = -n > 0$. Alors $a^n = \dfrac{1}{a^m}$, donc $\ln(a^n) = -\ln(a^m) = -m\ln a = n\ln a$.

---

## Thème 2 — Équations et inéquations

*Méthodes associées : [Méthode 2](methodes.md#methode-2-resoudre-une-equation-ou-une-inequation) et [Méthode 3](methodes.md#methode-3-poser-un-changement-de-variable).*

### Exercice 6 — Équations simples <span class="etoiles">★</span>

Résoudre dans $\mathbb{R}$ :

1. $\ln x = 2$
2. $e^x = 5$
3. $\ln(2x - 1) = 0$
4. $e^{3x - 1} = 7$

??? success "Correction"
    1. Sur $]0 \,;\, +\infty[$ : $x = e^2$.
    2. $x = \ln 5$.
    3. Il faut $2x - 1 > 0$, soit $x > \frac{1}{2}$. Alors $2x - 1 = e^0 = 1$, donc $x = 1$, qui convient.
    4. $3x - 1 = \ln 7$, donc $x = \dfrac{1 + \ln 7}{3}$.

### Exercice 7 — Inéquations simples <span class="etoiles">★</span>

Résoudre :

1. $\ln x < 1$
2. $e^x > 2$
3. $\ln(x - 3) \geq 0$
4. $e^{-2x} \leq 4$

??? success "Correction"
    1. Sur $]0 \,;\, +\infty[$ : $\ln x < \ln e \iff x < e$. $\mathcal{S} = \,]0 \,;\, e[$.
    2. $x > \ln 2$. $\mathcal{S} = \,]\ln 2 \,;\, +\infty[$.
    3. Il faut $x > 3$. $\ln(x - 3) \geq \ln 1 \iff x - 3 \geq 1 \iff x \geq 4$. $\mathcal{S} = [4 \,;\, +\infty[$.
    4. $-2x \leq \ln 4 \iff x \geq -\dfrac{\ln 4}{2} = -\ln 2$. $\mathcal{S} = [-\ln 2 \,;\, +\infty[$.

### Exercice 8 — Regrouper les logarithmes <span class="etoiles">★★</span>

Résoudre $\ln x + \ln(x - 1) = \ln 6$.

??? success "Correction"
    Ensemble de résolution : $x > 0$ et $x > 1$, donc $]1 \,;\, +\infty[$.

    $\ln\big(x(x - 1)\big) = \ln 6 \iff x^2 - x - 6 = 0 \iff (x - 3)(x + 2) = 0$. Seul $x = 3$ est dans $]1 \,;\, +\infty[$ : $\mathcal{S} = \{3\}$.

### Exercice 9 — Changement de variable avec l'exponentielle <span class="etoiles">★★</span>

Résoudre dans $\mathbb{R}$ : $e^{2x} - 3e^x + 2 = 0$, puis $e^{2x} - 3e^x + 2 > 0$.

??? success "Correction"
    On pose $X = e^x > 0$ : $X^2 - 3X + 2 = (X - 1)(X - 2)$.

    **Équation** : $X = 1$ ou $X = 2$, donc $x = 0$ ou $x = \ln 2$.

    **Inéquation** : $(X - 1)(X - 2) > 0 \iff X < 1$ ou $X > 2$, soit $e^x < 1$ ou $e^x > 2$, c'est-à-dire $x < 0$ ou $x > \ln 2$. $\mathcal{S} = \,]-\infty \,;\, 0[ \,\cup\, ]\ln 2 \,;\, +\infty[$.

### Exercice 10 — Inéquation avec deux logarithmes <span class="etoiles">★★</span>

Résoudre sur $]0 \,;\, +\infty[$ : $\ln(x + 1) - \ln x \leq \ln 2$.

??? success "Correction"
    $\ln\dfrac{x + 1}{x} \leq \ln 2 \iff \dfrac{x + 1}{x} \leq 2 \iff x + 1 \leq 2x$ (car $x > 0$) $\iff x \geq 1$. $\mathcal{S} = [1 \,;\, +\infty[$.

### Exercice 11 — Changement de variable avec le logarithme <span class="etoiles">★★</span>

Résoudre $(\ln x)^2 - \ln x - 2 = 0$.

??? success "Correction"
    Sur $]0 \,;\, +\infty[$, on pose $X = \ln x$ : $X^2 - X - 2 = (X - 2)(X + 1) = 0$, donc $X = 2$ ou $X = -1$. D'où $x = e^2$ ou $x = e^{-1}$.

---

## Thème 3 — Dérivées et études de fonctions

*Méthode associée : [Méthode 4](methodes.md#methode-4-etudier-une-fonction-contenant-ln).*

### Exercice 12 — Calculs de dérivées <span class="etoiles">★</span>

Calculer la dérivée de chaque fonction sur son ensemble de définition.

1. $f(x) = x\ln x - x$
2. $g(x) = \ln(x^2 + 1)$
3. $h(x) = \dfrac{\ln x}{x}$
4. $k(x) = (\ln x)^2$

??? success "Correction"
    1. $f'(x) = \ln x + x \times \frac{1}{x} - 1 = \ln x$.
    2. $g'(x) = \dfrac{2x}{x^2 + 1}$.
    3. $h'(x) = \dfrac{\frac{1}{x} \times x - \ln x}{x^2} = \dfrac{1 - \ln x}{x^2}$.
    4. $k'(x) = 2 \times \frac{1}{x} \times \ln x = \dfrac{2\ln x}{x}$.

### Exercice 13 — La fonction $x\ln x$ <span class="etoiles">★★</span>

Soit $f(x) = x\ln x$ sur $]0 \,;\, +\infty[$. Étudier ses variations et ses limites, puis dresser son tableau de variations.

??? success "Correction"
    $f'(x) = \ln x + 1$. $f'(x) \geq 0 \iff \ln x \geq -1 \iff x \geq e^{-1}$. Minimum : $f(e^{-1}) = e^{-1} \times (-1) = -\frac{1}{e}$.

    Limites : en $0^+$, $x\ln x \to 0$ (croissance comparée) ; en $+\infty$, $f \to +\infty$ (produit).

    | $x$ | $0$ | | $\frac{1}{e}$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | |
    | $f(x)$ | $0$ | $\searrow$ | $-\frac{1}{e}$ | $\nearrow$ | $+\infty$ |

### Exercice 14 — La fonction $\frac{\ln x}{x}$ <span class="etoiles">★★</span>

Soit $f(x) = \dfrac{\ln x}{x}$ sur $]0 \,;\, +\infty[$.

1. Déterminer les limites de $f$ en $0^+$ et en $+\infty$.
2. Étudier les variations de $f$ et dresser son tableau.

??? success "Correction"
    **1.** En $0^+$ : $\ln x \to -\infty$ et $\frac{1}{x} \to +\infty$, donc $f \to -\infty$. En $+\infty$ : $f \to 0$ (croissance comparée).

    **2.** $f'(x) = \dfrac{1 - \ln x}{x^2}$, du signe de $1 - \ln x$, positif pour $x < e$. Maximum $f(e) = \frac{1}{e}$.

    | $x$ | $0$ | | $e$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $-\infty$ | $\nearrow$ | $\frac{1}{e}$ | $\searrow$ | $0$ |

### Exercice 15 — L'inégalité $\ln x \leq x - 1$ <span class="etoiles">★★</span>

Soit $f(x) = x - 1 - \ln x$ sur $]0 \,;\, +\infty[$. Étudier les variations de $f$ et en déduire que $\ln x \leq x - 1$ pour tout $x > 0$.

??? success "Correction"
    $f'(x) = 1 - \frac{1}{x} = \frac{x - 1}{x}$, du signe de $x - 1$. $f$ est décroissante sur $]0 \,;\, 1]$, croissante sur $[1 \,;\, +\infty[$, de minimum $f(1) = 0$. Donc $f(x) \geq 0$, c'est-à-dire $\ln x \leq x - 1$.

    *C'est l'inégalité de concavité du cours, retrouvée par une étude de fonction.*

### Exercice 16 — Logarithme d'un trinôme <span class="etoiles">★★</span>

Soit $f(x) = \ln(x^2 - 4x + 5)$.

1. Montrer que $f$ est définie sur $\mathbb{R}$.
2. Étudier les variations de $f$ et ses limites en $\pm\infty$.

??? success "Correction"
    **1.** Le discriminant de $x^2 - 4x + 5$ vaut $16 - 20 = -4 < 0$ : ce trinôme est toujours strictement positif. $f$ est définie sur $\mathbb{R}$.

    **2.** $f'(x) = \dfrac{2x - 4}{x^2 - 4x + 5}$, du signe de $2x - 4$. $f$ est décroissante sur $]-\infty \,;\, 2]$ et croissante sur $[2 \,;\, +\infty[$, de minimum $f(2) = \ln 1 = 0$. En $\pm\infty$, le trinôme tend vers $+\infty$, donc $f \to +\infty$ (composition).

### Exercice 17 — Concavité et moyennes <span class="etoiles">★★★</span>

1. Justifier que $\ln$ est concave sur $]0 \,;\, +\infty[$.
2. En déduire que pour tous $a > 0$ et $b > 0$ : $\ln\left(\dfrac{a + b}{2}\right) \geq \dfrac{\ln a + \ln b}{2}$.
3. En déduire que $\sqrt{ab} \leq \dfrac{a + b}{2}$.

??? success "Correction"
    **1.** $\ln''(x) = -\frac{1}{x^2} < 0$.

    **2.** Pour une fonction concave, l'inégalité du milieu est inversée (on l'applique à $-\ln$, qui est convexe) : $\ln\left(\frac{a + b}{2}\right) \geq \frac{\ln a + \ln b}{2}$.

    **3.** $\frac{\ln a + \ln b}{2} = \frac{1}{2}\ln(ab) = \ln\sqrt{ab}$. L'inégalité devient $\ln\left(\frac{a + b}{2}\right) \geq \ln\sqrt{ab}$, et comme $\ln$ est strictement croissante : $\frac{a + b}{2} \geq \sqrt{ab}$.

---

## Thème 4 — Limites et croissances comparées

*Méthode associée : [Méthode 5](methodes.md#methode-5-lever-une-forme-indeterminee-avec-ln).*

### Exercice 18 — Formes indéterminées <span class="etoiles">★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} (\ln x - x)$
2. $\displaystyle\lim_{x\to 0^+} \left(\ln x + \frac{1}{x}\right)$
3. $\displaystyle\lim_{x\to+\infty} \frac{\ln x}{\sqrt{x}}$

??? success "Correction"
    1. $\ln x - x = x\left(\frac{\ln x}{x} - 1\right)$. La parenthèse tend vers $-1$ : la limite est $-\infty$.
    2. $\ln x + \frac{1}{x} = \frac{1}{x}\left(x\ln x + 1\right)$. La parenthèse tend vers $1$ et $\frac{1}{x} \to +\infty$ : la limite est $+\infty$.
    3. On pose $X = \sqrt{x} \to +\infty$ : $\dfrac{\ln x}{\sqrt{x}} = \dfrac{\ln(X^2)}{X} = 2\dfrac{\ln X}{X} \to 0$.

### Exercice 19 — Taux d'accroissement <span class="etoiles">★★</span>

Déterminer $\displaystyle\lim_{x\to 0} \frac{\ln(1 + 2x)}{x}$ et $\displaystyle\lim_{x\to+\infty} x\ln\left(1 + \frac{1}{x}\right)$.

??? success "Correction"
    **1.** Avec $X = 2x \to 0$ : $\dfrac{\ln(1 + 2x)}{x} = 2 \times \dfrac{\ln(1 + X)}{X} \to 2$.

    **2.** Avec $X = \frac{1}{x} \to 0^+$ : $x\ln\left(1 + \frac{1}{x}\right) = \dfrac{\ln(1 + X)}{X} \to 1$.

### Exercice 20 — Regrouper avant de passer à la limite <span class="etoiles">★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} \left(\ln(x^2 + 1) - 2\ln x\right)$
2. $\displaystyle\lim_{x\to+\infty} \left(\ln(2x + 1) - \ln x\right)$

??? success "Correction"
    **1.** $\ln(x^2 + 1) - \ln(x^2) = \ln\dfrac{x^2 + 1}{x^2} = \ln\left(1 + \frac{1}{x^2}\right) \to \ln 1 = 0$.

    **2.** $\ln\dfrac{2x + 1}{x} = \ln\left(2 + \frac{1}{x}\right) \to \ln 2$.

### Exercice 21 — En $0^+$ <span class="etoiles">★★</span>

Déterminer $\displaystyle\lim_{x\to 0^+} x^2\ln x$ et $\displaystyle\lim_{x\to 0^+} \sqrt{x}\ln x$.

??? success "Correction"
    **1.** Croissance comparée avec $n = 2$ : la limite est $0$.

    **2.** Avec $X = \sqrt{x} \to 0^+$ : $\sqrt{x}\ln x = X\ln(X^2) = 2X\ln X \to 0$.

### Exercice 22 — Le carré du logarithme <span class="etoiles">★★★</span>

Déterminer $\displaystyle\lim_{x\to+\infty} \frac{(\ln x)^2}{x}$.

??? success "Correction"
    On pose $X = \ln x \to +\infty$, et $x = e^X$ : $\dfrac{(\ln x)^2}{x} = \dfrac{X^2}{e^X} \to 0$, par croissance comparée de l'exponentielle et de $X^2$.

    *Plus généralement, $\frac{(\ln x)^p}{x^q} \to 0$ pour tous entiers $p, q \geq 1$ : n'importe quelle puissance du logarithme est négligeable devant n'importe quelle puissance de $x$.*

---

## Thème 5 — Suites et modélisation

*Méthode associée : [Méthode 6](methodes.md#methode-6-resoudre-un-probleme-de-seuil).*

### Exercice 23 — Seuil d'une suite géométrique <span class="etoiles">★</span>

Soit $u_n = 3 \times 0{,}8^n$. Déterminer, par le calcul, le plus petit entier $n$ tel que $u_n < 0{,}01$.

??? success "Correction"
    $3 \times 0{,}8^n < 0{,}01 \iff 0{,}8^n < \dfrac{1}{300} \iff n\ln 0{,}8 < -\ln 300$.

    Comme $\ln 0{,}8 < 0$, on change le sens en divisant : $n > \dfrac{-\ln 300}{\ln 0{,}8} \approx 25{,}56$. Le plus petit entier est $n = 26$.

### Exercice 24 — Doublement d'un capital <span class="etoiles">★★</span>

On place 1 000 € à intérêts composés au taux annuel de 3 %. Au bout de combien d'années le capital aura-t-il doublé ?

??? success "Correction"
    Après $n$ années, le capital vaut $1000 \times 1{,}03^n$. On cherche $n$ tel que $1{,}03^n \geq 2$, soit $n\ln 1{,}03 \geq \ln 2$, c'est-à-dire $n \geq \dfrac{\ln 2}{\ln 1{,}03} \approx 23{,}45$ (ici $\ln 1{,}03 > 0$). Il faut **24 ans**.

    *Règle pratique des banquiers, dite « règle de 72 » : le temps de doublement vaut environ $72$ divisé par le taux en %, soit $72 / 3 = 24$ ans.*

### Exercice 25 — Datation au carbone 14 <span class="etoiles">★★</span>

La quantité de carbone 14 dans un organisme mort évolue selon $N(t) = N_0\,e^{-\lambda t}$, où $t$ est en années. La demi-vie du carbone 14 est de 5 730 ans.

1. Montrer que $\lambda = \dfrac{\ln 2}{5730}$.
2. Un os contient 30 % du carbone 14 initial. Estimer son âge.

??? success "Correction"
    **1.** $N(5730) = \frac{N_0}{2} \iff e^{-5730\lambda} = \frac{1}{2} \iff -5730\lambda = -\ln 2 \iff \lambda = \frac{\ln 2}{5730}$.

    **2.** $e^{-\lambda t} = 0{,}3 \iff -\lambda t = \ln 0{,}3 \iff t = \dfrac{-\ln 0{,}3}{\lambda} = \dfrac{5730\,\ln(1/0{,}3)}{\ln 2} \approx 9\,950$ ans.

### Exercice 26 — Résoudre exactement d'anciens problèmes <span class="etoiles">★★</span>

1. *(Chapitre 2, sujet 4.)* Résoudre exactement l'inéquation $\dfrac{1000}{1 + 9e^{-0{,}4t}} > 900$ pour $t \geq 0$.
2. *(Chapitre 4, sujet 4.)* Résoudre exactement $20 + 70e^{-0{,}1t} = 50$.

??? success "Correction"
    **1.** Comme $1 + 9e^{-0{,}4t} > 0$ :

    $$\frac{1000}{1 + 9e^{-0{,}4t}} > 900 \iff 1 + 9e^{-0{,}4t} < \frac{10}{9} \iff e^{-0{,}4t} < \frac{1}{81} \iff -0{,}4t < -\ln 81 \iff t > \frac{\ln 81}{0{,}4}.$$

    $\frac{\ln 81}{0{,}4} \approx 10{,}99$ : on retrouve que la population dépasse 900 animaux à partir de la 11ᵉ année.

    **2.** $70e^{-0{,}1t} = 30 \iff e^{-0{,}1t} = \frac{3}{7} \iff t = -10\ln\frac{3}{7} = 10\ln\frac{7}{3} \approx 8{,}47$ minutes.

---

## Thème 6 — Approfondissement

### Exercice 27 — Qui est le plus grand : $e^\pi$ ou $\pi^e$ ? <span class="etoiles">★★★</span>

On reprend $f(x) = \dfrac{\ln x}{x}$ de l'exercice 14.

1. Montrer que pour tout $x > e$ : $\ln x < \dfrac{x}{e}$.
2. En déduire, sans calculatrice, lequel des deux nombres $e^\pi$ et $\pi^e$ est le plus grand.

??? success "Correction"
    **1.** $f$ est strictement décroissante sur $[e \,;\, +\infty[$, donc pour $x > e$ : $f(x) < f(e) = \frac{1}{e}$, soit $\dfrac{\ln x}{x} < \dfrac{1}{e}$. Comme $x > 0$ : $\ln x < \dfrac{x}{e}$.

    **2.** $\pi > e$, donc $\ln\pi < \dfrac{\pi}{e}$, soit $e\ln\pi < \pi$, c'est-à-dire $\ln(\pi^e) < \ln(e^\pi)$. Comme $\ln$ est strictement croissante : $\pi^e < e^\pi$.

    *Vérification : $e^\pi \approx 23{,}14$ et $\pi^e \approx 22{,}46$.*

### Exercice 28 — Encadrer le logarithme <span class="etoiles">★★★</span>

1. En utilisant $\ln X \leq X - 1$ avec $X = \frac{1}{x}$, montrer que pour tout $x > 0$ : $1 - \dfrac{1}{x} \leq \ln x \leq x - 1$.
2. En déduire, sans utiliser la dérivée, que $\displaystyle\lim_{x\to 1^+} \frac{\ln x}{x - 1} = 1$.

??? success "Correction"
    **1.** La majoration est l'inégalité du cours. Avec $X = \frac{1}{x}$ : $\ln\frac{1}{x} \leq \frac{1}{x} - 1$, soit $-\ln x \leq \frac{1}{x} - 1$, donc $\ln x \geq 1 - \frac{1}{x}$.

    **2.** Pour $x > 1$, $x - 1 > 0$. On divise l'encadrement par $x - 1$, en remarquant que $1 - \frac{1}{x} = \frac{x - 1}{x}$ :

    $$\frac{1}{x} \leq \frac{\ln x}{x - 1} \leq 1.$$

    Quand $x \to 1^+$, $\frac{1}{x} \to 1$ : par les gendarmes, la limite est $1$. *C'est bien $\ln'(1) = 1$.*
