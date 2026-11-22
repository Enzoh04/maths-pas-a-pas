# Exercices corrigés — Géométrie repérée

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**, sauf l'exercice Python. Le repère est **orthonormé**.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Équations de droites | 1 à 6 |
| 2. Vecteur normal, perpendiculaires, projeté | 7 à 12 |
| 3. Équations de cercles | 13 à 18 |
| 4. Droites et cercles, tangentes | 19 à 23 |
| 5. Paraboles et approfondissement | 24 à 28 |

---

## Thème 1 — Équations de droites

*Méthode associée : [Méthode 1](methodes.md#methode-1-determiner-une-equation-de-droite).*

### Exercice 1 — Lire un vecteur directeur et un vecteur normal <span class="etoiles">★</span>

Donner un vecteur directeur et un vecteur normal de chacune des droites :

$d_1 : 2x - 5y + 1 = 0$ ; $d_2 : y = 3x - 4$ ; $d_3 : x = 7$.

??? success "Correction"
    - $d_1$ : normal $\vec{n}(2\,;\,-5)$, directeur $\vec{u}(5\,;\,2)$.
    - $d_2$ s'écrit $3x - y - 4 = 0$ : normal $(3\,;\,-1)$, directeur $(1\,;\,3)$.
    - $d_3$ s'écrit $1x + 0y - 7 = 0$ : normal $(1\,;\,0)$, directeur $(0\,;\,1)$.

### Exercice 2 — Droite passant par deux points <span class="etoiles">★</span>

Déterminer une équation cartésienne, puis l'équation réduite, de la droite $(AB)$ avec $A(1\,;\,3)$ et $B(4\,;\,-3)$.

??? success "Correction"
    $\overrightarrow{AB}(3\,;\,-6)$ dirige la droite, ainsi que $(1\,;\,-2)$. Un vecteur normal est $(2\,;\,1)$ : $2x + y + c = 0$, et avec $A$ : $2 + 3 + c = 0$, donc $c = -5$.

    Équation : $2x + y - 5 = 0$ (vérification avec $B$ : $8 - 3 - 5 = 0$). Équation réduite : $y = -2x + 5$.

### Exercice 3 — Avec un vecteur normal <span class="etoiles">★</span>

Déterminer une équation de la droite $d$ passant par $A(-2\,;\,1)$ et de vecteur normal $\vec{n}(3\,;\,-4)$. Quel est le point de $d$ d'abscisse $2$ ?

??? success "Correction"
    $3x - 4y + c = 0$ avec $-6 - 4 + c = 0$ : $d : 3x - 4y + 10 = 0$. Pour $x = 2$ : $6 - 4y + 10 = 0$, donc $y = 4$. Le point est $(2\,;\,4)$.

### Exercice 4 — Droites parallèles ? <span class="etoiles">★</span>

On considère $d : 4x - 6y + 1 = 0$, $d' : -2x + 3y + 5 = 0$ et $d'' : 3x + 2y = 0$. Lesquelles sont parallèles ?

??? success "Correction"
    $d$ et $d'$ : $4 \times 3 - (-2) \times (-6) = 12 - 12 = 0$, elles sont parallèles. Elles sont distinctes : en multipliant l'équation de $d'$ par $-2$, on obtient $4x - 6y - 10 = 0$, qui diffère de $d$ par la constante.

    $d$ et $d''$ : $4 \times 2 - 3 \times (-6) = 26 \neq 0$, elles sont sécantes (et $d''$ n'est pas non plus parallèle à $d'$).

### Exercice 5 — Point d'intersection <span class="etoiles">★★</span>

Déterminer le point d'intersection des droites $d_1 : 2x + y - 5 = 0$ et $d_2 : x - 3y + 1 = 0$.

??? success "Correction"
    $d_2$ donne $x = 3y - 1$. Dans $d_1$ : $6y - 2 + y - 5 = 0$, donc $y = 1$, puis $x = 2$. Le point d'intersection est $(2\,;\,1)$.

### Exercice 6 — Une famille de droites <span class="etoiles">★★</span>

Pour tout réel $m$, on note $d_m$ la droite d'équation $(m - 1)x + 2y - 3 = 0$, et $d : 3x - y + 2 = 0$.

1. Pour quelle valeur de $m$ la droite $d_m$ est-elle parallèle à $d$ ?
2. Pour quelle valeur de $m$ est-elle perpendiculaire à $d$ ?
3. Pour quelle valeur de $m$ passe-t-elle par le point $(1\,;\,1)$ ?

??? success "Correction"
    1. $(m - 1)(-1) - 3 \times 2 = 0 \iff -m - 5 = 0 \iff m = -5$.
    2. Vecteurs normaux orthogonaux : $3(m - 1) + 2 \times (-1) = 0 \iff m = \frac{5}{3}$.
    3. $(m - 1) + 2 - 3 = 0 \iff m = 2$.

---

## Thème 2 — Vecteur normal, perpendiculaires, projeté

*Méthodes associées : [Méthode 1](methodes.md#methode-1-determiner-une-equation-de-droite) et [Méthode 2](methodes.md#methode-2-calculer-le-projete-orthogonal-dun-point-et-une-distance).*

### Exercice 7 — Perpendiculaires ? <span class="etoiles">★</span>

Les droites suivantes sont-elles perpendiculaires ?

1. $2x - 3y + 1 = 0$ et $3x + 2y - 4 = 0$.
2. $y = 2x + 1$ et $y = -\frac{1}{2}x + 3$.
3. $y = 3x$ et $y = -3x$.

??? success "Correction"
    1. $2 \times 3 + (-3) \times 2 = 0$ : oui.
    2. $2 \times \left(-\frac{1}{2}\right) = -1$ : oui.
    3. $3 \times (-3) = -9 \neq -1$ : non.

### Exercice 8 — Hauteurs et orthocentre <span class="etoiles">★</span>

On donne $A(0\,;\,0)$, $B(6\,;\,0)$ et $C(2\,;\,4)$.

1. Déterminer une équation de la hauteur issue de $C$, puis de la hauteur issue de $A$.
2. En déduire les coordonnées de l'orthocentre $H$, et vérifier qu'il est sur la hauteur issue de $B$.

??? success "Correction"
    1. Hauteur issue de $C$ : $\overrightarrow{AB}(6\,;\,0)$ est normal, donc $x + c = 0$ avec $C$ : $x = 2$. Hauteur issue de $A$ : $\overrightarrow{BC}(-4\,;\,4)$, ou $(-1\,;\,1)$, est normal : $-x + y = 0$ (elle passe par $A$), soit $y = x$.
    2. $H(2\,;\,2)$. Hauteur issue de $B$ : $\overrightarrow{AC}(2\,;\,4)$, ou $(1\,;\,2)$, est normal : $x + 2y - 6 = 0$ (passe par $B$). Avec $H$ : $2 + 4 - 6 = 0$. ✓

### Exercice 9 — Médiatrices et cercle circonscrit <span class="etoiles">★★</span>

On donne $A(1\,;\,2)$, $B(5\,;\,4)$ et $C(1\,;\,6)$.

1. Déterminer une équation de la médiatrice de $[AB]$, puis de celle de $[AC]$.
2. En déduire le centre $\Omega$ et le rayon du cercle circonscrit au triangle $ABC$.

??? success "Correction"
    1. Médiatrice de $[AB]$ : elle passe par le milieu $(3\,;\,3)$ et a pour vecteur normal $\overrightarrow{AB}(4\,;\,2)$, ou $(2\,;\,1)$ : $2x + y - 9 = 0$. Médiatrice de $[AC]$ : milieu $(1\,;\,4)$, vecteur normal $\overrightarrow{AC}(0\,;\,4)$ : $y = 4$.
    2. $y = 4$ et $2x + 4 - 9 = 0$ : $\Omega\left(\frac{5}{2}\,;\,4\right)$. Rayon : $\Omega A^2 = \frac{9}{4} + 4 = \frac{25}{4}$, donc $r = \frac{5}{2}$ (on vérifie $\Omega B^2 = \frac{25}{4} + 0$ et $\Omega C^2 = \frac{9}{4} + 4$).

### Exercice 10 — Projeté orthogonal <span class="etoiles">★★</span>

Déterminer le projeté orthogonal $H$ du point $M(3\,;\,0)$ sur la droite $d : x - y + 1 = 0$, puis la distance de $M$ à $d$.

??? success "Correction"
    $\vec{n}(1\,;\,-1)$ dirige la perpendiculaire $\Delta$, donc $(1\,;\,1)$ lui est normal : $\Delta : x + y - 3 = 0$. Le système $x - y = -1$, $x + y = 3$ donne $x = 1$, $y = 2$ : $H(1\,;\,2)$.

    $MH = \sqrt{4 + 4} = 2\sqrt{2}$. Vérification : $\frac{|3 - 0 + 1|}{\sqrt{2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2}$.

### Exercice 11 — Formule de la distance <span class="etoiles">★★</span>

1. Calculer la distance du point $A(2\,;\,-1)$ à la droite $5x + 12y + 11 = 0$.
2. Les droites $3x + 4y - 5 = 0$ et $3x + 4y + 15 = 0$ sont parallèles. Calculer la distance qui les sépare.

??? success "Correction"
    1. $\dfrac{|10 - 12 + 11|}{\sqrt{25 + 144}} = \dfrac{9}{13}$.
    2. Le point $(-1\,;\,2)$ est sur la première droite ($-3 + 8 - 5 = 0$). Sa distance à la seconde est $\dfrac{|-3 + 8 + 15|}{5} = 4$.

### Exercice 12 — Symétrique d'un point <span class="etoiles">★★★</span>

On reprend $M(3\,;\,0)$ et $d : x - y + 1 = 0$ de l'exercice 10.

1. Déterminer les coordonnées du point $M'$ symétrique de $M$ par rapport à $d$.
2. Vérifier que $d$ est la médiatrice de $[MM']$.

??? success "Correction"
    1. Le projeté $H(1\,;\,2)$ est le milieu de $[MM']$ : $M' = (2 \times 1 - 3\,;\,2 \times 2 - 0) = (-1\,;\,4)$.
    2. Le milieu de $[MM']$ est $H$, qui est sur $d$. De plus $\overrightarrow{MM'}(-4\,;\,4)$ est colinéaire au vecteur normal $(1\,;\,-1)$ de $d$, donc $(MM') \perp d$. La droite $d$ est bien la médiatrice de $[MM']$.

---

## Thème 3 — Équations de cercles

*Méthode associée : [Méthode 3](methodes.md#methode-3-trouver-le-centre-et-le-rayon-dun-cercle).*

### Exercice 13 — Écrire une équation de cercle <span class="etoiles">★</span>

1. Écrire une équation du cercle $\mathcal{C}$ de centre $\Omega(2\,;\,-3)$ et de rayon $4$, puis la développer.
2. Les points $A(2\,;\,1)$ et $B(5\,;\,0)$ sont-ils sur $\mathcal{C}$ ?

??? success "Correction"
    1. $(x - 2)^2 + (y + 3)^2 = 16$, soit $x^2 + y^2 - 4x + 6y - 3 = 0$.
    2. $A$ : $0 + 16 = 16$, oui. $B$ : $9 + 9 = 18 \neq 16$, non ($B$ est à l'extérieur, car $\Omega B = \sqrt{18} > 4$).

### Exercice 14 — Reconnaître un cercle <span class="etoiles">★</span>

Déterminer la nature de chacun des ensembles suivants.

1. $x^2 + y^2 - 8x + 2y + 8 = 0$.
2. $x^2 + y^2 + 4x - 6y + 13 = 0$.
3. $x^2 + y^2 - 2x + 5 = 0$.

??? success "Correction"
    1. $(x - 4)^2 - 16 + (y + 1)^2 - 1 + 8 = 0 \iff (x - 4)^2 + (y + 1)^2 = 9$ : cercle de centre $(4\,;\,-1)$ et de rayon $3$.
    2. $(x + 2)^2 - 4 + (y - 3)^2 - 9 + 13 = 0 \iff (x + 2)^2 + (y - 3)^2 = 0$ : le point $(-2\,;\,3)$.
    3. $(x - 1)^2 - 1 + y^2 + 5 = 0 \iff (x - 1)^2 + y^2 = -4$ : ensemble vide.

### Exercice 15 — Cercle de centre donné passant par un point <span class="etoiles">★</span>

Déterminer une équation du cercle de centre $\Omega(1\,;\,-2)$ passant par $A(4\,;\,2)$.

??? success "Correction"
    $r^2 = \Omega A^2 = 9 + 16 = 25$ : $(x - 1)^2 + (y + 2)^2 = 25$.

### Exercice 16 — Cercle de diamètre $[AB]$ <span class="etoiles">★★</span>

On donne $A(-1\,;\,0)$ et $B(3\,;\,4)$.

1. Déterminer une équation du cercle $\mathcal{C}$ de diamètre $[AB]$ de deux façons : avec le centre et le rayon, puis avec $\overrightarrow{MA} \cdot \overrightarrow{MB} = 0$.
2. Le point $C(3\,;\,0)$ est-il sur $\mathcal{C}$ ? Qu'en déduit-on pour le triangle $ABC$ ?

??? success "Correction"
    1. Centre : milieu $(1\,;\,2)$ ; rayon : $\frac{AB}{2}$ avec $AB^2 = 32$, donc $r^2 = \frac{32}{4} = 8$ : $(x - 1)^2 + (y - 2)^2 = 8$.

        Avec le produit scalaire : $(x + 1)(x - 3) + y(y - 4) = 0 \iff x^2 - 2x - 3 + y^2 - 4y = 0 \iff (x - 1)^2 + (y - 2)^2 = 8$. ✓
    2. $4 + 4 = 8$ : oui. Le triangle $ABC$ est rectangle en $C$.

### Exercice 17 — Cercle passant par trois points <span class="etoiles">★★</span>

On cherche le cercle passant par $A(1\,;\,0)$, $B(5\,;\,0)$ et $C(0\,;\,5)$, sous la forme $x^2 + y^2 + \alpha x + \beta y + \gamma = 0$.

1. Écrire le système vérifié par $\alpha$, $\beta$ et $\gamma$, et le résoudre.
2. En déduire le centre et le rayon du cercle.

??? success "Correction"
    1. $A$ : $1 + \alpha + \gamma = 0$ ; $B$ : $25 + 5\alpha + \gamma = 0$ ; $C$ : $25 + 5\beta + \gamma = 0$. En soustrayant les deux premières : $24 + 4\alpha = 0$, donc $\alpha = -6$ et $\gamma = 5$. Puis $5\beta = -30$, $\beta = -6$.
    2. $x^2 + y^2 - 6x - 6y + 5 = 0 \iff (x - 3)^2 + (y - 3)^2 = 13$ : centre $(3\,;\,3)$, rayon $\sqrt{13}$.

### Exercice 18 — Un lieu de points <span class="etoiles">★★★</span>

On donne $A(-1\,;\,0)$ et $B(3\,;\,0)$. Déterminer l'ensemble des points $M(x\,;\,y)$ tels que $MA^2 + MB^2 = 20$. Retrouver le résultat avec le théorème de la médiane.

??? success "Correction"
    $(x + 1)^2 + y^2 + (x - 3)^2 + y^2 = 20 \iff 2x^2 - 4x + 10 + 2y^2 = 20 \iff x^2 - 2x + y^2 = 5 \iff (x - 1)^2 + y^2 = 6$.

    C'est le cercle de centre $I(1\,;\,0)$, milieu de $[AB]$, et de rayon $\sqrt{6}$. Avec le théorème de la médiane : $MA^2 + MB^2 = 2MI^2 + \frac{AB^2}{2} = 2MI^2 + 8$, donc $MI^2 = 6$.

---

## Thème 4 — Droites et cercles, tangentes

*Méthode associée : [Méthode 4](methodes.md#methode-4-etudier-lintersection-dune-droite-et-dun-cercle).*

### Exercice 19 — Tangente en un point <span class="etoiles">★</span>

Le cercle $\mathcal{C}$ a pour centre $\Omega(2\,;\,1)$ et passe par $T(5\,;\,5)$. Déterminer une équation de la tangente à $\mathcal{C}$ en $T$.

??? success "Correction"
    $\overrightarrow{\Omega T}(3\,;\,4)$ est normal à la tangente : $3x + 4y + c = 0$ avec $15 + 20 + c = 0$. Tangente : $3x + 4y - 35 = 0$.

### Exercice 20 — Points d'intersection <span class="etoiles">★★</span>

Déterminer les points d'intersection du cercle $\mathcal{C} : (x - 1)^2 + y^2 = 10$ et de la droite $d : x - y + 1 = 0$.

??? success "Correction"
    $d$ : $y = x + 1$. Dans $\mathcal{C}$ : $(x - 1)^2 + (x + 1)^2 = 10 \iff 2x^2 + 2 = 10 \iff x^2 = 4$. Donc $x = 2$ ou $x = -2$ : points $(2\,;\,3)$ et $(-2\,;\,-1)$.

### Exercice 21 — Position relative par la distance <span class="etoiles">★★</span>

$\mathcal{C}$ est le cercle de centre $\Omega(1\,;\,2)$ et de rayon $3$. Étudier la position de $\mathcal{C}$ par rapport à chacune des droites :

$d_1 : 4x + 3y + 5 = 0$ ; $d_2 : x - y + 4 = 0$ ; $d_3 : y = -3$.

Pour la droite tangente, déterminer le point de contact.

??? success "Correction"
    - $d_1$ : $\frac{|4 + 6 + 5|}{5} = 3 = r$ : **tangente**.
    - $d_2$ : $\frac{|1 - 2 + 4|}{\sqrt{2}} = \frac{3}{\sqrt{2}} < 3$ : **sécante** (deux points).
    - $d_3$ : distance $|2 - (-3)| = 5 > 3$ : **aucun point commun**.

    Point de contact avec $d_1$ : c'est le projeté de $\Omega$ sur $d_1$. La perpendiculaire passant par $\Omega$ est dirigée par $(4\,;\,3)$ : elle a pour équation $3x - 4y + 5 = 0$. Le système avec $d_1$ donne $x = -\frac{7}{5}$ et $y = \frac{1}{5}$. Vérification : $\left(-\frac{12}{5}\right)^2 + \left(-\frac{9}{5}\right)^2 = \frac{144 + 81}{25} = 9$. ✓

### Exercice 22 — Tangentes de direction donnée <span class="etoiles">★★</span>

$\mathcal{C}$ est le cercle d'équation $x^2 + y^2 = 5$. Déterminer les tangentes à $\mathcal{C}$ de coefficient directeur $2$, et leurs points de contact.

??? success "Correction"
    Une droite $y = 2x + p$ s'écrit $2x - y + p = 0$. Elle est tangente si et seulement si sa distance à $O$ vaut $\sqrt{5}$ : $\frac{|p|}{\sqrt{5}} = \sqrt{5} \iff |p| = 5$.

    Tangentes : $y = 2x + 5$ et $y = 2x - 5$. Pour la première : $x^2 + (2x + 5)^2 = 5 \iff 5x^2 + 20x + 20 = 0 \iff (x + 2)^2 = 0$ : point $(-2\,;\,1)$. Par symétrie de centre $O$, l'autre point est $(2\,;\,-1)$.

### Exercice 23 — Discussion selon un paramètre <span class="etoiles">★★★</span>

$\mathcal{C}$ est le cercle $x^2 + y^2 = 8$ et, pour tout réel $p$, $d_p$ est la droite $y = x + p$. Selon les valeurs de $p$, déterminer le nombre de points communs à $\mathcal{C}$ et $d_p$ :

1. avec un discriminant ;
2. avec la distance du centre à la droite.

??? success "Correction"
    1. $x^2 + (x + p)^2 = 8 \iff 2x^2 + 2px + p^2 - 8 = 0$. $\Delta = 4p^2 - 8(p^2 - 8) = 64 - 4p^2 = 4(16 - p^2)$.
        - $-4 < p < 4$ : deux points communs ;
        - $p = 4$ ou $p = -4$ : un point (tangente) ;
        - $p < -4$ ou $p > 4$ : aucun point.
    2. $d_p : x - y + p = 0$, distance à $O$ : $\frac{|p|}{\sqrt{2}}$, à comparer à $r = 2\sqrt{2}$ : $\frac{|p|}{\sqrt{2}} < 2\sqrt{2} \iff |p| < 4$. Même conclusion.

---

## Thème 5 — Paraboles et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-etudier-une-parabole).*

### Exercice 24 — Sommet et axe <span class="etoiles">★</span>

Déterminer le sommet et l'axe de symétrie des paraboles d'équations $y = 2x^2 - 12x + 13$ et $y = -x^2 - 2x + 3$. Pour la seconde, calculer les points d'intersection avec l'axe des abscisses et vérifier la symétrie.

??? success "Correction"
    - $\alpha = \frac{12}{4} = 3$, $\beta = 18 - 36 + 13 = -5$ : sommet $(3\,;\,-5)$, axe $x = 3$.
    - $\alpha = -\frac{-2}{-2} = -1$, $\beta = -1 + 2 + 3 = 4$ : sommet $(-1\,;\,4)$, axe $x = -1$. $-x^2 - 2x + 3 = -(x + 3)(x - 1)$ : racines $-3$ et $1$, dont la moyenne vaut bien $-1$.

### Exercice 25 — Parabole passant par trois points <span class="etoiles">★★</span>

Déterminer la parabole d'équation $y = ax^2 + bx + c$ passant par $(0\,;\,3)$, $(1\,;\,0)$ et $(4\,;\,3)$. Quel est son axe de symétrie ? Pouvait-on le prévoir ?

??? success "Correction"
    $c = 3$ ; $a + b + 3 = 0$ ; $16a + 4b + 3 = 3$, donc $b = -4a$. Alors $-3a = -3$ : $a = 1$, $b = -4$. Parabole : $y = x^2 - 4x + 3$, d'axe $x = 2$.

    On pouvait le prévoir : les points $(0\,;\,3)$ et $(4\,;\,3)$ ont la même ordonnée, ils sont symétriques par rapport à l'axe, qui passe donc par l'abscisse $\frac{0 + 4}{2} = 2$.

### Exercice 26 — Parabole et droites <span class="etoiles">★★</span>

$\mathcal{P}$ est la parabole $y = x^2 - 2x$.

1. Déterminer les points d'intersection de $\mathcal{P}$ et de la droite $y = 2x - 3$.
2. Déterminer le réel $p$ pour lequel la droite $y = 2x + p$ n'a qu'un seul point commun avec $\mathcal{P}$. Quel est ce point ?

??? success "Correction"
    1. $x^2 - 2x = 2x - 3 \iff x^2 - 4x + 3 = 0 \iff x = 1$ ou $x = 3$. Points $(1\,;\,-1)$ et $(3\,;\,3)$.
    2. $x^2 - 4x - p = 0$ a une seule solution si $\Delta = 16 + 4p = 0$, soit $p = -4$. La solution double est $x = 2$ : point $(2\,;\,0)$. La droite $y = 2x - 4$ est la tangente à $\mathcal{P}$ en ce point (on retrouve $f'(2) = 2 \times 2 - 2 = 2$).

### Exercice 27 — Géométrie repérée en Python <span class="etoiles">★★★</span>

Un point est représenté par une liste `[x, y]` et une droite $ax + by + c = 0$ par la liste `[a, b, c]`.

1. Écrire une fonction `droite(A, B)` qui renvoie une équation de la droite $(AB)$.
2. Écrire une fonction `distance(M, d)` qui renvoie la distance du point `M` à la droite `d`.
3. Écrire une fonction `position(centre, r, d)` qui renvoie le nombre de points communs entre le cercle de centre `centre` et de rayon `r` et la droite `d`.

??? success "Correction"
    ```python
    from math import sqrt

    def droite(A, B):
        # vecteur directeur (B - A), vecteur normal (yB - yA, -(xB - xA))
        a = B[1] - A[1]
        b = A[0] - B[0]
        c = -a * A[0] - b * A[1]
        return [a, b, c]

    def distance(M, d):
        a, b, c = d
        return abs(a * M[0] + b * M[1] + c) / sqrt(a**2 + b**2)

    def position(centre, r, d):
        delta = distance(centre, d)
        if abs(delta - r) < 1e-9:
            return 1
        elif delta < r:
            return 2
        else:
            return 0

    print(droite([1, 3], [4, -3]))            # [-6, -3, 15], soit 2x + y - 5 = 0
    print(position([1, 2], 3, [4, 3, 5]))     # 1 (exercice 21)
    ```

### Exercice 28 — Foyer d'une parabole <span class="etoiles">★★★</span>

On considère le point $F(0\,;\,1)$ et la droite $\Delta : y = -1$. Déterminer l'ensemble des points $M(x\,;\,y)$ situés à la même distance de $F$ et de $\Delta$.

??? success "Correction"
    $MF^2 = x^2 + (y - 1)^2$ et la distance de $M$ à $\Delta$ est $|y + 1|$. Les deux distances sont égales si et seulement si leurs carrés le sont :
    $$x^2 + (y - 1)^2 = (y + 1)^2 \iff x^2 - 2y + 1 = 2y + 1 \iff y = \frac{x^2}{4}.$$
    C'est une **parabole** : $F$ est son **foyer** et $\Delta$ sa **directrice**. Toute parabole peut être définie de cette façon.
