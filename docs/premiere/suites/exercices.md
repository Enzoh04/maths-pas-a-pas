# Exercices corrigés — Suites numériques, modèles discrets

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Les exercices marqués « calculatrice » sont les seuls où elle est utile ; tous les autres se font à la main.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Générer une suite | 1 à 6 |
| 2. Sens de variation | 7 à 11 |
| 3. Suites arithmétiques | 12 à 17 |
| 4. Suites géométriques | 18 à 24 |
| 5. Comportement à l'infini et approfondissement | 25 à 28 |

---

## Thème 1 — Générer une suite

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-des-termes).*

### Exercice 1 — Suite explicite <span class="etoiles">★</span>

Soit $u_n = n^2 - 3n$ pour tout entier naturel $n$. Calculer $u_0$, $u_1$, $u_2$ et $u_{10}$, puis exprimer $u_{n+1}$ en fonction de $n$.

??? success "Correction"
    $u_0 = 0$, $u_1 = -2$, $u_2 = -2$, $u_{10} = 70$. Puis $u_{n+1} = (n+1)^2 - 3(n+1) = n^2 + 2n + 1 - 3n - 3 = n^2 - n - 2$.

### Exercice 2 — Suite récurrente <span class="etoiles">★</span>

Soit $(u_n)$ définie par $u_0 = 2$ et $u_{n+1} = 3u_n - 1$. Calculer $u_1$, $u_2$, $u_3$ et $u_4$.

??? success "Correction"
    $u_1 = 5$, $u_2 = 14$, $u_3 = 41$, $u_4 = 122$.

### Exercice 3 — Un motif d'allumettes <span class="etoiles">★★</span>

On aligne des carrés faits d'allumettes, deux carrés voisins partageant un côté. Il faut $4$ allumettes pour un carré, $7$ pour deux carrés, $10$ pour trois carrés.

1. On note $a_n$ le nombre d'allumettes pour $n$ carrés. Exprimer $a_{n+1}$ en fonction de $a_n$.
2. En déduire $a_n$ en fonction de $n$, et le nombre d'allumettes pour $50$ carrés.
3. Combien de carrés peut-on former avec $100$ allumettes ?

??? success "Correction"
    **1.** Chaque nouveau carré réutilise un côté et demande $3$ allumettes : $a_{n+1} = a_n + 3$.

    **2.** $(a_n)$ est arithmétique de raison $3$ avec $a_1 = 4$ : $a_n = 4 + 3(n - 1) = 3n + 1$. Pour $50$ carrés : $151$ allumettes.

    **3.** $3n + 1 \leq 100 \iff n \leq 33$. On peut former $33$ carrés (avec $100$ allumettes exactement).

### Exercice 4 — Deux définitions de la même suite <span class="etoiles">★★</span>

On pose $u_n = 2^n - 1$. Calculer les cinq premiers termes, puis montrer que $u_{n+1} = 2u_n + 1$ pour tout $n$.

??? success "Correction"
    $u_0 = 0$, $u_1 = 1$, $u_2 = 3$, $u_3 = 7$, $u_4 = 15$. Puis $2u_n + 1 = 2(2^n - 1) + 1 = 2^{n+1} - 2 + 1 = 2^{n+1} - 1 = u_{n+1}$.

### Exercice 5 — Une liste en Python <span class="etoiles">★</span>

Que contient la liste `L` à la fin du programme suivant ? Quelle suite représente-t-elle ?

```python
L = [1]
for n in range(5):
    L.append(L[n] + 2 * n + 3)
```

??? success "Correction"
    On part de $L[0] = 1$, puis on ajoute $3$, $5$, $7$, $9$, $11$ : `L = [1, 4, 9, 16, 25, 36]`. Ce sont les carrés $u_n = (n+1)^2$ : en effet, $(n + 2)^2 - (n + 1)^2 = 2n + 3$.

### Exercice 6 — Somme des nombres impairs <span class="etoiles">★★</span>

Soit $(u_n)$ définie par $u_0 = 0$ et $u_{n+1} = u_n + 2n + 1$.

1. Calculer $u_1$, …, $u_5$. Conjecturer une expression de $u_n$.
2. Interpréter $u_n$ comme une somme de nombres impairs.
3. Démontrer la conjecture à l'aide de la formule $1 + 2 + \cdots + (n-1) = \frac{(n-1)n}{2}$.

??? success "Correction"
    **1.** $1, 4, 9, 16, 25$ : on conjecture $u_n = n^2$.

    **2.** $u_n = 1 + 3 + 5 + \cdots + (2n - 1)$, somme des $n$ premiers nombres impairs.

    **3.** $u_n = \sum_{k=0}^{n-1} (2k + 1) = 2\,(0 + 1 + \cdots + (n-1)) + n = 2 \times \frac{(n-1)n}{2} + n = n^2 - n + n = n^2$.

---

## Thème 2 — Sens de variation

*Méthode associée : [Méthode 2](methodes.md#methode-2-etudier-le-sens-de-variation).*

### Exercice 7 — Avec la différence <span class="etoiles">★</span>

Étudier le sens de variation de la suite définie par $u_n = 3n - 7$.

??? success "Correction"
    $u_{n+1} - u_n = 3 > 0$ : la suite est strictement croissante.

### Exercice 8 — Pas monotone dès le départ <span class="etoiles">★★</span>

Étudier le sens de variation de la suite définie par $u_n = n^2 - 10n$.

??? success "Correction"
    $u_{n+1} - u_n = 2n + 1 - 10 = 2n - 9$, négatif pour $n \leq 4$ et positif pour $n \geq 5$. La suite décroît de $u_0$ à $u_5$, puis croît : elle est croissante à partir du rang $5$, mais elle n'est pas monotone.

### Exercice 9 — Une suite de quotients <span class="etoiles">★</span>

Étudier le sens de variation de la suite définie par $u_n = \dfrac{1}{n+1}$.

??? success "Correction"
    $u_{n+1} - u_n = \dfrac{1}{n+2} - \dfrac{1}{n+1} = \dfrac{(n+1) - (n+2)}{(n+1)(n+2)} = \dfrac{-1}{(n+1)(n+2)} < 0$ : strictement décroissante. *On peut aussi dire que $x \mapsto \frac{1}{x+1}$ est décroissante sur $[0\,;\,+\infty[$.*

### Exercice 10 — Avec le quotient <span class="etoiles">★</span>

Étudier le sens de variation de la suite définie par $u_n = 5 \times 0{,}8^n$.

??? success "Correction"
    Les termes sont strictement positifs et $\dfrac{u_{n+1}}{u_n} = 0{,}8 < 1$ : la suite est strictement décroissante.

### Exercice 11 — Une suite récurrente <span class="etoiles">★★</span>

Soit $(u_n)$ définie par $u_0 = 0{,}5$ et $u_{n+1} = u_n - u_n^2$. Montrer que la suite est décroissante.

??? success "Correction"
    $u_{n+1} - u_n = -u_n^2 \leq 0$ pour tout $n$ : la suite est décroissante. On n'a même pas besoin de calculer les termes.

---

## Thème 3 — Suites arithmétiques

*Méthodes associées : [Méthode 3](methodes.md#methode-3-montrer-quune-suite-est-arithmetique-ou-geometrique), [Méthode 4](methodes.md#methode-4-exprimer-u_n-en-fonction-de-n) et [Méthode 5](methodes.md#methode-5-calculer-une-somme-de-termes).*

### Exercice 12 — Application directe <span class="etoiles">★</span>

$(u_n)$ est arithmétique de premier terme $u_0 = 5$ et de raison $3$. Calculer $u_1$, $u_{20}$, puis exprimer $u_n$ en fonction de $n$.

??? success "Correction"
    $u_1 = 8$, $u_{20} = 5 + 60 = 65$, $u_n = 5 + 3n$.

### Exercice 13 — Avec deux termes <span class="etoiles">★★</span>

$(u_n)$ est arithmétique, avec $u_5 = 17$ et $u_{12} = 38$. Déterminer la raison, $u_0$, puis $u_{100}$.

??? success "Correction"
    $7r = 38 - 17 = 21$, donc $r = 3$. $u_0 = 17 - 15 = 2$, et $u_{100} = 2 + 300 = 302$.

### Exercice 14 — La somme de Gauss <span class="etoiles">★</span>

1. Calculer $1 + 2 + \cdots + 100$.
2. Calculer $1 + 2 + \cdots + 1\,000$.
3. Calculer $51 + 52 + \cdots + 100$.

??? success "Correction"
    **1.** $\frac{100 \times 101}{2} = 5\,050$. **2.** $\frac{1000 \times 1001}{2} = 500\,500$. **3.** $5\,050 - (1 + \cdots + 50) = 5\,050 - 1\,275 = 3\,775$. *Ou : $50$ termes, $50 \times \frac{51 + 100}{2} = 3\,775$.*

### Exercice 15 — Somme de termes consécutifs <span class="etoiles">★★</span>

Avec la suite de l'exercice 12, calculer $S = u_0 + u_1 + \cdots + u_{20}$.

??? success "Correction"
    $21$ termes : $S = 21 \times \frac{5 + 65}{2} = 21 \times 35 = 735$.

### Exercice 16 — Arithmétique ou non ? <span class="etoiles">★</span>

Les suites suivantes sont-elles arithmétiques ? $u_n = \dfrac{2n + 3}{5}$ ; $v_n = n^2 + 1$ ; $w_n = (n + 1)^2 - n^2$.

??? success "Correction"
    - $u_{n+1} - u_n = \frac{2}{5}$ : arithmétique de raison $\frac{2}{5}$.
    - $v_0 = 1$, $v_1 = 2$, $v_2 = 5$ : différences $1$ et $3$, pas arithmétique.
    - $w_n = 2n + 1$ : arithmétique de raison $2$.

### Exercice 17 — Un salaire qui augmente <span class="etoiles">★★</span>

Un salarié gagne $1\,800$ € par mois la première année. Son salaire mensuel augmente de $50$ € chaque année.

1. On note $s_n$ son salaire mensuel l'année $n$ (avec $s_0 = 1\,800$). Exprimer $s_n$ en fonction de $n$.
2. Quel est son salaire mensuel la dixième année ?
3. Combien gagne-t-il au total sur ses $10$ premières années (en comptant $12$ mois par an) ?

??? success "Correction"
    **1.** $s_n = 1\,800 + 50n$.

    **2.** La dixième année correspond à $n = 9$ : $s_9 = 2\,250$ €.

    **3.** Somme des salaires mensuels : $s_0 + \cdots + s_9 = 10 \times \frac{1800 + 2250}{2} = 20\,250$ €. Total sur $10$ ans : $12 \times 20\,250 = 243\,000$ €.

---

## Thème 4 — Suites géométriques

*Méthodes associées : [Méthode 4](methodes.md#methode-4-exprimer-u_n-en-fonction-de-n), [Méthode 5](methodes.md#methode-5-calculer-une-somme-de-termes) et [Méthode 6](methodes.md#methode-6-modeliser-une-evolution-et-chercher-un-seuil).*

### Exercice 18 — Application directe <span class="etoiles">★</span>

$(u_n)$ est géométrique de premier terme $u_0 = 3$ et de raison $2$. Calculer $u_5$ et $u_0 + u_1 + \cdots + u_5$.

??? success "Correction"
    $u_5 = 3 \times 32 = 96$. Somme de $6$ termes : $3 \times \frac{1 - 2^6}{1 - 2} = 3 \times 63 = 189$.

### Exercice 19 — Avec deux termes <span class="etoiles">★★</span>

$(u_n)$ est géométrique de raison positive, avec $u_2 = 12$ et $u_5 = 96$. Déterminer la raison et $u_0$.

??? success "Correction"
    $u_5 = u_2\,q^3$, donc $q^3 = 8$ et $q = 2$. Puis $u_0 = \frac{12}{4} = 3$.

### Exercice 20 — Des sommes de puissances <span class="etoiles">★★</span>

1. Calculer $1 + 2 + 2^2 + \cdots + 2^{10}$.
2. Montrer que $1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n} = 2 - \frac{1}{2^n}$.
3. Que peut-on conjecturer sur cette somme quand $n$ devient grand ?

??? success "Correction"
    **1.** $\frac{1 - 2^{11}}{1 - 2} = 2\,047$.

    **2.** $\dfrac{1 - (1/2)^{n+1}}{1 - 1/2} = 2\left(1 - \dfrac{1}{2^{n+1}}\right) = 2 - \dfrac{1}{2^n}$.

    **3.** $\frac{1}{2^n}$ devient très petit, donc la somme se rapproche de $2$ sans jamais l'atteindre. C'est le paradoxe de Zénon : on fait la moitié du chemin restant, encore et encore, sans dépasser l'arrivée.

### Exercice 21 — Une population <span class="etoiles">★</span>

Une population de $1\,000$ bactéries augmente de $3\,\%$ par heure. On note $p_n$ le nombre de bactéries après $n$ heures. Justifier que $(p_n)$ est géométrique, donner $p_n$ en fonction de $n$ et son sens de variation.

??? success "Correction"
    Augmenter de $3\,\%$ revient à multiplier par $1{,}03$ : $p_{n+1} = 1{,}03\,p_n$. Donc $(p_n)$ est géométrique de raison $1{,}03$, $p_n = 1\,000 \times 1{,}03^n$, et elle est croissante car $q > 1$ et $p_0 > 0$.

### Exercice 22 — Intérêts simples ou composés <span class="etoiles">★★</span> (calculatrice)

On place $1\,000$ €. Placement A : on ajoute $40$ € chaque année. Placement B : le capital augmente de $4\,\%$ chaque année.

1. Exprimer les capitaux $a_n$ et $b_n$ après $n$ années.
2. Comparer les capitaux après $1$ an, puis après $10$ ans.
3. Lequel des deux modèles finit par l'emporter, et pourquoi ?

??? success "Correction"
    **1.** $a_n = 1\,000 + 40n$ (arithmétique) et $b_n = 1\,000 \times 1{,}04^n$ (géométrique).

    **2.** Après $1$ an : $1\,040$ € pour les deux. Après $10$ ans : $a_{10} = 1\,400$ € et $b_{10} \approx 1\,480{,}24$ €.

    **3.** Le placement B : il rapporte des intérêts sur les intérêts. Une croissance exponentielle finit toujours par dépasser une croissance linéaire.

### Exercice 23 — Élimination d'un médicament <span class="etoiles">★★</span> (calculatrice)

On injecte $100$ mg d'un médicament. Chaque heure, l'organisme en élimine $20\,\%$. On note $c_n$ la quantité restante après $n$ heures.

1. Exprimer $c_n$ en fonction de $n$.
2. Au bout de combien d'heures restera-t-il moins de $10$ mg ?
3. Écrire un programme Python qui répond à la question 2.

??? success "Correction"
    **1.** $c_n = 100 \times 0{,}8^n$.

    **2.** La calculatrice donne $c_{10} \approx 10{,}74$ et $c_{11} \approx 8{,}59$ : au bout de $11$ heures.

    **3.**

    ```python
    n = 0
    c = 100
    while c >= 10:
        c = 0.8 * c
        n = n + 1
    print(n)    # 11
    ```

### Exercice 24 — Le sens de variation en général <span class="etoiles">★★</span>

Soit $(u_n)$ géométrique de premier terme $u_0 > 0$ et de raison $q > 0$.

1. Montrer que $u_{n+1} - u_n = u_0\,q^n\,(q - 1)$.
2. En déduire le sens de variation de $(u_n)$ selon la valeur de $q$.
3. Que se passe-t-il si $u_0 < 0$ ?

??? success "Correction"
    **1.** $u_0\,q^{n+1} - u_0\,q^n = u_0\,q^n\,(q - 1)$.

    **2.** $u_0\,q^n > 0$, donc le signe est celui de $q - 1$ : croissante si $q > 1$, décroissante si $q < 1$, constante si $q = 1$.

    **3.** $u_0\,q^n < 0$, les sens sont inversés : décroissante si $q > 1$, croissante si $0 < q < 1$.

---

## Thème 5 — Comportement à l'infini et approfondissement

### Exercice 25 — Conjecturer <span class="etoiles">★</span>

Conjecturer le comportement, quand $n$ devient grand, des suites $a_n = n^2$, $b_n = \dfrac{1}{n+1}$, $c_n = 0{,}5^n$, $d_n = (-1)^n$ et $e_n = 3 - \dfrac{2}{n+1}$.

??? success "Correction"
    $(a_n)$ tend vers $+\infty$ ; $(b_n)$ et $(c_n)$ convergent vers $0$ ; $(d_n)$ alterne entre $1$ et $-1$, elle ne converge pas ; $(e_n)$ converge vers $3$.

### Exercice 26 — Une suite arithmético-géométrique <span class="etoiles">★★★</span>

Soit $(u_n)$ définie par $u_0 = 0$ et $u_{n+1} = 0{,}5\,u_n + 2$ (c'est la suite de la construction en escalier du cours). On pose $v_n = u_n - 4$.

1. Montrer que $(v_n)$ est géométrique ; préciser sa raison et son premier terme.
2. En déduire $u_n$ en fonction de $n$.
3. Étudier le sens de variation de $(u_n)$ et conjecturer son comportement quand $n$ devient grand.
4. D'où vient le nombre $4$ ?

??? success "Correction"
    **1.** $v_{n+1} = u_{n+1} - 4 = 0{,}5\,u_n - 2 = 0{,}5\,(u_n - 4) = 0{,}5\,v_n$. Géométrique de raison $0{,}5$, avec $v_0 = -4$.

    **2.** $v_n = -4 \times 0{,}5^n$, donc $u_n = 4 - 4 \times 0{,}5^n$.

    **3.** $u_{n+1} - u_n = -4 \times 0{,}5^{n+1} + 4 \times 0{,}5^n = 4 \times 0{,}5^n \times (1 - 0{,}5) > 0$ : croissante. Comme $0{,}5^n$ tend vers $0$, $u_n$ semble converger vers $4$.

    **4.** C'est la solution de $\ell = 0{,}5\,\ell + 2$ : l'abscisse de l'intersection des droites $y = 0{,}5x + 2$ et $y = x$.

### Exercice 27 — Le temps de doublement <span class="etoiles">★★</span>

1. Écrire une fonction Python `doublement(t)` qui renvoie le nombre d'années nécessaires pour qu'une quantité qui augmente de $t\,\%$ par an double.
2. Que renvoie `doublement(3)` ?
3. Comparer à la « règle de 70 » des économistes : le temps de doublement vaut environ $\frac{70}{t}$.

??? success "Correction"
    **1.**

    ```python
    def doublement(t):
        n = 0
        x = 1
        while x < 2:
            x = x * (1 + t / 100)
            n = n + 1
        return n
    ```

    **2.** $24$ ($1{,}03^{23} \approx 1{,}97$ et $1{,}03^{24} \approx 2{,}03$).

    **3.** $\frac{70}{3} \approx 23{,}3$ : la règle donne une très bonne approximation. Elle s'explique avec le logarithme, vu en Terminale.

### Exercice 28 — La légende de l'échiquier <span class="etoiles">★★</span>

Selon la légende, l'inventeur des échecs demanda en récompense un grain de riz sur la première case de l'échiquier, deux sur la deuxième, quatre sur la troisième, et ainsi de suite en doublant jusqu'à la $64^{\text{e}}$ case.

1. Combien de grains sur la $64^{\text{e}}$ case ?
2. Combien de grains au total ?
3. Sachant que $2^{10} \approx 10^3$, donner un ordre de grandeur du total. Un grain de riz pèse environ $0{,}02$ g ; comparer à la production mondiale annuelle de riz, d'environ $5 \times 10^{14}$ g.

??? success "Correction"
    **1.** $2^{63}$ grains.

    **2.** $1 + 2 + \cdots + 2^{63} = 2^{64} - 1$.

    **3.** $2^{64} = 2^4 \times (2^{10})^6 \approx 16 \times 10^{18} \approx 1{,}6 \times 10^{19}$ grains (la valeur exacte est environ $1{,}8 \times 10^{19}$). Cela fait environ $3 \times 10^{17}$ g, soit des centaines de fois la production mondiale annuelle de riz.
