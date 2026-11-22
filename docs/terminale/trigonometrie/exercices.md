# Exercices corrigés — Fonctions sinus et cosinus

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Cercle trigonométrique et formules | 1 à 5 |
| 2. Équations et inéquations | 6 à 11 |
| 3. Parité et périodicité | 12 à 14 |
| 4. Dérivées et études de fonctions | 15 à 21 |
| 5. Limites | 22 à 25 |
| 6. Approfondissement | 26 à 28 |

---

## Thème 1 — Cercle trigonométrique et formules

### Exercice 1 — Valeurs exactes <span class="etoiles">★</span>

Donner la valeur exacte de :

1. $\cos\frac{2\pi}{3}$
2. $\sin\frac{5\pi}{6}$
3. $\cos\left(-\frac{\pi}{4}\right)$
4. $\sin\frac{7\pi}{6}$
5. $\cos\frac{11\pi}{3}$

??? success "Correction"
    1. $\cos\frac{2\pi}{3} = \cos\left(\pi - \frac{\pi}{3}\right) = -\cos\frac{\pi}{3} = -\frac{1}{2}$.
    2. $\sin\frac{5\pi}{6} = \sin\left(\pi - \frac{\pi}{6}\right) = \sin\frac{\pi}{6} = \frac{1}{2}$.
    3. $\cos\left(-\frac{\pi}{4}\right) = \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$.
    4. $\sin\frac{7\pi}{6} = \sin\left(\pi + \frac{\pi}{6}\right) = -\frac{1}{2}$.
    5. $\frac{11\pi}{3} = 4\pi - \frac{\pi}{3}$, donc $\cos\frac{11\pi}{3} = \cos\left(-\frac{\pi}{3}\right) = \frac{1}{2}$.

### Exercice 2 — Mesure principale <span class="etoiles">★</span>

La **mesure principale** d'un réel $x$ est l'unique réel de $]-\pi \,;\, \pi]$ associé au même point du cercle. Déterminer celle de $\frac{17\pi}{4}$, de $-\frac{11\pi}{6}$ et de $\frac{25\pi}{3}$.

??? success "Correction"
    - $\frac{17\pi}{4} = 4\pi + \frac{\pi}{4}$ : mesure principale $\frac{\pi}{4}$.
    - $-\frac{11\pi}{6} = -2\pi + \frac{\pi}{6}$ : mesure principale $\frac{\pi}{6}$.
    - $\frac{25\pi}{3} = 8\pi + \frac{\pi}{3}$ : mesure principale $\frac{\pi}{3}$.

### Exercice 3 — Du sinus au cosinus <span class="etoiles">★★</span>

On sait que $\sin x = \frac{3}{5}$ et $x \in \left[\frac{\pi}{2} \,;\, \pi\right]$. Calculer $\cos x$, puis $\sin(2x)$.

??? success "Correction"
    $\cos^2 x = 1 - \sin^2 x = 1 - \frac{9}{25} = \frac{16}{25}$, donc $\cos x = \pm\frac{4}{5}$. Sur $\left[\frac{\pi}{2} \,;\, \pi\right]$, $\cos x \leq 0$, donc $\cos x = -\frac{4}{5}$.

    $\sin(2x) = 2\sin x\cos x = 2 \times \frac{3}{5} \times \left(-\frac{4}{5}\right) = -\frac{24}{25}$.

### Exercice 4 — Simplifier avec les angles associés <span class="etoiles">★★</span>

Simplifier $A = \cos(\pi - x) + \cos(\pi + x) + \sin\left(\frac{\pi}{2} - x\right)$ et $B = \sin(-x) + \sin(\pi - x) + \cos\left(\frac{\pi}{2} + x\right)$.

??? success "Correction"
    $A = -\cos x - \cos x + \cos x = -\cos x$.

    $B = -\sin x + \sin x - \sin x = -\sin x$.

### Exercice 5 — Une valeur exacte inattendue <span class="etoiles">★★★</span>

1. En écrivant $\frac{\pi}{12} = \frac{\pi}{3} - \frac{\pi}{4}$, calculer la valeur exacte de $\cos\frac{\pi}{12}$.
2. En déduire $\sin\frac{\pi}{12}$.

??? success "Correction"
    **1.** $\cos\left(\frac{\pi}{3} - \frac{\pi}{4}\right) = \cos\frac{\pi}{3}\cos\frac{\pi}{4} + \sin\frac{\pi}{3}\sin\frac{\pi}{4} = \frac{1}{2} \cdot \frac{\sqrt{2}}{2} + \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{2}}{2} = \dfrac{\sqrt{2} + \sqrt{6}}{4}$.

    **2.** $\sin\left(\frac{\pi}{3} - \frac{\pi}{4}\right) = \sin\frac{\pi}{3}\cos\frac{\pi}{4} - \cos\frac{\pi}{3}\sin\frac{\pi}{4} = \dfrac{\sqrt{6} - \sqrt{2}}{4}$.

---

## Thème 2 — Équations et inéquations

*Méthodes associées : [Méthode 1](methodes.md#methode-1-resoudre-une-equation-trigonometrique) et [Méthode 2](methodes.md#methode-2-resoudre-une-inequation-trigonometrique).*

### Exercice 6 — Équation en cosinus <span class="etoiles">★</span>

Résoudre $\cos x = \frac{1}{2}$ dans $\mathbb{R}$, puis dans $[0 \,;\, 2\pi[$.

??? success "Correction"
    Dans $\mathbb{R}$ : $x = \frac{\pi}{3} + 2k\pi$ ou $x = -\frac{\pi}{3} + 2k\pi$, $k \in \mathbb{Z}$.

    Dans $[0 \,;\, 2\pi[$ : $\mathcal{S} = \left\{\frac{\pi}{3} \,;\, \frac{5\pi}{3}\right\}$.

### Exercice 7 — Équation en sinus <span class="etoiles">★</span>

Résoudre $\sin x = -\frac{\sqrt{2}}{2}$ dans $]-\pi \,;\, \pi]$.

??? success "Correction"
    $-\frac{\sqrt{2}}{2} = \sin\left(-\frac{\pi}{4}\right)$. Donc $x = -\frac{\pi}{4} + 2k\pi$ ou $x = \pi + \frac{\pi}{4} + 2k\pi = \frac{5\pi}{4} + 2k\pi$. Dans $]-\pi \,;\, \pi]$ : $x = -\frac{\pi}{4}$ ou $x = \frac{5\pi}{4} - 2\pi = -\frac{3\pi}{4}$.

    $\mathcal{S} = \left\{-\frac{3\pi}{4} \,;\, -\frac{\pi}{4}\right\}$.

### Exercice 8 — Avec un coefficient <span class="etoiles">★★</span>

Résoudre $\cos(2x) = 0$ dans $[0 \,;\, 2\pi[$.

??? success "Correction"
    $\cos X = 0 \iff X = \frac{\pi}{2} + k\pi$. Donc $2x = \frac{\pi}{2} + k\pi$, soit $x = \frac{\pi}{4} + \frac{k\pi}{2}$. Pour $k = 0, 1, 2, 3$ :

    $\mathcal{S} = \left\{\frac{\pi}{4} \,;\, \frac{3\pi}{4} \,;\, \frac{5\pi}{4} \,;\, \frac{7\pi}{4}\right\}$.

### Exercice 9 — Équation du second degré en $\sin x$ <span class="etoiles">★★</span>

Résoudre $2\sin^2 x - \sin x - 1 = 0$ dans $[0 \,;\, 2\pi[$.

??? success "Correction"
    On pose $X = \sin x$ : $2X^2 - X - 1 = (2X + 1)(X - 1) = 0$, donc $X = 1$ ou $X = -\frac{1}{2}$.

    - $\sin x = 1 \iff x = \frac{\pi}{2}$ (dans $[0 \,;\, 2\pi[$).
    - $\sin x = -\frac{1}{2} = \sin\left(-\frac{\pi}{6}\right) \iff x = \frac{7\pi}{6}$ ou $x = \frac{11\pi}{6}$.

    $\mathcal{S} = \left\{\frac{\pi}{2} \,;\, \frac{7\pi}{6} \,;\, \frac{11\pi}{6}\right\}$.

### Exercice 10 — Inéquation en cosinus <span class="etoiles">★★</span>

Résoudre $\cos x \geq \frac{1}{2}$ dans $[-\pi \,;\, \pi]$, puis dans $[0 \,;\, 2\pi]$.

??? success "Correction"
    Sur le cercle, les points d'abscisse au moins $\frac{1}{2}$ forment l'arc compris entre les points associés à $-\frac{\pi}{3}$ et $\frac{\pi}{3}$, du côté du point $I$.

    - Dans $[-\pi \,;\, \pi]$ : $\mathcal{S} = \left[-\frac{\pi}{3} \,;\, \frac{\pi}{3}\right]$.
    - Dans $[0 \,;\, 2\pi]$ : $\mathcal{S} = \left[0 \,;\, \frac{\pi}{3}\right] \cup \left[\frac{5\pi}{3} \,;\, 2\pi\right]$.

### Exercice 11 — Inéquation en sinus <span class="etoiles">★★</span>

Résoudre $\sin x < \frac{1}{2}$ dans $[0 \,;\, 2\pi[$.

??? success "Correction"
    $\sin x = \frac{1}{2}$ pour $x = \frac{\pi}{6}$ et $x = \frac{5\pi}{6}$. Les points d'ordonnée supérieure ou égale à $\frac{1}{2}$ forment l'arc « du haut », entre ces deux valeurs. On garde le reste :

    $\mathcal{S} = \left[0 \,;\, \frac{\pi}{6}\right[ \cup \left]\frac{5\pi}{6} \,;\, 2\pi\right[$.

---

## Thème 3 — Parité et périodicité

*Méthode associée : [Méthode 3](methodes.md#methode-3-exploiter-parite-et-periodicite).*

### Exercice 12 — Paire, impaire ou ni l'un ni l'autre ? <span class="etoiles">★</span>

Étudier la parité de $f(x) = x\sin x$, $g(x) = \sin x\cos x$ et $h(x) = \cos x + \sin x$.

??? success "Correction"
    - $f(-x) = (-x)\sin(-x) = (-x)(-\sin x) = f(x)$ : $f$ est **paire**.
    - $g(-x) = (-\sin x)\cos x = -g(x)$ : $g$ est **impaire**.
    - $h(-x) = \cos x - \sin x$. Pour $x = \frac{\pi}{4}$ : $h\left(\frac{\pi}{4}\right) = \sqrt{2}$ et $h\left(-\frac{\pi}{4}\right) = 0$, qui n'est égal ni à $\sqrt{2}$ ni à $-\sqrt{2}$. $h$ n'est **ni paire ni impaire**.

### Exercice 13 — Trouver une période <span class="etoiles">★★</span>

Montrer que $x \mapsto \cos(3x)$ est périodique de période $\frac{2\pi}{3}$, et que $x \mapsto \sin\left(\frac{x}{2}\right)$ est périodique de période $4\pi$.

??? success "Correction"
    $\cos\left(3\left(x + \frac{2\pi}{3}\right)\right) = \cos(3x + 2\pi) = \cos(3x)$.

    $\sin\left(\frac{x + 4\pi}{2}\right) = \sin\left(\frac{x}{2} + 2\pi\right) = \sin\frac{x}{2}$.

### Exercice 14 — Réduire l'intervalle d'étude <span class="etoiles">★★</span>

Soit $f(x) = \cos(2x) + 2\cos x$. Montrer qu'il suffit d'étudier $f$ sur $[0 \,;\, \pi]$ pour connaître sa courbe sur $\mathbb{R}$.

??? success "Correction"
    $f(x + 2\pi) = \cos(2x + 4\pi) + 2\cos(x + 2\pi) = f(x)$ : $f$ est $2\pi$-périodique. On l'étudie sur $[-\pi \,;\, \pi]$.

    $f(-x) = \cos(-2x) + 2\cos(-x) = f(x)$ : $f$ est paire. Sa courbe sur $[-\pi \,;\, 0]$ s'obtient par symétrie par rapport à l'axe des ordonnées à partir de celle sur $[0 \,;\, \pi]$.

---

## Thème 4 — Dérivées et études de fonctions

*Méthode associée : [Méthode 4](methodes.md#methode-4-etudier-le-signe-dune-derivee-trigonometrique).*

### Exercice 15 — Calculs de dérivées <span class="etoiles">★</span>

Dériver :

1. $f(x) = 3\sin x - 2\cos x$
2. $g(x) = \sin(2x + 1)$
3. $h(x) = \cos^2 x$
4. $k(x) = x\sin x$
5. $m(x) = e^x\cos x$

??? success "Correction"
    1. $f'(x) = 3\cos x + 2\sin x$.
    2. $g'(x) = 2\cos(2x + 1)$.
    3. $h'(x) = 2\cos x \times (-\sin x) = -2\sin x\cos x = -\sin(2x)$.
    4. $k'(x) = \sin x + x\cos x$.
    5. $m'(x) = e^x\cos x - e^x\sin x = e^x(\cos x - \sin x)$.

### Exercice 16 — L'inégalité $\sin x \leq x$ <span class="etoiles">★★</span>

Soit $f(x) = x - \sin x$ sur $[0 \,;\, +\infty[$. Étudier les variations de $f$ et en déduire que $\sin x \leq x$ pour tout $x \geq 0$.

??? success "Correction"
    $f'(x) = 1 - \cos x \geq 0$ : $f$ est croissante sur $[0 \,;\, +\infty[$. Donc $f(x) \geq f(0) = 0$, c'est-à-dire $\sin x \leq x$.

    *On retrouve, sans argument d'aire, l'inégalité démontrée dans le cours.*

### Exercice 17 — L'inégalité $\cos x \geq 1 - \frac{x^2}{2}$ <span class="etoiles">★★</span>

Soit $g(x) = \cos x - 1 + \frac{x^2}{2}$ sur $[0 \,;\, +\infty[$.

1. En utilisant l'exercice 16, étudier les variations de $g$.
2. En déduire que $\cos x \geq 1 - \frac{x^2}{2}$ pour tout réel $x$.

??? success "Correction"
    **1.** $g'(x) = -\sin x + x \geq 0$ d'après l'exercice 16. $g$ est croissante, donc $g(x) \geq g(0) = 0$ pour $x \geq 0$.

    **2.** On a donc $\cos x \geq 1 - \frac{x^2}{2}$ pour $x \geq 0$. Les deux membres sont des fonctions paires de $x$, donc l'inégalité est vraie aussi pour $x \leq 0$.

### Exercice 18 — La fonction $\sin(2x)$ <span class="etoiles">★★</span>

Étudier les variations de $f(x) = \sin(2x)$ sur $[0 \,;\, \pi]$.

??? success "Correction"
    $f'(x) = 2\cos(2x)$. Pour $x \in [0 \,;\, \pi]$, $2x \in [0 \,;\, 2\pi]$, et $\cos(2x) > 0 \iff 2x \in \left[0 \,;\, \frac{\pi}{2}\right[ \cup \left]\frac{3\pi}{2} \,;\, 2\pi\right] \iff x \in \left[0 \,;\, \frac{\pi}{4}\right[ \cup \left]\frac{3\pi}{4} \,;\, \pi\right]$.

    | $x$ | $0$ | | $\frac{\pi}{4}$ | | $\frac{3\pi}{4}$ | | $\pi$ |
    |---|---|---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
    | $f(x)$ | $0$ | $\nearrow$ | $1$ | $\searrow$ | $-1$ | $\nearrow$ | $0$ |

### Exercice 19 — Une étude complète <span class="etoiles">★★</span>

On reprend $f(x) = \cos(2x) + 2\cos x$ sur $[0 \,;\, \pi]$ (exercice 14).

1. Montrer que $f'(x) = -2\sin x\,(2\cos x + 1)$.
2. Dresser le tableau de variations de $f$ sur $[0 \,;\, \pi]$.

??? success "Correction"
    **1.** $f'(x) = -2\sin(2x) - 2\sin x = -4\sin x\cos x - 2\sin x = -2\sin x\,(2\cos x + 1)$.

    **2.** Sur $[0 \,;\, \pi]$ : $\sin x \geq 0$, et $2\cos x + 1 > 0 \iff x < \frac{2\pi}{3}$. Donc $f' \leq 0$ sur $\left[0 \,;\, \frac{2\pi}{3}\right]$ et $f' \geq 0$ sur $\left[\frac{2\pi}{3} \,;\, \pi\right]$.

    $f(0) = 3$, $f\left(\frac{2\pi}{3}\right) = \cos\frac{4\pi}{3} + 2\cos\frac{2\pi}{3} = -\frac{1}{2} - 1 = -\frac{3}{2}$, $f(\pi) = 1 - 2 = -1$.

    | $x$ | $0$ | | $\frac{2\pi}{3}$ | | $\pi$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | $0$ | $-$ | $0$ | $+$ | $0$ |
    | $f(x)$ | $3$ | $\searrow$ | $-\frac{3}{2}$ | $\nearrow$ | $-1$ |

### Exercice 20 — Inégalité de Jordan <span class="etoiles">★★★</span>

1. Montrer que $\sin$ est concave sur $\left[0 \,;\, \frac{\pi}{2}\right]$.
2. En déduire que pour tout $x \in \left[0 \,;\, \frac{\pi}{2}\right]$ : $\dfrac{2}{\pi}x \leq \sin x \leq x$.

??? success "Correction"
    **1.** $\sin'' = -\sin \leq 0$ sur $\left[0 \,;\, \frac{\pi}{2}\right]$.

    **2.** Une fonction concave est **au-dessus de ses sécantes** et **en dessous de ses tangentes** (chapitre 3).

    - La sécante entre les points $(0 \,;\, 0)$ et $\left(\frac{\pi}{2} \,;\, 1\right)$ a pour équation $y = \frac{2}{\pi}x$ : donc $\sin x \geq \frac{2}{\pi}x$.
    - La tangente en $0$ a pour équation $y = x$ : donc $\sin x \leq x$.

### Exercice 21 — Oscillation amortie <span class="etoiles">★★</span>

Soit $f(t) = e^{-t}\cos t$ sur $[0 \,;\, +\infty[$.

1. Montrer que $-e^{-t} \leq f(t) \leq e^{-t}$ et en déduire la limite de $f$ en $+\infty$.
2. Calculer $f'(t)$.
3. Résoudre $f(t) = 0$ sur $[0 \,;\, 2\pi]$.

??? success "Correction"
    **1.** $-1 \leq \cos t \leq 1$ et $e^{-t} > 0$, d'où l'encadrement. Les deux bornes tendent vers $0$ : $f(t) \to 0$ (gendarmes).

    **2.** $f'(t) = -e^{-t}\cos t - e^{-t}\sin t = -e^{-t}(\cos t + \sin t)$.

    **3.** $e^{-t} > 0$, donc $f(t) = 0 \iff \cos t = 0 \iff t = \frac{\pi}{2}$ ou $t = \frac{3\pi}{2}$ (dans $[0 \,;\, 2\pi]$).

---

## Thème 5 — Limites

*Méthode associée : [Méthode 5](methodes.md#methode-5-calculer-une-limite-avec-sinus-ou-cosinus).*

### Exercice 22 — Limites en $0$ et en l'infini <span class="etoiles">★</span>

Déterminer :

1. $\displaystyle\lim_{x\to 0} \frac{\sin(3x)}{x}$
2. $\displaystyle\lim_{x\to 0} \frac{\sin x}{2x}$
3. $\displaystyle\lim_{x\to+\infty} \frac{\sin x}{x}$

??? success "Correction"
    1. $\frac{\sin(3x)}{x} = 3 \times \frac{\sin(3x)}{3x} \to 3$.
    2. $\frac{1}{2} \times \frac{\sin x}{x} \to \frac{1}{2}$.
    3. Pour $x > 0$, $-\frac{1}{x} \leq \frac{\sin x}{x} \leq \frac{1}{x}$ : par les gendarmes, la limite est $0$.

### Exercice 23 — Limite de $\frac{1 - \cos x}{x^2}$ <span class="etoiles">★★</span>

En utilisant $1 - \cos x = 2\sin^2\frac{x}{2}$, déterminer $\displaystyle\lim_{x\to 0} \frac{1 - \cos x}{x^2}$.

??? success "Correction"
    $\dfrac{1 - \cos x}{x^2} = \dfrac{2\sin^2\frac{x}{2}}{x^2} = \dfrac{1}{2}\left(\dfrac{\sin\frac{x}{2}}{\frac{x}{2}}\right)^2$. Avec $X = \frac{x}{2} \to 0$, le quotient tend vers $1$. La limite vaut $\frac{1}{2}$.

### Exercice 24 — $x\sin\frac{1}{x}$ <span class="etoiles">★★</span>

Déterminer $\displaystyle\lim_{x\to+\infty} x\sin\frac{1}{x}$ et $\displaystyle\lim_{x\to 0} x\sin\frac{1}{x}$.

??? success "Correction"
    **En $+\infty$.** Avec $X = \frac{1}{x} \to 0^+$ : $x\sin\frac{1}{x} = \frac{\sin X}{X} \to 1$.

    **En $0$.** $\left|x\sin\frac{1}{x}\right| \leq |x| \to 0$ : par les gendarmes, la limite est $0$.

### Exercice 25 — La tangente <span class="etoiles">★★★</span>

On pose $\tan x = \dfrac{\sin x}{\cos x}$ pour $x \in \left]-\frac{\pi}{2} \,;\, \frac{\pi}{2}\right[$.

1. Déterminer $\displaystyle\lim_{x\to 0} \frac{\tan x}{x}$.
2. Montrer que $\tan' = 1 + \tan^2 = \dfrac{1}{\cos^2}$ et en déduire les variations de $\tan$.
3. Déterminer les limites de $\tan$ en $\frac{\pi}{2}^-$ et en $-\frac{\pi}{2}^+$.

??? success "Correction"
    **1.** $\dfrac{\tan x}{x} = \dfrac{\sin x}{x} \times \dfrac{1}{\cos x} \to 1 \times 1 = 1$.

    **2.** Par la formule du quotient : $\tan'(x) = \dfrac{\cos x \cos x - \sin x(-\sin x)}{\cos^2 x} = \dfrac{\cos^2 x + \sin^2 x}{\cos^2 x} = \dfrac{1}{\cos^2 x}$, et aussi $= 1 + \dfrac{\sin^2 x}{\cos^2 x} = 1 + \tan^2 x$. Cette dérivée est strictement positive : $\tan$ est strictement croissante.

    **3.** En $\frac{\pi}{2}^-$ : $\sin x \to 1$ et $\cos x \to 0^+$, donc $\tan x \to +\infty$. Par imparité, $\tan x \to -\infty$ en $-\frac{\pi}{2}^+$.

---

## Thème 6 — Approfondissement

### Exercice 26 — Une somme sinus + cosinus <span class="etoiles">★★★</span>

1. Montrer que pour tout réel $x$ : $\sin x + \cos x = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)$.
2. En déduire le maximum de $x \mapsto \sin x + \cos x$ sur $\mathbb{R}$.
3. Résoudre $\sin x + \cos x = 1$ dans $[0 \,;\, 2\pi[$.

??? success "Correction"
    **1.** $\sqrt{2}\sin\left(x + \frac{\pi}{4}\right) = \sqrt{2}\left(\sin x\cos\frac{\pi}{4} + \cos x\sin\frac{\pi}{4}\right) = \sqrt{2} \times \frac{\sqrt{2}}{2}(\sin x + \cos x) = \sin x + \cos x$.

    **2.** Le maximum de $\sin$ est $1$, atteint quand $x + \frac{\pi}{4} = \frac{\pi}{2}$, soit $x = \frac{\pi}{4}$. Le maximum vaut $\sqrt{2}$.

    **3.** $\sin\left(x + \frac{\pi}{4}\right) = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} = \sin\frac{\pi}{4}$. Donc $x + \frac{\pi}{4} = \frac{\pi}{4} + 2k\pi$ ou $x + \frac{\pi}{4} = \frac{3\pi}{4} + 2k\pi$, soit $x = 2k\pi$ ou $x = \frac{\pi}{2} + 2k\pi$. Dans $[0 \,;\, 2\pi[$ : $\mathcal{S} = \left\{0 \,;\, \frac{\pi}{2}\right\}$.

### Exercice 27 — L'équation $f'' + f = 0$ <span class="etoiles">★★★</span>

1. Vérifier que pour tous réels $A$ et $B$, la fonction $f(x) = A\cos x + B\sin x$ vérifie $f'' + f = 0$.
2. Soit $g$ deux fois dérivable sur $\mathbb{R}$ telle que $g'' + g = 0$, $g(0) = 0$ et $g'(0) = 0$. On pose $E(x) = g(x)^2 + g'(x)^2$. Montrer que $E' = 0$ et en déduire que $g$ est la fonction nulle.
3. *(Bonus.)* Soit $f$ telle que $f'' + f = 0$. Montrer que $f(x) = f(0)\cos x + f'(0)\sin x$ pour tout $x$.

??? success "Correction"
    **1.** $f'(x) = -A\sin x + B\cos x$ et $f''(x) = -A\cos x - B\sin x = -f(x)$.

    **2.** $E'(x) = 2g(x)g'(x) + 2g'(x)g''(x) = 2g'(x)\big(g(x) + g''(x)\big) = 0$. Donc $E$ est constante (chapitre 3, § 1.3), égale à $E(0) = 0$. Ainsi $g(x)^2 + g'(x)^2 = 0$, une somme de carrés nulle : $g(x) = 0$ pour tout $x$.

    **3.** La fonction $g(x) = f(x) - f(0)\cos x - f'(0)\sin x$ vérifie $g'' + g = 0$ (par linéarité et la question 1), $g(0) = 0$ et $g'(0) = f'(0) - f'(0) = 0$. D'après la question 2, $g = 0$.

    *Toutes les solutions de $y'' + y = 0$ sont donc de la forme $A\cos x + B\sin x$. C'est l'équation d'un ressort sans frottement : la quantité $E$ est son énergie, qui se conserve.*

### Exercice 28 — Résoudre $\cos x = x$ <span class="etoiles">★★</span>

1. Montrer que l'équation $\cos x = x$ admet une unique solution $\alpha$ dans $[0 \,;\, 1]$, puis dans $\mathbb{R}$.
2. Écrire une fonction Python qui donne un encadrement de $\alpha$ d'amplitude $10^{-6}$ par dichotomie.

??? success "Correction"
    **1.** Soit $g(x) = \cos x - x$, continue sur $\mathbb{R}$. Sur $[0 \,;\, 1]$, $\sin x \geq 0$ donc $g'(x) = -\sin x - 1 \leq -1 < 0$ : $g$ est strictement décroissante. $g(0) = 1 > 0$ et $g(1) = \cos 1 - 1 < 0$ : par le corollaire du TVI, il y a une unique solution $\alpha \in [0 \,;\, 1]$.

    En dehors de $[0 \,;\, 1]$, il n'y a pas de solution : si $x > 1$, alors $\cos x \leq 1 < x$ ; si $-1 \leq x < 0$, alors $\cos x > 0 > x$ (car $|x| < \frac{\pi}{2}$) ; si $x < -1$, alors $\cos x \geq -1 > x$. Donc $\alpha$ est l'unique solution sur $\mathbb{R}$.

    **2.**

    ```python
    from math import cos

    def dicho():
        a, b = 0, 1
        while b - a > 1e-6:
            m = (a + b) / 2
            if cos(m) - m > 0:
                a = m
            else:
                b = m
        return a, b
    ```

    On obtient $\alpha \approx 0{,}739085$. *Ce nombre s'obtient aussi en appuyant de nombreuses fois sur la touche « cos » d'une calculatrice en radians !*
