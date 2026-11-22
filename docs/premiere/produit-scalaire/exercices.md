# Exercices corrigés — Calcul vectoriel et produit scalaire

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**, sauf l'exercice Python. Sauf mention contraire, les repères sont **orthonormés**.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Calcul vectoriel | 1 à 5 |
| 2. Calculer un produit scalaire | 6 à 11 |
| 3. Orthogonalité et angles | 12 à 17 |
| 4. Formule d'Al-Kashi et longueurs | 18 à 23 |
| 5. Ensembles de points et approfondissement | 24 à 28 |

---

## Thème 1 — Calcul vectoriel

*Méthode associée : [Méthode 2](methodes.md#methode-2-demontrer-que-deux-droites-sont-perpendiculaires-ou-paralleles).*

### Exercice 1 — Coordonnées <span class="etoiles">★</span>

On donne $A(-1\,;\,2)$, $B(3\,;\,4)$ et $C(5\,;\,-2)$.

1. Calculer les coordonnées de $\overrightarrow{AB}$, $\overrightarrow{AC}$ et $2\overrightarrow{AB} - \overrightarrow{AC}$.
2. Calculer les coordonnées du milieu de $[BC]$.
3. Déterminer les coordonnées du point $D$ tel que $ABCD$ soit un parallélogramme.

??? success "Correction"
    1. $\overrightarrow{AB}\begin{pmatrix} 4 \\ 2 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 6 \\ -4 \end{pmatrix}$, $2\overrightarrow{AB} - \overrightarrow{AC}\begin{pmatrix} 2 \\ 8 \end{pmatrix}$.
    2. $\left(\frac{3 + 5}{2}\,;\,\frac{4 - 2}{2}\right) = (4\,;\,1)$.
    3. $ABCD$ est un parallélogramme si et seulement si $\overrightarrow{AD} = \overrightarrow{BC}$. Or $\overrightarrow{BC}\begin{pmatrix} 2 \\ -6 \end{pmatrix}$, donc $x_D = -1 + 2 = 1$ et $y_D = 2 - 6 = -4$ : $D(1\,;\,-4)$.

### Exercice 2 — Colinéarité <span class="etoiles">★</span>

1. Les vecteurs $\vec{u}\begin{pmatrix} 3 \\ -6 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -2 \\ 4 \end{pmatrix}$ sont-ils colinéaires ? Et $\vec{u}$ et $\vec{w}\begin{pmatrix} 5 \\ -9 \end{pmatrix}$ ?
2. Déterminer les réels $m$ tels que $\begin{pmatrix} m \\ 3 \end{pmatrix}$ et $\begin{pmatrix} 2 \\ m + 1 \end{pmatrix}$ soient colinéaires.

??? success "Correction"
    1. $\det(\vec{u}, \vec{v}) = 3 \times 4 - (-2) \times (-6) = 12 - 12 = 0$ : colinéaires (d'ailleurs $\vec{v} = -\frac{2}{3}\vec{u}$). $\det(\vec{u}, \vec{w}) = 3 \times (-9) - 5 \times (-6) = -27 + 30 = 3 \neq 0$ : non colinéaires.
    2. $m(m + 1) - 2 \times 3 = 0 \iff m^2 + m - 6 = 0 \iff (m - 2)(m + 3) = 0$. Donc $m = 2$ ou $m = -3$.

### Exercice 3 — Points alignés <span class="etoiles">★</span>

On donne $A(1\,;\,-1)$, $B(3\,;\,3)$, $C(-2\,;\,-7)$ et $D(4\,;\,6)$.

1. Les points $A$, $B$, $C$ sont-ils alignés ?
2. Les points $A$, $B$, $D$ sont-ils alignés ?

??? success "Correction"
    1. $\overrightarrow{AB}\begin{pmatrix} 2 \\ 4 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} -3 \\ -6 \end{pmatrix}$ : $\det = 2 \times (-6) - (-3) \times 4 = -12 + 12 = 0$. Les points sont alignés.
    2. $\overrightarrow{AD}\begin{pmatrix} 3 \\ 7 \end{pmatrix}$ : $\det\left(\overrightarrow{AB}, \overrightarrow{AD}\right) = 14 - 12 = 2 \neq 0$. Les points ne sont pas alignés.

### Exercice 4 — Centre de gravité <span class="etoiles">★★</span>

Soit $ABC$ un triangle, $I$ le milieu de $[BC]$ et $G$ le point tel que $\overrightarrow{AG} = \frac{2}{3}\overrightarrow{AI}$.

1. Exprimer $\overrightarrow{AI}$, puis $\overrightarrow{AG}$, en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AC}$.
2. Montrer que $\overrightarrow{GA} + \overrightarrow{GB} + \overrightarrow{GC} = \vec{0}$.

??? success "Correction"
    1. $\overrightarrow{AI} = \overrightarrow{AB} + \overrightarrow{BI} = \overrightarrow{AB} + \frac{1}{2}\overrightarrow{BC} = \overrightarrow{AB} + \frac{1}{2}\left(\overrightarrow{AC} - \overrightarrow{AB}\right) = \frac{1}{2}\overrightarrow{AB} + \frac{1}{2}\overrightarrow{AC}$. Donc $\overrightarrow{AG} = \frac{1}{3}\overrightarrow{AB} + \frac{1}{3}\overrightarrow{AC}$.
    2. $\overrightarrow{GA} = -\frac{1}{3}\overrightarrow{AB} - \frac{1}{3}\overrightarrow{AC}$ ; $\overrightarrow{GB} = \overrightarrow{GA} + \overrightarrow{AB} = \frac{2}{3}\overrightarrow{AB} - \frac{1}{3}\overrightarrow{AC}$ ; $\overrightarrow{GC} = \overrightarrow{GA} + \overrightarrow{AC} = -\frac{1}{3}\overrightarrow{AB} + \frac{2}{3}\overrightarrow{AC}$. En additionnant, les coefficients de $\overrightarrow{AB}$ et de $\overrightarrow{AC}$ sont nuls : la somme vaut $\vec{0}$.

### Exercice 5 — Alignement dans un repère non orthonormé <span class="etoiles">★★</span>

$ABCD$ est un parallélogramme. On définit $E$ et $F$ par $\overrightarrow{AE} = \frac{3}{2}\overrightarrow{AB}$ et $\overrightarrow{AF} = 3\overrightarrow{AD}$. On se place dans le repère $\left(A\,;\,\overrightarrow{AB},\,\overrightarrow{AD}\right)$.

1. Donner les coordonnées de $B$, $C$, $D$, $E$ et $F$.
2. Démontrer que $E$, $C$ et $F$ sont alignés.

??? success "Correction"
    1. $B(1\,;\,0)$, $D(0\,;\,1)$, $C(1\,;\,1)$ (car $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{AD}$), $E\left(\frac{3}{2}\,;\,0\right)$, $F(0\,;\,3)$.
    2. $\overrightarrow{CE}\begin{pmatrix} \frac{1}{2} \\ -1 \end{pmatrix}$ et $\overrightarrow{CF}\begin{pmatrix} -1 \\ 2 \end{pmatrix}$ : $\det = \frac{1}{2} \times 2 - (-1) \times (-1) = 1 - 1 = 0$. Les points sont alignés.

    *Le critère du déterminant marche dans **n'importe quel** repère, contrairement aux formules de norme et de produit scalaire, qui demandent un repère orthonormé.*

---

## Thème 2 — Calculer un produit scalaire

*Méthode associée : [Méthode 1](methodes.md#methode-1-choisir-la-bonne-formule-pour-calculer-un-produit-scalaire).*

### Exercice 6 — Avec les coordonnées <span class="etoiles">★</span>

Calculer $\vec{u} \cdot \vec{v}$ dans chaque cas.

1. $\vec{u}\begin{pmatrix} 2 \\ 5 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -3 \\ 1 \end{pmatrix}$.
2. $\vec{u}\begin{pmatrix} \sqrt{2} \\ 1 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} \sqrt{2} \\ -3 \end{pmatrix}$.
3. $\vec{u} = \overrightarrow{AB}$ et $\vec{v} = \overrightarrow{AC}$ avec $A(1\,;\,2)$, $B(4\,;\,-1)$ et $C(0\,;\,5)$.

??? success "Correction"
    1. $-6 + 5 = -1$.
    2. $2 - 3 = -1$.
    3. $\overrightarrow{AB}\begin{pmatrix} 3 \\ -3 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} -1 \\ 3 \end{pmatrix}$ : $-3 - 9 = -12$.

### Exercice 7 — Avec le cosinus <span class="etoiles">★</span>

1. $\|\vec{u}\| = 3$, $\|\vec{v}\| = 4$ et l'angle entre $\vec{u}$ et $\vec{v}$ vaut $\frac{\pi}{3}$. Calculer $\vec{u} \cdot \vec{v}$.
2. Même question avec un angle de $\frac{3\pi}{4}$.
3. $AB = 5$, $AC = 2$ et $\widehat{BAC} = 150°$. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$.

??? success "Correction"
    1. $3 \times 4 \times \frac{1}{2} = 6$.
    2. $12 \times \left(-\frac{\sqrt{2}}{2}\right) = -6\sqrt{2}$.
    3. $10 \times \cos\frac{5\pi}{6} = 10 \times \left(-\frac{\sqrt{3}}{2}\right) = -5\sqrt{3}$.

### Exercice 8 — Triangle équilatéral <span class="etoiles">★</span>

$ABC$ est un triangle équilatéral de côté $2$. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$, $\overrightarrow{AB} \cdot \overrightarrow{BC}$ et $\overrightarrow{CA} \cdot \overrightarrow{CB}$.

??? success "Correction"
    - $\overrightarrow{AB} \cdot \overrightarrow{AC} = 2 \times 2 \times \cos\frac{\pi}{3} = 2$.
    - Attention : $\overrightarrow{AB}$ et $\overrightarrow{BC}$ ne partent pas du même point. $\overrightarrow{AB} \cdot \overrightarrow{BC} = -\overrightarrow{BA} \cdot \overrightarrow{BC} = -2$. (L'angle entre les vecteurs $\overrightarrow{AB}$ et $\overrightarrow{BC}$ vaut $\frac{2\pi}{3}$, pas $\frac{\pi}{3}$.)
    - $\overrightarrow{CA} \cdot \overrightarrow{CB} = 2$.

### Exercice 9 — Dans un carré <span class="etoiles">★★</span>

$ABCD$ est un carré de côté $3$ et de centre $O$. Calculer, sans repère :

$\overrightarrow{AB} \cdot \overrightarrow{AC}$ ; $\overrightarrow{AB} \cdot \overrightarrow{AD}$ ; $\overrightarrow{AB} \cdot \overrightarrow{CD}$ ; $\overrightarrow{AB} \cdot \overrightarrow{AO}$ ; $\overrightarrow{AC} \cdot \overrightarrow{BD}$.

??? success "Correction"
    - Le projeté de $C$ sur $(AB)$ est $B$ : $\overrightarrow{AB} \cdot \overrightarrow{AC} = AB^2 = 9$.
    - $\overrightarrow{AB} \perp \overrightarrow{AD}$ : $0$.
    - $\overrightarrow{CD} = -\overrightarrow{AB}$ : $-AB^2 = -9$.
    - Le projeté de $O$ sur $(AB)$ est le milieu de $[AB]$ : $3 \times \frac{3}{2} = \frac{9}{2}$.
    - Les diagonales d'un carré sont perpendiculaires : $0$.

### Exercice 10 — Avec les normes seulement <span class="etoiles">★★</span>

On sait que $\|\vec{u}\| = 3$, $\|\vec{v}\| = 5$ et $\|\vec{u} + \vec{v}\| = 7$.

1. Calculer $\vec{u} \cdot \vec{v}$.
2. Calculer $\|\vec{u} - \vec{v}\|$.
3. Déterminer l'angle entre $\vec{u}$ et $\vec{v}$.

??? success "Correction"
    1. $\vec{u} \cdot \vec{v} = \frac{1}{2}(49 - 9 - 25) = \frac{15}{2}$.
    2. $\|\vec{u} - \vec{v}\|^2 = 9 - 15 + 25 = 19$, donc $\|\vec{u} - \vec{v}\| = \sqrt{19}$.
    3. $\cos\theta = \dfrac{15/2}{3 \times 5} = \frac{1}{2}$, donc $\theta = \frac{\pi}{3}$.

### Exercice 11 — Bilinéarité <span class="etoiles">★★</span>

On sait que $\|\vec{u}\| = 2$, $\|\vec{v}\| = 3$ et $\vec{u} \cdot \vec{v} = -2$. Calculer :

1. $(2\vec{u} - \vec{v}) \cdot (\vec{u} + 3\vec{v})$ ;
2. $\|\vec{u} + \vec{v}\|$ ;
3. $(\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v})$.

??? success "Correction"
    1. On développe : $2\vec{u}^{\,2} + 6\,\vec{u} \cdot \vec{v} - \vec{v} \cdot \vec{u} - 3\vec{v}^{\,2} = 2 \times 4 + 5 \times (-2) - 3 \times 9 = 8 - 10 - 27 = -29$.
    2. $\|\vec{u} + \vec{v}\|^2 = 4 + 2 \times (-2) + 9 = 9$, donc $\|\vec{u} + \vec{v}\| = 3$.
    3. $\|\vec{u}\|^2 - \|\vec{v}\|^2 = 4 - 9 = -5$.

---

## Thème 3 — Orthogonalité et angles

*Méthodes associées : [Méthode 2](methodes.md#methode-2-demontrer-que-deux-droites-sont-perpendiculaires-ou-paralleles) et [Méthode 4](methodes.md#methode-4-calculer-un-angle-avec-les-coordonnees).*

### Exercice 12 — Vecteurs orthogonaux <span class="etoiles">★</span>

1. $\vec{u}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 3 \\ 2 \end{pmatrix}$ sont-ils orthogonaux ?
2. Même question pour $\vec{u}\begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}$ et $\vec{v}\begin{pmatrix} \sqrt{3} \\ -1 \end{pmatrix}$.
3. Déterminer $m$ pour que $\begin{pmatrix} m \\ 2 \end{pmatrix}$ et $\begin{pmatrix} 3 \\ m - 5 \end{pmatrix}$ soient orthogonaux.

??? success "Correction"
    1. $12 - 12 = 0$ : oui.
    2. $\sqrt{3} - \sqrt{3} = 0$ : oui.
    3. $3m + 2(m - 5) = 0 \iff 5m = 10 \iff m = 2$.

### Exercice 13 — Triangle rectangle ? <span class="etoiles">★</span>

On donne $A(-2\,;\,1)$, $B(2\,;\,3)$ et $C(3\,;\,1)$. Le triangle $ABC$ est-il rectangle ? Si oui, en quel sommet ?

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 4 \\ 2 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 5 \\ 0 \end{pmatrix}$, $\overrightarrow{BC}\begin{pmatrix} 1 \\ -2 \end{pmatrix}$.

    $\overrightarrow{BA} \cdot \overrightarrow{BC} = (-4) \times 1 + (-2) \times (-2) = 0$ : le triangle est **rectangle en $B$**. (On vérifie que $\overrightarrow{AB} \cdot \overrightarrow{AC} = 20$ et $\overrightarrow{CA} \cdot \overrightarrow{CB} = 5$ ne sont pas nuls.)

### Exercice 14 — Calcul d'un angle <span class="etoiles">★★</span>

On donne $A(1\,;\,1)$, $B(3\,;\,2)$ et $C(2\,;\,4)$. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$, puis la mesure de l'angle $\widehat{BAC}$.

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $\overrightarrow{AC}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$ : $\overrightarrow{AB} \cdot \overrightarrow{AC} = 2 + 3 = 5$. $AB = \sqrt{5}$ et $AC = \sqrt{10}$.

    $\cos\widehat{BAC} = \dfrac{5}{\sqrt{5}\sqrt{10}} = \dfrac{5}{\sqrt{50}} = \dfrac{5}{5\sqrt{2}} = \dfrac{\sqrt{2}}{2}$, donc $\widehat{BAC} = \frac{\pi}{4}$.

### Exercice 15 — Rectangle particulier <span class="etoiles">★★</span>

$ABCD$ est un rectangle avec $AD = 1$ et $AB = \sqrt{2}$. $I$ est le milieu de $[AB]$. Démontrer que les droites $(DI)$ et $(AC)$ sont perpendiculaires.

??? success "Correction"
    Repère orthonormé d'origine $A$ : $A(0\,;\,0)$, $B(\sqrt{2}\,;\,0)$, $C(\sqrt{2}\,;\,1)$, $D(0\,;\,1)$, $I\left(\frac{\sqrt{2}}{2}\,;\,0\right)$.

    $\overrightarrow{DI}\begin{pmatrix} \frac{\sqrt{2}}{2} \\ -1 \end{pmatrix}$ et $\overrightarrow{AC}\begin{pmatrix} \sqrt{2} \\ 1 \end{pmatrix}$ : $\overrightarrow{DI} \cdot \overrightarrow{AC} = \frac{2}{2} - 1 = 0$. Les droites sont perpendiculaires.

    *Plus généralement, avec $AB = a$ et $AD = b$, le produit vaut $\frac{a^2}{2} - b^2$ : les droites sont perpendiculaires si et seulement si $a = b\sqrt{2}$ (c'est le format des feuilles A4).*

### Exercice 16 — Sans repère <span class="etoiles">★★</span>

$ABCD$ est un carré, $E$ est le milieu de $[BC]$ et $F$ le milieu de $[CD]$. En exprimant $\overrightarrow{AE}$ et $\overrightarrow{BF}$ en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AD}$, démontrer que $(AE) \perp (BF)$.

??? success "Correction"
    $\overrightarrow{AE} = \overrightarrow{AB} + \overrightarrow{BE} = \overrightarrow{AB} + \frac{1}{2}\overrightarrow{AD}$ (car $\overrightarrow{BC} = \overrightarrow{AD}$).

    $\overrightarrow{BF} = \overrightarrow{BC} + \overrightarrow{CF} = \overrightarrow{AD} - \frac{1}{2}\overrightarrow{AB}$ (car $\overrightarrow{CD} = -\overrightarrow{AB}$).

    En notant $c$ le côté, avec $\overrightarrow{AB} \cdot \overrightarrow{AD} = 0$ :
    $$\overrightarrow{AE} \cdot \overrightarrow{BF} = \overrightarrow{AB} \cdot \overrightarrow{AD} - \frac{1}{2}AB^2 + \frac{1}{2}AD^2 - \frac{1}{4}\overrightarrow{AD} \cdot \overrightarrow{AB} = 0 - \frac{c^2}{2} + \frac{c^2}{2} - 0 = 0.$$

### Exercice 17 — Inégalité de Cauchy-Schwarz <span class="etoiles">★★★</span>

1. En utilisant les vecteurs $\vec{u}\begin{pmatrix} a \\ b \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$, démontrer que pour tous réels $a$ et $b$ : $(a + 2b)^2 \leq 5(a^2 + b^2)$. Quand y a-t-il égalité ?
2. Démontrer que pour tout réel $x$, $3\cos x + 4\sin x \leq 5$. Cette valeur est-elle atteinte ?

??? success "Correction"
    1. $\vec{u} \cdot \vec{v} = a + 2b$, $\|\vec{u}\|^2 = a^2 + b^2$ et $\|\vec{v}\|^2 = 5$. L'inégalité de Cauchy-Schwarz, élevée au carré, donne $(a + 2b)^2 \leq 5(a^2 + b^2)$. Égalité si et seulement si $\vec{u}$ et $\vec{v}$ sont colinéaires : $2a - b = 0$, soit $b = 2a$.
    2. Avec $\vec{u}\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ et $\vec{w}\begin{pmatrix} \cos x \\ \sin x \end{pmatrix}$ : $3\cos x + 4\sin x = \vec{u} \cdot \vec{w} \leq \|\vec{u}\| \times \|\vec{w}\| = 5 \times 1 = 5$. Il y a égalité quand $\vec{w}$ a la même direction et le même sens que $\vec{u}$, c'est-à-dire $\cos x = \frac{3}{5}$ et $\sin x = \frac{4}{5}$ : un tel $x$ existe (car $\frac{9}{25} + \frac{16}{25} = 1$). Le maximum $5$ est atteint.

---

## Thème 4 — Formule d'Al-Kashi et longueurs

*Méthode associée : [Méthode 3](methodes.md#methode-3-calculer-une-longueur-ou-un-angle-avec-al-kashi).*

### Exercice 18 — Calculer un côté <span class="etoiles">★</span>

Dans un triangle $ABC$, $AC = 4$, $AB = 6$ et $\widehat{BAC} = \frac{\pi}{3}$. Calculer $BC$.

??? success "Correction"
    $BC^2 = 16 + 36 - 2 \times 4 \times 6 \times \frac{1}{2} = 52 - 24 = 28$, donc $BC = \sqrt{28} = 2\sqrt{7}$.

### Exercice 19 — Calculer un angle <span class="etoiles">★</span>

Un triangle a pour côtés $3$, $5$ et $7$. Calculer la mesure de son plus grand angle.

??? success "Correction"
    Le plus grand angle est opposé au plus grand côté, $7$ :
    $$\cos\theta = \frac{3^2 + 5^2 - 7^2}{2 \times 3 \times 5} = \frac{9 + 25 - 49}{30} = -\frac{1}{2}, \quad \text{donc } \theta = \frac{2\pi}{3}.$$

### Exercice 20 — Diagonales d'un parallélogramme <span class="etoiles">★★</span>

$ABCD$ est un parallélogramme avec $AB = 5$, $AD = 3$ et $\widehat{BAD} = \frac{\pi}{3}$.

1. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AD}$.
2. En écrivant $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{AD}$ et $\overrightarrow{BD} = \overrightarrow{AD} - \overrightarrow{AB}$, calculer $AC$ et $BD$.
3. Vérifier que $AC^2 + BD^2 = 2(AB^2 + AD^2)$.

??? success "Correction"
    1. $5 \times 3 \times \frac{1}{2} = \frac{15}{2}$.
    2. $AC^2 = 25 + 2 \times \frac{15}{2} + 9 = 49$, donc $AC = 7$. $BD^2 = 9 - 15 + 25 = 19$, donc $BD = \sqrt{19}$.
    3. $49 + 19 = 68 = 2 \times (25 + 9)$. C'est l'**identité du parallélogramme**, vraie pour tout parallélogramme (les doubles produits s'annulent).

### Exercice 21 — Deux bateaux <span class="etoiles">★★</span>

Deux bateaux quittent un port en même temps. Après une heure, le premier a parcouru $6$ km en ligne droite et le second $10$ km, dans deux directions qui forment un angle de $120°$. Quelle distance les sépare ?

??? success "Correction"
    $d^2 = 6^2 + 10^2 - 2 \times 6 \times 10 \times \cos 120° = 36 + 100 + 60 = 196$, donc $d = 14$ km.

### Exercice 22 — Un côté inconnu <span class="etoiles">★★</span>

Dans un triangle $ABC$, $BC = 7$, $AB = 5$ et $\widehat{BAC} = \frac{2\pi}{3}$. On cherche $AC = x$.

1. Montrer que $x$ est solution de $x^2 + 5x - 24 = 0$.
2. En déduire $AC$.

??? success "Correction"
    1. Al-Kashi en $A$ : $BC^2 = AB^2 + AC^2 - 2 \times AB \times AC \times \cos\widehat{A}$, soit $49 = 25 + x^2 - 10x \times \left(-\frac{1}{2}\right) = 25 + x^2 + 5x$. Donc $x^2 + 5x - 24 = 0$.
    2. $\Delta = 25 + 96 = 121$, racines $\frac{-5 \pm 11}{2}$ : $3$ et $-8$. Une longueur est positive : $AC = 3$.

### Exercice 23 — Médiane, angle et aire <span class="etoiles">★★★</span>

Soit $ABC$ un triangle avec $AB = 4$, $AC = 6$ et $BC = 8$, et $I$ le milieu de $[BC]$.

1. Calculer la longueur de la médiane $AI$ à l'aide du théorème de la médiane.
2. Calculer $\cos\widehat{BAC}$. L'angle est-il aigu ou obtus ?
3. En déduire $\sin\widehat{BAC}$, puis l'aire du triangle (rappel : $\mathcal{A} = \frac{1}{2}\,AB \times AC \times \sin\widehat{A}$).

??? success "Correction"
    1. $AB^2 + AC^2 = 2AI^2 + \frac{BC^2}{2}$ : $16 + 36 = 2AI^2 + 32$, donc $AI^2 = 10$ et $AI = \sqrt{10}$.
    2. $\cos\widehat{A} = \dfrac{16 + 36 - 64}{2 \times 4 \times 6} = \dfrac{-12}{48} = -\dfrac{1}{4}$ : l'angle est obtus.
    3. $\sin^2\widehat{A} = 1 - \frac{1}{16} = \frac{15}{16}$ et $\sin\widehat{A} > 0$ (angle entre $0$ et $\pi$) : $\sin\widehat{A} = \frac{\sqrt{15}}{4}$. Aire : $\frac{1}{2} \times 4 \times 6 \times \frac{\sqrt{15}}{4} = 3\sqrt{15}$.

---

## Thème 5 — Ensembles de points et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-determiner-un-ensemble-de-points).*

### Exercice 24 — Cercle de diamètre $[AB]$ en coordonnées <span class="etoiles">★★</span>

On donne $A(1\,;\,2)$ et $B(5\,;\,-2)$. Soit $M(x\,;\,y)$.

1. Traduire $\overrightarrow{MA} \cdot \overrightarrow{MB} = 0$ par une équation en $x$ et $y$.
2. Montrer que cette équation s'écrit $(x - 3)^2 + y^2 = 8$. Retrouver le centre et le rayon du cercle de diamètre $[AB]$.

??? success "Correction"
    1. $\overrightarrow{MA}\begin{pmatrix} 1 - x \\ 2 - y \end{pmatrix}$, $\overrightarrow{MB}\begin{pmatrix} 5 - x \\ -2 - y \end{pmatrix}$ : $(1 - x)(5 - x) + (2 - y)(-2 - y) = 0$, soit $x^2 - 6x + 5 + y^2 - 4 = 0$.
    2. $x^2 - 6x = (x - 3)^2 - 9$, donc l'équation devient $(x - 3)^2 + y^2 = 8$. C'est le cercle de centre $(3\,;\,0)$, le milieu de $[AB]$, et de rayon $\sqrt{8} = 2\sqrt{2}$. On vérifie : $AB = \sqrt{16 + 16} = 4\sqrt{2}$, dont la moitié vaut $2\sqrt{2}$.

### Exercice 25 — Lignes de niveau de $\overrightarrow{MA} \cdot \overrightarrow{MB}$ <span class="etoiles">★★</span>

$A$ et $B$ sont deux points tels que $AB = 4$, et $I$ est le milieu de $[AB]$.

1. Rappeler l'expression de $\overrightarrow{MA} \cdot \overrightarrow{MB}$ en fonction de $MI$.
2. Déterminer l'ensemble des points $M$ tels que $\overrightarrow{MA} \cdot \overrightarrow{MB} = k$ pour $k = 5$, puis $k = -4$, puis $k = -6$.

??? success "Correction"
    1. $\overrightarrow{MA} \cdot \overrightarrow{MB} = MI^2 - \frac{AB^2}{4} = MI^2 - 4$.
    2. - $k = 5$ : $MI^2 = 9$, cercle de centre $I$ et de rayon $3$.
       - $k = -4$ : $MI^2 = 0$, l'ensemble est réduit au point $I$.
       - $k = -6$ : $MI^2 = -2$ est impossible, l'ensemble est vide.

### Exercice 26 — Lignes de niveau de $\overrightarrow{AB} \cdot \overrightarrow{AM}$ <span class="etoiles">★★</span>

$A$ et $B$ sont deux points tels que $AB = 4$. Déterminer l'ensemble des points $M$ tels que :

1. $\overrightarrow{AB} \cdot \overrightarrow{AM} = 8$ ;
2. $\overrightarrow{AB} \cdot \overrightarrow{AM} = -4$.

??? success "Correction"
    Soit $H$ le projeté orthogonal de $M$ sur $(AB)$ : $\overrightarrow{AB} \cdot \overrightarrow{AM} = \overrightarrow{AB} \cdot \overrightarrow{AH}$.

    1. $\overrightarrow{AB} \cdot \overrightarrow{AH} = 8 > 0$ : $\overrightarrow{AH}$ a le sens de $\overrightarrow{AB}$ et $4 \times AH = 8$, donc $AH = 2$ : $H$ est le milieu de $[AB]$. L'ensemble est la droite perpendiculaire à $(AB)$ passant par ce milieu : la **médiatrice de $[AB]$**.
    2. $\overrightarrow{AB} \cdot \overrightarrow{AH} = -4 < 0$ : $H$ est sur $(AB)$, du côté opposé à $B$ par rapport à $A$, avec $AH = 1$. L'ensemble est la droite perpendiculaire à $(AB)$ passant par ce point $H$.

### Exercice 27 — Produit scalaire en Python <span class="etoiles">★★★</span>

On représente un vecteur par une **liste** de deux nombres, par exemple `u = [3, -2]`.

1. Écrire une fonction `prod_scal(u, v)` qui renvoie le produit scalaire de `u` et `v` dans une base orthonormée.
2. Écrire une fonction `norme(u)`, puis une fonction `angle(u, v)` qui renvoie l'angle entre deux vecteurs non nuls, en degrés.
3. Écrire une fonction `rectangle(A, B, C)` qui renvoie `True` si le triangle $ABC$ (points donnés par des listes de coordonnées) est rectangle.

??? success "Correction"
    ```python
    from math import sqrt, acos, degrees

    def prod_scal(u, v):
        return u[0] * v[0] + u[1] * v[1]

    def norme(u):
        return sqrt(prod_scal(u, u))

    def angle(u, v):
        return degrees(acos(prod_scal(u, v) / (norme(u) * norme(v))))

    def vecteur(P, Q):
        return [Q[0] - P[0], Q[1] - P[1]]

    def rectangle(A, B, C):
        pA = prod_scal(vecteur(A, B), vecteur(A, C))
        pB = prod_scal(vecteur(B, A), vecteur(B, C))
        pC = prod_scal(vecteur(C, A), vecteur(C, B))
        return pA == 0 or pB == 0 or pC == 0

    print(angle([2, 1], [1, 3]))               # 45.0 (à l'arrondi près)
    print(rectangle([-2, 1], [2, 3], [3, 1]))  # True (exercice 13)
    ```

    Avec des coordonnées décimales, on remplacera le test `== 0` par `abs(...) < 1e-9`, car les calculs sur les flottants ne sont pas exacts.

### Exercice 28 — Une formule d'addition <span class="etoiles">★★★</span>

Soit $a$ et $b$ deux réels avec $0 \leq a \leq b \leq a + \pi$. On considère les vecteurs $\vec{u}\begin{pmatrix} \cos a \\ \sin a \end{pmatrix}$ et $\vec{v}\begin{pmatrix} \cos b \\ \sin b \end{pmatrix}$, dont l'angle géométrique vaut $b - a$.

1. Calculer $\vec{u} \cdot \vec{v}$ de deux façons. En déduire que $\cos(b - a) = \cos a\cos b + \sin a\sin b$.
2. En remarquant que $\frac{\pi}{12} = \frac{\pi}{3} - \frac{\pi}{4}$, calculer la valeur exacte de $\cos\frac{\pi}{12}$.

??? success "Correction"
    1. Avec les coordonnées : $\vec{u} \cdot \vec{v} = \cos a\cos b + \sin a\sin b$. Avec le cosinus : $\|\vec{u}\| = \|\vec{v}\| = 1$ (car $\cos^2 + \sin^2 = 1$), donc $\vec{u} \cdot \vec{v} = \cos(b - a)$. D'où l'égalité. *Elle reste vraie pour tous réels $a$ et $b$ : on le démontre en Terminale.*
    2. $\cos\frac{\pi}{12} = \cos\frac{\pi}{4}\cos\frac{\pi}{3} + \sin\frac{\pi}{4}\sin\frac{\pi}{3} = \frac{\sqrt{2}}{2} \times \frac{1}{2} + \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} = \frac{\sqrt{2} + \sqrt{6}}{4}$.
