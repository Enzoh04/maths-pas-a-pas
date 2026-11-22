# Sujets type bac — Concentration, loi des grands nombres

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets dans l'esprit de l'épreuve. Au bac, ce chapitre arrive presque toujours en fin d'exercice de probabilités, après une loi binomiale ou une somme de variables aléatoires.

| Sujet | Thème | Durée conseillée |
|---|---|---|
| 1 | Un jeu répété | 40 min |
| 2 | Démonstration guidée et contrôle de qualité | 45 min |
| 3 | QCM | 20 min |
| 4 | Calculer une aire par simulation | 40 min |

## Sujet 1 — Un jeu répété

À un jeu, le gain $X$ d'un joueur (en euros) vaut $-1$ avec probabilité $0{,}5$, $0$ avec probabilité $0{,}3$ et $4$ avec probabilité $0{,}2$.

1. Calculer $E(X)$ et montrer que $V(X) = 3{,}61$.
2. a. À l'aide de l'inégalité de Bienaymé-Tchebychev, majorer $P\big(|X - 0{,}3| \geq 3\big)$.
   b. Calculer la valeur exacte de cette probabilité et comparer.
3. Un joueur joue $n$ parties indépendantes. On note $M_n$ son gain moyen par partie.
   a. Donner $E(M_n)$ et $V(M_n)$.
   b. Déterminer une valeur de $n$ pour laquelle la probabilité que $M_n$ s'écarte de $0{,}3$ d'au moins $0{,}5$ soit inférieure ou égale à $0{,}1$.
4. On prend $n = 145$. On note $S_{145}$ le gain total du joueur.
   a. Justifier que si $S_{145} \leq 0$, alors $|M_{145} - 0{,}3| \geq 0{,}3$.
   b. En déduire une majoration de la probabilité que le joueur ne gagne pas d'argent sur ses $145$ parties.
5. Le jeu est-il favorable à l'organisateur ?

??? success "Correction"
    **1.** $E(X) = -0{,}5 + 0 + 0{,}8 = 0{,}3$. $E(X^2) = 0{,}5 + 0 + 3{,}2 = 3{,}7$, donc $V(X) = 3{,}7 - 0{,}09 = 3{,}61$.

    **2. a.** $P\big(|X - 0{,}3| \geq 3\big) \leq \frac{3{,}61}{9} \approx 0{,}401$.

    **b.** $|X - 0{,}3| \geq 3 \iff X \geq 3{,}3$ ou $X \leq -2{,}7$, ce qui n'arrive que pour $X = 4$ : la probabilité exacte vaut $0{,}2$. Le majorant est correct, mais deux fois trop grand.

    **3. a.** Les parties forment un échantillon : $E(M_n) = 0{,}3$ et $V(M_n) = \frac{3{,}61}{n}$.

    **b.** D'après l'inégalité de concentration, $P\big(|M_n - 0{,}3| \geq 0{,}5\big) \leq \frac{3{,}61}{0{,}25n}$. Il suffit que $\frac{3{,}61}{0{,}25n} \leq 0{,}1$, soit $n \geq 144{,}4$ : $n = 145$ convient.

    **4. a.** Si $S_{145} \leq 0$, alors $M_{145} \leq 0$, donc $0{,}3 - M_{145} \geq 0{,}3$, et a fortiori $|M_{145} - 0{,}3| \geq 0{,}3$.

    **b.** Donc $P(S_{145} \leq 0) \leq P\big(|M_{145} - 0{,}3| \geq 0{,}3\big) \leq \frac{3{,}61}{145 \times 0{,}09} \approx 0{,}277$.

    **5.** Non : l'espérance du gain du joueur est positive ($0{,}3$ € par partie), et d'après la loi des grands nombres, sur un grand nombre de parties, le gain moyen par partie se rapproche de $0{,}3$ €. L'organisateur perd de l'argent à long terme.

---

## Sujet 2 — Démonstration guidée et contrôle de qualité

**Partie A — L'inégalité de concentration**

On admet l'inégalité de Bienaymé-Tchebychev. Soit $(X_1, \ldots, X_n)$ un échantillon d'une variable aléatoire $X$ d'espérance $\mu$ et de variance $V$, et $M_n = \frac{X_1 + \cdots + X_n}{n}$.

1. Montrer que $E(M_n) = \mu$, en précisant la propriété utilisée.
2. Montrer que $V(M_n) = \dfrac{V}{n}$, en précisant les propriétés utilisées.
3. En déduire que pour tout $\delta > 0$, $P\big(|M_n - \mu| \geq \delta\big) \leq \dfrac{V}{n\delta^2}$.

**Partie B — Application**

Une usine produit des composants, dont $4\,\%$ sont défectueux. On prélève un lot de $500$ composants, assimilé à un tirage avec remise, et l'on note $X$ le nombre de composants défectueux.

1. Justifier que $X$ suit une loi binomiale ; donner $E(X)$ et $V(X)$.
2. À l'aide de l'inégalité de Bienaymé-Tchebychev, minorer $P(12 < X < 28)$.
3. À la calculatrice, donner une valeur approchée de $P(13 \leq X \leq 27)$. Commenter.
4. On prélève maintenant $n$ composants et l'on note $F_n$ la fréquence de composants défectueux. Déterminer une valeur de $n$ telle que $P\big(|F_n - 0{,}04| \geq 0{,}01\big) \leq 0{,}05$.

??? success "Correction"
    **Partie A**

    **1.** Par linéarité de l'espérance, $E(M_n) = \frac{1}{n}\big(E(X_1) + \cdots + E(X_n)\big) = \frac{n\mu}{n} = \mu$.

    **2.** Les $X_i$ sont indépendantes, donc $V(X_1 + \cdots + X_n) = V(X_1) + \cdots + V(X_n) = nV$. Puis $V(aY) = a^2V(Y)$ avec $a = \frac{1}{n}$ : $V(M_n) = \frac{nV}{n^2} = \frac{V}{n}$.

    **3.** On applique l'inégalité de Bienaymé-Tchebychev à $M_n$ : $P\big(|M_n - \mu| \geq \delta\big) \leq \frac{V(M_n)}{\delta^2} = \frac{V}{n\delta^2}$.

    **Partie B**

    **1.** On répète $500$ fois, de façon identique et indépendante, une épreuve à deux issues, le succès « le composant est défectueux » ayant pour probabilité $0{,}04$, et $X$ compte les succès : $X \sim \mathcal{B}(500\,;\,0{,}04)$. $E(X) = 20$ et $V(X) = 500 \times 0{,}04 \times 0{,}96 = 19{,}2$.

    **2.** $12 < X < 28 \iff |X - 20| < 8$, donc $P(12 < X < 28) \geq 1 - \frac{19{,}2}{64} = 0{,}7$.

    **3.** $P(13 \leq X \leq 27) = P(X \leq 27) - P(X \leq 12) \approx 0{,}915$. C'est le même événement que $12 < X < 28$ ($X$ est entier) : la minoration $0{,}7$ est vraie, mais très prudente.

    **4.** $F_n$ est la moyenne d'un échantillon de la loi de Bernoulli de paramètre $0{,}04$, de variance $0{,}04 \times 0{,}96 = 0{,}0384$. D'après la Partie A, il suffit que $\frac{0{,}0384}{n \times 0{,}01^2} \leq 0{,}05$, soit $n \geq 7\,680$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Justifier. Dans les questions 1 et 2, $X$ est une variable aléatoire d'espérance $5$ et de variance $1$.

**Question 1.** L'inégalité de Bienaymé-Tchebychev permet d'affirmer que $P\big(|X - 5| \geq 2\big)$ est :

a. égale à $\frac{1}{4}$ ; b. inférieure ou égale à $\frac{1}{4}$ ; c. inférieure ou égale à $\frac{1}{2}$ ; d. supérieure ou égale à $\frac{3}{4}$.

**Question 2.** On peut affirmer que $P(3 < X < 7)$ est :

a. supérieure ou égale à $0{,}75$ ; b. inférieure ou égale à $0{,}25$ ; c. égale à $0{,}75$ ; d. supérieure ou égale à $0{,}95$.

**Question 3.** Pour un échantillon de taille $50$ d'une loi de variance $2$, l'inégalité de concentration donne $P\big(|M_{50} - \mu| \geq 0{,}4\big) \leq$ :

a. $0{,}04$ ; b. $0{,}1$ ; c. $0{,}25$ ; d. $0{,}8$.

**Question 4.** Pour une fréquence $F_n$ de succès dans un schéma de Bernoulli de paramètre $p$ inconnu, la plus petite taille $n$ donnée par l'inégalité de concentration pour garantir $P\big(|F_n - p| \geq 0{,}1\big) \leq 0{,}05$ est :

a. $50$ ; b. $100$ ; c. $500$ ; d. $2\,500$.

**Question 5.** On lance une pièce équilibrée. La loi des grands nombres affirme que :

a. après $5$ Face consécutifs, Pile est plus probable au lancer suivant ;
b. sur $1\,000$ lancers, on obtient exactement $500$ Pile ;
c. la probabilité que la fréquence de Pile s'écarte de $0{,}5$ d'au moins $0{,}01$ tend vers $0$ quand le nombre de lancers tend vers $+\infty$ ;
d. l'écart entre le nombre de Pile et la moitié du nombre de lancers tend vers $0$.

??? success "Correction"
    **Question 1 : b.** $\frac{V}{\delta^2} = \frac{1}{4}$. L'inégalité ne donne qu'une majoration.

    **Question 2 : a.** $3 < X < 7 \iff |X - 5| < 2$, donc $P \geq 1 - \frac{1}{4} = 0{,}75$.

    **Question 3 : c.** $\frac{2}{50 \times 0{,}16} = 0{,}25$.

    **Question 4 : c.** $\frac{1}{4n \times 0{,}01} \leq 0{,}05 \iff n \geq 500$.

    **Question 5 : c.** C'est l'énoncé même de la loi (faible) des grands nombres pour $\delta = 0{,}01$. La réponse a. est le sophisme du joueur ; b. est faux (ce n'est qu'une tendance) ; d. est faux : cet écart a plutôt tendance à grandir, comme $\sqrt{n}$.

---

## Sujet 4 — Calculer une aire par simulation

On note $\mathcal{D}$ le domaine du carré $[0, 1] \times [0, 1]$ situé sous la courbe de la fonction $x \mapsto x^2$.

1. Calculer l'aire de $\mathcal{D}$ à l'aide d'une intégrale (chapitre 8).
2. On choisit un point $M(x, y)$ au hasard dans le carré, $x$ et $y$ étant obtenus par `random()`. On admet que la probabilité que $M$ soit dans $\mathcal{D}$ est égale à l'aire de $\mathcal{D}$. On répète l'expérience $n$ fois de façon indépendante, et l'on note $F_n$ la fréquence des points situés dans $\mathcal{D}$.
   a. Justifier que $E(F_n) = \frac{1}{3}$ et calculer $V(F_n)$.
   b. Déterminer une valeur de $n$ telle que $P\left(\left|F_n - \frac{1}{3}\right| \geq 0{,}01\right) \leq 0{,}05$.
3. Compléter la fonction Python suivante, qui renvoie $F_n$.

    ```python
    from random import random

    def frequence(n):
        compteur = 0
        for i in range(n):
            x = random()
            y = random()
            if ...:
                compteur = compteur + 1
        return ...
    ```

4. Un appel `frequence(50000)` a renvoyé `0.3312`. Ce résultat est-il cohérent avec la question 2 ?
5. Expliquer comment cette méthode permettrait d'estimer l'aire sous la courbe d'une fonction dont on ne connaît pas de primitive, comme $x \mapsto e^{-x^2}$ sur $[0, 1]$.

??? success "Correction"
    **1.** $\int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3}$.

    **2. a.** $F_n$ est la moyenne d'un échantillon de la loi de Bernoulli de paramètre $p = \frac{1}{3}$ : $E(F_n) = \frac{1}{3}$ et $V(F_n) = \frac{p(1 - p)}{n} = \frac{2}{9n}$.

    **b.** D'après l'inégalité de concentration, il suffit que $\frac{2/9}{n \times 0{,}01^2} \leq 0{,}05$, soit $n \geq \frac{2}{9 \times 0{,}05 \times 0{,}0001} \approx 44\,444{,}4$. La valeur $n = 44\,445$ convient.

    **3.** La condition est `y <= x**2` et la fonction renvoie `compteur / n`.

    **4.** $50\,000 \geq 44\,445$, donc l'écart $\left|F_n - \frac{1}{3}\right|$ est inférieur à $0{,}01$ avec une probabilité d'au moins $0{,}95$. Ici, $|0{,}3312 - 0{,}3333| \approx 0{,}002 < 0{,}01$ : le résultat est cohérent.

    **5.** On remplace la condition par `y <= exp(-x**2)` (la fonction est à valeurs dans $[0, 1]$ sur $[0, 1]$). D'après la loi des grands nombres, la fréquence obtenue se rapproche de l'aire cherchée, et l'inégalité de concentration (avec $V \leq \frac{1}{4}$) indique combien de points utiliser. C'est la **méthode de Monte-Carlo**.
