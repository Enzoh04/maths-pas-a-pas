# Exercices corrigés — Droites du plan

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf l'exercice Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Équations cartésiennes | 1 à 6 |
| 2. Équations réduites | 7 à 12 |
| 3. Parallélisme et intersection | 13 à 17 |
| 4. Systèmes linéaires | 18 à 23 |
| 5. Problèmes et approfondissement | 24 à 28 |

---

## Thème 1 — Équations cartésiennes

*Méthode associée : [Méthode 1](methodes.md#methode-1-determiner-une-equation-cartesienne).*

### Exercice 1 — Appartenance <span class="etoiles">★</span>

$d$ a pour équation $3x - 2y + 4 = 0$. Les points $A(0\,;\,2)$, $B(2\,;\,5)$ et $C(-2\,;\,0)$ sont-ils sur $d$ ? Donner un vecteur directeur de $d$.

??? success "Correction"
    $A$ : $0 - 4 + 4 = 0$, oui. $B$ : $6 - 10 + 4 = 0$, oui. $C$ : $-6 - 0 + 4 = -2 \neq 0$, non. Vecteur directeur : $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ (avec $\begin{pmatrix} -b \\ a \end{pmatrix}$).

### Exercice 2 — Point et vecteur directeur <span class="etoiles">★</span>

Déterminer une équation cartésienne de la droite passant par $A(1\,;\,-2)$ et dirigée par $\vec{u}\begin{pmatrix} 4 \\ -1 \end{pmatrix}$.

??? success "Correction"
    $\det\left(\overrightarrow{AM}, \vec{u}\right) = (x - 1)(-1) - 4(y + 2) = 0 \iff -x - 4y - 7 = 0$, ou $x + 4y + 7 = 0$.

### Exercice 3 — Deux points <span class="etoiles">★</span>

Déterminer une équation cartésienne de $(AB)$ avec $A(-3\,;\,1)$ et $B(2\,;\,4)$.

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 5 \\ 3 \end{pmatrix}$ : $3x - 5y + c = 0$. Avec $A$ : $-9 - 5 + c = 0$, $c = 14$. Équation : $3x - 5y + 14 = 0$ (vérification avec $B$ : $6 - 20 + 14 = 0$).

### Exercice 4 — Droites particulières <span class="etoiles">★</span>

Déterminer une équation de la droite passant par $A(2\,;\,-3)$ et parallèle à l'axe des abscisses, puis de celle parallèle à l'axe des ordonnées.

??? success "Correction"
    $y = -3$ (ou $y + 3 = 0$) ; $x = 2$ (ou $x - 2 = 0$).

### Exercice 5 — Coupe avec les axes <span class="etoiles">★★</span>

Déterminer les points d'intersection de $d : 4x - 3y - 12 = 0$ avec les axes, puis tracer $d$.

??? success "Correction"
    $x = 0$ : $y = -4$, point $(0\,;\,-4)$. $y = 0$ : $x = 3$, point $(3\,;\,0)$. On trace la droite passant par ces deux points.

### Exercice 6 — Une famille de droites <span class="etoiles">★★★</span>

Pour tout réel $m$, $d_m$ est l'ensemble des points $M(x\,;\,y)$ tels que $(m - 1)x + my - 2 = 0$.

1. Justifier que $d_m$ est une droite pour tout $m$.
2. Pour quelle valeur de $m$ la droite $d_m$ passe-t-elle par $A(1\,;\,1)$ ?
3. Pour quelle valeur de $m$ est-elle parallèle à l'axe des ordonnées ?
4. Montrer que toutes les droites $d_m$ passent par un même point.

??? success "Correction"
    1. $m - 1$ et $m$ ne peuvent pas être nuls en même temps.
    2. $m - 1 + m - 2 = 0 \iff m = \frac{3}{2}$.
    3. Il faut $b = m = 0$ : $d_0 : -x - 2 = 0$, soit $x = -2$.
    4. L'équation s'écrit $m(x + y) - x - 2 = 0$. Elle est vraie pour tout $m$ si $x + y = 0$ et $x + 2 = 0$ : le point $(-2\,;\,2)$ est sur toutes les droites.

---

## Thème 2 — Équations réduites

*Méthodes associées : [Méthode 2](methodes.md#methode-2-determiner-lequation-reduite-passant-par-deux-points) et [Méthode 3](methodes.md#methode-3-tracer-une-droite-et-lire-son-equation).*

### Exercice 7 — Lire $m$ et $p$ <span class="etoiles">★</span>

Donner le coefficient directeur et l'ordonnée à l'origine de : $y = -3x + 2$ ; $y = \frac{x}{4}$ ; $y = 5$ ; $2x + 3y = 6$.

??? success "Correction"
    $m = -3$, $p = 2$ ; $m = \frac{1}{4}$, $p = 0$ ; $m = 0$, $p = 5$ ; $y = -\frac{2}{3}x + 2$, $m = -\frac{2}{3}$, $p = 2$.

### Exercice 8 — Coefficient directeur <span class="etoiles">★</span>

Calculer le coefficient directeur de $(AB)$ dans chaque cas : $A(1\,;\,3)$, $B(4\,;\,9)$ ; $A(-2\,;\,5)$, $B(2\,;\,-3)$ ; $A(3\,;\,1)$, $B(3\,;\,7)$.

??? success "Correction"
    $\frac{6}{3} = 2$ ; $\frac{-8}{4} = -2$ ; $x_A = x_B$ : la droite est parallèle à l'axe des ordonnées, pas de coefficient directeur.

### Exercice 9 — Équation réduite par deux points <span class="etoiles">★</span>

Déterminer l'équation réduite de $(AB)$ avec $A(-1\,;\,4)$ et $B(3\,;\,-4)$.

??? success "Correction"
    $m = \frac{-8}{4} = -2$ ; $4 = 2 + p$, $p = 2$. $y = -2x + 2$.

### Exercice 10 — Passer d'une forme à l'autre <span class="etoiles">★★</span>

1. Écrire l'équation réduite de $d : 5x - 2y + 8 = 0$.
2. Écrire une équation cartésienne à coefficients entiers de $d' : y = \frac{2}{3}x - \frac{1}{2}$.

??? success "Correction"
    1. $2y = 5x + 8$, $y = \frac{5}{2}x + 4$.
    2. En multipliant par $6$ : $6y = 4x - 3$, soit $4x - 6y - 3 = 0$.

### Exercice 11 — Lecture graphique <span class="etoiles">★★</span>

Une droite passe par les points $(0\,;\,-1)$ et $(3\,;\,1)$, qu'on lit sur un graphique. Déterminer son équation réduite, puis l'abscisse de son point d'intersection avec l'axe des abscisses.

??? success "Correction"
    $p = -1$, $m = \frac{2}{3}$ : $y = \frac{2}{3}x - 1$. $y = 0 \iff x = \frac{3}{2}$.

### Exercice 12 — Points alignés et équation <span class="etoiles">★★</span>

Les points $A(1\,;\,-1)$, $B(3\,;\,3)$ et $C(-2\,;\,-7)$ sont-ils alignés ? Utiliser l'équation réduite de $(AB)$.

??? success "Correction"
    $m = \frac{4}{2} = 2$, $-1 = 2 + p$, $p = -3$ : $y = 2x - 3$. Pour $C$ : $2 \times (-2) - 3 = -7$. ✓ Les points sont alignés.

---

## Thème 3 — Parallélisme et intersection

*Méthode associée : [Méthode 4](methodes.md#methode-4-etudier-la-position-relative-de-deux-droites).*

### Exercice 13 — Parallèles ? <span class="etoiles">★</span>

Les droites suivantes sont-elles parallèles ? $d_1 : y = 3x - 1$ et $d_2 : 6x - 2y + 5 = 0$ ; $d_3 : 2x + y = 4$ et $d_4 : y = 2x + 4$.

??? success "Correction"
    $d_2 : y = 3x + \frac{5}{2}$ : même coefficient $3$, parallèles (et distinctes). $d_3 : y = -2x + 4$ et $d_4$ : $-2 \neq 2$, sécantes.

### Exercice 14 — Parallèle passant par un point <span class="etoiles">★</span>

Déterminer l'équation réduite de la droite parallèle à $y = -\frac{1}{2}x + 7$ passant par $A(4\,;\,1)$.

??? success "Correction"
    $m = -\frac{1}{2}$ ; $1 = -2 + p$, $p = 3$ : $y = -\frac{1}{2}x + 3$.

### Exercice 15 — Point d'intersection <span class="etoiles">★★</span>

Déterminer le point d'intersection de $d : y = 3x - 4$ et $d' : y = -2x + 6$.

??? success "Correction"
    $3x - 4 = -2x + 6 \iff 5x = 10 \iff x = 2$ ; $y = 2$. Point $(2\,;\,2)$.

### Exercice 16 — Avec des équations cartésiennes <span class="etoiles">★★</span>

Déterminer, s'il existe, le point d'intersection de $d : 2x + y - 4 = 0$ et $d' : x - y + 1 = 0$.

??? success "Correction"
    $2 \times (-1) - 1 \times 1 = -3 \neq 0$ : sécantes. En additionnant : $3x - 3 = 0$, $x = 1$, puis $y = 2$. Point $(1\,;\,2)$.

### Exercice 17 — Triangle et médianes <span class="etoiles">★★★</span>

On donne $A(0\,;\,0)$, $B(6\,;\,0)$ et $C(0\,;\,4)$.

1. Déterminer les équations réduites des médianes issues de $A$ et de $B$.
2. En déduire les coordonnées de leur point d'intersection $G$.
3. Vérifier que $G$ est aussi sur la médiane issue de $C$.

??? success "Correction"
    1. Milieu de $[BC]$ : $I(3\,;\,2)$ ; médiane $(AI)$ : $y = \frac{2}{3}x$. Milieu de $[AC]$ : $J(0\,;\,2)$ ; médiane $(BJ)$ : $m = \frac{2 - 0}{0 - 6} = -\frac{1}{3}$, $y = -\frac{1}{3}x + 2$.
    2. $\frac{2}{3}x = -\frac{1}{3}x + 2 \iff x = 2$, $y = \frac{4}{3}$. $G\left(2\,;\,\frac{4}{3}\right)$.
    3. Milieu de $[AB]$ : $K(3\,;\,0)$ ; $(CK)$ : $m = -\frac{4}{3}$, $y = -\frac{4}{3}x + 4$. Pour $x = 2$ : $-\frac{8}{3} + 4 = \frac{4}{3}$. ✓

---

## Thème 4 — Systèmes linéaires

*Méthode associée : [Méthode 5](methodes.md#methode-5-resoudre-un-probleme-avec-un-systeme).*

### Exercice 18 — Par substitution <span class="etoiles">★</span>

Résoudre $\begin{cases} x + y = 12 \\ x - y = 4 \end{cases}$ et $\begin{cases} 3x - 2y = 4 \\ x + 4y = 6 \end{cases}$.

??? success "Correction"
    - En additionnant : $2x = 16$, $x = 8$, $y = 4$.
    - $x = 6 - 4y$, puis $3(6 - 4y) - 2y = 4 \iff 18 - 14y = 4 \iff y = 1$, $x = 2$.

### Exercice 19 — Par combinaison <span class="etoiles">★</span>

Résoudre $\begin{cases} 2x + 3y = 1 \\ 5x - 2y = 12 \end{cases}$.

??? success "Correction"
    $\times 2$ et $\times 3$ : $4x + 6y = 2$ et $15x - 6y = 36$. En additionnant : $19x = 38$, $x = 2$, puis $3y = 1 - 4 = -3$, $y = -1$. Solution $(2\,;\,-1)$.

### Exercice 20 — Nombre de solutions <span class="etoiles">★★</span>

Sans résoudre, déterminer le nombre de solutions de chaque système.

1. $\begin{cases} 2x - y = 3 \\ -4x + 2y = 1 \end{cases}$ 
2. $\begin{cases} x + 2y = 3 \\ 3x + 6y = 9 \end{cases}$ 
3. $\begin{cases} x + 2y = 3 \\ 2x - y = 1 \end{cases}$

??? success "Correction"
    1. $2 \times 2 - (-4)(-1) = 0$ : droites parallèles. La seconde équation donne $2x - y = -\frac{1}{2} \neq 3$ : strictement parallèles, **aucune** solution.
    2. La seconde est la première multipliée par $3$ : droites confondues, **infinité** de solutions.
    3. $1 \times (-1) - 2 \times 2 = -5 \neq 0$ : **une** solution.

### Exercice 21 — Un système à paramètre <span class="etoiles">★★</span>

Pour quelles valeurs de $k$ le système $\begin{cases} kx + 2y = 1 \\ 2x + ky = 1 \end{cases}$ a-t-il une unique solution ?

??? success "Correction"
    Il faut $k \times k - 2 \times 2 \neq 0$, c'est-à-dire $k^2 \neq 4$ : $k \neq 2$ et $k \neq -2$.

### Exercice 22 — Résolution graphique <span class="etoiles">★★</span>

Résoudre graphiquement puis par le calcul $\begin{cases} y = 2x - 1 \\ y = -x + 5 \end{cases}$.

??? success "Correction"
    Les deux droites se coupent au point $(2\,;\,3)$ : $2x - 1 = -x + 5 \iff x = 2$, $y = 3$.

### Exercice 23 — Un système à trois inconnues <span class="etoiles">★★★</span>

Résoudre $\begin{cases} x + y + z = 6 \\ x - y = -1 \\ y - z = -1 \end{cases}$ en exprimant $x$ et $z$ en fonction de $y$.

??? success "Correction"
    $x = y - 1$ et $z = y + 1$. Dans la première équation : $3y = 6$, $y = 2$, puis $x = 1$, $z = 3$.

---

## Thème 5 — Problèmes et approfondissement

### Exercice 24 — Billets <span class="etoiles">★★</span>

Un distributeur contient $30$ billets de $10$ € et de $20$ €, pour un total de $420$ €. Combien y a-t-il de billets de chaque sorte ?

??? success "Correction"
    $\begin{cases} a + b = 30 \\ 10a + 20b = 420 \end{cases}$. $a = 30 - b$, puis $300 + 10b = 420$, $b = 12$, $a = 18$ : $18$ billets de $10$ € et $12$ de $20$ €.

### Exercice 25 — Poules et lapins <span class="etoiles">★★</span>

Dans une ferme, on compte $35$ têtes et $94$ pattes de poules et de lapins. Combien y a-t-il de poules et de lapins ?

??? success "Correction"
    $\begin{cases} p + \ell = 35 \\ 2p + 4\ell = 94 \end{cases}$. En retranchant le double de la première : $2\ell = 24$, $\ell = 12$, $p = 23$.

### Exercice 26 — Tarifs de taxi <span class="etoiles">★★</span>

Un taxi facture une prise en charge fixe plus un prix par kilomètre. Une course de $10$ km coûte $19$ €, une course de $25$ km coûte $40$ €.

1. Déterminer la prise en charge et le prix au kilomètre.
2. Un autre taxi facture $5$ € puis $1{,}60$ € par km. À partir de quelle distance le premier taxi est-il moins cher ?

??? success "Correction"
    1. $\begin{cases} a + 10b = 19 \\ a + 25b = 40 \end{cases}$ : $15b = 21$, $b = 1{,}4$ €/km, $a = 5$ €.
    2. $5 + 1{,}4d < 5 + 1{,}6d \iff 0 < 0{,}2d$ : dès que $d > 0$. Le premier taxi est toujours moins cher.

### Exercice 27 — Systèmes en Python <span class="etoiles">★★★</span>

Écrire une fonction `resoudre(a, b, c, d, e, f)` qui renvoie la solution du système $\begin{cases} ax + by = e \\ cx + dy = f \end{cases}$ lorsqu'elle est unique, et `None` sinon. *On admettra les formules (dites de Cramer) $x = \dfrac{ed - bf}{ad - bc}$ et $y = \dfrac{af - ec}{ad - bc}$, et on les vérifiera sur l'exercice 19.*

??? success "Correction"
    ```python
    def resoudre(a, b, c, d, e, f):
        D = a * d - b * c
        if D == 0:
            return None
        x = (e * d - b * f) / D
        y = (a * f - e * c) / D
        return [x, y]

    print(resoudre(2, 3, 5, -2, 1, 12))   # [2.0, -1.0]
    ```

    On peut démontrer les formules par combinaison : multiplier la première équation par $d$, la seconde par $b$, et soustraire pour éliminer $y$.

### Exercice 28 — Le point fixe <span class="etoiles">★★★</span>

Pour tout réel $m$, $\Delta_m$ est la droite d'équation $y = mx - 2m + 3$.

1. Montrer que toutes les droites $\Delta_m$ passent par un même point $P$.
2. Quelle droite $\Delta_m$ passe par l'origine ?
3. Existe-t-il une droite passant par $P$ qui n'est d'aucune des formes $\Delta_m$ ?

??? success "Correction"
    1. $y = m(x - 2) + 3$ : pour $x = 2$, $y = 3$ quel que soit $m$. $P(2\,;\,3)$.
    2. $0 = -2m + 3$, $m = \frac{3}{2}$ : $y = \frac{3}{2}x$.
    3. Oui : la droite verticale $x = 2$, qui n'a pas d'équation réduite.
