# Cours — Sommes de variables aléatoires

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.

Dans tout le chapitre, $\Omega$ est un univers **fini** muni d'une probabilité $P$. Une variable aléatoire $X$ associe un réel $X(\omega)$ à chaque issue $\omega$. On note $x_1, \ldots, x_r$ ses valeurs.

---

## 1. Rappels et un nouveau point de vue sur l'espérance

!!! definition "Espérance, variance, écart type (Première)"
    $$E(X) = \sum_{i=1}^{r} x_i\,P(X = x_i), \qquad V(X) = \sum_{i=1}^{r} P(X = x_i)\,\big(x_i - E(X)\big)^2, \qquad \sigma(X) = \sqrt{V(X)}.$$

!!! propriete "L'espérance comme somme sur les issues"
    $$E(X) = \sum_{\omega \in \Omega} X(\omega)\,P(\{\omega\}).$$
    Plus généralement, pour toute fonction $f$, $E\big(f(X)\big) = \sum_{\omega \in \Omega} f\big(X(\omega)\big)P(\{\omega\}) = \sum_{i=1}^{r} f(x_i)\,P(X = x_i)$.

??? demoplus "Démonstration — pour aller plus loin"
    On regroupe les issues selon la valeur prise par $X$. Les issues $\omega$ telles que $X(\omega) = x_i$ forment l'événement $\{X = x_i\}$, et la somme de leurs probabilités est $P(X = x_i)$. Donc
    $$\sum_{\omega \in \Omega} X(\omega)P(\{\omega\}) = \sum_{i=1}^{r}\ \sum_{\omega : X(\omega) = x_i} x_i\,P(\{\omega\}) = \sum_{i=1}^{r} x_i\,P(X = x_i) = E(X).$$
    Le même regroupement donne la formule avec $f$.

Ce point de vue est la clé de tout le chapitre : il permet d'additionner des variables issue par issue.

!!! propriete "Transformation affine et formule de König-Huygens"
    Pour tous réels $a$ et $b$ :
    $$E(aX + b) = aE(X) + b, \qquad V(aX + b) = a^2V(X), \qquad V(X) = E(X^2) - E(X)^2.$$

??? demoplus "Démonstration — pour aller plus loin"
    Avec la somme sur les issues, et $\sum_\omega P(\{\omega\}) = 1$ :
    $$E(aX + b) = \sum_\omega \big(aX(\omega) + b\big)P(\{\omega\}) = a\sum_\omega X(\omega)P(\{\omega\}) + b = aE(X) + b.$$
    Puis $(aX + b) - E(aX + b) = a\big(X - E(X)\big)$, donc $V(aX + b) = E\big(a^2(X - E(X))^2\big) = a^2V(X)$. La formule de König-Huygens a été démontrée au chapitre 13, § 4.

---

## 2. Somme de deux variables et linéarité de l'espérance

### 2.1 La variable $X + Y$

!!! definition "Somme de variables aléatoires"
    Si $X$ et $Y$ sont deux variables aléatoires sur $\Omega$, la variable $X + Y$ associe à chaque issue $\omega$ le réel $X(\omega) + Y(\omega)$. De même, $aX$ associe $aX(\omega)$.

Pour obtenir la **loi** de $X + Y$, il faut connaître les probabilités $P\big(\{X = x\} \cap \{Y = y\}\big)$ (la **loi du couple**), puis additionner celles qui correspondent à une même somme :
$$P(X + Y = s) = \sum_{x + y = s} P\big(\{X = x\} \cap \{Y = y\}\big).$$

**Exemple.** On lance deux dés équilibrés ; $X$ et $Y$ sont les deux résultats et $S = X + Y$. Les $36$ couples sont équiprobables. En comptant dans un tableau à double entrée :

| $s$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $36 \times P(S = s)$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ |

### 2.2 Linéarité de l'espérance

!!! theoreme "Linéarité de l'espérance"
    Pour toutes variables aléatoires $X$ et $Y$ et tout réel $a$ :
    $$E(X + Y) = E(X) + E(Y), \qquad E(aX) = aE(X).$$
    Par récurrence, $E(X_1 + X_2 + \cdots + X_n) = E(X_1) + E(X_2) + \cdots + E(X_n)$.

??? demoplus "Démonstration — pour aller plus loin"
    Avec l'espérance comme somme sur les issues :
    $$E(X + Y) = \sum_\omega \big(X(\omega) + Y(\omega)\big)P(\{\omega\}) = \sum_\omega X(\omega)P(\{\omega\}) + \sum_\omega Y(\omega)P(\{\omega\}) = E(X) + E(Y).$$
    Le cas de $aX$ est le § 1 avec $b = 0$. Pour $n$ variables, on applique le résultat à $(X_1 + \cdots + X_{n-1}) + X_n$.

!!! warning "Aucune hypothèse d'indépendance"
    La linéarité de l'espérance est **toujours** vraie, même si $X$ et $Y$ sont liées. C'est ce qui la rend si puissante : on peut calculer $E(X + Y)$ sans connaître la loi de $X + Y$.

**Exemple.** Pour les deux dés : $E(S) = E(X) + E(Y) = 3{,}5 + 3{,}5 = 7$, sans utiliser le tableau.

!!! warning "Le produit, lui, n'est pas linéaire"
    En général, $E(XY) \neq E(X)E(Y)$. Si $X$ suit la loi de Bernoulli de paramètre $\frac{1}{2}$ et $Y = X$, alors $XY = X^2 = X$, donc $E(XY) = \frac{1}{2}$, alors que $E(X)E(Y) = \frac{1}{4}$.

---

## 3. Variables indépendantes et variance d'une somme

### 3.1 Indépendance

!!! definition "Variables aléatoires indépendantes"
    Deux variables $X$ et $Y$ sont **indépendantes** lorsque, pour toute valeur $x$ de $X$ et toute valeur $y$ de $Y$,
    $$P\big(\{X = x\} \cap \{Y = y\}\big) = P(X = x) \times P(Y = y).$$

!!! propriete "Le cas des épreuves indépendantes"
    Dans une succession de deux épreuves indépendantes, si $X$ ne dépend que du résultat de la première épreuve et $Y$ que du résultat de la seconde, alors $X$ et $Y$ sont indépendantes.

??? demoplus "Démonstration — pour aller plus loin"
    Avec $\Omega = \Omega_1 \times \Omega_2$, l'événement $\{X = x\}$ s'écrit $A \times \Omega_2$ et $\{Y = y\}$ s'écrit $\Omega_1 \times B$. Leur intersection est $A \times B$. D'après le chapitre 13, § 1.1 :
    $$P(A \times B) = P_1(A)P_2(B) = P(A \times \Omega_2) \times P(\Omega_1 \times B) = P(X = x) \times P(Y = y).$$

C'est la situation la plus fréquente : deux dés, deux tirages avec remise, deux jeux joués séparément… Pour des variables indépendantes, la loi de $X + Y$ se calcule avec des **produits** :
$$P(X + Y = s) = \sum_{x + y = s} P(X = x)\,P(Y = y).$$

### 3.2 Variance d'une somme

!!! propriete "Espérance d'un produit"
    Si $X$ et $Y$ sont indépendantes, alors $E(XY) = E(X)\,E(Y)$.

??? demoplus "Démonstration — pour aller plus loin"
    On regroupe les issues selon le couple de valeurs $(X(\omega), Y(\omega))$, comme au § 1 :
    $$E(XY) = \sum_\omega X(\omega)Y(\omega)P(\{\omega\}) = \sum_{x}\sum_{y} xy\,P\big(\{X = x\} \cap \{Y = y\}\big).$$
    Par indépendance, chaque terme vaut $xy\,P(X = x)P(Y = y)$, et la double somme se factorise :
    $$E(XY) = \Big(\sum_x x\,P(X = x)\Big)\Big(\sum_y y\,P(Y = y)\Big) = E(X)\,E(Y).$$

!!! theoreme "Variance d'une somme de variables indépendantes"
    Si $X$ et $Y$ sont **indépendantes** :
    $$V(X + Y) = V(X) + V(Y).$$

??? demoplus "Démonstration — pour aller plus loin"
    Avec la formule de König-Huygens et la linéarité de l'espérance :
    $$\begin{aligned} V(X + Y) &= E\big((X + Y)^2\big) - \big(E(X) + E(Y)\big)^2 \\ &= E(X^2) + 2E(XY) + E(Y^2) - E(X)^2 - 2E(X)E(Y) - E(Y)^2, \end{aligned}$$
    soit $V(X + Y) = V(X) + V(Y) + 2\big(E(XY) - E(X)E(Y)\big)$. Le dernier terme est nul par indépendance.

!!! warning "Trois erreurs à éviter"
    - **Sans indépendance, c'est faux.** Avec $Y = X$ : $V(2X) = 4V(X)$, et non $2V(X)$.
    - **La variance d'une différence s'ajoute aussi** : $V(X - Y) = V(X) + V(-Y) = V(X) + (-1)^2V(Y) = V(X) + V(Y)$.
    - **Les écarts types ne s'ajoutent pas** : $\sigma(X + Y) = \sqrt{\sigma(X)^2 + \sigma(Y)^2}$.

**Exemple.** Un dé équilibré a pour variance $V(X) = \dfrac{1 + 4 + 9 + 16 + 25 + 36}{6} - 3{,}5^2 = \dfrac{91}{6} - \dfrac{49}{4} = \dfrac{35}{12}$. La somme de deux dés indépendants a donc pour variance $\dfrac{35}{6}$.

### 3.3 Plus de deux variables

!!! definition "Variables mutuellement indépendantes"
    Les variables $X_1, \ldots, X_n$ sont **(mutuellement) indépendantes** lorsque, pour toutes valeurs $x_1, \ldots, x_n$,
    $$P\big(\{X_1 = x_1\} \cap \cdots \cap \{X_n = x_n\}\big) = P(X_1 = x_1) \times \cdots \times P(X_n = x_n).$$
    C'est le cas, comme au § 3.1, quand chaque $X_i$ ne dépend que de la $i$-ème épreuve d'une succession d'épreuves indépendantes.

!!! theoreme "Variance d'une somme de $n$ variables indépendantes"
    Si $X_1, \ldots, X_n$ sont indépendantes :
    $$V(X_1 + \cdots + X_n) = V(X_1) + \cdots + V(X_n).$$

??? demoplus "Démonstration — pour aller plus loin"
    On raisonne par récurrence. Posons $T = X_1 + \cdots + X_{n-1}$ ; il suffit de montrer que $T$ et $X_n$ sont indépendantes, puis d'appliquer le § 3.2.

    D'abord, en sommant l'égalité de définition sur toutes les valeurs $x_n$ de $X_n$, on obtient $P\big(\{X_1 = x_1\} \cap \cdots \cap \{X_{n-1} = x_{n-1}\}\big) = P(X_1 = x_1) \times \cdots \times P(X_{n-1} = x_{n-1})$.

    Ensuite, l'événement $\{T = t\} \cap \{X_n = x\}$ est la réunion disjointe des événements $\{X_1 = x_1\} \cap \cdots \cap \{X_{n-1} = x_{n-1}\} \cap \{X_n = x\}$ pour les listes $(x_1, \ldots, x_{n-1})$ de somme $t$. En sommant leurs probabilités et en factorisant par $P(X_n = x)$, on trouve $P(\{T = t\} \cap \{X_n = x\}) = P(T = t)\,P(X_n = x)$.

---

## 4. Retour sur la loi binomiale

!!! propriete "Une variable binomiale est une somme de variables de Bernoulli"
    Dans un schéma de Bernoulli de paramètres $n$ et $p$, notons $X_i$ la variable qui vaut $1$ si la $i$-ème épreuve est un succès et $0$ sinon. Alors :

    - chaque $X_i$ suit la loi de Bernoulli de paramètre $p$ ;
    - $X_1, \ldots, X_n$ sont indépendantes (chacune ne dépend que d'une épreuve) ;
    - le nombre de succès est $X = X_1 + X_2 + \cdots + X_n$, qui suit la loi $\mathcal{B}(n, p)$.

!!! theoreme "Espérance et variance de la loi binomiale"
    Si $X \sim \mathcal{B}(n, p)$, alors $E(X) = np$ et $V(X) = np(1 - p)$.

??? demo "Démonstration — au programme du bac"
    On écrit $X = X_1 + \cdots + X_n$, où les $X_i$ sont des variables de Bernoulli de paramètre $p$, indépendantes. D'après le chapitre 13, $E(X_i) = p$ et $V(X_i) = p(1 - p)$.

    **Espérance.** Par linéarité de l'espérance :
    $$E(X) = E(X_1) + \cdots + E(X_n) = p + \cdots + p = np.$$

    **Variance.** Les $X_i$ étant indépendantes, les variances s'ajoutent :
    $$V(X) = V(X_1) + \cdots + V(X_n) = np(1 - p).$$

*Compare avec la démonstration directe du chapitre 13 : écrire la variable comme une somme simplifie considérablement les calculs.*

!!! propriete "Somme de deux binomiales"
    Si $X \sim \mathcal{B}(n, p)$ et $Y \sim \mathcal{B}(m, p)$ sont indépendantes (même $p$), alors $X + Y \sim \mathcal{B}(n + m, p)$ : on enchaîne deux schémas de Bernoulli indépendants de même paramètre, ce qui en fait un seul de $n + m$ épreuves.

---

## 5. Échantillons : somme et moyenne

!!! definition "Échantillon"
    Un **échantillon de taille $n$** de la loi d'une variable $X$ est une liste $(X_1, \ldots, X_n)$ de variables **indépendantes** qui ont toutes **la même loi** que $X$. On lui associe :

    - la **somme** $S_n = X_1 + X_2 + \cdots + X_n$ ;
    - la **moyenne** $M_n = \dfrac{S_n}{n}$.

**Exemple.** On lance $n$ fois un dé : les résultats forment un échantillon de taille $n$ de la loi uniforme sur $\{1, \ldots, 6\}$. Le nombre de succès d'un schéma de Bernoulli est la somme d'un échantillon de la loi de Bernoulli.

!!! theoreme "Somme et moyenne d'un échantillon"
    $$E(S_n) = nE(X), \qquad V(S_n) = nV(X), \qquad \sigma(S_n) = \sqrt{n}\,\sigma(X),$$

    $$E(M_n) = E(X), \qquad V(M_n) = \frac{V(X)}{n}, \qquad \sigma(M_n) = \frac{\sigma(X)}{\sqrt{n}}.$$

??? demoplus "Démonstration — pour aller plus loin"
    Par linéarité, $E(S_n) = nE(X)$. Par indépendance, $V(S_n) = nV(X)$, d'où $\sigma(S_n) = \sqrt{n}\,\sigma(X)$. Puis, avec $a = \frac{1}{n}$ : $E(M_n) = \frac{1}{n}E(S_n) = E(X)$ et $V(M_n) = \frac{1}{n^2}V(S_n) = \frac{V(X)}{n}$.

!!! tip "Pourquoi on fait des moyennes"
    La moyenne $M_n$ a la même espérance que $X$, mais un écart type **divisé par $\sqrt{n}$** : elle fluctue de moins en moins autour de $E(X)$ quand $n$ grandit. Pour diviser l'écart type par $10$, il faut un échantillon $100$ fois plus grand. C'est le point de départ de la loi des grands nombres (chapitre 15).

---

## 6. Pour aller plus loin

- **Covariance.** La quantité $\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y)$ apparaît dans la démonstration du § 3.2 : $V(X + Y) = V(X) + V(Y) + 2\operatorname{Cov}(X, Y)$. Deux variables indépendantes ont une covariance nulle, mais **la réciproque est fausse** : si $X$ prend les valeurs $-1$, $0$, $1$ avec probabilité $\frac{1}{3}$ et $Y = X^2$, alors $\operatorname{Cov}(X, Y) = E(X^3) - 0 = 0$, alors que $Y$ dépend entièrement de $X$.
- **Variables continues.** Tout ce chapitre s'étend aux variables qui prennent une infinité de valeurs (durées, tailles…), avec des intégrales à la place des sommes (L2).
- **Théorème central limite.** Pour $n$ grand, la loi de $S_n$ ressemble à une courbe en cloche (loi normale), quelle que soit la loi de $X$. C'est l'un des résultats les plus importants des probabilités (L3).

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les exercices corrigés.
