# Exercices corrigés — Trigonométrie

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**, sauf les exercices Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Radians et cercle trigonométrique | 1 à 5 |
| 2. Valeurs remarquables et angles associés | 6 à 11 |
| 3. Équations et inéquations | 12 à 17 |
| 4. Fonctions cosinus et sinus | 18 à 23 |
| 5. Approfondissement | 24 à 28 |

---

## Thème 1 — Radians et cercle trigonométrique

*Méthode associée : [Méthode 1](methodes.md#methode-1-convertir-placer-un-point-trouver-la-mesure-principale).*

### Exercice 1 — Conversions <span class="etoiles">★</span>

Convertir en radians : $15°$, $72°$, $210°$, $270°$. Convertir en degrés : $\frac{5\pi}{4}$, $\frac{\pi}{12}$, $\frac{7\pi}{6}$.

??? success "Correction"
    $15° = \frac{\pi}{12}$ ; $72° = \frac{2\pi}{5}$ ; $210° = \frac{7\pi}{6}$ ; $270° = \frac{3\pi}{2}$. Et $\frac{5\pi}{4} = 225°$ ; $\frac{\pi}{12} = 15°$ ; $\frac{7\pi}{6} = 210°$.

### Exercice 2 — Mesures principales <span class="etoiles">★</span>

Déterminer la mesure principale de : $\frac{17\pi}{3}$ ; $-\frac{13\pi}{4}$ ; $\frac{31\pi}{6}$ ; $15\pi$.

??? success "Correction"
    - $\frac{17\pi}{3} = 6\pi - \frac{\pi}{3}$ : $-\frac{\pi}{3}$.
    - $-\frac{13\pi}{4} = -4\pi + \frac{3\pi}{4}$ : $\frac{3\pi}{4}$.
    - $\frac{31\pi}{6} = 4\pi + \frac{7\pi}{6} = 6\pi - \frac{5\pi}{6}$ : $-\frac{5\pi}{6}$.
    - $15\pi = 14\pi + \pi$ : $\pi$.

### Exercice 3 — Même point ? <span class="etoiles">★</span>

Les réels $\frac{\pi}{5}$ et $\frac{21\pi}{5}$ correspondent-ils au même point du cercle ? Et $\frac{\pi}{5}$ et $\frac{16\pi}{5}$ ?

??? success "Correction"
    $\frac{21\pi}{5} - \frac{\pi}{5} = 4\pi = 2 \times 2\pi$ : oui. $\frac{16\pi}{5} - \frac{\pi}{5} = 3\pi$, qui n'est pas un multiple de $2\pi$ : non (ce sont des points diamétralement opposés).

### Exercice 4 — Longueur d'arc <span class="etoiles">★★</span>

Sur un cercle de rayon $r$, un angle de $\theta$ radians intercepte un arc de longueur $r\theta$.

1. Quelle est la longueur de l'arc intercepté par un angle de $\frac{\pi}{3}$ sur un cercle de rayon $6$ cm ?
2. La Terre a un rayon d'environ $6\,400$ km. Quelle distance (le long de la surface) sépare deux villes situées sur le même méridien, avec une différence de latitude de $1°$ ?

??? success "Correction"
    **1.** $6 \times \frac{\pi}{3} = 2\pi \approx 6{,}3$ cm.

    **2.** $1° = \frac{\pi}{180}$ rad, donc $6\,400 \times \frac{\pi}{180} \approx 112$ km. *C'est ainsi qu'Ératosthène estima le rayon de la Terre, au IIIᵉ siècle avant notre ère.*

### Exercice 5 — Placer des points <span class="etoiles">★</span>

Placer sur un cercle trigonométrique les points associés à $\frac{2\pi}{3}$, $-\frac{\pi}{4}$, $\frac{7\pi}{6}$ et $\frac{9\pi}{2}$. Dans quel quadrant se trouve chacun ?

??? success "Correction"
    $\frac{2\pi}{3}$ : en haut à gauche. $-\frac{\pi}{4}$ : en bas à droite. $\frac{7\pi}{6}$ : en bas à gauche. $\frac{9\pi}{2} = 4\pi + \frac{\pi}{2}$ : au point $J$, sur l'axe des ordonnées.

---

## Thème 2 — Valeurs remarquables et angles associés

*Méthodes associées : [Méthode 2](methodes.md#methode-2-calculer-le-cosinus-ou-le-sinus-dun-angle-remarquable), [Méthode 3](methodes.md#methode-3-calculer-cos-x-connaissant-sin-x-ou-linverse) et [Méthode 4](methodes.md#methode-4-simplifier-une-expression-avec-des-angles-associes).*

### Exercice 6 — Calculer <span class="etoiles">★</span>

Calculer : $\cos\frac{2\pi}{3}$ ; $\sin\frac{5\pi}{6}$ ; $\cos\left(-\frac{\pi}{4}\right)$ ; $\sin\frac{7\pi}{6}$ ; $\cos\frac{3\pi}{4}$ ; $\sin\left(-\frac{\pi}{3}\right)$.

??? success "Correction"
    $-\frac{1}{2}$ ; $\frac{1}{2}$ ; $\frac{\sqrt{2}}{2}$ ; $-\frac{1}{2}$ ; $-\frac{\sqrt{2}}{2}$ ; $-\frac{\sqrt{3}}{2}$.

### Exercice 7 — Grands angles <span class="etoiles">★★</span>

Calculer : $\cos\frac{13\pi}{3}$ ; $\sin\frac{19\pi}{6}$ ; $\cos(2027\pi)$ ; $\sin\frac{-17\pi}{4}$.

??? success "Correction"
    - $\frac{13\pi}{3} = 4\pi + \frac{\pi}{3}$ : $\frac{1}{2}$.
    - $\frac{19\pi}{6} = 2\pi + \frac{7\pi}{6}$ : $\sin\frac{7\pi}{6} = -\frac{1}{2}$.
    - $2027\pi = 2026\pi + \pi$ : $\cos\pi = -1$.
    - $-\frac{17\pi}{4} = -4\pi - \frac{\pi}{4}$ : $-\frac{\sqrt{2}}{2}$.

### Exercice 8 — Du sinus au cosinus <span class="etoiles">★★</span>

On sait que $\cos x = -\frac{1}{3}$ et que $x \in [-\pi\,;\,0]$. Calculer $\sin x$.

??? success "Correction"
    $\sin^2 x = 1 - \frac{1}{9} = \frac{8}{9}$. Sur $[-\pi\,;\,0]$, le sinus est négatif : $\sin x = -\frac{\sqrt{8}}{3} = -\frac{2\sqrt{2}}{3}$.

### Exercice 9 — Encore <span class="etoiles">★★</span>

On sait que $\sin x = \frac{4}{5}$ et que $x \in \left[\frac{\pi}{2}\,;\,\pi\right]$. Calculer $\cos x$, puis $\cos(\pi - x)$, $\sin(\pi + x)$ et $\cos\left(\frac{\pi}{2} - x\right)$.

??? success "Correction"
    $\cos^2 x = 1 - \frac{16}{25} = \frac{9}{25}$, et $\cos x \leq 0$ sur cet intervalle : $\cos x = -\frac{3}{5}$. Puis $\cos(\pi - x) = -\cos x = \frac{3}{5}$ ; $\sin(\pi + x) = -\sin x = -\frac{4}{5}$ ; $\cos\left(\frac{\pi}{2} - x\right) = \sin x = \frac{4}{5}$.

### Exercice 10 — Simplifier <span class="etoiles">★★</span>

Simplifier : $B = \sin(\pi - x) + \sin(-x)$ ; $C = \cos\left(\frac{\pi}{2} - x\right) - \sin(\pi + x)$ ; $D = \sin(x + \pi) + \cos\left(\frac{\pi}{2} + x\right)$.

??? success "Correction"
    $B = \sin x - \sin x = 0$. $C = \sin x + \sin x = 2\sin x$. Pour $D$ : $\sin(x + \pi) = -\sin x$ et $\cos\left(\frac{\pi}{2} + x\right) = \cos\left(\frac{\pi}{2} - (-x)\right) = \sin(-x) = -\sin x$. Donc $D = -2\sin x$.

### Exercice 11 — Une somme <span class="etoiles">★★★</span>

Calculer, sans calculatrice, $S = \cos\frac{\pi}{5} + \cos\frac{2\pi}{5} + \cos\frac{3\pi}{5} + \cos\frac{4\pi}{5}$.

??? success "Correction"
    $\cos\frac{4\pi}{5} = \cos\left(\pi - \frac{\pi}{5}\right) = -\cos\frac{\pi}{5}$ et $\cos\frac{3\pi}{5} = -\cos\frac{2\pi}{5}$. Donc $S = 0$.

---

## Thème 3 — Équations et inéquations

*Méthode associée : [Méthode 5](methodes.md#methode-5-resoudre-une-equation-ou-une-inequation).*

### Exercice 12 — Cosinus <span class="etoiles">★</span>

Résoudre $\cos x = \frac{\sqrt{2}}{2}$ dans $]-\pi\,;\,\pi]$, puis dans $\mathbb{R}$.

??? success "Correction"
    $\cos x = \cos\frac{\pi}{4}$. Dans $]-\pi\,;\,\pi]$ : $S = \left\{-\frac{\pi}{4}\,;\,\frac{\pi}{4}\right\}$. Dans $\mathbb{R}$ : $x = \frac{\pi}{4} + 2k\pi$ ou $x = -\frac{\pi}{4} + 2k\pi$, $k \in \mathbb{Z}$.

### Exercice 13 — Sinus <span class="etoiles">★</span>

Résoudre $\sin x = \frac{1}{2}$ dans $[0\,;\,2\pi[$.

??? success "Correction"
    $\sin x = \sin\frac{\pi}{6}$ : $x = \frac{\pi}{6}$ ou $x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$. $S = \left\{\frac{\pi}{6}\,;\,\frac{5\pi}{6}\right\}$.

### Exercice 14 — Une valeur négative <span class="etoiles">★★</span>

Résoudre $2\cos x + 1 = 0$ dans $]-\pi\,;\,\pi]$.

??? success "Correction"
    $\cos x = -\frac{1}{2} = \cos\frac{2\pi}{3}$. $S = \left\{-\frac{2\pi}{3}\,;\,\frac{2\pi}{3}\right\}$.

### Exercice 15 — Un carré <span class="etoiles">★★</span>

Résoudre $4\sin^2 x = 3$ dans $]-\pi\,;\,\pi]$.

??? success "Correction"
    $\sin x = \frac{\sqrt{3}}{2}$ ou $\sin x = -\frac{\sqrt{3}}{2}$. Solutions : $\frac{\pi}{3}$, $\frac{2\pi}{3}$, $-\frac{\pi}{3}$, $-\frac{2\pi}{3}$.

### Exercice 16 — Second degré en $\cos x$ <span class="etoiles">★★★</span>

Résoudre $2\cos^2 x - \cos x - 1 = 0$ dans $]-\pi\,;\,\pi]$. *On pourra poser $X = \cos x$.*

??? success "Correction"
    $2X^2 - X - 1 = 0$ : $1$ est racine évidente, et le produit des racines vaut $-\frac{1}{2}$, donc l'autre racine est $-\frac{1}{2}$. Ainsi $\cos x = 1$ ($x = 0$) ou $\cos x = -\frac{1}{2}$ ($x = \pm\frac{2\pi}{3}$). $S = \left\{-\frac{2\pi}{3}\,;\,0\,;\,\frac{2\pi}{3}\right\}$.

### Exercice 17 — Inéquation <span class="etoiles">★★</span>

Résoudre dans $]-\pi\,;\,\pi]$ : $\sin x > \frac{\sqrt{2}}{2}$, puis $\cos x < 0$.

??? success "Correction"
    $\sin x > \frac{\sqrt{2}}{2}$ : arc au-dessus de la droite $y = \frac{\sqrt{2}}{2}$, entre $\frac{\pi}{4}$ et $\frac{3\pi}{4}$ : $S = \left]\frac{\pi}{4}\,;\,\frac{3\pi}{4}\right[$.

    $\cos x < 0$ : moitié gauche du cercle : $S = \left]-\pi\,;\,-\frac{\pi}{2}\right[ \cup \left]\frac{\pi}{2}\,;\,\pi\right]$.

---

## Thème 4 — Fonctions cosinus et sinus

### Exercice 18 — Parité <span class="etoiles">★</span>

Étudier la parité de $f(x) = x\sin x$, $g(x) = \sin x\cos x$ et $h(x) = \cos x + x$.

??? success "Correction"
    $f(-x) = (-x)(-\sin x) = f(x)$ : paire. $g(-x) = -\sin x\cos x = -g(x)$ : impaire. $h(\pi) = -1 + \pi$ et $h(-\pi) = -1 - \pi$ : ni paire ni impaire.

### Exercice 19 — Période <span class="etoiles">★★</span>

Montrer que $f(x) = \cos(2x)$ vérifie $f(x + \pi) = f(x)$. Quelle est l'allure de sa courbe par rapport à celle du cosinus ?

??? success "Correction"
    $\cos(2x + 2\pi) = \cos(2x)$. La courbe est celle du cosinus « comprimée » horizontalement d'un facteur $2$ : elle fait deux oscillations sur un intervalle de longueur $2\pi$.

### Exercice 20 — Lecture de la courbe <span class="etoiles">★</span>

À l'aide de la courbe du cours, donner le nombre de solutions de $\cos x = 0{,}3$ dans $[-2\pi\,;\,2\pi]$, puis de $\sin x = 1$ dans le même intervalle.

??? success "Correction"
    La droite $y = 0{,}3$ coupe la courbe du cosinus $4$ fois sur $[-2\pi\,;\,2\pi]$. La droite $y = 1$ touche la courbe du sinus en $\frac{\pi}{2}$ et $-\frac{3\pi}{2}$ : $2$ solutions.

### Exercice 21 — Une identité <span class="etoiles">★★</span>

Montrer que pour tout réel $x$ : $(\cos x + \sin x)^2 + (\cos x - \sin x)^2 = 2$.

??? success "Correction"
    En développant : $2\cos^2 x + 2\sin^2 x = 2$.

### Exercice 22 — Une autre identité <span class="etoiles">★★</span>

Montrer que pour tout réel $x$ : $\cos^4 x - \sin^4 x = \cos^2 x - \sin^2 x$.

??? success "Correction"
    $\cos^4 x - \sin^4 x = (\cos^2 x - \sin^2 x)(\cos^2 x + \sin^2 x) = \cos^2 x - \sin^2 x$.

### Exercice 23 — Encadrement <span class="etoiles">★★</span>

Montrer que pour tout réel $x$ : $-2 \leq 2\cos x - \sin^2 x \leq 2$. Pour quelles valeurs de $x$ les bornes sont-elles atteintes ?

??? success "Correction"
    Avec $\sin^2 x = 1 - \cos^2 x$ : $2\cos x - \sin^2 x = \cos^2 x + 2\cos x - 1 = (\cos x + 1)^2 - 2$. Comme $0 \leq \cos x + 1 \leq 2$, on a $0 \leq (\cos x + 1)^2 \leq 4$, d'où l'encadrement. Le minimum $-2$ est atteint quand $\cos x = -1$, soit $x = \pi + 2k\pi$ ; le maximum $2$ quand $\cos x = 1$, soit $x = 2k\pi$ ($k \in \mathbb{Z}$).

---

## Thème 5 — Approfondissement

### Exercice 24 — Le cosinus de $\frac{\pi}{6}$ autrement <span class="etoiles">★★</span>

Soit $ABC$ un triangle équilatéral de côté $2$, et $H$ le milieu de $[BC]$.

1. Calculer $AH$.
2. Quelle est la mesure de l'angle $\widehat{BAH}$ ? En déduire $\cos\frac{\pi}{6}$ et $\sin\frac{\pi}{6}$ dans le triangle $ABH$.

??? success "Correction"
    **1.** $(AH)$ est la hauteur et la médiane : $BH = 1$, et par Pythagore $AH = \sqrt{4 - 1} = \sqrt{3}$.

    **2.** $(AH)$ est aussi bissectrice : $\widehat{BAH} = 30° = \frac{\pi}{6}$. Dans $ABH$ rectangle en $H$ : $\cos\frac{\pi}{6} = \frac{AH}{AB} = \frac{\sqrt{3}}{2}$ et $\sin\frac{\pi}{6} = \frac{BH}{AB} = \frac{1}{2}$.

### Exercice 25 — Le cosinus de $\frac{\pi}{5}$ <span class="etoiles">★★★</span>

On admet que $c = \cos\frac{\pi}{5}$ vérifie $4c^2 - 2c - 1 = 0$ (cela se démontre avec les formules de trigonométrie de Terminale).

1. Résoudre l'équation $4X^2 - 2X - 1 = 0$.
2. En déduire $\cos\frac{\pi}{5}$, et le relier au nombre d'or $\varphi = \frac{1 + \sqrt{5}}{2}$.

??? success "Correction"
    **1.** $\Delta = 4 + 16 = 20$, racines $\frac{2 \pm 2\sqrt{5}}{8} = \frac{1 \pm \sqrt{5}}{4}$.

    **2.** $\frac{\pi}{5} \in \left]0\,;\,\frac{\pi}{2}\right[$, donc $\cos\frac{\pi}{5} > 0$ : $\cos\frac{\pi}{5} = \frac{1 + \sqrt{5}}{4} = \frac{\varphi}{2}$. *Le nombre d'or apparaît dans le pentagone régulier.*

### Exercice 26 — Démonstration de $\cos^2 + \sin^2 = 1$ <span class="etoiles">★</span>

Rédiger la démonstration de la relation $\cos^2 x + \sin^2 x = 1$, en précisant le théorème utilisé.

??? success "Correction"
    $M(x)$ a pour coordonnées $(\cos x\,;\,\sin x)$ et appartient au cercle de centre $O$ et de rayon $1$. Dans un repère orthonormé, la distance $OM$ vérifie $OM^2 = \cos^2 x + \sin^2 x$ (c'est le théorème de Pythagore). Comme $OM = 1$, on conclut.

### Exercice 27 — Table de valeurs en Python <span class="etoiles">★★</span>

Écrire un programme Python qui affiche, pour chaque angle de $0°$ à $180°$ par pas de $15°$, sa mesure en radians, son cosinus et son sinus (arrondis à $10^{-3}$). Vérifier les valeurs remarquables.

??? success "Correction"
    ```python
    from math import pi, cos, sin

    for deg in range(0, 181, 15):
        x = deg * pi / 180
        print(deg, round(x, 3), round(cos(x), 3), round(sin(x), 3))
    ```

    On lit par exemple, pour $60°$ : $1{,}047$ ; $0{,}5$ ; $0{,}866$, et $\frac{\sqrt{3}}{2} \approx 0{,}866$.

### Exercice 28 — La méthode d'Archimède <span class="etoiles">★★★</span>

On inscrit un polygone régulier à $n$ côtés dans le cercle de rayon $1$.

1. Montrer que chaque côté mesure $2\sin\frac{\pi}{n}$, et que le périmètre vaut $p_n = 2n\sin\frac{\pi}{n}$. *On considérera le triangle formé par $O$ et un côté, coupé en deux par sa hauteur.*
2. Calculer $p_6$ sans calculatrice.
3. Écrire un programme Python qui affiche $\frac{p_n}{2}$ pour $n = 6$, $12$, $96$, $1\,000$. Vers quoi ces nombres semblent-ils se rapprocher ? Pourquoi ?

??? success "Correction"
    **1.** Le côté $[AB]$ est vu depuis $O$ sous un angle $\frac{2\pi}{n}$. La hauteur issue de $O$ coupe le triangle isocèle $OAB$ en deux triangles rectangles d'angle $\frac{\pi}{n}$ en $O$ et d'hypoténuse $1$ : la moitié du côté vaut $\sin\frac{\pi}{n}$. Donc le côté mesure $2\sin\frac{\pi}{n}$, et $p_n = 2n\sin\frac{\pi}{n}$.

    **2.** $p_6 = 12\sin\frac{\pi}{6} = 6$ : le côté de l'hexagone régulier inscrit est égal au rayon.

    **3.**

    ```python
    from math import sin, pi

    for n in [6, 12, 96, 1000]:
        print(n, n * sin(pi / n))
    ```

    On obtient $3$ ; $3{,}1058$ ; $3{,}1410$ ; $3{,}14158$ : on se rapproche de $\pi$, demi-périmètre du cercle. Archimède, avec $96$ côtés et sans calculatrice, en avait déduit $3{,}1408 < \pi < 3{,}1429$. *Le programme utilise `pi` pour calculer les sinus : c'est une vérification, pas une méthode de calcul de $\pi$.*
