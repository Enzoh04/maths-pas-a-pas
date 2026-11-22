# Cours — Dérivation et convexité

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, $I$ désigne un intervalle de $\mathbb{R}$ (non réduit à un point).

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Rappels de Première

### 1.1 Nombre dérivé et dérivées usuelles

!!! definition "Nombre dérivé"
    $f$ est **dérivable en $a$** si le taux d'accroissement $\dfrac{f(a + h) - f(a)}{h}$ admet une limite finie quand $h \to 0$. Cette limite est le **nombre dérivé** $f'(a)$. La tangente à $\mathcal{C}_f$ au point d'abscisse $a$ a pour équation :

    $$y = f'(a)(x - a) + f(a).$$

| $f(x)$ | $f'(x)$ | Validité |
|---|---|---|
| $k$ (constante) | $0$ | $\mathbb{R}$ |
| $x^n$ ($n \geq 1$ entier) | $nx^{n-1}$ | $\mathbb{R}$ |
| $\dfrac{1}{x}$ | $-\dfrac{1}{x^2}$ | $x \neq 0$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ | $x > 0$ |
| $e^x$ | $e^x$ | $\mathbb{R}$ |

!!! propriete "Opérations"
    Si $u$ et $v$ sont dérivables sur $I$ et $k$ est un réel :

    $$(u + v)' = u' + v', \qquad (ku)' = ku', \qquad (uv)' = u'v + uv', \qquad \left(\frac{1}{v}\right)' = -\frac{v'}{v^2}, \qquad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$$

    (là où $v$ ne s'annule pas).

??? demoplus "Démonstration du produit et de l'inverse — pour aller plus loin"
    **Produit.** On écrit le taux d'accroissement de $uv$ en $a$ en ajoutant et retranchant $u(a)v(a+h)$ :

    $$\frac{u(a+h)v(a+h) - u(a)v(a)}{h} = \frac{u(a+h) - u(a)}{h}\,v(a+h) + u(a)\,\frac{v(a+h) - v(a)}{h}.$$

    Quand $h \to 0$ : le premier quotient tend vers $u'(a)$, $v(a+h)$ tend vers $v(a)$ (une fonction dérivable est continue, voir § 1.2), et le dernier quotient tend vers $v'(a)$. La limite vaut $u'(a)v(a) + u(a)v'(a)$.

    **Inverse.** Pour $h$ assez petit, $v(a+h) \neq 0$ et :

    $$\frac{1}{h}\left(\frac{1}{v(a+h)} - \frac{1}{v(a)}\right) = -\frac{v(a+h) - v(a)}{h} \times \frac{1}{v(a+h)\,v(a)} \longrightarrow -\frac{v'(a)}{v(a)^2}.$$

    **Quotient.** $\dfrac{u}{v} = u \times \dfrac{1}{v}$ : on combine les deux formules.

### 1.2 Dérivabilité et continuité

!!! propriete "Une fonction dérivable est continue"
    Si $f$ est dérivable en $a$, alors $\displaystyle\lim_{h\to 0} f(a + h) = f(a)$.

??? demoplus "Démonstration — pour aller plus loin"
    Pour $h \neq 0$ : $f(a + h) - f(a) = h \times \dfrac{f(a+h) - f(a)}{h}$. Quand $h \to 0$, le premier facteur tend vers $0$ et le second vers $f'(a)$. Le produit tend vers $0 \times f'(a) = 0$.

### 1.3 Dérivée et sens de variation

!!! theoreme "Signe de la dérivée et variations"
    Soit $f$ dérivable sur un **intervalle** $I$.

    - Si $f' \geq 0$ sur $I$, alors $f$ est croissante sur $I$.
    - Si $f' \leq 0$ sur $I$, alors $f$ est décroissante sur $I$.
    - Si $f' = 0$ sur $I$, alors $f$ est constante sur $I$.

??? admis "Pourquoi ce résultat est admis"
    Ce théorème, admis depuis la Première, repose sur le **théorème des accroissements finis** : si $f$ est dérivable sur $[a \,;\, b]$, il existe $c \in \,]a \,;\, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$. Avec ce théorème, si $f' \geq 0$, alors $f(b) - f(a) \geq 0$ pour tous $a < b$ : $f$ est croissante.

    Le théorème des accroissements finis se démontre en **première année du supérieur** (L1, MPSI). Sa preuve utilise le fait qu'une fonction continue sur un segment atteint son maximum, ce qui repose sur la **complétude de $\mathbb{R}$** (voir le chapitre 1).

    La réciproque, en revanche, se démontre facilement : si $f$ est croissante, ses taux d'accroissement sont positifs, donc leur limite $f'(a)$ est positive.

---

## 2. Dérivée d'une fonction composée

!!! theoreme "Dérivée d'une composée"
    Soit $u$ dérivable sur $I$, à valeurs dans un intervalle $J$, et $v$ dérivable sur $J$. Alors $v \circ u$ est dérivable sur $I$ et :

    $$(v \circ u)' = u' \times (v' \circ u), \qquad \text{c'est-à-dire} \qquad \big(v(u(x))\big)' = u'(x)\,v'\big(u(x)\big).$$

??? demoplus "Démonstration — pour aller plus loin"
    Fixons $a \in I$ et notons $b = u(a)$. L'idée naturelle est d'écrire

    $$\frac{v(u(a+h)) - v(u(a))}{h} = \frac{v(u(a+h)) - v(b)}{u(a+h) - b} \times \frac{u(a+h) - u(a)}{h},$$

    mais le dénominateur $u(a+h) - b$ peut s'annuler. On contourne la difficulté avec une fonction auxiliaire. Pour $k$ réel tel que $b + k \in J$, on pose :

    $$\varphi(k) = \frac{v(b + k) - v(b)}{k} \text{ si } k \neq 0, \qquad \varphi(0) = v'(b).$$

    Par définition de $v'(b)$, $\varphi(k) \to v'(b) = \varphi(0)$ quand $k \to 0$. De plus, **pour tout $k$**, y compris $k = 0$ : $v(b + k) - v(b) = k\,\varphi(k)$.

    On applique cette égalité avec $k(h) = u(a + h) - u(a)$, de sorte que $b + k(h) = u(a+h)$ :

    $$\frac{v(u(a+h)) - v(u(a))}{h} = \frac{k(h)}{h} \times \varphi\big(k(h)\big).$$

    Quand $h \to 0$ : $\dfrac{k(h)}{h} \to u'(a)$ ; $k(h) \to 0$ car $u$ est continue en $a$ (§ 1.2) ; donc $\varphi(k(h)) \to \varphi(0) = v'(b)$ (composition de limites). Le taux d'accroissement tend vers $u'(a)\,v'(u(a))$.

!!! propriete "Cas particuliers à connaître"
    Si $u$ est dérivable sur $I$ :

    | Fonction | Dérivée | Condition |
    |---|---|---|
    | $e^{u}$ | $u'e^{u}$ | |
    | $u^n$ ($n \geq 1$ entier) | $nu'u^{n-1}$ | |
    | $\dfrac{1}{u^n}$ | $-\dfrac{nu'}{u^{n+1}}$ | $u \neq 0$ |
    | $\sqrt{u}$ | $\dfrac{u'}{2\sqrt{u}}$ | $u > 0$ |
    | $f(ax + b)$ | $af'(ax + b)$ | |

??? demoplus "Démonstration — pour aller plus loin"
    On applique le théorème avec $v(X) = e^X$, $X^n$, $X^{-n}$, $\sqrt{X}$, puis $u(x) = ax + b$ (de dérivée $a$). Par exemple, pour $\sqrt{u}$ : $v'(X) = \frac{1}{2\sqrt{X}}$, donc $(\sqrt{u})' = u' \times \frac{1}{2\sqrt{u}}$.

**Exemples.**

- $(e^{-x^2})' = -2x\,e^{-x^2}$.
- $\left((3x - 1)^4\right)' = 4 \times 3 \times (3x - 1)^3 = 12(3x - 1)^3$.
- $\left(\sqrt{x^2 + 1}\right)' = \dfrac{2x}{2\sqrt{x^2 + 1}} = \dfrac{x}{\sqrt{x^2 + 1}}$.

---

## 3. Dérivée seconde

!!! definition "Dérivée seconde"
    Si $f$ est dérivable sur $I$ et si sa dérivée $f'$ est elle-même dérivable sur $I$, on dit que $f$ est **deux fois dérivable** sur $I$. La dérivée de $f'$ s'appelle la **dérivée seconde** de $f$ et se note $f''$.

**Exemple.** $f(x) = x^3 - 6x^2 + 1$ : $f'(x) = 3x^2 - 12x$ et $f''(x) = 6x - 12$.

**En physique.** Si $f(t)$ est la position d'un mobile, $f'(t)$ est sa vitesse et $f''(t)$ son accélération.

---

## 4. Fonctions convexes et concaves

### 4.1 Définition

!!! definition "Convexité"
    Soit $f$ définie sur $I$. On dit que $f$ est **convexe** sur $I$ si, pour tous points $A$ et $B$ de sa courbe d'abscisses $a < b$ dans $I$, la courbe est **en dessous de la sécante $[AB]$** entre $a$ et $b$ :

    $$\text{pour tout } x \in [a \,;\, b], \quad f(x) \leq f(a) + \frac{f(b) - f(a)}{b - a}\,(x - a).$$

    On dit que $f$ est **concave** sur $I$ si sa courbe est **au-dessus** de toutes ses sécantes, ce qui revient à dire que $-f$ est convexe.

**Image mentale.** Une courbe convexe « sourit » comme $x \mapsto x^2$ ; une courbe concave « fait la moue » comme $x \mapsto \sqrt{x}$. Une fonction affine est à la fois convexe et concave : ses sécantes sont confondues avec sa courbe.

!!! propriete "Écriture avec un paramètre $t$"
    $f$ est convexe sur $I$ si et seulement si, pour tous $a$, $b$ de $I$ et tout $t \in [0 \,;\, 1]$ :

    $$f\big(ta + (1 - t)b\big) \leq t\,f(a) + (1 - t)\,f(b).$$

??? demoplus "Démonstration — pour aller plus loin"
    Soit $a < b$. Quand $t$ parcourt $[0 \,;\, 1]$, $x = ta + (1 - t)b$ parcourt $[a \,;\, b]$, et $x - a = (1 - t)(b - a)$. L'ordonnée du point de la sécante d'abscisse $x$ vaut donc

    $$f(a) + \frac{f(b) - f(a)}{b - a}(1 - t)(b - a) = f(a) + (1 - t)\big(f(b) - f(a)\big) = t\,f(a) + (1 - t)\,f(b).$$

    Les deux inégalités disent donc exactement la même chose. Le cas $a > b$ s'obtient en échangeant les rôles de $a$ et $b$ (et de $t$ et $1 - t$) ; le cas $a = b$ est évident.

### 4.2 Caractérisations de la convexité

Pour une fonction dérivable, on dispose de critères bien plus pratiques que la définition.

!!! theoreme "Convexité et dérivées"
    Soit $f$ dérivable sur $I$. Les propriétés suivantes sont équivalentes :

    1. $f$ est convexe sur $I$ ;
    2. la courbe de $f$ est **au-dessus de toutes ses tangentes** sur $I$ ;
    3. $f'$ est **croissante** sur $I$.

    Si de plus $f$ est deux fois dérivable sur $I$, elles équivalent aussi à :

    4. $f'' \geq 0$ sur $I$.

    De même, $f$ est concave $\iff$ courbe en dessous de ses tangentes $\iff$ $f'$ décroissante $\iff$ $f'' \leq 0$.

??? demo "Démonstration — au programme du bac : si $f'' \geq 0$, la courbe est au-dessus de ses tangentes"
    Soit $a \in I$. La tangente au point d'abscisse $a$ a pour équation $y = f'(a)(x - a) + f(a)$. On étudie l'écart entre la courbe et cette tangente :

    $$\varphi(x) = f(x) - \big(f'(a)(x - a) + f(a)\big), \qquad x \in I.$$

    $\varphi$ est deux fois dérivable, avec $\varphi'(x) = f'(x) - f'(a)$ et $\varphi''(x) = f''(x) \geq 0$.

    - Comme $\varphi'' \geq 0$, la fonction $\varphi'$ est croissante sur $I$. Or $\varphi'(a) = 0$. Donc $\varphi'(x) \leq 0$ pour $x \leq a$ et $\varphi'(x) \geq 0$ pour $x \geq a$.
    - Ainsi $\varphi$ est décroissante puis croissante : elle admet un minimum en $a$, égal à $\varphi(a) = f(a) - f(a) = 0$.

    Donc $\varphi(x) \geq 0$ pour tout $x \in I$ : la courbe est au-dessus de sa tangente en $a$. C'est vrai pour tout $a \in I$.

??? demoplus "Démonstration complète des équivalences — pour aller plus loin"
    **(3) $\Rightarrow$ (2).** C'est la démonstration précédente, en partant directement de « $\varphi' = f' - f'(a)$ est croissante » : on n'a pas besoin de $f''$.

    **(2) $\Rightarrow$ (3).** Soit $a < b$ dans $I$. La courbe est au-dessus de la tangente en $a$, en particulier au point $b$ ; et au-dessus de la tangente en $b$, au point $a$ :

    $$f(b) \geq f(a) + f'(a)(b - a), \qquad f(a) \geq f(b) + f'(b)(a - b).$$

    La première donne $f'(a)(b - a) \leq f(b) - f(a)$ ; la seconde donne $f(b) - f(a) \leq f'(b)(b - a)$. Donc $f'(a)(b - a) \leq f'(b)(b - a)$, et comme $b - a > 0$ : $f'(a) \leq f'(b)$. $f'$ est croissante.

    **(2) $\Rightarrow$ (1).** Soit $a < b$ dans $I$ et $x \in [a \,;\, b]$. On écrit que la courbe est au-dessus de la tangente **en $x$**, aux points $a$ et $b$ :

    $$f(a) \geq f(x) + f'(x)(a - x), \qquad f(b) \geq f(x) + f'(x)(b - x).$$

    On multiplie la première par $b - x \geq 0$, la seconde par $x - a \geq 0$, et on ajoute. Les termes en $f'(x)$ s'annulent, car $(a - x)(b - x) + (b - x)(x - a) = 0$ :

    $$(b - x)f(a) + (x - a)f(b) \geq (b - a)f(x).$$

    En divisant par $b - a > 0$ : $f(x) \leq \dfrac{(b - x)f(a) + (x - a)f(b)}{b - a} = f(a) + \dfrac{f(b) - f(a)}{b - a}(x - a)$. C'est l'inégalité de la sécante.

    **(1) $\Rightarrow$ (3).** Soit $a < b$ dans $I$, et $p = \dfrac{f(b) - f(a)}{b - a}$ la pente de la sécante. Pour $x \in \,]a \,;\, b[$, l'inégalité de la sécante s'écrit de deux façons (la droite passe par $A$ et par $B$) :

    $$f(x) \leq f(a) + p(x - a) \qquad \text{et} \qquad f(x) \leq f(b) + p(x - b).$$

    En divisant la première par $x - a > 0$ et la seconde par $x - b < 0$ (ce qui change le sens) :

    $$\frac{f(x) - f(a)}{x - a} \leq p \leq \frac{f(x) - f(b)}{x - b}.$$

    On fait tendre $x$ vers $a$ dans la première inégalité : le taux d'accroissement tend vers $f'(a)$, donc $f'(a) \leq p$ (passage à la limite). On fait tendre $x$ vers $b$ dans la seconde : $p \leq f'(b)$. Donc $f'(a) \leq f'(b)$.

    **(3) $\Leftrightarrow$ (4).** Si $f'' \geq 0$, alors $f'$ est croissante : c'est le théorème du § 1.3 appliqué à $f'$ (admis). Réciproquement, si $f'$ est croissante, ses taux d'accroissement sont positifs, donc leur limite $f''(a)$ est positive.

    Les énoncés sur la concavité s'obtiennent en appliquant tout ceci à $-f$.

!!! tip "En pratique"
    Pour étudier la convexité d'une fonction, on calcule $f''$ et on étudie son **signe** : $f'' \geq 0$ donne convexe, $f'' \leq 0$ donne concave.

**Exemples.**

- $x \mapsto x^2$ : $f'' = 2 > 0$, convexe sur $\mathbb{R}$.
- $x \mapsto e^x$ : $f'' = e^x > 0$, convexe sur $\mathbb{R}$.
- $x \mapsto \sqrt{x}$ : $f'(x) = \frac{1}{2}x^{-1/2}$, $f''(x) = -\frac{1}{4}x^{-3/2} < 0$, concave sur $]0 \,;\, +\infty[$.
- $x \mapsto x^3$ : $f'' = 6x$, concave sur $]-\infty \,;\, 0]$, convexe sur $[0 \,;\, +\infty[$.

---

## 5. Point d'inflexion

!!! definition "Point d'inflexion"
    Soit $f$ dérivable sur $I$ et $a$ un point de $I$ qui n'est pas une borne. Le point $A(a \,;\, f(a))$ est un **point d'inflexion** de $\mathcal{C}_f$ si la courbe **traverse sa tangente** en $A$.

!!! propriete "Point d'inflexion et dérivée seconde"
    Si $f$ est deux fois dérivable et si $f''$ **s'annule en changeant de signe** en $a$, alors $A(a \,;\, f(a))$ est un point d'inflexion. La fonction change alors de convexité en $a$.

??? demoplus "Démonstration — pour aller plus loin"
    Supposons par exemple $f'' \leq 0$ sur $[a - r \,;\, a]$ et $f'' \geq 0$ sur $[a \,;\, a + r]$ pour un certain $r > 0$.

    - Sur $[a \,;\, a + r]$, $f$ est convexe : la courbe est au-dessus de toutes ses tangentes sur cet intervalle, en particulier de la tangente en $a$.
    - Sur $[a - r \,;\, a]$, $f$ est concave : la courbe est en dessous de la tangente en $a$.

    La courbe passe donc d'un côté de la tangente à l'autre en $A$ : elle la traverse. Le cas inverse est symétrique.

!!! warning "Attention : $f''(a) = 0$ ne suffit pas"
    Pour $f(x) = x^4$, on a $f''(x) = 12x^2$, donc $f''(0) = 0$. Mais $f'' \geq 0$ partout : $f$ est convexe sur $\mathbb{R}$, et l'origine **n'est pas** un point d'inflexion. Il faut un **changement de signe**.

**Exemple.** $f(x) = x^3 - 6x^2 + 1$ : $f''(x) = 6(x - 2)$ s'annule en changeant de signe en $2$. Le point $(2 \,;\, -15)$ est un point d'inflexion : $f$ est concave sur $]-\infty \,;\, 2]$ et convexe sur $[2 \,;\, +\infty[$.

---

## 6. Inégalités de convexité

La convexité est un outil très puissant pour démontrer des inégalités.

!!! propriete "Deux façons d'obtenir une inégalité"
    - **Tangente** : si $f$ est convexe sur $I$ et $a \in I$, alors pour tout $x \in I$, $f(x) \geq f'(a)(x - a) + f(a)$. (Inégalité inverse si $f$ est concave.)
    - **Milieu** : si $f$ est convexe sur $I$, alors pour tous $a$, $b$ de $I$ :

    $$f\left(\frac{a + b}{2}\right) \leq \frac{f(a) + f(b)}{2}.$$

??? demoplus "Démonstration — pour aller plus loin"
    Le premier point est la caractérisation (2) du théorème du § 4.2. Le second est l'écriture avec un paramètre du § 4.1, avec $t = \frac{1}{2}$.

**Exemples classiques.**

- $\exp$ est convexe, de tangente $y = x + 1$ en $0$ : **$e^x \geq 1 + x$** pour tout réel $x$.
- $\sqrt{\phantom{x}}$ est concave, de tangente $y = \frac{1}{2}(x - 1) + 1 = \frac{x + 1}{2}$ en $1$ : **$\sqrt{x} \leq \dfrac{x + 1}{2}$** pour tout $x \geq 0$.

---

## 7. Pour aller plus loin

- **Inégalité de Jensen** : si $f$ est convexe, $f\left(\frac{x_1 + \dots + x_n}{n}\right) \leq \frac{f(x_1) + \dots + f(x_n)}{n}$. Elle se démontre par récurrence et donne par exemple l'inégalité entre moyennes arithmétique et géométrique.
- **Encadrement du nombre $e$** : l'exercice 22 montre que $\left(1 + \frac{1}{n}\right)^n \leq e \leq \left(1 + \frac{1}{n}\right)^{n+1}$.
- **Logarithme** (chapitre 5) : c'est une fonction concave, ce qui donne l'inégalité $\ln x \leq x - 1$.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
