# Exercices corrigés — Sommes de variables aléatoires

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Linéarité de l'espérance | 1 à 6 |
| 2. Indépendance et variance | 7 à 12 |
| 3. Loi binomiale et variables de Bernoulli | 13 à 17 |
| 4. Échantillons, sommes et moyennes | 18 à 23 |
| 5. Approfondissement | 24 à 28 |

---

## Thème 1 — Linéarité de l'espérance

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-lesperance-dune-somme).*

### Exercice 1 — Révisions de Première <span class="etoiles">★</span>

La variable $X$ prend les valeurs $-1$, $0$, $2$ avec les probabilités $0{,}2$, $0{,}5$, $0{,}3$. Calculer $E(X)$, $V(X)$, puis $E(3X - 2)$ et $V(3X - 2)$.

??? success "Correction"
    $E(X) = -0{,}2 + 0 + 0{,}6 = 0{,}4$. $E(X^2) = 0{,}2 + 0 + 1{,}2 = 1{,}4$, donc $V(X) = 1{,}4 - 0{,}16 = 1{,}24$. Puis $E(3X - 2) = 1{,}2 - 2 = -0{,}8$ et $V(3X - 2) = 9 \times 1{,}24 = 11{,}16$.

### Exercice 2 — Combinaisons linéaires <span class="etoiles">★</span>

On sait que $E(X) = 5$ et $E(Y) = -2$. Calculer $E(X + Y)$ et $E(2X - 3Y + 1)$. A-t-on besoin de savoir si $X$ et $Y$ sont indépendantes ?

??? success "Correction"
    $E(X + Y) = 3$ et $E(2X - 3Y + 1) = 10 + 6 + 1 = 17$. Non : la linéarité de l'espérance est vraie sans hypothèse d'indépendance.

### Exercice 3 — Une moyenne coefficientée <span class="etoiles">★</span>

Un élève a trois notes aléatoires $A$, $B$, $C$ d'espérances respectives $12$, $10$ et $14$. Sa moyenne est $N = \dfrac{2A + 3B + C}{6}$. Calculer $E(N)$.

??? success "Correction"
    $E(N) = \dfrac{2 \times 12 + 3 \times 10 + 14}{6} = \dfrac{68}{6} = \dfrac{34}{3} \approx 11{,}33$.

### Exercice 4 — Un dé et une pièce <span class="etoiles">★</span>

On lance un dé équilibré et une pièce équilibrée. On marque le résultat du dé, plus $10$ points si la pièce tombe sur Pile. Calculer l'espérance du score, puis sa variance.

??? success "Correction"
    Score $S = D + 10P$, où $D$ est le résultat du dé et $P$ vaut $1$ si Pile, $0$ sinon. $E(S) = 3{,}5 + 10 \times 0{,}5 = 8{,}5$. Les deux lancers sont indépendants, donc $V(S) = V(D) + 100\,V(P) = \frac{35}{12} + 100 \times \frac{1}{4} = \frac{335}{12} \approx 27{,}9$.

### Exercice 5 — Dix dés <span class="etoiles">★</span>

On lance dix dés équilibrés. Quelle est l'espérance de la somme des résultats ? Pourquoi serait-il très long de la calculer à partir de la loi de la somme ?

??? success "Correction"
    Par linéarité : $E = 10 \times 3{,}5 = 35$. La somme prend $51$ valeurs (de $10$ à $60$) et il y a $6^{10}$ issues : déterminer sa loi serait très long, alors que la linéarité donne l'espérance en une ligne.

### Exercice 6 — Le produit n'est pas linéaire <span class="etoiles">★★</span>

$X$ prend les valeurs $-1$ et $1$ avec la probabilité $\frac{1}{2}$, et $Y = X$. Comparer $E(XY)$ et $E(X)E(Y)$. Que peut-on en déduire sur l'indépendance de $X$ et $Y$ ?

??? success "Correction"
    $XY = X^2 = 1$, donc $E(XY) = 1$, alors que $E(X)E(Y) = 0 \times 0 = 0$. Si $X$ et $Y$ étaient indépendantes, on aurait $E(XY) = E(X)E(Y)$ : elles ne le sont donc pas (ce qui est évident ici, puisque $Y = X$).

---

## Thème 2 — Indépendance et variance

*Méthodes associées : [Méthode 2](methodes.md#methode-2-determiner-la-loi-dune-somme-de-deux-variables-independantes) et [Méthode 3](methodes.md#methode-3-calculer-la-variance-dune-somme).*

### Exercice 7 — La somme de deux dés <span class="etoiles">★</span>

On lance deux dés équilibrés et $S$ est la somme des résultats. Calculer $P(S = 7)$ et $P(S \geq 10)$.

??? success "Correction"
    Les $36$ couples sont équiprobables. $S = 7$ pour $6$ couples : $P(S = 7) = \frac{1}{6}$. $S \geq 10$ pour $3 + 2 + 1 = 6$ couples : $P(S \geq 10) = \frac{1}{6}$.

### Exercice 8 — Variance de deux dés <span class="etoiles">★★</span>

1. Montrer que la variance du résultat d'un dé équilibré est $\frac{35}{12}$.
2. En déduire la variance et l'écart type de la somme $S$ de deux dés.
3. Retrouver $V(S)$ à partir de la loi de $S$ (cours, § 2.1).

??? success "Correction"
    **1.** $E(X^2) = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6}$, donc $V(X) = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12}$.

    **2.** Les dés sont indépendants : $V(S) = \frac{35}{6} \approx 5{,}83$ et $\sigma(S) \approx 2{,}42$.

    **3.** $E(S^2) = \frac{1}{36}\left(4 + 18 + 48 + 100 + 180 + 294 + 320 + 324 + 300 + 242 + 144\right) = \frac{1974}{36} = \frac{329}{6}$, donc $V(S) = \frac{329}{6} - 49 = \frac{35}{6}$.

### Exercice 9 — Règles de calcul <span class="etoiles">★</span>

$X$ et $Y$ sont indépendantes, avec $V(X) = 3$ et $V(Y) = 1$. Calculer $V(X + Y)$, $V(X - Y)$ et $V(3X - 2Y + 7)$.

??? success "Correction"
    $V(X + Y) = 4$, $V(X - Y) = 3 + 1 = 4$, $V(3X - 2Y + 7) = 9 \times 3 + 4 \times 1 = 31$.

### Exercice 10 — Quand l'indépendance manque <span class="etoiles">★★</span>

$X$ suit la loi de Bernoulli de paramètre $\frac{1}{2}$ et $Y = 1 - X$. Calculer $V(X)$, $V(Y)$ et $V(X + Y)$. Commenter.

??? success "Correction"
    $V(X) = V(Y) = \frac{1}{4}$. Mais $X + Y = 1$ est constante, donc $V(X + Y) = 0 \neq \frac{1}{2}$. Les variables ne sont pas indépendantes ($Y$ est entièrement déterminée par $X$) : la formule d'additivité ne s'applique pas.

### Exercice 11 — Loi d'une somme <span class="etoiles">★★</span>

$X$ suit la loi uniforme sur $\{1, 2, 3\}$ et $Y$ la loi uniforme sur $\{0, 1\}$ ; elles sont indépendantes.

1. Déterminer la loi de $S = X + Y$.
2. Calculer $E(S)$ de deux façons.
3. Calculer $V(S)$ de deux façons.

??? success "Correction"
    **1.** Chaque couple a la probabilité $\frac{1}{3} \times \frac{1}{2} = \frac{1}{6}$ :

    | $s$ | $1$ | $2$ | $3$ | $4$ |
    |---|---|---|---|---|
    | $P(S = s)$ | $\frac{1}{6}$ | $\frac{2}{6}$ | $\frac{2}{6}$ | $\frac{1}{6}$ |

    **2.** Avec la loi : $\frac{1 + 4 + 6 + 4}{6} = \frac{15}{6} = 2{,}5$. Par linéarité : $2 + 0{,}5 = 2{,}5$.

    **3.** Avec la loi : $E(S^2) = \frac{1 + 8 + 18 + 16}{6} = \frac{43}{6}$, donc $V(S) = \frac{43}{6} - \frac{25}{4} = \frac{11}{12}$. Par indépendance : $V(X) = \frac{14}{3} - 4 = \frac{2}{3}$ et $V(Y) = \frac{1}{4}$, donc $V(S) = \frac{2}{3} + \frac{1}{4} = \frac{11}{12}$.

### Exercice 12 — Deux variables de Bernoulli <span class="etoiles">★★</span>

$X_1$ et $X_2$ suivent la loi de Bernoulli de paramètre $p$ et sont indépendantes. Déterminer la loi de $X_1 + X_2$ et la reconnaître.

??? success "Correction"
    Avec $q = 1 - p$ : $P(X_1 + X_2 = 0) = q^2$, $P(X_1 + X_2 = 1) = pq + qp = 2pq$, $P(X_1 + X_2 = 2) = p^2$. C'est la loi $\mathcal{B}(2, p)$.

---

## Thème 3 — Loi binomiale et variables de Bernoulli

*Méthode associée : [Méthode 4](methodes.md#methode-4-decomposer-une-variable-de-comptage).*

### Exercice 13 — La démonstration du cours <span class="etoiles">★</span>

Rédiger sans regarder le cours la démonstration de $E(X) = np$ et $V(X) = np(1 - p)$ pour $X \sim \mathcal{B}(n, p)$, en précisant où l'indépendance intervient.

??? success "Correction"
    Voir le cours, § 4. L'indépendance des $X_i$ n'intervient **que pour la variance**. L'espérance utilise seulement la linéarité.

### Exercice 14 — Le nombre de six <span class="etoiles">★</span>

On lance $12$ fois un dé. En décomposant le nombre $X$ de six obtenus en une somme de variables de Bernoulli, calculer $E(X)$ et $V(X)$.

??? success "Correction"
    $X = X_1 + \cdots + X_{12}$, où $X_i$ vaut $1$ si le $i$-ème lancer donne un six. Chaque $X_i$ suit la loi de Bernoulli de paramètre $\frac{1}{6}$, et les lancers sont indépendants. $E(X) = 12 \times \frac{1}{6} = 2$ et $V(X) = 12 \times \frac{1}{6} \times \frac{5}{6} = \frac{5}{3}$.

### Exercice 15 — Retour au QCM <span class="etoiles">★★</span>

Un QCM a $20$ questions à $4$ réponses ; une bonne réponse rapporte $1$ point, une mauvaise en retire $\frac{1}{3}$. Un candidat répond au hasard. On note $N_i$ les points obtenus à la question $i$ et $N = N_1 + \cdots + N_{20}$.

1. Calculer $E(N_i)$ et $V(N_i)$.
2. En déduire $E(N)$ et $V(N)$.

??? success "Correction"
    **1.** $N_i$ vaut $1$ avec probabilité $\frac{1}{4}$ et $-\frac{1}{3}$ avec probabilité $\frac{3}{4}$. $E(N_i) = \frac{1}{4} - \frac{1}{4} = 0$. $E(N_i^2) = \frac{1}{4} + \frac{1}{9} \times \frac{3}{4} = \frac{1}{3}$, donc $V(N_i) = \frac{1}{3}$.

    **2.** $E(N) = 0$, et, les réponses étant indépendantes, $V(N) = \frac{20}{3}$. On retrouve le résultat du chapitre 13 (exercice 16), où $N = \frac{4X - 20}{3}$ donnait $V(N) = \frac{16}{9} \times \frac{15}{4} = \frac{20}{3}$.

### Exercice 16 — Tirages sans remise <span class="etoiles">★★★</span>

Une urne contient $10$ boules dont $4$ rouges. On tire successivement $3$ boules **sans remise**, et $X$ est le nombre de boules rouges. On note $X_i$ la variable qui vaut $1$ si la $i$-ème boule tirée est rouge.

1. Montrer que $P(X_2 = 1) = \frac{4}{10}$. Admettre que de même, $P(X_3 = 1) = \frac{4}{10}$.
2. En déduire $E(X)$. La loi de $X$ est-elle binomiale ?
3. Vérifier $E(X)$ avec la loi de $X$.

??? success "Correction"
    **1.** Formule des probabilités totales : $P(X_2 = 1) = \frac{4}{10} \times \frac{3}{9} + \frac{6}{10} \times \frac{4}{9} = \frac{12 + 24}{90} = \frac{4}{10}$. *Plus généralement, chaque boule a la même chance d'occuper chaque rang.*

    **2.** $X = X_1 + X_2 + X_3$ et par linéarité, $E(X) = 3 \times \frac{4}{10} = 1{,}2$ : la même valeur que pour des tirages avec remise. Mais la loi n'est pas binomiale : les tirages ne sont pas indépendants.

    **3.** $P(X = k) = \dfrac{\binom{4}{k}\binom{6}{3-k}}{\binom{10}{3}}$, soit $\frac{20}{120}$, $\frac{60}{120}$, $\frac{36}{120}$, $\frac{4}{120}$ pour $k = 0, 1, 2, 3$. Alors $E(X) = \frac{60 + 72 + 12}{120} = 1{,}2$.

### Exercice 17 — Somme de deux binomiales <span class="etoiles">★</span>

$X \sim \mathcal{B}(10\,;\,0{,}3)$ et $Y \sim \mathcal{B}(20\,;\,0{,}3)$ sont indépendantes. Calculer $E(X + Y)$ et $V(X + Y)$, puis reconnaître la loi de $X + Y$.

??? success "Correction"
    $E(X + Y) = 3 + 6 = 9$ et $V(X + Y) = 2{,}1 + 4{,}2 = 6{,}3$. $X + Y \sim \mathcal{B}(30\,;\,0{,}3)$, et l'on vérifie bien $30 \times 0{,}3 = 9$ et $30 \times 0{,}3 \times 0{,}7 = 6{,}3$.

---

## Thème 4 — Échantillons, sommes et moyennes

*Méthode associée : [Méthode 5](methodes.md#methode-5-etudier-un-echantillon).*

### Exercice 18 — Paramètres d'un échantillon <span class="etoiles">★</span>

$X$ a pour espérance $10$ et pour écart type $2$. Pour un échantillon de taille $n$, donner $E(S_n)$, $\sigma(S_n)$, $E(M_n)$ et $\sigma(M_n)$, puis leurs valeurs pour $n = 100$.

??? success "Correction"
    $E(S_n) = 10n$, $\sigma(S_n) = 2\sqrt{n}$, $E(M_n) = 10$, $\sigma(M_n) = \frac{2}{\sqrt{n}}$. Pour $n = 100$ : $1\,000$, $20$, $10$ et $0{,}2$.

### Exercice 19 — Taille d'échantillon <span class="etoiles">★★</span>

Avec les données de l'exercice 18, quelle taille d'échantillon faut-il pour que $\sigma(M_n) \leq 0{,}1$ ?

??? success "Correction"
    $\frac{2}{\sqrt{n}} \leq 0{,}1 \iff \sqrt{n} \geq 20 \iff n \geq 400$.

### Exercice 20 — Un trajet en trois étapes <span class="etoiles">★★</span>

Un trajet comporte trois étapes de durées indépendantes, d'espérances $10$, $15$ et $20$ minutes et d'écarts types $2$, $3$ et $6$ minutes. Calculer l'espérance et l'écart type de la durée totale. Que penser de l'affirmation « l'écart type total est $2 + 3 + 6 = 11$ minutes » ?

??? success "Correction"
    $E(T) = 45$ min. $V(T) = 4 + 9 + 36 = 49$, donc $\sigma(T) = 7$ min. L'affirmation est fausse : ce sont les **variances** qui s'ajoutent, pas les écarts types. Les retards et les avances se compensent en partie.

### Exercice 21 — La moyenne de $n$ dés <span class="etoiles">★</span>

On lance $n$ dés et l'on fait la moyenne des résultats. Donner son espérance et son écart type, puis la valeur de l'écart type pour $n = 1$ et $n = 100$.

??? success "Correction"
    $E(M_n) = 3{,}5$ et $\sigma(M_n) = \dfrac{\sqrt{35/12}}{\sqrt{n}}$. Pour $n = 1$ : environ $1{,}71$ ; pour $n = 100$ : environ $0{,}17$.

### Exercice 22 — La fréquence de succès <span class="etoiles">★★</span>

Dans un schéma de Bernoulli de paramètres $n$ et $p$, on note $F_n = \frac{X}{n}$ la fréquence de succès.

1. Calculer $E(F_n)$ et $V(F_n)$.
2. Montrer que $V(F_n) \leq \dfrac{1}{4n}$, quel que soit $p$.

??? success "Correction"
    **1.** $F_n$ est la moyenne d'un échantillon de la loi de Bernoulli : $E(F_n) = p$ et $V(F_n) = \dfrac{p(1 - p)}{n}$.

    **2.** $p(1 - p) = \frac{1}{4} - \left(p - \frac{1}{2}\right)^2 \leq \frac{1}{4}$, d'où le résultat.

### Exercice 23 — Pourquoi le casino gagne <span class="etoiles">★★</span>

À la roulette, on mise $1$ € sur « rouge » : on gagne $1$ € avec probabilité $\frac{18}{37}$, et l'on perd sa mise sinon.

1. Calculer l'espérance et la variance du gain $G$ d'une partie.
2. Un joueur joue $1\,000$ parties indépendantes. Calculer l'espérance et l'écart type de son gain total. Commenter.

??? success "Correction"
    **1.** $E(G) = \frac{18}{37} - \frac{19}{37} = -\frac{1}{37} \approx -0{,}027$. $E(G^2) = 1$, donc $V(G) = 1 - \frac{1}{37^2} \approx 0{,}9993$.

    **2.** $E(S) = -\frac{1000}{37} \approx -27$ € et $\sigma(S) = \sqrt{1000 \times 0{,}9993} \approx 31{,}6$ €. Sur une soirée, le joueur peut gagner, l'aléa est du même ordre que l'espérance. Mais le casino joue des millions de parties : son gain moyen par partie a un écart type minuscule, et il gagne presque sûrement environ $2{,}7$ centimes par euro misé.

---

## Thème 5 — Approfondissement

### Exercice 24 — Le problème des chapeaux <span class="etoiles">★★★</span>

$n$ personnes déposent leur chapeau au vestiaire ; à la sortie, les chapeaux sont rendus au hasard (toutes les attributions sont équiprobables). Soit $X$ le nombre de personnes qui récupèrent leur propre chapeau. Calculer $E(X)$.

??? success "Correction"
    Soit $X_i$ la variable qui vaut $1$ si la personne $i$ récupère son chapeau. Il y a $n!$ attributions, dont $(n - 1)!$ donnent à la personne $i$ son chapeau : $P(X_i = 1) = \frac{1}{n}$. Par linéarité, $E(X) = n \times \frac{1}{n} = 1$, **quel que soit $n$**. Les $X_i$ ne sont pas indépendantes, mais la linéarité n'en a pas besoin.

### Exercice 25 — Le paradoxe des anniversaires <span class="etoiles">★★★</span>

Dans une classe de $30$ élèves, on suppose les dates d'anniversaire indépendantes et uniformes sur $365$ jours. Calculer l'espérance du nombre de **paires** d'élèves nés le même jour.

??? success "Correction"
    Il y a $\binom{30}{2} = 435$ paires. Pour chacune, la probabilité que les deux élèves soient nés le même jour est $\frac{1}{365}$. Avec une indicatrice par paire et la linéarité : $E = \frac{435}{365} \approx 1{,}19$. En moyenne, il y a plus d'une paire d'élèves partageant leur anniversaire, ce qui surprend souvent.

### Exercice 26 — Diversifier pour réduire le risque <span class="etoiles">★★★</span>

Deux placements indépendants ont des rendements $X$ et $Y$ de même espérance $m$, avec $V(X) = 1$ et $V(Y) = 4$. On place une proportion $t \in [0, 1]$ sur le premier et $1 - t$ sur le second ; le rendement est $R = tX + (1 - t)Y$.

1. Montrer que $E(R) = m$ et $V(R) = t^2 + 4(1 - t)^2$.
2. Déterminer $t$ pour que le risque $V(R)$ soit minimal. Comparer avec le placement le moins risqué seul.

??? success "Correction"
    **1.** Par linéarité, $E(R) = tm + (1 - t)m = m$. Par indépendance, $V(R) = t^2V(X) + (1 - t)^2V(Y) = t^2 + 4(1 - t)^2$.

    **2.** $V(R) = 5t^2 - 8t + 4$ est minimal pour $t = \frac{8}{10} = \frac{4}{5}$, où il vaut $\frac{16}{25} + \frac{4}{25} = \frac{4}{5}$. C'est **moins** que $V(X) = 1$ : mélanger les deux placements, même avec le plus risqué, réduit le risque. C'est le principe de la diversification.

### Exercice 27 — Simuler la somme de deux dés <span class="etoiles">★★</span>

Écrire un programme Python qui simule $10\,000$ lancers de deux dés et affiche la fréquence de chaque somme de $2$ à $12$. Comparer avec la loi du cours.

??? success "Correction"
    ```python
    from random import randint

    N = 10000
    effectifs = [0] * 13                 # indices 0 à 12
    for i in range(N):
        s = randint(1, 6) + randint(1, 6)
        effectifs[s] += 1
    for s in range(2, 13):
        print(s, effectifs[s] / N, round((6 - abs(s - 7)) / 36, 3))
    ```

    La formule $\frac{6 - |s - 7|}{36}$ résume le tableau du cours ; les fréquences en sont proches.

### Exercice 28 — L'écart type de la moyenne <span class="etoiles">★★</span>

Écrire un programme Python qui, pour $n = 1$, $4$, $16$ et $64$, simule $5\,000$ fois la moyenne de $n$ dés et calcule l'écart type des moyennes obtenues. Vérifier qu'il est divisé environ par $2$ quand $n$ est multiplié par $4$.

??? success "Correction"
    ```python
    from random import randint
    from math import sqrt

    def ecart_type(valeurs):
        m = sum(valeurs) / len(valeurs)
        return sqrt(sum((v - m)**2 for v in valeurs) / len(valeurs))

    for n in [1, 4, 16, 64]:
        moyennes = [sum(randint(1, 6) for i in range(n)) / n for k in range(5000)]
        print(n, ecart_type(moyennes))
    ```

    On obtient environ $1{,}71$ ; $0{,}85$ ; $0{,}43$ ; $0{,}21$, conformément à $\sigma(M_n) = \frac{1{,}71}{\sqrt{n}}$.
