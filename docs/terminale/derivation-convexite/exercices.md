# Exercices corrigés — Dérivation et convexité

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Dérivée d'une fonction composée | 1 à 7 |
| 2. Dérivée seconde et convexité | 8 à 13 |
| 3. Points d'inflexion | 14 à 17 |
| 4. Inégalités de convexité | 18 à 22 |
| 5. Études de fonctions complètes | 23 à 26 |
| 6. Approfondissement | 27 et 28 |

---

## Thème 1 — Dérivée d'une fonction composée

*Méthode associée : [Méthode 1](methodes.md#methode-1-deriver-une-fonction-composee).*

### Exercice 1 — Formules de base <span class="etoiles">★</span>

Calculer la dérivée de chaque fonction (on ne précise pas l'ensemble de dérivabilité).

1. $f(x) = (3x - 1)^4$
2. $g(x) = e^{x^2}$
3. $h(x) = \sqrt{x^2 + 1}$
4. $k(x) = \dfrac{1}{(2x + 5)^2}$

??? success "Correction"
    1. $u = 3x - 1$, $u' = 3$ : $f'(x) = 4 \times 3 \times (3x - 1)^3 = 12(3x - 1)^3$.
    2. $u = x^2$, $u' = 2x$ : $g'(x) = 2x\,e^{x^2}$.
    3. $u = x^2 + 1$, $u' = 2x$ : $h'(x) = \dfrac{2x}{2\sqrt{x^2 + 1}} = \dfrac{x}{\sqrt{x^2 + 1}}$.
    4. $k = \dfrac{1}{u^2}$ avec $u = 2x + 5$ : $k'(x) = -\dfrac{2u'}{u^3} = -\dfrac{4}{(2x + 5)^3}$.

### Exercice 2 — Exponentielles composées <span class="etoiles">★</span>

Calculer les dérivées de :

1. $f(x) = e^{-3x + 1}$
2. $g(x) = e^{1/x}$ sur $]0 \,;\, +\infty[$
3. $h(x) = x\,e^{-x^2}$

??? success "Correction"
    1. $f'(x) = -3e^{-3x + 1}$.
    2. $u = \frac{1}{x}$, $u' = -\frac{1}{x^2}$ : $g'(x) = -\dfrac{e^{1/x}}{x^2}$.
    3. Produit : $h'(x) = e^{-x^2} + x \times (-2x)e^{-x^2} = (1 - 2x^2)\,e^{-x^2}$.

### Exercice 3 — Produits et quotients <span class="etoiles">★★</span>

1. Soit $f(x) = (x + 1)\sqrt{2x + 3}$ sur $\left]-\frac{3}{2} \,;\, +\infty\right[$. Montrer que $f'(x) = \dfrac{3x + 4}{\sqrt{2x + 3}}$.
2. Soit $g(x) = \dfrac{e^{2x}}{1 + e^{2x}}$. Montrer que $g'(x) = \dfrac{2e^{2x}}{(1 + e^{2x})^2}$ et en déduire le sens de variation de $g$.

??? success "Correction"
    **1.** $(\sqrt{2x + 3})' = \dfrac{2}{2\sqrt{2x + 3}} = \dfrac{1}{\sqrt{2x + 3}}$. Par la formule du produit :

    $$f'(x) = \sqrt{2x + 3} + \frac{x + 1}{\sqrt{2x + 3}} = \frac{(2x + 3) + (x + 1)}{\sqrt{2x + 3}} = \frac{3x + 4}{\sqrt{2x + 3}}.$$

    **2.** Formule du quotient avec $u = e^{2x}$, $u' = 2e^{2x}$, $v = 1 + e^{2x}$, $v' = 2e^{2x}$ :

    $$g'(x) = \frac{2e^{2x}(1 + e^{2x}) - e^{2x} \times 2e^{2x}}{(1 + e^{2x})^2} = \frac{2e^{2x}}{(1 + e^{2x})^2}.$$

    Cette dérivée est strictement positive : $g$ est strictement croissante sur $\mathbb{R}$.

### Exercice 4 — Utiliser la formule générale <span class="etoiles">★★</span>

Soit $v(X) = X^3 - X$ et $u(x) = e^x$.

1. Calculer $(v \circ u)'(x)$ avec la formule de dérivation d'une composée.
2. Retrouver le résultat en développant d'abord $v(u(x))$.

??? success "Correction"
    **1.** $v'(X) = 3X^2 - 1$ et $u'(x) = e^x$, donc $(v \circ u)'(x) = e^x\big(3(e^x)^2 - 1\big) = e^x(3e^{2x} - 1)$.

    **2.** $v(u(x)) = e^{3x} - e^x$, de dérivée $3e^{3x} - e^x = e^x(3e^{2x} - 1)$. On retrouve bien le même résultat.

### Exercice 5 — Tangente <span class="etoiles">★★</span>

Déterminer une équation de la tangente à la courbe de $f(x) = \sqrt{4x + 1}$ au point d'abscisse $2$.

??? success "Correction"
    $f(2) = \sqrt{9} = 3$. $f'(x) = \dfrac{4}{2\sqrt{4x + 1}} = \dfrac{2}{\sqrt{4x + 1}}$, donc $f'(2) = \dfrac{2}{3}$.

    La tangente a pour équation $y = \frac{2}{3}(x - 2) + 3$, soit $y = \dfrac{2}{3}x + \dfrac{5}{3}$.

### Exercice 6 — Étude d'une gaussienne <span class="etoiles">★★</span>

Soit $f(x) = e^{-x^2}$ sur $\mathbb{R}$.

1. Calculer $f'(x)$ et dresser le tableau de variations de $f$, limites comprises.
2. Montrer que la courbe est symétrique par rapport à l'axe des ordonnées.

??? success "Correction"
    **1.** $f'(x) = -2x\,e^{-x^2}$, du signe de $-x$. En $\pm\infty$, $-x^2 \to -\infty$ donc $f(x) \to 0$ (composition).

    | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $0$ | $\nearrow$ | $1$ | $\searrow$ | $0$ |

    **2.** Pour tout $x$, $f(-x) = e^{-(-x)^2} = e^{-x^2} = f(x)$ : $f$ est paire, sa courbe est symétrique par rapport à l'axe des ordonnées.

    *Cette courbe en « cloche » est celle de la loi normale, très utilisée en probabilités et en statistique.*

### Exercice 7 — Démontrer la formule de $(u^n)'$ <span class="etoiles">★★★</span>

Soit $u$ une fonction dérivable sur $I$. Démontrer par récurrence que pour tout entier $n \geq 1$, $(u^n)' = n\,u'\,u^{n-1}$, en utilisant seulement la formule de dérivation d'un produit.

??? success "Correction"
    Soit $\mathcal{P}(n)$ : « $(u^n)' = n\,u'\,u^{n-1}$ ».

    - Initialisation : $(u^1)' = u' = 1 \times u' \times u^0$. $\mathcal{P}(1)$ est vraie.
    - Hérédité : supposons $\mathcal{P}(n)$ vraie. On écrit $u^{n+1} = u \times u^n$ :

    $$(u^{n+1})' = u' \times u^n + u \times n\,u'\,u^{n-1} = u'u^n + n\,u'u^n = (n + 1)\,u'\,u^n.$$

    - Conclusion : $\mathcal{P}(n)$ est vraie pour tout $n \geq 1$.

---

## Thème 2 — Dérivée seconde et convexité

*Méthode associée : [Méthode 2](methodes.md#methode-2-etudier-la-convexite-dune-fonction).*

### Exercice 8 — Calculs de dérivées secondes <span class="etoiles">★</span>

Pour chaque fonction, calculer $f''$ et étudier la convexité.

1. $f(x) = x^3 - 6x^2 + 1$ sur $\mathbb{R}$
2. $g(x) = e^{2x}$ sur $\mathbb{R}$
3. $h(x) = \dfrac{1}{x}$ sur $]0 \,;\, +\infty[$, puis sur $]-\infty \,;\, 0[$

??? success "Correction"
    1. $f'(x) = 3x^2 - 12x$, $f''(x) = 6x - 12 = 6(x - 2)$. $f$ est concave sur $]-\infty \,;\, 2]$ et convexe sur $[2 \,;\, +\infty[$.
    2. $g'(x) = 2e^{2x}$, $g''(x) = 4e^{2x} > 0$ : $g$ est convexe sur $\mathbb{R}$.
    3. $h'(x) = -\frac{1}{x^2}$, $h''(x) = \frac{2}{x^3}$. $h$ est convexe sur $]0 \,;\, +\infty[$ (où $h'' > 0$) et concave sur $]-\infty \,;\, 0[$.

### Exercice 9 — Fonctions de référence <span class="etoiles">★</span>

Étudier la convexité de $x \mapsto \sqrt{x}$ sur $]0 \,;\, +\infty[$, de $x \mapsto e^{-x}$ sur $\mathbb{R}$ et de $x \mapsto x^4$ sur $\mathbb{R}$.

??? success "Correction"
    - $\sqrt{x}$ : $f'(x) = \frac{1}{2}x^{-1/2}$ et $f''(x) = -\frac{1}{4}x^{-3/2} < 0$ : concave.
    - $e^{-x}$ : $f'(x) = -e^{-x}$ et $f''(x) = e^{-x} > 0$ : convexe.
    - $x^4$ : $f''(x) = 12x^2 \geq 0$ : convexe sur $\mathbb{R}$.

### Exercice 10 — La fonction $x e^x$ <span class="etoiles">★★</span>

Soit $f(x) = x\,e^x$ sur $\mathbb{R}$.

1. Calculer $f'(x)$ et $f''(x)$.
2. Étudier la convexité de $f$ et donner les coordonnées de son point d'inflexion.

??? success "Correction"
    **1.** $f'(x) = e^x + xe^x = (x + 1)e^x$ et $f''(x) = e^x + (x + 1)e^x = (x + 2)e^x$.

    **2.** $f''(x)$ a le signe de $x + 2$. $f$ est concave sur $]-\infty \,;\, -2]$ et convexe sur $[-2 \,;\, +\infty[$. $f''$ s'annule en changeant de signe en $-2$ : le point $\left(-2 \,;\, -2e^{-2}\right)$ est un point d'inflexion.

### Exercice 11 — Deux points d'inflexion <span class="etoiles">★★</span>

Étudier la convexité de $f(x) = x^4 - 6x^2$ et préciser ses points d'inflexion.

??? success "Correction"
    $f'(x) = 4x^3 - 12x$ et $f''(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$.

    | $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $f''(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
    | convexité | | convexe | | concave | | convexe | |

    $f''$ change de signe en $-1$ et en $1$. Comme $f(\pm 1) = 1 - 6 = -5$, les points d'inflexion sont $(-1 \,;\, -5)$ et $(1 \,;\, -5)$.

### Exercice 12 — Un paramètre <span class="etoiles">★★</span>

Soit $a$ un réel et $f(x) = x^3 + a x^2 + 3x$. Déterminer $a$ pour que la courbe de $f$ ait un point d'inflexion d'abscisse $1$.

??? success "Correction"
    $f'(x) = 3x^2 + 2ax + 3$ et $f''(x) = 6x + 2a$. Il faut $f''(1) = 0$, soit $6 + 2a = 0$, donc $a = -3$.

    Réciproquement, pour $a = -3$, $f''(x) = 6x - 6 = 6(x - 1)$ change bien de signe en $1$ : c'est un point d'inflexion.

### Exercice 13 — Revenir à la définition <span class="etoiles">★★★</span>

On rappelle que $f$ est convexe sur $I$ si et seulement si, pour tous $a$, $b$ de $I$ et tout $t \in [0 \,;\, 1]$ : $f(ta + (1 - t)b) \leq t\,f(a) + (1 - t)\,f(b)$.

1. Montrer que $t a^2 + (1 - t) b^2 - \big(ta + (1 - t)b\big)^2 = t(1 - t)(a - b)^2$. En déduire, sans dériver, que $x \mapsto x^2$ est convexe sur $\mathbb{R}$.
2. Montrer que $x \mapsto |x|$ est convexe sur $\mathbb{R}$. Pourquoi ne peut-on pas utiliser $f''$ ici ?

??? success "Correction"
    **1.** On développe : $(ta + (1 - t)b)^2 = t^2a^2 + 2t(1 - t)ab + (1 - t)^2b^2$. Donc la différence vaut

    $$t(1 - t)a^2 + (1 - t)t\,b^2 - 2t(1 - t)ab = t(1 - t)(a^2 - 2ab + b^2) = t(1 - t)(a - b)^2,$$

    en utilisant $t - t^2 = t(1 - t)$ et $(1 - t) - (1 - t)^2 = t(1 - t)$. Pour $t \in [0 \,;\, 1]$, cette quantité est positive : $(ta + (1 - t)b)^2 \leq t a^2 + (1 - t) b^2$. La fonction carré est convexe.

    **2.** Par l'inégalité triangulaire, et comme $t \geq 0$ et $1 - t \geq 0$ :

    $$|ta + (1 - t)b| \leq |ta| + |(1 - t)b| = t|a| + (1 - t)|b|.$$

    Donc $|\cdot|$ est convexe. On ne peut pas utiliser $f''$ car la valeur absolue n'est **pas dérivable en $0$**. La définition par les sécantes est plus générale que le critère $f'' \geq 0$.

---

## Thème 3 — Points d'inflexion

*Méthode associée : [Méthode 3](methodes.md#methode-3-trouver-les-points-dinflexion).*

### Exercice 14 — Inflexion et tangente <span class="etoiles">★</span>

Soit $f(x) = x^3 - 3x^2 + 2$.

1. Montrer que la courbe de $f$ admet un unique point d'inflexion $I$.
2. Déterminer l'équation de la tangente en $I$.

??? success "Correction"
    **1.** $f'(x) = 3x^2 - 6x$, $f''(x) = 6x - 6$, qui s'annule en changeant de signe uniquement en $1$. Comme $f(1) = 0$, le point d'inflexion est $I(1 \,;\, 0)$.

    **2.** $f'(1) = 3 - 6 = -3$. La tangente a pour équation $y = -3(x - 1) + 0$, soit $y = -3x + 3$. La courbe la traverse en $I$.

### Exercice 15 — Inflexions de la gaussienne <span class="etoiles">★★</span>

Soit $f(x) = e^{-x^2}$.

1. Montrer que $f''(x) = (4x^2 - 2)\,e^{-x^2}$.
2. En déduire les points d'inflexion de la courbe.

??? success "Correction"
    **1.** $f'(x) = -2x\,e^{-x^2}$. Par la formule du produit :

    $$f''(x) = -2e^{-x^2} + (-2x)(-2x)e^{-x^2} = (4x^2 - 2)e^{-x^2}.$$

    **2.** $f''(x)$ a le signe de $4x^2 - 2 = 4\left(x - \frac{1}{\sqrt{2}}\right)\left(x + \frac{1}{\sqrt{2}}\right)$, qui change de signe en $\pm\frac{1}{\sqrt{2}}$. Comme $f\left(\pm\frac{1}{\sqrt{2}}\right) = e^{-1/2}$, les points d'inflexion sont $\left(\pm\frac{1}{\sqrt{2}} \,;\, e^{-1/2}\right)$.

    *La courbe est concave entre ces deux points, convexe à l'extérieur.*

### Exercice 16 — Courbe logistique <span class="etoiles">★★</span>

Soit $f(x) = \dfrac{1}{1 + e^{-x}}$ sur $\mathbb{R}$.

1. Montrer que $f'(x) = \dfrac{e^{-x}}{(1 + e^{-x})^2}$, puis que $f''(x) = \dfrac{e^{-x}(e^{-x} - 1)}{(1 + e^{-x})^3}$.
2. En déduire que la courbe a un point d'inflexion, dont on donnera les coordonnées.

??? success "Correction"
    **1.** $f = (1 + e^{-x})^{-1}$, donc $f'(x) = -(-e^{-x})(1 + e^{-x})^{-2} = \dfrac{e^{-x}}{(1 + e^{-x})^2}$.

    On dérive $f' = e^{-x} \times (1 + e^{-x})^{-2}$ comme un produit :

    $$f''(x) = -e^{-x}(1 + e^{-x})^{-2} + e^{-x} \times (-2)(-e^{-x})(1 + e^{-x})^{-3} = \frac{e^{-x}\left[-(1 + e^{-x}) + 2e^{-x}\right]}{(1 + e^{-x})^3} = \frac{e^{-x}(e^{-x} - 1)}{(1 + e^{-x})^3}.$$

    **2.** $f''(x)$ a le signe de $e^{-x} - 1$. Or $e^{-x} > 1 \iff -x > 0 \iff x < 0$. Donc $f'' > 0$ sur $]-\infty \,;\, 0[$ et $f'' < 0$ sur $]0 \,;\, +\infty[$ : $f''$ change de signe en $0$. Comme $f(0) = \frac{1}{2}$, le point d'inflexion est $\left(0 \,;\, \frac{1}{2}\right)$.

### Exercice 17 — Une condition nécessaire mais pas suffisante <span class="etoiles">★★★</span>

1. Montrer que l'origine est un point d'inflexion de la courbe de $x \mapsto x^3$.
2. Montrer que, pour $g(x) = x^4$, on a $g''(0) = 0$ mais que l'origine n'est pas un point d'inflexion.
3. Montrer que si $f$ est deux fois dérivable et si $A(a \,;\, f(a))$ est un point d'inflexion avec $f''$ continue, alors $f''(a) = 0$. *On admettra que si $f''(a) > 0$ et $f''$ est continue, alors $f'' > 0$ sur un intervalle autour de $a$.*

??? success "Correction"
    **1.** $f''(x) = 6x$ change de signe en $0$. La tangente en $0$ est l'axe $y = 0$, et $x^3$ est négatif à gauche, positif à droite : la courbe traverse bien sa tangente.

    **2.** $g''(x) = 12x^2$ donc $g''(0) = 0$. Mais $g'' \geq 0$ sur $\mathbb{R}$ : $g$ est convexe, donc sa courbe est au-dessus de sa tangente en $0$ (l'axe $y = 0$) des deux côtés. Elle ne la traverse pas.

    **3.** Raisonnons par l'absurde. Si $f''(a) > 0$, alors $f'' > 0$ sur un intervalle $J$ autour de $a$ : $f$ est convexe sur $J$, et la courbe est au-dessus de sa tangente en $a$ des deux côtés. Elle ne la traverse pas, ce qui contredit le fait que $A$ est un point d'inflexion. De même si $f''(a) < 0$. Donc $f''(a) = 0$.

    *Conclusion : $f''(a) = 0$ est **nécessaire** pour un point d'inflexion, mais **pas suffisant**.*

---

## Thème 4 — Inégalités de convexité

*Méthode associée : [Méthode 5](methodes.md#methode-5-demontrer-une-inegalite-par-convexite).*

### Exercice 18 — Une tangente à l'exponentielle <span class="etoiles">★</span>

Montrer que pour tout réel $x$ : $e^x \geq e\,x$. Pour quelle valeur de $x$ a-t-on égalité ?

??? success "Correction"
    $\exp$ est convexe sur $\mathbb{R}$. Sa tangente en $1$ a pour équation $y = e^1(x - 1) + e^1 = e\,x$. La courbe étant au-dessus de ses tangentes, $e^x \geq e\,x$ pour tout $x$. L'égalité a lieu au point de tangence, $x = 1$.

### Exercice 19 — Racine carrée et moyennes <span class="etoiles">★★</span>

1. Montrer que pour tout $x \geq 0$ : $\sqrt{x} \leq \dfrac{x + 1}{2}$.
2. En déduire que pour tous réels $a > 0$ et $b > 0$ : $\sqrt{ab} \leq \dfrac{a + b}{2}$.

??? success "Correction"
    **1.** La fonction racine carrée est concave sur $]0 \,;\, +\infty[$ (exercice 9). Sa tangente en $1$ : $y = \frac{1}{2}(x - 1) + 1 = \frac{x + 1}{2}$. La courbe est en dessous de ses tangentes, donc $\sqrt{x} \leq \frac{x + 1}{2}$ pour $x > 0$. Pour $x = 0$, l'inégalité $0 \leq \frac{1}{2}$ est évidente.

    **2.** On applique la question 1 à $x = \frac{a}{b} > 0$ : $\sqrt{\frac{a}{b}} \leq \frac{1}{2}\left(\frac{a}{b} + 1\right)$. On multiplie par $b > 0$, en écrivant $b\sqrt{\frac{a}{b}} = \sqrt{b^2 \cdot \frac{a}{b}} = \sqrt{ab}$ :

    $$\sqrt{ab} \leq \frac{a + b}{2}.$$

    *La moyenne géométrique est toujours inférieure à la moyenne arithmétique.*

### Exercice 20 — Encadrer l'exponentielle <span class="etoiles">★★</span>

1. Montrer que pour tout réel $x$ : $e^{-x} \geq 1 - x$.
2. En déduire que pour tout $x \in [0 \,;\, 1[$ : $1 + x \leq e^x \leq \dfrac{1}{1 - x}$.
3. Donner un encadrement de $e^{0{,}1}$.

??? success "Correction"
    **1.** On applique $e^X \geq 1 + X$ (cours) avec $X = -x$.

    **2.** La minoration est $e^x \geq 1 + x$. Pour $x \in [0 \,;\, 1[$, $1 - x > 0$, et la question 1 donne $e^{-x} \geq 1 - x > 0$. En passant aux inverses (la fonction inverse est décroissante sur $]0 \,;\, +\infty[$) : $e^x \leq \dfrac{1}{1 - x}$.

    **3.** $1{,}1 \leq e^{0{,}1} \leq \dfrac{1}{0{,}9} \approx 1{,}1111$. (Valeur réelle : $e^{0{,}1} \approx 1{,}10517$.)

### Exercice 21 — Inégalité du milieu <span class="etoiles">★★</span>

1. Justifier que pour tous réels $a$ et $b$ : $e^{\frac{a + b}{2}} \leq \dfrac{e^a + e^b}{2}$.
2. En posant $x = e^a$ et $y = e^b$, en déduire que $\sqrt{xy} \leq \dfrac{x + y}{2}$ pour tous les réels $x$, $y$ qui s'écrivent sous cette forme.

??? success "Correction"
    **1.** $\exp$ est convexe, et l'inégalité du milieu (cours, § 6) donne le résultat.

    **2.** $e^{\frac{a + b}{2}} = \sqrt{e^{a + b}} = \sqrt{e^a e^b} = \sqrt{xy}$, car $\left(e^{\frac{a+b}{2}}\right)^2 = e^{a + b}$ et $e^{\frac{a+b}{2}} > 0$. L'inégalité devient $\sqrt{xy} \leq \frac{x + y}{2}$.

    *Avec le logarithme (chapitre 5), on verra que **tout** réel strictement positif s'écrit $e^a$ : on retrouve ainsi le résultat de l'exercice 19 par une autre méthode.*

### Exercice 22 — Encadrer le nombre $e$ <span class="etoiles">★★★</span>

1. En utilisant $e^x \geq 1 + x$ avec $x = \frac{1}{n}$, montrer que pour tout entier $n \geq 1$ : $\left(1 + \frac{1}{n}\right)^n \leq e$.
2. En utilisant $e^{-x} \geq 1 - x$ avec $x = \frac{1}{n + 1}$, montrer que $e \leq \left(1 + \frac{1}{n}\right)^{n+1}$.
3. En déduire un encadrement de $e$ pour $n = 100$ (à la calculatrice), puis la limite de la suite $u_n = \left(1 + \frac{1}{n}\right)^n$. *Indication : écrire $\left(1 + \frac{1}{n}\right)^{n+1} = \left(1 + \frac{1}{n}\right)^{n} \left(1 + \frac{1}{n}\right)$.*

??? success "Correction"
    **1.** $1 + \frac{1}{n} \leq e^{1/n}$. Les deux membres sont positifs, et la fonction $t \mapsto t^n$ est croissante sur $[0 \,;\, +\infty[$, donc $\left(1 + \frac{1}{n}\right)^n \leq \left(e^{1/n}\right)^n = e$.

    **2.** $1 - \frac{1}{n + 1} = \frac{n}{n + 1} \leq e^{-\frac{1}{n+1}}$. En passant aux inverses (nombres positifs) : $\frac{n + 1}{n} \geq e^{\frac{1}{n+1}}$, soit $1 + \frac{1}{n} \geq e^{\frac{1}{n+1}}$. On élève à la puissance $n + 1$ : $\left(1 + \frac{1}{n}\right)^{n+1} \geq e$.

    **3.** Pour $n = 100$ : $1{,}01^{100} \approx 2{,}7048 \leq e \leq 1{,}01^{101} \approx 2{,}7319$.

    D'après la question 2 et l'indication : $u_n \geq \dfrac{e}{1 + \frac{1}{n}}$. Donc

    $$\frac{e}{1 + \frac{1}{n}} \leq u_n \leq e.$$

    La borne de gauche tend vers $e$ : par les gendarmes, $\displaystyle\lim_{n\to+\infty} \left(1 + \frac{1}{n}\right)^n = e$.

---

## Thème 5 — Études de fonctions complètes

### Exercice 23 — La fonction $(x - 1)e^x$ <span class="etoiles">★★</span>

Soit $f(x) = (x - 1)e^x$ sur $\mathbb{R}$.

1. Déterminer les limites de $f$ en $-\infty$ et en $+\infty$.
2. Étudier les variations de $f$.
3. Étudier la convexité de $f$ et préciser le point d'inflexion.

??? success "Correction"
    **1.** En $-\infty$ : $f(x) = xe^x - e^x$. Par croissance comparée $xe^x \to 0$, et $e^x \to 0$ : $f(x) \to 0$. En $+\infty$ : $(x - 1) \to +\infty$ et $e^x \to +\infty$, donc $f(x) \to +\infty$.

    **2.** $f'(x) = e^x + (x - 1)e^x = x\,e^x$, du signe de $x$. $f$ est décroissante sur $]-\infty \,;\, 0]$ et croissante sur $[0 \,;\, +\infty[$, avec un minimum $f(0) = -1$.

    **3.** $f''(x) = e^x + xe^x = (x + 1)e^x$, du signe de $x + 1$. $f$ est concave sur $]-\infty \,;\, -1]$ et convexe sur $[-1 \,;\, +\infty[$. Point d'inflexion : $\left(-1 \,;\, -2e^{-1}\right)$.

### Exercice 24 — La fonction $x + e^{-x}$ <span class="etoiles">★★</span>

Soit $f(x) = x + e^{-x}$ sur $\mathbb{R}$.

1. Étudier la convexité de $f$.
2. Étudier les variations de $f$ et en déduire que $x + e^{-x} \geq 1$ pour tout réel $x$.
3. Montrer que la droite $y = x$ est asymptote à la courbe en $+\infty$.

??? success "Correction"
    **1.** $f'(x) = 1 - e^{-x}$ et $f''(x) = e^{-x} > 0$ : $f$ est convexe sur $\mathbb{R}$.

    **2.** $f'(x) \geq 0 \iff e^{-x} \leq 1 \iff -x \leq 0 \iff x \geq 0$ (car $\exp$ est strictement croissante et $e^0 = 1$). $f$ est décroissante puis croissante, de minimum $f(0) = 1$. Donc $f(x) \geq 1$.

    **3.** $f(x) - x = e^{-x} \to 0$ en $+\infty$ : la droite $y = x$ est asymptote oblique, et la courbe est au-dessus.

### Exercice 25 — Trois points d'inflexion <span class="etoiles">★★★</span>

Soit $f(x) = \dfrac{x}{1 + x^2}$ sur $\mathbb{R}$.

1. Montrer que $f'(x) = \dfrac{1 - x^2}{(1 + x^2)^2}$ et dresser le tableau de variations de $f$.
2. Montrer que $f''(x) = \dfrac{2x(x^2 - 3)}{(1 + x^2)^3}$.
3. En déduire que la courbe a trois points d'inflexion, et qu'ils sont alignés.

??? success "Correction"
    **1.** Formule du quotient : $f'(x) = \dfrac{(1 + x^2) - x \times 2x}{(1 + x^2)^2} = \dfrac{1 - x^2}{(1 + x^2)^2}$, du signe de $1 - x^2$.

    Les limites en $\pm\infty$ valent $0$ (termes dominants $\frac{x}{x^2}$).

    | $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
    | $f(x)$ | $0$ | $\searrow$ | $-\frac{1}{2}$ | $\nearrow$ | $\frac{1}{2}$ | $\searrow$ | $0$ |

    **2.** On dérive $f' = \dfrac{u}{v}$ avec $u = 1 - x^2$, $u' = -2x$, $v = (1 + x^2)^2$, $v' = 2 \times 2x(1 + x^2) = 4x(1 + x^2)$ :

    $$f''(x) = \frac{-2x(1 + x^2)^2 - (1 - x^2) \times 4x(1 + x^2)}{(1 + x^2)^4} = \frac{-2x(1 + x^2) - 4x(1 - x^2)}{(1 + x^2)^3}.$$

    Le numérateur vaut $-2x - 2x^3 - 4x + 4x^3 = 2x^3 - 6x = 2x(x^2 - 3)$.

    **3.** $f''(x)$ a le signe de $x(x - \sqrt{3})(x + \sqrt{3})$, qui change de signe en $-\sqrt{3}$, $0$ et $\sqrt{3}$. Les points d'inflexion sont

    $$\left(-\sqrt{3} \,;\, -\tfrac{\sqrt{3}}{4}\right), \qquad (0 \,;\, 0), \qquad \left(\sqrt{3} \,;\, \tfrac{\sqrt{3}}{4}\right),$$

    car $f(\sqrt{3}) = \frac{\sqrt{3}}{4}$ et $f$ est impaire. Ils sont tous sur la droite d'équation $y = \frac{1}{4}x$ : ils sont alignés.

### Exercice 26 — Position par rapport à une tangente <span class="etoiles">★★</span>

Soit $f(x) = x^3$ et $T$ sa tangente au point d'abscisse $1$.

1. Déterminer une équation de $T$.
2. Vérifier que $x^3 - 3x + 2 = (x - 1)^2(x + 2)$ et en déduire la position de la courbe par rapport à $T$.
3. Ce résultat est-il cohérent avec la convexité de $f$ ?

??? success "Correction"
    **1.** $f(1) = 1$ et $f'(1) = 3$ : $T : y = 3(x - 1) + 1 = 3x - 2$.

    **2.** $(x - 1)^2(x + 2) = (x^2 - 2x + 1)(x + 2) = x^3 - 3x + 2$. Donc $f(x) - (3x - 2) = (x - 1)^2(x + 2)$, du signe de $x + 2$. La courbe est au-dessus de $T$ pour $x \geq -2$ et en dessous pour $x \leq -2$.

    **3.** Oui. $f$ est convexe sur $[0 \,;\, +\infty[$, donc la courbe est au-dessus de $T$ sur cet intervalle. Mais la convexité ne dit rien **en dehors** de l'intervalle : sur $]-\infty \,;\, 0]$, $f$ est concave, et la courbe finit par passer sous $T$.

---

## Thème 6 — Approfondissement

### Exercice 27 — Vrai ou faux ? <span class="etoiles">★★</span>

Justifier chaque réponse.

1. Une fonction convexe sur $\mathbb{R}$ est croissante.
2. La somme de deux fonctions convexes sur $I$ est convexe sur $I$.
3. Le produit de deux fonctions convexes sur $\mathbb{R}$ est convexe sur $\mathbb{R}$.
4. Si $f$ est deux fois dérivable, convexe et positive sur $I$, alors $f^2$ est convexe sur $I$.
5. Si $f$ est convexe sur $[0 \,;\, 1]$ et convexe sur $[1 \,;\, 2]$, alors $f$ est convexe sur $[0 \,;\, 2]$.

??? success "Correction"
    **1. Faux.** $x \mapsto x^2$ est convexe mais décroissante sur $]-\infty \,;\, 0]$.

    **2. Vrai.** Si $f$ et $g$ vérifient l'inégalité des sécantes, on peut les additionner : $f + g$ la vérifie aussi. (Ou bien $(f + g)'' = f'' + g'' \geq 0$ si elles sont deux fois dérivables.)

    **3. Faux.** $x \mapsto x$ (affine, donc convexe) et $x \mapsto x^2$ sont convexes, mais leur produit $x^3$ est concave sur $]-\infty \,;\, 0]$.

    **4. Vrai.** $(f^2)' = 2ff'$ et $(f^2)'' = 2f'^2 + 2ff''$. Les deux termes sont positifs (car $f \geq 0$ et $f'' \geq 0$), donc $(f^2)'' \geq 0$.

    **5. Faux.** $f(x) = -|x - 1|$ est affine sur $[0 \,;\, 1]$ (elle vaut $x - 1$) et sur $[1 \,;\, 2]$ (elle vaut $1 - x$), donc convexe sur chacun. Mais sur $[0 \,;\, 2]$, la sécante entre $0$ et $2$ est la droite $y = -1$, et $f(1) = 0 > -1$ : la courbe passe au-dessus de cette sécante. $f$ n'est pas convexe sur $[0 \,;\, 2]$.

### Exercice 28 — Convexité et minimum <span class="etoiles">★★★</span>

1. Soit $f$ convexe et dérivable sur $I$, et $a \in I$ tel que $f'(a) = 0$. Montrer que $f(a)$ est le **minimum** de $f$ sur $I$.
2. Application : montrer que pour tout réel $x$, $e^x + e^{-x} \geq 2$.

??? success "Correction"
    **1.** La courbe de $f$ est au-dessus de sa tangente en $a$, dont l'équation est $y = f'(a)(x - a) + f(a) = f(a)$, une droite horizontale. Donc $f(x) \geq f(a)$ pour tout $x \in I$.

    *Pour une fonction convexe, un point où la dérivée s'annule est donc automatiquement un minimum global. Ce résultat est au cœur des méthodes d'optimisation, en économie comme en intelligence artificielle.*

    **2.** Soit $g(x) = e^x + e^{-x}$. $g'(x) = e^x - e^{-x}$ et $g''(x) = e^x + e^{-x} > 0$ : $g$ est convexe. De plus $g'(0) = 1 - 1 = 0$. D'après la question 1, $g(x) \geq g(0) = 2$ pour tout $x$.
