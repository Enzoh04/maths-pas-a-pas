# Exercices corrigés — Continuité

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Fonctions continues | 1 à 6 |
| 2. Continuité et suites | 7 à 11 |
| 3. Théorème des valeurs intermédiaires | 12 à 18 |
| 4. Algorithmes d'approximation | 19 à 22 |
| 5. Synthèse | 23 à 28 |

---

## Thème 1 — Fonctions continues

*Méthode associée : [Méthode 1](methodes.md#methode-1-justifier-quune-fonction-est-continue).*

### Exercice 1 — Fonction définie par morceaux <span class="etoiles">★</span>

Soit $f$ définie sur $\mathbb{R}$ par $f(x) = x^2$ si $x \leq 1$ et $f(x) = 2x - 1$ si $x > 1$. Montrer que $f$ est continue sur $\mathbb{R}$.

??? success "Correction"
    Sur $]-\infty \,;\, 1[$ et sur $]1 \,;\, +\infty[$, $f$ coïncide avec une fonction polynôme, donc elle est continue.

    En $1$ : $f(1) = 1^2 = 1$. À gauche, $\displaystyle\lim_{x\to 1^-} x^2 = 1$. À droite, $\displaystyle\lim_{x\to 1^+} (2x - 1) = 1$. Les trois valeurs sont égales, donc $f$ est continue en $1$.

    Conclusion : $f$ est continue sur $\mathbb{R}$.

### Exercice 2 — Trouver le bon paramètre <span class="etoiles">★★</span>

Soit $a$ un réel et $f$ définie par $f(x) = ax + 1$ si $x < 2$, et $f(x) = x^2 - a$ si $x \geq 2$. Déterminer $a$ pour que $f$ soit continue sur $\mathbb{R}$.

??? success "Correction"
    $f$ est continue sur $]-\infty \,;\, 2[$ et sur $]2 \,;\, +\infty[$ (polynômes). En $2$ : $f(2) = 4 - a$, la limite à droite vaut aussi $4 - a$, et la limite à gauche vaut $2a + 1$.

    $f$ est continue en $2$ si et seulement si $2a + 1 = 4 - a$, c'est-à-dire $a = 1$.

### Exercice 3 — Prolonger par continuité <span class="etoiles">★</span>

Soit $g(x) = \dfrac{x^2 - 1}{x - 1}$ pour $x \neq 1$. Quelle valeur faut-il donner à $g(1)$ pour que $g$ soit continue sur $\mathbb{R}$ ?

??? success "Correction"
    Pour $x \neq 1$, $g(x) = \dfrac{(x - 1)(x + 1)}{x - 1} = x + 1$, donc $\displaystyle\lim_{x\to 1} g(x) = 2$. En posant $g(1) = 2$, on obtient $g(x) = x + 1$ pour tout réel $x$ : $g$ est continue sur $\mathbb{R}$. On dit qu'on a **prolongé $g$ par continuité** en $1$.

### Exercice 4 — Continue mais pas dérivable <span class="etoiles">★★</span>

Soit $f(x) = |x - 2|$.

1. Montrer que $f$ est continue sur $\mathbb{R}$.
2. Montrer que $f$ n'est pas dérivable en $2$. Interpréter graphiquement.

??? success "Correction"
    **1.** $f$ est la composée de $x \mapsto x - 2$ (continue) et de la valeur absolue (continue) : elle est continue sur $\mathbb{R}$.

    **2.** Le taux d'accroissement en $2$ vaut $\dfrac{f(2 + h) - f(2)}{h} = \dfrac{|h|}{h}$, égal à $1$ si $h > 0$ et à $-1$ si $h < 0$. Les limites à droite ($1$) et à gauche ($-1$) diffèrent : $f$ n'est pas dérivable en $2$. La courbe a un **point anguleux** en $(2 \,;\, 0)$, avec deux demi-tangentes de pentes $1$ et $-1$.

### Exercice 5 — Revenir à la définition <span class="etoiles">★★★</span>

1. Montrer que pour tous réels $x \geq 0$ et $a > 0$ : $\left|\sqrt{x} - \sqrt{a}\right| \leq \dfrac{|x - a|}{\sqrt{a}}$.
2. Soit $\varepsilon > 0$. Trouver $\delta > 0$ tel que, pour tout $x \geq 0$ avec $|x - a| < \delta$, on ait $\left|\sqrt{x} - \sqrt{a}\right| < \varepsilon$. Que vient-on de démontrer ?

??? success "Correction"
    **1.** En multipliant par la quantité conjuguée : $\sqrt{x} - \sqrt{a} = \dfrac{x - a}{\sqrt{x} + \sqrt{a}}$. Comme $\sqrt{x} + \sqrt{a} \geq \sqrt{a} > 0$, on obtient l'inégalité.

    **2.** On prend $\delta = \varepsilon\sqrt{a}$. Si $|x - a| < \delta$, alors $\left|\sqrt{x} - \sqrt{a}\right| \leq \dfrac{|x - a|}{\sqrt{a}} < \dfrac{\varepsilon\sqrt{a}}{\sqrt{a}} = \varepsilon$.

    On a démontré, avec la définition, que $\displaystyle\lim_{x \to a} \sqrt{x} = \sqrt{a}$ : la racine carrée est continue en tout $a > 0$.

### Exercice 6 — Vrai ou faux ? <span class="etoiles">★★</span>

Justifier chaque réponse.

1. Toute fonction continue sur $\mathbb{R}$ est dérivable sur $\mathbb{R}$.
2. La somme de deux fonctions discontinues peut être continue.
3. Si $f$ est continue sur $[a \,;\, b]$ et si $f(a)$ et $f(b)$ sont de signes contraires, alors $f$ s'annule sur $[a \,;\, b]$.
4. Si $f$ est continue sur $[a \,;\, b]$ et si $f(a)$ et $f(b)$ sont de même signe, alors $f$ ne s'annule pas sur $[a \,;\, b]$.
5. Si $f$ est continue sur $[0 \,;\, 1]$, l'équation $f(x) = \frac{f(0) + f(1)}{2}$ a au moins une solution dans $[0 \,;\, 1]$.

??? success "Correction"
    **1. Faux.** $x \mapsto |x|$ est continue mais pas dérivable en $0$.

    **2. Vrai.** $f = E$ (partie entière) et $g = -E$ sont discontinues en chaque entier, mais $f + g = 0$ est continue.

    **3. Vrai.** $0$ est compris entre $f(a)$ et $f(b)$ : c'est le TVI.

    **4. Faux.** $f(x) = x^2 - 1$ sur $[-2 \,;\, 2]$ : $f(-2) = f(2) = 3 > 0$, mais $f(1) = 0$.

    **5. Vrai.** $\frac{f(0) + f(1)}{2}$ est la moyenne de $f(0)$ et $f(1)$, donc elle est comprise entre ces deux nombres. On applique le TVI.

---

## Thème 2 — Continuité et suites

*Méthode associée : [Méthode 5](methodes.md#methode-5-calculer-la-limite-dune-suite-u_n1-fu_n).*

### Exercice 7 — Image d'une suite convergente <span class="etoiles">★</span>

Déterminer la limite de :

1. $a_n = e^{1/n}$ (pour $n \geq 1$)
2. $b_n = f\!\left(2 + \frac{1}{n}\right)$ avec $f(x) = x^2 - 3x$
3. $c_n = \sqrt{\dfrac{9n + 1}{n + 1}}$

??? success "Correction"
    1. $\frac{1}{n} \to 0$ et $\exp$ est continue en $0$ : $a_n \to e^0 = 1$.
    2. $2 + \frac{1}{n} \to 2$ et $f$ est continue en $2$ (polynôme) : $b_n \to f(2) = 4 - 6 = -2$.
    3. $\dfrac{9n + 1}{n + 1} \to 9$ et la racine carrée est continue en $9$ : $c_n \to 3$.

### Exercice 8 — Point fixe d'une fonction affine <span class="etoiles">★★</span>

On considère $u_0 = 1$ et $u_{n+1} = 0{,}5\,u_n + 3$.

1. Montrer par récurrence que $u_n \leq u_{n+1} \leq 6$ pour tout $n$.
2. En déduire que $(u_n)$ converge, puis déterminer sa limite par le théorème du point fixe.

??? success "Correction"
    **1.** Soit $f(x) = 0{,}5x + 3$, croissante sur $\mathbb{R}$. Initialisation : $u_0 = 1$, $u_1 = 3{,}5$, et $1 \leq 3{,}5 \leq 6$. Hérédité : si $u_n \leq u_{n+1} \leq 6$, on applique $f$ croissante : $f(u_n) \leq f(u_{n+1}) \leq f(6)$, soit $u_{n+1} \leq u_{n+2} \leq 6$.

    **2.** $(u_n)$ est croissante et majorée par $6$ : elle converge vers $\ell$. $f$ est continue, donc $\ell = 0{,}5\ell + 3$, soit $\ell = 6$.

### Exercice 9 — Une suite avec racine carrée <span class="etoiles">★★</span>

On considère $u_0 = 0$ et $u_{n+1} = \sqrt{u_n + 2}$. On admet (chapitre 1, exercice 24) que $0 \leq u_n \leq u_{n+1} \leq 2$ pour tout $n$. Déterminer la limite de $(u_n)$.

??? success "Correction"
    La suite est croissante et majorée par $2$ : elle converge vers un réel $\ell$, et $0 \leq \ell \leq 2$ par passage à la limite. La fonction $f(x) = \sqrt{x + 2}$ est continue sur $[-2 \,;\, +\infty[$, donc en $\ell$. Par le théorème du point fixe : $\ell = \sqrt{\ell + 2}$.

    En élevant au carré : $\ell^2 = \ell + 2$, soit $(\ell - 2)(\ell + 1) = 0$. Comme $\ell \geq 0$, on obtient $\ell = 2$.

### Exercice 10 — Une suite avec exponentielle <span class="etoiles">★★</span>

On considère $u_0 = 1$ et $u_{n+1} = u_n\,e^{-u_n}$.

1. Montrer par récurrence que $u_n > 0$ pour tout $n$.
2. Montrer que $(u_n)$ est décroissante.
3. En déduire que $(u_n)$ converge, et déterminer sa limite.

??? success "Correction"
    **1.** $u_0 = 1 > 0$. Si $u_n > 0$, alors $u_{n+1} = u_n e^{-u_n} > 0$ comme produit de deux nombres strictement positifs.

    **2.** $u_{n+1} - u_n = u_n(e^{-u_n} - 1)$. Comme $u_n > 0$, on a $-u_n < 0$ et $e^{-u_n} < 1$. Donc $u_{n+1} - u_n < 0$.

    **3.** La suite est décroissante et minorée par $0$ : elle converge vers $\ell \geq 0$. La fonction $f(x) = xe^{-x}$ est continue sur $\mathbb{R}$, donc $\ell = \ell e^{-\ell}$, soit $\ell(e^{-\ell} - 1) = 0$. Or $e^{-\ell} - 1 = 0 \iff \ell = 0$. Dans tous les cas, $\ell = 0$.

### Exercice 11 — Quand la continuité manque <span class="etoiles">★★★</span>

1. Soit $f$ définie sur $[0 \,;\, +\infty[$ par $f(0) = 1$ et $f(x) = \frac{x}{2}$ pour $x > 0$. On pose $u_0 = 1$ et $u_{n+1} = f(u_n)$. Exprimer $u_n$ en fonction de $n$ et déterminer sa limite $\ell$. A-t-on $f(\ell) = \ell$ ? Expliquer.
2. On considère $v_0 = 1$ et $v_{n+1} = 1 + \dfrac{1}{v_n}$. On **admet** que $(v_n)$ converge et que $v_n \geq 1$ pour tout $n$. Déterminer sa limite.

??? success "Correction"
    **1.** Tous les termes sont strictement positifs, donc $u_{n+1} = \frac{u_n}{2}$ : $(u_n)$ est géométrique de raison $\frac{1}{2}$, et $u_n = \frac{1}{2^n} \to 0$. Mais $f(0) = 1 \neq 0$.

    Le théorème du point fixe ne s'applique pas, car $f$ n'est **pas continue en $0$** : $\displaystyle\lim_{x\to 0^+} f(x) = 0 \neq f(0)$.

    **2.** La fonction $g(x) = 1 + \frac{1}{x}$ est continue sur $[1 \,;\, +\infty[$, et la limite $\ell$ vérifie $\ell \geq 1$. Donc $\ell = 1 + \frac{1}{\ell}$, soit $\ell^2 - \ell - 1 = 0$. Les solutions sont $\frac{1 \pm \sqrt{5}}{2}$, et comme $\ell \geq 1$ :

    $$\ell = \frac{1 + \sqrt{5}}{2} \approx 1{,}618.$$

    C'est le **nombre d'or**. Les termes $v_n$ sont des quotients de deux nombres de Fibonacci consécutifs : $1, 2, \frac{3}{2}, \frac{5}{3}, \frac{8}{5}, \dots$

---

## Thème 3 — Théorème des valeurs intermédiaires

*Méthodes associées : [Méthode 2](methodes.md#methode-2-appliquer-le-tvi-ou-son-corollaire) et [Méthode 3](methodes.md#methode-3-compter-les-solutions-sur-tout-le-domaine).*

### Exercice 12 — Une application directe <span class="etoiles">★</span>

Soit $f(x) = x^3 + x - 1$.

1. Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ dans $[0 \,;\, 1]$.
2. Donner un encadrement de $\alpha$ d'amplitude $0{,}1$.

??? success "Correction"
    **1.** $f$ est continue (polynôme) et $f'(x) = 3x^2 + 1 > 0$ : $f$ est strictement croissante. $f(0) = -1 < 0$ et $f(1) = 1 > 0$. D'après le corollaire du TVI, l'équation $f(x) = 0$ admet une unique solution $\alpha \in [0 \,;\, 1]$.

    **2.** $f(0{,}6) = -0{,}184 < 0$ et $f(0{,}7) = 0{,}043 > 0$, donc $0{,}6 < \alpha < 0{,}7$.

### Exercice 13 — Sur tout $\mathbb{R}$ <span class="etoiles">★★</span>

Soit $f(x) = e^x + x$ sur $\mathbb{R}$.

1. Déterminer les limites de $f$ en $-\infty$ et en $+\infty$, et ses variations.
2. Montrer que l'équation $f(x) = 0$ a une unique solution $\alpha$ dans $\mathbb{R}$, puis que $\alpha \in [-1 \,;\, 0]$.
3. Donner un encadrement de $\alpha$ d'amplitude $10^{-2}$.

??? success "Correction"
    **1.** En $-\infty$ : $e^x \to 0$ et $x \to -\infty$, donc $f \to -\infty$. En $+\infty$ : $f \to +\infty$. $f'(x) = e^x + 1 > 0$ : $f$ est strictement croissante.

    **2.** $f$ est continue et strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$ : l'équation $f(x) = 0$ a une unique solution $\alpha$ (corollaire étendu). $f(-1) = e^{-1} - 1 < 0$ et $f(0) = 1 > 0$, donc $\alpha \in \,]-1 \,;\, 0[$.

    **3.** $f(-0{,}57) \approx -0{,}0045 < 0$ et $f(-0{,}56) \approx 0{,}011 > 0$, donc $-0{,}57 < \alpha < -0{,}56$.

### Exercice 14 — Trois solutions <span class="etoiles">★★</span>

Montrer que l'équation $x^3 - 3x + 1 = 0$ admet exactement trois solutions réelles, et donner pour chacune un intervalle d'amplitude $1$ qui la contient.

??? success "Correction"
    Soit $f(x) = x^3 - 3x + 1$, continue sur $\mathbb{R}$. $f'(x) = 3(x - 1)(x + 1)$, $f(-1) = 3$, $f(1) = -1$, et les limites en $\pm\infty$ sont $\pm\infty$.

    | $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $f(x)$ | $-\infty$ | $\nearrow$ | $3$ | $\searrow$ | $-1$ | $\nearrow$ | $+\infty$ |

    Sur chacun des trois intervalles, $f$ est continue et strictement monotone, et $0$ est compris entre les valeurs aux bornes : une solution par intervalle, soit trois au total.

    - $f(-2) = -1 < 0$ et $f(-1) = 3 > 0$ : la première est dans $]-2 \,;\, -1[$.
    - $f(0) = 1 > 0$ et $f(1) = -1 < 0$ : la deuxième est dans $]0 \,;\, 1[$.
    - $f(1) = -1 < 0$ et $f(2) = 3 > 0$ : la troisième est dans $]1 \,;\, 2[$.

### Exercice 15 — Discuter selon un paramètre <span class="etoiles">★★</span>

Soit $f(x) = x\,e^{-x}$ sur $[0 \,;\, +\infty[$. On rappelle (chapitre 2, exercice 23) que $f$ est croissante sur $[0 \,;\, 1]$, décroissante sur $[1 \,;\, +\infty[$, avec $f(0) = 0$, $f(1) = \frac{1}{e}$ et $\displaystyle\lim_{+\infty} f = 0$.

Selon la valeur du réel $k$, déterminer le nombre de solutions de l'équation $f(x) = k$ sur $[0 \,;\, +\infty[$.

??? success "Correction"
    $f$ est continue et strictement monotone sur $[0 \,;\, 1]$ et sur $[1 \,;\, +\infty[$. Elle prend toutes ses valeurs dans $\left[0 \,;\, \frac{1}{e}\right]$.

    - Si $k < 0$ ou $k > \frac{1}{e}$ : **aucune** solution.
    - Si $k = 0$ : **une** solution, $x = 0$ (sur $]1 \,;\, +\infty[$, $f(x) > 0$, et la valeur $0$ n'est qu'une limite).
    - Si $0 < k < \frac{1}{e}$ : **deux** solutions, une dans $]0 \,;\, 1[$ et une dans $]1 \,;\, +\infty[$.
    - Si $k = \frac{1}{e}$ : **une** solution, $x = 1$.

### Exercice 16 — Un théorème de point fixe <span class="etoiles">★★★</span>

Soit $f$ une fonction continue sur $[0 \,;\, 1]$, à valeurs dans $[0 \,;\, 1]$. Montrer qu'il existe $c \in [0 \,;\, 1]$ tel que $f(c) = c$. *Indication : étudier $g(x) = f(x) - x$.*

??? success "Correction"
    $g$ est continue sur $[0 \,;\, 1]$ comme différence de fonctions continues.

    - $g(0) = f(0) - 0 = f(0) \geq 0$, car $f$ est à valeurs dans $[0 \,;\, 1]$ ;
    - $g(1) = f(1) - 1 \leq 0$.

    $0$ est compris entre $g(1)$ et $g(0)$ : d'après le TVI, il existe $c \in [0 \,;\, 1]$ tel que $g(c) = 0$, c'est-à-dire $f(c) = c$.

    *Graphiquement : la courbe de $f$ va du côté gauche au côté droit du carré $[0 \,;\, 1]^2$, et elle doit couper la diagonale $y = x$.*

### Exercice 17 — Polynômes de degré 3 <span class="etoiles">★★</span>

Soit $P(x) = x^3 + bx^2 + cx + d$, avec $b$, $c$, $d$ réels. Montrer que $P$ admet au moins une racine réelle.

??? success "Correction"
    Par la règle du terme dominant, $\displaystyle\lim_{x\to-\infty} P(x) = -\infty$ et $\displaystyle\lim_{x\to+\infty} P(x) = +\infty$. Il existe donc un réel $a$ tel que $P(a) < 0$, et un réel $a'$ tel que $P(a') > 0$, avec $a < a'$. $P$ est continue sur $[a \,;\, a']$ et $0$ est compris entre $P(a)$ et $P(a')$ : d'après le TVI, $P$ s'annule sur $[a \,;\, a']$.

    *Ce raisonnement marche pour tout polynôme de degré impair. Pour un degré pair, c'est faux : $x^2 + 1$ n'a pas de racine réelle.*

### Exercice 18 — Le randonneur <span class="etoiles">★★★</span>

Un randonneur monte au sommet d'une montagne : il part du pied à 8 h et arrive au sommet à 18 h. Le lendemain, il redescend **par le même chemin**, de 8 h à 18 h, à un rythme quelconque (pauses, accélérations…). Montrer qu'il existe une heure de la journée à laquelle il se trouve exactement au même endroit les deux jours.

*On note $L$ la longueur du chemin, et $p_1(t)$, $p_2(t)$ la distance parcourue depuis le pied à l'heure $t$, le premier et le second jour. On admet que $p_1$ et $p_2$ sont continues sur $[8 \,;\, 18]$.*

??? success "Correction"
    On pose $d(t) = p_1(t) - p_2(t)$, continue sur $[8 \,;\, 18]$.

    - À 8 h : $p_1(8) = 0$ (au pied) et $p_2(8) = L$ (au sommet), donc $d(8) = -L < 0$.
    - À 18 h : $p_1(18) = L$ et $p_2(18) = 0$, donc $d(18) = L > 0$.

    D'après le TVI, il existe $t_0 \in [8 \,;\, 18]$ tel que $d(t_0) = 0$, soit $p_1(t_0) = p_2(t_0)$ : à l'heure $t_0$, il est au même endroit les deux jours.

    *Astuce pour se convaincre : imagine deux randonneurs, l'un qui monte et l'autre qui descend le même jour. Ils se croisent forcément !*

---

## Thème 4 — Algorithmes d'approximation

*Méthode associée : [Méthode 4](methodes.md#methode-4-encadrer-une-solution).*

### Exercice 19 — Dichotomie à la main <span class="etoiles">★</span>

On cherche la solution positive de $x^2 - 2 = 0$ dans $[1 \,;\, 2]$. Effectuer trois étapes de dichotomie et donner l'encadrement obtenu.

??? success "Correction"
    Soit $f(x) = x^2 - 2$ : $f(1) = -1 < 0$ et $f(2) = 2 > 0$.

    1. $m = 1{,}5$ : $f(1{,}5) = 0{,}25 > 0$. On garde $[1 \,;\, 1{,}5]$.
    2. $m = 1{,}25$ : $f(1{,}25) = -0{,}4375 < 0$. On garde $[1{,}25 \,;\, 1{,}5]$.
    3. $m = 1{,}375$ : $f(1{,}375) \approx -0{,}109 < 0$. On garde $[1{,}375 \,;\, 1{,}5]$.

    Donc $1{,}375 < \sqrt{2} < 1{,}5$, encadrement d'amplitude $\frac{1}{8} = 0{,}125$.

### Exercice 20 — Nombre d'étapes <span class="etoiles">★★</span>

1. On applique la dichotomie sur un intervalle de longueur $1$. Combien d'étapes faut-il pour obtenir un encadrement d'amplitude inférieure à $10^{-3}$ ? à $10^{-6}$ ?
2. Avec un balayage de pas $10^{-6}$ sur le même intervalle, combien de calculs de $f(x)$ peut-il falloir ?

??? success "Correction"
    **1.** Après $n$ étapes, l'amplitude est $\frac{1}{2^n}$. Il faut $2^n \geq 1000$, soit $n = 10$ ($2^{10} = 1024$). Pour $10^{-6}$ : $2^n \geq 10^6$, soit $n = 20$ ($2^{20} = 1\,048\,576$).

    **2.** Jusqu'à $10^6$ calculs, contre $20$ pour la dichotomie. La dichotomie est beaucoup plus efficace : chaque étape fait gagner un « chiffre binaire » de précision.

### Exercice 21 — Balayage en Python <span class="etoiles">★★</span>

On reprend $f(x) = e^x + x$ et la solution $\alpha \in [-1 \,;\, 0]$ de l'exercice 13.

1. Compléter la fonction suivante pour qu'elle renvoie la plus petite valeur de $x$ de la forme $-1 + 0{,}01k$ telle que $f(x) \geq 0$.

    ```python
    from math import exp

    def balayage():
        x = -1
        while ......:
            x = ......
        return x
    ```

2. Quelle valeur renvoie-t-elle ? Quel encadrement de $\alpha$ en déduit-on ?

??? success "Correction"
    **1.**

    ```python
    from math import exp

    def balayage():
        x = -1
        while exp(x) + x < 0:
            x = x + 0.01
        return x
    ```

    **2.** Elle renvoie $-0{,}56$ (à un arrondi machine près). Comme $f(-0{,}57) < 0 \leq f(-0{,}56)$, on a $-0{,}57 < \alpha \leq -0{,}56$.

    *En pratique, les flottants comme $0{,}01$ ne sont pas représentés exactement en machine. On peut écrire `x = round(x + 0.01, 2)` pour éviter les petites erreurs d'arrondi.*

### Exercice 22 — Programmer la dichotomie <span class="etoiles">★★★</span>

1. Écrire une fonction Python `dicho(a, b, n)` qui applique $n$ étapes de dichotomie à $f(x) = x^3 + x - 1$ sur $[a \,;\, b]$ et renvoie l'encadrement obtenu.
2. Justifier que l'algorithme fonctionne : pourquoi garde-t-on toujours un intervalle qui contient la solution ?

??? success "Correction"
    **1.**

    ```python
    def f(x):
        return x**3 + x - 1

    def dicho(a, b, n):
        for i in range(n):
            m = (a + b) / 2
            if f(a) * f(m) <= 0:
                b = m
            else:
                a = m
        return a, b
    ```

    `dicho(0, 1, 10)` renvoie un intervalle d'amplitude $\frac{1}{1024}$ contenant $\alpha \approx 0{,}6823$.

    **2.** À chaque étape, $f(a)$ et $f(b)$ sont de signes contraires (ou l'un est nul). Si $f(a) \times f(m) \leq 0$, alors $f(a)$ et $f(m)$ sont de signes contraires et, par le TVI, $[a \,;\, m]$ contient une solution. Sinon, $f(m)$ est du signe de $f(a)$, donc de signe contraire à $f(b)$, et c'est $[m \,;\, b]$ qui en contient une. Comme $f$ est ici strictement croissante, cette solution est l'unique $\alpha$.

---

## Thème 5 — Synthèse

### Exercice 23 — Une unique solution sur $\mathbb{R}$ <span class="etoiles">★★</span>

Soit $g(x) = x^3 - 3x - 3$.

1. Dresser le tableau de variations de $g$.
2. Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$ sur $\mathbb{R}$, et que $2 < \alpha < 3$.
3. Donner un encadrement de $\alpha$ d'amplitude $10^{-2}$.

??? success "Correction"
    **1.** $g'(x) = 3(x - 1)(x + 1)$. $g(-1) = -1 + 3 - 3 = -1$ et $g(1) = 1 - 3 - 3 = -5$.

    | $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $g(x)$ | $-\infty$ | $\nearrow$ | $-1$ | $\searrow$ | $-5$ | $\nearrow$ | $+\infty$ |

    **2.** Sur $]-\infty \,;\, 1]$, le maximum de $g$ est $-1 < 0$ : pas de solution. Sur $[1 \,;\, +\infty[$, $g$ est continue, strictement croissante, de $-5$ à $+\infty$ : une unique solution $\alpha$. Comme $g(2) = -1 < 0$ et $g(3) = 15 > 0$, on a $2 < \alpha < 3$.

    **3.** $g(2{,}10) \approx -0{,}039 < 0$ et $g(2{,}11) \approx 0{,}064 > 0$ : $2{,}10 < \alpha < 2{,}11$.

### Exercice 24 — Utiliser $\alpha$ pour étudier une autre fonction <span class="etoiles">★★</span>

On reprend $g$ et $\alpha$ de l'exercice 23. Soit $h(x) = \dfrac{x^4}{4} - \dfrac{3x^2}{2} - 3x$.

1. Calculer $h'(x)$.
2. En déduire le signe de $h'(x)$ puis les variations de $h$.

??? success "Correction"
    **1.** $h'(x) = x^3 - 3x - 3 = g(x)$.

    **2.** D'après l'exercice 23, $g(x) < 0$ pour $x < \alpha$ et $g(x) > 0$ pour $x > \alpha$. Donc $h$ est décroissante sur $]-\infty \,;\, \alpha]$ et croissante sur $[\alpha \,;\, +\infty[$ : elle admet un minimum en $\alpha$.

    *C'est un schéma très fréquent au bac : on étudie une fonction auxiliaire $g$ pour obtenir le signe de la dérivée d'une autre fonction.*

### Exercice 25 — Résoudre $e^x = 3 - x$ <span class="etoiles">★★</span>

Montrer que l'équation $e^x = 3 - x$ admet une unique solution réelle $\alpha$, et que $0{,}7 < \alpha < 0{,}8$.

??? success "Correction"
    On pose $f(x) = e^x + x - 3$ : l'équation équivaut à $f(x) = 0$. $f$ est continue et $f'(x) = e^x + 1 > 0$. En $-\infty$, $f \to -\infty$ ; en $+\infty$, $f \to +\infty$. Par le corollaire du TVI, il existe une unique solution $\alpha$.

    $f(0{,}7) \approx -0{,}286 < 0$ et $f(0{,}8) \approx 0{,}026 > 0$, donc $0{,}7 < \alpha < 0{,}8$.

### Exercice 26 — Prolongement de $\frac{e^x - 1}{x}$ <span class="etoiles">★★★</span>

Soit $f$ définie sur $\mathbb{R}$ par $f(x) = \dfrac{e^x - 1}{x}$ si $x \neq 0$, et $f(0) = 1$.

1. Montrer que $f$ est continue sur $\mathbb{R}$.
2. Montrer que $f(x) > 0$ pour tout réel $x$.

??? success "Correction"
    **1.** Sur $]-\infty \,;\, 0[$ et sur $]0 \,;\, +\infty[$, $f$ est un quotient de fonctions continues à dénominateur non nul. En $0$ : $\displaystyle\lim_{x\to 0} \frac{e^x - 1}{x} = 1 = f(0)$ (chapitre 2, § 7.5). $f$ est donc continue sur $\mathbb{R}$.

    **2.** $f(0) = 1 > 0$. Pour $x > 0$ : $e^x > 1$ donc $e^x - 1 > 0$, et $x > 0$, donc $f(x) > 0$. Pour $x < 0$ : $e^x - 1 < 0$ et $x < 0$, donc $f(x) > 0$.

### Exercice 27 — Intersection de deux courbes <span class="etoiles">★★</span>

Montrer que les courbes de $x \mapsto e^{-x}$ et de $x \mapsto x$ se coupent en un unique point, dont l'abscisse $\alpha$ vérifie $0 < \alpha < 1$.

??? success "Correction"
    Soit $g(x) = e^{-x} - x$. Les courbes se coupent aux points d'abscisse $x$ tels que $g(x) = 0$. $g$ est continue et $g'(x) = -e^{-x} - 1 < 0$ : $g$ est strictement décroissante sur $\mathbb{R}$. Limites : $g \to +\infty$ en $-\infty$ et $g \to -\infty$ en $+\infty$. Il y a donc une unique solution $\alpha$.

    $g(0) = 1 > 0$ et $g(1) = e^{-1} - 1 < 0$, donc $0 < \alpha < 1$. *(Valeur approchée : $\alpha \approx 0{,}5671$.)*

### Exercice 28 — Retrouver $\alpha$ comme limite <span class="etoiles">★★★</span>

On reprend $\alpha$ de l'exercice 27, et on pose $u_0 = 0$ et $u_{n+1} = e^{-u_n}$.

1. Calculer des valeurs approchées de $u_1$ à $u_5$. Que remarque-t-on ?
2. On **admet** que $(u_n)$ converge. Montrer que sa limite est $\alpha$.

??? success "Correction"
    **1.** $u_1 = 1$, $u_2 \approx 0{,}3679$, $u_3 \approx 0{,}6922$, $u_4 \approx 0{,}5005$, $u_5 \approx 0{,}6062$. La suite n'est pas monotone : elle oscille autour d'une valeur proche de $0{,}57$, en s'en rapprochant.

    **2.** Soit $\ell$ la limite. La fonction $x \mapsto e^{-x}$ est continue sur $\mathbb{R}$, donc par le théorème du point fixe, $\ell = e^{-\ell}$, c'est-à-dire $g(\ell) = 0$ avec la fonction $g$ de l'exercice 27. Comme $\alpha$ est l'unique solution de cette équation, $\ell = \alpha$.

    *La preuve de la convergence utilise le fait que $(u_{2n})$ et $(u_{2n+1})$ sont monotones (suites adjacentes), ce qui dépasse un peu le programme.*
