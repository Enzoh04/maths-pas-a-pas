# Cours — Limites de fonctions

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, $f$ est une fonction définie sur un ensemble $D_f$, et $\mathcal{C}_f$ est sa courbe représentative dans un repère.

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Limite d'une fonction en l'infini

### 1.1 Limite infinie en l'infini

Les définitions sont les mêmes que pour les suites, en remplaçant « à partir d'un certain rang » par « pour $x$ assez grand ».

!!! definition "Définition"
    On dit que $f$ **tend vers $+\infty$ en $+\infty$** si, pour tout réel $A$, il existe un réel $B$ tel que :

    $$\text{pour tout } x \in D_f \text{ tel que } x > B, \quad f(x) > A.$$

    Autrement dit, l'intervalle $]A \,;\, +\infty[$ contient toutes les valeurs $f(x)$ dès que $x$ est assez grand. On note $\displaystyle\lim_{x \to +\infty} f(x) = +\infty$.

On définit de la même façon $\displaystyle\lim_{x \to +\infty} f(x) = -\infty$ (avec $f(x) < A$), et les limites en $-\infty$ (avec « $x < B$ »).

**Exemple.** $\displaystyle\lim_{x\to+\infty} x^2 = +\infty$ : pour $A > 0$, dès que $x > \sqrt{A}$, on a $x^2 > A$.

### 1.2 Limite finie en l'infini, asymptote horizontale

!!! definition "Définition"
    On dit que $f$ **tend vers le réel $\ell$ en $+\infty$** si, pour tout $\varepsilon > 0$, il existe un réel $B$ tel que :

    $$\text{pour tout } x \in D_f \text{ tel que } x > B, \quad |f(x) - \ell| < \varepsilon.$$

    On note $\displaystyle\lim_{x \to +\infty} f(x) = \ell$. Dans ce cas, la droite d'équation $y = \ell$ est **asymptote horizontale** à $\mathcal{C}_f$ en $+\infty$.

Même définition en $-\infty$, avec « $x < B$ ».

**Interprétation.** Quand $x$ devient grand, l'écart vertical entre la courbe et la droite $y = \ell$ devient aussi petit qu'on veut.

**Exemple.** $\displaystyle\lim_{x\to+\infty} \left(2 + \frac{1}{x}\right) = 2$ : la droite $y = 2$ est asymptote horizontale en $+\infty$. Ici la courbe est **au-dessus** de l'asymptote, car $\frac{1}{x} > 0$ pour $x > 0$.

!!! warning "Une courbe peut couper son asymptote"
    $f(x) = \dfrac{\sin x}{x}$ tend vers $0$ en $+\infty$, et sa courbe coupe la droite $y = 0$ en tous les points $x = k\pi$.

!!! propriete "Unicité de la limite"
    Si $f$ admet une limite en $+\infty$ (finie ou infinie), cette limite est unique. De même en $-\infty$ et en un réel $a$.

??? demoplus "Démonstration — pour aller plus loin"
    C'est la même démonstration que pour les suites (chapitre 1). Si $f$ tendait vers $\ell$ et vers $\ell' > \ell$, on poserait $d = \ell' - \ell$. Pour $x$ assez grand, $f(x)$ serait à la fois dans $\left]\ell - \frac{d}{3} \,;\, \ell + \frac{d}{3}\right[$ et dans $\left]\ell' - \frac{d}{3} \,;\, \ell' + \frac{d}{3}\right[$, qui sont disjoints. C'est impossible.

---

## 2. Limite d'une fonction en un réel $a$

Ici, $a$ est un réel qui est une borne de $D_f$ (par exemple $a = 0$ pour $f(x) = \frac{1}{x}$) : $f$ n'est pas forcément définie en $a$, mais elle est définie « tout près » de $a$.

### 2.1 Limite infinie en $a$, asymptote verticale

!!! definition "Définition"
    On dit que $f$ **tend vers $+\infty$ quand $x$ tend vers $a$** si, pour tout réel $A$, il existe un réel $\delta > 0$ tel que :

    $$\text{pour tout } x \in D_f \text{ tel que } |x - a| < \delta, \quad f(x) > A.$$

    On note $\displaystyle\lim_{x \to a} f(x) = +\infty$. Dans ce cas, la droite d'équation $x = a$ est **asymptote verticale** à $\mathcal{C}_f$.

**Limites à gauche et à droite.** Souvent, $f$ n'a pas le même comportement des deux côtés de $a$. On parle alors de :

- **limite à droite** en $a$, notée $\displaystyle\lim_{\substack{x \to a \\ x > a}} f(x)$ ou $\displaystyle\lim_{x \to a^+} f(x)$, quand on ne considère que les $x > a$ ;
- **limite à gauche**, notée $\displaystyle\lim_{\substack{x \to a \\ x < a}} f(x)$ ou $\displaystyle\lim_{x \to a^-} f(x)$, quand on ne considère que les $x < a$.

Une seule limite infinie, à gauche ou à droite, suffit pour avoir une asymptote verticale.

**Exemple.** $\displaystyle\lim_{x \to 0^+} \frac{1}{x} = +\infty$ et $\displaystyle\lim_{x \to 0^-} \frac{1}{x} = -\infty$. La droite $x = 0$ (l'axe des ordonnées) est asymptote verticale à la courbe de la fonction inverse.

### 2.2 Limite finie en $a$

!!! definition "Définition"
    On dit que $f$ **tend vers le réel $\ell$ quand $x$ tend vers $a$** si, pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que :

    $$\text{pour tout } x \in D_f \text{ tel que } |x - a| < \delta, \quad |f(x) - \ell| < \varepsilon.$$

**Exemple.** Pour $x \neq 2$, $\dfrac{x^2 - 4}{x - 2} = x + 2$, qui s'approche de $4$ quand $x$ s'approche de $2$. Donc $\displaystyle\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 4$. Cette notion sera au cœur du chapitre Continuité.

---

## 3. Limites des fonctions de référence

!!! propriete "Limites à connaître"
    Pour tout entier $n \geq 1$ :

    | | en $+\infty$ | en $-\infty$ | en $0$ |
    |---|---|---|---|
    | $x^n$ | $+\infty$ | $+\infty$ si $n$ pair, $-\infty$ si $n$ impair | $0$ |
    | $\dfrac{1}{x^n}$ | $0$ | $0$ | $0^+$ : $+\infty$ ; $0^-$ : $+\infty$ si $n$ pair, $-\infty$ si $n$ impair |
    | $\sqrt{x}$ | $+\infty$ | — | $0$ |
    | $\dfrac{1}{\sqrt{x}}$ | $0$ | — | $0^+$ : $+\infty$ |

??? demoplus "Démonstration — pour aller plus loin"
    **$x^n$ en $+\infty$.** Soit $A > 0$. Pour $x > \max(1, A)$, on a $x^n \geq x > A$ (car $x \geq 1$ entraîne $x^n \geq x$).

    **$x^n$ en $-\infty$.** On écrit $x^n = (-1)^n (-x)^n$. Quand $x \to -\infty$, $-x \to +\infty$ donc $(-x)^n \to +\infty$. Le signe est donné par $(-1)^n$.

    **$\frac{1}{x^n}$ en $+\infty$.** Soit $\varepsilon > 0$. Pour $x > \max\left(1, \frac{1}{\varepsilon}\right)$ : $0 < \frac{1}{x^n} \leq \frac{1}{x} < \varepsilon$.

    **$\frac{1}{x^n}$ en $0^+$.** Soit $A > 0$. Pour $0 < x < \min\left(1, \frac{1}{A}\right)$ : $0 < x^n \leq x < \frac{1}{A}$, donc $\frac{1}{x^n} > A$. En $0^-$, on écrit $\frac{1}{x^n} = \frac{(-1)^n}{(-x)^n}$ avec $-x \to 0^+$.

    **$\sqrt{x}$ en $+\infty$.** Pour $A > 0$ et $x > A^2$ : $\sqrt{x} > A$, car la racine carrée est strictement croissante.

    **$\frac{1}{\sqrt{x}}$ en $0^+$.** Pour $A > 0$ et $0 < x < \frac{1}{A^2}$ : $\sqrt{x} < \frac{1}{A}$, donc $\frac{1}{\sqrt{x}} > A$.

    Les limites en $0$ de $x^n$ et $\sqrt{x}$ découlent de la continuité de ces fonctions, étudiée au chapitre 4.

---

## 4. Opérations sur les limites

!!! theoreme "Mêmes règles que pour les suites"
    Les tableaux de somme, de produit et de quotient du [chapitre 1](../suites/cours.md#3-operations-sur-les-limites) restent valables pour les fonctions, que $x$ tende vers $+\infty$, vers $-\infty$ ou vers un réel $a$. Les **formes indéterminées** sont les mêmes :

    $$\infty - \infty \qquad 0 \times \infty \qquad \frac{\infty}{\infty} \qquad \frac{0}{0}$$

??? demoplus "Démonstration — pour aller plus loin"
    Les démonstrations sont exactement celles du chapitre 1 : il suffit de remplacer « à partir d'un certain rang $N$ » par « pour $x > B$ » (en $+\infty$) ou par « pour $|x - a| < \delta$ » (en $a$). Par exemple, pour la somme de deux limites finies en $+\infty$ :

    soit $\varepsilon > 0$. Il existe $B_1$ tel que $|f(x) - \ell| < \frac{\varepsilon}{2}$ pour $x > B_1$, et $B_2$ tel que $|g(x) - \ell'| < \frac{\varepsilon}{2}$ pour $x > B_2$. Pour $x > \max(B_1, B_2)$ :

    $$|f(x) + g(x) - (\ell + \ell')| \leq |f(x) - \ell| + |g(x) - \ell'| < \varepsilon.$$

**Limite à gauche ou à droite d'un quotient.** Quand le dénominateur tend vers $0$, il faut connaître son **signe** : on note $0^+$ s'il tend vers $0$ en restant positif, et $0^-$ s'il reste négatif. Par exemple, $\dfrac{3}{0^+} \to +\infty$ et $\dfrac{3}{0^-} \to -\infty$.

**Exemple.** $\displaystyle\lim_{x \to 1^+} \frac{2x + 1}{x - 1}$ : le numérateur tend vers $3$, et pour $x > 1$, $x - 1 \to 0^+$. Donc la limite est $+\infty$.

!!! propriete "Polynômes et fractions rationnelles en l'infini"
    - En $+\infty$ ou $-\infty$, un **polynôme** a la même limite que son **terme de plus haut degré**.
    - En $+\infty$ ou $-\infty$, une **fraction rationnelle** (quotient de deux polynômes) a la même limite que le **quotient des termes de plus haut degré**.

    **Exemple.** $\displaystyle\lim_{x \to -\infty} \frac{3x^2 - x + 1}{1 - 2x} = \lim_{x \to -\infty} \frac{3x^2}{-2x} = \lim_{x \to -\infty} \left(-\frac{3}{2}x\right) = +\infty$.

??? demoplus "Démonstration — pour aller plus loin"
    Soit $P(x) = a_p x^p + a_{p-1} x^{p-1} + \dots + a_0$ avec $a_p \neq 0$. Pour $x \neq 0$, on factorise par le terme dominant :

    $$P(x) = a_p x^p \left(1 + \frac{a_{p-1}}{a_p}\cdot\frac{1}{x} + \dots + \frac{a_0}{a_p}\cdot\frac{1}{x^p}\right).$$

    Chaque terme $\frac{1}{x^k}$ tend vers $0$ en $\pm\infty$, donc la parenthèse tend vers $1$. Par produit, $P(x)$ a la même limite que $a_p x^p$.

    Pour un quotient $\dfrac{P(x)}{Q(x)}$ avec $Q(x) = b_q x^q + \dots$, on factorise de même le numérateur et le dénominateur :

    $$\frac{P(x)}{Q(x)} = \frac{a_p x^p}{b_q x^q} \times \frac{1 + \dots}{1 + \dots},$$

    et le second quotient tend vers $1$.

!!! warning "Uniquement en l'infini"
    Cette règle est **fausse** en un réel $a$. Par exemple, en $0$, $x^2 + 3$ tend vers $3$, et non vers la limite de $x^2$.

---

## 5. Composition de limites

!!! definition "Rappel : fonction composée"
    Si $u$ est définie sur $I$, à valeurs dans $J$, et si $v$ est définie sur $J$, la **composée** $v \circ u$ est la fonction définie sur $I$ par $(v \circ u)(x) = v(u(x))$.

    **Exemple.** $h(x) = \sqrt{x^2 + 1}$ est la composée de $u(x) = x^2 + 1$ suivie de $v(X) = \sqrt{X}$.

!!! theoreme "Limite d'une fonction composée"
    Soit $a$, $b$, $c$ des réels ou $+\infty$ ou $-\infty$. Si

    $$\lim_{x \to a} u(x) = b \quad \text{et} \quad \lim_{X \to b} v(X) = c, \quad \text{alors} \quad \lim_{x \to a} v(u(x)) = c.$$

??? demoplus "Démonstration — pour aller plus loin (cas $a = +\infty$, $b = +\infty$, $c = \ell$ réel)"
    Soit $\varepsilon > 0$.

    - Comme $\displaystyle\lim_{X \to +\infty} v(X) = \ell$, il existe $B'$ tel que : pour tout $X > B'$, $|v(X) - \ell| < \varepsilon$.
    - Comme $\displaystyle\lim_{x \to +\infty} u(x) = +\infty$, en prenant $A = B'$, il existe $B$ tel que : pour tout $x > B$, $u(x) > B'$.

    Pour $x > B$, on peut donc appliquer la première propriété à $X = u(x)$ : $|v(u(x)) - \ell| < \varepsilon$. Ainsi, $v(u(x)) \to \ell$.

    Les autres cas se démontrent exactement de la même façon : on « enchaîne » les deux définitions, en partant de la limite finale.

**Exemple.** $\displaystyle\lim_{x \to +\infty} \sqrt{4 + \frac{1}{x}}$. On pose $X = 4 + \frac{1}{x}$, qui tend vers $4$ ; et $\displaystyle\lim_{X \to 4} \sqrt{X} = 2$. Donc la limite vaut $2$.

!!! propriete "Composée d'une suite et d'une fonction"
    Si $\displaystyle\lim_{n\to+\infty} u_n = a$ et si $\displaystyle\lim_{x \to a} f(x) = \ell$ ($a$ et $\ell$ réels ou infinis), alors $\displaystyle\lim_{n\to+\infty} f(u_n) = \ell$.

??? demoplus "Démonstration — pour aller plus loin (cas $a$ et $\ell$ réels)"
    Soit $\varepsilon > 0$. Il existe $\delta > 0$ tel que : pour $x \in D_f$ avec $|x - a| < \delta$, $|f(x) - \ell| < \varepsilon$. Comme $u_n \to a$, il existe un rang $N$ à partir duquel $|u_n - a| < \delta$. Pour $n \geq N$, on a donc $|f(u_n) - \ell| < \varepsilon$.

**Exemple.** $\displaystyle\lim_{n \to +\infty} \sqrt{9 + \frac{1}{n}} = \sqrt{9} = 3$.

---

## 6. Théorèmes de comparaison

!!! theoreme "Théorèmes de comparaison et des gendarmes"
    Soit $f$, $g$, $h$ trois fonctions et $a$ un réel ou $\pm\infty$. On suppose les inégalités vraies **pour $x$ assez proche de $a$** (ou assez grand si $a = +\infty$).

    1. Si $f(x) \leq g(x)$ et $\displaystyle\lim_{x\to a} f(x) = +\infty$, alors $\displaystyle\lim_{x\to a} g(x) = +\infty$.
    2. Si $f(x) \leq g(x)$ et $\displaystyle\lim_{x\to a} g(x) = -\infty$, alors $\displaystyle\lim_{x\to a} f(x) = -\infty$.
    3. **Gendarmes** : si $f(x) \leq g(x) \leq h(x)$ et si $f$ et $h$ ont la **même limite finie** $\ell$ en $a$, alors $\displaystyle\lim_{x\to a} g(x) = \ell$.

??? demoplus "Démonstration — pour aller plus loin (en $+\infty$)"
    **Point 1.** Il existe $B_0$ tel que $f(x) \leq g(x)$ pour $x > B_0$. Soit $A$ un réel : il existe $B_1$ tel que $f(x) > A$ pour $x > B_1$. Pour $x > \max(B_0, B_1)$, $g(x) \geq f(x) > A$.

    **Point 2.** On applique le point 1 à $-g \leq -f$.

    **Point 3.** Soit $\varepsilon > 0$. Pour $x$ assez grand, on a à la fois $f(x) \leq g(x) \leq h(x)$, $f(x) > \ell - \varepsilon$ et $h(x) < \ell + \varepsilon$. Donc $\ell - \varepsilon < g(x) < \ell + \varepsilon$, soit $|g(x) - \ell| < \varepsilon$.

    En un réel $a$, on remplace « $x > B$ » par « $|x - a| < \delta$ » et on prend le plus petit des $\delta$.

**Exemple.** $\displaystyle\lim_{x\to+\infty} \frac{\cos x}{x}$. Pour $x > 0$, $-\frac{1}{x} \leq \frac{\cos x}{x} \leq \frac{1}{x}$, et les deux bornes tendent vers $0$. Par les gendarmes, la limite est $0$.

---

## 7. La fonction exponentielle

### 7.1 Rappels de Première

!!! propriete "Ce qu'on sait de l'exponentielle"
    La fonction exponentielle est l'unique fonction $f$ dérivable sur $\mathbb{R}$ telle que $f' = f$ et $f(0) = 1$. On la note $x \mapsto e^x$. Pour tous réels $a$, $b$ et tout entier $n$ :

    $$e^{a+b} = e^a e^b, \qquad e^{-a} = \frac{1}{e^a}, \qquad (e^a)^n = e^{na}, \qquad e^a > 0.$$

    Elle est strictement croissante sur $\mathbb{R}$ (car sa dérivée $e^x$ est strictement positive).

??? admis "Pourquoi l'existence de l'exponentielle est admise"
    Que deux fonctions vérifiant $f' = f$ et $f(0) = 1$ soient égales se démontre en Première. En revanche, **l'existence** d'une telle fonction est admise. La démontrer demande de construire la fonction : par exemple comme somme d'une série $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$ (séries entières, L2 ou deuxième année de prépa), ou comme réciproque du logarithme défini par une intégrale (L1). On peut aussi utiliser le théorème de Cauchy-Lipschitz sur les équations différentielles (L2-L3).

    Au lycée, on peut quand même s'en approcher : la méthode d'Euler, vue en Première, construit des approximations de plus en plus précises de cette fonction.

### 7.2 Une inégalité fondamentale

!!! propriete "Inégalité de convexité"
    Pour tout réel $x$ : $e^x \geq 1 + x$.

??? demo "Démonstration — au programme du bac (elle sert pour la limite en $+\infty$)"
    On pose $g(x) = e^x - x - 1$, dérivable sur $\mathbb{R}$, avec $g'(x) = e^x - 1$.

    Comme l'exponentielle est strictement croissante et $e^0 = 1$ : $g'(x) < 0$ si $x < 0$, et $g'(x) > 0$ si $x > 0$. Donc $g$ est décroissante sur $]-\infty \,;\, 0]$ et croissante sur $[0 \,;\, +\infty[$ : elle admet un minimum en $0$, égal à $g(0) = 1 - 0 - 1 = 0$.

    Ainsi $g(x) \geq 0$ pour tout $x$, c'est-à-dire $e^x \geq 1 + x$.

Géométriquement : la courbe de l'exponentielle est au-dessus de sa tangente en $0$, la droite $y = x + 1$.

### 7.3 Limites en $+\infty$ et $-\infty$

!!! theoreme "Limites de l'exponentielle"
    $$\lim_{x \to +\infty} e^x = +\infty \qquad\qquad \lim_{x \to -\infty} e^x = 0$$

    La droite $y = 0$ est asymptote horizontale à la courbe de l'exponentielle en $-\infty$.

??? demo "Démonstration — au programme du bac"
    **En $+\infty$.** Pour tout $x$, $e^x \geq 1 + x$. Comme $\displaystyle\lim_{x\to+\infty} (1 + x) = +\infty$, le théorème de comparaison donne $\displaystyle\lim_{x\to+\infty} e^x = +\infty$.

    **En $-\infty$.** Pour tout $x$, $e^x = \dfrac{1}{e^{-x}}$. On pose $X = -x$ : quand $x \to -\infty$, $X \to +\infty$, donc $e^{X} \to +\infty$ (par composition). Par quotient, $\dfrac{1}{e^{-x}} \to 0$. Donc $\displaystyle\lim_{x\to-\infty} e^x = 0$.

### 7.4 Croissances comparées

Quand $x \to +\infty$, $e^x$ et $x^n$ tendent tous deux vers $+\infty$ : le quotient $\frac{e^x}{x^n}$ est une forme indéterminée. Le théorème suivant dit que **l'exponentielle l'emporte**.

!!! theoreme "Croissances comparées"
    Pour tout entier naturel $n$ :

    $$\lim_{x \to +\infty} \frac{e^x}{x^n} = +\infty \qquad\qquad \lim_{x \to -\infty} x^n e^x = 0$$

    En particulier : $\displaystyle\lim_{x \to +\infty} \frac{e^x}{x} = +\infty$, $\displaystyle\lim_{x \to +\infty} x e^{-x} = 0$ et $\displaystyle\lim_{x \to -\infty} x e^x = 0$.

??? demo "Démonstration — au programme du bac (limite en $+\infty$)"
    **Étape 1 : cas $n = 1$.** On pose $h(x) = e^x - \dfrac{x^2}{2}$ sur $[0 \,;\, +\infty[$. Alors $h'(x) = e^x - x$. D'après l'inégalité $e^x \geq 1 + x$, on a $h'(x) \geq 1 > 0$. Donc $h$ est croissante sur $[0 \,;\, +\infty[$, et $h(x) \geq h(0) = 1 > 0$.

    Ainsi, pour $x > 0$, $e^x > \dfrac{x^2}{2}$, donc $\dfrac{e^x}{x} > \dfrac{x}{2}$. Comme $\dfrac{x}{2} \to +\infty$, par comparaison $\displaystyle\lim_{x\to+\infty} \frac{e^x}{x} = +\infty$.

    **Étape 2 : cas général $n \geq 1$.** Pour $x > 0$, en posant $X = \dfrac{x}{n}$, on a $x = nX$ et $e^x = \left(e^{X}\right)^n$, donc :

    $$\frac{e^x}{x^n} = \frac{\left(e^X\right)^n}{n^n X^n} = \frac{1}{n^n} \left(\frac{e^X}{X}\right)^n.$$

    Quand $x \to +\infty$, $X \to +\infty$, donc $\dfrac{e^X}{X} \to +\infty$ (étape 1), puis sa puissance $n$-ième tend vers $+\infty$. Comme $\frac{1}{n^n} > 0$ est constant, $\dfrac{e^x}{x^n} \to +\infty$.

    **Cas $n = 0$** : c'est la limite $e^x \to +\infty$.

??? demoplus "Démonstration des autres limites — pour aller plus loin"
    **$x^n e^{-x} \to 0$ en $+\infty$** : c'est l'inverse de $\frac{e^x}{x^n}$, qui tend vers $+\infty$.

    **$x^n e^x \to 0$ en $-\infty$** : on pose $X = -x$, qui tend vers $+\infty$. Alors $x^n e^x = (-1)^n X^n e^{-X} = (-1)^n \dfrac{X^n}{e^X}$, qui tend vers $0$ d'après ce qui précède.

!!! tip "À retenir"
    En l'infini, **l'exponentielle impose sa limite** aux puissances de $x$. Pour lever une forme indéterminée avec des exponentielles, on **factorise par le terme qui croît le plus vite** (voir [Méthode 6](methodes.md#methode-6-utiliser-les-croissances-comparees)).

### 7.5 Une limite en $0$

!!! propriete "Limite du taux d'accroissement en $0$"
    $$\lim_{x \to 0} \frac{e^x - 1}{x} = 1.$$

??? demoplus "Démonstration — pour aller plus loin"
    $\dfrac{e^x - 1}{x} = \dfrac{e^x - e^0}{x - 0}$ est le taux d'accroissement de l'exponentielle entre $0$ et $x$. Comme l'exponentielle est dérivable en $0$, ce taux tend vers le nombre dérivé $\exp'(0) = e^0 = 1$ (définition du nombre dérivé, vue en Première).

---

## 8. Pour aller plus loin

- **Asymptote oblique** : si $\displaystyle\lim_{x\to+\infty} \big(f(x) - (mx + p)\big) = 0$, la droite $y = mx + p$ est asymptote oblique à $\mathcal{C}_f$ (voir l'exercice 9).
- **Logarithme** : au chapitre 5, on verra les croissances comparées du logarithme, qui à l'inverse est « plus lent » que toute puissance de $x$.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
