# Exercices corrigés — Calcul numérique et algébrique

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Fractions et puissances | 1 à 6 |
| 2. Racines carrées | 7 à 11 |
| 3. Développer et factoriser | 12 à 17 |
| 4. Comparer et encadrer | 18 à 23 |
| 5. Formules et approfondissement | 24 à 28 |

---

## Thème 1 — Fractions et puissances

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-avec-des-puissances).*

### Exercice 1 — Fractions <span class="etoiles">★</span>

Calculer et donner le résultat sous forme irréductible :

$A = \dfrac{3}{4} - \dfrac{5}{6} + \dfrac{1}{3}$ ; $B = \dfrac{\frac{2}{3} + \frac{1}{2}}{\frac{5}{6} - \frac{1}{4}}$ ; $C = \dfrac{3}{5} \times \dfrac{10}{9} - \dfrac{1}{3}$.

??? success "Correction"
    $A = \frac{9 - 10 + 4}{12} = \frac{3}{12} = \frac{1}{4}$.

    $B = \dfrac{\frac{7}{6}}{\frac{7}{12}} = \frac{7}{6} \times \frac{12}{7} = 2$.

    $C = \frac{30}{45} - \frac{1}{3} = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}$.

### Exercice 2 — Puissances <span class="etoiles">★</span>

Écrire sous la forme $a^n$ : $2^5 \times 2^{-3}$ ; $\dfrac{7^4}{7^{-2}}$ ; $\left(5^{-2}\right)^3$ ; $3^4 \times 9^{-1}$ ; $\dfrac{10^{-3} \times 10^{5}}{10^{4}}$.

??? success "Correction"
    $2^2$ ; $7^6$ ; $5^{-6}$ ; $3^4 \times 3^{-2} = 3^2$ ; $10^{-2}$.

### Exercice 3 — Avec plusieurs bases <span class="etoiles">★</span>

Calculer $A = \dfrac{3^4 \times 9^{-1}}{27^{-1} \times 3^2}$ et $B = \dfrac{6^3 \times 2^{-2}}{3^2 \times 4}$.

??? success "Correction"
    $A = \dfrac{3^4 \times 3^{-2}}{3^{-3} \times 3^2} = 3^{2 - (-1)} = 3^3 = 27$.

    $B = \dfrac{2^3 \times 3^3 \times 2^{-2}}{3^2 \times 2^2} = 2^{3 - 2 - 2} \times 3^{3 - 2} = 2^{-1} \times 3 = \frac{3}{2}$.

### Exercice 4 — Notation scientifique <span class="etoiles">★</span>

Donner l'écriture scientifique de : $45\,000\,000$ ; $0{,}000\,307$ ; $12 \times 10^{-5}$ ; $0{,}08 \times 10^{7}$.

??? success "Correction"
    $4{,}5 \times 10^7$ ; $3{,}07 \times 10^{-4}$ ; $1{,}2 \times 10^{-4}$ ; $8 \times 10^{5}$.

### Exercice 5 — Calcul en physique <span class="etoiles">★★</span>

1. Calculer $\dfrac{6 \times 10^{-4} \times 5 \times 10^{7}}{1{,}5 \times 10^{2}}$.
2. La lumière parcourt environ $3 \times 10^8$ m par seconde, et une année compte environ $3{,}15 \times 10^7$ secondes. Calculer un ordre de grandeur d'une **année-lumière**, en mètres.

??? success "Correction"
    1. $\frac{6 \times 5}{1{,}5} \times 10^{-4 + 7 - 2} = 20 \times 10^{1} = 2 \times 10^{2}$.
    2. $3 \times 3{,}15 \times 10^{15} = 9{,}45 \times 10^{15}$ m, soit environ $10^{16}$ m.

### Exercice 6 — Simplifier des expressions littérales <span class="etoiles">★★</span>

Pour $x \neq 0$, simplifier $\dfrac{x^5 \times x^{-2}}{x^4}$ et $\dfrac{(2x^3)^2}{4x}$.

??? success "Correction"
    $x^{5 - 2 - 4} = x^{-1} = \frac{1}{x}$ ; $\frac{4x^6}{4x} = x^5$.

---

## Thème 2 — Racines carrées

*Méthode associée : [Méthode 2](methodes.md#methode-2-simplifier-une-expression-avec-des-racines).*

### Exercice 7 — Simplifier <span class="etoiles">★</span>

Écrire sous la forme $a\sqrt{b}$ avec $b$ entier le plus petit possible : $\sqrt{12}$ ; $\sqrt{45}$ ; $\sqrt{98}$ ; $\sqrt{300}$ ; $\sqrt{0{,}08}$.

??? success "Correction"
    $2\sqrt{3}$ ; $3\sqrt{5}$ ; $7\sqrt{2}$ ; $10\sqrt{3}$ ; $\sqrt{\frac{8}{100}} = \frac{2\sqrt{2}}{10} = \frac{\sqrt{2}}{5}$.

### Exercice 8 — Réduire <span class="etoiles">★</span>

Calculer : $A = \sqrt{12} + \sqrt{27} - \sqrt{75}$ ; $B = 2\sqrt{20} - 3\sqrt{5} + \sqrt{80}$.

??? success "Correction"
    $A = 2\sqrt{3} + 3\sqrt{3} - 5\sqrt{3} = 0$. $B = 4\sqrt{5} - 3\sqrt{5} + 4\sqrt{5} = 5\sqrt{5}$.

### Exercice 9 — Avec les identités remarquables <span class="etoiles">★★</span>

Développer et réduire : $\left(2 + \sqrt{3}\right)^2$ ; $\left(\sqrt{5} - \sqrt{2}\right)^2$ ; $\left(3\sqrt{2} + 1\right)\left(3\sqrt{2} - 1\right)$.

??? success "Correction"
    $4 + 4\sqrt{3} + 3 = 7 + 4\sqrt{3}$ ; $5 - 2\sqrt{10} + 2 = 7 - 2\sqrt{10}$ ; $18 - 1 = 17$.

### Exercice 10 — Dénominateurs sans racine <span class="etoiles">★★</span>

Écrire sans racine au dénominateur : $\dfrac{6}{\sqrt{3}}$ ; $\dfrac{\sqrt{2}}{\sqrt{8} + \sqrt{2}}$ ; $\dfrac{2}{\sqrt{5} + 1}$.

??? success "Correction"
    $\frac{6\sqrt{3}}{3} = 2\sqrt{3}$ ; $\frac{\sqrt{2}}{2\sqrt{2} + \sqrt{2}} = \frac{\sqrt{2}}{3\sqrt{2}} = \frac{1}{3}$ ; $\frac{2\left(\sqrt{5} - 1\right)}{5 - 1} = \frac{\sqrt{5} - 1}{2}$.

### Exercice 11 — Vrai ou faux <span class="etoiles">★★★</span>

Pour chaque affirmation, démontrer qu'elle est vraie ou donner un contre-exemple.

1. Pour tous réels $a, b \geq 0$, $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$.
2. Pour tout réel $x$, $\sqrt{x^2} = x$.
3. Pour tout réel $x \geq 0$, $\sqrt{4x} = 2\sqrt{x}$.
4. Le nombre d'or $\varphi = \frac{1 + \sqrt{5}}{2}$ vérifie $\varphi^2 = \varphi + 1$.

??? success "Correction"
    1. Faux : $\sqrt{9 + 16} = 5 \neq 7$. (C'est vrai seulement si $a = 0$ ou $b = 0$.)
    2. Faux : $\sqrt{(-2)^2} = 2 \neq -2$. On a $\sqrt{x^2} = |x|$.
    3. Vrai : $\sqrt{4x} = \sqrt{4}\sqrt{x} = 2\sqrt{x}$.
    4. Vrai : $\varphi^2 = \frac{1 + 2\sqrt{5} + 5}{4} = \frac{6 + 2\sqrt{5}}{4} = \frac{3 + \sqrt{5}}{2}$ et $\varphi + 1 = \frac{1 + \sqrt{5} + 2}{2} = \frac{3 + \sqrt{5}}{2}$.

---

## Thème 3 — Développer et factoriser

*Méthode associée : [Méthode 3](methodes.md#methode-3-developper-et-factoriser).*

### Exercice 12 — Développer <span class="etoiles">★</span>

Développer et réduire : $A = (3x - 2)^2$ ; $B = (x + 5)(x - 5)$ ; $C = (2x + 1)(x - 3) - (x - 1)^2$.

??? success "Correction"
    $A = 9x^2 - 12x + 4$ ; $B = x^2 - 25$ ; $C = 2x^2 - 6x + x - 3 - (x^2 - 2x + 1) = x^2 - 3x - 4$.

### Exercice 13 — Facteur commun <span class="etoiles">★</span>

Factoriser : $A = 6x^2 - 15x$ ; $B = (x + 2)(3x - 1) + (x + 2)(x + 4)$ ; $C = (2x - 1)^2 - (2x - 1)(x + 3)$.

??? success "Correction"
    $A = 3x(2x - 5)$ ; $B = (x + 2)(4x + 3)$ ; $C = (2x - 1)\big[(2x - 1) - (x + 3)\big] = (2x - 1)(x - 4)$.

### Exercice 14 — Identités remarquables <span class="etoiles">★</span>

Factoriser : $x^2 - 49$ ; $4x^2 + 12x + 9$ ; $25 - 10x + x^2$ ; $9x^2 - 2$.

??? success "Correction"
    $(x - 7)(x + 7)$ ; $(2x + 3)^2$ ; $(5 - x)^2$ ou $(x - 5)^2$ ; $\left(3x - \sqrt{2}\right)\left(3x + \sqrt{2}\right)$.

### Exercice 15 — Factorisations plus difficiles <span class="etoiles">★★</span>

Factoriser : $A = (x + 3)^2 - 25$ ; $B = (2x - 1)^2 - (x + 4)^2$ ; $C = x^2 - 6x + 9 - (x - 3)(2x + 1)$.

??? success "Correction"
    $A = (x + 3 - 5)(x + 3 + 5) = (x - 2)(x + 8)$.

    $B = \big[(2x - 1) - (x + 4)\big]\big[(2x - 1) + (x + 4)\big] = (x - 5)(3x + 3) = 3(x - 5)(x + 1)$.

    $C = (x - 3)^2 - (x - 3)(2x + 1) = (x - 3)\big[(x - 3) - (2x + 1)\big] = (x - 3)(-x - 4) = -(x - 3)(x + 4)$.

### Exercice 16 — Choisir la forme <span class="etoiles">★★</span>

Soit $f(x) = (x - 1)^2 - 4$.

1. Développer $f(x)$, puis factoriser $f(x)$.
2. En choisissant la forme la plus adaptée, calculer $f(0)$, $f(1)$, $f\left(\sqrt{2}\right)$ et résoudre $f(x) = 0$.

??? success "Correction"
    1. Développée : $x^2 - 2x - 3$. Factorisée : $(x - 1 - 2)(x - 1 + 2) = (x - 3)(x + 1)$.
    2. $f(0) = -3$ (développée) ; $f(1) = -4$ (forme de l'énoncé) ; $f\left(\sqrt{2}\right) = 2 - 2\sqrt{2} - 3 = -1 - 2\sqrt{2}$ ; $f(x) = 0 \iff x = 3$ ou $x = -1$ (factorisée).

### Exercice 17 — Calcul mental astucieux <span class="etoiles">★★★</span>

Sans calculatrice, calculer à l'aide des identités remarquables : $101^2$ ; $99^2$ ; $103 \times 97$ ; $1\,001^2 - 999^2$.

??? success "Correction"
    $(100 + 1)^2 = 10\,201$ ; $(100 - 1)^2 = 9\,801$ ; $(100 + 3)(100 - 3) = 10\,000 - 9 = 9\,991$ ; $(1\,001 - 999)(1\,001 + 999) = 2 \times 2\,000 = 4\,000$.

---

## Thème 4 — Comparer et encadrer

*Méthodes associées : [Méthode 4](methodes.md#methode-4-comparer-deux-nombres) et [Méthode 5](methodes.md#methode-5-encadrer-une-expression).*

### Exercice 18 — Comparer des fractions <span class="etoiles">★</span>

Comparer $\frac{13}{17}$ et $\frac{10}{13}$ en calculant leur différence.

??? success "Correction"
    $\frac{13}{17} - \frac{10}{13} = \frac{169 - 170}{221} = -\frac{1}{221} < 0$, donc $\frac{13}{17} < \frac{10}{13}$.

### Exercice 19 — Comparer des racines <span class="etoiles">★</span>

Comparer $4\sqrt{3}$ et $3\sqrt{5}$, puis $\sqrt{2} + \sqrt{3}$ et $\sqrt{10}$.

??? success "Correction"
    $(4\sqrt{3})^2 = 48 > 45 = (3\sqrt{5})^2$, donc $4\sqrt{3} > 3\sqrt{5}$ (nombres positifs).

    $\left(\sqrt{2} + \sqrt{3}\right)^2 = 5 + 2\sqrt{6}$. Comparons ce nombre à $10$ : $5 + 2\sqrt{6} < 10 \iff 2\sqrt{6} < 5 \iff 24 < 25$ (en élevant au carré des nombres positifs), ce qui est vrai. Donc $\left(\sqrt{2} + \sqrt{3}\right)^2 < 10$ et $\sqrt{2} + \sqrt{3} < \sqrt{10}$.

### Exercice 20 — $a$, $a^2$, $\sqrt{a}$ <span class="etoiles">★</span>

Ranger dans l'ordre croissant, sans calculatrice : $0{,}7$ ; $0{,}7^2$ ; $\sqrt{0{,}7}$. Puis : $1{,}2$ ; $1{,}2^2$ ; $\sqrt{1{,}2}$.

??? success "Correction"
    $0 < 0{,}7 < 1$ : $0{,}7^2 < 0{,}7 < \sqrt{0{,}7}$. $1{,}2 > 1$ : $\sqrt{1{,}2} < 1{,}2 < 1{,}2^2$.

### Exercice 21 — Encadrer <span class="etoiles">★★</span>

On sait que $-2 \leq x \leq 3$. Encadrer $2x + 5$, $1 - 4x$ et $x^2$ (attention !).

??? success "Correction"
    $-4 \leq 2x \leq 6$, donc $1 \leq 2x + 5 \leq 11$.

    $-12 \leq 4x \leq 8$, donc $-8 \leq -4x \leq 12$ et $-7 \leq 1 - 4x \leq 13$.

    $x^2$ : on ne peut pas élever directement au carré, car $x$ change de signe. Si $-2 \leq x \leq 0$, $0 \leq x^2 \leq 4$ ; si $0 \leq x \leq 3$, $0 \leq x^2 \leq 9$. Donc $0 \leq x^2 \leq 9$.

### Exercice 22 — Une inégalité classique <span class="etoiles">★★</span>

1. Démontrer que pour tous réels $a$ et $b$, $a^2 + b^2 \geq 2ab$.
2. En déduire que pour tout réel $x > 0$, $x + \dfrac{1}{x} \geq 2$.

??? success "Correction"
    1. $a^2 + b^2 - 2ab = (a - b)^2 \geq 0$.
    2. Avec $a = \sqrt{x}$ et $b = \frac{1}{\sqrt{x}}$ : $x + \frac{1}{x} \geq 2 \times \sqrt{x} \times \frac{1}{\sqrt{x}} = 2$. *Autre méthode : $x + \frac{1}{x} - 2 = \frac{x^2 - 2x + 1}{x} = \frac{(x - 1)^2}{x} \geq 0$.*

### Exercice 23 — Comparer par différence <span class="etoiles">★★★</span>

Soit $a$ et $b$ deux réels strictement positifs, avec $a < b$. Comparer $\dfrac{a}{b}$ et $\dfrac{a + 1}{b + 1}$. Interpréter avec une fraction comme $\frac{3}{7}$.

??? success "Correction"
    $\frac{a + 1}{b + 1} - \frac{a}{b} = \frac{b(a + 1) - a(b + 1)}{b(b + 1)} = \frac{b - a}{b(b + 1)} > 0$. Donc $\frac{a}{b} < \frac{a + 1}{b + 1}$ : ajouter $1$ au numérateur et au dénominateur d'une fraction inférieure à $1$ la fait augmenter. Exemple : $\frac{3}{7} \approx 0{,}43 < \frac{4}{8} = 0{,}5$.

---

## Thème 5 — Formules et approfondissement

### Exercice 24 — Isoler une variable <span class="etoiles">★</span>

Exprimer la variable demandée en fonction des autres (toutes les grandeurs sont strictement positives).

1. $P = UI$ : exprimer $I$.
2. $\mathcal{V} = \pi r^2 h$ : exprimer $h$, puis $r$.
3. $\frac{1}{f} = \frac{1}{a} + \frac{1}{b}$ : exprimer $f$.

??? success "Correction"
    1. $I = \frac{P}{U}$.
    2. $h = \frac{\mathcal{V}}{\pi r^2}$ ; $r = \sqrt{\frac{\mathcal{V}}{\pi h}}$.
    3. $\frac{1}{f} = \frac{a + b}{ab}$, donc $f = \frac{ab}{a + b}$.

### Exercice 25 — Convertir une température <span class="etoiles">★★</span>

La température en degrés Fahrenheit est $F = \frac{9}{5}C + 32$, où $C$ est la température en degrés Celsius.

1. Exprimer $C$ en fonction de $F$.
2. Convertir $98{,}6$ °F en °C. Pour quelle température les deux valeurs sont-elles égales ?

??? success "Correction"
    1. $C = \frac{5}{9}(F - 32)$.
    2. $\frac{5}{9} \times 66{,}6 = 37$ °C. Égalité : $C = \frac{9}{5}C + 32 \iff -\frac{4}{5}C = 32 \iff C = -40$.

### Exercice 26 — Identité de Lagrange (version simple) <span class="etoiles">★★</span>

Démontrer que pour tous réels $a$, $b$, $c$, $d$ :
$$(a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad - bc)^2.$$
En déduire une écriture de $65 = 5 \times 13$ comme somme de deux carrés, de deux façons.

??? success "Correction"
    À gauche : $a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2$. À droite : $a^2c^2 + 2abcd + b^2d^2 + a^2d^2 - 2abcd + b^2c^2$. Les deux sont égaux.

    $5 = 1^2 + 2^2$ et $13 = 2^2 + 3^2$. Avec $a = 1$, $b = 2$, $c = 2$, $d = 3$ : $65 = (2 + 6)^2 + (3 - 4)^2 = 64 + 1$. Avec $c = 3$, $d = 2$ : $65 = (3 + 4)^2 + (2 - 6)^2 = 49 + 16$.

### Exercice 27 — Moyennes <span class="etoiles">★★★</span>

Pour deux réels $a$ et $b$ strictement positifs, on définit la moyenne arithmétique $m = \frac{a + b}{2}$ et la moyenne géométrique $g = \sqrt{ab}$.

1. Démontrer que $m - g = \frac{1}{2}\left(\sqrt{a} - \sqrt{b}\right)^2$. En déduire que $g \leq m$.
2. Application : parmi tous les rectangles de périmètre $40$ cm, lequel a la plus grande aire ?

??? success "Correction"
    1. $\frac{1}{2}\left(\sqrt{a} - \sqrt{b}\right)^2 = \frac{1}{2}\left(a - 2\sqrt{ab} + b\right) = \frac{a + b}{2} - \sqrt{ab}$. C'est un carré divisé par $2$ : il est positif.
    2. Côtés $a$ et $b$ avec $a + b = 20$ : l'aire vaut $ab = g^2 \leq m^2 = 10^2 = 100$. L'égalité a lieu quand $\sqrt{a} = \sqrt{b}$, c'est-à-dire $a = b = 10$ : le **carré** de côté $10$ cm.

### Exercice 28 — Une expression à simplifier <span class="etoiles">★★★</span>

Démontrer que $\sqrt{7 + 4\sqrt{3}} = 2 + \sqrt{3}$, puis simplifier $\sqrt{7 + 4\sqrt{3}} - \sqrt{7 - 4\sqrt{3}}$.

??? success "Correction"
    $2 + \sqrt{3}$ est positif et $\left(2 + \sqrt{3}\right)^2 = 4 + 4\sqrt{3} + 3 = 7 + 4\sqrt{3}$ : c'est donc la racine carrée de $7 + 4\sqrt{3}$.

    De même, $2 - \sqrt{3} > 0$ (car $\sqrt{3} < 2$) et $\left(2 - \sqrt{3}\right)^2 = 7 - 4\sqrt{3}$. La différence vaut $(2 + \sqrt{3}) - (2 - \sqrt{3}) = 2\sqrt{3}$.
