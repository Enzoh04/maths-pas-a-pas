# Exercices corrigés — Suites : récurrence et limites

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

29 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Raisonnement par récurrence | 1 à 7 |
| 2. Calculs de limites | 8 à 13 |
| 3. Théorèmes de comparaison | 14 à 18 |
| 4. Suites géométriques et arithmético-géométriques | 19 à 23 |
| 5. Convergence monotone et suites récurrentes | 24 à 27 |
| 6. Algorithmique | 28 et 29 |

---

## Thème 1 — Raisonnement par récurrence

*Méthode associée : [Méthode 1](methodes.md#methode-1-rediger-une-demonstration-par-recurrence).*

### Exercice 1 — Somme des impairs <span class="etoiles">★</span>

Démontrer par récurrence que, pour tout entier $n \geq 1$ :

$$1 + 3 + 5 + \dots + (2n - 1) = n^2.$$

??? success "Correction"
    Pour $n \geq 1$, on note $\mathcal{P}(n)$ : « $1 + 3 + \dots + (2n-1) = n^2$ ».

    **Initialisation.** Pour $n = 1$, le membre de gauche vaut $1$ et le membre de droite $1^2 = 1$. $\mathcal{P}(1)$ est vraie.

    **Hérédité.** Soit $n \geq 1$ tel que $\mathcal{P}(n)$ est vraie. Le terme suivant de la somme est $2(n+1) - 1 = 2n + 1$, donc :

    $$1 + 3 + \dots + (2n-1) + (2n+1) = n^2 + 2n + 1 = (n+1)^2.$$

    $\mathcal{P}(n+1)$ est vraie.

    **Conclusion.** Par récurrence, pour tout $n \geq 1$, $1 + 3 + \dots + (2n-1) = n^2$.

### Exercice 2 — Formule explicite <span class="etoiles">★</span>

On définit $(u_n)$ par $u_0 = 1$ et, pour tout $n \in \mathbb{N}$, $u_{n+1} = u_n + 2n + 3$.

1. Calculer $u_1$, $u_2$ et $u_3$.
2. Conjecturer une expression de $u_n$ en fonction de $n$, puis la démontrer par récurrence.

??? success "Correction"
    **1.** $u_1 = 1 + 0 + 3 = 4$, $u_2 = 4 + 2 + 3 = 9$, $u_3 = 9 + 4 + 3 = 16$.

    **2.** On reconnaît des carrés : on conjecture $u_n = (n+1)^2$.

    Soit $\mathcal{P}(n)$ : « $u_n = (n+1)^2$ ».

    - Initialisation : $u_0 = 1 = (0+1)^2$.
    - Hérédité : supposons $u_n = (n+1)^2$ pour un certain $n$. Alors

    $$u_{n+1} = (n+1)^2 + 2n + 3 = n^2 + 2n + 1 + 2n + 3 = n^2 + 4n + 4 = (n+2)^2.$$

    - Conclusion : pour tout $n \in \mathbb{N}$, $u_n = (n+1)^2$.

### Exercice 3 — Somme des carrés <span class="etoiles">★</span>

Démontrer par récurrence que, pour tout entier $n \geq 1$ :

$$1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}.$$

??? success "Correction"
    Soit $\mathcal{P}(n)$ : « $1^2 + \dots + n^2 = \dfrac{n(n+1)(2n+1)}{6}$ ».

    **Initialisation.** $1^2 = 1$ et $\dfrac{1 \times 2 \times 3}{6} = 1$ : $\mathcal{P}(1)$ est vraie.

    **Hérédité.** Supposons $\mathcal{P}(n)$ vraie pour un certain $n \geq 1$. Alors :

    $$1^2 + \dots + n^2 + (n+1)^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)\left[n(2n+1) + 6(n+1)\right]}{6} = \frac{(n+1)(2n^2 + 7n + 6)}{6}.$$

    Or $(n+2)(2n+3) = 2n^2 + 3n + 4n + 6 = 2n^2 + 7n + 6$. Donc la somme vaut $\dfrac{(n+1)(n+2)(2n+3)}{6}$, ce qui est exactement $\mathcal{P}(n+1)$, puisque $2(n+1) + 1 = 2n + 3$.

    **Conclusion.** La formule est vraie pour tout $n \geq 1$.

    !!! tip "Astuce"
        Factorise par $(n+1)$ **avant** de développer : les calculs sont beaucoup plus courts.

### Exercice 4 — Divisibilité <span class="etoiles">★★</span>

Démontrer que, pour tout entier naturel $n$, $4^n - 1$ est divisible par $3$.

??? success "Correction"
    Soit $\mathcal{P}(n)$ : « il existe un entier $k$ tel que $4^n - 1 = 3k$ ».

    **Initialisation.** $4^0 - 1 = 0 = 3 \times 0$ : $\mathcal{P}(0)$ est vraie.

    **Hérédité.** Supposons $4^n - 1 = 3k$ avec $k$ entier. Alors $4^n = 3k + 1$ et

    $$4^{n+1} - 1 = 4 \times 4^n - 1 = 4(3k + 1) - 1 = 12k + 3 = 3(4k + 1).$$

    Comme $4k + 1$ est un entier, $4^{n+1} - 1$ est divisible par $3$.

    **Conclusion.** Pour tout $n \in \mathbb{N}$, $4^n - 1$ est divisible par $3$.

### Exercice 5 — Conjecturer puis démontrer <span class="etoiles">★★</span>

On définit $(u_n)$ par $u_0 = 2$ et $u_{n+1} = 2u_n - 1$.

1. Calculer $u_1$, $u_2$, $u_3$ et $u_4$.
2. Conjecturer une expression de $u_n$ en fonction de $n$ et la démontrer.
3. En déduire la limite de $(u_n)$.

??? success "Correction"
    **1.** $u_1 = 3$, $u_2 = 5$, $u_3 = 9$, $u_4 = 17$.

    **2.** Ce sont les puissances de $2$ augmentées de $1$ : $2 = 2^0 + 1$, $3 = 2^1 + 1$, $5 = 2^2 + 1$… On conjecture $u_n = 2^n + 1$.

    - Initialisation : $2^0 + 1 = 2 = u_0$.
    - Hérédité : si $u_n = 2^n + 1$, alors $u_{n+1} = 2(2^n + 1) - 1 = 2^{n+1} + 2 - 1 = 2^{n+1} + 1$.
    - Conclusion : pour tout $n$, $u_n = 2^n + 1$.

    **3.** $2 > 1$ donc $\lim 2^n = +\infty$, et $\lim u_n = +\infty$.

### Exercice 6 — Une inégalité avec la factorielle <span class="etoiles">★★</span>

Pour $n \geq 1$, on note $n! = 1 \times 2 \times \dots \times n$ (« factorielle $n$ »). Ainsi $(n+1)! = (n+1) \times n!$.

1. Démontrer par récurrence que pour tout $n \geq 1$ : $n! \geq 2^{n-1}$.
2. En déduire la limite de $(n!)$.

??? success "Correction"
    **1.** Soit $\mathcal{P}(n)$ : « $n! \geq 2^{n-1}$ ».

    - Initialisation : $1! = 1$ et $2^0 = 1$ : $\mathcal{P}(1)$ est vraie.
    - Hérédité : supposons $n! \geq 2^{n-1}$ pour un $n \geq 1$. Comme $n + 1 > 0$ :

    $$(n+1)! = (n+1) \times n! \geq (n+1) \times 2^{n-1}.$$

    Or $n \geq 1$ donc $n + 1 \geq 2$, et $(n+1) \times 2^{n-1} \geq 2 \times 2^{n-1} = 2^n$. Donc $(n+1)! \geq 2^n$ : $\mathcal{P}(n+1)$ est vraie.

    - Conclusion : pour tout $n \geq 1$, $n! \geq 2^{n-1}$.

    **2.** $\lim 2^{n-1} = +\infty$ (car $2 > 1$). Par comparaison, $\lim n! = +\infty$.

### Exercice 7 — Comparer $2^n$ et $n^2$ <span class="etoiles">★★★</span>

1. Montrer que pour tout entier $n \geq 3$ : $2n^2 \geq (n+1)^2$.
2. Démontrer par récurrence que pour tout entier $n \geq 4$ : $2^n \geq n^2$.
3. En déduire $\displaystyle\lim_{n\to+\infty} \frac{n}{2^n}$.

??? success "Correction"
    **1.** $2n^2 - (n+1)^2 = n^2 - 2n - 1 = (n-1)^2 - 2$. Pour $n \geq 3$, $(n-1)^2 \geq 4 > 2$, donc $2n^2 - (n+1)^2 > 0$.

    **2.** Soit $\mathcal{P}(n)$ : « $2^n \geq n^2$ », pour $n \geq 4$.

    - Initialisation : $2^4 = 16$ et $4^2 = 16$. $\mathcal{P}(4)$ est vraie.
    - Hérédité : soit $n \geq 4$ tel que $2^n \geq n^2$. Alors $2^{n+1} = 2 \times 2^n \geq 2n^2$. D'après la question 1 (valable car $n \geq 4 \geq 3$), $2n^2 \geq (n+1)^2$. Donc $2^{n+1} \geq (n+1)^2$.
    - Conclusion : pour tout $n \geq 4$, $2^n \geq n^2$.

    !!! note "Remarque"
        La propriété est fausse pour $n = 3$ ($8 < 9$) : d'où l'initialisation à $n = 4$.

    **3.** Pour $n \geq 4$, $2^n \geq n^2 > 0$, donc $\dfrac{1}{2^n} \leq \dfrac{1}{n^2}$ et

    $$0 \leq \frac{n}{2^n} \leq \frac{n}{n^2} = \frac{1}{n}.$$

    Comme $\lim \dfrac{1}{n} = 0$, le théorème des gendarmes donne $\displaystyle\lim_{n\to+\infty} \frac{n}{2^n} = 0$.

---

## Thème 2 — Calculs de limites

*Méthode associée : [Méthode 2](methodes.md#methode-2-lever-une-forme-indeterminee).*

### Exercice 8 — Calculs de limites <span class="etoiles">★</span>

Déterminer la limite de chaque suite.

1. $a_n = 3n^2 - 5n + 1$
2. $b_n = \dfrac{2n + 1}{n + 3}$
3. $c_n = \dfrac{1 - n}{n^2 + 1}$
4. $d_n = 5 - \dfrac{2}{\sqrt{n}}$ (pour $n \geq 1$)

??? success "Correction"
    **1.** Forme $\infty - \infty$. On factorise par $n^2$ : $a_n = n^2\left(3 - \dfrac{5}{n} + \dfrac{1}{n^2}\right)$. La parenthèse tend vers $3$ et $n^2 \to +\infty$, donc $\lim a_n = +\infty$.

    **2.** Forme $\dfrac{\infty}{\infty}$. On factorise par $n$ :

    $$b_n = \frac{n\left(2 + \frac{1}{n}\right)}{n\left(1 + \frac{3}{n}\right)} = \frac{2 + \frac{1}{n}}{1 + \frac{3}{n}} \longrightarrow \frac{2}{1} = 2.$$

    **3.** Forme $\dfrac{\infty}{\infty}$. On factorise par les termes dominants :

    $$c_n = \frac{n\left(\frac{1}{n} - 1\right)}{n^2\left(1 + \frac{1}{n^2}\right)} = \frac{1}{n} \times \frac{\frac{1}{n} - 1}{1 + \frac{1}{n^2}}.$$

    Le premier facteur tend vers $0$ et le second vers $-1$, donc $\lim c_n = 0$.

    **4.** $\lim \sqrt{n} = +\infty$ donc $\lim \dfrac{2}{\sqrt{n}} = 0$, et $\lim d_n = 5$.

### Exercice 9 — Quotients <span class="etoiles">★★</span>

Déterminer la limite de chaque suite (pour $n \geq 1$).

1. $a_n = \dfrac{2n^2 - n}{n + 5}$
2. $b_n = \dfrac{n - \sqrt{n}}{n + \sqrt{n}}$
3. $c_n = \dfrac{3^n + 2^n}{3^n - 2^n}$
4. $d_n = \dfrac{2^n - 5^n}{4^n}$

??? success "Correction"
    **1.** On factorise par $n$ : $a_n = \dfrac{n(2n - 1)}{n\left(1 + \frac{5}{n}\right)} = \dfrac{2n - 1}{1 + \frac{5}{n}}$. Le numérateur tend vers $+\infty$ et le dénominateur vers $1$ : $\lim a_n = +\infty$.

    **2.** On divise numérateur et dénominateur par $n$, sachant que $\dfrac{\sqrt{n}}{n} = \dfrac{1}{\sqrt{n}}$ :

    $$b_n = \frac{1 - \frac{1}{\sqrt{n}}}{1 + \frac{1}{\sqrt{n}}} \longrightarrow \frac{1}{1} = 1.$$

    **3.** On divise par $3^n$, la plus grande puissance :

    $$c_n = \frac{1 + \left(\frac{2}{3}\right)^n}{1 - \left(\frac{2}{3}\right)^n}.$$

    Comme $0 < \frac{2}{3} < 1$, $\left(\frac{2}{3}\right)^n \to 0$ et $\lim c_n = 1$.

    **4.** $d_n = \dfrac{2^n}{4^n} - \dfrac{5^n}{4^n} = \left(\dfrac{1}{2}\right)^n - \left(\dfrac{5}{4}\right)^n$. Le premier terme tend vers $0$, le second vers $+\infty$ (car $\frac{5}{4} > 1$). Donc $\lim d_n = -\infty$.

### Exercice 10 — Quantité conjuguée <span class="etoiles">★★</span>

1. Déterminer $\displaystyle\lim_{n\to+\infty} \left(\sqrt{n+1} - \sqrt{n}\right)$.
2. Déterminer $\displaystyle\lim_{n\to+\infty} \left(\sqrt{n^2 + n} - n\right)$.

??? success "Correction"
    **1.** Forme $\infty - \infty$. On multiplie par la quantité conjuguée :

    $$\sqrt{n+1} - \sqrt{n} = \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}}.$$

    Le dénominateur tend vers $+\infty$, donc la limite est $0$.

    **2.** Forme $\infty - \infty$. Pour $n \geq 1$ :

    $$\sqrt{n^2 + n} - n = \frac{(n^2 + n) - n^2}{\sqrt{n^2 + n} + n} = \frac{n}{\sqrt{n^2 + n} + n}.$$

    On a encore une forme $\dfrac{\infty}{\infty}$. Comme $n > 0$, $\sqrt{n^2 + n} = n\sqrt{1 + \frac{1}{n}}$, d'où

    $$\sqrt{n^2 + n} - n = \frac{n}{n\left(\sqrt{1 + \frac{1}{n}} + 1\right)} = \frac{1}{\sqrt{1 + \frac{1}{n}} + 1} \longrightarrow \frac{1}{1 + 1} = \frac{1}{2}.$$

### Exercice 11 — Différence de deux racines <span class="etoiles">★★★</span>

Déterminer $\displaystyle\lim_{n\to+\infty} \left(\sqrt{n^2 + 3n} - \sqrt{n^2 + 1}\right)$.

??? success "Correction"
    Forme $\infty - \infty$. Avec la quantité conjuguée :

    $$\sqrt{n^2 + 3n} - \sqrt{n^2 + 1} = \frac{(n^2 + 3n) - (n^2 + 1)}{\sqrt{n^2 + 3n} + \sqrt{n^2 + 1}} = \frac{3n - 1}{\sqrt{n^2 + 3n} + \sqrt{n^2 + 1}}.$$

    Pour $n \geq 1$, on factorise par $n$ en haut et en bas, en utilisant $\sqrt{n^2 + 3n} = n\sqrt{1 + \frac{3}{n}}$ et $\sqrt{n^2 + 1} = n\sqrt{1 + \frac{1}{n^2}}$ :

    $$\frac{n\left(3 - \frac{1}{n}\right)}{n\left(\sqrt{1 + \frac{3}{n}} + \sqrt{1 + \frac{1}{n^2}}\right)} = \frac{3 - \frac{1}{n}}{\sqrt{1 + \frac{3}{n}} + \sqrt{1 + \frac{1}{n^2}}} \longrightarrow \frac{3}{1 + 1} = \frac{3}{2}.$$

### Exercice 12 — Somme télescopique <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $S_n = \displaystyle\sum_{k=1}^{n} \frac{1}{k(k+1)}$.

1. Vérifier que pour tout $k \geq 1$ : $\dfrac{1}{k(k+1)} = \dfrac{1}{k} - \dfrac{1}{k+1}$.
2. En déduire une expression simple de $S_n$, puis sa limite.

??? success "Correction"
    **1.** $\dfrac{1}{k} - \dfrac{1}{k+1} = \dfrac{(k+1) - k}{k(k+1)} = \dfrac{1}{k(k+1)}$.

    **2.** En écrivant la somme terme à terme, les termes intermédiaires s'annulent deux à deux :

    $$S_n = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right) = 1 - \frac{1}{n+1}.$$

    Comme $\lim \dfrac{1}{n+1} = 0$, on obtient $\lim S_n = 1$.

### Exercice 13 — Vrai ou faux ? <span class="etoiles">★★</span>

Pour chaque affirmation, dire si elle est vraie ou fausse, en justifiant (preuve ou contre-exemple).

1. Si $\lim u_n = +\infty$ et $\lim v_n = -\infty$, alors $\lim (u_n + v_n) = 0$.
2. Toute suite croissante tend vers $+\infty$.
3. Une suite qui tend vers $+\infty$ est croissante à partir d'un certain rang.
4. Si $u_n \leq v_n$ pour tout $n$ et si $(v_n)$ converge, alors $(u_n)$ converge.
5. Toute suite bornée converge.
6. Si $(u_n)$ converge vers $\ell > 0$, alors $u_n > 0$ à partir d'un certain rang.

??? success "Correction"
    **1. Faux.** C'est une forme indéterminée. Contre-exemple : $u_n = 2n$ et $v_n = -n$ donnent $u_n + v_n = n \to +\infty$.

    **2. Faux.** $u_n = 1 - \dfrac{1}{n+1}$ est croissante mais converge vers $1$.

    **3. Faux.** $u_n = n + 2(-1)^n$ tend vers $+\infty$ car $u_n \geq n - 2$. Pourtant, pour $n$ pair, $u_{n+1} - u_n = 1 - 4 = -3 < 0$ : la suite décroît à chaque rang pair, aussi loin qu'on aille.

    **4. Faux.** $u_n = -n$ et $v_n = 0$ : on a bien $u_n \leq v_n$, $(v_n)$ converge, mais $(u_n)$ tend vers $-\infty$.

    **5. Faux.** $u_n = (-1)^n$ est bornée entre $-1$ et $1$ mais n'a pas de limite.

    **6. Vrai.** L'intervalle $\left]\frac{\ell}{2} \,;\, \frac{3\ell}{2}\right[$ est un intervalle ouvert contenant $\ell$. Par définition de la limite, il contient tous les $u_n$ à partir d'un certain rang. Pour ces rangs, $u_n > \frac{\ell}{2} > 0$.

---

## Thème 3 — Théorèmes de comparaison

*Méthode associée : [Méthode 3](methodes.md#methode-3-utiliser-un-theoreme-de-comparaison).*

### Exercice 14 — Comparaison directe <span class="etoiles">★</span>

Déterminer la limite de chaque suite.

1. $u_n = n^2 + (-1)^n n$
2. $v_n = 3 - n + \sin(n^2)$

??? success "Correction"
    **1.** $(-1)^n n \geq -n$, donc $u_n \geq n^2 - n = n(n - 1)$. Comme $\lim n(n-1) = +\infty$, par comparaison $\lim u_n = +\infty$.

    **2.** $\sin(n^2) \leq 1$, donc $v_n \leq 4 - n$. Comme $\lim (4 - n) = -\infty$, par comparaison $\lim v_n = -\infty$.

### Exercice 15 — Comparaison et gendarmes <span class="etoiles">★★</span>

Déterminer la limite de chaque suite.

1. $u_n = n + \sin n$
2. $v_n = \dfrac{\cos n}{n + 1}$
3. $w_n = \dfrac{n + (-1)^n}{n + 2}$

??? success "Correction"
    **1.** Pour tout $n$, $\sin n \geq -1$ donc $u_n \geq n - 1$. Comme $\lim (n - 1) = +\infty$, le théorème de comparaison donne $\lim u_n = +\infty$.

    **2.** Pour tout $n$, $-1 \leq \cos n \leq 1$ et $n + 1 > 0$, donc

    $$-\frac{1}{n+1} \leq v_n \leq \frac{1}{n+1}.$$

    Les deux bornes tendent vers $0$. D'après le théorème des gendarmes, $\lim v_n = 0$.

    **3.** Pour tout $n$, $-1 \leq (-1)^n \leq 1$ et $n + 2 > 0$, donc

    $$\frac{n - 1}{n + 2} \leq w_n \leq \frac{n + 1}{n + 2}.$$

    En factorisant par $n$, $\dfrac{n-1}{n+2} = \dfrac{1 - \frac{1}{n}}{1 + \frac{2}{n}} \to 1$ et de même $\dfrac{n+1}{n+2} \to 1$. D'après le théorème des gendarmes, $\lim w_n = 1$.

### Exercice 16 — Encadrer avant de passer à la limite <span class="etoiles">★★</span>

On pose $u_n = \dfrac{2n + \sin n}{n + 1}$.

1. Montrer que pour tout $n \in \mathbb{N}$ : $\dfrac{2n - 1}{n + 1} \leq u_n \leq \dfrac{2n + 1}{n + 1}$.
2. En déduire la limite de $(u_n)$.

??? success "Correction"
    **1.** $-1 \leq \sin n \leq 1$, donc $2n - 1 \leq 2n + \sin n \leq 2n + 1$. On divise par $n + 1 > 0$ (l'ordre est conservé) et on obtient l'encadrement.

    **2.** $\dfrac{2n - 1}{n + 1} = \dfrac{2 - \frac{1}{n}}{1 + \frac{1}{n}} \to 2$ et de même $\dfrac{2n + 1}{n + 1} \to 2$. D'après le théorème des gendarmes, $\lim u_n = 2$.

### Exercice 17 — Une somme qui diverge <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $S_n = \displaystyle\sum_{k=1}^{n} \frac{1}{\sqrt{k}} = \frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n}}$.

1. Montrer que, pour tout entier $k$ tel que $1 \leq k \leq n$, $\dfrac{1}{\sqrt{k}} \geq \dfrac{1}{\sqrt{n}}$.
2. En déduire que $S_n \geq \sqrt{n}$, puis la limite de $(S_n)$.

??? success "Correction"
    **1.** Si $1 \leq k \leq n$, alors $0 < \sqrt{k} \leq \sqrt{n}$ (la racine carrée est croissante). La fonction inverse est décroissante sur $]0 \,;\, +\infty[$, donc $\dfrac{1}{\sqrt{k}} \geq \dfrac{1}{\sqrt{n}}$.

    **2.** $S_n$ est une somme de $n$ termes, chacun supérieur ou égal à $\dfrac{1}{\sqrt{n}}$ :

    $$S_n \geq n \times \frac{1}{\sqrt{n}} = \frac{n}{\sqrt{n}} = \sqrt{n}.$$

    Comme $\lim \sqrt{n} = +\infty$, le théorème de comparaison donne $\lim S_n = +\infty$.

### Exercice 18 — Une somme qui converge <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $u_n = \displaystyle\sum_{k=1}^{n} \frac{1}{n + k} = \frac{1}{n+1} + \frac{1}{n+2} + \dots + \frac{1}{2n}$.

1. Montrer que pour tout $n \geq 1$ : $\dfrac{1}{2} \leq u_n \leq \dfrac{n}{n+1}$.
2. Montrer que $u_{n+1} - u_n = \dfrac{1}{2n+1} - \dfrac{1}{2n+2}$, puis que $(u_n)$ est croissante.
3. En déduire que $(u_n)$ converge vers une limite $\ell$ telle que $\dfrac{1}{2} \leq \ell \leq 1$.

??? success "Correction"
    **1.** $u_n$ est une somme de $n$ termes. Pour $1 \leq k \leq n$, on a $n + 1 \leq n + k \leq 2n$, donc $\dfrac{1}{2n} \leq \dfrac{1}{n+k} \leq \dfrac{1}{n+1}$. En additionnant ces $n$ inégalités :

    $$n \times \frac{1}{2n} \leq u_n \leq n \times \frac{1}{n+1}, \quad \text{soit} \quad \frac{1}{2} \leq u_n \leq \frac{n}{n+1}.$$

    **2.** $u_{n+1} = \dfrac{1}{n+2} + \dots + \dfrac{1}{2n} + \dfrac{1}{2n+1} + \dfrac{1}{2n+2}$. Par rapport à $u_n$, on perd le terme $\dfrac{1}{n+1}$ et on gagne $\dfrac{1}{2n+1}$ et $\dfrac{1}{2n+2}$. Donc :

    $$u_{n+1} - u_n = \frac{1}{2n+1} + \frac{1}{2n+2} - \frac{1}{n+1} = \frac{1}{2n+1} + \frac{1}{2n+2} - \frac{2}{2n+2} = \frac{1}{2n+1} - \frac{1}{2n+2}.$$

    Comme $2n + 1 < 2n + 2$, on a $\dfrac{1}{2n+1} > \dfrac{1}{2n+2}$, donc $u_{n+1} - u_n > 0$ : $(u_n)$ est croissante.

    **3.** $(u_n)$ est croissante et majorée par $1$ (car $\frac{n}{n+1} < 1$) : elle converge vers un réel $\ell$. Par passage à la limite dans l'encadrement de la question 1 : $\dfrac{1}{2} \leq \ell \leq 1$.

    !!! note "Pour aller plus loin"
        On montre après le chapitre sur le logarithme que $\ell = \ln 2 \approx 0{,}693$.

---

## Thème 4 — Suites géométriques et arithmético-géométriques

*Méthode associée : [Méthode 5](methodes.md#methode-5-etudier-une-suite-arithmetico-geometrique).*

### Exercice 19 — Limites de suites géométriques <span class="etoiles">★</span>

Déterminer la limite de chaque suite.

1. $a_n = 3 \times \left(\dfrac{1}{2}\right)^n$
2. $b_n = -2 \times 1{,}05^n$
3. $c_n = 4^n - 3^n$
4. $S_n = 1 + \dfrac{1}{3} + \dfrac{1}{3^2} + \dots + \dfrac{1}{3^n}$

??? success "Correction"
    **1.** $-1 < \dfrac{1}{2} < 1$ donc $\lim \left(\dfrac{1}{2}\right)^n = 0$ et $\lim a_n = 0$.

    **2.** $1{,}05 > 1$ donc $\lim 1{,}05^n = +\infty$. Par produit avec $-2 < 0$, $\lim b_n = -\infty$.

    **3.** Forme $\infty - \infty$. On factorise par $4^n$ : $c_n = 4^n\left(1 - \left(\dfrac{3}{4}\right)^n\right)$. Comme $0 < \dfrac{3}{4} < 1$, la parenthèse tend vers $1$ ; et $4^n \to +\infty$. Donc $\lim c_n = +\infty$.

    **4.** C'est la somme des $n+1$ premiers termes d'une suite géométrique de raison $q = \dfrac{1}{3}$ :

    $$S_n = \frac{1 - \left(\frac{1}{3}\right)^{n+1}}{1 - \frac{1}{3}} = \frac{3}{2}\left(1 - \left(\frac{1}{3}\right)^{n+1}\right).$$

    Comme $\lim \left(\frac{1}{3}\right)^{n+1} = 0$, on obtient $\lim S_n = \dfrac{3}{2}$.

### Exercice 20 — Reconnaître la valeur de $q$ <span class="etoiles">★</span>

Déterminer, si elle existe, la limite de chaque suite.

1. $(-0{,}9)^n$
2. $(-2)^n$
3. $\left(\dfrac{2}{3}\right)^n + 1$
4. $\dfrac{5^n}{2^{2n}}$

??? success "Correction"
    **1.** $-1 < -0{,}9 < 1$ : la limite est $0$.

    **2.** $-2 \leq -1$ : la suite n'a pas de limite. Ses termes changent de signe et leur valeur absolue $2^n$ tend vers $+\infty$.

    **3.** $\left(\frac{2}{3}\right)^n \to 0$, donc la limite est $1$.

    **4.** $2^{2n} = (2^2)^n = 4^n$, donc $\dfrac{5^n}{4^n} = \left(\dfrac{5}{4}\right)^n$. Comme $\frac{5}{4} > 1$, la limite est $+\infty$.

### Exercice 21 — Limite d'une somme géométrique <span class="etoiles">★★</span>

Pour $n \in \mathbb{N}$, on pose $S_n = 3 + 3 \times 0{,}9 + 3 \times 0{,}9^2 + \dots + 3 \times 0{,}9^n$.

1. Exprimer $S_n$ en fonction de $n$.
2. Déterminer la limite de $(S_n)$.

??? success "Correction"
    **1.** On factorise par $3$ et on applique la formule de la somme géométrique de raison $0{,}9 \neq 1$ :

    $$S_n = 3 \times \frac{1 - 0{,}9^{n+1}}{1 - 0{,}9} = 30\left(1 - 0{,}9^{n+1}\right).$$

    **2.** $-1 < 0{,}9 < 1$ donc $\lim 0{,}9^{n+1} = 0$ et $\lim S_n = 30$.

### Exercice 22 — Suite arithmético-géométrique <span class="etoiles">★★</span>

On définit $(u_n)$ par $u_0 = 10$ et $u_{n+1} = 0{,}5\,u_n + 3$. On pose $v_n = u_n - 6$.

1. Montrer que $(v_n)$ est géométrique ; préciser sa raison et son premier terme.
2. En déduire l'expression de $u_n$ en fonction de $n$.
3. Étudier le sens de variation de $(u_n)$ et déterminer sa limite.

??? success "Correction"
    **1.** Pour tout $n$ :

    $$v_{n+1} = u_{n+1} - 6 = 0{,}5\,u_n + 3 - 6 = 0{,}5\,u_n - 3 = 0{,}5\,(u_n - 6) = 0{,}5\,v_n.$$

    $(v_n)$ est géométrique de raison $0{,}5$ et de premier terme $v_0 = 10 - 6 = 4$.

    **2.** $v_n = 4 \times 0{,}5^n$, donc $u_n = v_n + 6 = 4 \times 0{,}5^n + 6$.

    **3.** $u_{n+1} - u_n = 4 \times 0{,}5^{n+1} - 4 \times 0{,}5^n = 4 \times 0{,}5^n (0{,}5 - 1) = -2 \times 0{,}5^n < 0$.

    La suite $(u_n)$ est donc strictement décroissante. Comme $-1 < 0{,}5 < 1$, $\lim 0{,}5^n = 0$ et donc $\lim u_n = 6$.

### Exercice 23 — Modéliser un nombre d'abonnés <span class="etoiles">★★</span>

Une salle de sport compte 1 200 abonnés en 2026. Chaque année, 75 % des abonnés renouvellent leur abonnement et 400 nouveaux abonnés s'inscrivent. On note $u_n$ le nombre d'abonnés l'année $2026 + n$, donc $u_0 = 1200$.

1. Justifier que $u_{n+1} = 0{,}75\,u_n + 400$.
2. On pose $v_n = u_n - 1600$. Montrer que $(v_n)$ est géométrique.
3. En déduire $u_n$ en fonction de $n$, puis la limite de $(u_n)$. Interpréter.
4. À partir de quelle année la salle dépassera-t-elle 1 550 abonnés ?

??? success "Correction"
    **1.** Les abonnés de l'année $n+1$ sont 75 % des abonnés de l'année $n$, plus 400 nouveaux : $u_{n+1} = 0{,}75\,u_n + 400$.

    **2.** $v_{n+1} = u_{n+1} - 1600 = 0{,}75\,u_n + 400 - 1600 = 0{,}75\,u_n - 1200 = 0{,}75\,(u_n - 1600) = 0{,}75\,v_n$.

    $(v_n)$ est géométrique de raison $0{,}75$, avec $v_0 = 1200 - 1600 = -400$.

    **3.** $v_n = -400 \times 0{,}75^n$, donc $u_n = 1600 - 400 \times 0{,}75^n$.

    Comme $-1 < 0{,}75 < 1$, $\lim 0{,}75^n = 0$ et $\lim u_n = 1600$. À long terme, le nombre d'abonnés se stabilise autour de 1 600.

    **4.** $u_n > 1550 \iff 400 \times 0{,}75^n < 50 \iff 0{,}75^n < 0{,}125$.

    À la calculatrice : $0{,}75^7 \approx 0{,}133 > 0{,}125$ et $0{,}75^8 \approx 0{,}100 < 0{,}125$. Comme $(0{,}75^n)$ est décroissante, la condition est vérifiée à partir de $n = 8$, soit en **2034**.

---

## Thème 5 — Convergence monotone et suites récurrentes

*Méthodes associées : [Méthode 1](methodes.md#methode-1-rediger-une-demonstration-par-recurrence) et [Méthode 4](methodes.md#methode-4-montrer-quune-suite-converge-sans-calculer-sa-limite).*

### Exercice 24 — Suite récurrente et convergence monotone <span class="etoiles">★★</span>

On définit $(u_n)$ par $u_0 = 0$ et $u_{n+1} = \sqrt{u_n + 2}$.

1. Démontrer par récurrence que, pour tout $n \in \mathbb{N}$ : $0 \leq u_n \leq u_{n+1} \leq 2$.
2. En déduire que $(u_n)$ converge.

??? success "Correction"
    **1.** Soit $\mathcal{P}(n)$ : « $0 \leq u_n \leq u_{n+1} \leq 2$ ».

    - Initialisation : $u_0 = 0$ et $u_1 = \sqrt{2} \approx 1{,}41$. On a bien $0 \leq 0 \leq \sqrt{2} \leq 2$.
    - Hérédité : supposons $0 \leq u_n \leq u_{n+1} \leq 2$. En ajoutant $2$ :

    $$2 \leq u_n + 2 \leq u_{n+1} + 2 \leq 4.$$

    La fonction racine carrée est croissante sur $[0 \,;\, +\infty[$, donc elle conserve l'ordre :

    $$\sqrt{2} \leq u_{n+1} \leq u_{n+2} \leq 2.$$

    Comme $\sqrt{2} \geq 0$, on obtient $0 \leq u_{n+1} \leq u_{n+2} \leq 2$ : $\mathcal{P}(n+1)$ est vraie.

    - Conclusion : $\mathcal{P}(n)$ est vraie pour tout $n \in \mathbb{N}$.

    **2.** D'après la question 1, $(u_n)$ est croissante ($u_n \leq u_{n+1}$) et majorée par $2$. D'après le théorème de convergence monotone, elle converge.

    !!! note "Pour aller plus loin"
        Avec le chapitre Continuité, on montrera que la limite $\ell$ vérifie $\ell = \sqrt{\ell + 2}$. On en déduit $\ell^2 - \ell - 2 = 0$, c'est-à-dire $(\ell - 2)(\ell + 1) = 0$, et comme $\ell \geq 0$ : $\ell = 2$.

### Exercice 25 — Suite homographique <span class="etoiles">★★</span>

On définit $(u_n)$ par $u_0 = 5$ et $u_{n+1} = \dfrac{u_n}{1 + u_n}$.

1. Montrer par récurrence que $u_n > 0$ pour tout $n$.
2. Montrer que $(u_n)$ est décroissante. En déduire qu'elle converge.
3. On pose $w_n = \dfrac{1}{u_n}$. Montrer que $(w_n)$ est arithmétique.
4. En déduire $u_n$ en fonction de $n$ et la limite de $(u_n)$.

??? success "Correction"
    **1.** $u_0 = 5 > 0$. Si $u_n > 0$, alors $1 + u_n > 0$ et $u_{n+1} = \dfrac{u_n}{1 + u_n} > 0$ comme quotient de deux nombres positifs. Par récurrence, $u_n > 0$ pour tout $n$.

    **2.** $u_{n+1} - u_n = \dfrac{u_n - u_n(1 + u_n)}{1 + u_n} = \dfrac{-u_n^2}{1 + u_n} < 0$, car $u_n > 0$. La suite est décroissante. Elle est minorée par $0$ : elle converge.

    **3.** $w_{n+1} = \dfrac{1}{u_{n+1}} = \dfrac{1 + u_n}{u_n} = \dfrac{1}{u_n} + 1 = w_n + 1$.

    $(w_n)$ est arithmétique de raison $1$ et de premier terme $w_0 = \dfrac{1}{5}$.

    **4.** $w_n = \dfrac{1}{5} + n = \dfrac{5n + 1}{5}$, donc $u_n = \dfrac{1}{w_n} = \dfrac{5}{5n + 1}$. Le dénominateur tend vers $+\infty$, donc $\lim u_n = 0$.

### Exercice 26 — La méthode de Héron pour approcher $\sqrt{2}$ <span class="etoiles">★★★</span>

On définit $(u_n)$ par $u_0 = 2$ et $u_{n+1} = \dfrac{1}{2}\left(u_n + \dfrac{2}{u_n}\right)$.

1. Calculer $u_1$, $u_2$ et une valeur approchée de $u_3$.
2. Montrer que pour tout $n$, $u_n > 0$.
3. Montrer que pour tout $n$ : $u_{n+1} - \sqrt{2} = \dfrac{(u_n - \sqrt{2})^2}{2u_n}$. En déduire que $u_n \geq \sqrt{2}$ pour tout $n$.
4. Montrer que $(u_n)$ est décroissante, puis qu'elle converge.

??? success "Correction"
    **1.** $u_1 = \dfrac{1}{2}(2 + 1) = 1{,}5$, $u_2 = \dfrac{1}{2}\left(1{,}5 + \dfrac{2}{1{,}5}\right) = \dfrac{17}{12} \approx 1{,}41667$, puis $u_3 \approx 1{,}414216$. On reconnaît $\sqrt{2} \approx 1{,}414214$.

    **2.** $u_0 = 2 > 0$, et si $u_n > 0$, alors $u_n + \dfrac{2}{u_n} > 0$ donc $u_{n+1} > 0$. Par récurrence, $u_n > 0$ pour tout $n$.

    **3.** On met au même dénominateur :

    $$u_{n+1} - \sqrt{2} = \frac{u_n^2 + 2}{2u_n} - \sqrt{2} = \frac{u_n^2 - 2\sqrt{2}\,u_n + 2}{2u_n} = \frac{(u_n - \sqrt{2})^2}{2u_n}.$$

    Le numérateur est un carré, donc positif, et $2u_n > 0$. Donc $u_{n+1} - \sqrt{2} \geq 0$ pour tout $n$ : $u_n \geq \sqrt{2}$ pour tout $n \geq 1$. C'est aussi vrai pour $n = 0$, car $u_0 = 2 \geq \sqrt{2}$.

    **4.** $u_{n+1} - u_n = \dfrac{1}{2}\left(\dfrac{2}{u_n} - u_n\right) = \dfrac{2 - u_n^2}{2u_n}$. Comme $u_n \geq \sqrt{2}$, on a $u_n^2 \geq 2$, donc $u_{n+1} - u_n \leq 0$ : la suite est décroissante. Elle est minorée par $\sqrt{2}$ : elle converge.

    !!! note "Pour aller plus loin"
        La limite $\ell$ vérifie $\ell = \frac{1}{2}\left(\ell + \frac{2}{\ell}\right)$ (chapitre Continuité), d'où $\ell^2 = 2$ et $\ell = \sqrt{2}$. La convergence est très rapide : le nombre de décimales exactes double environ à chaque étape.

### Exercice 27 — Une somme majorée <span class="etoiles">★★★</span>

Pour $n \geq 1$, on pose $u_n = \displaystyle\sum_{k=1}^{n} \frac{1}{k^2} = 1 + \frac{1}{4} + \frac{1}{9} + \dots + \frac{1}{n^2}$.

1. Montrer que $(u_n)$ est croissante.
2. Montrer que pour tout $k \geq 2$ : $\dfrac{1}{k^2} \leq \dfrac{1}{k-1} - \dfrac{1}{k}$.
3. En déduire que $u_n \leq 2 - \dfrac{1}{n}$ pour tout $n \geq 1$, puis que $(u_n)$ converge.

??? success "Correction"
    **1.** $u_{n+1} - u_n = \dfrac{1}{(n+1)^2} > 0$ : la suite est croissante.

    **2.** $\dfrac{1}{k-1} - \dfrac{1}{k} = \dfrac{k - (k-1)}{k(k-1)} = \dfrac{1}{k(k-1)}$. Comme $0 < k(k-1) < k^2$, on a $\dfrac{1}{k^2} \leq \dfrac{1}{k(k-1)}$.

    **3.** Pour $n = 1$ : $u_1 = 1 = 2 - 1$. Pour $n \geq 2$, on somme les inégalités de la question 2 pour $k$ allant de $2$ à $n$. La somme de droite est télescopique :

    $$\sum_{k=2}^{n} \frac{1}{k^2} \leq \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n-1} - \frac{1}{n}\right) = 1 - \frac{1}{n}.$$

    En ajoutant le premier terme $1$ : $u_n \leq 2 - \dfrac{1}{n} < 2$.

    $(u_n)$ est croissante et majorée par $2$ : elle converge.

    !!! note "Pour aller plus loin"
        Le mathématicien Euler a montré en 1735 que cette limite vaut $\dfrac{\pi^2}{6} \approx 1{,}645$.

---

## Thème 6 — Algorithmique

*Méthode associée : [Méthode 6](methodes.md#methode-6-ecrire-un-algorithme-de-seuil-en-python).*

### Exercice 28 — Algorithme de seuil <span class="etoiles">★★</span>

On reprend la suite de l'exercice 22 : $u_0 = 10$, $u_{n+1} = 0{,}5\,u_n + 3$.

1. Justifier qu'il existe un rang à partir duquel $u_n < 6{,}01$.
2. Écrire une fonction Python `seuil()` qui renvoie le plus petit entier $n$ tel que $u_n < 6{,}01$.
3. Quelle valeur renvoie-t-elle ?

??? success "Correction"
    **1.** $(u_n)$ converge vers $6$. L'intervalle $]5{,}99 \,;\, 6{,}01[$ est un intervalle ouvert qui contient $6$ : par définition de la limite, il contient tous les $u_n$ à partir d'un certain rang. En particulier, $u_n < 6{,}01$ à partir de ce rang.

    **2.**

    ```python
    def seuil():
        n = 0
        u = 10
        while u >= 6.01:
            u = 0.5 * u + 3
            n = n + 1
        return n
    ```

    **3.** On cherche le plus petit $n$ tel que $4 \times 0{,}5^n < 0{,}01$, c'est-à-dire $0{,}5^n < 0{,}0025$.

    - $0{,}5^8 = 0{,}00390625 > 0{,}0025$, donc $u_8 \approx 6{,}0156$ ;
    - $0{,}5^9 = 0{,}001953125 < 0{,}0025$, donc $u_9 \approx 6{,}0078$.

    La suite étant décroissante, la fonction renvoie **9**.

### Exercice 29 — Dépasser 1000 <span class="etoiles">★</span>

On reprend la suite de l'exercice 2 : $u_0 = 1$ et $u_{n+1} = u_n + 2n + 3$.

1. Compléter la fonction suivante pour qu'elle renvoie le plus petit $n$ tel que $u_n > 1000$.

    ```python
    def seuil():
        n = 0
        u = 1
        while ......:
            u = ......
            n = n + 1
        return n
    ```

2. Sans exécuter le programme, déterminer la valeur renvoyée à l'aide de l'exercice 2.

??? success "Correction"
    **1.** On continue tant que la condition n'est **pas** atteinte. Attention à l'ordre des instructions : la relation utilise l'ancienne valeur de $n$, donc on met à jour `u` **avant** `n`.

    ```python
    def seuil():
        n = 0
        u = 1
        while u <= 1000:
            u = u + 2 * n + 3
            n = n + 1
        return n
    ```

    **2.** D'après l'exercice 2, $u_n = (n+1)^2$. On cherche le plus petit $n$ tel que $(n+1)^2 > 1000$. Or $31^2 = 961$ et $32^2 = 1024$, donc $n + 1 = 32$ : la fonction renvoie **31**.
