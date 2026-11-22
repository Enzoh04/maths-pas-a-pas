# Exercices corrigés — Fonction exponentielle

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). On rappelle que $e \approx 2{,}718$.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Calcul algébrique | 1 à 6 |
| 2. Équations et inéquations | 7 à 12 |
| 3. Dérivées | 13 à 17 |
| 4. Études de fonctions | 18 à 23 |
| 5. Modélisation et approfondissement | 24 à 28 |

---

## Thème 1 — Calcul algébrique

*Méthode associée : [Méthode 1](methodes.md#methode-1-simplifier-une-expression).*

### Exercice 1 — Simplifier <span class="etoiles">★</span>

Écrire sous la forme $e^k$ : $A = e^5 \times e^{-3}$ ; $B = (e^{-2})^3 \times e^7$ ; $C = \dfrac{e^{x+1}}{e^{x-1}}$ ; $D = e^{2x} \times e^{-2x + 1}$.

??? success "Correction"
    $A = e^2$ ; $B = e^{-6 + 7} = e$ ; $C = e^{(x + 1) - (x - 1)} = e^2$ ; $D = e^1 = e$.

### Exercice 2 — Une identité <span class="etoiles">★</span>

Montrer que pour tout réel $x$ : $\left(e^x + e^{-x}\right)^2 - \left(e^x - e^{-x}\right)^2 = 4$.

??? success "Correction"
    En développant : $(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x}) = 4$, car $e^x e^{-x} = 1$.

### Exercice 3 — Factoriser <span class="etoiles">★★</span>

Montrer que pour tout réel $x \neq 0$ : $\dfrac{e^{2x} - 1}{e^x - 1} = e^x + 1$.

??? success "Correction"
    $e^{2x} - 1 = (e^x)^2 - 1 = (e^x - 1)(e^x + 1)$, et $e^x - 1 \neq 0$ car $x \neq 0$.

### Exercice 4 — Deux écritures <span class="etoiles">★★</span>

Montrer que pour tout réel $x$ : $\dfrac{1}{1 + e^{-x}} = \dfrac{e^x}{e^x + 1}$.

??? success "Correction"
    On multiplie numérateur et dénominateur par $e^x > 0$ : $\dfrac{e^x}{e^x + e^x e^{-x}} = \dfrac{e^x}{e^x + 1}$.

### Exercice 5 — Comparer sans calculatrice <span class="etoiles">★★</span>

Comparer : $e^{-1}$ et $e^{-2}$ ; $e^{\sqrt{2}}$ et $e^{1{,}5}$ ; $e^2$ et $7$ (on utilisera $e > 2{,}7$).

??? success "Correction"
    $-2 < -1$ donc $e^{-2} < e^{-1}$ ; $\sqrt{2} < 1{,}5$ (car $2 < 2{,}25$) donc $e^{\sqrt{2}} < e^{1{,}5}$ ; $e^2 > 2{,}7^2 = 7{,}29 > 7$.

### Exercice 6 — Parité <span class="etoiles">★★</span>

Étudier la parité de $f(x) = e^x + e^{-x}$ et de $g(x) = e^x - e^{-x}$.

??? success "Correction"
    $f(-x) = e^{-x} + e^x = f(x)$ : $f$ est paire. $g(-x) = e^{-x} - e^x = -g(x)$ : $g$ est impaire. *Leurs moitiés s'appellent cosinus et sinus hyperboliques.*

---

## Thème 2 — Équations et inéquations

*Méthode associée : [Méthode 2](methodes.md#methode-2-resoudre-une-equation-ou-une-inequation).*

### Exercice 7 — Équation simple <span class="etoiles">★</span>

Résoudre $e^{3x - 2} = e^{x + 4}$.

??? success "Correction"
    $3x - 2 = x + 4 \iff x = 3$. $S = \{3\}$.

### Exercice 8 — Avec $1 = e^0$ <span class="etoiles">★</span>

Résoudre $e^{x^2 - 1} = 1$, puis $e^{x^2 - 1} \leq 1$.

??? success "Correction"
    $e^{x^2 - 1} = e^0 \iff x^2 = 1 \iff x = \pm 1$. Et $e^{x^2 - 1} \leq e^0 \iff x^2 \leq 1 \iff x \in [-1\,;\,1]$.

### Exercice 9 — Inéquation <span class="etoiles">★</span>

Résoudre $e^{2x} \leq e^{1 - x}$.

??? success "Correction"
    $2x \leq 1 - x \iff x \leq \frac{1}{3}$. $S = \left]-\infty\,;\,\frac{1}{3}\right]$.

### Exercice 10 — Produits <span class="etoiles">★</span>

Résoudre $(2x - 1)e^x = 0$, puis $(x + 3)e^{-x} > 0$.

??? success "Correction"
    $e^x \neq 0$ donc $2x - 1 = 0$ : $x = \frac{1}{2}$. Comme $e^{-x} > 0$, l'inéquation équivaut à $x + 3 > 0$ : $S = \,]-3\,;\,+\infty[$.

### Exercice 11 — Changement de variable <span class="etoiles">★★</span>

Résoudre $e^{2x} - (1 + e^2)\,e^x + e^2 = 0$.

??? success "Correction"
    Avec $X = e^x$ : $X^2 - (1 + e^2)X + e^2 = 0$, de racines $1$ et $e^2$ (somme $1 + e^2$, produit $e^2$). Donc $e^x = 1$ ou $e^x = e^2$ : $S = \{0\,;\,2\}$.

### Exercice 12 — Inéquation du second degré <span class="etoiles">★★</span>

Résoudre $e^{x^2} < e^x \times e^2$.

??? success "Correction"
    $e^{x^2} < e^{x + 2} \iff x^2 - x - 2 < 0 \iff (x - 2)(x + 1) < 0 \iff x \in\, ]-1\,;\,2[$.

---

## Thème 3 — Dérivées

*Méthode associée : [Méthode 3](methodes.md#methode-3-deriver-une-fonction-avec-lexponentielle).*

### Exercice 13 — Dérivées directes <span class="etoiles">★</span>

Dériver : $f(x) = e^{3x}$ ; $g(x) = e^{-x}$ ; $h(x) = 5e^{2x - 1}$ ; $k(x) = 2e^x - 3x^2$.

??? success "Correction"
    $f'(x) = 3e^{3x}$ ; $g'(x) = -e^{-x}$ ; $h'(x) = 10e^{2x - 1}$ ; $k'(x) = 2e^x - 6x$.

### Exercice 14 — Produit <span class="etoiles">★</span>

Dériver $f(x) = (x + 1)e^x$ et factoriser le résultat.

??? success "Correction"
    $f'(x) = e^x + (x + 1)e^x = (x + 2)e^x$.

### Exercice 15 — Produit avec $e^{-x}$ <span class="etoiles">★★</span>

Dériver $f(x) = x^2 e^{-x}$ et factoriser.

??? success "Correction"
    $f'(x) = 2x e^{-x} - x^2 e^{-x} = x(2 - x)e^{-x}$.

### Exercice 16 — Quotient <span class="etoiles">★★</span>

Dériver $f(x) = \dfrac{e^x}{x + 1}$ sur $]-1\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = \dfrac{e^x(x + 1) - e^x}{(x + 1)^2} = \dfrac{x\,e^x}{(x + 1)^2}$.

### Exercice 17 — Un autre quotient <span class="etoiles">★★</span>

Dériver $f(x) = \dfrac{e^x + 1}{e^x - 1}$ sur $]0\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = \dfrac{e^x(e^x - 1) - (e^x + 1)e^x}{(e^x - 1)^2} = \dfrac{-2e^x}{(e^x - 1)^2}$.

---

## Thème 4 — Études de fonctions

*Méthode associée : [Méthode 4](methodes.md#methode-4-etudier-une-fonction).*

### Exercice 18 — Un minimum <span class="etoiles">★</span>

Étudier les variations de $f(x) = (x + 1)e^x$ (voir l'exercice 14).

??? success "Correction"
    $f'(x) = (x + 2)e^x$, du signe de $x + 2$. $f$ est décroissante sur $]-\infty\,;\,-2]$, croissante sur $[-2\,;\,+\infty[$, de minimum $f(-2) = -e^{-2}$.

### Exercice 19 — Deux extremums <span class="etoiles">★★</span>

Étudier les variations de $f(x) = x^2 e^{-x}$ (voir l'exercice 15).

??? success "Correction"
    $f'(x) = x(2 - x)e^{-x}$, du signe de $x(2 - x)$ : négatif sur $]-\infty\,;\,0[$, positif sur $]0\,;\,2[$, négatif sur $]2\,;\,+\infty[$. Minimum local $f(0) = 0$, maximum local $f(2) = 4e^{-2}$.

### Exercice 20 — L'exponentielle l'emporte <span class="etoiles">★★</span>

Étudier les variations de $f(x) = e^x - x$. En déduire que $e^x > x$ pour tout réel $x$.

??? success "Correction"
    $f'(x) = e^x - 1$, positif si et seulement si $e^x \geq e^0$, c'est-à-dire $x \geq 0$. Donc $f$ a un minimum en $0$ : $f(0) = 1 > 0$. Ainsi $e^x - x \geq 1 > 0$.

### Exercice 21 — Au-dessus de sa tangente <span class="etoiles">★★</span>

1. Déterminer l'équation de la tangente à la courbe de l'exponentielle au point d'abscisse $0$.
2. Montrer que $e^x \geq 1 + x$ pour tout réel $x$.

??? success "Correction"
    **1.** $y = x + 1$.

    **2.** $h(x) = e^x - 1 - x$, $h'(x) = e^x - 1$, négatif sur $]-\infty\,;\,0[$ et positif sur $]0\,;\,+\infty[$. Minimum $h(0) = 0$, donc $h \geq 0$.

### Exercice 22 — La tangente en $1$ <span class="etoiles">★★</span>

Déterminer l'équation de la tangente à la courbe de l'exponentielle au point d'abscisse $1$, puis étudier la position de la courbe par rapport à cette tangente.

??? success "Correction"
    $y = e(x - 1) + e = ex$. Avec $h(x) = e^x - ex$ : $h'(x) = e^x - e$, négatif pour $x < 1$ et positif pour $x > 1$. Minimum $h(1) = 0$ : la courbe est au-dessus de sa tangente. *La tangente en $1$ passe par l'origine.*

### Exercice 23 — Avec $e^{2x}$ <span class="etoiles">★★★</span>

Étudier les variations de $f(x) = e^{2x} - 2e^x$ et en déduire son minimum.

??? success "Correction"
    $f'(x) = 2e^{2x} - 2e^x = 2e^x(e^x - 1)$, du signe de $e^x - 1$ : négatif pour $x < 0$, positif pour $x > 0$. Minimum $f(0) = 1 - 2 = -1$. *Autre méthode : $f(x) = (e^x - 1)^2 - 1 \geq -1$.*

---

## Thème 5 — Modélisation et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-modeliser-une-evolution-exponentielle).*

### Exercice 24 — Une suite <span class="etoiles">★</span>

Soit $u_n = 3e^{-0{,}2n}$. Montrer que $(u_n)$ est géométrique, et donner son sens de variation.

??? success "Correction"
    $u_{n+1} = 3e^{-0{,}2n}e^{-0{,}2} = e^{-0{,}2}u_n$ : géométrique de raison $e^{-0{,}2}$, avec $0 < e^{-0{,}2} < 1$ et $u_0 = 3 > 0$ : décroissante.

### Exercice 25 — Radioactivité <span class="etoiles">★★</span>

La masse (en grammes) d'un échantillon radioactif après $t$ années est $m(t) = 50\,e^{-0{,}1t}$.

1. Quelle est la masse initiale ? Étudier le sens de variation de $m$.
2. Montrer que pour tout $t \geq 0$, $m(t + 10) = \dfrac{m(t)}{e}$. Interpréter.
3. Exprimer $m(30)$ en fonction de $e$.

??? success "Correction"
    **1.** $m(0) = 50$ g. $m'(t) = -5\,e^{-0{,}1t} < 0$ : la masse décroît.

    **2.** $m(t + 10) = 50\,e^{-0{,}1t - 1} = m(t)\,e^{-1}$. Tous les $10$ ans, la masse est divisée par $e \approx 2{,}718$.

    **3.** $m(30) = 50\,e^{-3} = \dfrac{50}{e^3}$ (environ $2{,}5$ g).

### Exercice 26 — Euler pour $e^2$ <span class="etoiles">★★</span>

Adapter le programme du cours pour approcher $e^2$ par la méthode d'Euler, avec $n$ pas de longueur $h = \frac{2}{n}$. Tester avec $n = 1\,000$ et comparer à $e^2 \approx 7{,}389$.

??? success "Correction"
    ```python
    def euler(x, n):
        h = x / n
        y = 1
        for k in range(n):
            y = y + h * y
        return y

    print(euler(2, 1000))   # environ 7.374
    ```

    On calcule $\left(1 + \frac{2}{n}\right)^n$, qui se rapproche de $e^2$ quand $n$ grandit (l'erreur relative est d'environ $0{,}2\,\%$ pour $n = 1\,000$).

### Exercice 27 — Deux façons d'approcher $e$ <span class="etoiles">★★</span>

1. Écrire un programme qui calcule $\left(1 + \frac{1}{n}\right)^n$ pour $n = 10$, $100$, $1\,000$.
2. Écrire un programme qui calcule $1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots + \frac{1}{k!}$ pour $k = 10$.
3. Quelle méthode converge le plus vite vers $e = 2{,}718\,281\,8\ldots$ ?

??? success "Correction"
    ```python
    for n in [10, 100, 1000]:
        print(n, (1 + 1/n)**n)      # 2.5937, 2.7048, 2.7169

    s = 0
    terme = 1                      # 1/0! = 1
    for k in range(11):
        s = s + terme
        terme = terme / (k + 1)    # passe de 1/k! à 1/(k+1)!
    print(s)                       # 2.7182818...
    ```

    La somme des $\frac{1}{k!}$ converge **beaucoup** plus vite : $11$ termes donnent $7$ décimales exactes, alors que $\left(1 + \frac{1}{1000}\right)^{1000}$ n'en donne que $2$.

### Exercice 28 — Une équation différentielle <span class="etoiles">★★★</span>

On cherche les fonctions $f$ dérivables sur $\mathbb{R}$ telles que $f' = 2f$ et $f(0) = 3$.

1. Vérifier que $x \mapsto 3e^{2x}$ convient.
2. Soit $f$ une telle fonction. On pose $g(x) = f(x)\,e^{-2x}$. Montrer que $g$ est constante, et en déduire que $f(x) = 3e^{2x}$.

??? success "Correction"
    **1.** $(3e^{2x})' = 6e^{2x} = 2 \times 3e^{2x}$, et $3e^0 = 3$.

    **2.** $g'(x) = f'(x)e^{-2x} - 2f(x)e^{-2x} = (2f(x) - 2f(x))e^{-2x} = 0$. Donc $g$ est constante, égale à $g(0) = 3$ : $f(x)e^{-2x} = 3$, soit $f(x) = 3e^{2x}$. *C'est la méthode de Terminale pour résoudre $y' = ay$.*
