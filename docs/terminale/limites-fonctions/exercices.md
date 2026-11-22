# Exercices corrigés — Limites de fonctions

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Définitions et asymptotes | 1 à 4 |
| 2. Polynômes et fractions rationnelles | 5 à 9 |
| 3. Limites en un réel | 10 à 13 |
| 4. Racines carrées et composition | 14 à 18 |
| 5. Exponentielle et croissances comparées | 19 à 24 |
| 6. Théorèmes de comparaison | 25 à 28 |

---

## Thème 1 — Définitions et asymptotes

*Méthode associée : [Méthode 1](methodes.md#methode-1-traduire-une-limite-en-asymptote-et-inversement).*

### Exercice 1 — Traduire graphiquement <span class="etoiles">★</span>

Pour chaque information, dire si la courbe de $f$ admet une asymptote, et laquelle.

1. $\displaystyle\lim_{x\to+\infty} f(x) = 3$
2. $\displaystyle\lim_{x\to 2^+} f(x) = -\infty$
3. $\displaystyle\lim_{x\to-\infty} f(x) = +\infty$
4. $\displaystyle\lim_{x\to-\infty} f(x) = 0$

??? success "Correction"
    1. La droite d'équation $y = 3$ est asymptote horizontale en $+\infty$.
    2. La droite d'équation $x = 2$ est asymptote verticale.
    3. Aucune asymptote horizontale en $-\infty$ : on ne peut rien déduire d'autre.
    4. La droite d'équation $y = 0$ (l'axe des abscisses) est asymptote horizontale en $-\infty$.

### Exercice 2 — Lire un tableau de variations <span class="etoiles">★</span>

Une fonction $f$, définie sur $]-\infty \,;\, 1[ \,\cup\, ]1 \,;\, +\infty[$, a le tableau de variations suivant.

| $x$ | $-\infty$ | | $1^-$ | $1^+$ | | $+\infty$ |
|---|---|---|---|---|---|---|
| $f(x)$ | $2$ | $\nearrow$ | $+\infty$ | $-\infty$ | $\nearrow$ | $2$ |

1. Lire les limites de $f$ aux bornes de son ensemble de définition, et en déduire les asymptotes.
2. On admet que $f(x) = 2 + \dfrac{1}{1 - x}$. Retrouver ces limites par le calcul.

??? success "Correction"
    **1.** $\displaystyle\lim_{x\to-\infty} f(x) = \lim_{x\to+\infty} f(x) = 2$, $\displaystyle\lim_{x\to 1^-} f(x) = +\infty$ et $\displaystyle\lim_{x\to 1^+} f(x) = -\infty$.

    La droite $y = 2$ est asymptote horizontale en $-\infty$ et en $+\infty$. La droite $x = 1$ est asymptote verticale.

    **2.** En $\pm\infty$ : $1 - x \to \mp\infty$, donc $\dfrac{1}{1 - x} \to 0$ et $f(x) \to 2$.

    En $1^-$ : $x < 1$ donc $1 - x \to 0^+$ et $\dfrac{1}{1-x} \to +\infty$. En $1^+$ : $1 - x \to 0^-$ et $\dfrac{1}{1-x} \to -\infty$.

### Exercice 3 — Construire des exemples <span class="etoiles">★★</span>

Donner l'expression d'une fonction $f$ vérifiant les conditions demandées.

1. $\displaystyle\lim_{x\to+\infty} f(x) = 1$ et $\displaystyle\lim_{x\to-\infty} f(x) = +\infty$.
2. La courbe de $f$ admet la droite $x = 3$ comme asymptote verticale et la droite $y = 0$ comme asymptote horizontale en $+\infty$ et en $-\infty$.
3. $\displaystyle\lim_{x\to+\infty} f(x) = +\infty$, mais $f$ n'est croissante sur aucun intervalle de la forme $[A \,;\, +\infty[$.

??? success "Correction"
    Il y a beaucoup de réponses possibles. Par exemple :

    **1.** $f(x) = 1 + e^{-x}$. En $+\infty$, $e^{-x} \to 0$ donc $f(x) \to 1$. En $-\infty$, $-x \to +\infty$ donc $e^{-x} \to +\infty$.

    **2.** $f(x) = \dfrac{1}{x - 3}$ : en $3^\pm$, $f(x) \to \pm\infty$ ; en $\pm\infty$, $f(x) \to 0$.

    **3.** $f(x) = x + 2\sin x$. Elle tend vers $+\infty$ car $f(x) \geq x - 2$. Mais $f'(x) = 1 + 2\cos x$ est strictement négative dès que $\cos x < -\frac{1}{2}$, c'est-à-dire sur chaque intervalle $\left]\frac{2\pi}{3} + 2k\pi \,;\, \frac{4\pi}{3} + 2k\pi\right[$, pour tout entier $k$. Il existe de tels intervalles aussi loin qu'on veut, sur lesquels $f$ est strictement décroissante : $f$ n'est croissante sur aucun intervalle $[A \,;\, +\infty[$.

### Exercice 4 — Vrai ou faux ? <span class="etoiles">★★</span>

Justifier chaque réponse par une preuve ou un contre-exemple.

1. Si $\displaystyle\lim_{x\to+\infty} f(x) = 0$, alors $f(x) > 0$ pour $x$ assez grand.
2. Une courbe ne peut pas couper son asymptote horizontale.
3. Si $\displaystyle\lim_{x\to+\infty} f(x) = +\infty$ et $\displaystyle\lim_{x\to+\infty} g(x) = +\infty$, alors $\displaystyle\lim_{x\to+\infty} \frac{f(x)}{g(x)} = 1$.
4. Si $g(x) \leq f(x)$ pour tout $x$ et si $f$ a une limite finie en $+\infty$, alors $g$ a une limite en $+\infty$.
5. Si $\displaystyle\lim_{x\to+\infty} f(x) = 2$, alors $f(x) > 1$ pour $x$ assez grand.

??? success "Correction"
    **1. Faux.** $f(x) = -\frac{1}{x}$ tend vers $0$ en restant négative.

    **2. Faux.** $f(x) = \frac{\sin x}{x}$ tend vers $0$ (gendarmes) et s'annule en chaque $x = k\pi$.

    **3. Faux.** $f(x) = x^2$ et $g(x) = x$ : le quotient vaut $x$ et tend vers $+\infty$. C'est une forme indéterminée.

    **4. Faux.** $f(x) = 1$ et $g(x) = \sin x$ : on a $g \leq f$, mais $\sin x$ n'a pas de limite en $+\infty$.

    **5. Vrai.** Avec $\varepsilon = 1$ dans la définition : pour $x$ assez grand, $|f(x) - 2| < 1$, donc $f(x) > 1$.

---

## Thème 2 — Polynômes et fractions rationnelles

*Méthode associée : [Méthode 2](methodes.md#methode-2-polynomes-et-fractions-rationnelles-en-linfini).*

### Exercice 5 — Polynômes <span class="etoiles">★</span>

Déterminer les limites en $+\infty$ et en $-\infty$ de :

1. $f(x) = -2x^3 + 5x - 1$
2. $g(x) = x^4 - 3x^2 + x$

??? success "Correction"
    **1.** $f(x) = x^3\left(-2 + \dfrac{5}{x^2} - \dfrac{1}{x^3}\right)$. La parenthèse tend vers $-2$.

    - En $+\infty$ : $x^3 \to +\infty$, donc $f(x) \to -\infty$.
    - En $-\infty$ : $x^3 \to -\infty$, donc $f(x) \to +\infty$.

    **2.** $g(x) = x^4\left(1 - \dfrac{3}{x^2} + \dfrac{1}{x^3}\right)$. La parenthèse tend vers $1$ et $x^4 \to +\infty$ en $\pm\infty$ (puissance paire) : $g(x) \to +\infty$ en $+\infty$ et en $-\infty$.

### Exercice 6 — Fractions rationnelles <span class="etoiles">★</span>

Déterminer les limites suivantes.

1. $\displaystyle\lim_{x\to+\infty} \frac{3x^2 - 1}{x^2 + 4}$
2. $\displaystyle\lim_{x\to-\infty} \frac{2x + 1}{x^2 - 5}$
3. $\displaystyle\lim_{x\to-\infty} \frac{x^3 - 1}{2x + 3}$
4. $\displaystyle\lim_{x\to+\infty} \frac{1 - 4x^2}{x + 1}$

??? success "Correction"
    On applique la règle du quotient des termes de plus haut degré (démontrée dans le cours).

    1. $\dfrac{3x^2}{x^2} = 3$ : la limite est $3$.
    2. $\dfrac{2x}{x^2} = \dfrac{2}{x} \to 0$ : la limite est $0$.
    3. $\dfrac{x^3}{2x} = \dfrac{x^2}{2} \to +\infty$ en $-\infty$ : la limite est $+\infty$.
    4. $\dfrac{-4x^2}{x} = -4x \to -\infty$ : la limite est $-\infty$.

### Exercice 7 — Justifier la règle sur un exemple <span class="etoiles">★★</span>

Sans utiliser la règle du terme dominant, déterminer $\displaystyle\lim_{x\to+\infty} \frac{5x^3 - 2x + 7}{1 - x^3}$ en factorisant.

??? success "Correction"
    Pour $x > 0$, on factorise par $x^3$ au numérateur et au dénominateur :

    $$\frac{5x^3 - 2x + 7}{1 - x^3} = \frac{x^3\left(5 - \frac{2}{x^2} + \frac{7}{x^3}\right)}{x^3\left(\frac{1}{x^3} - 1\right)} = \frac{5 - \frac{2}{x^2} + \frac{7}{x^3}}{\frac{1}{x^3} - 1}.$$

    Le numérateur tend vers $5$ et le dénominateur vers $-1$. La limite vaut $-5$.

### Exercice 8 — Asymptote et position relative <span class="etoiles">★★</span>

Soit $f(x) = \dfrac{2x^2 + 3x - 1}{x^2 + 1}$, définie sur $\mathbb{R}$.

1. Montrer que la courbe $\mathcal{C}_f$ admet une asymptote horizontale $\Delta$ en $+\infty$ et en $-\infty$.
2. Montrer que $f(x) - 2 = \dfrac{3x - 3}{x^2 + 1}$.
3. Étudier la position relative de $\mathcal{C}_f$ et de $\Delta$.

??? success "Correction"
    **1.** Par la règle du terme dominant, $\displaystyle\lim_{x\to\pm\infty} f(x) = \frac{2x^2}{x^2} = 2$. La droite $\Delta : y = 2$ est asymptote horizontale en $\pm\infty$.

    **2.** $f(x) - 2 = \dfrac{2x^2 + 3x - 1 - 2(x^2 + 1)}{x^2 + 1} = \dfrac{3x - 3}{x^2 + 1}$.

    **3.** Le dénominateur est strictement positif, donc $f(x) - 2$ a le signe de $3x - 3 = 3(x - 1)$ :

    - pour $x < 1$, $\mathcal{C}_f$ est **en dessous** de $\Delta$ ;
    - pour $x > 1$, $\mathcal{C}_f$ est **au-dessus** de $\Delta$ ;
    - elles se coupent au point d'abscisse $1$.

### Exercice 9 — Asymptote oblique <span class="etoiles">★★★</span>

Soit $f(x) = \dfrac{x^2 + x + 1}{x - 1}$ sur $]1 \,;\, +\infty[$.

1. Déterminer les limites de $f$ en $1^+$ et en $+\infty$.
2. Montrer que pour tout $x > 1$ : $f(x) = x + 2 + \dfrac{3}{x - 1}$.
3. En déduire que $\displaystyle\lim_{x\to+\infty} \big(f(x) - (x + 2)\big) = 0$. On dit que la droite $D : y = x + 2$ est **asymptote oblique** à $\mathcal{C}_f$. Préciser la position de $\mathcal{C}_f$ par rapport à $D$.

??? success "Correction"
    **1.** En $1^+$ : le numérateur tend vers $3$, et $x - 1 \to 0^+$, donc $f(x) \to +\infty$ (asymptote verticale $x = 1$). En $+\infty$ : $\dfrac{x^2}{x} = x \to +\infty$.

    **2.** $(x + 2)(x - 1) + 3 = x^2 + x - 2 + 3 = x^2 + x + 1$. En divisant par $x - 1 \neq 0$, on obtient l'égalité.

    **3.** $f(x) - (x + 2) = \dfrac{3}{x - 1} \to 0$ en $+\infty$. Comme $\dfrac{3}{x-1} > 0$ pour $x > 1$, la courbe est **au-dessus** de $D$.

---

## Thème 3 — Limites en un réel

*Méthode associée : [Méthode 3](methodes.md#methode-3-limite-en-un-reel-etudier-le-signe-du-denominateur).*

### Exercice 10 — Fonctions de référence en $0$ <span class="etoiles">★</span>

Déterminer les limites à gauche et à droite en $0$ de :

1. $\dfrac{1}{x}$
2. $\dfrac{1}{x^2}$
3. $-\dfrac{3}{x^3}$

Puis déterminer $\displaystyle\lim_{x\to 0^+} \frac{1}{\sqrt{x}}$.

??? success "Correction"
    1. $\dfrac{1}{x} \to +\infty$ en $0^+$ et $-\infty$ en $0^-$.
    2. $x^2 > 0$ des deux côtés : $\dfrac{1}{x^2} \to +\infty$ en $0^+$ et en $0^-$.
    3. En $0^+$, $x^3 \to 0^+$, donc $\dfrac{3}{x^3} \to +\infty$ et $-\dfrac{3}{x^3} \to -\infty$. En $0^-$, $x^3 \to 0^-$ et $-\dfrac{3}{x^3} \to +\infty$.

    Enfin, $\sqrt{x} \to 0^+$ en $0^+$, donc $\dfrac{1}{\sqrt{x}} \to +\infty$.

### Exercice 11 — Une fonction homographique <span class="etoiles">★★</span>

Soit $f(x) = \dfrac{x + 1}{x - 2}$, définie sur $\mathbb{R} \setminus \{2\}$.

1. Déterminer les limites de $f$ en $2^-$ et en $2^+$.
2. Déterminer les limites de $f$ en $\pm\infty$.
3. En déduire les asymptotes à $\mathcal{C}_f$.

??? success "Correction"
    **1.** Le numérateur tend vers $3 > 0$. Pour $x < 2$, $x - 2 \to 0^-$ donc $f(x) \to -\infty$. Pour $x > 2$, $x - 2 \to 0^+$ donc $f(x) \to +\infty$.

    **2.** $\dfrac{x}{x} = 1$ : $f(x) \to 1$ en $+\infty$ et en $-\infty$.

    **3.** Asymptote verticale $x = 2$ et asymptote horizontale $y = 1$ en $\pm\infty$.

### Exercice 12 — Tableau de signes du dénominateur <span class="etoiles">★★</span>

Soit $g(x) = \dfrac{2x - 1}{x^2 - 4x + 3}$.

1. Factoriser $x^2 - 4x + 3$ et dresser son tableau de signes.
2. Déterminer les limites de $g$ en $1^-$, $1^+$, $3^-$ et $3^+$.
3. Déterminer les limites en $\pm\infty$ et donner toutes les asymptotes.

??? success "Correction"
    **1.** $x^2 - 4x + 3 = (x - 1)(x - 3)$ (racines $1$ et $3$). Ce trinôme est positif à l'extérieur des racines et négatif entre elles :

    | $x$ | $-\infty$ | | $1$ | | $3$ | | $+\infty$ |
    |---|---|---|---|---|---|---|---|
    | $(x-1)(x-3)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |

    **2.** En $1$, le numérateur tend vers $1 > 0$ :

    - $\displaystyle\lim_{x\to 1^-} g(x) = \frac{1}{0^+} = +\infty$ ;
    - $\displaystyle\lim_{x\to 1^+} g(x) = \frac{1}{0^-} = -\infty$.

    En $3$, le numérateur tend vers $5 > 0$ :

    - $\displaystyle\lim_{x\to 3^-} g(x) = \frac{5}{0^-} = -\infty$ ;
    - $\displaystyle\lim_{x\to 3^+} g(x) = \frac{5}{0^+} = +\infty$.

    **3.** En $\pm\infty$ : $\dfrac{2x}{x^2} = \dfrac{2}{x} \to 0$. Asymptotes : verticales $x = 1$ et $x = 3$, horizontale $y = 0$.

### Exercice 13 — Formes $\frac{0}{0}$ <span class="etoiles">★★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to 2} \frac{x^2 - 4}{x - 2}$
2. $\displaystyle\lim_{x\to 1} \frac{x^2 + x - 2}{x^2 - 1}$
3. $\displaystyle\lim_{x\to 0} \frac{\sqrt{1 + x} - 1}{x}$

??? success "Correction"
    **1.** Pour $x \neq 2$, $\dfrac{x^2 - 4}{x - 2} = \dfrac{(x-2)(x+2)}{x - 2} = x + 2 \to 4$.

    **2.** $1$ est racine du numérateur et du dénominateur : $x^2 + x - 2 = (x - 1)(x + 2)$ et $x^2 - 1 = (x - 1)(x + 1)$. Pour $x \neq 1$ :

    $$\frac{x^2 + x - 2}{x^2 - 1} = \frac{x + 2}{x + 1} \longrightarrow \frac{3}{2}.$$

    **3.** Avec la quantité conjuguée, pour $x \neq 0$ :

    $$\frac{\sqrt{1+x} - 1}{x} = \frac{(1 + x) - 1}{x\left(\sqrt{1+x} + 1\right)} = \frac{1}{\sqrt{1+x} + 1} \longrightarrow \frac{1}{2}.$$

    *Remarque :* c'est le nombre dérivé de $x \mapsto \sqrt{x}$ en $1$, qui vaut $\frac{1}{2\sqrt{1}} = \frac{1}{2}$.

---

## Thème 4 — Racines carrées et composition

*Méthodes associées : [Méthode 4](methodes.md#methode-4-fonctions-avec-des-racines-carrees) et [Méthode 5](methodes.md#methode-5-utiliser-la-composition).*

### Exercice 14 — Composition directe <span class="etoiles">★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} \sqrt{4 + \frac{1}{x}}$
2. $\displaystyle\lim_{x\to+\infty} e^{-x^2}$
3. $\displaystyle\lim_{x\to+\infty} e^{1/x}$
4. $\displaystyle\lim_{x\to-\infty} \sqrt{x^2 + 1}$

??? success "Correction"
    1. $X = 4 + \frac{1}{x} \to 4$ et $\sqrt{X} \to 2$ : la limite est $2$.
    2. $X = -x^2 \to -\infty$ et $e^X \to 0$ : la limite est $0$.
    3. $X = \frac{1}{x} \to 0$ et $e^X \to e^0 = 1$ : la limite est $1$.
    4. $X = x^2 + 1 \to +\infty$ et $\sqrt{X} \to +\infty$ : la limite est $+\infty$.

### Exercice 15 — Composition avec une fraction <span class="etoiles">★★</span>

1. Déterminer $\displaystyle\lim_{x\to+\infty} \sqrt{\frac{9x^2 + 1}{x^2 + 3}}$.
2. Déterminer les limites de $h(x) = e^{\frac{1}{1-x}}$ en $1^-$ et en $1^+$. La courbe de $h$ a-t-elle une asymptote verticale ?

??? success "Correction"
    **1.** $\dfrac{9x^2 + 1}{x^2 + 3} \to 9$ (termes dominants), et $\sqrt{X} \to 3$ quand $X \to 9$. La limite est $3$.

    **2.** En $1^-$ : $1 - x \to 0^+$, donc $X = \frac{1}{1-x} \to +\infty$ et $e^X \to +\infty$. En $1^+$ : $X \to -\infty$ et $e^X \to 0$.

    La droite $x = 1$ est asymptote verticale, à cause de la limite infinie à gauche. À droite, la courbe « rejoint » le point $(1 \,;\, 0)$.

### Exercice 16 — Quantité conjuguée <span class="etoiles">★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} \left(\sqrt{x + 3} - \sqrt{x}\right)$
2. $\displaystyle\lim_{x\to+\infty} \left(\sqrt{x^2 + 2x} - x\right)$

??? success "Correction"
    **1.** $\sqrt{x + 3} - \sqrt{x} = \dfrac{(x + 3) - x}{\sqrt{x+3} + \sqrt{x}} = \dfrac{3}{\sqrt{x+3} + \sqrt{x}}$. Le dénominateur tend vers $+\infty$, donc la limite est $0$.

    **2.** $\sqrt{x^2 + 2x} - x = \dfrac{2x}{\sqrt{x^2 + 2x} + x}$. Pour $x > 0$, $\sqrt{x^2 + 2x} = x\sqrt{1 + \frac{2}{x}}$, donc

    $$\sqrt{x^2 + 2x} - x = \frac{2x}{x\left(\sqrt{1 + \frac{2}{x}} + 1\right)} = \frac{2}{\sqrt{1 + \frac{2}{x}} + 1} \longrightarrow \frac{2}{2} = 1.$$

### Exercice 17 — Le piège de $\sqrt{x^2}$ en $-\infty$ <span class="etoiles">★★★</span>

1. Déterminer $\displaystyle\lim_{x\to-\infty} \left(\sqrt{x^2 + 1} + x\right)$.
2. Déterminer $\displaystyle\lim_{x\to-\infty} \frac{\sqrt{x^2 + x}}{x}$ (la fonction est définie pour $x \leq -1$).

??? success "Correction"
    **1.** Forme $+\infty - \infty$ (car $x \to -\infty$). Avec la quantité conjuguée :

    $$\sqrt{x^2 + 1} + x = \frac{(x^2 + 1) - x^2}{\sqrt{x^2 + 1} - x} = \frac{1}{\sqrt{x^2 + 1} - x}.$$

    En $-\infty$, $\sqrt{x^2 + 1} \to +\infty$ et $-x \to +\infty$ : le dénominateur tend vers $+\infty$, la limite est $0$.

    **2.** Pour $x \leq -1$ : $\sqrt{x^2 + x} = \sqrt{x^2}\sqrt{1 + \frac{1}{x}} = |x|\sqrt{1 + \frac{1}{x}} = -x\sqrt{1 + \frac{1}{x}}$, car $x < 0$. Donc

    $$\frac{\sqrt{x^2 + x}}{x} = -\sqrt{1 + \frac{1}{x}} \longrightarrow -1.$$

    !!! warning "Erreur fréquente"
        Écrire $\sqrt{x^2} = x$ donnerait la réponse fausse $+1$. Un quotient d'un nombre positif par un nombre négatif est négatif : la limite ne peut pas être $+1$.

### Exercice 18 — Composée d'une suite et d'une fonction <span class="etoiles">★★</span>

Déterminer la limite des suites :

1. $u_n = e^{1/n}$ (pour $n \geq 1$)
2. $v_n = \dfrac{\sqrt{9n^2 + 1}}{n + 1}$
3. $w_n = \sqrt{\dfrac{4n + 1}{n + 2}}$

??? success "Correction"
    **1.** $\frac{1}{n} \to 0$ et $\displaystyle\lim_{x\to 0} e^x = 1$, donc $u_n \to 1$.

    **2.** Pour $n \geq 1$, $\sqrt{9n^2 + 1} = n\sqrt{9 + \frac{1}{n^2}}$, donc $v_n = \dfrac{\sqrt{9 + \frac{1}{n^2}}}{1 + \frac{1}{n}}$. Le numérateur tend vers $\sqrt{9} = 3$ (composition) et le dénominateur vers $1$ : $v_n \to 3$.

    **3.** $\dfrac{4n + 1}{n + 2} \to 4$, et $\displaystyle\lim_{x\to 4} \sqrt{x} = 2$, donc $w_n \to 2$.

---

## Thème 5 — Exponentielle et croissances comparées

*Méthode associée : [Méthode 6](methodes.md#methode-6-utiliser-les-croissances-comparees).*

### Exercice 19 — Limites directes <span class="etoiles">★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} e^{-x}$
2. $\displaystyle\lim_{x\to-\infty} (e^x - x)$
3. $\displaystyle\lim_{x\to-\infty} (3e^x + 2)$
4. $\displaystyle\lim_{x\to+\infty} \frac{1}{1 + e^x}$ et $\displaystyle\lim_{x\to-\infty} \frac{1}{1 + e^x}$

??? success "Correction"
    1. $-x \to -\infty$ et $e^X \to 0$ : la limite est $0$.
    2. $e^x \to 0$ et $-x \to +\infty$ : par somme, la limite est $+\infty$.
    3. $e^x \to 0$ : la limite est $2$.
    4. En $+\infty$, $1 + e^x \to +\infty$ donc la limite est $0$. En $-\infty$, $1 + e^x \to 1$ donc la limite est $1$.

### Exercice 20 — Formes indéterminées avec l'exponentielle <span class="etoiles">★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} (e^x - x)$
2. $\displaystyle\lim_{x\to+\infty} \frac{e^x + 1}{e^x - 1}$ et $\displaystyle\lim_{x\to-\infty} \frac{e^x + 1}{e^x - 1}$
3. $\displaystyle\lim_{x\to+\infty} \frac{2e^x - x^2}{e^x + x}$

??? success "Correction"
    **1.** Forme $\infty - \infty$. $e^x - x = e^x\left(1 - \dfrac{x}{e^x}\right)$. Par croissance comparée, $\frac{x}{e^x} \to 0$ : la parenthèse tend vers $1$ et la limite est $+\infty$.

    **2.** En $+\infty$, forme $\frac{\infty}{\infty}$ : on divise par $e^x$, ce qui donne $\dfrac{1 + e^{-x}}{1 - e^{-x}} \to 1$.

    En $-\infty$, il n'y a pas de forme indéterminée : $e^x \to 0$, donc le quotient tend vers $\dfrac{1}{-1} = -1$.

    **3.** On divise par $e^x$ : $\dfrac{2 - \frac{x^2}{e^x}}{1 + \frac{x}{e^x}}$. Par croissances comparées, $\frac{x^2}{e^x} \to 0$ et $\frac{x}{e^x} \to 0$. La limite est $2$.

### Exercice 21 — Croissances comparées <span class="etoiles">★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} x^3 e^{-x}$
2. $\displaystyle\lim_{x\to-\infty} (x^2 + 1)e^x$
3. $\displaystyle\lim_{x\to+\infty} \frac{e^x}{x^2 + x}$

??? success "Correction"
    **1.** $x^3 e^{-x} = \dfrac{x^3}{e^x} \to 0$ par croissance comparée.

    **2.** $(x^2 + 1)e^x = x^2 e^x + e^x$. Par croissance comparée, $x^2 e^x \to 0$ en $-\infty$, et $e^x \to 0$. La limite est $0$.

    **3.** $\dfrac{e^x}{x^2 + x} = \dfrac{e^x}{x^2} \times \dfrac{1}{1 + \frac{1}{x}}$. Le premier facteur tend vers $+\infty$ et le second vers $1$. La limite est $+\infty$.

### Exercice 22 — Limites en $0$ <span class="etoiles">★★</span>

On rappelle que $\displaystyle\lim_{x\to 0} \frac{e^x - 1}{x} = 1$. Déterminer :

1. $\displaystyle\lim_{x\to 0} \frac{e^{2x} - 1}{x}$
2. $\displaystyle\lim_{x\to+\infty} x\left(e^{1/x} - 1\right)$

??? success "Correction"
    **1.** On pose $X = 2x$, qui tend vers $0$. Alors $\dfrac{e^{2x} - 1}{x} = 2 \times \dfrac{e^X - 1}{X} \to 2 \times 1 = 2$.

    **2.** On pose $X = \frac{1}{x}$, qui tend vers $0^+$ quand $x \to +\infty$. Alors $x\left(e^{1/x} - 1\right) = \dfrac{e^X - 1}{X} \to 1$.

### Exercice 23 — Étude d'une fonction <span class="etoiles">★★</span>

Soit $f(x) = x e^{-x}$ sur $[0 \,;\, +\infty[$.

1. Déterminer la limite de $f$ en $+\infty$. Interpréter graphiquement.
2. Étudier les variations de $f$ et dresser son tableau de variations.
3. En déduire que pour tout $x \geq 0$ : $0 \leq x e^{-x} \leq \dfrac{1}{e}$.

??? success "Correction"
    **1.** Par croissance comparée, $\dfrac{x}{e^x} \to 0$. La droite $y = 0$ est asymptote horizontale en $+\infty$.

    **2.** $f'(x) = e^{-x} - x e^{-x} = (1 - x)e^{-x}$. Comme $e^{-x} > 0$, $f'(x)$ a le signe de $1 - x$ : positive sur $[0 \,;\, 1]$, négative sur $[1 \,;\, +\infty[$.

    | $x$ | $0$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $0$ | $\nearrow$ | $\frac{1}{e}$ | $\searrow$ | $0$ |

    **3.** Le maximum de $f$ sur $[0 \,;\, +\infty[$ est $f(1) = e^{-1} = \frac{1}{e}$. De plus, $f(x) \geq 0$ comme produit de deux nombres positifs.

### Exercice 24 — Changement de variable <span class="etoiles">★★★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} \frac{e^{\sqrt{x}}}{x}$
2. $\displaystyle\lim_{x\to+\infty} x e^{-\sqrt{x}}$

??? success "Correction"
    On pose $X = \sqrt{x}$, qui tend vers $+\infty$, et l'on a $x = X^2$.

    **1.** $\dfrac{e^{\sqrt{x}}}{x} = \dfrac{e^X}{X^2} \to +\infty$ par croissance comparée (avec $n = 2$).

    **2.** $x e^{-\sqrt{x}} = \dfrac{X^2}{e^X} \to 0$ par croissance comparée.

---

## Thème 6 — Théorèmes de comparaison

*Méthode associée : [Méthode 7](methodes.md#methode-7-encadrer-une-fonction-qui-oscille).*

### Exercice 25 — Comparaison et gendarmes <span class="etoiles">★</span>

Déterminer :

1. $\displaystyle\lim_{x\to+\infty} (x + \sin x)$
2. $\displaystyle\lim_{x\to+\infty} \frac{\cos x}{x}$
3. $\displaystyle\lim_{x\to+\infty} e^{-x}\cos x$

??? success "Correction"
    **1.** $\sin x \geq -1$ donc $x + \sin x \geq x - 1 \to +\infty$. Par comparaison, la limite est $+\infty$.

    **2.** Pour $x > 0$, $-\frac{1}{x} \leq \frac{\cos x}{x} \leq \frac{1}{x}$. Les bornes tendent vers $0$ : par les gendarmes, la limite est $0$.

    **3.** Comme $e^{-x} > 0$ : $-e^{-x} \leq e^{-x}\cos x \leq e^{-x}$. Les bornes tendent vers $0$ : la limite est $0$.

### Exercice 26 — Encadrer un quotient <span class="etoiles">★★</span>

Déterminer $\displaystyle\lim_{x\to+\infty} \frac{2x + \cos x}{x + 1}$.

??? success "Correction"
    Pour $x > 0$, de $-1 \leq \cos x \leq 1$ on tire, en divisant par $x + 1 > 0$ :

    $$\frac{2x - 1}{x + 1} \leq \frac{2x + \cos x}{x + 1} \leq \frac{2x + 1}{x + 1}.$$

    Les deux bornes tendent vers $2$ (termes dominants). Par les gendarmes, la limite est $2$.

### Exercice 27 — Minorer, encadrer <span class="etoiles">★★</span>

1. Montrer que pour tout réel $x$ : $x \sin x \geq -|x|$. En déduire les limites de $f(x) = x^2 + x\sin x$ en $+\infty$ et en $-\infty$.
2. Déterminer $\displaystyle\lim_{x\to+\infty} \frac{x^2 + 3\sin x}{x^2 + 1}$.

??? success "Correction"
    **1.** $|x \sin x| = |x|\,|\sin x| \leq |x|$, donc $x\sin x \geq -|x|$. Ainsi $f(x) \geq x^2 - |x| = |x|\,(|x| - 1)$.

    Quand $x \to \pm\infty$, $|x| \to +\infty$, donc $|x|(|x| - 1) \to +\infty$. Par comparaison, $f(x) \to +\infty$ en $+\infty$ et en $-\infty$.

    **2.** $\dfrac{x^2 - 3}{x^2 + 1} \leq \dfrac{x^2 + 3\sin x}{x^2 + 1} \leq \dfrac{x^2 + 3}{x^2 + 1}$, et les deux bornes tendent vers $1$. La limite est $1$.

### Exercice 28 — Revenir à la définition <span class="etoiles">★★★</span>

1. Soit $f(x) = \dfrac{2x + 1}{x}$ pour $x > 0$. Soit $\varepsilon > 0$. Trouver un réel $B$ tel que, pour tout $x > B$, $|f(x) - 2| < \varepsilon$. Que vient-on de démontrer ?
2. Démontrer à l'aide de la définition que $\displaystyle\lim_{x\to+\infty} (x^2 - x) = +\infty$. *Indication : montrer d'abord que $x^2 - x \geq x$ pour $x \geq 2$.*

??? success "Correction"
    **1.** $f(x) - 2 = \dfrac{2x + 1 - 2x}{x} = \dfrac{1}{x}$. Pour $x > 0$ : $|f(x) - 2| < \varepsilon \iff \dfrac{1}{x} < \varepsilon \iff x > \dfrac{1}{\varepsilon}$.

    Le réel $B = \dfrac{1}{\varepsilon}$ convient. On a démontré, avec la définition, que $\displaystyle\lim_{x\to+\infty} f(x) = 2$.

    **2.** Pour $x \geq 2$ : $x^2 - x - x = x(x - 2) \geq 0$, donc $x^2 - x \geq x$.

    Soit $A$ un réel. On pose $B = \max(2, A)$. Pour $x > B$, on a $x \geq 2$ et $x > A$, donc $x^2 - x \geq x > A$. C'est exactement la définition de $\displaystyle\lim_{x\to+\infty} (x^2 - x) = +\infty$.
