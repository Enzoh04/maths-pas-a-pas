# Exercices corrigés — Variations et courbes représentatives

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Sauf mention « calculatrice », tout se fait à la main.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Parité | 1 à 5 |
| 2. Sens de variation | 6 à 12 |
| 3. Extremums | 13 à 17 |
| 4. Inégalités et position relative | 18 à 23 |
| 5. Optimisation | 24 à 28 |

---

## Thème 1 — Parité

*Méthode associée : [Méthode 1](methodes.md#methode-1-etudier-la-parite-dune-fonction).*

### Exercice 1 — Paire, impaire, ou ni l'un ni l'autre ? <span class="etoiles">★</span>

Étudier la parité de : $f_1(x) = x^4 - x^2$ ; $f_2(x) = x^3 + x$ ; $f_3(x) = x^2 + x$ ; $f_4(x) = \dfrac{1}{x}$ sur $\mathbb{R}^*$ ; $f_5(x) = |x| + 1$ ; $f_6(x) = \sqrt{x}$ sur $[0\,;\,+\infty[$.

??? success "Correction"
    $f_1$ paire ; $f_2$ impaire ; $f_3$ ni l'un ni l'autre ($f_3(1) = 2$, $f_3(-1) = 0$) ; $f_4$ impaire ; $f_5$ paire ; $f_6$ ni l'un ni l'autre : son ensemble de définition n'est pas symétrique.

### Exercice 2 — Avec une valeur absolue <span class="etoiles">★</span>

Montrer que $f(x) = x\,|x|$ est impaire sur $\mathbb{R}$.

??? success "Correction"
    $f(-x) = (-x)\,|-x| = -x\,|x| = -f(x)$, car $|-x| = |x|$.

### Exercice 3 — Compléter une courbe <span class="etoiles">★</span>

Une fonction $f$ est paire, et l'on sait que $f(2) = 5$, $f'(2) = 3$ et que $f$ est croissante sur $[0\,;\,4]$. Que valent $f(-2)$ ? Quel est le sens de variation de $f$ sur $[-4\,;\,0]$ ? Même question si $f$ est impaire.

??? success "Correction"
    **Paire** : $f(-2) = 5$, et $f$ est décroissante sur $[-4\,;\,0]$ (symétrie d'axe $(Oy)$).

    **Impaire** : $f(-2) = -5$, et $f$ est croissante sur $[-4\,;\,0]$ (symétrie de centre $O$).

### Exercice 4 — Produits <span class="etoiles">★★</span>

Soit $f$ et $g$ deux fonctions définies sur $\mathbb{R}$. Montrer que si $f$ et $g$ sont impaires, alors $fg$ est paire. Que dire si $f$ est paire et $g$ impaire ?

??? success "Correction"
    $(fg)(-x) = f(-x)\,g(-x) = (-f(x))(-g(x)) = f(x)\,g(x)$ : paire. Si $f$ est paire et $g$ impaire : $(fg)(-x) = f(x)(-g(x)) = -(fg)(x)$ : impaire. *Comme pour les signes : impair × impair = pair.*

### Exercice 5 — Dérivée d'une fonction paire <span class="etoiles">★★★</span>

Soit $f$ une fonction paire et dérivable sur $\mathbb{R}$. En dérivant les deux membres de l'égalité $f(-x) = f(x)$ (on utilisera la dérivée de $x \mapsto g(ax + b)$), montrer que $f'$ est impaire. En déduire que $f'(0) = 0$.

??? success "Correction"
    La dérivée de $x \mapsto f(-x)$ est $-f'(-x)$. En dérivant $f(-x) = f(x)$, on obtient $-f'(-x) = f'(x)$, soit $f'(-x) = -f'(x)$ : $f'$ est impaire. Avec $x = 0$ : $f'(0) = -f'(0)$, donc $f'(0) = 0$. *La tangente en $0$ à la courbe d'une fonction paire est horizontale.*

---

## Thème 2 — Sens de variation

*Méthode associée : [Méthode 2](methodes.md#methode-2-etudier-les-variations-dune-fonction).*

### Exercice 6 — Un polynôme de degré 3 <span class="etoiles">★</span>

Dresser le tableau de variations de $f(x) = 2x^3 - 3x^2 - 12x + 1$ sur $\mathbb{R}$.

??? success "Correction"
    $f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x - 2)(x + 1)$. $f$ est croissante sur $]-\infty\,;\,-1]$, décroissante sur $[-1\,;\,2]$, croissante sur $[2\,;\,+\infty[$. $f(-1) = -2 - 3 + 12 + 1 = 8$ et $f(2) = 16 - 12 - 24 + 1 = -19$.

### Exercice 7 — Un autre degré 3 <span class="etoiles">★</span>

Étudier les variations de $f(x) = x^3 - 6x^2 + 9x + 1$.

??? success "Correction"
    $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$. Croissante sur $]-\infty\,;\,1]$, décroissante sur $[1\,;\,3]$, croissante sur $[3\,;\,+\infty[$. $f(1) = 5$, $f(3) = 1$.

### Exercice 8 — Avec une racine carrée <span class="etoiles">★★</span>

Étudier les variations de $f(x) = x^2 - 4\sqrt{x}$ sur $]0\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = 2x - \dfrac{2}{\sqrt{x}} = \dfrac{2(x\sqrt{x} - 1)}{\sqrt{x}}$. Or $x\sqrt{x} \geq 1 \iff x \geq 1$ (la fonction $x \mapsto x\sqrt{x}$ est croissante et vaut $1$ en $1$). Donc $f$ est décroissante sur $]0\,;\,1]$, croissante sur $[1\,;\,+\infty[$, avec un minimum $f(1) = -3$.

### Exercice 9 — Un quotient <span class="etoiles">★</span>

Étudier les variations de $f(x) = \dfrac{x - 1}{x + 2}$ sur $]-2\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = \dfrac{(x + 2) - (x - 1)}{(x + 2)^2} = \dfrac{3}{(x + 2)^2} > 0$ : $f$ est strictement croissante sur $]-2\,;\,+\infty[$.

### Exercice 10 — Produit avec une racine <span class="etoiles">★★</span>

Étudier les variations de $f(x) = x\sqrt{x} - 3x$ sur $[0\,;\,+\infty[$ (on admet que $f$ est dérivable sur $]0\,;\,+\infty[$).

??? success "Correction"
    $f'(x) = \frac{3}{2}\sqrt{x} - 3 = \frac{3}{2}(\sqrt{x} - 2)$, négatif pour $x < 4$ et positif pour $x > 4$. $f$ est décroissante sur $[0\,;\,4]$, croissante sur $[4\,;\,+\infty[$, de minimum $f(4) = 8 - 12 = -4$.

### Exercice 11 — Degré 4 <span class="etoiles">★★</span>

Étudier les variations de $f(x) = x^4 - 2x^2$. Utiliser la parité pour vérifier le résultat.

??? success "Correction"
    $f'(x) = 4x^3 - 4x = 4x(x - 1)(x + 1)$.

    | $x$ | $-\infty$ | | $-1$ | | $0$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ | |
    | $f$ | | $\searrow$ | $-1$ | $\nearrow$ | $0$ | $\searrow$ | $-1$ | $\nearrow$ | |

    $f$ est paire : le tableau est bien symétrique par rapport à $0$.

### Exercice 12 — Lire la dérivée <span class="etoiles">★★</span>

On sait que la dérivée $f'$ d'une fonction $f$ définie sur $[-3\,;\,4]$ est négative sur $[-3\,;\,-1]$, positive sur $[-1\,;\,2]$ et négative sur $[2\,;\,4]$, et qu'elle ne s'annule qu'en $-1$ et $2$. On sait aussi que $f(-3) = 1$, $f(-1) = -2$, $f(2) = 4$, $f(4) = 0$.

1. Dresser le tableau de variations de $f$.
2. Quel est le maximum de $f$ sur $[-3\,;\,4]$ ? Son minimum ?
3. Combien de tangentes horizontales la courbe possède-t-elle ?

??? success "Correction"
    **1.** Décroissante de $1$ à $-2$ sur $[-3\,;\,-1]$, croissante jusqu'à $4$ sur $[-1\,;\,2]$, décroissante jusqu'à $0$ sur $[2\,;\,4]$.

    **2.** Maximum $4$ (en $2$), minimum $-2$ (en $-1$).

    **3.** Deux : aux points d'abscisses $-1$ et $2$.

---

## Thème 3 — Extremums

*Méthode associée : [Méthode 3](methodes.md#methode-3-determiner-les-extremums).*

### Exercice 13 — Local ou global ? <span class="etoiles">★</span>

Avec la fonction de l'exercice 6 sur l'intervalle $[-2\,;\,4]$ : calculer $f(-2)$ et $f(4)$, puis donner le maximum et le minimum de $f$ sur $[-2\,;\,4]$. Sont-ils atteints en des points où $f'$ s'annule ?

??? success "Correction"
    $f(-2) = -16 - 12 + 24 + 1 = -3$ et $f(4) = 128 - 48 - 48 + 1 = 33$. Maximum $33$ (en $4$, une borne, où $f'(4) = 36 \neq 0$) ; minimum $-19$ (en $2$, où $f'(2) = 0$). Le maximum local $8$ n'est pas le maximum sur l'intervalle.

### Exercice 14 — Une dérivée nulle sans extremum <span class="etoiles">★</span>

Soit $f(x) = x^3 + 1$. Calculer $f'(0)$. La fonction $f$ admet-elle un extremum en $0$ ?

??? success "Correction"
    $f'(x) = 3x^2$, $f'(0) = 0$. Mais $f' \geq 0$ sur $\mathbb{R}$ et ne s'annule qu'en $0$ : $f$ est strictement croissante, sans extremum. La dérivée s'annule sans changer de signe.

### Exercice 15 — Retrouver des coefficients <span class="etoiles">★★</span>

On cherche $f(x) = x^3 + ax + b$ telle que $f$ admette un maximum local égal à $3$ en $x = -1$.

1. Traduire les conditions, et en déduire $a$ et $b$.
2. Vérifier qu'il s'agit bien d'un maximum local, et trouver l'autre extremum local.

??? success "Correction"
    **1.** $f'(-1) = 3 + a = 0$ donc $a = -3$ ; $f(-1) = -1 + 3 + b = 3$ donc $b = 1$. $f(x) = x^3 - 3x + 1$.

    **2.** $f'(x) = 3(x - 1)(x + 1)$ : positive avant $-1$, négative entre $-1$ et $1$ : c'est bien un maximum local. Minimum local en $1$ : $f(1) = -1$.

### Exercice 16 — Un encadrement <span class="etoiles">★★</span>

Montrer que pour tout $x \in [-2\,;\,2]$, $-2 \leq x^3 - 3x \leq 2$.

??? success "Correction"
    D'après le cours, $f(x) = x^3 - 3x$ a un maximum local $2$ en $-1$ et un minimum local $-2$ en $1$. Aux bornes : $f(-2) = -2$ et $f(2) = 2$. Sur $[-2\,;\,2]$, le maximum vaut donc $2$ et le minimum $-2$.

### Exercice 17 — Un minimum <span class="etoiles">★★</span>

Déterminer le minimum de $f(x) = x^2 + \dfrac{16}{x}$ sur $]0\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = 2x - \dfrac{16}{x^2} = \dfrac{2(x^3 - 8)}{x^2}$, du signe de $x^3 - 8$ : négatif pour $x < 2$, positif pour $x > 2$ (la fonction cube est croissante). Minimum $f(2) = 4 + 8 = 12$.

---

## Thème 4 — Inégalités et position relative

*Méthode associée : [Méthode 4](methodes.md#methode-4-demontrer-une-inegalite-comparer-deux-courbes).*

### Exercice 18 — Une inégalité polynomiale <span class="etoiles">★★</span>

1. Vérifier que $x^3 - 3x + 2 = (x - 1)^2(x + 2)$.
2. En déduire que $x^3 \geq 3x - 2$ pour tout $x \geq -2$.
3. Retrouver ce résultat en étudiant les variations de $h(x) = x^3 - 3x + 2$ sur $[-2\,;\,+\infty[$.

??? success "Correction"
    **1.** $(x^2 - 2x + 1)(x + 2) = x^3 - 3x + 2$.

    **2.** $(x - 1)^2 \geq 0$ et $x + 2 \geq 0$ : le produit est positif ou nul.

    **3.** $h'(x) = 3(x - 1)(x + 1)$. Sur $[-2\,;\,+\infty[$ : $h$ croît de $h(-2) = 0$ à $h(-1) = 4$, décroît jusqu'à $h(1) = 0$, puis croît. Son minimum vaut $0$, donc $h \geq 0$.

### Exercice 19 — Inverse et droite <span class="etoiles">★★</span>

Montrer que pour tout $x > 0$, $\dfrac{1}{x} \geq 2 - x$, de deux façons : en étudiant une fonction, puis par un calcul algébrique. Interpréter graphiquement.

??? success "Correction"
    **Fonction.** $h(x) = \frac{1}{x} + x - 2$, $h'(x) = 1 - \frac{1}{x^2}$, négative sur $]0\,;\,1[$ et positive sur $]1\,;\,+\infty[$ : minimum $h(1) = 0$.

    **Algèbre.** $h(x) = \dfrac{1 + x^2 - 2x}{x} = \dfrac{(x - 1)^2}{x} \geq 0$.

    **Interprétation.** La droite $y = 2 - x$ est la tangente à l'hyperbole $y = \frac{1}{x}$ au point d'abscisse $1$, et l'hyperbole est au-dessus de cette tangente sur $]0\,;\,+\infty[$.

### Exercice 20 — Carré et racine carrée <span class="etoiles">★</span>

Comparer les courbes de $x \mapsto x^2$ et $x \mapsto \sqrt{x}$ sur $[0\,;\,+\infty[$.

??? success "Correction"
    $x^2 - \sqrt{x} = \sqrt{x}\,(x\sqrt{x} - 1)$. Pour $x > 0$, c'est du signe de $x\sqrt{x} - 1$, négatif sur $]0\,;\,1[$ et positif sur $]1\,;\,+\infty[$. La parabole est sous la courbe de la racine carrée sur $]0\,;\,1[$, au-dessus sur $]1\,;\,+\infty[$ ; elles se coupent en $(0\,;\,0)$ et $(1\,;\,1)$.

### Exercice 21 — Fonction et tangente <span class="etoiles">★★</span>

Soit $f(x) = x^3$ et $T$ sa tangente au point d'abscisse $1$.

1. Déterminer l'équation de $T$.
2. Étudier la position de la courbe par rapport à $T$ (utiliser l'exercice 18).

??? success "Correction"
    **1.** $f(1) = 1$, $f'(1) = 3$ : $T : y = 3x - 2$.

    **2.** $f(x) - (3x - 2) = (x - 1)^2(x + 2)$ : la courbe est au-dessus de $T$ sur $]-2\,;\,+\infty[$ (sauf en $1$, point de contact), et en dessous sur $]-\infty\,;\,-2[$.

### Exercice 22 — Une inégalité classique <span class="etoiles">★★</span>

Montrer que pour tout réel $x \neq 0$, $x^2 + \dfrac{1}{x^2} \geq 2$. Quand y a-t-il égalité ?

??? success "Correction"
    $x^2 + \frac{1}{x^2} - 2 = \left(x - \frac{1}{x}\right)^2 \geq 0$. Égalité si et seulement si $x = \frac{1}{x}$, soit $x = 1$ ou $x = -1$.

### Exercice 23 — Un encadrement <span class="etoiles">★★★</span>

Montrer que pour tout $x \geq 0$ :
$$x - x^2 \leq \frac{x}{1 + x} \leq x.$$
En déduire un encadrement de $\dfrac{0{,}1}{1{,}1}$.

??? success "Correction"
    **À droite.** $x - \dfrac{x}{1 + x} = \dfrac{x(1 + x) - x}{1 + x} = \dfrac{x^2}{1 + x} \geq 0$.

    **À gauche.** $\dfrac{x}{1 + x} - (x - x^2) = \dfrac{x - (x - x^2)(1 + x)}{1 + x} = \dfrac{x - x - x^2 + x^2 + x^3}{1 + x} = \dfrac{x^3}{1 + x} \geq 0$.

    **Application** avec $x = 0{,}1$ : $0{,}09 \leq \dfrac{0{,}1}{1{,}1} \leq 0{,}1$. (Valeur exacte : $0{,}0909\ldots$)

---

## Thème 5 — Optimisation

*Méthode associée : [Méthode 5](methodes.md#methode-5-resoudre-un-probleme-doptimisation).*

### Exercice 24 — Une boîte <span class="etoiles">★★</span>

Dans un carré de carton de $12$ cm de côté, on découpe aux quatre coins des carrés de côté $x$, puis l'on replie pour former une boîte sans couvercle. Quelle valeur de $x$ rend le volume maximal ? Quel est ce volume ?

??? success "Correction"
    $V(x) = x(12 - 2x)^2$ pour $0 < x < 6$. $V'(x) = (12 - 2x)^2 - 4x(12 - 2x) = (12 - 2x)(12 - 6x)$. Sur $]0\,;\,6[$, $12 - 2x > 0$ : $V'$ a le signe de $12 - 6x$, positif avant $2$, négatif après. Volume maximal pour $x = 2$ cm : $V(2) = 2 \times 64 = 128$ cm³.

### Exercice 25 — Une canette <span class="etoiles">★★★</span>

Une canette cylindrique doit contenir un volume $V = 16\pi$ cm³. On note $r$ son rayon et $h$ sa hauteur (en cm).

1. Exprimer $h$ en fonction de $r$, puis montrer que l'aire totale du métal (fond, couvercle et paroi) est $S(r) = 2\pi r^2 + \dfrac{32\pi}{r}$.
2. Déterminer le rayon qui minimise la quantité de métal, et la hauteur correspondante. Que remarque-t-on ?

??? success "Correction"
    **1.** $\pi r^2 h = 16\pi$ donne $h = \frac{16}{r^2}$. $S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{32\pi}{r}$.

    **2.** $S'(r) = 4\pi r - \dfrac{32\pi}{r^2} = \dfrac{4\pi(r^3 - 8)}{r^2}$, négatif pour $r < 2$, positif pour $r > 2$. Minimum pour $r = 2$ cm, et $h = 4$ cm : la hauteur est égale au **diamètre**. (Les canettes réelles sont plus hautes, pour des raisons de prise en main et de solidité.)

### Exercice 26 — Bénéfice maximal <span class="etoiles">★★</span>

Une entreprise produit $q$ tonnes ($0 \leq q \leq 6$) d'un produit vendu $15$ milliers d'euros la tonne, pour un coût $C(q) = q^3 - 6q^2 + 15q$ milliers d'euros. Déterminer la production qui maximise le bénéfice.

??? success "Correction"
    $B(q) = 15q - C(q) = -q^3 + 6q^2$, $B'(q) = -3q^2 + 12q = -3q(q - 4)$ : positive sur $]0\,;\,4[$, négative sur $]4\,;\,6[$. Bénéfice maximal pour $q = 4$ tonnes : $B(4) = -64 + 96 = 32$ milliers d'euros.

### Exercice 27 — Distance à une parabole <span class="etoiles">★★★</span>

Soit $\mathcal{P}$ la parabole d'équation $y = x^2$ et $A(0\,;\,2)$. Pour $M(x\,;\,x^2)$ sur $\mathcal{P}$, on note $d(x) = AM^2$ (repère orthonormé).

1. Montrer que $d(x) = x^4 - 3x^2 + 4$.
2. Étudier les variations de $d$ et en déduire la distance minimale entre $A$ et $\mathcal{P}$.

??? success "Correction"
    **1.** $AM^2 = x^2 + (x^2 - 2)^2 = x^2 + x^4 - 4x^2 + 4 = x^4 - 3x^2 + 4$.

    **2.** $d'(x) = 4x^3 - 6x = 2x(2x^2 - 3)$, qui s'annule en $0$ et $\pm\sqrt{\frac{3}{2}}$. $d$ décroît sur $\left]-\infty\,;\,-\sqrt{\frac{3}{2}}\right]$, croît sur $\left[-\sqrt{\frac{3}{2}}\,;\,0\right]$, décroît sur $\left[0\,;\,\sqrt{\frac{3}{2}}\right]$, puis croît. Minimum : $d\left(\sqrt{\frac{3}{2}}\right) = \frac{9}{4} - \frac{9}{2} + 4 = \frac{7}{4}$. La distance minimale vaut $\sqrt{\frac{7}{4}} = \frac{\sqrt{7}}{2}$. *Le point $O$, le plus « évident », n'est pas le plus proche : $AO = 2 > \frac{\sqrt{7}}{2} \approx 1{,}32$.*

### Exercice 28 — Chercher un minimum en Python <span class="etoiles">★★</span>

Écrire un programme Python qui calcule les valeurs de $d(x) = x^4 - 3x^2 + 4$ pour $x$ allant de $0$ à $2$ avec un pas de $0{,}001$, et affiche la plus petite valeur trouvée ainsi que l'abscisse correspondante. Comparer avec l'exercice 27.

??? success "Correction"
    ```python
    def d(x):
        return x**4 - 3*x**2 + 4

    meilleur_x = 0
    meilleur_d = d(0)
    for k in range(2001):
        x = k / 1000
        if d(x) < meilleur_d:
            meilleur_x = x
            meilleur_d = d(x)
    print(meilleur_x, meilleur_d)    # 1.225 et 1.75000...
    ```

    On trouve $x \approx 1{,}225$ et $d \approx 1{,}75$, conformément à $\sqrt{1{,}5} \approx 1{,}2247$ et $\frac{7}{4} = 1{,}75$. *La méthode par balayage donne une valeur approchée ; l'étude de la dérivée donne la valeur exacte.*
