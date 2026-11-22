# Cours — Fonction logarithme népérien

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.

---

## 1. Définition

### 1.1 Le logarithme d'un nombre strictement positif

On sait résoudre $e^x = 1$ (solution $0$) ou $e^x = e$ (solution $1$). Mais comment résoudre $e^x = 5$ ? Le théorème suivant assure qu'il y a une solution, et une seule.

!!! propriete "Existence et unicité"
    Pour tout réel $a > 0$, l'équation $e^x = a$ admet une **unique** solution réelle.

??? demoplus "Démonstration — pour aller plus loin"
    La fonction exponentielle est continue et strictement croissante sur $\mathbb{R}$, avec $\displaystyle\lim_{x\to-\infty} e^x = 0$ et $\displaystyle\lim_{x\to+\infty} e^x = +\infty$ (chapitre 2). Pour $a \in \,]0 \,;\, +\infty[$, le corollaire du théorème des valeurs intermédiaires, dans sa version avec limites (chapitre 4, § 3.3), donne une unique solution.

!!! definition "Logarithme népérien"
    Pour tout réel $a > 0$, on appelle **logarithme népérien de $a$**, noté $\ln a$ ou $\ln(a)$, l'unique réel $x$ tel que $e^x = a$.

    La fonction $\ln : x \mapsto \ln x$ est définie sur $]0 \,;\, +\infty[$.

**En résumé**, pour $a > 0$ et $x$ réel : $\quad e^x = a \iff x = \ln a$.

!!! propriete "Conséquences immédiates"
    - Pour tout réel $x > 0$ : $e^{\ln x} = x$.
    - Pour tout réel $x$ : $\ln(e^x) = x$.
    - $\ln 1 = 0$ et $\ln e = 1$.

??? demoplus "Démonstration — pour aller plus loin"
    Le premier point est la définition de $\ln x$. Pour le deuxième, $\ln(e^x)$ est l'unique réel $y$ tel que $e^y = e^x$ ; or $y = x$ convient, donc $\ln(e^x) = x$. Enfin, $e^0 = 1$ donne $\ln 1 = 0$ et $e^1 = e$ donne $\ln e = 1$.

On dit que $\ln$ est la **fonction réciproque** de l'exponentielle : chacune « défait » ce que fait l'autre.

!!! propriete "Courbes symétriques"
    Dans un repère orthonormé, les courbes de $\exp$ et de $\ln$ sont symétriques par rapport à la droite d'équation $y = x$.

??? demoplus "Démonstration — pour aller plus loin"
    Le symétrique du point $M(a \,;\, b)$ par rapport à la droite $y = x$ est le point $M'(b \,;\, a)$. Or $M$ est sur la courbe de $\ln$ $\iff$ $b = \ln a$ $\iff$ $e^b = a$ $\iff$ $M'$ est sur la courbe de $\exp$.

### 1.2 Sens de variation, équations et inéquations

!!! propriete "Le logarithme est strictement croissant"
    Pour tous réels $a > 0$ et $b > 0$ :

    $$\ln a = \ln b \iff a = b, \qquad \ln a < \ln b \iff a < b.$$

    En particulier : $\ln x < 0 \iff 0 < x < 1$, et $\ln x > 0 \iff x > 1$.

??? demoplus "Démonstration — pour aller plus loin"
    On écrit $a = e^{\ln a}$ et $b = e^{\ln b}$. L'exponentielle étant strictement croissante, $\ln a < \ln b \iff e^{\ln a} < e^{\ln b} \iff a < b$. L'égalité se traite de même. Le cas particulier s'obtient avec $b = 1$, puisque $\ln 1 = 0$.

**Exemples.**

- $e^x = 5 \iff x = \ln 5$.
- $e^{2x} > 3 \iff 2x > \ln 3 \iff x > \frac{\ln 3}{2}$ (on applique $\ln$, strictement croissante).
- $\ln x \leq 2 \iff 0 < x \leq e^2$ (on applique $\exp$, strictement croissante, sans oublier que $x > 0$).

---

## 2. Propriétés algébriques

!!! theoreme "Relation fonctionnelle"
    Pour tous réels $a > 0$ et $b > 0$ :

    $$\ln(ab) = \ln a + \ln b.$$

??? demoplus "Démonstration — pour aller plus loin"
    $e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = a \times b$. Donc $\ln a + \ln b$ est l'unique réel dont l'exponentielle vaut $ab$ : c'est $\ln(ab)$.

**Le logarithme transforme les produits en sommes.** C'est pour cela qu'il a été inventé, au XVIIᵉ siècle, par John Napier (Neper) : les astronomes et les navigateurs remplaçaient les longues multiplications par des additions, à l'aide de tables de logarithmes.

!!! propriete "Conséquences"
    Pour tous réels $a > 0$, $b > 0$ et tout entier relatif $n$ :

    $$\ln\left(\frac{1}{a}\right) = -\ln a, \qquad \ln\left(\frac{a}{b}\right) = \ln a - \ln b, \qquad \ln(a^n) = n\ln a, \qquad \ln\sqrt{a} = \frac{1}{2}\ln a.$$

??? demoplus "Démonstration — pour aller plus loin"
    - $\ln a + \ln\frac{1}{a} = \ln\left(a \times \frac{1}{a}\right) = \ln 1 = 0$, d'où $\ln\frac{1}{a} = -\ln a$.
    - $\ln\frac{a}{b} = \ln\left(a \times \frac{1}{b}\right) = \ln a + \ln\frac{1}{b} = \ln a - \ln b$.
    - $\ln(a^n) = n \ln a$ : par récurrence pour $n \geq 0$ (on a $\ln(a^{n+1}) = \ln(a^n) + \ln a$), puis, pour $n < 0$, $\ln(a^n) = \ln\frac{1}{a^{-n}} = -(-n)\ln a = n\ln a$ (voir l'exercice 5).
    - $2\ln\sqrt{a} = \ln\left((\sqrt{a})^2\right) = \ln a$.

!!! warning "Erreurs fréquentes"
    - $\ln(a + b) \neq \ln a + \ln b$ ! Par exemple, $\ln 2 = \ln(1 + 1) \neq \ln 1 + \ln 1 = 0$.
    - $\ln(x^2) = 2\ln x$ n'est vrai que pour $x > 0$. Pour tout $x \neq 0$, $\ln(x^2) = 2\ln|x|$.

---

## 3. Étude de la fonction logarithme

### 3.1 Continuité et dérivabilité

!!! propriete "Continuité"
    La fonction $\ln$ est continue sur $]0 \,;\, +\infty[$.

??? demoplus "Démonstration — pour aller plus loin"
    Soit $a > 0$ et $\varepsilon > 0$. Comme $\ln$ et $\exp$ sont strictement croissantes :

    $$\ln a - \varepsilon < \ln x < \ln a + \varepsilon \iff a e^{-\varepsilon} < x < a e^{\varepsilon}.$$

    L'intervalle $\left]a e^{-\varepsilon} \,;\, a e^{\varepsilon}\right[$ contient $a$, car $e^{-\varepsilon} < 1 < e^{\varepsilon}$. On pose $\delta = \min\left(a - a e^{-\varepsilon},\, a e^{\varepsilon} - a\right) > 0$. Si $|x - a| < \delta$, alors $x$ est dans cet intervalle, donc $|\ln x - \ln a| < \varepsilon$.

!!! theoreme "Dérivée du logarithme"
    La fonction $\ln$ est dérivable sur $]0 \,;\, +\infty[$ et

    $$\ln'(x) = \frac{1}{x}.$$

??? demo "Démonstration — au programme du bac (la dérivabilité étant admise)"
    Pour tout $x > 0$, on a $e^{\ln x} = x$. On dérive les deux membres. À gauche, on dérive la composée $e^{u}$ avec $u = \ln$, ce qui donne $\ln'(x)\,e^{\ln x}$. À droite, on obtient $1$. Donc :

    $$\ln'(x) \times e^{\ln x} = 1, \quad \text{soit} \quad \ln'(x) \times x = 1, \quad \text{d'où} \quad \ln'(x) = \frac{1}{x}.$$

??? demoplus "Démonstration de la dérivabilité — pour aller plus loin"
    Soit $a > 0$ et $b = \ln a$. Pour $x > 0$, $x \neq a$, on pose $y = \ln x$ ; alors $y \neq b$ (car $\ln$ est strictement croissante) et $x = e^y$, $a = e^b$. Le taux d'accroissement s'écrit :

    $$\frac{\ln x - \ln a}{x - a} = \frac{y - b}{e^y - e^b} = \frac{1}{\dfrac{e^y - e^b}{y - b}}.$$

    Quand $x \to a$, on a $y = \ln x \to \ln a = b$ par continuité de $\ln$. Et $\dfrac{e^y - e^b}{y - b} \to \exp'(b) = e^b = a$, qui est non nul. Par composition et quotient, le taux tend vers $\dfrac{1}{a}$.

!!! propriete "Conséquences"
    - $\ln$ est **strictement croissante** sur $]0 \,;\, +\infty[$ (sa dérivée $\frac{1}{x}$ est strictement positive).
    - $\ln$ est **concave** sur $]0 \,;\, +\infty[$ : $\ln''(x) = -\dfrac{1}{x^2} < 0$.
    - La tangente au point d'abscisse $1$ a pour équation $y = x - 1$. Par concavité : **$\ln x \leq x - 1$** pour tout $x > 0$.

### 3.2 Limites

!!! propriete "Limites aux bornes"
    $$\lim_{x \to +\infty} \ln x = +\infty \qquad\qquad \lim_{x \to 0^+} \ln x = -\infty$$

    La droite $x = 0$ (l'axe des ordonnées) est asymptote verticale à la courbe de $\ln$.

??? demoplus "Démonstration — pour aller plus loin"
    **En $+\infty$.** Soit $A$ un réel. Pour $x > e^A$, on a $\ln x > \ln(e^A) = A$, car $\ln$ est croissante.

    **En $0^+$.** Soit $A$ un réel. Pour $0 < x < e^{A}$, on a $\ln x < A$. Donc $\ln x$ devient inférieur à n'importe quel réel quand $x$ s'approche de $0$ : $\ln x \to -\infty$.

| $x$ | $0$ | | $1$ | | $e$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $\ln'(x) = \frac{1}{x}$ | | $+$ | | $+$ | | $+$ | |
| $\ln x$ | $-\infty$ | $\nearrow$ | $0$ | $\nearrow$ | $1$ | $\nearrow$ | $+\infty$ |

!!! propriete "Une limite en $0$"
    $$\lim_{x\to 0} \frac{\ln(1 + x)}{x} = 1.$$

??? demoplus "Démonstration — pour aller plus loin"
    $\dfrac{\ln(1 + x)}{x} = \dfrac{\ln(1 + x) - \ln 1}{(1 + x) - 1}$ est le taux d'accroissement de $\ln$ entre $1$ et $1 + x$. Il tend vers $\ln'(1) = 1$.

---

## 4. Dérivée de $\ln(u)$

!!! theoreme "Dérivée de $\ln u$"
    Si $u$ est dérivable et **strictement positive** sur un intervalle $I$, alors $\ln(u)$ est dérivable sur $I$ et

    $$\big(\ln(u)\big)' = \frac{u'}{u}.$$

??? demoplus "Démonstration — pour aller plus loin"
    C'est la dérivée d'une composée (chapitre 3) avec $v = \ln$ et $v'(X) = \frac{1}{X}$ : $(\ln u)' = u' \times \frac{1}{u}$.

**Exemples.**

- $\left(\ln(x^2 + 1)\right)' = \dfrac{2x}{x^2 + 1}$ sur $\mathbb{R}$.
- $\left(\ln(3x - 6)\right)' = \dfrac{3}{3x - 6} = \dfrac{1}{x - 2}$ sur $]2 \,;\, +\infty[$.

!!! tip "Signe de la dérivée"
    Comme $u > 0$, la dérivée de $\ln u$ a le **signe de $u'$** : $\ln u$ a les mêmes variations que $u$.

---

## 5. Croissances comparées

En $+\infty$, $\ln x$ et $x$ tendent tous deux vers $+\infty$, mais le logarithme est **beaucoup plus lent**.

!!! theoreme "Croissances comparées du logarithme"
    Pour tout entier $n \geq 1$ :

    $$\lim_{x \to +\infty} \frac{\ln x}{x^n} = 0 \qquad\qquad \lim_{x \to 0^+} x^n \ln x = 0$$

    En particulier : $\displaystyle\lim_{x \to +\infty} \frac{\ln x}{x} = 0$ et $\displaystyle\lim_{x \to 0^+} x \ln x = 0$.

??? demo "Démonstration — au programme du bac : limite de $x \ln x$ en $0$"
    On pose $X = \ln x$, de sorte que $x = e^X$. Quand $x \to 0^+$, $X \to -\infty$. Alors :

    $$x \ln x = e^X \times X = X e^X.$$

    Or, par croissance comparée (chapitre 2), $\displaystyle\lim_{X \to -\infty} X e^X = 0$. Par composition, $\displaystyle\lim_{x\to 0^+} x\ln x = 0$.

??? demoplus "Démonstration des autres limites — pour aller plus loin"
    **$\frac{\ln x}{x}$ en $+\infty$.** Avec $X = \ln x \to +\infty$ : $\dfrac{\ln x}{x} = \dfrac{X}{e^X} \to 0$ par croissance comparée de l'exponentielle.

    **$\frac{\ln x}{x^n}$ en $+\infty$.** Pour $n \geq 1$ et $x > 1$ : $\ln x > 0$ et $x^n \geq x$, donc $0 < \dfrac{\ln x}{x^n} \leq \dfrac{\ln x}{x}$. Par les gendarmes, la limite est $0$.

    **$x^n \ln x$ en $0^+$.** Pour $n \geq 1$, $x^n \ln x = x^{n-1} \times x\ln x$. Pour $0 < x < 1$, $0 < x^{n-1} \leq 1$, donc $|x^n \ln x| \leq |x\ln x|$, qui tend vers $0$.

!!! tip "À retenir"
    En l'infini, **les puissances de $x$ l'emportent sur le logarithme**, et **l'exponentielle l'emporte sur les puissances** :

    $$\ln x \ll x^n \ll e^x \quad \text{quand } x \to +\infty.$$

---

## 6. Applications

### 6.1 Résoudre exactement des problèmes de seuil

Le logarithme permet de résoudre les inéquations du type $q^n < a$, qu'on traitait jusqu'ici à la calculatrice ou avec un algorithme.

**Exemple.** Le plus petit entier $n$ tel que $0{,}8^n < 0{,}01$. On applique $\ln$, strictement croissante :

$$0{,}8^n < 0{,}01 \iff n\ln 0{,}8 < \ln 0{,}01 \iff n > \frac{\ln 0{,}01}{\ln 0{,}8} \approx 20{,}6.$$

!!! warning "Attention au signe"
    $\ln 0{,}8 < 0$ (car $0{,}8 < 1$) : en divisant par $\ln 0{,}8$, **on change le sens de l'inégalité**. Le plus petit entier est $n = 21$.

### 6.2 Croissance et décroissance exponentielles

Une grandeur qui évolue selon $N(t) = N_0\,e^{kt}$ double (si $k > 0$) ou est divisée par $2$ (si $k < 0$) en un temps fixe :

- **temps de doublement** : $t_d = \dfrac{\ln 2}{k}$ ;
- **demi-vie** (radioactivité, médicaments) : $t_{1/2} = \dfrac{\ln 2}{|k|}$.

En effet, $N_0 e^{kt} = 2N_0 \iff e^{kt} = 2 \iff kt = \ln 2$.

---

## 7. Pour aller plus loin

- **Logarithme décimal** : $\log x = \dfrac{\ln x}{\ln 10}$. Il vérifie $\log(10^n) = n$, et sert pour le pH, les décibels ou l'échelle de Richter (voir le sujet type bac 4).
- **Puissances réelles** : pour $a > 0$ et $x$ réel, on définit $a^x = e^{x \ln a}$. On retrouve les puissances entières, et l'on peut écrire $2^{\sqrt{2}}$ ou $10^{0{,}3}$.
- **Le logarithme comme intégrale** : au chapitre 8, on verra que $\ln x = \displaystyle\int_1^x \frac{1}{t}\,\mathrm{d}t$. C'est souvent ainsi qu'on le définit dans le supérieur.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
