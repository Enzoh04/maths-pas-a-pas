# Cours — Primitives et équations différentielles

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, $I$ désigne un intervalle de $\mathbb{R}$.

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Équations différentielles

!!! definition "Équation différentielle"
    Une **équation différentielle** est une égalité qui relie une fonction inconnue $y$ et ses dérivées $y'$, $y''$… **Résoudre** l'équation sur $I$, c'est trouver **toutes** les fonctions dérivables sur $I$ qui la vérifient.

**Exemples.**

- $y' = 2y$ : on cherche les fonctions $f$ telles que $f'(x) = 2f(x)$ pour tout $x$. La fonction $f(x) = 3e^{2x}$ convient, car $f'(x) = 6e^{2x} = 2f(x)$.
- $y' = \cos x$ : on cherche les fonctions dont la dérivée est le cosinus. La fonction $\sin$ convient.

**Pourquoi c'est important.** Les lois de la physique, de la biologie ou de l'économie relient souvent une grandeur à sa **vitesse de variation** : la vitesse de désintégration d'un échantillon radioactif est proportionnelle à sa masse, la vitesse de refroidissement d'un objet est proportionnelle à l'écart de température avec l'air… Ces lois s'écrivent sous forme d'équations différentielles.

---

## 2. Primitives

### 2.1 Définition

!!! definition "Primitive"
    Soit $f$ une fonction définie sur $I$. On appelle **primitive** de $f$ sur $I$ toute fonction $F$ dérivable sur $I$ telle que $F' = f$.

    Autrement dit, $F$ est une solution de l'équation différentielle $y' = f$.

**Exemple.** $F(x) = x^2$ est une primitive de $f(x) = 2x$ sur $\mathbb{R}$. Mais $x^2 + 5$ et $x^2 - \pi$ aussi !

!!! theoreme "Ensemble des primitives"
    Si $F$ est une primitive de $f$ sur un **intervalle** $I$, alors les primitives de $f$ sur $I$ sont exactement les fonctions $x \mapsto F(x) + C$, où $C$ est une constante réelle.

    Autrement dit : **deux primitives d'une même fonction sur un intervalle diffèrent d'une constante**.

??? demo "Démonstration — au programme du bac"
    - Pour tout réel $C$, $(F + C)' = F' = f$ : la fonction $F + C$ est bien une primitive.
    - Réciproquement, soit $G$ une primitive de $f$ sur $I$. Alors $(G - F)' = G' - F' = f - f = 0$ sur $I$. Une fonction de dérivée nulle sur un **intervalle** est constante (chapitre 3, § 1.3) : il existe un réel $C$ tel que $G - F = C$, soit $G = F + C$.

!!! warning "Sur un intervalle"
    Sur $\mathbb{R}^* = \,]-\infty \,;\, 0[ \,\cup\, ]0 \,;\, +\infty[$, qui n'est pas un intervalle, la fonction $F$ définie par $F(x) = -\frac{1}{x}$ pour $x > 0$ et $F(x) = -\frac{1}{x} + 7$ pour $x < 0$ a pour dérivée $\frac{1}{x^2}$, mais ne diffère pas de $-\frac{1}{x}$ d'une seule constante.

!!! propriete "Primitive prenant une valeur donnée"
    Si $f$ admet une primitive sur $I$, alors pour tous $x_0 \in I$ et $y_0 \in \mathbb{R}$, il existe une **unique** primitive $F$ de $f$ sur $I$ telle que $F(x_0) = y_0$.

??? demoplus "Démonstration — pour aller plus loin"
    Si $G$ est une primitive, les primitives sont les $G + C$. La condition $G(x_0) + C = y_0$ impose $C = y_0 - G(x_0)$, et une seule valeur de $C$ convient.

!!! theoreme "Existence"
    Toute fonction **continue** sur un intervalle $I$ admet des primitives sur $I$.

??? admis "Pourquoi ce résultat est admis"
    Pour les fonctions usuelles, on trouve une primitive « à la main » (tableau du § 2.2). Pour une fonction continue quelconque, on construit une primitive à l'aide de l'**intégrale** : $F(x) = \displaystyle\int_a^x f(t)\,\mathrm{d}t$. Le chapitre 8 le démontre dans le cas d'une fonction continue, positive et croissante. Le cas général demande de définir l'intégrale de toute fonction continue (intégrale de Riemann), ce qui se fait en **première année du supérieur** et repose encore sur la complétude de $\mathbb{R}$.

    Attention : certaines fonctions continues très simples, comme $x \mapsto e^{-x^2}$, ont des primitives qu'on **ne peut pas** écrire avec les fonctions usuelles. Elles existent pourtant !

### 2.2 Primitives usuelles

Pour trouver une primitive, on lit le tableau des dérivées « à l'envers ». Dans le tableau, $C$ est une constante réelle.

| $f(x)$ | Une primitive $F(x)$ | Sur |
|---|---|---|
| $a$ (constante) | $ax$ | $\mathbb{R}$ |
| $x^n$ ($n \geq 0$ entier) | $\dfrac{x^{n+1}}{n + 1}$ | $\mathbb{R}$ |
| $\dfrac{1}{x^2}$ | $-\dfrac{1}{x}$ | $]0 \,;\, +\infty[$ ou $]-\infty \,;\, 0[$ |
| $\dfrac{1}{x^n}$ ($n \geq 2$) | $-\dfrac{1}{(n - 1)x^{n-1}}$ | $]0 \,;\, +\infty[$ ou $]-\infty \,;\, 0[$ |
| $\dfrac{1}{\sqrt{x}}$ | $2\sqrt{x}$ | $]0 \,;\, +\infty[$ |
| $\dfrac{1}{x}$ | $\ln x$ | $]0 \,;\, +\infty[$ |
| $e^x$ | $e^x$ | $\mathbb{R}$ |
| $\cos x$ | $\sin x$ | $\mathbb{R}$ |
| $\sin x$ | $-\cos x$ | $\mathbb{R}$ |

!!! propriete "Opérations et formes composées"
    Si $F$ et $G$ sont des primitives de $f$ et $g$, et $k$ un réel, alors $F + G$ est une primitive de $f + g$ et $kF$ une primitive de $kf$.

    Si $u$ est dérivable sur $I$ :

    | Fonction | Une primitive | Condition |
    |---|---|---|
    | $u'e^{u}$ | $e^{u}$ | |
    | $u'u^n$ ($n \geq 0$) | $\dfrac{u^{n+1}}{n + 1}$ | |
    | $\dfrac{u'}{u^2}$ | $-\dfrac{1}{u}$ | $u$ ne s'annule pas |
    | $\dfrac{u'}{\sqrt{u}}$ | $2\sqrt{u}$ | $u > 0$ |
    | $\dfrac{u'}{u}$ | $\ln u$ | $u > 0$ |
    | $u'\cos u$ | $\sin u$ | |
    | $u'\sin u$ | $-\cos u$ | |
    | $f(ax + b)$ | $\dfrac{1}{a}F(ax + b)$ | $a \neq 0$ |

??? demoplus "Démonstration — pour aller plus loin"
    Il suffit de **dériver** la fonction proposée, avec la formule de dérivation d'une composée (chapitre 3). Par exemple, $\left(\frac{u^{n+1}}{n + 1}\right)' = \frac{(n + 1)u'u^n}{n + 1} = u'u^n$, et $\left(\frac{1}{a}F(ax + b)\right)' = \frac{1}{a} \times a\,f(ax + b) = f(ax + b)$.

!!! tip "Vérifier, toujours"
    Une primitive se **vérifie** en la dérivant. C'est rapide et cela évite la plupart des erreurs de coefficients.

**Exemples.**

- $f(x) = x\,e^{x^2}$. Avec $u = x^2$, $u' = 2x$ : $f = \frac{1}{2}u'e^u$, donc $F(x) = \frac{1}{2}e^{x^2}$.
- $f(x) = \dfrac{3}{3x + 1}$ sur $\left]-\frac{1}{3} \,;\, +\infty\right[$ : c'est $\frac{u'}{u}$ avec $u = 3x + 1 > 0$, donc $F(x) = \ln(3x + 1)$.

---

## 3. L'équation $y' = ay$

!!! theoreme "Solutions de $y' = ay$"
    Soit $a$ un réel. Les solutions sur $\mathbb{R}$ de l'équation différentielle $y' = ay$ sont les fonctions

    $$x \mapsto Ce^{ax}, \qquad C \in \mathbb{R}.$$

??? demo "Démonstration — au programme du bac"
    - Pour tout réel $C$, la fonction $f(x) = Ce^{ax}$ vérifie $f'(x) = aCe^{ax} = af(x)$ : c'est une solution.
    - Réciproquement, soit $f$ une solution. On pose $g(x) = f(x)e^{-ax}$. Alors

    $$g'(x) = f'(x)e^{-ax} - af(x)e^{-ax} = \big(f'(x) - af(x)\big)e^{-ax} = 0.$$

    Donc $g$ est constante sur $\mathbb{R}$ (qui est un intervalle) : il existe $C$ tel que $f(x)e^{-ax} = C$, soit $f(x) = Ce^{ax}$.

!!! propriete "Avec une condition initiale"
    Pour tous réels $x_0$ et $y_0$, il existe une **unique** solution $f$ de $y' = ay$ telle que $f(x_0) = y_0$ : c'est $f(x) = y_0\,e^{a(x - x_0)}$.

??? demoplus "Démonstration — pour aller plus loin"
    $f(x) = Ce^{ax}$ et $f(x_0) = y_0 \iff Ce^{ax_0} = y_0 \iff C = y_0e^{-ax_0}$. Une seule valeur de $C$ convient, et l'on obtient $f(x) = y_0e^{-ax_0}e^{ax} = y_0e^{a(x - x_0)}$.

**Remarque.** Avec $a = 1$ et $f(0) = 1$, on retrouve que l'exponentielle est l'**unique** fonction égale à sa dérivée et valant $1$ en $0$ : c'est sa définition, vue en Première.

---

## 4. L'équation $y' = ay + b$

!!! theoreme "Solutions de $y' = ay + b$"
    Soit $a \neq 0$ et $b$ deux réels. Les solutions sur $\mathbb{R}$ de $y' = ay + b$ sont les fonctions

    $$x \mapsto Ce^{ax} - \frac{b}{a}, \qquad C \in \mathbb{R}.$$

    La fonction constante $x \mapsto -\frac{b}{a}$ est la **solution particulière constante** (ou « solution d'équilibre »).

??? demoplus "Démonstration — pour aller plus loin"
    La fonction constante $p(x) = -\frac{b}{a}$ est solution : $p' = 0$ et $ap + b = -b + b = 0$.

    Soit $f$ une fonction dérivable. On pose $g = f - p = f + \frac{b}{a}$. Alors $g' = f'$ et $ag = af + b$. Donc

    $$f' = af + b \iff g' = ag \iff g(x) = Ce^{ax} \iff f(x) = Ce^{ax} - \frac{b}{a}.$$

!!! tip "Comportement à l'infini"
    Si $a < 0$, alors $Ce^{ax} \to 0$ quand $x \to +\infty$ : **toutes** les solutions tendent vers la solution d'équilibre $-\frac{b}{a}$, quelle que soit la condition initiale. C'est par exemple le cas d'un objet qui refroidit jusqu'à la température de la pièce.

**Exemple.** $y' = -2y + 6$. Solution constante : $-\frac{6}{-2} = 3$. Solutions : $f(x) = Ce^{-2x} + 3$. Avec $f(0) = 1$ : $C + 3 = 1$, donc $C = -2$, et $f(x) = 3 - 2e^{-2x}$.

---

## 5. L'équation $y' = ay + f$

!!! theoreme "Solution particulière et solutions générales"
    Soit $a$ un réel et $f$ une fonction définie sur $I$. Si $p$ est **une** solution particulière de $y' = ay + f$ sur $I$, alors les solutions de cette équation sur $I$ sont les fonctions

    $$x \mapsto p(x) + Ce^{ax}, \qquad C \in \mathbb{R}.$$

    En résumé : **solution générale = solution particulière + solutions de $y' = ay$**.

??? demoplus "Démonstration — pour aller plus loin"
    Soit $g$ dérivable sur $I$. Comme $p' = ap + f$ :

    $$g' = ag + f \iff g' - p' = ag + f - (ap + f) \iff (g - p)' = a(g - p).$$

    D'après le § 3 (la démonstration marche sur tout intervalle), cela équivaut à $g - p = Ce^{ax}$, soit $g = p + Ce^{ax}$.

**Trouver une solution particulière.** Au bac, elle est en général donnée ou suggérée : on cherche $p$ « de la même forme » que $f$.

| Si $f(x)$ est… | On cherche $p(x)$ de la forme… |
|---|---|
| un polynôme de degré $n$ | un polynôme de degré $n$ (si $a \neq 0$) |
| $ke^{mx}$ avec $m \neq a$ | $\lambda e^{mx}$ |
| $ke^{ax}$ | $\lambda x e^{ax}$ |
| $k_1\cos(\omega x) + k_2\sin(\omega x)$ | $\lambda\cos(\omega x) + \mu\sin(\omega x)$ |

**Exemple.** $y' = 2y + x$. On cherche $p(x) = \alpha x + \beta$ : $p'(x) = \alpha$ et $2p(x) + x = (2\alpha + 1)x + 2\beta$. Par identification : $2\alpha + 1 = 0$ et $\alpha = 2\beta$, donc $\alpha = -\frac{1}{2}$ et $\beta = -\frac{1}{4}$. Les solutions sont $x \mapsto -\frac{x}{2} - \frac{1}{4} + Ce^{2x}$.

---

## 6. Modélisation

| Phénomène | Équation | Solution |
|---|---|---|
| Désintégration radioactive | $N' = -\lambda N$ | $N(t) = N_0e^{-\lambda t}$ |
| Refroidissement (loi de Newton) | $\theta' = -k(\theta - \theta_{\text{air}})$ | $\theta(t) = \theta_{\text{air}} + (\theta_0 - \theta_{\text{air}})e^{-kt}$ |
| Charge d'un condensateur | $RC\,u' + u = E$ | $u(t) = E\left(1 - e^{-t/(RC)}\right)$ si $u(0) = 0$ |
| Chute avec frottement | $v' = g - \frac{k}{m}v$ | $v(t) = \frac{mg}{k}\left(1 - e^{-kt/m}\right)$ si $v(0) = 0$ |

Dans tous ces exemples, la grandeur tend vers une **valeur d'équilibre** : $0$, la température de l'air, la tension $E$, ou la « vitesse limite » $\frac{mg}{k}$.

---

## 7. Pour aller plus loin

- **Méthode d'Euler** (vue en Première) : pour approcher la solution de $y' = F(x, y)$, on avance par petits pas $h$ en utilisant l'approximation affine $y(x + h) \approx y(x) + h\,y'(x)$. Voir l'exercice 28.
- **Équation logistique** $y' = ay\left(1 - \frac{y}{K}\right)$ : elle modélise une population limitée par les ressources. L'exercice 27 la résout par le changement de fonction $z = \frac{1}{y}$.
- **Équations du second ordre** : $y'' + \omega^2 y = 0$ (ressort, pendule) a pour solutions $A\cos(\omega x) + B\sin(\omega x)$ (chapitre 6, exercice 27). Ces équations sont étudiées en détail dans le supérieur.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
