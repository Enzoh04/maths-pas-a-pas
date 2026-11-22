# Exercices corrigés — Fonctions de référence

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf l'exercice Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Fonctions affines | 1 à 5 |
| 2. Fonction carré | 6 à 11 |
| 3. Fonction inverse | 12 à 16 |
| 4. Racine carrée, cube, valeur absolue | 17 à 22 |
| 5. Comparaisons et approfondissement | 23 à 28 |

---

## Thème 1 — Fonctions affines

### Exercice 1 — Reconnaître <span class="etoiles">★</span>

Parmi les fonctions suivantes, lesquelles sont affines ? Préciser $m$ et $p$. $f(x) = 3 - 2x$ ; $g(x) = \frac{x + 4}{5}$ ; $h(x) = x^2 + 1$ ; $k(x) = (x + 1)^2 - x^2$ ; $\ell(x) = \frac{2}{x}$.

??? success "Correction"
    $f$ : $m = -2$, $p = 3$. $g$ : $m = \frac{1}{5}$, $p = \frac{4}{5}$. $h$ : non. $k(x) = 2x + 1$ : affine, $m = 2$, $p = 1$. $\ell$ : non.

### Exercice 2 — Déterminer une fonction affine <span class="etoiles">★</span>

Déterminer la fonction affine $f$ telle que $f(1) = 5$ et $f(3) = -1$.

??? success "Correction"
    $m = \frac{-1 - 5}{3 - 1} = -3$ ; $5 = -3 + p$, $p = 8$. $f(x) = -3x + 8$.

### Exercice 3 — Variations et signe <span class="etoiles">★</span>

Donner les variations et dresser le tableau de signes de $f(x) = -\frac{1}{2}x + 3$.

??? success "Correction"
    $m = -\frac{1}{2} < 0$ : $f$ est décroissante sur $\mathbb{R}$. Elle s'annule en $x = 6$ : positive sur $]-\infty\,;\,6[$, négative sur $]6\,;\,+\infty[$.

### Exercice 4 — Proportionnalité <span class="etoiles">★★</span>

Un abonnement coûte $12$ € par mois plus $0{,}05$ € par SMS envoyé au-delà de $100$ SMS. Exprimer le coût mensuel $C(n)$ pour $n \geq 100$ SMS. Est-ce une fonction affine de $n$ ? Linéaire ?

??? success "Correction"
    $C(n) = 12 + 0{,}05(n - 100) = 0{,}05n + 7$. Affine, mais pas linéaire ($p = 7 \neq 0$).

### Exercice 5 — Fonction affine par morceaux <span class="etoiles">★★★</span>

On définit $f(x) = |x - 2| + |x + 1|$.

1. Écrire $f(x)$ sans valeur absolue sur chacun des intervalles $]-\infty\,;\,-1]$, $[-1\,;\,2]$ et $[2\,;\,+\infty[$.
2. Tracer la courbe de $f$ et déterminer son minimum.

??? success "Correction"
    1. Sur $]-\infty\,;\,-1]$ : $f(x) = -(x - 2) - (x + 1) = -2x + 1$. Sur $[-1\,;\,2]$ : $f(x) = -(x - 2) + (x + 1) = 3$. Sur $[2\,;\,+\infty[$ : $f(x) = 2x - 1$.
    2. La courbe est formée d'une demi-droite descendante, d'un palier à $3$, puis d'une demi-droite montante. Minimum $3$, atteint pour tout $x \in [-1\,;\,2]$ (la somme des distances de $x$ à $2$ et à $-1$ est minimale entre les deux).

---

## Thème 2 — Fonction carré

*Méthodes associées : [Méthode 1](methodes.md#methode-1-comparer-des-images-a-laide-des-variations), [Méthode 2](methodes.md#methode-2-encadrer-fx-a-partir-dun-encadrement-de-x) et [Méthode 3](methodes.md#methode-3-resoudre-x2-k-x2-k-x2-k).*

### Exercice 6 — Comparer des carrés <span class="etoiles">★</span>

Sans calculer, comparer : $1{,}3^2$ et $1{,}31^2$ ; $(-5)^2$ et $(-4{,}9)^2$ ; $(-2)^2$ et $3^2$.

??? success "Correction"
    $1{,}3^2 < 1{,}31^2$ (croissante sur $[0\,;\,+\infty[$) ; $(-5)^2 > (-4{,}9)^2$ (décroissante sur $]-\infty\,;\,0]$) ; les nombres ne sont pas dans un même intervalle de monotonie, mais $(-2)^2 = 2^2 < 3^2$ par parité.

### Exercice 7 — Encadrer un carré <span class="etoiles">★</span>

Encadrer $x^2$ dans chaque cas : $2 \leq x \leq 5$ ; $-4 \leq x \leq -1$ ; $-1 \leq x \leq 3$.

??? success "Correction"
    $4 \leq x^2 \leq 25$ ; $1 \leq x^2 \leq 16$ (décroissante : les bornes s'inversent) ; $0 \leq x^2 \leq 9$ (le minimum $0$ est atteint en $0$).

### Exercice 8 — Équations <span class="etoiles">★</span>

Résoudre : $x^2 = 36$ ; $x^2 = 7$ ; $3x^2 + 12 = 0$ ; $(x - 2)^2 = 16$.

??? success "Correction"
    $\{-6\,;\,6\}$ ; $\left\{-\sqrt{7}\,;\,\sqrt{7}\right\}$ ; $x^2 = -4$, $\varnothing$ ; $x - 2 = \pm 4$, $\{-2\,;\,6\}$.

### Exercice 9 — Inéquations <span class="etoiles">★★</span>

Résoudre : $x^2 < 25$ ; $x^2 \geq 3$ ; $x^2 > -1$ ; $4 - x^2 \geq 0$.

??? success "Correction"
    $]-5\,;\,5[$ ; $\left]-\infty\,;\,-\sqrt{3}\right] \cup \left[\sqrt{3}\,;\,+\infty\right[$ ; $\mathbb{R}$ ; $x^2 \leq 4$, $[-2\,;\,2]$.

### Exercice 10 — Variations par le calcul <span class="etoiles">★★</span>

Soit $g(x) = x^2 + 3$. Démontrer que $g$ est décroissante sur $]-\infty\,;\,0]$ et croissante sur $[0\,;\,+\infty[$.

??? success "Correction"
    $g(b) - g(a) = b^2 - a^2 = (b - a)(b + a)$, exactement comme pour la fonction carré : même conclusion. (La courbe de $g$ est celle de la fonction carré décalée de $3$ vers le haut.)

### Exercice 11 — Une parabole décalée <span class="etoiles">★★★</span>

Soit $h(x) = (x - 3)^2$.

1. Montrer que pour $a < b$, $h(b) - h(a) = (b - a)(a + b - 6)$.
2. En déduire les variations de $h$ et son minimum.
3. Comment obtient-on la courbe de $h$ à partir de celle de la fonction carré ?

??? success "Correction"
    1. $(b - 3)^2 - (a - 3)^2 = \big[(b - 3) - (a - 3)\big]\big[(b - 3) + (a - 3)\big] = (b - a)(a + b - 6)$.
    2. Si $a < b \leq 3$ : $a + b < 6$, $h$ décroissante sur $]-\infty\,;\,3]$. Si $3 \leq a < b$ : $a + b > 6$, $h$ croissante sur $[3\,;\,+\infty[$. Minimum $0$ en $3$.
    3. Par une translation de $3$ unités vers la droite.

---

## Thème 3 — Fonction inverse

*Méthode associée : [Méthode 4](methodes.md#methode-4-resoudre-frac1x-k-frac1x-k).*

### Exercice 12 — Comparer des inverses <span class="etoiles">★</span>

Comparer, sans calculatrice : $\frac{1}{0{,}7}$ et $\frac{1}{0{,}71}$ ; $\frac{1}{-3}$ et $\frac{1}{-2}$ ; $\frac{1}{-2}$ et $\frac{1}{5}$.

??? success "Correction"
    $\frac{1}{0{,}7} > \frac{1}{0{,}71}$ (décroissante sur $]0\,;\,+\infty[$) ; $-3 < -2 < 0$, donc $\frac{1}{-3} > \frac{1}{-2}$ ; un négatif est inférieur à un positif : $\frac{1}{-2} < \frac{1}{5}$.

### Exercice 13 — Encadrer un inverse <span class="etoiles">★</span>

Encadrer $\frac{1}{x}$ si $4 \leq x \leq 10$, puis si $-2 \leq x \leq -\frac{1}{2}$.

??? success "Correction"
    $\frac{1}{10} \leq \frac{1}{x} \leq \frac{1}{4}$ ; $-2 \leq \frac{1}{x} \leq -\frac{1}{2}$.

### Exercice 14 — Équations <span class="etoiles">★</span>

Résoudre $\frac{1}{x} = 4$, $\frac{1}{x} = -\frac{2}{3}$ et $\frac{1}{x} = 0$.

??? success "Correction"
    $x = \frac{1}{4}$ ; $x = -\frac{3}{2}$ ; aucune solution (l'inverse d'un réel n'est jamais nul).

### Exercice 15 — Inéquations <span class="etoiles">★★</span>

Résoudre : $\frac{1}{x} \geq 3$ ; $\frac{1}{x} > -1$.

??? success "Correction"
    - Si $x < 0$, $\frac{1}{x} < 0 < 3$ : pas de solution. Si $x > 0$ : $\frac{1}{x} \geq \frac{1}{1/3} \iff x \leq \frac{1}{3}$. $S = \left]0\,;\,\frac{1}{3}\right]$.
    - Si $x > 0$ : toujours vrai. Si $x < 0$ : $\frac{1}{x} > \frac{1}{-1} \iff x < -1$ (décroissante sur $]-\infty\,;\,0[$). $S = ]-\infty\,;\,-1[ \cup ]0\,;\,+\infty[$.

### Exercice 16 — Une fonction homographique <span class="etoiles">★★★</span>

Soit $f(x) = \frac{2}{x - 1}$ sur $]1\,;\,+\infty[$.

1. Pour $1 < a < b$, montrer que $f(b) - f(a) = \dfrac{2(a - b)}{(a - 1)(b - 1)}$.
2. En déduire le sens de variation de $f$ sur $]1\,;\,+\infty[$.
3. Résoudre $f(x) \leq 1$ sur cet intervalle.

??? success "Correction"
    1. $\frac{2}{b - 1} - \frac{2}{a - 1} = \frac{2(a - 1) - 2(b - 1)}{(a - 1)(b - 1)} = \frac{2(a - b)}{(a - 1)(b - 1)}$.
    2. $a - b < 0$ et $(a - 1)(b - 1) > 0$ : $f$ est strictement décroissante.
    3. $f(3) = 1$ et $f$ est décroissante : $f(x) \leq 1 \iff x \geq 3$. $S = [3\,;\,+\infty[$.

---

## Thème 4 — Racine carrée, cube, valeur absolue

### Exercice 17 — Racine carrée <span class="etoiles">★</span>

Résoudre $\sqrt{x} = 5$, $\sqrt{x} = -1$, $\sqrt{x} \leq 3$ et $\sqrt{x} > 1{,}5$.

??? success "Correction"
    $x = 25$ ; pas de solution ; $[0\,;\,9]$ ; $]2{,}25\,;\,+\infty[$.

### Exercice 18 — Cube <span class="etoiles">★</span>

Résoudre $x^3 = 64$, $x^3 = -1$, $x^3 < 8$ et $x^3 \geq -27$.

??? success "Correction"
    $x = 4$ ; $x = -1$ ; la fonction cube étant croissante, $x^3 < 2^3 \iff x < 2$ ; $x^3 \geq (-3)^3 \iff x \geq -3$.

### Exercice 19 — Valeur absolue <span class="etoiles">★</span>

Résoudre $|x| = 3$, $|x| \leq 2$, $|x| > 5$ et $|x - 1| = 4$.

??? success "Correction"
    $\{-3\,;\,3\}$ ; $[-2\,;\,2]$ ; $]-\infty\,;\,-5[ \cup ]5\,;\,+\infty[$ ; $\{-3\,;\,5\}$.

### Exercice 20 — Encadrements <span class="etoiles">★★</span>

On sait que $-2 \leq x \leq 3$. Encadrer $x^3$, $|x|$ et $\sqrt{x + 2}$.

??? success "Correction"
    Cube croissante : $-8 \leq x^3 \leq 27$. Valeur absolue : minimum $0$ en $0$, maximum $3$ en $3$, donc $0 \leq |x| \leq 3$. $0 \leq x + 2 \leq 5$, donc $0 \leq \sqrt{x + 2} \leq \sqrt{5}$.

### Exercice 21 — Parité <span class="etoiles">★★</span>

Quelles fonctions de référence sont paires ? impaires ? Justifier, puis donner une fonction qui n'est ni paire ni impaire.

??? success "Correction"
    Paires : carré ($(-x)^2 = x^2$), valeur absolue ($|-x| = |x|$). Impaires : inverse ($\frac{1}{-x} = -\frac{1}{x}$), cube ($(-x)^3 = -x^3$), linéaires $x \mapsto mx$. La racine carrée n'est ni paire ni impaire (son ensemble de définition $[0\,;\,+\infty[$ n'est pas symétrique) ; $x \mapsto x + 1$ non plus.

### Exercice 22 — Croissance de la racine <span class="etoiles">★★★</span>

1. Démontrer que pour $0 \leq a < b$, $\sqrt{b} - \sqrt{a} = \dfrac{b - a}{\sqrt{b} + \sqrt{a}}$.
2. En déduire que la fonction racine carrée est croissante, puis que $\sqrt{b} - \sqrt{a} \leq \dfrac{b - a}{2}$ lorsque $1 \leq a < b$.

??? success "Correction"
    1. On multiplie et on divise par $\sqrt{b} + \sqrt{a} > 0$, et $\left(\sqrt{b} - \sqrt{a}\right)\left(\sqrt{b} + \sqrt{a}\right) = b - a$.
    2. Le quotient est positif : croissante. Si $1 \leq a < b$, $\sqrt{a} \geq 1$ et $\sqrt{b} > 1$, donc $\sqrt{b} + \sqrt{a} > 2$, et $\sqrt{b} - \sqrt{a} < \frac{b - a}{2}$.

---

## Thème 5 — Comparaisons et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-demontrer-un-sens-de-variation).*

### Exercice 23 — Ranger <span class="etoiles">★</span>

Ranger dans l'ordre croissant : $0{,}6$ ; $0{,}6^2$ ; $0{,}6^3$ ; $\sqrt{0{,}6}$. Puis : $1{,}5$ ; $1{,}5^2$ ; $1{,}5^3$ ; $\sqrt{1{,}5}$.

??? success "Correction"
    $0{,}6^3 < 0{,}6^2 < 0{,}6 < \sqrt{0{,}6}$ ; $\sqrt{1{,}5} < 1{,}5 < 1{,}5^2 < 1{,}5^3$.

### Exercice 24 — Intersections de courbes <span class="etoiles">★★</span>

Déterminer les points d'intersection des courbes des fonctions carré et inverse, puis des fonctions carré et cube.

??? success "Correction"
    $x^2 = \frac{1}{x}$ (avec $x \neq 0$) $\iff x^3 = 1 \iff x = 1$ : point $(1\,;\,1)$.

    $x^2 = x^3 \iff x^2(x - 1) = 0 \iff x = 0$ ou $x = 1$ : points $(0\,;\,0)$ et $(1\,;\,1)$.

### Exercice 25 — Courbe et droite <span class="etoiles">★★</span>

Résoudre graphiquement puis par le calcul $x^2 \leq x + 2$.

??? success "Correction"
    Les courbes se coupent en $x = -1$ et $x = 2$ ; la parabole est sous la droite entre ces valeurs. Par le calcul : $x^2 - x - 2 = (x - 2)(x + 1) \leq 0 \iff x \in [-1\,;\,2]$.

### Exercice 26 — Inverse et droite <span class="etoiles">★★★</span>

Résoudre $\frac{1}{x} \leq x$ en étudiant le signe de $\frac{1}{x} - x$.

??? success "Correction"
    $\frac{1}{x} - x = \frac{(1 - x)(1 + x)}{x}$. Tableau de signes (zéros $-1$, $1$, valeur interdite $0$) : le quotient est négatif ou nul sur $[-1\,;\,0[ \cup [1\,;\,+\infty[$. $S = [-1\,;\,0[ \cup [1\,;\,+\infty[$.

### Exercice 27 — Courbes en Python <span class="etoiles">★★★</span>

Écrire un programme qui affiche, pour $x$ allant de $0$ à $2$ avec un pas de $0{,}25$, les valeurs de $x$, $x^2$, $x^3$ et $\sqrt{x}$. Vérifier sur l'affichage la propriété des positions relatives.

??? success "Correction"
    ```python
    from math import sqrt

    for k in range(9):
        x = 0.25 * k
        print(x, x**2, x**3, round(sqrt(x), 3))
    ```

    Pour $x < 1$, la colonne $x^3$ est la plus petite et $\sqrt{x}$ la plus grande ; pour $x > 1$, c'est l'inverse ; pour $x = 1$, tout vaut $1$.

### Exercice 28 — Optimisation <span class="etoiles">★★★</span>

Un rectangle a une aire de $16$ cm². On note $x$ sa largeur, en cm.

1. Exprimer son périmètre $P(x)$ en fonction de $x$.
2. Montrer que $P(x) - 16 = \dfrac{2(x - 4)^2}{x}$.
3. En déduire le rectangle d'aire $16$ cm² de périmètre minimal.

??? success "Correction"
    1. Longueur $\frac{16}{x}$ : $P(x) = 2x + \frac{32}{x}$.
    2. $2x + \frac{32}{x} - 16 = \frac{2x^2 - 16x + 32}{x} = \frac{2(x^2 - 8x + 16)}{x} = \frac{2(x - 4)^2}{x}$.
    3. Pour $x > 0$, ce quotient est positif, nul seulement en $x = 4$ : $P(x) \geq 16 = P(4)$. Le périmètre minimal est $16$ cm, pour le **carré** de côté $4$ cm.
