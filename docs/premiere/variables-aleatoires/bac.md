# Sujets type épreuve anticipée — Variables aléatoires réelles

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

L'épreuve anticipée de mathématiques dure **2 heures, sans calculatrice**, avec un **QCM d'automatismes** (6 points) et **deux ou trois exercices** (14 points). Chaque sujet ci-dessous comporte **six questions d'automatismes** puis **un exercice**. Compte environ **40 minutes** par sujet.

| Sujet | Exercice | Durée conseillée |
|---|---|---|
| 1 | La roue de la fête foraine | 35 min |
| 2 | Trois épreuves de Bernoulli | 40 min |
| 3 | Une loi à compléter | 35 min |
| 4 | Avec ou sans remise ? | 40 min |

## Sujet 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** $X$ prend les valeurs $1$ et $3$ avec les probabilités $0{,}6$ et $0{,}4$. $E(X)$ vaut :

a. $2$ ; b. $1{,}8$ ; c. $2{,}2$ ; d. $1{,}2$.

**Question 2.** Si $E(X) = 4$, alors $E(2X - 3)$ vaut :

a. $8$ ; b. $5$ ; c. $11$ ; d. $1$.

**Question 3.** Si $V(X) = 9$, alors $\sigma(-2X + 5)$ vaut :

a. $-6$ ; b. $6$ ; c. $36$ ; d. $11$.

**Question 4.** $\dfrac{1}{8} + \dfrac{3}{8} \times 2$ est égal à :

a. $\frac{7}{8}$ ; b. $\frac{1}{2}$ ; c. $\frac{4}{8}$ ; d. $\frac{7}{16}$.

**Question 5.** Le nombre $10^{-3}$ est égal à :

a. $-1\,000$ ; b. $0{,}001$ ; c. $0{,}0001$ ; d. $-0{,}001$.

**Question 6.** La solution de $\frac{x}{4} - 1 = 2$ est :

a. $12$ ; b. $4$ ; c. $\frac{3}{4}$ ; d. $8$.

### Partie 2 — Exercice

Une roue est partagée en $8$ secteurs de même taille : $1$ secteur rapporte $10$ €, $3$ secteurs rapportent $2$ €, et $4$ secteurs ne rapportent rien. Une partie coûte $2$ €. On note $G$ le gain net du joueur sur une partie.

1. Déterminer la loi de $G$.
2. Calculer $E(G)$. Le jeu est-il équitable ?
3. Calculer $V(G)$ et $\sigma(G)$.
4. L'organisateur veut gagner en moyenne $0{,}50$ € par partie. Quel prix doit-il fixer pour une partie ?

??? success "Correction"
    **Partie 1**

    1. **b.** $0{,}6 + 1{,}2$. 2. **b.** 3. **b.** $2 \times 3$. 4. **a.** 5. **b.** 6. **a.**

    **Partie 2**

    **1.** $P(G = 8) = \frac{1}{8}$, $P(G = 0) = \frac{3}{8}$, $P(G = -2) = \frac{4}{8} = \frac{1}{2}$.

    **2.** $E(G) = 1 + 0 - 1 = 0$ : le jeu est équitable.

    **3.** $E\left(G^2\right) = \frac{64}{8} + 0 + \frac{4}{2} = 10$, donc $V(G) = 10 - 0 = 10$ et $\sigma(G) = \sqrt{10}$ €.

    **4.** La somme reçue $R$ a pour espérance $\frac{10}{8} + \frac{3 \times 2}{8} = 2$. Avec un prix $m$, le gain du joueur vaut $R - m$, d'espérance $2 - m$ ; l'organisateur gagne en moyenne $m - 2$. On veut $m - 2 = 0{,}5$ : $m = 2{,}50$ €.

---

## Sujet 2

### Partie 1 — Automatismes (QCM)

**Question 1.** Une variable de Bernoulli de paramètre $0{,}2$ a pour variance :

a. $0{,}2$ ; b. $0{,}04$ ; c. $0{,}16$ ; d. $0{,}8$.

**Question 2.** $0{,}8^3$ est égal à :

a. $2{,}4$ ; b. $0{,}512$ ; c. $0{,}64$ ; d. $0{,}0512$.

**Question 3.** $3 \times 0{,}2 \times 0{,}8^2$ est égal à :

a. $0{,}384$ ; b. $0{,}096$ ; c. $0{,}48$ ; d. $0{,}128$.

**Question 4.** On répète $3$ fois une épreuve. Le nombre de chemins de l'arbre comportant exactement un succès est :

a. $1$ ; b. $2$ ; c. $3$ ; d. $8$.

**Question 5.** La moyenne de la série $2 \,;\, 2 \,;\, 5 \,;\, 7$ est :

a. $4$ ; b. $3{,}5$ ; c. $5$ ; d. $16$.

**Question 6.** Une droite passe par $(0\,;\,1)$ et $(2\,;\,5)$. Son coefficient directeur est :

a. $3$ ; b. $2$ ; c. $\frac{1}{2}$ ; d. $4$.

### Partie 2 — Exercice

Un jeu de grattage est gagnant avec la probabilité $0{,}2$. Un joueur achète $3$ tickets ; on admet que les résultats sont indépendants. On note $S$ le nombre de tickets gagnants.

1. Justifier que la situation est une répétition de $3$ épreuves de Bernoulli identiques et indépendantes, dont on précisera le paramètre.
2. Déterminer la loi de $S$.
3. Calculer $E(S)$ et $V(S)$.
4. Chaque ticket coûte $1$ € et chaque ticket gagnant rapporte $4$ €. Exprimer le gain net $G$ en fonction de $S$, puis calculer $E(G)$ et $\sigma(G)$.

??? success "Correction"
    **Partie 1**

    1. **c.** $0{,}2 \times 0{,}8$. 2. **b.** 3. **a.** 4. **c.** 5. **a.** 6. **b.**

    **Partie 2**

    **1.** Chaque ticket est une épreuve à deux issues : gagnant (succès, $p = 0{,}2$) ou perdant. Les $3$ épreuves sont identiques et indépendantes.

    **2.** $P(S = 0) = 0{,}8^3 = 0{,}512$ ; $P(S = 1) = 3 \times 0{,}2 \times 0{,}64 = 0{,}384$ ; $P(S = 2) = 3 \times 0{,}04 \times 0{,}8 = 0{,}096$ ; $P(S = 3) = 0{,}008$. La somme vaut $1$.

    **3.** $E(S) = 0{,}384 + 0{,}192 + 0{,}024 = 0{,}6$. $E\left(S^2\right) = 0{,}384 + 0{,}384 + 0{,}072 = 0{,}84$, donc $V(S) = 0{,}84 - 0{,}36 = 0{,}48$. *(On retrouve $np = 0{,}6$ et $np(1 - p) = 0{,}48$.)*

    **4.** $G = 4S - 3$. $E(G) = 4 \times 0{,}6 - 3 = -0{,}6$ € ; $\sigma(G) = 4\sqrt{0{,}48} = 4 \times \sqrt{\frac{48}{100}} = \frac{4 \times 4\sqrt{3}}{10} = \frac{8\sqrt{3}}{5}$ €.

---

## Sujet 3

### Partie 1 — Automatismes (QCM)

**Question 1.** Les probabilités d'une loi sont $0{,}1$, $0{,}25$, $0{,}4$ et $a$. Alors $a$ vaut :

a. $0{,}35$ ; b. $0{,}25$ ; c. $0{,}3$ ; d. $0{,}15$.

**Question 2.** Si $E(X) = 2$ et $E\left(X^2\right) = 7$, alors $V(X)$ vaut :

a. $5$ ; b. $3$ ; c. $9$ ; d. $\sqrt{3}$.

**Question 3.** $1{,}9^2$ est égal à :

a. $3{,}8$ ; b. $3{,}61$ ; c. $3{,}81$ ; d. $1{,}81$.

**Question 4.** Le système $x + y = 0{,}5$ et $x + 3y = 1{,}1$ a pour solution :

a. $x = 0{,}3$, $y = 0{,}2$ ; b. $x = 0{,}2$, $y = 0{,}3$ ; c. $x = 0{,}1$, $y = 0{,}4$ ; d. $x = 0{,}25$, $y = 0{,}25$.

**Question 5.** Un prix de $120$ € augmente de $5\,\%$. Le nouveau prix est :

a. $125$ € ; b. $126$ € ; c. $114$ € ; d. $180$ €.

**Question 6.** La fonction $f(x) = x^2 - 4$ s'annule en :

a. $4$ seulement ; b. $-2$ et $2$ ; c. $2$ seulement ; d. $-4$ et $4$.

### Partie 2 — Exercice

Une variable aléatoire $X$ suit la loi suivante, où $x$ et $y$ sont deux réels :

| $k$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $P(X = k)$ | $0{,}1$ | $x$ | $0{,}4$ | $y$ |

On sait de plus que $E(X) = 1{,}9$.

1. Montrer que $x + y = 0{,}5$ et $x + 3y = 1{,}1$. En déduire $x$ et $y$.
2. Calculer $P(X \geq 2)$.
3. Calculer $V(X)$.
4. On pose $Y = 2X + 1$. Calculer $E(Y)$ et $V(Y)$.

??? success "Correction"
    **Partie 1**

    1. **b.** $1 - 0{,}75$. 2. **b.** $7 - 4$. 3. **b.** 4. **b.** $2y = 0{,}6$. 5. **b.** $120 \times 1{,}05$. 6. **b.**

    **Partie 2**

    **1.** La somme des probabilités vaut $1$ : $0{,}5 + x + y = 1$. L'espérance : $x + 0{,}8 + 3y = 1{,}9$. En soustrayant : $2y = 0{,}6$, donc $y = 0{,}3$ et $x = 0{,}2$.

    **2.** $P(X \geq 2) = 0{,}4 + 0{,}3 = 0{,}7$.

    **3.** $E\left(X^2\right) = 0{,}2 + 1{,}6 + 2{,}7 = 4{,}5$, donc $V(X) = 4{,}5 - 1{,}9^2 = 4{,}5 - 3{,}61 = 0{,}89$.

    **4.** $E(Y) = 2 \times 1{,}9 + 1 = 4{,}8$ ; $V(Y) = 4 \times 0{,}89 = 3{,}56$.

---

## Sujet 4

### Partie 1 — Automatismes (QCM)

**Question 1.** Une urne contient $2$ boules rouges et $2$ bleues. On tire deux boules sans remise. La probabilité d'obtenir deux rouges est :

a. $\frac{1}{4}$ ; b. $\frac{1}{6}$ ; c. $\frac{1}{3}$ ; d. $\frac{1}{2}$.

**Question 2.** Même urne, deux tirages avec remise. La probabilité d'obtenir deux rouges est :

a. $\frac{1}{4}$ ; b. $\frac{1}{6}$ ; c. $\frac{1}{3}$ ; d. $\frac{1}{2}$.

**Question 3.** $E(X) = 0{,}5$ et $E\left(X^2\right) = 7{,}5$. Alors $V(X)$ vaut :

a. $7$ ; b. $7{,}25$ ; c. $7{,}5$ ; d. $6{,}75$.

**Question 4.** $\dfrac{36}{6} + \dfrac{9}{6}$ est égal à :

a. $7{,}5$ ; b. $\frac{45}{12}$ ; c. $6{,}5$ ; d. $8$.

**Question 5.** Le minimum de $x \mapsto (x - 1)^2 + 3$ sur $\mathbb{R}$ vaut :

a. $1$ ; b. $-1$ ; c. $3$ ; d. $4$.

**Question 6.** Un article coûte $45$ € après une baisse de $10\,\%$. Son prix initial était :

a. $49{,}50$ € ; b. $50$ € ; c. $40{,}50$ € ; d. $55$ €.

### Partie 2 — Exercice

Une urne contient $2$ boules rouges et $2$ boules bleues. Un joueur tire deux boules. Il gagne $6$ € s'il obtient deux rouges, ne gagne ni ne perd rien s'il en obtient une, et perd $3$ € s'il n'en obtient aucune. On note $G$ son gain.

1. **Tirages sans remise.**  
    a. Déterminer la loi du nombre $X$ de boules rouges, puis la loi de $G$.  
    b. Calculer $E(G)$ et $V(G)$.
2. **Tirages avec remise.**  
    a. Déterminer la nouvelle loi de $G$.  
    b. Calculer $E(G)$.
3. Quelle règle le joueur doit-il préférer ?

??? success "Correction"
    **Partie 1**

    1. **b.** $\frac{2}{4} \times \frac{1}{3}$. 2. **a.** $\frac{1}{2} \times \frac{1}{2}$. 3. **b.** $7{,}5 - 0{,}25$. 4. **a.** 5. **c.** 6. **b.** $\frac{45}{0{,}9}$.

    **Partie 2**

    **1. a.** $P(X = 2) = \frac{2}{4} \times \frac{1}{3} = \frac{1}{6}$ ; $P(X = 0) = \frac{1}{6}$ (même calcul avec les bleues) ; $P(X = 1) = 1 - \frac{2}{6} = \frac{2}{3}$. D'où $P(G = 6) = \frac{1}{6}$, $P(G = 0) = \frac{2}{3}$, $P(G = -3) = \frac{1}{6}$.

    **b.** $E(G) = 1 + 0 - \frac{1}{2} = \frac{1}{2}$. $E\left(G^2\right) = \frac{36}{6} + \frac{9}{6} = 7{,}5$, donc $V(G) = 7{,}5 - 0{,}25 = 7{,}25$.

    **2. a.** Épreuves indépendantes de paramètre $\frac{1}{2}$ : $P(G = 6) = \frac{1}{4}$, $P(G = 0) = \frac{1}{2}$, $P(G = -3) = \frac{1}{4}$.

    **b.** $E(G) = \frac{6}{4} - \frac{3}{4} = \frac{3}{4}$.

    **3.** L'espérance est plus grande avec remise ($0{,}75$ € contre $0{,}50$ €) : le joueur a intérêt à jouer avec remise (le risque est aussi un peu plus grand : $V(G) = 9 + 2{,}25 - 0{,}5625 = 10{,}6875$).
