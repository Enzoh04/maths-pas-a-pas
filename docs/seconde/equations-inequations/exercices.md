# Exercices corrigés — Équations et inéquations

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf l'exercice Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Équations du premier degré | 1 à 5 |
| 2. Produit nul et $x^2 = a$ | 6 à 11 |
| 3. Équations quotient | 12 à 15 |
| 4. Inéquations du premier degré | 16 à 19 |
| 5. Tableaux de signes et approfondissement | 20 à 28 |

---

## Thème 1 — Équations du premier degré

*Méthode associée : [Méthode 1](methodes.md#methode-1-resoudre-une-equation-en-se-ramenant-a-un-produit-nul).*

### Exercice 1 — Résoudre <span class="etoiles">★</span>

Résoudre : $4x - 7 = 13$ ; $3(x - 2) = 5x + 4$ ; $\dfrac{x}{3} + 1 = \dfrac{x}{2}$ ; $2(x + 1) - 3 = 2x - 1$.

??? success "Correction"
    - $4x = 20$, $x = 5$.
    - $3x - 6 = 5x + 4 \iff -2x = 10 \iff x = -5$.
    - En multipliant par $6$ : $2x + 6 = 3x \iff x = 6$.
    - $2x - 1 = 2x - 1$ : l'égalité est toujours vraie, $S = \mathbb{R}$.

### Exercice 2 — Avec des fractions <span class="etoiles">★</span>

Résoudre $\dfrac{x - 1}{4} - \dfrac{2x + 1}{6} = \dfrac{1}{3}$.

??? success "Correction"
    En multipliant par $12$ : $3(x - 1) - 2(2x + 1) = 4 \iff 3x - 3 - 4x - 2 = 4 \iff -x = 9 \iff x = -9$.

### Exercice 3 — Entiers consécutifs <span class="etoiles">★</span>

La somme de trois entiers consécutifs vaut $87$. Quels sont ces entiers ?

??? success "Correction"
    $n + (n + 1) + (n + 2) = 87 \iff 3n + 3 = 87 \iff n = 28$ : les entiers sont $28$, $29$ et $30$.

### Exercice 4 — Retrouver un prix <span class="etoiles">★★</span>

Le prix d'un article augmente de $20\,\%$, puis on lui applique une remise de $15$ €. Il coûte alors $105$ €. Quel était son prix initial ?

??? success "Correction"
    $1{,}2p - 15 = 105 \iff 1{,}2p = 120 \iff p = 100$ €.

### Exercice 5 — Une équation avec paramètre <span class="etoiles">★★</span>

Soit $m$ un réel. Résoudre, selon les valeurs de $m$, l'équation $mx + 2 = 3x - 1$.

??? success "Correction"
    $(m - 3)x = -3$. Si $m \neq 3$ : $x = \frac{-3}{m - 3} = \frac{3}{3 - m}$. Si $m = 3$ : $0x = -3$, pas de solution.

---

## Thème 2 — Produit nul et $x^2 = a$

*Méthode associée : [Méthode 1](methodes.md#methode-1-resoudre-une-equation-en-se-ramenant-a-un-produit-nul).*

### Exercice 6 — Produit nul <span class="etoiles">★</span>

Résoudre : $(x - 4)(3x + 2) = 0$ ; $x(5 - x) = 0$ ; $(2x + 1)^2 = 0$.

??? success "Correction"
    $S = \left\{-\frac{2}{3}\,;\,4\right\}$ ; $S = \{0\,;\,5\}$ ; $S = \left\{-\frac{1}{2}\right\}$.

### Exercice 7 — Équations $x^2 = a$ <span class="etoiles">★</span>

Résoudre : $x^2 = 16$ ; $x^2 = -9$ ; $2x^2 = 10$ ; $(x + 1)^2 = 3$.

??? success "Correction"
    $\{-4\,;\,4\}$ ; $\varnothing$ ; $x^2 = 5$, $\left\{-\sqrt{5}\,;\,\sqrt{5}\right\}$ ; $x + 1 = \pm\sqrt{3}$, $\left\{-1 - \sqrt{3}\,;\,-1 + \sqrt{3}\right\}$.

### Exercice 8 — Factoriser pour résoudre <span class="etoiles">★★</span>

Résoudre : $x^2 - 6x = 0$ ; $4x^2 - 9 = 0$ ; $(x - 1)(x + 2) - (x - 1)(2x - 3) = 0$ ; $x^2 + 10x + 25 = 0$.

??? success "Correction"
    - $x(x - 6) = 0$ : $\{0\,;\,6\}$.
    - $(2x - 3)(2x + 3) = 0$ : $\left\{-\frac{3}{2}\,;\,\frac{3}{2}\right\}$.
    - $(x - 1)\big[(x + 2) - (2x - 3)\big] = (x - 1)(-x + 5) = 0$ : $\{1\,;\,5\}$.
    - $(x + 5)^2 = 0$ : $\{-5\}$.

### Exercice 9 — Deux carrés égaux <span class="etoiles">★★</span>

Résoudre $(2x - 1)^2 = (x + 3)^2$, puis $x^3 = 4x$.

??? success "Correction"
    $(2x - 1)^2 - (x + 3)^2 = 0 \iff (x - 4)(3x + 2) = 0$ : $S = \left\{-\frac{2}{3}\,;\,4\right\}$.

    $x^3 - 4x = 0 \iff x(x - 2)(x + 2) = 0$ : $S = \{-2\,;\,0\,;\,2\}$. (Diviser par $x$ aurait fait perdre la solution $0$.)

### Exercice 10 — Un rectangle <span class="etoiles">★★</span>

Un rectangle a une longueur qui dépasse sa largeur de $3$ cm, et une aire de $40$ cm².

1. On note $x$ la largeur. Montrer que $x^2 + 3x - 40 = 0$.
2. Vérifier que $x^2 + 3x - 40 = (x + 8)(x - 5)$ et en déduire les dimensions du rectangle.

??? success "Correction"
    1. $x(x + 3) = 40 \iff x^2 + 3x - 40 = 0$.
    2. $(x + 8)(x - 5) = x^2 - 5x + 8x - 40$. ✓ Solutions $-8$ et $5$ ; une largeur est positive : $5$ cm sur $8$ cm.

### Exercice 11 — Problèmes <span class="etoiles">★★★</span>

1. Si l'on augmente de $2$ cm le côté d'un carré, son aire augmente de $24$ cm². Quel est son côté ?
2. Résoudre $(x - 1)^2 = 2x - 2$.

??? success "Correction"
    1. $(c + 2)^2 - c^2 = 24 \iff 4c + 4 = 24 \iff c = 5$ cm.
    2. $(x - 1)^2 - 2(x - 1) = 0 \iff (x - 1)(x - 3) = 0$ : $S = \{1\,;\,3\}$.

---

## Thème 3 — Équations quotient

*Méthode associée : [Méthode 2](methodes.md#methode-2-resoudre-une-equation-quotient).*

### Exercice 12 — Quotients nuls <span class="etoiles">★</span>

Résoudre : $\dfrac{x - 5}{x + 1} = 0$ ; $\dfrac{x^2 - 9}{x - 3} = 0$ ; $\dfrac{2x}{x^2 + 1} = 0$.

??? success "Correction"
    - Interdite : $-1$. $S = \{5\}$.
    - Interdite : $3$. $x^2 - 9 = 0 \iff x = \pm 3$ ; on exclut $3$ : $S = \{-3\}$.
    - Pas de valeur interdite ($x^2 + 1 > 0$). $S = \{0\}$.

### Exercice 13 — Produits en croix <span class="etoiles">★★</span>

Résoudre $\dfrac{3}{x - 2} = \dfrac{5}{x + 1}$.

??? success "Correction"
    Interdites : $2$ et $-1$. Pour $x$ non interdit : $3(x + 1) = 5(x - 2) \iff 3x + 3 = 5x - 10 \iff x = \frac{13}{2}$, qui n'est pas interdit. $S = \left\{\frac{13}{2}\right\}$.

### Exercice 14 — Attention aux valeurs interdites <span class="etoiles">★★</span>

Résoudre $\dfrac{x + 3}{x - 1} = 2$, puis $\dfrac{x}{x - 2} = \dfrac{2}{x - 2}$.

??? success "Correction"
    - Interdite : $1$. $x + 3 = 2(x - 1) \iff x = 5$. $S = \{5\}$.
    - Interdite : $2$. On obtiendrait $x = 2$, qui est interdit : $S = \varnothing$.

### Exercice 15 — Résistances en parallèle <span class="etoiles">★★★</span>

Deux résistances $R_1$ et $R_2$ montées en parallèle ont une résistance équivalente $R$ telle que $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$. On a $R = 2\ \Omega$ et $R_1 = 3\ \Omega$. Calculer $R_2$.

??? success "Correction"
    $\frac{1}{R_2} = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$, donc $R_2 = 6\ \Omega$.

---

## Thème 4 — Inéquations du premier degré

*Méthode associée : [Méthode 3](methodes.md#methode-3-resoudre-une-inequation-du-premier-degre).*

### Exercice 16 — Résoudre <span class="etoiles">★</span>

Résoudre et donner les solutions sous forme d'intervalle : $3x - 5 \geq 7$ ; $-2x + 1 < 9$ ; $5 - x \leq 2x + 11$ ; $\dfrac{x}{2} - 1 > \dfrac{x}{3}$.

??? success "Correction"
    $[4\,;\,+\infty[$ ; $-2x < 8 \iff x > -4$ : $]-4\,;\,+\infty[$ ; $-3x \leq 6 \iff x \geq -2$ : $[-2\,;\,+\infty[$ ; en multipliant par $6$ : $3x - 6 > 2x \iff x > 6$ : $]6\,;\,+\infty[$.

### Exercice 17 — Plus petit entier <span class="etoiles">★</span>

Quel est le plus petit entier solution de $7x - 3 > 4x + 8$ ?

??? success "Correction"
    $3x > 11 \iff x > \frac{11}{3} \approx 3{,}67$. Le plus petit entier solution est $4$.

### Exercice 18 — Comparer deux forfaits <span class="etoiles">★★</span>

Un forfait A coûte $20$ € par mois plus $0{,}15$ € par minute ; un forfait B coûte $0{,}25$ € par minute. Pour quelles durées mensuelles le forfait B est-il le moins cher ?

??? success "Correction"
    $0{,}25t < 20 + 0{,}15t \iff 0{,}1t < 20 \iff t < 200$. B est moins cher pour moins de $200$ minutes par mois.

### Exercice 19 — Double inégalité <span class="etoiles">★★</span>

Déterminer les réels $x$ tels que $-3 \leq 2x + 1 \leq 5$, puis tels que $-1 < 4 - 3x < 7$.

??? success "Correction"
    $-4 \leq 2x \leq 4 \iff -2 \leq x \leq 2$ : $[-2\,;\,2]$.

    $-5 < -3x < 3 \iff -1 < x < \frac{5}{3}$ (on divise par $-3$, les sens changent) : $\left]-1\,;\,\frac{5}{3}\right[$.

---

## Thème 5 — Tableaux de signes et approfondissement

*Méthodes associées : [Méthode 4](methodes.md#methode-4-dresser-un-tableau-de-signes) et [Méthode 5](methodes.md#methode-5-resoudre-une-inequation-produit-ou-quotient).*

### Exercice 20 — Signe d'expressions affines <span class="etoiles">★</span>

Donner le signe, selon $x$, de $3x - 6$, de $-2x + 5$ et de $4 - \frac{x}{2}$.

??? success "Correction"
    - $3x - 6$ : négatif sur $]-\infty\,;\,2[$, nul en $2$, positif sur $]2\,;\,+\infty[$.
    - $-2x + 5$ : positif sur $\left]-\infty\,;\,\frac{5}{2}\right[$, négatif sur $\left]\frac{5}{2}\,;\,+\infty\right[$.
    - $4 - \frac{x}{2}$ : positif sur $]-\infty\,;\,8[$, négatif sur $]8\,;\,+\infty[$.

### Exercice 21 — Un premier tableau <span class="etoiles">★</span>

Dresser le tableau de signes de $(x + 1)(x - 4)$.

??? success "Correction"
    | $x$ | $-\infty$ | | $-1$ | | $4$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $x + 1$ | | $-$ | $0$ | $+$ | | $+$ | |
    | $x - 4$ | | $-$ | | $-$ | $0$ | $+$ | |
    | produit | | $+$ | $0$ | $-$ | $0$ | $+$ | |

### Exercice 22 — Inéquations produit <span class="etoiles">★★</span>

Résoudre : $(2 - x)(x + 3) > 0$ ; $(x - 1)^2 \geq 0$ ; $x^2 < 9$.

??? success "Correction"
    - $2 - x$ s'annule en $2$ (positif avant), $x + 3$ en $-3$ (positif après) : le produit est positif entre les deux. $S = ]-3\,;\,2[$.
    - Un carré est toujours positif : $S = \mathbb{R}$.
    - $x^2 - 9 < 0 \iff (x - 3)(x + 3) < 0$ : $S = ]-3\,;\,3[$.

### Exercice 23 — Inéquations quotient <span class="etoiles">★★</span>

Résoudre $\dfrac{x - 2}{x + 5} \leq 0$ et $\dfrac{3x + 1}{2 - x} > 0$.

??? success "Correction"
    - Zéros : $2$ (numérateur), $-5$ (interdit). Le quotient est négatif entre $-5$ et $2$ : $S = ]-5\,;\,2]$.
    - $3x + 1$ s'annule en $-\frac{1}{3}$ (positif après) ; $2 - x$ en $2$ (positif avant, interdit). Le quotient est positif entre les deux : $S = \left]-\frac{1}{3}\,;\,2\right[$.

### Exercice 24 — Factoriser d'abord <span class="etoiles">★★</span>

Résoudre $x^2 - 4x \geq 0$, puis $(x + 1)^2 < 4$.

??? success "Correction"
    - $x(x - 4) \geq 0$ : positif à l'extérieur des racines. $S = ]-\infty\,;\,0] \cup [4\,;\,+\infty[$.
    - $(x + 1)^2 - 4 < 0 \iff (x - 1)(x + 3) < 0$ : $S = ]-3\,;\,1[$.

### Exercice 25 — Se ramener à un quotient <span class="etoiles">★★</span>

Résoudre $\dfrac{x + 1}{x - 2} \geq 2$.

??? success "Correction"
    Interdite : $2$. $\frac{x + 1}{x - 2} - 2 \geq 0 \iff \frac{x + 1 - 2x + 4}{x - 2} \geq 0 \iff \frac{-x + 5}{x - 2} \geq 0$.

    $-x + 5$ s'annule en $5$ (positif avant), $x - 2$ en $2$ (positif après) : le quotient est positif entre $2$ et $5$. $S = ]2\,;\,5]$.

### Exercice 26 — Comparer $x$ et son inverse <span class="etoiles">★★★</span>

Résoudre l'inéquation $\dfrac{1}{x} \geq x$.

??? success "Correction"
    Interdite : $0$. $\frac{1}{x} - x \geq 0 \iff \frac{1 - x^2}{x} \geq 0 \iff \frac{(1 - x)(1 + x)}{x} \geq 0$.

    | $x$ | $-\infty$ | | $-1$ | | $0$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|---|---|
    | $1 - x$ | | $+$ | | $+$ | | $+$ | $0$ | $-$ | |
    | $1 + x$ | | $-$ | $0$ | $+$ | | $+$ | | $+$ | |
    | $x$ | | $-$ | | $-$ | $0$ | $+$ | | $+$ | |
    | quotient | | $+$ | $0$ | $-$ | $\parallel$ | $+$ | $0$ | $-$ | |

    $S = ]-\infty\,;\,-1] \cup ]0\,;\,1]$.

### Exercice 27 — Un bénéfice positif <span class="etoiles">★★★</span>

Une entreprise fabrique $x$ centaines d'objets ($0 \leq x \leq 10$). Son bénéfice, en milliers d'euros, est $B(x) = -x^2 + 10x - 16$.

1. Vérifier que $B(x) = -(x - 2)(x - 8)$.
2. Pour quelles productions l'entreprise est-elle bénéficiaire ($B(x) \geq 0$) ?

??? success "Correction"
    1. $-(x - 2)(x - 8) = -(x^2 - 10x + 16) = -x^2 + 10x - 16$. ✓
    2. $(x - 2)(x - 8)$ est négatif entre $2$ et $8$, donc $B(x) \geq 0 \iff x \in [2\,;\,8]$ : entre $200$ et $800$ objets.

### Exercice 28 — Inéquation du premier degré en Python <span class="etoiles">★★★</span>

Écrire une fonction `resoudre(a, b)` qui affiche l'ensemble des solutions de l'inéquation $ax + b > 0$, en traitant tous les cas ($a > 0$, $a < 0$, $a = 0$).

??? success "Correction"
    ```python
    def resoudre(a, b):
        if a > 0:
            print("S = ]", -b / a, "; +inf[")
        elif a < 0:
            print("S = ]-inf ;", -b / a, "[")
        else:
            if b > 0:
                print("S = R")
            else:
                print("S = ensemble vide")

    resoudre(2, -6)    # S = ] 3.0 ; +inf[
    resoudre(-1, 4)    # S = ]-inf ; 4.0 [
    resoudre(0, -1)    # S = ensemble vide
    ```
