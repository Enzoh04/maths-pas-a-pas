# Sujets type bac — Sommes de variables aléatoires

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets dans l'esprit de l'épreuve. Au bac, les sommes de variables aléatoires apparaissent souvent en fin d'exercice de probabilités, combinées avec la loi binomiale et la concentration (chapitre 15).

| Sujet | Thème | Durée conseillée |
|---|---|---|
| 1 | Deux jeux successifs | 45 min |
| 2 | Pièces défectueuses de deux machines | 40 min |
| 3 | QCM | 20 min |
| 4 | Sondage et mesures répétées | 35 min |

## Sujet 1 — Deux jeux successifs

Dans une fête foraine, un joueur fait tourner une roue, puis lance une fléchette ; les deux jeux sont indépendants.

- **La roue.** Le gain $X$ (en euros) vaut $-2$ avec probabilité $0{,}5$, $0$ avec probabilité $0{,}3$ et $5$ avec probabilité $0{,}2$.
- **La fléchette.** Le gain $Y$ vaut $2$ si la cible est atteinte, ce qui arrive avec probabilité $0{,}4$, et $-1$ sinon.

On note $S = X + Y$ le gain total.

1. Calculer $E(X)$, $V(X)$, $E(Y)$ et $V(Y)$.
2. En déduire $E(S)$ et $V(S)$, en justifiant.
3. Déterminer la loi de $S$, puis vérifier la valeur de $E(S)$.
4. Calculer la probabilité que le joueur gagne de l'argent.
5. Le forain accueille $100$ joueurs par jour, dont les gains sont indépendants. On note $T$ la somme de leurs gains. Calculer $E(T)$ et $\sigma(T)$, puis interpréter $E(T)$ du point de vue du forain.
6. Le forain veut modifier la somme gagnée quand la fléchette atteint la cible, pour que l'espérance du gain total d'un joueur soit $-0{,}10$ €. Quelle somme doit-il proposer ?

??? success "Correction"
    **1.** $E(X) = -1 + 0 + 1 = 0$. $E(X^2) = 2 + 0 + 5 = 7$, donc $V(X) = 7$. $E(Y) = 0{,}8 - 0{,}6 = 0{,}2$. $E(Y^2) = 1{,}6 + 0{,}6 = 2{,}2$, donc $V(Y) = 2{,}2 - 0{,}04 = 2{,}16$.

    **2.** Par linéarité, $E(S) = 0{,}2$. Les jeux étant indépendants, $V(S) = 7 + 2{,}16 = 9{,}16$.

    **3.** Par indépendance, chaque couple a pour probabilité le produit des probabilités :

    | $s$ | $-3$ | $-1$ | $0$ | $2$ | $4$ | $7$ |
    |---|---|---|---|---|---|---|
    | couple $(x, y)$ | $(-2, -1)$ | $(0, -1)$ | $(-2, 2)$ | $(0, 2)$ | $(5, -1)$ | $(5, 2)$ |
    | $P(S = s)$ | $0{,}30$ | $0{,}18$ | $0{,}20$ | $0{,}12$ | $0{,}12$ | $0{,}08$ |

    $E(S) = -0{,}9 - 0{,}18 + 0 + 0{,}24 + 0{,}48 + 0{,}56 = 0{,}2$.

    **4.** $P(S > 0) = 0{,}12 + 0{,}12 + 0{,}08 = 0{,}32$.

    **5.** $E(T) = 100 \times 0{,}2 = 20$ et $\sigma(T) = \sqrt{100 \times 9{,}16} = \sqrt{916} \approx 30{,}3$. En moyenne, le forain **perd** $20$ € par jour : le jeu est défavorable pour lui.

    **6.** Avec un gain $g$ : $E(Y) = 0{,}4g - 0{,}6$, et $E(S) = 0{,}4g - 0{,}6 = -0{,}1 \iff g = 1{,}25$. Il doit proposer $1{,}25$ €.

---

## Sujet 2 — Deux machines

Une entreprise utilise deux machines indépendantes. Chaque jour, la machine A produit $200$ pièces, chacune défectueuse avec probabilité $0{,}02$ ; la machine B produit $300$ pièces, chacune défectueuse avec probabilité $0{,}01$. Les défauts des pièces sont indépendants. On note $X$ et $Y$ les nombres de pièces défectueuses produites par A et par B en une journée, et $D = X + Y$.

1. Donner la loi de $X$ et celle de $Y$.
2. Calculer $E(D)$, $V(D)$ et $\sigma(D)$.
3. Calculer la probabilité qu'aucune pièce ne soit défectueuse dans la journée.
4. On veut savoir si $D$ suit une loi binomiale de paramètres $n = 500$ et $p$.
   a. Quelle valeur de $p$ donnerait la même espérance ?
   b. Calculer alors la variance de cette loi binomiale. Conclure.
5. Chaque pièce défectueuse coûte $15$ € à l'entreprise, qui paie en plus $50$ € de contrôle par jour. On note $C$ le coût journalier. Exprimer $C$ en fonction de $D$, puis calculer $E(C)$ et $\sigma(C)$.

??? success "Correction"
    **1.** Pour chaque machine, on répète de façon identique et indépendante une épreuve à deux issues : $X \sim \mathcal{B}(200\,;\,0{,}02)$ et $Y \sim \mathcal{B}(300\,;\,0{,}01)$.

    **2.** $E(D) = 4 + 3 = 7$. Les machines sont indépendantes, donc $V(D) = 200 \times 0{,}02 \times 0{,}98 + 300 \times 0{,}01 \times 0{,}99 = 3{,}92 + 2{,}97 = 6{,}89$, et $\sigma(D) \approx 2{,}62$.

    **3.** $P(D = 0) = P(X = 0) \times P(Y = 0) = 0{,}98^{200} \times 0{,}99^{300} \approx 0{,}0176 \times 0{,}0490 \approx 0{,}000\,86$.

    **4. a.** $500p = 7$ donne $p = 0{,}014$.

    **b.** $500 \times 0{,}014 \times 0{,}986 = 6{,}902 \neq 6{,}89$. Une loi binomiale de paramètre $n = 500$ ayant la même espérance que $D$ n'a pas la même variance : $D$ ne suit pas une loi binomiale de paramètre $n = 500$. C'est logique : les $500$ pièces n'ont pas toutes la même probabilité d'être défectueuses.

    **5.** $C = 15D + 50$. $E(C) = 15 \times 7 + 50 = 155$ €. $V(C) = 225 \times 6{,}89 = 1\,550{,}25$, donc $\sigma(C) = 15\,\sigma(D) \approx 39{,}4$ €.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Justifier.

**Question 1.** Si $E(X) = 2$ et $E(Y) = -1$, alors $E(3X - 2Y + 1)$ vaut :

a. $5$ ; b. $7$ ; c. $9$ ; d. on ne peut pas savoir sans l'indépendance.

**Question 2.** $X$ et $Y$ sont indépendantes, $V(X) = 2$ et $V(Y) = 3$. Alors $V(X - 2Y)$ vaut :

a. $-4$ ; b. $8$ ; c. $14$ ; d. $-1$.

**Question 3.** $X$ et $Y$ sont indépendantes, $\sigma(X) = 3$ et $\sigma(Y) = 4$. Alors $\sigma(X + Y)$ vaut :

a. $7$ ; b. $5$ ; c. $25$ ; d. $1$.

**Question 4.** On considère un échantillon de taille $100$ d'une loi d'écart type $5$. L'écart type de la moyenne $M_{100}$ vaut :

a. $0{,}05$ ; b. $0{,}5$ ; c. $5$ ; d. $50$.

**Question 5.** Une variable de loi $\mathcal{B}(n, p)$ peut s'écrire comme la somme de :

a. $n$ variables de Bernoulli de paramètre $p$, indépendantes ;
b. $p$ variables de Bernoulli de paramètre $n$ ;
c. $n$ variables de Bernoulli de paramètre $\frac{p}{n}$ ;
d. deux variables de loi $\mathcal{B}\left(\frac{n}{2}, \frac{p}{2}\right)$.

??? success "Correction"
    **Question 1 : c.** $6 + 2 + 1 = 9$, par linéarité, sans hypothèse d'indépendance.

    **Question 2 : c.** $V(X) + (-2)^2V(Y) = 2 + 12 = 14$.

    **Question 3 : b.** $V(X + Y) = 9 + 16 = 25$, donc $\sigma(X + Y) = 5$.

    **Question 4 : b.** $\frac{5}{\sqrt{100}} = 0{,}5$.

    **Question 5 : a.** C'est le résultat du § 4 du cours.

---

## Sujet 4 — Sondage et mesures répétées

**Partie A — Un sondage**

Dans une grande population, une proportion inconnue $p$ de personnes est favorable à un projet. On interroge $n$ personnes au hasard, ce que l'on assimile à des tirages avec remise. On note $X_i$ la variable qui vaut $1$ si la $i$-ème personne est favorable, $0$ sinon, et $F_n = \dfrac{X_1 + \cdots + X_n}{n}$ la fréquence des personnes favorables dans l'échantillon.

1. Calculer $E(F_n)$ et $V(F_n)$ en fonction de $n$ et $p$.
2. Montrer que $\sigma(F_n) \leq \dfrac{1}{2\sqrt{n}}$.
3. Quelle taille d'échantillon garantit $\sigma(F_n) \leq 0{,}01$, quel que soit $p$ ?
4. Pour $n = 1\,000$ et $p = 0{,}52$, calculer $\sigma(F_n)$. Comparer à la majoration de la question 2.

**Partie B — Mesures répétées**

Un instrument mesure une longueur $\ell$ avec une erreur aléatoire : chaque mesure est une variable aléatoire d'espérance $\ell$ et d'écart type $0{,}5$ mm, les mesures étant indépendantes. On fait $n$ mesures et l'on retient leur moyenne $M_n$.

1. Calculer $E(M_n)$ et $\sigma(M_n)$.
2. Combien de mesures faut-il faire pour que $\sigma(M_n) \leq 0{,}1$ mm ?

??? success "Correction"
    **Partie A**

    **1.** Les $X_i$ forment un échantillon de la loi de Bernoulli de paramètre $p$ : $E(F_n) = p$ et $V(F_n) = \dfrac{p(1 - p)}{n}$.

    **2.** $p(1 - p) = \frac{1}{4} - \left(p - \frac{1}{2}\right)^2 \leq \frac{1}{4}$, donc $V(F_n) \leq \dfrac{1}{4n}$ et $\sigma(F_n) \leq \dfrac{1}{2\sqrt{n}}$.

    **3.** Il suffit que $\dfrac{1}{2\sqrt{n}} \leq 0{,}01$, soit $\sqrt{n} \geq 50$, c'est-à-dire $n \geq 2\,500$.

    **4.** $\sigma(F_n) = \sqrt{\dfrac{0{,}52 \times 0{,}48}{1\,000}} \approx 0{,}0158$, et la majoration donne $\dfrac{1}{2\sqrt{1\,000}} \approx 0{,}0158$ également : quand $p$ est proche de $\frac{1}{2}$, la majoration est presque une égalité.

    **Partie B**

    **1.** $E(M_n) = \ell$ (la moyenne ne fausse pas la mesure) et $\sigma(M_n) = \dfrac{0{,}5}{\sqrt{n}}$.

    **2.** $\dfrac{0{,}5}{\sqrt{n}} \leq 0{,}1 \iff \sqrt{n} \geq 5 \iff n \geq 25$.
