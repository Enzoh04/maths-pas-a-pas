# Cours — Continuité

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, $I$ désigne un intervalle de $\mathbb{R}$, et $f$ une fonction définie sur $I$.

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

    Ce chapitre ne contient pas de démonstration classiquement demandée au bac : la version classique du cours ne contient donc que les énoncés.

---

## 1. Fonctions continues

### 1.1 Définition

!!! definition "Continuité"
    Soit $a \in I$.

    - $f$ est **continue en $a$** si $\displaystyle\lim_{x \to a} f(x) = f(a)$.
    - $f$ est **continue sur $I$** si elle est continue en tout point de $I$.

**Interprétation graphique.** Sur un intervalle, la courbe d'une fonction continue se trace « sans lever le crayon » : elle ne fait pas de saut. Cette image est utile, mais elle n'est pas une définition : certaines fonctions continues ont des courbes trop « agitées » pour être dessinées.

**Exemple de discontinuité.** La **fonction partie entière** associe à tout réel $x$ le plus grand entier inférieur ou égal à $x$, noté $E(x)$ ou $\lfloor x \rfloor$. Par exemple $E(2{,}7) = 2$, $E(3) = 3$ et $E(-1{,}5) = -2$. Sa courbe est un « escalier » : elle est discontinue en chaque entier.

??? demoplus "Démonstration de la discontinuité en un entier $n$ — pour aller plus loin"
    Pour $x \in [n - 1 \,;\, n[$, on a $E(x) = n - 1$. Donc $\displaystyle\lim_{x \to n^-} E(x) = n - 1$, alors que $E(n) = n$. La limite à gauche n'est pas égale à la valeur en $n$ : $E$ n'est pas continue en $n$.

### 1.2 Les fonctions usuelles sont continues

!!! propriete "Continuité des fonctions de référence"
    - Les fonctions polynômes, la fonction valeur absolue et la fonction exponentielle sont continues sur $\mathbb{R}$.
    - La fonction racine carrée est continue sur $[0 \,;\, +\infty[$.
    - Les fonctions rationnelles (quotients de polynômes) sont continues sur chaque intervalle où leur dénominateur ne s'annule pas.
    - Les sommes, produits, quotients (dénominateur non nul) et composées de fonctions continues sont continus.

??? demoplus "Démonstration — pour aller plus loin"
    **Opérations et composition.** Si $f$ et $g$ sont continues en $a$, alors $f(x) \to f(a)$ et $g(x) \to g(a)$ ; par les opérations sur les limites (chapitre 2), $f(x) + g(x) \to f(a) + g(a)$, et de même pour le produit et le quotient. Pour la composée, si $u$ est continue en $a$ et $v$ continue en $u(a)$, le théorème de composition des limites donne $v(u(x)) \to v(u(a))$.

    **Polynômes.** La fonction $x \mapsto x$ est continue : pour $\varepsilon > 0$, il suffit de prendre $\delta = \varepsilon$. Les constantes sont continues. Par produits et sommes, tout polynôme est continu, puis toute fonction rationnelle là où elle est définie.

    **Valeur absolue.** D'après l'inégalité triangulaire, $\big||x| - |a|\big| \leq |x - a|$. Donc si $|x - a| < \varepsilon$, alors $\big||x| - |a|\big| < \varepsilon$.

    **Racine carrée en $a > 0$.** Pour $x \geq 0$ :

    $$\left|\sqrt{x} - \sqrt{a}\right| = \frac{|x - a|}{\sqrt{x} + \sqrt{a}} \leq \frac{|x - a|}{\sqrt{a}}.$$

    Le majorant tend vers $0$ quand $x \to a$ : par les gendarmes, $\sqrt{x} \to \sqrt{a}$.

    **Racine carrée en $0$.** Pour $\varepsilon > 0$, si $0 \leq x < \varepsilon^2$, alors $0 \leq \sqrt{x} < \varepsilon$.

    **Exponentielle.** Elle est dérivable sur $\mathbb{R}$, donc continue (chapitre 3, § 1.2).

### 1.3 Dérivabilité et continuité

!!! propriete "Dérivable implique continue"
    Si $f$ est dérivable sur $I$, alors $f$ est continue sur $I$. La **réciproque est fausse**.

??? demoplus "Démonstration — pour aller plus loin"
    Le sens direct a été démontré au chapitre 3 (§ 1.2).

    **Contre-exemple à la réciproque.** La valeur absolue est continue en $0$. Son taux d'accroissement en $0$ vaut $\dfrac{|h|}{h}$, c'est-à-dire $1$ si $h > 0$ et $-1$ si $h < 0$. Les limites à droite et à gauche sont différentes : il n'y a pas de limite, donc la valeur absolue n'est pas dérivable en $0$. Graphiquement, sa courbe a un « point anguleux » en l'origine.

!!! tip "Convention des tableaux de variations"
    Dans un tableau de variations, une **flèche** indique que la fonction est **continue et strictement monotone** sur l'intervalle correspondant.

---

## 2. Continuité et suites

!!! propriete "Image d'une suite convergente"
    Si $(u_n)$ converge vers $\ell \in I$ et si $f$ est continue en $\ell$, alors $\big(f(u_n)\big)$ converge vers $f(\ell)$.

??? demoplus "Démonstration — pour aller plus loin"
    C'est la propriété « composée d'une suite et d'une fonction » du chapitre 2, avec $\displaystyle\lim_{x \to \ell} f(x) = f(\ell)$ par continuité.

**Exemple.** $u_n = 2 + \dfrac{1}{n}$ tend vers $2$, et $f(x) = x^2 - 3x$ est continue. Donc $f(u_n) \to f(2) = -2$.

!!! theoreme "Théorème du point fixe"
    Soit $f$ une fonction définie sur $I$ et $(u_n)$ une suite définie par $u_0 \in I$ et $u_{n+1} = f(u_n)$, avec $u_n \in I$ pour tout $n$.

    Si $(u_n)$ **converge** vers un réel $\ell \in I$ et si $f$ est **continue en $\ell$**, alors

    $$f(\ell) = \ell.$$

    On dit que $\ell$ est un **point fixe** de $f$.

??? demoplus "Démonstration — pour aller plus loin"
    On calcule la limite de $u_{n+1}$ de deux façons.

    - $(u_{n+1})$ est la suite $(u_n)$ « décalée d'un rang » : elle converge aussi vers $\ell$.
    - $u_{n+1} = f(u_n)$, et d'après la propriété précédente, $f(u_n) \to f(\ell)$.

    Par unicité de la limite, $\ell = f(\ell)$.

!!! warning "Ce que le théorème ne dit pas"
    1. Il faut d'abord **prouver que la suite converge** (par exemple avec le théorème de convergence monotone). Le théorème ne donne que les **valeurs possibles** de la limite.
    2. Si l'équation $f(x) = x$ a plusieurs solutions, il faut utiliser d'autres informations (un encadrement de $u_n$, par exemple) pour choisir la bonne.
    3. L'hypothèse de continuité est indispensable : voir l'exercice 11.

**Exemple.** On a montré au chapitre 1 (exercice 24) que la suite $u_0 = 0$, $u_{n+1} = \sqrt{u_n + 2}$ converge et que $0 \leq u_n \leq 2$. Sa limite $\ell \in [0 \,;\, 2]$ vérifie $\ell = \sqrt{\ell + 2}$, donc $\ell^2 = \ell + 2$, soit $(\ell - 2)(\ell + 1) = 0$. Comme $\ell \geq 0$ : $\ell = 2$.

---

## 3. Le théorème des valeurs intermédiaires

### 3.1 Énoncé

!!! theoreme "Théorème des valeurs intermédiaires (TVI)"
    Soit $f$ une fonction **continue** sur un intervalle $[a \,;\, b]$. Pour tout réel $k$ compris entre $f(a)$ et $f(b)$, l'équation $f(x) = k$ admet **au moins une** solution $c \in [a \,;\, b]$.

**Interprétation.** Une fonction continue ne « saute » aucune valeur : pour passer de $f(a)$ à $f(b)$, elle prend toutes les valeurs intermédiaires.

!!! warning "La continuité est indispensable"
    La fonction partie entière vaut $0$ en $0$ et $1$ en $1$, mais ne prend jamais la valeur $\frac{1}{2}$.

??? admis "Statut de ce théorème"
    Le théorème des valeurs intermédiaires est **admis** dans le programme du bac. Sa preuve repose sur la **complétude de $\mathbb{R}$**, étudiée en première année du supérieur. Comme nous avons admis au chapitre 1 le théorème de convergence monotone, qui exprime justement cette complétude, nous pouvons en déduire une preuve complète du TVI : c'est le bloc suivant.

??? demoplus "Démonstration par dichotomie — pour aller plus loin"
    On suppose $f(a) \leq k \leq f(b)$ (sinon, on applique le raisonnement à $-f$ et $-k$). On construit deux suites $(a_n)$ et $(b_n)$ :

    - $a_0 = a$ et $b_0 = b$ ;
    - si $a_n$ et $b_n$ sont construits, on pose $m = \dfrac{a_n + b_n}{2}$ ; si $f(m) \leq k$, on pose $a_{n+1} = m$ et $b_{n+1} = b_n$ ; sinon, $a_{n+1} = a_n$ et $b_{n+1} = m$.

    Par récurrence, on vérifie que pour tout $n$ :

    $$a \leq a_n \leq a_{n+1} \leq b_{n+1} \leq b_n \leq b, \qquad b_n - a_n = \frac{b - a}{2^n}, \qquad f(a_n) \leq k \leq f(b_n).$$

    En effet, à chaque étape on garde une moitié de l'intervalle, et on choisit celle dont les extrémités « encadrent » $k$.

    - $(a_n)$ est croissante et majorée par $b$ : elle converge vers un réel $c$. $(b_n)$ est décroissante et minorée par $a$ : elle converge vers un réel $c'$. *(Théorème de convergence monotone, admis au chapitre 1.)*
    - $b_n - a_n = \frac{b - a}{2^n} \to 0$, donc $c' - c = 0$ : les deux suites ont la même limite $c$. Par passage à la limite dans $a \leq a_n \leq b$, on a $c \in [a \,;\, b]$.
    - $f$ est continue en $c$, donc $f(a_n) \to f(c)$ et $f(b_n) \to f(c)$. Par passage à la limite dans $f(a_n) \leq k \leq f(b_n)$ : $f(c) \leq k \leq f(c)$.

    Donc $f(c) = k$. Cette preuve donne en plus un **algorithme** pour approcher $c$ : c'est la méthode de dichotomie du § 4.

### 3.2 Le cas des fonctions strictement monotones

!!! theoreme "Corollaire du TVI"
    Soit $f$ une fonction **continue et strictement monotone** sur $[a \,;\, b]$. Pour tout réel $k$ compris entre $f(a)$ et $f(b)$, l'équation $f(x) = k$ admet une **unique** solution dans $[a \,;\, b]$.

??? demoplus "Démonstration — pour aller plus loin"
    **Existence** : c'est le TVI.

    **Unicité** : supposons $f$ strictement croissante, et soit $c$, $c'$ deux solutions. Si $c < c'$, alors $f(c) < f(c')$, ce qui contredit $f(c) = f(c') = k$. De même si $c > c'$. Donc $c = c'$. Le cas strictement décroissant est identique.

### 3.3 Extension aux intervalles ouverts ou infinis

!!! propriete "Avec des limites aux bornes"
    Le théorème et son corollaire restent vrais sur un intervalle $]a \,;\, b[$, $[a \,;\, +\infty[$, $\mathbb{R}$…, en remplaçant les valeurs aux bornes par les **limites** aux bornes.

    Par exemple, si $f$ est continue et strictement croissante sur $\mathbb{R}$, avec $\displaystyle\lim_{-\infty} f = -\infty$ et $\displaystyle\lim_{+\infty} f = +\infty$, alors pour tout réel $k$, l'équation $f(x) = k$ a une unique solution dans $\mathbb{R}$.

??? demoplus "Démonstration (sur l'exemple) — pour aller plus loin"
    Soit $k$ un réel. Comme $f \to -\infty$ en $-\infty$, il existe $x_1$ tel que $f(x_1) < k$ (définition de la limite avec $A = k$). Comme $f \to +\infty$ en $+\infty$, il existe $x_2$ tel que $f(x_2) > k$. Comme $f$ est croissante, $x_1 < x_2$. On applique le corollaire sur $[x_1 \,;\, x_2]$ : il existe une solution. L'unicité vient de la stricte monotonie sur $\mathbb{R}$. Les autres cas se traitent de la même façon.

**Exemple.** $f(x) = x^3 + x - 1$ est continue et strictement croissante sur $\mathbb{R}$ (car $f'(x) = 3x^2 + 1 > 0$). Comme $f(0) = -1 < 0$ et $f(1) = 1 > 0$, l'équation $f(x) = 0$ a une unique solution $\alpha$, et $\alpha \in \,]0 \,;\, 1[$.

---

## 4. Approcher une solution

Le TVI prouve qu'une solution **existe**, mais ne la calcule pas. Deux méthodes permettent de l'approcher.

### 4.1 Balayage

On calcule $f(x)$ pour des valeurs de $x$ régulièrement espacées, d'un pas $p$, jusqu'à observer un changement de signe. On obtient un encadrement d'amplitude $p$. C'est ce que fait le tableau de valeurs d'une calculatrice.

### 4.2 Dichotomie

On coupe l'intervalle en deux à chaque étape et on garde la moitié où il y a un changement de signe (voir la démonstration du TVI). **Après $n$ étapes, l'amplitude est divisée par $2^n$.**

```python
def dichotomie(f, a, b, precision):
    # On suppose f continue et f(a), f(b) de signes contraires
    while b - a > precision:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:   # changement de signe dans [a, m]
            b = m
        else:                  # changement de signe dans [m, b]
            a = m
    return a, b
```

**Exemple.** Sur $[0 \,;\, 1]$, pour une précision de $10^{-3}$, il faut $n$ étapes avec $\frac{1}{2^n} \leq 10^{-3}$, soit $2^n \geq 1000$ : $n = 10$ étapes suffisent ($2^{10} = 1024$). Un balayage de pas $10^{-3}$ demanderait jusqu'à $1000$ calculs.

---

## 5. Pour aller plus loin

- **Théorème des bornes** : une fonction continue sur un segment $[a \,;\, b]$ est bornée et **atteint** son maximum et son minimum. Comme le TVI, il repose sur la complétude de $\mathbb{R}$ (L1).
- **Image d'un intervalle** : l'image d'un intervalle par une fonction continue est un intervalle. C'est une reformulation du TVI.
- **Point fixe** : l'exercice 16 montre que toute fonction continue de $[0 \,;\, 1]$ dans $[0 \,;\, 1]$ a un point fixe. C'est la version en dimension 1 d'un théorème célèbre, le **théorème de Brouwer**.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
