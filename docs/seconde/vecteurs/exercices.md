# Exercices corrigés — Vecteurs

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf l'exercice Python. Sauf mention contraire, les repères sont **orthonormés**.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Égalité, somme, relation de Chasles | 1 à 6 |
| 2. Produit par un réel, colinéarité | 7 à 11 |
| 3. Coordonnées, milieu, distance | 12 à 17 |
| 4. Déterminant, alignement, parallélisme | 18 à 23 |
| 5. Problèmes et approfondissement | 24 à 28 |

---

## Thème 1 — Égalité, somme, relation de Chasles

*Méthode associée : [Méthode 1](methodes.md#methode-1-simplifier-une-somme-de-vecteurs-avec-la-relation-de-chasles).*

### Exercice 1 — Vecteurs égaux <span class="etoiles">★</span>

$ABCD$ est un parallélogramme de centre $O$. Citer tous les vecteurs égaux à $\overrightarrow{AB}$, à $\overrightarrow{AO}$ et à $\overrightarrow{BO}$ dont les extrémités sont parmi $A$, $B$, $C$, $D$, $O$.

??? success "Correction"
    $\overrightarrow{AB} = \overrightarrow{DC}$ ; $\overrightarrow{AO} = \overrightarrow{OC}$ ; $\overrightarrow{BO} = \overrightarrow{OD}$ (les diagonales d'un parallélogramme se coupent en leur milieu).

### Exercice 2 — Chasles <span class="etoiles">★</span>

Simplifier : $\overrightarrow{AB} + \overrightarrow{BC} + \overrightarrow{CD}$ ; $\overrightarrow{MN} - \overrightarrow{PN}$ ; $\overrightarrow{AB} - \overrightarrow{AC} + \overrightarrow{BC}$.

??? success "Correction"
    $\overrightarrow{AD}$ ; $\overrightarrow{MN} + \overrightarrow{NP} = \overrightarrow{MP}$ ; $\overrightarrow{AB} + \overrightarrow{CA} + \overrightarrow{BC} = \overrightarrow{CA} + \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{CC} = \vec{0}$.

### Exercice 3 — Construire une somme <span class="etoiles">★</span>

$ABC$ est un triangle. Construire les points $D$ et $E$ tels que $\overrightarrow{AD} = \overrightarrow{AB} + \overrightarrow{AC}$ et $\overrightarrow{BE} = \overrightarrow{BA} + \overrightarrow{CB}$. Quelle est la nature de $ABDC$ ?

??? success "Correction"
    Par la règle du parallélogramme, $ABDC$ est un parallélogramme : $D$ est le quatrième sommet, opposé à $A$.

    $\overrightarrow{BE} = \overrightarrow{CB} + \overrightarrow{BA} = \overrightarrow{CA}$ : $E$ est l'image de $B$ par la translation de vecteur $\overrightarrow{CA}$ ($BEAC$ est un parallélogramme, et $\overrightarrow{BE} = \overrightarrow{CA}$).

### Exercice 4 — Décomposer <span class="etoiles">★★</span>

$ABCD$ est un parallélogramme. Exprimer en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AD}$ les vecteurs $\overrightarrow{AC}$, $\overrightarrow{BD}$ et $\overrightarrow{CA} + \overrightarrow{BD}$.

??? success "Correction"
    $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AB} + \overrightarrow{AD}$. $\overrightarrow{BD} = \overrightarrow{BA} + \overrightarrow{AD} = \overrightarrow{AD} - \overrightarrow{AB}$. $\overrightarrow{CA} + \overrightarrow{BD} = -\overrightarrow{AB} - \overrightarrow{AD} + \overrightarrow{AD} - \overrightarrow{AB} = -2\overrightarrow{AB}$.

### Exercice 5 — Égalité à démontrer <span class="etoiles">★★</span>

Démontrer que pour tous points $A$, $B$, $C$, $D$ : $\overrightarrow{AB} + \overrightarrow{CD} = \overrightarrow{AD} + \overrightarrow{CB}$.

??? success "Correction"
    $\overrightarrow{AB} + \overrightarrow{CD} = \left(\overrightarrow{AD} + \overrightarrow{DB}\right) + \left(\overrightarrow{CB} + \overrightarrow{BD}\right) = \overrightarrow{AD} + \overrightarrow{CB} + \left(\overrightarrow{DB} + \overrightarrow{BD}\right) = \overrightarrow{AD} + \overrightarrow{CB}$.

### Exercice 6 — Le point $G$ <span class="etoiles">★★★</span>

$ABC$ est un triangle et $G$ le point tel que $\overrightarrow{GA} + \overrightarrow{GB} + \overrightarrow{GC} = \vec{0}$.

1. En utilisant la relation de Chasles avec le point $A$, montrer que $\overrightarrow{AG} = \frac{1}{3}\left(\overrightarrow{AB} + \overrightarrow{AC}\right)$.
2. Soit $I$ le milieu de $[BC]$. Montrer que $\overrightarrow{AB} + \overrightarrow{AC} = 2\overrightarrow{AI}$, puis que $\overrightarrow{AG} = \frac{2}{3}\overrightarrow{AI}$. Que représente $G$ ?

??? success "Correction"
    1. $\overrightarrow{GB} = \overrightarrow{GA} + \overrightarrow{AB}$ et $\overrightarrow{GC} = \overrightarrow{GA} + \overrightarrow{AC}$, donc $3\overrightarrow{GA} + \overrightarrow{AB} + \overrightarrow{AC} = \vec{0}$, soit $3\overrightarrow{AG} = \overrightarrow{AB} + \overrightarrow{AC}$.
    2. $\overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AI} + \overrightarrow{IB} + \overrightarrow{AI} + \overrightarrow{IC} = 2\overrightarrow{AI}$, car $\overrightarrow{IB} + \overrightarrow{IC} = \vec{0}$. Donc $\overrightarrow{AG} = \frac{2}{3}\overrightarrow{AI}$ : $G$ est sur la médiane issue de $A$, aux deux tiers depuis $A$. C'est le **centre de gravité** du triangle.

---

## Thème 2 — Produit par un réel, colinéarité

### Exercice 7 — Construire <span class="etoiles">★</span>

Sur un segment $[AB]$ de longueur $6$ cm, placer les points $M$, $N$, $P$ tels que $\overrightarrow{AM} = \frac{1}{3}\overrightarrow{AB}$, $\overrightarrow{AN} = -\frac{1}{2}\overrightarrow{AB}$ et $\overrightarrow{BP} = \frac{3}{2}\overrightarrow{BA}$. Calculer $AM$, $AN$ et $AP$.

??? success "Correction"
    $M$ est sur $[AB]$ avec $AM = 2$ cm. $N$ est sur la droite $(AB)$, du côté opposé à $B$, avec $AN = 3$ cm. $\overrightarrow{BP}$ a le sens de $\overrightarrow{BA}$ et mesure $9$ cm : $P$ est au-delà de $A$, avec $AP = 9 - 6 = 3$ cm. En fait $P = N$.

### Exercice 8 — Réduire <span class="etoiles">★</span>

Simplifier $\vec{w} = 3(\vec{u} - 2\vec{v}) - 2(\vec{u} + \vec{v}) + 8\vec{v}$.

??? success "Correction"
    $3\vec{u} - 6\vec{v} - 2\vec{u} - 2\vec{v} + 8\vec{v} = \vec{u}$.

### Exercice 9 — Milieux et parallèles <span class="etoiles">★★</span>

$ABC$ est un triangle, $I$ le milieu de $[AB]$ et $J$ le milieu de $[AC]$. Démontrer que $\overrightarrow{IJ} = \frac{1}{2}\overrightarrow{BC}$. Que retrouve-t-on ?

??? success "Correction"
    $\overrightarrow{IJ} = \overrightarrow{IA} + \overrightarrow{AJ} = \frac{1}{2}\overrightarrow{BA} + \frac{1}{2}\overrightarrow{AC} = \frac{1}{2}\left(\overrightarrow{BA} + \overrightarrow{AC}\right) = \frac{1}{2}\overrightarrow{BC}$. On retrouve le **théorème des milieux** : $(IJ) \parallel (BC)$ et $IJ = \frac{1}{2}BC$.

### Exercice 10 — Alignement sans repère <span class="etoiles">★★</span>

$ABC$ est un triangle. On définit $E$ et $F$ par $\overrightarrow{AE} = 2\overrightarrow{AB} + \overrightarrow{AC}$ et $\overrightarrow{BF} = \frac{1}{2}\overrightarrow{AC}$. Exprimer $\overrightarrow{AF}$ en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AC}$, puis démontrer que $A$, $E$, $F$ sont alignés.

??? success "Correction"
    $\overrightarrow{AF} = \overrightarrow{AB} + \overrightarrow{BF} = \overrightarrow{AB} + \frac{1}{2}\overrightarrow{AC}$. Alors $2\overrightarrow{AF} = 2\overrightarrow{AB} + \overrightarrow{AC} = \overrightarrow{AE}$ : les vecteurs $\overrightarrow{AE}$ et $\overrightarrow{AF}$ sont colinéaires, donc $A$, $E$, $F$ sont alignés ($F$ est même le milieu de $[AE]$).

### Exercice 11 — Un point aligné <span class="etoiles">★★★</span>

$ABCD$ est un parallélogramme. $E$ est défini par $\overrightarrow{BE} = \frac{1}{3}\overrightarrow{BC}$ et $F$ par $\overrightarrow{AF} = \frac{3}{2}\overrightarrow{AB}$.

1. Exprimer $\overrightarrow{DE}$ et $\overrightarrow{DF}$ en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AD}$.
2. En déduire que $D$, $E$, $F$ sont alignés.

??? success "Correction"
    1. $\overrightarrow{DE} = \overrightarrow{DA} + \overrightarrow{AB} + \overrightarrow{BE} = -\overrightarrow{AD} + \overrightarrow{AB} + \frac{1}{3}\overrightarrow{AD} = \overrightarrow{AB} - \frac{2}{3}\overrightarrow{AD}$.

        $\overrightarrow{DF} = \overrightarrow{DA} + \overrightarrow{AF} = \frac{3}{2}\overrightarrow{AB} - \overrightarrow{AD}$.
    2. $\frac{3}{2}\overrightarrow{DE} = \frac{3}{2}\overrightarrow{AB} - \overrightarrow{AD} = \overrightarrow{DF}$ : les vecteurs sont colinéaires, donc $D$, $E$, $F$ sont alignés.

---

## Thème 3 — Coordonnées, milieu, distance

*Méthodes associées : [Méthode 2](methodes.md#methode-2-construire-un-point-defini-par-une-egalite-vectorielle) et [Méthode 3](methodes.md#methode-3-determiner-la-nature-dun-triangle-ou-dun-quadrilatere).*

### Exercice 12 — Coordonnées de vecteurs <span class="etoiles">★</span>

On donne $A(2\,;\,-1)$, $B(5\,;\,3)$, $C(-1\,;\,4)$. Calculer les coordonnées de $\overrightarrow{AB}$, $\overrightarrow{AC}$, $\overrightarrow{AB} + \overrightarrow{AC}$ et $3\overrightarrow{AB} - 2\overrightarrow{AC}$.

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ ; $\overrightarrow{AC}\begin{pmatrix} -3 \\ 5 \end{pmatrix}$ ; somme $\begin{pmatrix} 0 \\ 9 \end{pmatrix}$ ; $\begin{pmatrix} 9 + 6 \\ 12 - 10 \end{pmatrix} = \begin{pmatrix} 15 \\ 2 \end{pmatrix}$.

### Exercice 13 — Milieu et symétrique <span class="etoiles">★</span>

On donne $A(-3\,;\,2)$ et $B(5\,;\,-4)$.

1. Calculer les coordonnées du milieu $I$ de $[AB]$ et la longueur $AB$.
2. Calculer les coordonnées du symétrique $A'$ de $A$ par rapport à $B$.

??? success "Correction"
    1. $I(1\,;\,-1)$ ; $AB = \sqrt{64 + 36} = 10$.
    2. $B$ est le milieu de $[AA']$ : $\frac{-3 + x}{2} = 5$, donc $x = 13$ ; $\frac{2 + y}{2} = -4$, donc $y = -10$. $A'(13\,;\,-10)$.

### Exercice 14 — Nature d'un triangle <span class="etoiles">★</span>

On donne $A(-1\,;\,2)$, $B(3\,;\,4)$ et $C(1\,;\,-2)$. Quelle est la nature du triangle $ABC$ ?

??? success "Correction"
    $AB^2 = 16 + 4 = 20$, $AC^2 = 4 + 16 = 20$, $BC^2 = 4 + 36 = 40$. $AB = AC$ et $AB^2 + AC^2 = BC^2$ : le triangle est **rectangle isocèle en $A$**.

### Exercice 15 — Quatrième sommet <span class="etoiles">★★</span>

On donne $A(1\,;\,0)$, $B(4\,;\,2)$ et $C(2\,;\,5)$. Déterminer les coordonnées de $D$ tel que $ABCD$ soit un parallélogramme, puis celles de son centre.

??? success "Correction"
    $\overrightarrow{AD} = \overrightarrow{BC}\begin{pmatrix} -2 \\ 3 \end{pmatrix}$, donc $D(-1\,;\,3)$. Le centre est le milieu de $[AC]$ : $\left(\frac{3}{2}\,;\,\frac{5}{2}\right)$ (c'est aussi le milieu de $[BD]$, ce qui vérifie le calcul).

### Exercice 16 — Nature d'un quadrilatère <span class="etoiles">★★</span>

On donne $A(1\,;\,-1)$, $B(4\,;\,3)$, $C(0\,;\,6)$ et $D(-3\,;\,2)$. Démontrer que $ABCD$ est un carré.

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \overrightarrow{DC}$ : parallélogramme. $AB^2 = 25$ et $AD^2 = 16 + 9 = 25$ : deux côtés consécutifs égaux, c'est un losange. $AC^2 = 1 + 49 = 50$ et $BD^2 = 49 + 1 = 50$ : diagonales de même longueur, c'est aussi un rectangle. C'est donc un **carré**.

### Exercice 17 — Cercle et distance <span class="etoiles">★★★</span>

Soit $\Omega(2\,;\,1)$ et $A(5\,;\,5)$.

1. Calculer le rayon du cercle $\mathcal{C}$ de centre $\Omega$ passant par $A$.
2. Les points $B(-2\,;\,4)$ et $C(6\,;\,-2)$ sont-ils sur $\mathcal{C}$ ?
3. Déterminer les coordonnées du point $A'$ diamétralement opposé à $A$.

??? success "Correction"
    1. $\Omega A = \sqrt{9 + 16} = 5$.
    2. $\Omega B = \sqrt{16 + 9} = 5$ : oui. $\Omega C = \sqrt{16 + 9} = 5$ : oui.
    3. $\Omega$ est le milieu de $[AA']$ : $A'(2 \times 2 - 5\,;\,2 \times 1 - 5) = (-1\,;\,-3)$.

---

## Thème 4 — Déterminant, alignement, parallélisme

*Méthode associée : [Méthode 4](methodes.md#methode-4-demontrer-un-alignement-ou-un-parallelisme).*

### Exercice 18 — Calculer des déterminants <span class="etoiles">★</span>

Les vecteurs suivants sont-ils colinéaires ?

1. $\vec{u}\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -2 \\ 3 \end{pmatrix}$.
2. $\vec{u}\begin{pmatrix} \sqrt{2} \\ 1 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 2 \\ \sqrt{2} \end{pmatrix}$.
3. $\vec{u}\begin{pmatrix} 3 \\ 5 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 5 \\ 8 \end{pmatrix}$.

??? success "Correction"
    1. $4 \times 3 - (-2) \times (-6) = 12 - 12 = 0$ : oui.
    2. $\sqrt{2} \times \sqrt{2} - 2 \times 1 = 0$ : oui.
    3. $24 - 25 = -1 \neq 0$ : non (même si les coordonnées « se ressemblent »).

### Exercice 19 — Points alignés <span class="etoiles">★</span>

Les points $A(-1\,;\,-2)$, $B(1\,;\,1)$ et $C(5\,;\,7)$ sont-ils alignés ? Et $A$, $B$ et $D(4\,;\,6)$ ?

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 6 \\ 9 \end{pmatrix}$ : $18 - 18 = 0$, alignés.

    $\overrightarrow{AD}\begin{pmatrix} 5 \\ 8 \end{pmatrix}$ : $16 - 15 = 1 \neq 0$, non alignés.

### Exercice 20 — Trouver un paramètre <span class="etoiles">★★</span>

1. Déterminer $m$ pour que $\vec{u}\begin{pmatrix} m \\ 4 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 3 \\ 6 \end{pmatrix}$ soient colinéaires.
2. Déterminer l'ordonnée $y$ du point $C(4\,;\,y)$ pour que $A(0\,;\,1)$, $B(2\,;\,4)$ et $C$ soient alignés.

??? success "Correction"
    1. $6m - 12 = 0 \iff m = 2$.
    2. $\overrightarrow{AB}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 4 \\ y - 1 \end{pmatrix}$ : $2(y - 1) - 12 = 0 \iff y = 7$.

### Exercice 21 — Trapèze <span class="etoiles">★★</span>

On donne $A(-2\,;\,0)$, $B(4\,;\,2)$, $C(3\,;\,5)$ et $D(0\,;\,4)$. Démontrer que $ABCD$ est un trapèze. Est-ce un parallélogramme ?

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 6 \\ 2 \end{pmatrix}$ et $\overrightarrow{DC}\begin{pmatrix} 3 \\ 1 \end{pmatrix}$ : $6 - 6 = 0$, donc $(AB) \parallel (DC)$ : trapèze. Comme $\overrightarrow{AB} = 2\overrightarrow{DC} \neq \overrightarrow{DC}$, ce n'est pas un parallélogramme.

### Exercice 22 — Intersection des diagonales <span class="etoiles">★★</span>

On reprend le trapèze de l'exercice 21. Vérifier que le point $M\left(\frac{4}{3}\,;\,\frac{10}{3}\right)$ appartient aux deux diagonales $(AC)$ et $(BD)$. Que représente-t-il ?

??? success "Correction"
    $\overrightarrow{AC}\begin{pmatrix} 5 \\ 5 \end{pmatrix}$ et $\overrightarrow{AM}\begin{pmatrix} \frac{10}{3} \\ \frac{10}{3} \end{pmatrix}$ : $5 \times \frac{10}{3} - \frac{10}{3} \times 5 = 0$, donc $M \in (AC)$.

    $\overrightarrow{BD}\begin{pmatrix} -4 \\ 2 \end{pmatrix}$ et $\overrightarrow{BM}\begin{pmatrix} -\frac{8}{3} \\ \frac{4}{3} \end{pmatrix}$ : $-4 \times \frac{4}{3} - \left(-\frac{8}{3}\right) \times 2 = -\frac{16}{3} + \frac{16}{3} = 0$, donc $M \in (BD)$.

    $M$ est le point d'intersection des diagonales du trapèze.

### Exercice 23 — Concours de droites <span class="etoiles">★★★</span>

Dans un repère, on donne $A(0\,;\,0)$, $B(6\,;\,0)$ et $C(0\,;\,6)$. $I$ est le milieu de $[BC]$, $J$ celui de $[AC]$, $K$ celui de $[AB]$, et $G(2\,;\,2)$.

1. Calculer les coordonnées de $I$, $J$ et $K$.
2. Démontrer que $G$ appartient aux trois médianes $(AI)$, $(BJ)$ et $(CK)$.

??? success "Correction"
    1. $I(3\,;\,3)$, $J(0\,;\,3)$, $K(3\,;\,0)$.
    2. $\overrightarrow{AI}\begin{pmatrix} 3 \\ 3 \end{pmatrix}$ et $\overrightarrow{AG}\begin{pmatrix} 2 \\ 2 \end{pmatrix}$ : $6 - 6 = 0$. $\overrightarrow{BJ}\begin{pmatrix} -6 \\ 3 \end{pmatrix}$ et $\overrightarrow{BG}\begin{pmatrix} -4 \\ 2 \end{pmatrix}$ : $-12 + 12 = 0$. $\overrightarrow{CK}\begin{pmatrix} 3 \\ -6 \end{pmatrix}$ et $\overrightarrow{CG}\begin{pmatrix} 2 \\ -4 \end{pmatrix}$ : $-12 + 12 = 0$. $G$ est sur les trois médianes : c'est le centre de gravité.

---

## Thème 5 — Problèmes et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-demontrer-quun-quadrilatere-est-un-parallelogramme).*

### Exercice 24 — Parallélogramme par les milieux <span class="etoiles">★★</span>

On donne $A(-1\,;\,1)$, $B(3\,;\,0)$, $C(5\,;\,3)$ et $D(1\,;\,4)$. Démontrer de deux façons que $ABCD$ est un parallélogramme.

??? success "Correction"
    $\overrightarrow{AB}\begin{pmatrix} 4 \\ -1 \end{pmatrix}$ et $\overrightarrow{DC}\begin{pmatrix} 4 \\ -1 \end{pmatrix}$ : égaux.

    Milieu de $[AC]$ : $(2\,;\,2)$ ; milieu de $[BD]$ : $(2\,;\,2)$ : les diagonales ont le même milieu.

### Exercice 25 — Théorème de Varignon <span class="etoiles">★★★</span>

$ABCD$ est un quadrilatère quelconque. $I$, $J$, $K$, $L$ sont les milieux de $[AB]$, $[BC]$, $[CD]$, $[DA]$. Démontrer que $\overrightarrow{IJ} = \frac{1}{2}\overrightarrow{AC} = \overrightarrow{LK}$. Qu'en déduit-on pour $IJKL$ ?

??? success "Correction"
    Comme dans l'exercice 9 : $\overrightarrow{IJ} = \overrightarrow{IB} + \overrightarrow{BJ} = \frac{1}{2}\overrightarrow{AB} + \frac{1}{2}\overrightarrow{BC} = \frac{1}{2}\overrightarrow{AC}$. De même, $\overrightarrow{LK} = \overrightarrow{LD} + \overrightarrow{DK} = \frac{1}{2}\overrightarrow{AD} + \frac{1}{2}\overrightarrow{DC} = \frac{1}{2}\overrightarrow{AC}$. Donc $\overrightarrow{IJ} = \overrightarrow{LK}$ : $IJKL$ est **toujours** un parallélogramme.

### Exercice 26 — Physique : somme de forces <span class="etoiles">★★</span>

Un objet est soumis à trois forces représentées par $\vec{F_1}\begin{pmatrix} 3 \\ 1 \end{pmatrix}$, $\vec{F_2}\begin{pmatrix} -1 \\ 4 \end{pmatrix}$ et $\vec{F_3}$ (en newtons). Il reste immobile, ce qui impose $\vec{F_1} + \vec{F_2} + \vec{F_3} = \vec{0}$. Déterminer $\vec{F_3}$ et sa norme.

??? success "Correction"
    $\vec{F_3} = -\vec{F_1} - \vec{F_2}\begin{pmatrix} -2 \\ -5 \end{pmatrix}$, de norme $\sqrt{4 + 25} = \sqrt{29} \approx 5{,}4$ N.

### Exercice 27 — Colinéarité en Python <span class="etoiles">★★★</span>

Un vecteur est représenté par une liste `[x, y]` et un point par une liste `[x, y]`.

1. Écrire une fonction `vecteur(A, B)` qui renvoie les coordonnées de $\overrightarrow{AB}$, et une fonction `det(u, v)`.
2. Écrire une fonction `alignes(A, B, C)` qui renvoie `True` si les trois points sont alignés.
3. Écrire une fonction `parallelogramme(A, B, C, D)`.

??? success "Correction"
    ```python
    def vecteur(A, B):
        return [B[0] - A[0], B[1] - A[1]]

    def det(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def alignes(A, B, C):
        return det(vecteur(A, B), vecteur(A, C)) == 0

    def parallelogramme(A, B, C, D):
        return vecteur(A, B) == vecteur(D, C)

    print(alignes([-1, -2], [1, 1], [5, 7]))                # True
    print(parallelogramme([1, 1], [5, 2], [6, 5], [2, 4]))  # True
    ```

    Avec des coordonnées décimales, on remplacera le test `== 0` par `abs(...) < 1e-9`.

### Exercice 28 — Un problème d'alignement <span class="etoiles">★★★</span>

$ABCD$ est un carré. On se place dans le repère $\left(A\,;\,\overrightarrow{AB},\,\overrightarrow{AD}\right)$. $E$ est le point tel que $BCE$ soit équilatéral, à l'extérieur du carré, et $F$ tel que $DCF$ soit équilatéral, à l'intérieur du carré. On admet que $E\left(1 + \frac{\sqrt{3}}{2}\,;\,\frac{1}{2}\right)$ et $F\left(\frac{1}{2}\,;\,1 - \frac{\sqrt{3}}{2}\right)$.

Démontrer que $A$, $F$ et $E$ sont alignés.

??? success "Correction"
    $\overrightarrow{AF}\begin{pmatrix} \frac{1}{2} \\ 1 - \frac{\sqrt{3}}{2} \end{pmatrix}$ et $\overrightarrow{AE}\begin{pmatrix} 1 + \frac{\sqrt{3}}{2} \\ \frac{1}{2} \end{pmatrix}$.
    $$\det = \frac{1}{2} \times \frac{1}{2} - \left(1 + \frac{\sqrt{3}}{2}\right)\left(1 - \frac{\sqrt{3}}{2}\right) = \frac{1}{4} - \left(1 - \frac{3}{4}\right) = \frac{1}{4} - \frac{1}{4} = 0.$$
    Les points $A$, $F$, $E$ sont alignés.
