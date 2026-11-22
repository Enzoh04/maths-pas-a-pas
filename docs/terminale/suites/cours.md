# Cours — Suites : récurrence et limites

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, $(u_n)$ désigne une suite de nombres réels définie pour tout entier naturel $n$ (ou à partir d'un certain rang).

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Le raisonnement par récurrence

### 1.1 L'idée

On veut démontrer qu'une propriété $\mathcal{P}(n)$ est vraie **pour tout entier** $n \geq n_0$. On ne peut pas vérifier une infinité de cas un par un. On s'y prend comme pour faire tomber une file de dominos :

- le **premier** domino tombe ;
- **si** un domino tombe, **alors** il fait tomber le suivant.

Alors tous les dominos tombent.

!!! theoreme "Principe de récurrence"
    Soit $\mathcal{P}(n)$ une propriété qui dépend d'un entier naturel $n$, et $n_0$ un entier naturel. Si :

    1. **Initialisation** : $\mathcal{P}(n_0)$ est vraie ;
    2. **Hérédité** : pour tout entier $n \geq n_0$, si $\mathcal{P}(n)$ est vraie, alors $\mathcal{P}(n+1)$ est vraie ;

    alors $\mathcal{P}(n)$ est vraie pour tout entier $n \geq n_0$.

??? demoplus "Démonstration — pour aller plus loin"
    On utilise une propriété fondamentale des entiers naturels : **toute partie non vide de $\mathbb{N}$ possède un plus petit élément**. Elle fait partie de la définition même de $\mathbb{N}$ et ne se démontre pas.

    Raisonnons par l'absurde : supposons que $\mathcal{P}(n)$ soit fausse pour au moins un entier $n \geq n_0$. L'ensemble $E$ des entiers $n \geq n_0$ pour lesquels $\mathcal{P}(n)$ est fausse est alors non vide. Il possède un plus petit élément $m$.

    - $m \neq n_0$, car $\mathcal{P}(n_0)$ est vraie (initialisation). Donc $m \geq n_0 + 1$, et $m - 1 \geq n_0$.
    - $m - 1$ est plus petit que $m$, donc $m - 1 \notin E$ : $\mathcal{P}(m-1)$ est vraie.
    - Par hérédité, $\mathcal{P}(m)$ est alors vraie, ce qui contredit $m \in E$.

    L'hypothèse de départ est donc fausse : $\mathcal{P}(n)$ est vraie pour tout $n \geq n_0$.

!!! warning "Les deux étapes sont indispensables"
    - Sans initialisation : la propriété « $10^n$ est un multiple de 3 » est héréditaire (si $10^n = 3k$, alors $10^{n+1} = 3 \times 10k$), mais elle est fausse pour tout $n$ !
    - Sans hérédité : « $n^2 - n + 41$ est un nombre premier » est vraie pour $n = 0, 1, \dots, 40$, mais fausse pour $n = 41$ (on obtient $41^2$).

### 1.2 Un premier exemple

**Exemple.** Montrons que pour tout entier $n \geq 1$ :

$$1 + 2 + \dots + n = \frac{n(n+1)}{2}.$$

Pour $n \geq 1$, on note $\mathcal{P}(n)$ : « $1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$ ».

- **Initialisation** ($n = 1$) : le membre de gauche vaut $1$ et celui de droite $\dfrac{1 \times 2}{2} = 1$. Donc $\mathcal{P}(1)$ est vraie.
- **Hérédité** : soit $n \geq 1$ tel que $\mathcal{P}(n)$ soit vraie (c'est l'**hypothèse de récurrence**). Alors :

$$1 + 2 + \dots + n + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2}.$$

C'est exactement $\mathcal{P}(n+1)$.

- **Conclusion** : par récurrence, $\mathcal{P}(n)$ est vraie pour tout entier $n \geq 1$.

### 1.3 L'inégalité de Bernoulli

!!! propriete "Inégalité de Bernoulli"
    Pour tout réel $a > 0$ et tout entier naturel $n$ :

    $$(1 + a)^n \geq 1 + na.$$

??? demo "Démonstration — au programme du bac"
    Soit $a > 0$. Pour $n \in \mathbb{N}$, on note $\mathcal{P}(n)$ : « $(1+a)^n \geq 1 + na$ ».

    - **Initialisation** : $(1+a)^0 = 1$ et $1 + 0 \times a = 1$. On a bien $1 \geq 1$, donc $\mathcal{P}(0)$ est vraie.
    - **Hérédité** : soit $n \in \mathbb{N}$ tel que $(1+a)^n \geq 1 + na$. Comme $1 + a > 0$, on peut multiplier les deux membres par $1+a$ sans changer le sens de l'inégalité :

    $$(1+a)^{n+1} \geq (1 + na)(1 + a) = 1 + a + na + na^2 = 1 + (n+1)a + na^2.$$

    Or $na^2 \geq 0$, donc $(1+a)^{n+1} \geq 1 + (n+1)a$ : $\mathcal{P}(n+1)$ est vraie.

    - **Conclusion** : pour tout $n \in \mathbb{N}$, $(1+a)^n \geq 1 + na$.

---

## 2. Limite d'une suite

### 2.1 Limite infinie

!!! definition "Définition"
    On dit que la suite $(u_n)$ **tend vers $+\infty$** si tout intervalle $]A \,;\, +\infty[$ contient tous les termes $u_n$ **à partir d'un certain rang**.

    Autrement dit : pour tout réel $A$, il existe un entier $N$ tel que, pour tout $n \geq N$, $u_n > A$.

    On note $\displaystyle\lim_{n \to +\infty} u_n = +\infty$.

On définit de même $\displaystyle\lim_{n \to +\infty} u_n = -\infty$ : tout intervalle $]-\infty \,;\, A[$ contient tous les termes à partir d'un certain rang.

**Exemple.** La suite $u_n = n^2$ tend vers $+\infty$. Soit $A > 0$ : dès que $n > \sqrt{A}$, on a $n^2 > A$.

!!! warning "Attention"
    Une suite qui tend vers $+\infty$ n'est pas forcément croissante. Par exemple, $u_n = n + 2(-1)^n$ tend vers $+\infty$ (car $u_n \geq n - 2$), alors que $u_1 = -1 < u_0 = 2$.

### 2.2 Limite finie

!!! definition "Définition"
    On dit que la suite $(u_n)$ **converge vers le réel $\ell$** si tout intervalle ouvert contenant $\ell$ contient tous les termes $u_n$ à partir d'un certain rang.

    On note $\displaystyle\lim_{n \to +\infty} u_n = \ell$.

Pour démontrer des résultats, on utilise souvent la forme suivante de la définition, avec des intervalles centrés en $\ell$.

!!! propriete "Formulation avec $\varepsilon$"
    $(u_n)$ converge vers $\ell$ si et seulement si, pour tout réel $\varepsilon > 0$, il existe un rang $N$ tel que :

    $$\text{pour tout } n \geq N, \quad |u_n - \ell| < \varepsilon.$$

    En particulier, $(u_n)$ converge vers $\ell$ si et seulement si $(u_n - \ell)$ converge vers $0$, si et seulement si $(|u_n - \ell|)$ converge vers $0$.

??? demoplus "Démonstration — pour aller plus loin"
    Rappelons que $|u_n - \ell| < \varepsilon$ équivaut à $\ell - \varepsilon < u_n < \ell + \varepsilon$, c'est-à-dire $u_n \in \left]\ell - \varepsilon \,;\, \ell + \varepsilon\right[$.

    - **Sens direct.** Si $(u_n)$ converge vers $\ell$ et si $\varepsilon > 0$, l'intervalle $\left]\ell - \varepsilon \,;\, \ell + \varepsilon\right[$ est ouvert et contient $\ell$ : il contient tous les $u_n$ à partir d'un certain rang.
    - **Réciproque.** Soit $]a \,;\, b[$ un intervalle ouvert contenant $\ell$, donc $a < \ell < b$. On pose $\varepsilon = \min(\ell - a,\, b - \ell) > 0$. Alors $\left]\ell - \varepsilon \,;\, \ell + \varepsilon\right[ \subset \,]a \,;\, b[$. À partir d'un certain rang, $u_n$ appartient au petit intervalle, donc au grand.

    La dernière phrase vient de ce que $|u_n - \ell| = |(u_n - \ell) - 0| = \big||u_n - \ell| - 0\big|$ : les trois conditions s'écrivent exactement de la même façon.

!!! propriete "Unicité de la limite"
    Si une suite converge, sa limite est **unique**.

??? demoplus "Démonstration — pour aller plus loin"
    Supposons que $(u_n)$ converge à la fois vers $\ell$ et vers $\ell'$, avec $\ell < \ell'$. On pose $d = \ell' - \ell > 0$.

    Les intervalles $I = \left]\ell - \frac{d}{3} \,;\, \ell + \frac{d}{3}\right[$ et $J = \left]\ell' - \frac{d}{3} \,;\, \ell' + \frac{d}{3}\right[$ sont **disjoints**, car $\ell + \frac{d}{3} < \ell' - \frac{d}{3}$ (cela revient à $\frac{2d}{3} < d$).

    Il existe un rang $N_1$ à partir duquel tous les $u_n$ sont dans $I$, et un rang $N_2$ à partir duquel ils sont tous dans $J$. Pour $n = \max(N_1, N_2)$, $u_n$ serait à la fois dans $I$ et dans $J$ : c'est impossible. Donc $\ell = \ell'$.

Une suite qui ne converge pas est dite **divergente**. Il y a deux façons de diverger :

- tendre vers $+\infty$ ou $-\infty$ ;
- **ne pas avoir de limite**, comme $u_n = (-1)^n$, qui vaut alternativement $1$ et $-1$.

??? demoplus "Démonstration que $(-1)^n$ n'a pas de limite — pour aller plus loin"
    - **Pas de limite infinie.** Tous les termes sont inférieurs ou égaux à $1$, donc l'intervalle $]1 \,;\, +\infty[$ ne contient aucun terme : la suite ne tend pas vers $+\infty$. De même avec $]-\infty \,;\, -1[$ pour $-\infty$.
    - **Pas de limite finie.** Supposons que $(-1)^n$ converge vers $\ell$. L'intervalle $\left]\ell - \frac{1}{2} \,;\, \ell + \frac{1}{2}\right[$, de longueur $1$, contiendrait tous les termes à partir d'un certain rang, donc à la fois la valeur $1$ (rangs pairs) et la valeur $-1$ (rangs impairs). Mais deux nombres d'un intervalle de longueur $1$ sont distants de moins de $1$, alors que $1$ et $-1$ sont distants de $2$. Contradiction.

!!! propriete "Une suite convergente est bornée à partir d'un certain rang"
    Si $(u_n)$ converge vers $\ell$, il existe un rang $N$ tel que, pour tout $n \geq N$ : $|u_n| \leq |\ell| + 1$.

??? demoplus "Démonstration — pour aller plus loin"
    On applique la formulation avec $\varepsilon = 1$ : il existe $N$ tel que pour $n \geq N$, $|u_n - \ell| < 1$. Alors, avec l'inégalité triangulaire $|a + b| \leq |a| + |b|$ :

    $$|u_n| = |(u_n - \ell) + \ell| \leq |u_n - \ell| + |\ell| < 1 + |\ell|.$$

### 2.3 Limites de référence

!!! propriete "Limites à connaître"
    $$\lim_{n \to +\infty} n = +\infty \qquad \lim_{n \to +\infty} n^2 = +\infty \qquad \lim_{n \to +\infty} n^k = +\infty \ (k \geq 1) \qquad \lim_{n \to +\infty} \sqrt{n} = +\infty$$

    $$\lim_{n \to +\infty} \frac{1}{n} = 0 \qquad \lim_{n \to +\infty} \frac{1}{n^2} = 0 \qquad \lim_{n \to +\infty} \frac{1}{n^k} = 0 \qquad \lim_{n \to +\infty} \frac{1}{\sqrt{n}} = 0$$

??? demoplus "Démonstration — pour aller plus loin"
    **Limites infinies.** Soit $A > 0$.

    - Soit $N$ un entier strictement supérieur à $A$. Pour tout $n \geq N$, on a $n > A$ : la suite $(n)$ tend vers $+\infty$.
    - Pour $k \geq 1$ et $n \geq 1$, on a $n^k \geq n$. Par comparaison (théorème du § 4.1), $n^k \to +\infty$.
    - Si $n > A^2$, alors $\sqrt{n} > \sqrt{A^2} = A$, car la fonction racine carrée est strictement croissante.

    **Limites nulles.** Soit $\varepsilon > 0$.

    - Si $n > \dfrac{1}{\varepsilon}$, alors $0 < \dfrac{1}{n} < \varepsilon$, donc $\left|\dfrac{1}{n} - 0\right| < \varepsilon$.
    - Si $n > \dfrac{1}{\varepsilon^2}$, alors $\sqrt{n} > \dfrac{1}{\varepsilon}$ et $0 < \dfrac{1}{\sqrt{n}} < \varepsilon$.
    - Pour $n \geq 1$ et $k \geq 1$ : $0 < \dfrac{1}{n^k} \leq \dfrac{1}{n}$. Par le théorème des gendarmes (§ 4.2), $\dfrac{1}{n^k} \to 0$.

---

## 3. Opérations sur les limites

Dans les tableaux, $\ell$ et $\ell'$ sont des réels. « **F.I.** » signifie **forme indéterminée** : on ne peut pas conclure directement, il faut transformer l'écriture (voir [Méthode 2](methodes.md#methode-2-lever-une-forme-indeterminee)).

**Somme** $u_n + v_n$

| $\lim u_n$ | $\ell$ | $\ell$ | $\ell$ | $+\infty$ | $-\infty$ | $+\infty$ |
|---|---|---|---|---|---|---|
| $\lim v_n$ | $\ell'$ | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | $-\infty$ |
| $\lim (u_n + v_n)$ | $\ell + \ell'$ | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | **F.I.** |

**Produit** $u_n \times v_n$

| $\lim u_n$ | $\ell$ | $\ell \neq 0$ | $\infty$ | $0$ |
|---|---|---|---|---|
| $\lim v_n$ | $\ell'$ | $\infty$ | $\infty$ | $\infty$ |
| $\lim (u_n v_n)$ | $\ell \ell'$ | $\infty$ | $\infty$ | **F.I.** |

Le signe de l'infini s'obtient avec la règle des signes.

**Quotient** $\dfrac{u_n}{v_n}$

| $\lim u_n$ | $\ell$ | $\ell$ | $\ell \neq 0$ ou $\infty$ | $\infty$ | $\infty$ | $0$ |
|---|---|---|---|---|---|---|
| $\lim v_n$ | $\ell' \neq 0$ | $\infty$ | $0$ (signe constant) | $\ell'$ | $\infty$ | $0$ |
| $\lim \frac{u_n}{v_n}$ | $\frac{\ell}{\ell'}$ | $0$ | $\infty$ | $\infty$ | **F.I.** | **F.I.** |

??? demoplus "Démonstration des cas principaux — pour aller plus loin"
    On démontre les cas qui contiennent toutes les idées. Les autres cases se traitent de la même façon, en changeant les signes.

    **a) Somme de deux suites convergentes.** Soit $\varepsilon > 0$. À partir d'un certain rang, $|u_n - \ell| < \frac{\varepsilon}{2}$ et $|v_n - \ell'| < \frac{\varepsilon}{2}$ (on prend le plus grand des deux rangs). Avec l'inégalité triangulaire :

    $$|(u_n + v_n) - (\ell + \ell')| \leq |u_n - \ell| + |v_n - \ell'| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

    **b) $\ell + (+\infty) = +\infty$.** Avec $\varepsilon = 1$, on a $u_n > \ell - 1$ à partir d'un certain rang. Donc $u_n + v_n > v_n + (\ell - 1)$. Or $v_n + (\ell - 1) \to +\infty$ : pour tout $A$, $v_n > A - \ell + 1$ à partir d'un certain rang. Par comparaison, $u_n + v_n \to +\infty$.

    **c) $(+\infty) + (+\infty) = +\infty$.** À partir d'un certain rang, $v_n > 0$, donc $u_n + v_n > u_n$. Par comparaison, $u_n + v_n \to +\infty$.

    **d) Un lemme utile.** *Si $(a_n)$ est bornée et si $b_n \to 0$, alors $a_n b_n \to 0$.* En effet, soit $M > 0$ tel que $|a_n| \leq M$ (à partir d'un certain rang). Alors $0 \leq |a_n b_n| \leq M|b_n|$. Or $M|b_n| \to 0$ : pour $\varepsilon > 0$, on a $|b_n| < \frac{\varepsilon}{M}$ à partir d'un certain rang. Par les gendarmes, $|a_n b_n| \to 0$, donc $a_n b_n \to 0$.

    **e) Produit de deux suites convergentes.** On écrit

    $$u_n v_n - \ell \ell' = u_n (v_n - \ell') + \ell' (u_n - \ell).$$

    $(u_n)$ est bornée à partir d'un certain rang (§ 2.2) et $v_n - \ell' \to 0$, donc le premier terme tend vers $0$ (lemme). La suite constante $\ell'$ est bornée et $u_n - \ell \to 0$, donc le second terme tend vers $0$. Par somme (a), $u_n v_n - \ell\ell' \to 0$.

    **f) Inverse : si $v_n \to \ell' \neq 0$, alors $\dfrac{1}{v_n} \to \dfrac{1}{\ell'}$.** Avec $\varepsilon = \frac{|\ell'|}{2}$, on a $|v_n - \ell'| < \frac{|\ell'|}{2}$ à partir d'un certain rang, donc $|v_n| \geq |\ell'| - |v_n - \ell'| > \frac{|\ell'|}{2}$ ; en particulier, $v_n \neq 0$. Alors :

    $$\left|\frac{1}{v_n} - \frac{1}{\ell'}\right| = \frac{|\ell' - v_n|}{|v_n|\,|\ell'|} \leq \frac{2}{\ell'^2}\,|v_n - \ell'|.$$

    Le majorant tend vers $0$ : par les gendarmes, $\frac{1}{v_n} - \frac{1}{\ell'} \to 0$. Le quotient $\frac{u_n}{v_n} = u_n \times \frac{1}{v_n}$ se traite alors avec le produit (e).

    **g) Si $v_n \to +\infty$, alors $\dfrac{1}{v_n} \to 0$.** Soit $\varepsilon > 0$. À partir d'un certain rang, $v_n > \frac{1}{\varepsilon} > 0$, donc $0 < \frac{1}{v_n} < \varepsilon$. On en déduit la case $\frac{\ell}{\infty} = 0$ avec le lemme (d).

    **h) $\ell \times (+\infty)$ avec $\ell > 0$.** Avec $\varepsilon = \frac{\ell}{2}$, on a $u_n > \frac{\ell}{2}$ à partir d'un certain rang, et aussi $v_n > 0$. Donc $u_n v_n \geq \frac{\ell}{2} v_n$, qui tend vers $+\infty$. Par comparaison, $u_n v_n \to +\infty$.

    **i) Si $v_n \to 0$ avec $v_n > 0$, alors $\dfrac{1}{v_n} \to +\infty$.** Soit $A > 0$. À partir d'un certain rang, $0 < v_n < \frac{1}{A}$, donc $\frac{1}{v_n} > A$. Avec (h), on en déduit la case « $\frac{\ell}{0}$ ».

!!! tip "Les quatre formes indéterminées"
    $$\infty - \infty \qquad 0 \times \infty \qquad \frac{\infty}{\infty} \qquad \frac{0}{0}$$

??? note "Pourquoi « indéterminée » ?"
    Parce qu'avec la même forme, on peut obtenir n'importe quel résultat. Par exemple, pour $\infty - \infty$ :

    $$n^2 - n \to +\infty, \qquad n - n^2 \to -\infty, \qquad (n + 3) - n = 3 \to 3, \qquad n + (-1)^n - n = (-1)^n \text{ n'a pas de limite}.$$

    Et pour $0 \times \infty$ : $\frac{1}{n} \times n^2 \to +\infty$, $\frac{1}{n^2} \times n \to 0$, $\frac{3}{n} \times n = 3$.

**Exemple.** $u_n = 3n^2 - n$ donne la forme $\infty - \infty$. On factorise par le terme dominant :

$$u_n = n^2\left(3 - \frac{1}{n}\right).$$

Comme $\lim n^2 = +\infty$ et $\lim \left(3 - \frac{1}{n}\right) = 3$, par produit $\lim u_n = +\infty$.

---

## 4. Théorèmes de comparaison

### 4.1 Limites infinies

!!! theoreme "Théorème de comparaison"
    Soit $(u_n)$ et $(v_n)$ deux suites telles que $u_n \leq v_n$ à partir d'un certain rang.

    - Si $\displaystyle\lim_{n\to+\infty} u_n = +\infty$, alors $\displaystyle\lim_{n\to+\infty} v_n = +\infty$.
    - Si $\displaystyle\lim_{n\to+\infty} v_n = -\infty$, alors $\displaystyle\lim_{n\to+\infty} u_n = -\infty$.

??? demo "Démonstration — au programme du bac (premier point)"
    Il existe un rang $n_0$ tel que $u_n \leq v_n$ pour tout $n \geq n_0$.

    Soit $A$ un réel. Comme $(u_n)$ tend vers $+\infty$, il existe un rang $N_1$ tel que $u_n > A$ pour tout $n \geq N_1$.

    Posons $N = \max(n_0, N_1)$. Pour tout $n \geq N$, on a à la fois $v_n \geq u_n$ et $u_n > A$, donc $v_n > A$.

    Ainsi, tout intervalle $]A \,;\, +\infty[$ contient tous les $v_n$ à partir du rang $N$ : $\displaystyle\lim_{n\to+\infty} v_n = +\infty$.

??? demoplus "Démonstration du second point — pour aller plus loin"
    Si $u_n \leq v_n$, alors $-v_n \leq -u_n$. Si $v_n \to -\infty$, alors $-v_n \to +\infty$ : pour tout $A$, l'inégalité $v_n < -A$ est vraie à partir d'un certain rang, donc $-v_n > A$. D'après le premier point, $-u_n \to +\infty$, donc $u_n \to -\infty$.

**Exemple.** $v_n = n + \cos n$. Comme $\cos n \geq -1$, on a $v_n \geq n - 1$, et $\lim (n-1) = +\infty$. Donc $\lim v_n = +\infty$.

### 4.2 Limites finies : le théorème des gendarmes

!!! theoreme "Théorème des gendarmes"
    Soit $(u_n)$, $(v_n)$ et $(w_n)$ trois suites telles que, à partir d'un certain rang :

    $$u_n \leq v_n \leq w_n.$$

    Si $(u_n)$ et $(w_n)$ convergent vers **la même limite** $\ell$, alors $(v_n)$ converge aussi vers $\ell$.

??? demoplus "Démonstration — pour aller plus loin (admise dans le programme du bac)"
    Soit $\varepsilon > 0$. À partir d'un certain rang (on prend le plus grand des rangs en jeu) :

    - $u_n \leq v_n \leq w_n$ ;
    - $|u_n - \ell| < \varepsilon$, donc en particulier $u_n > \ell - \varepsilon$ ;
    - $|w_n - \ell| < \varepsilon$, donc en particulier $w_n < \ell + \varepsilon$.

    On obtient $\ell - \varepsilon < u_n \leq v_n \leq w_n < \ell + \varepsilon$, donc $|v_n - \ell| < \varepsilon$. Ainsi $(v_n)$ converge vers $\ell$.

**Exemple.** $v_n = \dfrac{(-1)^n}{n}$ pour $n \geq 1$. On a $-\dfrac{1}{n} \leq v_n \leq \dfrac{1}{n}$, et les deux encadrants tendent vers $0$. Donc $\lim v_n = 0$.

!!! propriete "Une suite de limite strictement positive est positive à partir d'un certain rang"
    Si $(w_n)$ converge vers $d > 0$, alors $w_n > 0$ à partir d'un certain rang.

??? demoplus "Démonstration — pour aller plus loin"
    Avec $\varepsilon = \frac{d}{2}$ : à partir d'un certain rang, $|w_n - d| < \frac{d}{2}$, donc $w_n > d - \frac{d}{2} = \frac{d}{2} > 0$.

!!! propriete "Passage à la limite dans une inégalité"
    Si $u_n \leq v_n$ à partir d'un certain rang, et si $(u_n)$ et $(v_n)$ convergent respectivement vers $\ell$ et $\ell'$, alors $\ell \leq \ell'$.

??? demoplus "Démonstration — pour aller plus loin"
    Raisonnons par l'absurde : supposons $\ell > \ell'$. La suite $w_n = u_n - v_n$ converge vers $\ell - \ell' > 0$ (somme de limites). D'après la propriété précédente, $w_n > 0$ à partir d'un certain rang, c'est-à-dire $u_n > v_n$. Cela contredit $u_n \leq v_n$. Donc $\ell \leq \ell'$.

!!! warning "Les inégalités strictes deviennent larges"
    $\dfrac{1}{n} > 0$ pour tout $n \geq 1$, mais $\lim \dfrac{1}{n} = 0$ : on obtient seulement $0 \geq 0$.

---

## 5. Suites géométriques

!!! theoreme "Limite de $(q^n)$"
    Soit $q$ un réel.

    | Valeur de $q$ | $q \leq -1$ | $-1 < q < 1$ | $q = 1$ | $q > 1$ |
    |---|---|---|---|---|
    | $\lim q^n$ | pas de limite | $0$ | $1$ | $+\infty$ |

??? demo "Démonstration — au programme du bac (cas $q > 1$ et cas $-1 < q < 1$)"
    **Cas $q > 1$.** On pose $a = q - 1 > 0$. D'après l'inégalité de Bernoulli :

    $$q^n = (1 + a)^n \geq 1 + na.$$

    Comme $a > 0$, $\lim (1 + na) = +\infty$. Par comparaison, $\lim q^n = +\infty$.

    **Cas $-1 < q < 1$.** Si $q = 0$, la suite est nulle à partir du rang 1. Sinon, $0 < |q| < 1$, donc $\dfrac{1}{|q|} > 1$, et d'après le cas précédent :

    $$\lim_{n\to+\infty} \left(\frac{1}{|q|}\right)^n = +\infty, \quad \text{donc} \quad \lim_{n\to+\infty} |q|^n = \lim_{n\to+\infty} \frac{1}{\left(\frac{1}{|q|}\right)^n} = 0.$$

    Enfin $-|q|^n \leq q^n \leq |q|^n$, et par le théorème des gendarmes, $\lim q^n = 0$.

??? demoplus "Démonstration des cas $q = 1$ et $q \leq -1$ — pour aller plus loin"
    **Cas $q = 1$.** La suite est constante égale à $1$.

    **Cas $q = -1$.** C'est la suite $(-1)^n$, qui n'a pas de limite (§ 2.2).

    **Cas $q < -1$.** On a $|q| > 1$, donc $|q^n| = |q|^n \to +\infty$.

    - La suite ne peut pas converger : une suite convergente est bornée à partir d'un certain rang (§ 2.2), ce qui est impossible si $|q^n| \to +\infty$.
    - Elle ne peut pas tendre vers $+\infty$ : l'intervalle $]0 \,;\, +\infty[$ devrait contenir tous les termes à partir d'un certain rang, or $q^n < 0$ pour tous les $n$ impairs.
    - De même, elle ne tend pas vers $-\infty$, car $q^n > 0$ pour tous les $n$ pairs.

**Conséquence : limite d'une somme géométrique.** Pour $q \neq 1$ :

$$1 + q + q^2 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}.$$

??? demoplus "Démonstration de la formule — pour aller plus loin"
    Notons $S = 1 + q + \dots + q^n$. Alors $qS = q + q^2 + \dots + q^{n+1}$. En soustrayant, presque tous les termes s'annulent :

    $$S - qS = 1 - q^{n+1}, \quad \text{soit} \quad (1 - q)S = 1 - q^{n+1}.$$

    Comme $q \neq 1$, on peut diviser par $1 - q$.

Si $-1 < q < 1$, alors $\lim q^{n+1} = 0$ et donc :

$$\lim_{n\to+\infty} \left(1 + q + \dots + q^n\right) = \frac{1}{1-q}.$$

**Exemple.** $1 + \dfrac{1}{2} + \dfrac{1}{4} + \dots + \dfrac{1}{2^n} \longrightarrow \dfrac{1}{1 - \frac{1}{2}} = 2$.

---

## 6. Suites monotones

!!! definition "Rappels"
    - $(u_n)$ est **majorée** s'il existe un réel $M$ tel que $u_n \leq M$ pour tout $n$.
    - $(u_n)$ est **minorée** s'il existe un réel $m$ tel que $u_n \geq m$ pour tout $n$.
    - $(u_n)$ est **bornée** si elle est majorée et minorée.

!!! theoreme "Théorème de convergence monotone"
    - Toute suite **croissante et majorée** converge.
    - Toute suite **décroissante et minorée** converge.

??? admis "Pourquoi ce résultat est admis"
    Ce théorème ne peut pas être démontré avec les outils du lycée. Ce n'est pas une question de difficulté : il traduit une propriété profonde des nombres réels, la **complétude de $\mathbb{R}$** (ou « propriété de la borne supérieure »). Elle est étudiée en **première année du supérieur** (L1 ou MPSI), quand on construit précisément l'ensemble $\mathbb{R}$.

    **Pour sentir pourquoi c'est subtil**, imagine qu'on ne connaisse que les nombres rationnels (les fractions). La suite de Héron $u_0 = 2$, $u_{n+1} = \frac{1}{2}\left(u_n + \frac{2}{u_n}\right)$ (exercice 26) est formée de fractions. Elle est décroissante et minorée par $1$. Pourtant, sa limite $\sqrt{2}$ n'est pas une fraction. Dans le monde des fractions, cette suite « devrait » converger mais n'a aucune limite : il y manque des nombres. L'ensemble $\mathbb{R}$ est justement construit pour qu'il ne manque plus rien.

    En revanche, une fois ce théorème admis, on peut en déduire le second point à partir du premier : si $(u_n)$ est décroissante et minorée par $m$, alors $(-u_n)$ est croissante et majorée par $-m$, donc converge vers un réel $L$, et $(u_n)$ converge vers $-L$.

!!! warning "Ce que le théorème ne dit pas"
    Il assure que la limite **existe**, mais ne donne **pas** sa valeur. Si $(u_n)$ est croissante et majorée par $M$, sa limite $\ell$ vérifie seulement $\ell \leq M$. Par exemple, $u_n = 1 - \frac{1}{n+1}$ est croissante, majorée par $5$, et converge vers $1$.

!!! propriete "Suite croissante non majorée"
    Si $(u_n)$ est croissante et non majorée, alors $\displaystyle\lim_{n\to+\infty} u_n = +\infty$.

??? demo "Démonstration — au programme du bac"
    Soit $A$ un réel. La suite n'est pas majorée, donc $A$ n'est pas un majorant : il existe un rang $N$ tel que $u_N > A$.

    La suite est croissante, donc pour tout $n \geq N$, $u_n \geq u_N > A$.

    Ainsi, tout intervalle $]A \,;\, +\infty[$ contient tous les termes à partir du rang $N$ : $\displaystyle\lim_{n\to+\infty} u_n = +\infty$.

!!! propriete "Une suite croissante est majorée par sa limite"
    Si $(u_n)$ est croissante et converge vers $\ell$, alors $u_n \leq \ell$ pour tout $n$.

??? demoplus "Démonstration — pour aller plus loin"
    Soit $p$ un entier fixé. La suite étant croissante, $u_n \geq u_p$ pour tout $n \geq p$. Par passage à la limite dans cette inégalité (§ 4.2), en voyant $u_p$ comme une suite constante : $\ell \geq u_p$. Ceci vaut pour tout $p$.

---

## 7. Pour aller plus loin

- **Suites $u_{n+1} = f(u_n)$** : quand on sait que la suite converge vers $\ell$ et que $f$ est continue, on obtient $\ell = f(\ell)$. Ce résultat sera démontré dans le chapitre **Continuité**.
- **Suites adjacentes**, **méthode de Héron** pour approcher $\sqrt{2}$ : approfondissements possibles, traités en exercices.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
