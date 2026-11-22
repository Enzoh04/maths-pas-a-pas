# Exercices corrigés — Dérivation

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Sauf mention « calculatrice », tout se fait à la main.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Taux de variation et nombre dérivé | 1 à 6 |
| 2. Tangentes | 7 à 12 |
| 3. Calcul de dérivées | 13 à 19 |
| 4. Approximation linéaire | 20 à 23 |
| 5. Approfondissement | 24 à 28 |

---

## Thème 1 — Taux de variation et nombre dérivé

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-un-nombre-derive-avec-la-definition).*

### Exercice 1 — Un taux de variation <span class="etoiles">★</span>

Calculer le taux de variation de $f(x) = x^2$ entre $1$ et $3$, puis entre $-2$ et $2$. Interpréter le second résultat.

??? success "Correction"
    $\frac{9 - 1}{3 - 1} = 4$. $\frac{4 - 4}{2 - (-2)} = 0$ : la sécante passant par les points d'abscisses $-2$ et $2$ est horizontale (la parabole est symétrique par rapport à l'axe des ordonnées).

### Exercice 2 — Par la définition <span class="etoiles">★</span>

Soit $f(x) = 2x^2 - x$. Calculer $f'(1)$ à l'aide de la définition.

??? success "Correction"
    $\dfrac{f(1 + h) - f(1)}{h} = \dfrac{2(1 + 2h + h^2) - (1 + h) - 1}{h} = \dfrac{3h + 2h^2}{h} = 3 + 2h$, qui tend vers $3$. Donc $f'(1) = 3$.

### Exercice 3 — L'inverse en $2$ <span class="etoiles">★</span>

Calculer $f'(2)$ pour $f(x) = \dfrac{1}{x}$ à l'aide de la définition.

??? success "Correction"
    $\dfrac{\frac{1}{2 + h} - \frac{1}{2}}{h} = \dfrac{2 - (2 + h)}{2h(2 + h)} = \dfrac{-1}{2(2 + h)}$, qui tend vers $-\frac{1}{4}$.

### Exercice 4 — Le cube <span class="etoiles">★★</span>

Montrer, à l'aide de la définition, que la fonction cube est dérivable en tout réel $a$, de nombre dérivé $3a^2$.

??? success "Correction"
    $(a + h)^3 = a^3 + 3a^2h + 3ah^2 + h^3$, donc le taux vaut $3a^2 + 3ah + h^2$, qui tend vers $3a^2$.

### Exercice 5 — La racine carrée en $4$ <span class="etoiles">★★</span>

Calculer $f'(4)$ pour $f(x) = \sqrt{x}$ à l'aide de la définition, en multipliant par la quantité conjuguée.

??? success "Correction"
    $\dfrac{\sqrt{4 + h} - 2}{h} = \dfrac{(4 + h) - 4}{h(\sqrt{4 + h} + 2)} = \dfrac{1}{\sqrt{4 + h} + 2}$, qui tend vers $\frac{1}{4}$.

### Exercice 6 — La valeur absolue <span class="etoiles">★★</span>

Soit $f(x) = |x|$.

1. Calculer le taux de variation de $f$ entre $0$ et $h$ pour $h > 0$, puis pour $h < 0$.
2. $f$ est-elle dérivable en $0$ ? En $3$ ? En $-3$ ?

??? success "Correction"
    **1.** $\frac{|h|}{h}$ vaut $1$ si $h > 0$ et $-1$ si $h < 0$.

    **2.** En $0$ : non, le taux ne se rapproche pas d'un nombre unique. En $3$ : pour $h$ petit, $|3 + h| = 3 + h$, le taux vaut $1$, donc $f'(3) = 1$. En $-3$ : $|-3 + h| = 3 - h$, le taux vaut $-1$, donc $f'(-3) = -1$.

---

## Thème 2 — Tangentes

*Méthodes associées : [Méthode 2](methodes.md#methode-2-determiner-lequation-dune-tangente), [Méthode 3](methodes.md#methode-3-lire-un-nombre-derive-sur-un-graphique) et [Méthode 6](methodes.md#methode-6-resoudre-un-probleme-de-tangente).*

### Exercice 7 — Tangente à la parabole <span class="etoiles">★</span>

Déterminer l'équation de la tangente à la courbe de $f(x) = x^2$ au point d'abscisse $3$.

??? success "Correction"
    $f(3) = 9$, $f'(3) = 6$ : $y = 6(x - 3) + 9 = 6x - 9$.

### Exercice 8 — Lecture graphique <span class="etoiles">★</span>

On sait que la courbe d'une fonction $f$ passe par $A(-1\,;\,3)$ et que la tangente en $A$ passe aussi par $B(1\,;\,7)$. On sait aussi que la courbe admet une tangente horizontale au point d'abscisse $2$.

1. Déterminer $f(-1)$ et $f'(-1)$.
2. Déterminer l'équation de la tangente en $A$.
3. Que vaut $f'(2)$ ?

??? success "Correction"
    **1.** $f(-1) = 3$ et $f'(-1) = \frac{7 - 3}{1 - (-1)} = 2$.

    **2.** $y = 2(x + 1) + 3 = 2x + 5$.

    **3.** $f'(2) = 0$.

### Exercice 9 — Tangente à l'hyperbole <span class="etoiles">★</span>

Déterminer l'équation de la tangente à la courbe de $f(x) = \dfrac{1}{x}$ au point d'abscisse $2$.

??? success "Correction"
    $f(2) = \frac{1}{2}$, $f'(2) = -\frac{1}{4}$ : $y = -\frac{1}{4}(x - 2) + \frac{1}{2} = -\frac{1}{4}x + 1$.

### Exercice 10 — Tangentes horizontales <span class="etoiles">★★</span>

Déterminer les points de la courbe de $f(x) = x^3 - 12x$ où la tangente est horizontale.

??? success "Correction"
    $f'(x) = 3x^2 - 12 = 0 \iff x^2 = 4 \iff x = \pm 2$. Points $(2\,;\,-16)$ et $(-2\,;\,16)$.

### Exercice 11 — Tangente parallèle à une droite <span class="etoiles">★★</span>

Soit $f(x) = x^2 + x$. En quel point la tangente à la courbe est-elle parallèle à la droite d'équation $y = 4x$ ? Donner l'équation de cette tangente.

??? success "Correction"
    $f'(x) = 2x + 1 = 4 \iff x = \frac{3}{2}$. $f\left(\frac{3}{2}\right) = \frac{9}{4} + \frac{3}{2} = \frac{15}{4}$. Tangente : $y = 4\left(x - \frac{3}{2}\right) + \frac{15}{4} = 4x - \frac{9}{4}$.

### Exercice 12 — Tangentes issues d'un point <span class="etoiles">★★★</span>

Déterminer les tangentes à la parabole d'équation $y = x^2$ qui passent par le point $P(1\,;\,-3)$.

??? success "Correction"
    La tangente au point d'abscisse $a$ est $y = 2ax - a^2$. Elle passe par $P$ si et seulement si $-3 = 2a - a^2$, soit $a^2 - 2a - 3 = 0$, soit $a = 3$ ou $a = -1$. Tangentes : $y = 6x - 9$ et $y = -2x - 1$.

---

## Thème 3 — Calcul de dérivées

*Méthode associée : [Méthode 4](methodes.md#methode-4-calculer-une-fonction-derivee).*

### Exercice 13 — Polynômes <span class="etoiles">★</span>

Dériver : $f(x) = 3x^4 - 5x^2 + 2x - 7$ ; $g(x) = \dfrac{x^3}{3} - \dfrac{x^2}{2} + 1$ ; $h(x) = (x - 1)^2$.

??? success "Correction"
    $f'(x) = 12x^3 - 10x + 2$ ; $g'(x) = x^2 - x$ ; $h(x) = x^2 - 2x + 1$ donc $h'(x) = 2x - 2$.

### Exercice 14 — Produits <span class="etoiles">★</span>

Dériver : $f(x) = (x^2 + 1)(3x - 2)$ et $g(x) = x^2\sqrt{x}$ sur $]0\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = 2x(3x - 2) + 3(x^2 + 1) = 9x^2 - 4x + 3$.

    $g'(x) = 2x\sqrt{x} + x^2 \times \frac{1}{2\sqrt{x}} = 2x\sqrt{x} + \frac{x\sqrt{x}}{2} = \frac{5}{2}x\sqrt{x}$.

### Exercice 15 — Quotients <span class="etoiles">★★</span>

Dériver sur l'intervalle indiqué : $f(x) = \dfrac{2x + 1}{x - 3}$ sur $]3\,;\,+\infty[$ ; $g(x) = \dfrac{x^2}{x + 1}$ sur $]-1\,;\,+\infty[$.

??? success "Correction"
    $f'(x) = \dfrac{2(x - 3) - (2x + 1)}{(x - 3)^2} = \dfrac{-7}{(x - 3)^2}$.

    $g'(x) = \dfrac{2x(x + 1) - x^2}{(x + 1)^2} = \dfrac{x^2 + 2x}{(x + 1)^2}$.

### Exercice 16 — Inverses <span class="etoiles">★</span>

Dériver sur $\mathbb{R}$ : $f(x) = \dfrac{1}{x^2 + x + 1}$ (on justifiera que le dénominateur ne s'annule pas).

??? success "Correction"
    $x^2 + x + 1$ a pour discriminant $-3 < 0$ et $a = 1 > 0$ : il est toujours strictement positif. $f'(x) = -\dfrac{2x + 1}{(x^2 + x + 1)^2}$.

### Exercice 17 — Avec $g(ax + b)$ <span class="etoiles">★★</span>

Dériver : $f(x) = \sqrt{3x + 1}$ sur $\left]-\frac{1}{3}\,;\,+\infty\right[$ ; $g(x) = (2x - 5)^3$ ; $h(x) = \dfrac{1}{4 - x}$ sur $]-\infty\,;\,4[$.

??? success "Correction"
    $f'(x) = \dfrac{3}{2\sqrt{3x + 1}}$ ; $g'(x) = 2 \times 3(2x - 5)^2 = 6(2x - 5)^2$ ; $h'(x) = -1 \times \left(-\dfrac{1}{(4 - x)^2}\right) = \dfrac{1}{(4 - x)^2}$.

### Exercice 18 — Un produit avec une racine <span class="etoiles">★★</span>

Dériver $f(x) = (x + 1)\sqrt{x}$ sur $]0\,;\,+\infty[$ et écrire le résultat sous la forme d'un seul quotient.

??? success "Correction"
    $f'(x) = \sqrt{x} + \dfrac{x + 1}{2\sqrt{x}} = \dfrac{2x + x + 1}{2\sqrt{x}} = \dfrac{3x + 1}{2\sqrt{x}}$.

### Exercice 19 — Trouver l'erreur <span class="etoiles">★★</span>

Un élève écrit : « $f(x) = (x^2 + 1)(x - 2)$, donc $f'(x) = 2x \times 1 = 2x$. » Expliquer son erreur et corriger. Vérifier en développant $f(x)$ avant de dériver.

??? success "Correction"
    Il a multiplié les dérivées, alors que $(uv)' = u'v + uv'$. Correct : $f'(x) = 2x(x - 2) + (x^2 + 1) = 3x^2 - 4x + 1$. Vérification : $f(x) = x^3 - 2x^2 + x - 2$, donc $f'(x) = 3x^2 - 4x + 1$.

---

## Thème 4 — Approximation linéaire

*Méthode associée : [Méthode 5](methodes.md#methode-5-utiliser-lapproximation-lineaire).*

### Exercice 20 — Racine carrée <span class="etoiles">★</span>

Montrer que pour $h$ proche de $0$, $\sqrt{1 + h} \approx 1 + \frac{h}{2}$. En déduire des valeurs approchées de $\sqrt{1{,}02}$ et de $\sqrt{0{,}96}$.

??? success "Correction"
    Avec $f(x) = \sqrt{x}$ en $a = 1$ : $f(1) = 1$, $f'(1) = \frac{1}{2}$. Donc $\sqrt{1{,}02} \approx 1{,}01$ et $\sqrt{0{,}96} \approx 1 - 0{,}02 = 0{,}98$ (valeurs exactes : $1{,}00995\ldots$ et $0{,}97979\ldots$).

### Exercice 21 — Le carré <span class="etoiles">★</span>

Montrer que $(1 + h)^2 \approx 1 + 2h$ pour $h$ proche de $0$, et comparer avec la valeur exacte pour $h = 0{,}01$. Quelle est l'erreur commise ?

??? success "Correction"
    $f(x) = x^2$, $f(1) = 1$, $f'(1) = 2$. Pour $h = 0{,}01$ : approximation $1{,}02$, valeur exacte $1{,}0201$. L'erreur est $h^2 = 0{,}0001$, bien plus petite que $h$.

### Exercice 22 — L'inverse <span class="etoiles">★</span>

Donner une valeur approchée de $\dfrac{1}{0{,}98}$ à l'aide d'une approximation linéaire.

??? success "Correction"
    $f(x) = \frac{1}{x}$, $a = 1$, $h = -0{,}02$ : $\frac{1}{0{,}98} \approx 1 - (-0{,}02) = 1{,}02$ (valeur exacte : $1{,}0204\ldots$).

### Exercice 23 — Une erreur de mesure <span class="etoiles">★★</span>

Le volume d'une boule de rayon $r$ est $V(r) = \frac{4}{3}\pi r^3$.

1. Calculer $V'(r)$.
2. On mesure un rayon de $10$ cm avec une erreur de $0{,}1$ cm. Estimer l'erreur commise sur le volume.
3. Exprimer cette erreur en pourcentage du volume.

??? success "Correction"
    **1.** $V'(r) = 4\pi r^2$.

    **2.** $V(10 + h) - V(10) \approx V'(10) \times h = 400\pi \times 0{,}1 = 40\pi \approx 126$ cm³.

    **3.** $\frac{40\pi}{\frac{4}{3}\pi \times 1000} = \frac{40 \times 3}{4000} = 0{,}03$, soit $3\,\%$ : une erreur de $1\,\%$ sur le rayon donne environ $3\,\%$ d'erreur sur le volume.

---

## Thème 5 — Approfondissement

### Exercice 24 — La dérivée de $x^n$ <span class="etoiles">★★</span>

1. En écrivant $x^4 = x^3 \times x$, retrouver la dérivée de $x \mapsto x^4$.
2. Faire de même pour $x^5$, puis expliquer pourquoi la dérivée de $x^n$ est $nx^{n-1}$.

??? success "Correction"
    **1.** $(x^3 \times x)' = 3x^2 \times x + x^3 \times 1 = 4x^3$.

    **2.** $(x^4 \times x)' = 4x^3 \times x + x^4 = 5x^4$. À chaque étape, si $(x^{n-1})' = (n - 1)x^{n-2}$, alors $(x^{n-1} \times x)' = (n - 1)x^{n-2} \times x + x^{n-1} = nx^{n-1}$. *C'est le principe du raisonnement par récurrence, formalisé en Terminale.*

### Exercice 25 — Dérivable implique continue <span class="etoiles">★★</span>

Soit $f$ dérivable en $a$. Montrer que $f(a + h)$ tend vers $f(a)$ quand $h$ tend vers $0$. La réciproque est-elle vraie ?

??? success "Correction"
    $f(a + h) - f(a) = h \times \frac{f(a + h) - f(a)}{h}$ tend vers $0 \times f'(a) = 0$. La réciproque est fausse : $|x|$ et $\sqrt{x}$ sont continues en $0$ sans y être dérivables.

### Exercice 26 — Une propriété de la parabole <span class="etoiles">★★★</span>

Soit $a \neq 0$. Montrer que la tangente à la parabole $y = x^2$ au point d'abscisse $a$ coupe l'axe des abscisses au point d'abscisse $\frac{a}{2}$. En déduire une construction de la tangente à la règle.

??? success "Correction"
    La tangente a pour équation $y = 2ax - a^2$. Elle coupe l'axe des abscisses quand $2ax = a^2$, soit $x = \frac{a}{2}$. Pour tracer la tangente en $A(a\,;\,a^2)$, il suffit de relier $A$ au point $\left(\frac{a}{2}\,;\,0\right)$.

### Exercice 27 — Approcher un nombre dérivé en Python <span class="etoiles">★★</span>

1. Écrire une fonction Python `taux(f, a, h)` qui renvoie le taux de variation de $f$ entre $a$ et $a + h$.
2. L'utiliser avec $f(x) = x^3$, $a = 2$ et $h = 0{,}1$, puis $0{,}01$, puis $0{,}001$. Vers quelle valeur les résultats semblent-ils se rapprocher ? Pourquoi ?

??? success "Correction"
    ```python
    def taux(f, a, h):
        return (f(a + h) - f(a)) / h

    def cube(x):
        return x**3

    for h in [0.1, 0.01, 0.001]:
        print(h, taux(cube, 2, h))
    ```

    On obtient environ $12{,}61$ ; $12{,}06$ ; $12{,}006$. Les valeurs se rapprochent de $f'(2) = 3 \times 4 = 12$ : le taux vaut exactement $12 + 6h + h^2$ (exercice 4).

### Exercice 28 — La méthode de Newton <span class="etoiles">★★★</span>

On cherche une valeur approchée de $\sqrt{2}$, solution positive de $x^2 - 2 = 0$. On pose $f(x) = x^2 - 2$.

1. Montrer que la tangente à la courbe de $f$ au point d'abscisse $u$ ($u > 0$) coupe l'axe des abscisses au point d'abscisse $\dfrac{u}{2} + \dfrac{1}{u}$.
2. On part de $u_0 = 1$ et l'on pose $u_{n+1} = \dfrac{u_n}{2} + \dfrac{1}{u_n}$. Calculer $u_1$ et $u_2$ sous forme de fractions.
3. Écrire un programme Python qui affiche les cinq premiers termes. Que constate-t-on ?

??? success "Correction"
    **1.** Tangente : $y = 2u(x - u) + u^2 - 2$. Elle coupe l'axe quand $2u(x - u) = 2 - u^2$, soit $x = u + \frac{2 - u^2}{2u} = \frac{u}{2} + \frac{1}{u}$.

    **2.** $u_1 = \frac{1}{2} + 1 = \frac{3}{2}$, $u_2 = \frac{3}{4} + \frac{2}{3} = \frac{17}{12}$.

    **3.**

    ```python
    u = 1
    for n in range(5):
        u = u / 2 + 1 / u
        print(u)
    ```

    On obtient $1{,}5$ ; $1{,}41666\ldots$ ; $1{,}4142156\ldots$ ; $1{,}41421356\ldots$ : le nombre de décimales exactes de $\sqrt{2} = 1{,}41421356\ldots$ double environ à chaque étape. Cette méthode était déjà connue des Babyloniens.
