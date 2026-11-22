# Exercices corrigés — Équations, fonctions polynômes du second degré

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Les trois formes d'un trinôme | 1 à 6 |
| 2. Variations, sommet, optimisation | 7 à 11 |
| 3. Équations du second degré | 12 à 18 |
| 4. Signe et inéquations | 19 à 24 |
| 5. Problèmes et approfondissement | 25 à 28 |

---

## Thème 1 — Les trois formes d'un trinôme

*Méthode associée : [Méthode 1](methodes.md#methode-1-mettre-un-trinome-sous-forme-canonique).*

### Exercice 1 — Reconnaître <span class="etoiles">★</span>

Parmi les fonctions suivantes, lesquelles sont des fonctions polynômes du second degré ? Préciser alors $a$, $b$ et $c$.

$f_1(x) = 3x^2 - x$ ; $f_2(x) = (x + 1)^2 - x^2$ ; $f_3(x) = (2x - 1)(x + 3)$ ; $f_4(x) = 5 - x^2$ ; $f_5(x) = \dfrac{1}{x^2}$.

??? success "Correction"
    - $f_1$ : oui, $a = 3$, $b = -1$, $c = 0$.
    - $f_2(x) = 2x + 1$ : non, c'est une fonction affine.
    - $f_3(x) = 2x^2 + 5x - 3$ : oui, $a = 2$, $b = 5$, $c = -3$.
    - $f_4$ : oui, $a = -1$, $b = 0$, $c = 5$.
    - $f_5$ : non (ce n'est pas un polynôme).

### Exercice 2 — Développer <span class="etoiles">★</span>

Écrire sous forme développée : $f(x) = 2(x - 3)^2 + 1$ et $g(x) = -(x + 2)(x - 4)$.

??? success "Correction"
    $f(x) = 2(x^2 - 6x + 9) + 1 = 2x^2 - 12x + 19$. $g(x) = -(x^2 - 2x - 8) = -x^2 + 2x + 8$.

### Exercice 3 — Forme canonique ($a = 1$) <span class="etoiles">★</span>

Mettre sous forme canonique $x^2 - 6x + 5$ et $x^2 + 3x + 1$.

??? success "Correction"
    $x^2 - 6x + 5 = (x - 3)^2 - 9 + 5 = (x - 3)^2 - 4$.

    $x^2 + 3x + 1 = \left(x + \frac{3}{2}\right)^2 - \frac{9}{4} + 1 = \left(x + \frac{3}{2}\right)^2 - \frac{5}{4}$.

### Exercice 4 — Forme canonique ($a \neq 1$) <span class="etoiles">★★</span>

Mettre sous forme canonique $2x^2 + 8x + 3$ et $-3x^2 + 6x + 1$.

??? success "Correction"
    $2x^2 + 8x + 3 = 2\left[(x + 2)^2 - 4\right] + 3 = 2(x + 2)^2 - 5$.

    $-3x^2 + 6x + 1 = -3(x^2 - 2x) + 1 = -3\left[(x - 1)^2 - 1\right] + 1 = -3(x - 1)^2 + 4$.

### Exercice 5 — Retrouver un trinôme <span class="etoiles">★★</span>

Une parabole a pour sommet $S(1\,;\,-2)$ et passe par le point $A(3\,;\,6)$. Déterminer la fonction polynôme du second degré correspondante, sous forme canonique puis développée.

??? success "Correction"
    $f(x) = a(x - 1)^2 - 2$. Avec $A$ : $4a - 2 = 6$, donc $a = 2$. $f(x) = 2(x - 1)^2 - 2 = 2x^2 - 4x$.

### Exercice 6 — Trois écritures <span class="etoiles">★★</span>

Montrer que, pour tout réel $x$ :
$$2x^2 - 4x - 6 = 2(x - 1)^2 - 8 = 2(x + 1)(x - 3).$$
Utiliser la forme la plus adaptée pour : calculer $f(0)$ ; résoudre $f(x) = 0$ ; trouver le minimum de $f$ ; résoudre $f(x) = -6$.

??? success "Correction"
    En développant : $2(x^2 - 2x + 1) - 8 = 2x^2 - 4x - 6$ et $2(x^2 - 2x - 3) = 2x^2 - 4x - 6$.

    - $f(0) = -6$ (forme développée).
    - $f(x) = 0 \iff x = -1$ ou $x = 3$ (forme factorisée).
    - Minimum $-8$, atteint en $1$ (forme canonique, $a > 0$).
    - $f(x) = -6 \iff 2x^2 - 4x = 0 \iff 2x(x - 2) = 0 \iff x = 0$ ou $x = 2$ (forme développée).

---

## Thème 2 — Variations, sommet, optimisation

*Méthode associée : [Méthode 2](methodes.md#methode-2-trouver-un-extremum-resoudre-un-probleme-doptimisation).*

### Exercice 7 — Un maximum <span class="etoiles">★</span>

Dresser le tableau de variations de $f(x) = -x^2 + 4x + 1$ et préciser son extremum.

??? success "Correction"
    $\alpha = 2$, $\beta = f(2) = 5$, $a = -1 < 0$ : $f$ est croissante sur $]-\infty\,;\,2]$, décroissante sur $[2\,;\,+\infty[$. Son maximum vaut $5$, atteint en $2$.

### Exercice 8 — Un minimum <span class="etoiles">★</span>

Dresser le tableau de variations de $g(x) = 3x^2 - 12x + 7$.

??? success "Correction"
    $\alpha = \frac{12}{6} = 2$, $g(2) = 12 - 24 + 7 = -5$, $a = 3 > 0$ : $g$ est décroissante sur $]-\infty\,;\,2]$, croissante sur $[2\,;\,+\infty[$, de minimum $-5$.

### Exercice 9 — Lire une parabole <span class="etoiles">★★</span>

La courbe d'une fonction $f(x) = ax^2 + bx + c$ est une parabole tournée vers le bas, de sommet $S(-1\,;\,3)$, qui coupe l'axe des ordonnées au point d'ordonnée $1$.

1. Donner le signe de $a$. Écrire $f$ sous forme canonique en fonction de $a$.
2. Déterminer $a$, puis la forme développée.
3. Combien l'équation $f(x) = 0$ a-t-elle de solutions ? (sans calcul)

??? success "Correction"
    **1.** Tournée vers le bas : $a < 0$. $f(x) = a(x + 1)^2 + 3$.

    **2.** $f(0) = a + 3 = 1$, donc $a = -2$ et $f(x) = -2(x + 1)^2 + 3 = -2x^2 - 4x + 1$.

    **3.** Le maximum vaut $3 > 0$ et la parabole descend vers $-\infty$ de part et d'autre : elle coupe l'axe des abscisses en **deux** points.

### Exercice 10 — Hauteur maximale <span class="etoiles">★</span>

Un ballon est lancé verticalement. Sa hauteur (en mètres) après $t$ secondes est $h(t) = -5t^2 + 20t + 1{,}5$. Quelle hauteur maximale atteint-il, et à quel instant ?

??? success "Correction"
    $\alpha = \frac{-20}{-10} = 2$ et $h(2) = -20 + 40 + 1{,}5 = 21{,}5$. Hauteur maximale $21{,}5$ m, atteinte au bout de $2$ s.

### Exercice 11 — Bénéfice maximal <span class="etoiles">★★</span>

Une entreprise fabrique $x$ objets par jour, avec $0 \leq x \leq 60$. Son bénéfice (en euros) est $B(x) = -2x^2 + 120x - 1\,000$.

1. Pour quelle production le bénéfice est-il maximal ? Que vaut-il ?
2. Pour quelles productions l'entreprise est-elle rentable ($B(x) \geq 0$) ?

??? success "Correction"
    **1.** $\alpha = \frac{-120}{-4} = 30$ et $B(30) = -1\,800 + 3\,600 - 1\,000 = 800$ €.

    **2.** $B(x) = -2(x^2 - 60x + 500)$. $\Delta = 3\,600 - 2\,000 = 1\,600$, racines $\frac{60 - 40}{2} = 10$ et $\frac{60 + 40}{2} = 50$. Comme $a < 0$, $B(x) \geq 0$ entre les racines : la production doit être comprise entre $10$ et $50$ objets.

---

## Thème 3 — Équations du second degré

*Méthodes associées : [Méthode 3](methodes.md#methode-3-resoudre-une-equation-du-second-degre) et [Méthode 4](methodes.md#methode-4-factoriser-un-trinome).*

### Exercice 12 — Avec le discriminant <span class="etoiles">★</span>

Résoudre : $x^2 - 5x + 6 = 0$ ; $2x^2 + x - 1 = 0$ ; $x^2 + x + 1 = 0$ ; $9x^2 - 6x + 1 = 0$.

??? success "Correction"
    - $\Delta = 1$ : $S = \{2\,;\,3\}$.
    - $\Delta = 9$ : $S = \left\{-1\,;\,\frac{1}{2}\right\}$.
    - $\Delta = -3 < 0$ : $S = \varnothing$.
    - $\Delta = 0$ : $S = \left\{\frac{1}{3}\right\}$ (c'est $(3x - 1)^2$).

### Exercice 13 — Sans le discriminant <span class="etoiles">★</span>

Résoudre sans calculer de discriminant : $x^2 = 7x$ ; $(x - 3)^2 = 4$ ; $3x^2 - 12 = 0$ ; $x^2 + 5 = 0$.

??? success "Correction"
    - $x(x - 7) = 0$ : $S = \{0\,;\,7\}$.
    - $x - 3 = 2$ ou $x - 3 = -2$ : $S = \{1\,;\,5\}$.
    - $x^2 = 4$ : $S = \{-2\,;\,2\}$.
    - $x^2 = -5$ : impossible, $S = \varnothing$.

### Exercice 14 — Somme et produit <span class="etoiles">★</span>

Sans calculer $\Delta$, trouver deux nombres dont la somme vaut $7$ et le produit $10$. En déduire la factorisation de $x^2 - 7x + 10$.

??? success "Correction"
    $2$ et $5$ conviennent ($2 + 5 = 7$, $2 \times 5 = 10$). Ce sont les racines de $x^2 - 7x + 10$, qui vaut donc $(x - 2)(x - 5)$.

### Exercice 15 — Racine évidente <span class="etoiles">★★</span>

1. Vérifier que $1$ est racine de $3x^2 - 5x + 2$, et en déduire l'autre racine sans calculer $\Delta$.
2. Même question avec $-1$ et le trinôme $2x^2 + 7x + 5$.

??? success "Correction"
    **1.** $3 - 5 + 2 = 0$. Produit des racines : $\frac{2}{3}$, donc l'autre racine est $\frac{2}{3}$.

    **2.** $2 - 7 + 5 = 0$. Produit des racines : $\frac{5}{2}$, donc l'autre racine est $-\frac{5}{2}$.

### Exercice 16 — Racine double <span class="etoiles">★★</span>

Pour quelles valeurs du réel $m$ l'équation $x^2 + mx + 4 = 0$ a-t-elle une unique solution ? Préciser cette solution.

??? success "Correction"
    $\Delta = m^2 - 16 = 0 \iff m = 4$ ou $m = -4$. Pour $m = 4$ : $(x + 2)^2 = 0$, solution $-2$. Pour $m = -4$ : $(x - 2)^2 = 0$, solution $2$.

### Exercice 17 — Équation bicarrée <span class="etoiles">★★</span>

Résoudre $x^4 - 5x^2 + 4 = 0$ en posant $X = x^2$.

??? success "Correction"
    $X^2 - 5X + 4 = 0$ : $\Delta = 9$, $X = 1$ ou $X = 4$. Puis $x^2 = 1$ ou $x^2 = 4$ : $S = \{-2\,;\,-1\,;\,1\,;\,2\}$.

### Exercice 18 — Parabole et droite <span class="etoiles">★★</span>

Déterminer les points d'intersection de la parabole d'équation $y = x^2 - 3x + 1$ et de la droite d'équation $y = x - 2$.

??? success "Correction"
    $x^2 - 3x + 1 = x - 2 \iff x^2 - 4x + 3 = 0 \iff x = 1$ ou $x = 3$ (somme $4$, produit $3$). Points $(1\,;\,-1)$ et $(3\,;\,1)$.

---

## Thème 4 — Signe et inéquations

*Méthodes associées : [Méthode 5](methodes.md#methode-5-etudier-un-signe-resoudre-une-inequation) et [Méthode 6](methodes.md#methode-6-etudier-la-position-de-deux-courbes).*

### Exercice 19 — Tableau de signes <span class="etoiles">★</span>

Dresser le tableau de signes de $x^2 - x - 6$.

??? success "Correction"
    $\Delta = 25$, racines $-2$ et $3$, $a = 1 > 0$ : positif sur $]-\infty\,;\,-2[$ et $]3\,;\,+\infty[$, négatif sur $]-2\,;\,3[$, nul en $-2$ et $3$.

### Exercice 20 — Inéquation <span class="etoiles">★</span>

Résoudre $2x^2 - 3x - 2 \leq 0$, puis $2x^2 - 3x - 2 > 0$.

??? success "Correction"
    Racines $-\frac{1}{2}$ et $2$, $a > 0$. $2x^2 - 3x - 2 \leq 0 \iff x \in \left[-\frac{1}{2}\,;\,2\right]$, et $2x^2 - 3x - 2 > 0 \iff x \in \left]-\infty\,;\,-\frac{1}{2}\right[ \cup\, ]2\,;\,+\infty[$.

### Exercice 21 — Toujours négatif <span class="etoiles">★</span>

Montrer que $-x^2 + 2x - 3 < 0$ pour tout réel $x$, de deux façons.

??? success "Correction"
    **Avec $\Delta$** : $\Delta = 4 - 12 = -8 < 0$, donc le trinôme est toujours du signe de $a = -1$.

    **Avec la forme canonique** : $-x^2 + 2x - 3 = -(x - 1)^2 - 2 \leq -2 < 0$.

### Exercice 22 — Un ensemble de définition <span class="etoiles">★★</span>

Déterminer l'ensemble des réels $x$ pour lesquels $\sqrt{4 - x^2}$ existe, puis ceux pour lesquels $\sqrt{x^2 - 5x + 4}$ existe.

??? success "Correction"
    $4 - x^2 \geq 0 \iff x^2 \leq 4 \iff x \in [-2\,;\,2]$.

    $x^2 - 5x + 4 \geq 0$ : racines $1$ et $4$, $a > 0$, donc $x \in\, ]-\infty\,;\,1] \cup [4\,;\,+\infty[$.

### Exercice 23 — Deux paraboles <span class="etoiles">★★</span>

Soit $f(x) = x^2 + x - 1$ et $g(x) = -x^2 + 3x + 3$. Déterminer les points d'intersection de leurs courbes, puis leur position relative.

??? success "Correction"
    $f(x) - g(x) = 2x^2 - 2x - 4 = 2(x^2 - x - 2) = 2(x + 1)(x - 2)$. Les courbes se coupent en $(-1\,;\,-1)$ et $(2\,;\,5)$. La courbe de $f$ est au-dessus de celle de $g$ sur $]-\infty\,;\,-1[$ et sur $]2\,;\,+\infty[$, en dessous sur $]-1\,;\,2[$.

### Exercice 24 — Inéquation avec un quotient <span class="etoiles">★★★</span>

Résoudre $\dfrac{x + 3}{x^2 - x - 2} \leq 0$.

??? success "Correction"
    Le dénominateur s'annule en $-1$ et $2$ (valeurs interdites) ; il est positif à l'extérieur de ces racines. Le numérateur s'annule en $-3$.

    | $x$ | $-\infty$ | | $-3$ | | $-1$ | | $2$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|---|---|
    | $x + 3$ | | $-$ | $0$ | $+$ | | $+$ | | $+$ | |
    | $x^2 - x - 2$ | | $+$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
    | quotient | | $-$ | $0$ | $+$ | ‖ | $-$ | ‖ | $+$ | |

    $S = \,]-\infty\,;\,-3] \cup\, ]-1\,;\,2[$.

---

## Thème 5 — Problèmes et approfondissement

### Exercice 25 — Somme et produit donnés <span class="etoiles">★★</span>

Trouver deux nombres dont la somme vaut $10$ et le produit $21$. Existe-t-il deux nombres de somme $4$ et de produit $5$ ?

??? success "Correction"
    Ils sont solutions de $x^2 - 10x + 21 = 0$ : $\Delta = 16$, ce sont $3$ et $7$. Pour une somme $4$ et un produit $5$ : $x^2 - 4x + 5 = 0$ a pour discriminant $16 - 20 < 0$ : de tels nombres réels n'existent pas.

### Exercice 26 — Une trajectoire <span class="etoiles">★★</span>

On lance une balle du haut d'un immeuble. Sa hauteur (en mètres) au-dessus du sol après $t$ secondes est $h(t) = -5t^2 + 10t + 15$.

1. De quelle hauteur la balle est-elle lancée ?
2. Quelle hauteur maximale atteint-elle ?
3. À quel instant touche-t-elle le sol ?

??? success "Correction"
    **1.** $h(0) = 15$ m.

    **2.** $\alpha = 1$, $h(1) = 20$ m.

    **3.** $h(t) = 0 \iff t^2 - 2t - 3 = 0 \iff (t - 3)(t + 1) = 0$. Comme $t \geq 0$ : la balle touche le sol au bout de $3$ secondes.

### Exercice 27 — Discuter selon un paramètre <span class="etoiles">★★★</span>

Selon les valeurs du réel $m$, déterminer le nombre de solutions de l'équation $mx^2 + 2x + 1 = 0$.

??? success "Correction"
    **Cas $m = 0$** : l'équation est $2x + 1 = 0$, du premier degré, avec une solution $-\frac{1}{2}$.

    **Cas $m \neq 0$** : $\Delta = 4 - 4m$.

    - Si $m < 1$ (et $m \neq 0$) : $\Delta > 0$, deux solutions.
    - Si $m = 1$ : $\Delta = 0$, une solution ($x = -1$).
    - Si $m > 1$ : aucune solution.

    *Le piège classique est d'oublier le cas $m = 0$, où ce n'est plus une équation du second degré.*

### Exercice 28 — Une fonction Python <span class="etoiles">★★</span>

1. Écrire une fonction Python `canonique(a, b, c)` qui renvoie le couple $(\alpha, \beta)$ de la forme canonique.
2. Écrire une fonction `signe(a, b, c, x)` qui renvoie `"+"`, `"-"` ou `"0"` selon le signe du trinôme en $x$.
3. Écrire un programme qui affiche le signe de $x^2 - x - 6$ pour les entiers $x$ de $-4$ à $4$, et comparer avec l'exercice 19.

??? success "Correction"
    ```python
    def canonique(a, b, c):
        alpha = -b / (2 * a)
        beta = a * alpha**2 + b * alpha + c
        return alpha, beta

    def signe(a, b, c, x):
        v = a * x**2 + b * x + c
        if v > 0:
            return "+"
        elif v < 0:
            return "-"
        else:
            return "0"

    for x in range(-4, 5):
        print(x, signe(1, -1, -6, x))
    ```

    On obtient `+` pour $-4$ et $-3$, `0` pour $-2$, `-` de $-1$ à $2$, `0` pour $3$, et `+` pour $4$ : c'est cohérent avec le tableau de l'exercice 19.
