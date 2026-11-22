# Exercices corrigés — Nombres, ensembles et arithmétique

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf les exercices Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Ensembles de nombres | 1 à 6 |
| 2. Intervalles | 7 à 11 |
| 3. Valeur absolue et encadrements | 12 à 17 |
| 4. Multiples, diviseurs, parité | 18 à 23 |
| 5. Nombres premiers et approfondissement | 24 à 28 |

---

## Thème 1 — Ensembles de nombres

*Méthode associée : [Méthode 1](methodes.md#methode-1-determiner-le-plus-petit-ensemble-auquel-appartient-un-nombre).*

### Exercice 1 — Classer des nombres <span class="etoiles">★</span>

Donner le plus petit ensemble de nombres ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{D}$, $\mathbb{Q}$ ou $\mathbb{R}$) auquel appartient chaque nombre :

$-5$ ; $\frac{3}{4}$ ; $\sqrt{25}$ ; $\pi$ ; $\frac{-12}{3}$ ; $\frac{1}{7}$ ; $\frac{\sqrt{3}}{\sqrt{12}}$ ; $2{,}5 \times 10^{-3}$.

??? success "Correction"
    $-5 \in \mathbb{Z}$ ; $\frac{3}{4} = 0{,}75 \in \mathbb{D}$ ; $\sqrt{25} = 5 \in \mathbb{N}$ ; $\pi \in \mathbb{R}$ (irrationnel) ; $\frac{-12}{3} = -4 \in \mathbb{Z}$ ; $\frac{1}{7} \in \mathbb{Q}$ ; $\frac{\sqrt{3}}{\sqrt{12}} = \sqrt{\frac{3}{12}} = \sqrt{\frac{1}{4}} = \frac{1}{2} \in \mathbb{D}$ ; $2{,}5 \times 10^{-3} = 0{,}0025 \in \mathbb{D}$.

### Exercice 2 — Vrai ou faux <span class="etoiles">★</span>

$-3 \in \mathbb{N}$ ; $0{,}1 \in \mathbb{D}$ ; $\frac{2}{3} \in \mathbb{D}$ ; $\sqrt{16} \in \mathbb{Z}$ ; $\mathbb{Z} \subset \mathbb{Q}$ ; $\pi \in \mathbb{Q}$.

??? success "Correction"
    Faux ; vrai ; faux ; vrai ($\sqrt{16} = 4$) ; vrai ; faux.

### Exercice 3 — Décimal ou non ? <span class="etoiles">★</span>

Les nombres suivants sont-ils décimaux ? Justifier. $\frac{3}{8}$ ; $\frac{7}{25}$ ; $\frac{4}{15}$ ; $\frac{9}{12}$ ; $\frac{22}{55}$.

??? success "Correction"
    Une fraction **irréductible** est décimale si et seulement si son dénominateur n'a pas d'autres facteurs premiers que $2$ et $5$.

    - $\frac{3}{8} = 0{,}375$ : décimal ($8 = 2^3$).
    - $\frac{7}{25} = 0{,}28$ : décimal ($25 = 5^2$).
    - $\frac{4}{15}$ : irréductible et $15 = 3 \times 5$ contient $3$ : non décimal.
    - $\frac{9}{12} = \frac{3}{4} = 0{,}75$ : décimal.
    - $\frac{22}{55} = \frac{2}{5} = 0{,}4$ : décimal.

### Exercice 4 — Écriture fractionnaire d'un nombre périodique <span class="etoiles">★★</span>

1. Soit $x = 0{,}272727\ldots$ (le motif $27$ se répète indéfiniment). Calculer $100x - x$ et en déduire $x$ sous forme de fraction irréductible.
2. Même question pour $y = 1{,}2333\ldots$ (on calculera $100y - 10y$).

??? success "Correction"
    1. $100x = 27{,}2727\ldots$, donc $100x - x = 27$, soit $99x = 27$ et $x = \frac{27}{99} = \frac{3}{11}$.
    2. $100y = 123{,}333\ldots$ et $10y = 12{,}333\ldots$, donc $90y = 111$ et $y = \frac{111}{90} = \frac{37}{30}$.

### Exercice 5 — Un autre rationnel non décimal <span class="etoiles">★★</span>

En s'inspirant de la démonstration du cours pour $\frac{1}{3}$, démontrer que $\frac{1}{7}$ n'est pas décimal. *On pourra utiliser le fait que $10^n = 2^n \times 5^n$.*

??? success "Correction"
    Par l'absurde : si $\frac{1}{7} = \frac{a}{10^n}$, alors $10^n = 7a$, donc $7$ divise $10^n = 2^n \times 5^n$. Mais la décomposition en facteurs premiers de $10^n$ ne contient que des $2$ et des $5$ : $7$ n'y apparaît pas, ce qui contredit l'unicité de la décomposition. Donc $\frac{1}{7}$ n'est pas décimal.

### Exercice 6 — Sommes et produits d'irrationnels <span class="etoiles">★★★</span>

1. Démontrer par l'absurde que $1 + \sqrt{2}$ est irrationnel.
2. Le produit de deux irrationnels est-il toujours irrationnel ? La somme ?

??? success "Correction"
    1. Si $1 + \sqrt{2} = r$ avec $r$ rationnel, alors $\sqrt{2} = r - 1$ serait rationnel (différence de deux rationnels). C'est faux, donc $1 + \sqrt{2}$ est irrationnel.
    2. Non : $\sqrt{2} \times \sqrt{2} = 2$ est rationnel. Non plus pour la somme : $\sqrt{2} + \left(-\sqrt{2}\right) = 0$, ou $(1 + \sqrt{2}) + (1 - \sqrt{2}) = 2$.

---

## Thème 2 — Intervalles

*Méthode associée : [Méthode 2](methodes.md#methode-2-utiliser-les-intervalles).*

### Exercice 7 — Traduire <span class="etoiles">★</span>

1. Écrire sous forme d'intervalle l'ensemble des réels $x$ tels que : $x \geq -2$ ; $-1 < x \leq 4$ ; $x < 3$ ; $0 \leq x < \frac{1}{2}$.
2. Traduire par une inégalité : $x \in ]-\infty\,;\,5]$ ; $x \in ]-3\,;\,0[$.

??? success "Correction"
    1. $[-2\,;\,+\infty[$ ; $]-1\,;\,4]$ ; $]-\infty\,;\,3[$ ; $\left[0\,;\,\frac{1}{2}\right[$.
    2. $x \leq 5$ ; $-3 < x < 0$.

### Exercice 8 — Réunions et intersections <span class="etoiles">★</span>

Écrire le plus simplement possible :

1. $[-3\,;\,5] \cap [0\,;\,8]$ et $[-3\,;\,5] \cup [0\,;\,8]$ ;
2. $]-\infty\,;\,2[ \cap [2\,;\,6]$ et $]-\infty\,;\,2[ \cup [2\,;\,6]$ ;
3. $[1\,;\,4] \cap [6\,;\,9]$ et $[1\,;\,4] \cup [6\,;\,9]$.

??? success "Correction"
    1. $[0\,;\,5]$ et $[-3\,;\,8]$.
    2. $\varnothing$ ($2$ n'est pas dans le premier) et $]-\infty\,;\,6]$.
    3. $\varnothing$ et $[1\,;\,4] \cup [6\,;\,9]$ (ne se simplifie pas).

### Exercice 9 — Appartenance <span class="etoiles">★</span>

Dire si chaque affirmation est vraie : $2 \in ]2\,;\,5]$ ; $\pi \in [3{,}14\,;\,3{,}15]$ ; $-\sqrt{2} \in ]-1{,}5\,;\,-1{,}4[$ ; $\frac{1}{3} \in [0{,}33\,;\,0{,}34]$.

??? success "Correction"
    Faux ($2$ est exclu) ; vrai ($\pi \approx 3{,}1416$) ; vrai ($-\sqrt{2} \approx -1{,}414$) ; vrai ($0{,}33 < 0{,}333\ldots < 0{,}34$).

### Exercice 10 — Inéquations et intervalles <span class="etoiles">★★</span>

Résoudre et donner l'ensemble des solutions sous forme d'intervalle :

1. $2x - 3 > 5$ ;
2. $-3x + 1 \leq 7$ ;
3. les deux inéquations à la fois.

??? success "Correction"
    1. $2x > 8 \iff x > 4$ : $]4\,;\,+\infty[$.
    2. $-3x \leq 6 \iff x \geq -2$ (on divise par $-3 < 0$, le sens change) : $[-2\,;\,+\infty[$.
    3. Intersection : $]4\,;\,+\infty[$.

### Exercice 11 — Complémentaire <span class="etoiles">★★</span>

1. Écrire l'ensemble des réels qui n'appartiennent pas à $[-1\,;\,3[$.
2. Écrire l'ensemble des réels qui n'appartiennent ni à $]-\infty\,;\,0]$ ni à $[5\,;\,+\infty[$.

??? success "Correction"
    1. $]-\infty\,;\,-1[ \cup [3\,;\,+\infty[$.
    2. $]0\,;\,5[$.

---

## Thème 3 — Valeur absolue et encadrements

*Méthode associée : [Méthode 3](methodes.md#methode-3-utiliser-la-valeur-absolue-comme-une-distance).*

### Exercice 12 — Calculer des valeurs absolues <span class="etoiles">★</span>

Écrire sans valeur absolue : $|-7|$ ; $|3 - \pi|$ ; $|\sqrt{2} - 2|$ ; $|1 - \sqrt{3}|$.

??? success "Correction"
    $7$ ; $\pi - 3$ (car $3 - \pi < 0$) ; $2 - \sqrt{2}$ (car $\sqrt{2} < 2$) ; $\sqrt{3} - 1$ (car $\sqrt{3} > 1$).

### Exercice 13 — Distances <span class="etoiles">★</span>

Calculer la distance entre $-3$ et $5$, entre $-2{,}5$ et $-7$, entre $\sqrt{2}$ et $-\sqrt{2}$.

??? success "Correction"
    $|5 - (-3)| = 8$ ; $|-7 - (-2{,}5)| = 4{,}5$ ; $2\sqrt{2}$.

### Exercice 14 — Équations et inéquations avec valeur absolue <span class="etoiles">★★</span>

Résoudre : $|x - 4| = 3$ ; $|x + 1| \leq 2$ ; $|x - 2| > 5$ ; $|x| = -2$.

??? success "Correction"
    - Réels à distance $3$ de $4$ : $x = 1$ ou $x = 7$.
    - Distance à $-1$ au plus $2$ : $[-3\,;\,1]$.
    - Distance à $2$ strictement plus grande que $5$ : $]-\infty\,;\,-3[ \cup ]7\,;\,+\infty[$.
    - Une valeur absolue est positive : pas de solution.

### Exercice 15 — Avec une valeur absolue <span class="etoiles">★★</span>

Écrire chaque condition à l'aide d'une valeur absolue : $x \in [-1\,;\,7]$ ; $x \in ]2\,;\,3[$ ; $-0{,}5 \leq x \leq 0{,}5$.

??? success "Correction"
    $|x - 3| \leq 4$ ; $|x - 2{,}5| < 0{,}5$ ; $|x| \leq 0{,}5$.

### Exercice 16 — Encadrer $\sqrt{5}$ <span class="etoiles">★★</span>

1. Encadrer $\sqrt{5}$ entre deux décimaux consécutifs à $10^{-2}$ près, en calculant des carrés.
2. En calculant $2{,}235^2$, donner l'arrondi de $\sqrt{5}$ au centième.

??? success "Correction"
    1. $2{,}23^2 = 4{,}9729 < 5$ et $2{,}24^2 = 5{,}0176 > 5$ : $2{,}23 < \sqrt{5} < 2{,}24$.
    2. $2{,}235^2 = 4{,}995225 < 5$, donc $\sqrt{5} > 2{,}235$ : $\sqrt{5}$ est plus proche de $2{,}24$. Arrondi : $2{,}24$.

### Exercice 17 — Encadrement par balayage en Python <span class="etoiles">★★★</span>

1. Expliquer ce que fait la fonction suivante, et ce que renvoie `balayage(1)`.

    ```python
    def balayage(pas):
        x = 0
        while x**2 < 2:
            x = x + pas
        return x - pas, x
    ```

2. Que renvoie `balayage(0.01)` ? Pourquoi le résultat affiché peut-il comporter des chiffres « parasites » ?

??? success "Correction"
    1. Partant de $0$, on avance de `pas` en `pas` tant que $x^2 < 2$. On s'arrête au premier $x$ tel que $x^2 \geq 2$ : alors $x - \text{pas} < \sqrt{2} \leq x$. `balayage(1)` renvoie `(1, 2)`.
    2. Un encadrement de $\sqrt{2}$ d'amplitude $0{,}01$ : $(1{,}41\,;\,1{,}42)$. Python affiche par exemple `1.4100000000000008`, car les nombres comme $0{,}01$ ne sont pas représentés exactement en machine (ils sont stockés en binaire) : les erreurs d'arrondi s'accumulent.

---

## Thème 4 — Multiples, diviseurs, parité

*Méthode associée : [Méthode 4](methodes.md#methode-4-demontrer-une-propriete-sur-les-entiers).*

### Exercice 18 — Diviseurs <span class="etoiles">★</span>

1. Donner tous les diviseurs positifs de $36$, puis de $45$.
2. En déduire leurs diviseurs communs et le plus grand d'entre eux.

??? success "Correction"
    1. $36$ : $1, 2, 3, 4, 6, 9, 12, 18, 36$. $45$ : $1, 3, 5, 9, 15, 45$.
    2. Diviseurs communs : $1, 3, 9$. Le plus grand est $9$.

### Exercice 19 — Multiples <span class="etoiles">★</span>

1. $1\,001$ est-il un multiple de $7$ ? de $11$ ? de $13$ ?
2. Trouver tous les multiples de $17$ compris entre $100$ et $150$.

??? success "Correction"
    1. $1\,001 = 7 \times 143 = 7 \times 11 \times 13$ : oui pour les trois.
    2. $17 \times 6 = 102$, $17 \times 7 = 119$, $17 \times 8 = 136$ ($17 \times 9 = 153 > 150$).

### Exercice 20 — Trois entiers consécutifs <span class="etoiles">★★</span>

Démontrer que la somme de trois entiers consécutifs est un multiple de $3$.

??? success "Correction"
    Trois entiers consécutifs s'écrivent $n$, $n + 1$, $n + 2$. Leur somme vaut $3n + 3 = 3(n + 1)$, et $n + 1$ est un entier : c'est un multiple de $3$.

### Exercice 21 — Deux entiers consécutifs <span class="etoiles">★★</span>

Démontrer, par disjonction des cas, que le produit de deux entiers consécutifs est pair.

??? success "Correction"
    Soit $n$ et $n + 1$.

    - Si $n$ est pair, $n = 2k$ : $n(n + 1) = 2k(n + 1)$ est pair.
    - Si $n$ est impair, $n + 1$ est pair : $n + 1 = 2k$, et $n(n + 1) = 2kn$ est pair.

### Exercice 22 — Parité d'une somme et d'un produit <span class="etoiles">★★</span>

1. Démontrer que la somme d'un entier pair et d'un entier impair est impaire.
2. Démontrer que le produit de deux entiers impairs est impair.

??? success "Correction"
    1. $2k + (2k' + 1) = 2(k + k') + 1$ : impair.
    2. $(2k + 1)(2k' + 1) = 4kk' + 2k + 2k' + 1 = 2(2kk' + k + k') + 1$ : impair.

### Exercice 23 — Une conjecture <span class="etoiles">★★★</span>

1. Calculer $n^3 - n$ pour $n = 2, 3, 4, 5$. Que remarque-t-on ?
2. Factoriser $n^3 - n$, puis démontrer la conjecture.
3. L'affirmation « pour tout entier $n$, $n^2 + n + 41$ est premier » est-elle vraie ? *(Tester $n = 40$.)*

??? success "Correction"
    1. $6$, $24$, $60$, $120$ : ce sont des multiples de $6$ (donc de $2$ et de $3$).
    2. $n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1)$ : c'est le produit de trois entiers consécutifs. Parmi eux, au moins un est pair (le produit est pair) et un est multiple de $3$ (sur trois entiers consécutifs, l'un a pour reste $0$ dans la division par $3$). Le produit est donc multiple de $2$ et de $3$, donc de $6$.
    3. Pour $n = 40$ : $1\,600 + 40 + 41 = 1\,681 = 41^2$, qui n'est pas premier. L'affirmation est fausse, alors qu'elle est vraie pour $n = 0, 1, \ldots, 39$ ! Un grand nombre d'exemples ne constitue pas une démonstration.

---

## Thème 5 — Nombres premiers et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-decomposer-en-facteurs-premiers-et-simplifier).*

### Exercice 24 — Premier ou pas ? <span class="etoiles">★</span>

Les nombres $91$, $97$, $119$ et $2$ sont-ils premiers ?

??? success "Correction"
    - $91 = 7 \times 13$ : non.
    - $97$ n'est divisible ni par $2$, ni par $3$, ni par $5$, ni par $7$, et $11^2 = 121 > 97$ : il est premier.
    - $119 = 7 \times 17$ : non.
    - $2$ est premier (le seul premier pair).

### Exercice 25 — Décompositions <span class="etoiles">★</span>

Décomposer en produit de facteurs premiers : $180$ ; $1\,260$ ; $1\,024$.

??? success "Correction"
    $180 = 2^2 \times 3^2 \times 5$ ; $1\,260 = 2^2 \times 3^2 \times 5 \times 7$ ; $1\,024 = 2^{10}$.

### Exercice 26 — Simplifier <span class="etoiles">★★</span>

Rendre irréductibles les fractions $\frac{180}{1\,260}$ et $\frac{1\,260}{1\,024}$.

??? success "Correction"
    $\frac{180}{1\,260} = \frac{2^2 \times 3^2 \times 5}{2^2 \times 3^2 \times 5 \times 7} = \frac{1}{7}$ ; $\frac{1\,260}{1\,024} = \frac{2^2 \times 315}{2^2 \times 256} = \frac{315}{256}$.

### Exercice 27 — Carrés parfaits et nombre de diviseurs <span class="etoiles">★★</span>

1. Par quel plus petit entier faut-il multiplier $180$ pour obtenir un carré parfait ?
2. Combien $180$ a-t-il de diviseurs positifs ? *(Un diviseur s'écrit $2^a \times 3^b \times 5^c$.)*

??? success "Correction"
    1. $180 = 2^2 \times 3^2 \times 5$ : il faut que tous les exposants soient pairs. On multiplie par $5$ : $900 = 30^2$.
    2. $a \in \{0, 1, 2\}$, $b \in \{0, 1, 2\}$, $c \in \{0, 1\}$ : $3 \times 3 \times 2 = 18$ diviseurs.

### Exercice 28 — Nombres premiers en Python <span class="etoiles">★★★</span>

1. Écrire une fonction `est_premier(n)` qui renvoie `True` si l'entier `n` est premier.
2. Écrire une fonction `liste_premiers(N)` qui renvoie la **liste** des nombres premiers inférieurs ou égaux à `N`. Combien y en a-t-il jusqu'à $100$ ?

??? success "Correction"
    ```python
    def est_premier(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d = d + 1
        return True

    def liste_premiers(N):
        return [n for n in range(2, N + 1) if est_premier(n)]

    print(len(liste_premiers(100)))   # 25
    ```

    On peut s'arrêter dès que $d^2 > n$ : si $n = ab$ avec $2 \leq a \leq b$, alors $a^2 \leq n$, donc un diviseur aurait déjà été trouvé.
