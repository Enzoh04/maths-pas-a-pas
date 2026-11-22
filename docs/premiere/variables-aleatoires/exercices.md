# Exercices corrigés — Variables aléatoires réelles

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**, sauf l'exercice Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Lois de probabilité | 1 à 5 |
| 2. Espérance et jeux | 6 à 11 |
| 3. Variance et écart-type | 12 à 16 |
| 4. Linéarité, Bernoulli, nombre de succès | 17 à 22 |
| 5. Problèmes et approfondissement | 23 à 28 |

---

## Thème 1 — Lois de probabilité

*Méthode associée : [Méthode 1](methodes.md#methode-1-determiner-la-loi-dune-variable-aleatoire).*

### Exercice 1 — Une urne <span class="etoiles">★</span>

Une urne contient $5$ jetons : deux portent le numéro $1$, deux le numéro $2$ et un le numéro $3$. On tire un jeton au hasard et on note $X$ son numéro. Déterminer la loi de $X$.

??? success "Correction"
    $P(X = 1) = \frac{2}{5}$, $P(X = 2) = \frac{2}{5}$, $P(X = 3) = \frac{1}{5}$. La somme vaut $1$.

### Exercice 2 — Compléter une loi <span class="etoiles">★</span>

$X$ prend les valeurs $0$, $1$, $2$, $3$ avec les probabilités $0{,}1$, $0{,}3$, $a$ et $0{,}2$.

1. Calculer $a$.
2. Calculer $P(X \geq 2)$ et $P(X < 3)$.

??? success "Correction"
    1. $0{,}1 + 0{,}3 + a + 0{,}2 = 1$, donc $a = 0{,}4$.
    2. $P(X \geq 2) = 0{,}4 + 0{,}2 = 0{,}6$ ; $P(X < 3) = 1 - 0{,}2 = 0{,}8$.

### Exercice 3 — Écart entre deux dés <span class="etoiles">★</span>

On lance deux dés équilibrés et on note $X$ la valeur absolue de la différence des deux résultats.

1. À l'aide d'un tableau à double entrée, déterminer la loi de $X$.
2. Calculer $P(X \leq 1)$.

??? success "Correction"
    **1.** Sur les $36$ cases équiprobables :

    | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
    |---|---|---|---|---|---|---|
    | $P(X = k)$ | $\frac{6}{36}$ | $\frac{10}{36}$ | $\frac{8}{36}$ | $\frac{6}{36}$ | $\frac{4}{36}$ | $\frac{2}{36}$ |

    **2.** $\frac{6 + 10}{36} = \frac{16}{36} = \frac{4}{9}$.

### Exercice 4 — Tirages sans remise <span class="etoiles">★★</span>

Une urne contient $3$ boules rouges et $2$ vertes. On tire successivement deux boules sans remise ; $X$ est le nombre de boules rouges obtenues. Déterminer la loi de $X$.

??? success "Correction"
    Avec un arbre : $P(X = 2) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$ ; $P(X = 0) = \frac{2}{5} \times \frac{1}{4} = \frac{1}{10}$ ; $P(X = 1) = 1 - \frac{3}{10} - \frac{1}{10} = \frac{6}{10}$.

### Exercice 5 — Jusqu'au premier « pile » <span class="etoiles">★★</span>

On lance une pièce équilibrée jusqu'à obtenir « pile », sans dépasser $3$ lancers. $X$ est le nombre de lancers effectués.

1. Déterminer la loi de $X$.
2. Calculer $E(X)$.

??? success "Correction"
    1. $X = 1$ si pile au premier lancer : $\frac{1}{2}$. $X = 2$ si face puis pile : $\frac{1}{4}$. $X = 3$ si face puis face (le troisième lancer a lieu quel que soit son résultat) : $\frac{1}{4}$.
    2. $E(X) = \frac{1}{2} + \frac{2}{4} + \frac{3}{4} = \frac{7}{4}$.

---

## Thème 2 — Espérance et jeux

*Méthodes associées : [Méthode 2](methodes.md#methode-2-calculer-et-interpreter-une-esperance) et [Méthode 5](methodes.md#methode-5-trouver-un-parametre-pour-quun-jeu-soit-equitable).*

### Exercice 6 — Calcul direct <span class="etoiles">★</span>

$X$ prend les valeurs $-2$, $0$ et $5$ avec les probabilités $0{,}3$, $0{,}5$ et $0{,}2$. Calculer $E(X)$.

??? success "Correction"
    $E(X) = -0{,}6 + 0 + 1 = 0{,}4$.

### Exercice 7 — Dé et urne <span class="etoiles">★</span>

1. Calculer l'espérance du résultat d'un dé équilibré à six faces.
2. Calculer l'espérance de la variable $X$ de l'exercice 1.

??? success "Correction"
    1. $\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \frac{21}{6} = 3{,}5$.
    2. $\frac{2}{5} + \frac{4}{5} + \frac{3}{5} = \frac{9}{5}$.

### Exercice 8 — Un jeu de dé <span class="etoiles">★★</span>

Un joueur mise $3$ €, puis lance un dé équilibré. Si le résultat est pair, il reçoit le double du résultat (en euros) ; sinon, il ne reçoit rien. On note $G$ son gain net.

1. Déterminer la loi de $G$.
2. Le jeu est-il favorable au joueur ?

??? success "Correction"
    1. Résultat $2$ : $G = 4 - 3 = 1$ ; $4$ : $G = 5$ ; $6$ : $G = 9$ ; impair : $G = -3$. Loi : $P(G = 1) = P(G = 5) = P(G = 9) = \frac{1}{6}$ et $P(G = -3) = \frac{1}{2}$.
    2. $E(G) = \frac{1 + 5 + 9}{6} - \frac{3}{2} = \frac{15}{6} - \frac{9}{6} = 1$. Le jeu est favorable : $1$ € gagné en moyenne par partie.

### Exercice 9 — Une tombola <span class="etoiles">★★</span>

Une tombola vend $1\,000$ tickets à $2$ €. Elle offre $1$ lot de $500$ €, $5$ lots de $100$ € et $20$ lots de $10$ €. On achète un ticket ; $G$ est le gain net.

1. Déterminer la loi de $G$.
2. Calculer $E(G)$ et interpréter.

??? success "Correction"
    1. $G = 498$ avec probabilité $\frac{1}{1\,000}$ ; $98$ avec $\frac{5}{1\,000}$ ; $8$ avec $\frac{20}{1\,000}$ ; $-2$ avec $\frac{974}{1\,000}$.
    2. $E(G) = \frac{498 + 490 + 160 - 1\,948}{1\,000} = \frac{-800}{1\,000} = -0{,}8$ €. *Plus simple : les lots valent $1\,200$ € au total, soit $1{,}20$ € par ticket, pour une mise de $2$ €.* L'organisateur gagne en moyenne $0{,}80$ € par ticket, soit $800$ € au total.

### Exercice 10 — Une mise équitable <span class="etoiles">★★</span>

On lance deux pièces équilibrées. On reçoit $10$ € pour deux « pile », $2$ € pour un seul « pile », rien sinon. Quelle mise rend ce jeu équitable ?

??? success "Correction"
    La somme reçue $R$ a pour espérance $\frac{1}{4} \times 10 + \frac{1}{2} \times 2 + \frac{1}{4} \times 0 = 3{,}5$. Avec une mise $m$, le gain net est $R - m$, d'espérance $3{,}5 - m$ : le jeu est équitable pour $m = 3{,}50$ €.

### Exercice 11 — Retrouver une loi <span class="etoiles">★★★</span>

$X$ prend les valeurs $1$, $2$ et $3$. On sait que $P(X = 1) = 0{,}2$ et $E(X) = 2{,}2$.

1. Déterminer la loi de $X$.
2. Calculer $V(X)$.

??? success "Correction"
    1. Notons $b = P(X = 2)$ et $c = P(X = 3)$ : $b + c = 0{,}8$ et $0{,}2 + 2b + 3c = 2{,}2$, soit $2b + 3c = 2$. En remplaçant $b = 0{,}8 - c$ : $1{,}6 + c = 2$, donc $c = 0{,}4$ et $b = 0{,}4$.
    2. $E\left(X^2\right) = 0{,}2 + 4 \times 0{,}4 + 9 \times 0{,}4 = 5{,}4$, donc $V(X) = 5{,}4 - 2{,}2^2 = 5{,}4 - 4{,}84 = 0{,}56$.

---

## Thème 3 — Variance et écart-type

*Méthode associée : [Méthode 3](methodes.md#methode-3-calculer-une-variance-et-un-ecart-type).*

### Exercice 12 — Calcul direct <span class="etoiles">★</span>

Calculer la variance de la variable $X$ de l'exercice 6.

??? success "Correction"
    $E\left(X^2\right) = 0{,}3 \times 4 + 0{,}5 \times 0 + 0{,}2 \times 25 = 1{,}2 + 5 = 6{,}2$, donc $V(X) = 6{,}2 - 0{,}4^2 = 6{,}04$.

### Exercice 13 — Le dé <span class="etoiles">★</span>

Calculer la variance du résultat $X$ d'un dé équilibré.

??? success "Correction"
    $E\left(X^2\right) = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6}$, donc $V(X) = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12}$.

### Exercice 14 — Comparer deux placements <span class="etoiles">★★</span>

Un placement $A$ rapporte $2\,\%$ de façon certaine. Un placement $B$ rapporte $10\,\%$ ou perd $4\,\%$, avec la probabilité $\frac{1}{2}$ chacun. On note $R_A$ et $R_B$ les rendements (en $\%$).

1. Calculer l'espérance et l'écart-type de $R_A$ et de $R_B$.
2. Comparer les deux placements.

??? success "Correction"
    1. $E(R_A) = 2$ et $\sigma(R_A) = 0$. $E(R_B) = \frac{10 - 4}{2} = 3$ ; $E\left(R_B^2\right) = \frac{100 + 16}{2} = 58$, $V(R_B) = 58 - 9 = 49$, $\sigma(R_B) = 7$.
    2. $B$ rapporte plus en moyenne ($3\,\%$ contre $2\,\%$), mais il est beaucoup plus **risqué** (écart-type de $7$ points). Le choix dépend du goût du risque de l'investisseur.

### Exercice 15 — Deux méthodes <span class="etoiles">★★</span>

$X$ prend les valeurs $0$, $2$ et $4$ avec les probabilités $\frac{1}{4}$, $\frac{1}{2}$ et $\frac{1}{4}$. Calculer $V(X)$ avec la définition, puis avec la formule de König-Huygens.

??? success "Correction"
    $E(X) = 0 + 1 + 1 = 2$.

    Définition : $\frac{1}{4}(0 - 2)^2 + \frac{1}{2}(2 - 2)^2 + \frac{1}{4}(4 - 2)^2 = 1 + 0 + 1 = 2$.

    König-Huygens : $E\left(X^2\right) = 0 + 2 + 4 = 6$, et $6 - 4 = 2$.

### Exercice 16 — Une variance nulle <span class="etoiles">★★★</span>

1. Justifier que $V(X) \geq 0$ pour toute variable aléatoire $X$. En déduire que $E(X)^2 \leq E\left(X^2\right)$.
2. Montrer que $V(X) = 0$ si et seulement si $X$ ne prend qu'une seule valeur (avec une probabilité non nulle).

??? success "Correction"
    1. $V(X)$ est une somme de termes $p_i(x_i - E(X))^2$, tous positifs : $V(X) \geq 0$. Avec König-Huygens : $E\left(X^2\right) - E(X)^2 \geq 0$.
    2. Si $X$ ne prend que la valeur $c$ (avec probabilité $1$), $E(X) = c$ et $V(X) = 1 \times (c - c)^2 = 0$. Réciproquement, une somme de termes positifs est nulle si et seulement si chaque terme l'est : pour chaque valeur $x_i$ de probabilité $p_i > 0$, on a $x_i = E(X)$. Toutes ces valeurs sont donc égales à $E(X)$.

---

## Thème 4 — Linéarité, Bernoulli, nombre de succès

*Méthode associée : [Méthode 4](methodes.md#methode-4-utiliser-la-linearite).*

### Exercice 17 — Appliquer les formules <span class="etoiles">★</span>

On sait que $E(X) = 5$ et $V(X) = 4$. Calculer l'espérance, la variance et l'écart-type de $3X - 2$, puis de $-X + 1$.

??? success "Correction"
    $E(3X - 2) = 13$, $V(3X - 2) = 9 \times 4 = 36$, $\sigma = 6$.

    $E(-X + 1) = -4$, $V(-X + 1) = (-1)^2 \times 4 = 4$, $\sigma = 2$.

### Exercice 18 — Variable de Bernoulli <span class="etoiles">★</span>

$X$ suit une loi de Bernoulli de paramètre $0{,}3$. Calculer $E(X)$, $V(X)$ et $\sigma(X)$.

??? success "Correction"
    $E(X) = 0{,}3$ ; $V(X) = 0{,}3 \times 0{,}7 = 0{,}21$ ; $\sigma(X) = \sqrt{0{,}21}$.

### Exercice 19 — Changement d'unité <span class="etoiles">★★</span>

La température de midi dans une ville, en degrés Celsius, est une variable aléatoire $X$ d'espérance $20$ et d'écart-type $5$. La température en degrés Fahrenheit est $F = 1{,}8X + 32$. Calculer $E(F)$ et $\sigma(F)$.

??? success "Correction"
    $E(F) = 1{,}8 \times 20 + 32 = 68$ °F ; $\sigma(F) = 1{,}8 \times 5 = 9$ °F (la constante $32$ n'intervient pas).

### Exercice 20 — Variable centrée réduite <span class="etoiles">★★</span>

$X$ est une variable aléatoire d'espérance $\mu$ et d'écart-type $\sigma > 0$. On pose $Z = \dfrac{X - \mu}{\sigma}$.

1. Calculer $E(Z)$ et $V(Z)$.
2. Application : $\mu = 10$ et $\sigma = 2$. Exprimer $Z$ en fonction de $X$.

??? success "Correction"
    1. $Z = \frac{1}{\sigma}X - \frac{\mu}{\sigma}$, donc $E(Z) = \frac{\mu}{\sigma} - \frac{\mu}{\sigma} = 0$ et $V(Z) = \frac{1}{\sigma^2}V(X) = 1$. On dit que $Z$ est **centrée réduite**.
    2. $Z = \frac{X - 10}{2} = 0{,}5X - 5$.

### Exercice 21 — Trois lancers de pièce <span class="etoiles">★★</span>

On lance $3$ fois une pièce équilibrée ; $S$ est le nombre de « pile ».

1. Déterminer la loi de $S$.
2. Calculer $E(S)$ et $V(S)$. Comparer avec $np$ et $np(1 - p)$.

??? success "Correction"
    1. $P(S = 0) = \frac{1}{8}$, $P(S = 1) = \frac{3}{8}$, $P(S = 2) = \frac{3}{8}$, $P(S = 3) = \frac{1}{8}$.
    2. $E(S) = \frac{0 + 3 + 6 + 3}{8} = \frac{12}{8} = 1{,}5$ ; $E\left(S^2\right) = \frac{0 + 3 + 12 + 9}{8} = 3$, donc $V(S) = 3 - 2{,}25 = 0{,}75$. Avec $n = 3$ et $p = \frac{1}{2}$ : $np = 1{,}5$ et $np(1 - p) = 0{,}75$. ✓

### Exercice 22 — Deux épreuves, cas général <span class="etoiles">★★★</span>

On répète deux fois, de façon indépendante, une épreuve de Bernoulli de paramètre $p$. $S$ est le nombre de succès. Montrer que $E(S) = 2p$ et $V(S) = 2p(1 - p)$.

??? success "Correction"
    Loi : $P(S = 0) = (1 - p)^2$, $P(S = 1) = 2p(1 - p)$, $P(S = 2) = p^2$.

    $E(S) = 2p(1 - p) + 2p^2 = 2p$. $E\left(S^2\right) = 2p(1 - p) + 4p^2 = 2p + 2p^2$, donc $V(S) = 2p + 2p^2 - 4p^2 = 2p - 2p^2 = 2p(1 - p)$.

---

## Thème 5 — Problèmes et approfondissement

### Exercice 23 — Assurance <span class="etoiles">★★</span>

Un assureur estime que, pendant un an, un client a un accident grave (coût $5\,000$ €) avec la probabilité $0{,}01$, un accident léger (coût $400$ €) avec la probabilité $0{,}05$, et aucun accident sinon.

1. Calculer l'espérance du coût $C$ d'un client.
2. L'assureur fixe la prime annuelle à $100$ €. Quel est son gain moyen par client ? Pour $10\,000$ clients ?

??? success "Correction"
    1. $E(C) = 0{,}01 \times 5\,000 + 0{,}05 \times 400 = 50 + 20 = 70$ €.
    2. Gain $G = 100 - C$, $E(G) = 100 - 70 = 30$ € par client, soit environ $300\,000$ € pour $10\,000$ clients.

### Exercice 24 — Jeu à deux tirages <span class="etoiles">★★</span>

Une urne contient $2$ boules rouges et $3$ boules noires. On paie $2$ € pour tirer successivement deux boules **avec remise**, et on reçoit $5$ € par boule rouge. $S$ est le nombre de boules rouges, $G = 5S - 2$ le gain net.

1. Déterminer la loi de $S$, puis $E(S)$ et $V(S)$.
2. En déduire $E(G)$ et $\sigma(G)$.

??? success "Correction"
    1. $p = 0{,}4$ : $P(S = 0) = 0{,}36$, $P(S = 1) = 2 \times 0{,}4 \times 0{,}6 = 0{,}48$, $P(S = 2) = 0{,}16$. $E(S) = 0{,}48 + 0{,}32 = 0{,}8$ ; $E\left(S^2\right) = 0{,}48 + 0{,}64 = 1{,}12$, $V(S) = 1{,}12 - 0{,}64 = 0{,}48$.
    2. $E(G) = 5 \times 0{,}8 - 2 = 2$ € ; $V(G) = 25 \times 0{,}48 = 12$, $\sigma(G) = \sqrt{12} = 2\sqrt{3}$ €.

### Exercice 25 — Contrat de maintenance <span class="etoiles">★★</span>

Le nombre $X$ de pannes mensuelles d'une machine suit la loi :

| $k$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $P(X = k)$ | $0{,}5$ | $0{,}3$ | $0{,}15$ | $0{,}05$ |

Chaque panne coûte $200$ €, plus un coût fixe mensuel de $100$ €. Un réparateur propose un forfait de $240$ € par mois, toutes pannes comprises. Le forfait est-il intéressant en moyenne ?

??? success "Correction"
    $E(X) = 0{,}3 + 0{,}3 + 0{,}15 = 0{,}75$. Coût sans forfait : $C = 200X + 100$, $E(C) = 150 + 100 = 250$ €. Le forfait ($240$ €) est légèrement moins cher en moyenne, et il supprime le risque d'un mois coûteux.

### Exercice 26 — Jusqu'au premier $6$ <span class="etoiles">★★★</span>

On lance un dé au plus $3$ fois, en s'arrêtant au premier $6$. On gagne $10$ € si le $6$ sort au premier lancer, $5$ € s'il sort au deuxième, $2$ € s'il sort au troisième, et l'on perd $4$ € si aucun $6$ ne sort.

1. Déterminer la loi du gain $G$.
2. Calculer $E(G)$. Le jeu est-il favorable ?

??? success "Correction"
    1. $P(G = 10) = \frac{1}{6}$ ; $P(G = 5) = \frac{5}{6} \times \frac{1}{6} = \frac{5}{36}$ ; $P(G = 2) = \left(\frac{5}{6}\right)^2 \times \frac{1}{6} = \frac{25}{216}$ ; $P(G = -4) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}$.
    2. Au dénominateur $216$ : $E(G) = \frac{360 + 150 + 50 - 500}{216} = \frac{60}{216} = \frac{5}{18} \approx 0{,}28$ €. Le jeu est (légèrement) favorable.

### Exercice 27 — Simulation <span class="etoiles">★★★</span>

1. Écrire une fonction `partie()` qui simule le jeu de l'exercice 26 et renvoie le gain.
2. Écrire une fonction `moyenne_ecart(N)` qui simule $N$ parties, stocke les gains dans une liste et renvoie leur moyenne et leur écart-type.
3. Comparer avec $E(G) \approx 0{,}28$ et $\sigma(G) \approx 5{,}46$.

??? success "Correction"
    ```python
    from random import randint
    from math import sqrt

    def partie():
        gains = [10, 5, 2]
        for i in range(3):
            if randint(1, 6) == 6:
                return gains[i]
        return -4

    def moyenne_ecart(N):
        L = [partie() for i in range(N)]
        m = sum(L) / N
        v = sum((x - m)**2 for x in L) / N
        return m, sqrt(v)

    print(moyenne_ecart(100000))   # environ (0.28, 5.46)
    ```

    Avec $100\,000$ parties, la moyenne et l'écart-type observés sont très proches de $E(G)$ et de $\sigma(G) = \sqrt{\frac{4\,825}{162}} \approx 5{,}46$.

### Exercice 28 — Combien de gâteaux préparer ? <span class="etoiles">★★★</span>

Un pâtissier prépare chaque matin $n$ gâteaux ($n \in \{1, 2, 3\}$), qui lui coûtent $2$ € pièce ; il les vend $5$ € pièce, et les invendus sont perdus. La demande $D$ suit la loi : $P(D = 1) = 0{,}2$, $P(D = 2) = 0{,}5$, $P(D = 3) = 0{,}3$.

Pour chaque valeur de $n$, calculer l'espérance du bénéfice. Combien de gâteaux doit-il préparer ?

??? success "Correction"
    Il vend $\min(n, D)$ gâteaux ; bénéfice $B_n = 5\min(n, D) - 2n$.

    - $n = 1$ : il vend toujours $1$ gâteau, $B_1 = 3$, $E(B_1) = 3$.
    - $n = 2$ : $B_2 = 1$ si $D = 1$, $6$ sinon : $E(B_2) = 0{,}2 \times 1 + 0{,}8 \times 6 = 5$.
    - $n = 3$ : $B_3 = -1$, $4$ ou $9$ : $E(B_3) = -0{,}2 + 2 + 2{,}7 = 4{,}5$.

    Il a intérêt à préparer $2$ gâteaux.
