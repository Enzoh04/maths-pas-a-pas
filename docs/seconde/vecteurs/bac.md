# Évaluations type — Vecteurs

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Chaque évaluation dure environ **40 minutes**, **sans calculatrice**. Elle commence par **six questions d'automatismes** (comme dans l'épreuve anticipée de Première), puis comporte **un exercice** sur le chapitre. Les repères sont orthonormés.

| Évaluation | Exercice | Durée conseillée |
|---|---|---|
| 1 | Question de cours : critère de colinéarité | 35 min |
| 2 | Calcul vectoriel sans repère | 35 min |
| 3 | Nature d'un quadrilatère | 40 min |
| 4 | Alignement dans un repère | 40 min |

## Évaluation 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** Avec $A(1\,;\,3)$ et $B(4\,;\,-1)$, le vecteur $\overrightarrow{AB}$ a pour coordonnées :

a. $(5\,;\,2)$ ; b. $(3\,;\,-4)$ ; c. $(-3\,;\,4)$ ; d. $(3\,;\,4)$.

**Question 2.** La distance $AB$ (avec les mêmes points) vaut :

a. $5$ ; b. $7$ ; c. $25$ ; d. $\sqrt{7}$.

**Question 3.** Le milieu de $[AB]$ est :

a. $(2{,}5\,;\,1)$ ; b. $(1{,}5\,;\,-2)$ ; c. $(5\,;\,2)$ ; d. $(2{,}5\,;\,2)$.

**Question 4.** $\det\left(\begin{pmatrix} 2 \\ 5 \end{pmatrix}, \begin{pmatrix} 3 \\ 7 \end{pmatrix}\right)$ vaut :

a. $29$ ; b. $1$ ; c. $-1$ ; d. $0$.

**Question 5.** $\dfrac{5}{2} - \dfrac{1}{3}$ est égal à :

a. $\frac{13}{6}$ ; b. $\frac{4}{-1}$ ; c. $2$ ; d. $\frac{4}{6}$.

**Question 6.** Une hausse de $10\,\%$ suivie d'une baisse de $10\,\%$ revient à :

a. ne rien changer ; b. une baisse de $1\,\%$ ; c. une hausse de $1\,\%$ ; d. une baisse de $10\,\%$.

### Partie 2 — Exercice

**A. Question de cours.** Soit $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$.

1. Démontrer que si $\vec{u}$ et $\vec{v}$ sont colinéaires, alors $xy' - x'y = 0$.
2. Démontrer la réciproque dans le cas où $x \neq 0$.

**B. Application.** On donne $A(-2\,;\,-1)$, $B(1\,;\,1)$, $C(7\,;\,5)$ et $D(4\,;\,6)$.

1. Démontrer que $A$, $B$, $C$ sont alignés.
2. Les droites $(AB)$ et $(CD)$ sont-elles parallèles ?
3. Déterminer l'ordonnée $y$ du point $E(10\,;\,y)$ pour que $E$ soit sur la droite $(AB)$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **a.** $\sqrt{9 + 16}$. 3. **a.** 4. **c.** $14 - 15$. 5. **a.** 6. **b.** $1{,}1 \times 0{,}9 = 0{,}99$.

    **Partie 2**

    **A. 1.** Si $\vec{u} = \vec{0}$, le déterminant est nul. Sinon $\vec{v} = k\vec{u}$ : $x' = kx$, $y' = ky$, et $x(ky) - (kx)y = 0$.

    **2.** Si $xy' = x'y$ et $x \neq 0$, posons $k = \frac{x'}{x}$ : $x' = kx$ et $y' = \frac{x'y}{x} = ky$. Donc $\vec{v} = k\vec{u}$.

    **B. 1.** $\overrightarrow{AB}\begin{pmatrix} 3 \\ 2 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 9 \\ 6 \end{pmatrix}$ : $18 - 18 = 0$, alignés.

    **2.** $\overrightarrow{CD}\begin{pmatrix} -3 \\ 1 \end{pmatrix}$ : $3 \times 1 - (-3) \times 2 = 9 \neq 0$, non parallèles.

    **3.** $\overrightarrow{AE}\begin{pmatrix} 12 \\ y + 1 \end{pmatrix}$ : $3(y + 1) - 24 = 0 \iff y = 7$.

---

## Évaluation 2

### Partie 1 — Automatismes (QCM)

**Question 1.** $\overrightarrow{AB} + \overrightarrow{BC} + \overrightarrow{CA}$ est égal à :

a. $\overrightarrow{AC}$ ; b. $\vec{0}$ ; c. $2\overrightarrow{AC}$ ; d. $\overrightarrow{CA}$.

**Question 2.** $\overrightarrow{MA} - \overrightarrow{MB}$ est égal à :

a. $\overrightarrow{AB}$ ; b. $\overrightarrow{BA}$ ; c. $\vec{0}$ ; d. $2\overrightarrow{MA}$.

**Question 3.** Si $\overrightarrow{AB} = \overrightarrow{DC}$, alors :

a. $ABCD$ est un parallélogramme ; b. $ABDC$ est un parallélogramme ; c. $A = D$ ; d. $AB = 2DC$.

**Question 4.** $I$ est le milieu de $[AB]$ si et seulement si :

a. $\overrightarrow{IA} = \overrightarrow{IB}$ ; b. $\overrightarrow{AI} = \frac{1}{2}\overrightarrow{AB}$ ; c. $\overrightarrow{AI} = 2\overrightarrow{AB}$ ; d. $\overrightarrow{IA} + \overrightarrow{AB} = \vec{0}$.

**Question 5.** $(2x - 1)(2x + 1)$ est égal à :

a. $4x^2 - 1$ ; b. $4x^2 + 1$ ; c. $2x^2 - 1$ ; d. $4x^2 - 4x - 1$.

**Question 6.** La moyenne de $8$ notes est $12$. La somme des notes est :

a. $20$ ; b. $1{,}5$ ; c. $96$ ; d. $12$.

### Partie 2 — Exercice

$ABC$ est un triangle. On définit les points $D$ et $E$ par :
$$\overrightarrow{AD} = \frac{3}{2}\overrightarrow{AB} \qquad \text{et} \qquad \overrightarrow{CE} = \frac{1}{2}\overrightarrow{AB} - \overrightarrow{AC}.$$

1. Faire une figure.
2. Exprimer $\overrightarrow{AE}$ en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AC}$. Que peut-on dire des points $A$, $B$, $E$ ?
3. Exprimer $\overrightarrow{CD}$ en fonction de $\overrightarrow{AB}$ et $\overrightarrow{AC}$.
4. Soit $I$ le milieu de $[AB]$. Démontrer que $\overrightarrow{CI} = \frac{1}{2}\overrightarrow{AB} - \overrightarrow{AC}$, et en déduire la position de $E$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **b.** $\overrightarrow{MA} + \overrightarrow{BM} = \overrightarrow{BA}$. 3. **a.** 4. **b.** 5. **a.** 6. **c.**

    **Partie 2**

    **2.** $\overrightarrow{AE} = \overrightarrow{AC} + \overrightarrow{CE} = \frac{1}{2}\overrightarrow{AB}$ : $E$ est le **milieu de $[AB]$**, donc $A$, $B$, $E$ sont alignés.

    **3.** $\overrightarrow{CD} = \overrightarrow{CA} + \overrightarrow{AD} = \frac{3}{2}\overrightarrow{AB} - \overrightarrow{AC}$.

    **4.** $\overrightarrow{CI} = \overrightarrow{CA} + \overrightarrow{AI} = -\overrightarrow{AC} + \frac{1}{2}\overrightarrow{AB}$. Donc $\overrightarrow{CI} = \overrightarrow{CE}$, et $E = I$ : on retrouve que $E$ est le milieu de $[AB]$.

---

## Évaluation 3

### Partie 1 — Automatismes (QCM)

**Question 1.** Avec $A(-1\,;\,2)$ et $B(3\,;\,0)$, $AB^2$ vaut :

a. $20$ ; b. $8$ ; c. $\sqrt{20}$ ; d. $12$.

**Question 2.** $\sqrt{20}$ est égal à :

a. $4\sqrt{5}$ ; b. $2\sqrt{5}$ ; c. $5\sqrt{2}$ ; d. $10$.

**Question 3.** Un triangle de côtés $\sqrt{5}$, $\sqrt{20}$ et $5$ est :

a. équilatéral ; b. rectangle ; c. isocèle ; d. aucun des trois.

**Question 4.** Un parallélogramme dont les diagonales ont la même longueur est :

a. un losange ; b. un rectangle ; c. un trapèze ; d. toujours un carré.

**Question 5.** $\frac{1}{4}$ heure correspond à :

a. $25$ min ; b. $15$ min ; c. $40$ min ; d. $14$ min.

**Question 6.** $3^2 + 4^2$ est égal à :

a. $7^2$ ; b. $25$ ; c. $49$ ; d. $12$.

### Partie 2 — Exercice

On donne $A(-1\,;\,2)$, $B(3\,;\,0)$, $C(5\,;\,4)$.

1. Calculer $AB$, $BC$ et $AC$. Quelle est la nature du triangle $ABC$ ?
2. Déterminer les coordonnées du point $D$ tel que $ABCD$ soit un parallélogramme.
3. Démontrer que $ABCD$ est un carré.
4. Calculer les coordonnées du centre $\Omega$ du carré, et le rayon du cercle circonscrit.

??? success "Correction"
    **Partie 1**

    1. **a.** $16 + 4$. 2. **b.** 3. **b.** $5 + 20 = 25$. 4. **b.** 5. **b.** 6. **b.**

    **Partie 2**

    **1.** $AB^2 = 16 + 4 = 20$, $BC^2 = 4 + 16 = 20$, $AC^2 = 36 + 4 = 40$. $AB = BC = 2\sqrt{5}$ et $AB^2 + BC^2 = AC^2$ : rectangle isocèle en $B$.

    **2.** $\overrightarrow{AD} = \overrightarrow{BC}\begin{pmatrix} 2 \\ 4 \end{pmatrix}$, donc $D(1\,;\,6)$.

    **3.** Parallélogramme avec un angle droit en $B$ : c'est un rectangle ; avec deux côtés consécutifs égaux ($AB = BC$) : c'est un losange. C'est donc un carré.

    **4.** $\Omega$ est le milieu de $[AC]$ : $(2\,;\,3)$. Rayon : $\Omega A = \frac{AC}{2} = \frac{2\sqrt{10}}{2} = \sqrt{10}$.

---

## Évaluation 4

### Partie 1 — Automatismes (QCM)

**Question 1.** Les vecteurs $\begin{pmatrix} 2 \\ -3 \end{pmatrix}$ et $\begin{pmatrix} -4 \\ m \end{pmatrix}$ sont colinéaires pour $m$ égal à :

a. $6$ ; b. $-6$ ; c. $\frac{8}{3}$ ; d. $1$.

**Question 2.** $2\vec{u} - 3\vec{v}$ avec $\vec{u}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -1 \\ 1 \end{pmatrix}$ a pour coordonnées :

a. $(5\,;\,1)$ ; b. $(-1\,;\,1)$ ; c. $(5\,;\,7)$ ; d. $(-1\,;\,7)$.

**Question 3.** $\left(1 - \frac{\sqrt{2}}{2}\right)\left(1 + \frac{\sqrt{2}}{2}\right)$ est égal à :

a. $\frac{1}{2}$ ; b. $0$ ; c. $1 - \sqrt{2}$ ; d. $\frac{3}{2}$.

**Question 4.** La solution de $\frac{x}{3} = \frac{4}{6}$ est :

a. $2$ ; b. $8$ ; c. $\frac{1}{2}$ ; d. $4{,}5$.

**Question 5.** $5\,\%$ de $3\,000$ font :

a. $15$ ; b. $150$ ; c. $1\,500$ ; d. $60$.

**Question 6.** On tire une carte au hasard dans un jeu de $52$ cartes. La probabilité de tirer un as est :

a. $\frac{1}{52}$ ; b. $\frac{1}{4}$ ; c. $\frac{1}{13}$ ; d. $\frac{4}{13}$.

### Partie 2 — Exercice

$ABCD$ est un carré de côté $1$. On se place dans le repère orthonormé $\left(A\,;\,\overrightarrow{AB},\,\overrightarrow{AD}\right)$. $I$ est le milieu de $[BC]$, et $E$ est le point défini par $\overrightarrow{DE} = 2\overrightarrow{DC}$.

1. Donner les coordonnées de $A$, $B$, $C$, $D$, $I$ et $E$.
2. Démontrer que $A$, $I$, $E$ sont alignés.
3. Soit $F$ le point défini par $\overrightarrow{AF} = \frac{3}{2}\overrightarrow{AB}$. Les droites $(DF)$ et $(IE)$ sont-elles parallèles ?
4. Calculer la longueur $AE$ et vérifier que $AE = 2AI$.

??? success "Correction"
    **Partie 1**

    1. **a.** $2m - 12 = 0$. 2. **a.** $(2 + 3\,;\,4 - 3)$. 3. **a.** $1 - \frac{2}{4}$. 4. **a.** 5. **b.** 6. **c.** $\frac{4}{52}$.

    **Partie 2**

    **1.** $A(0\,;\,0)$, $B(1\,;\,0)$, $C(1\,;\,1)$, $D(0\,;\,1)$, $I\left(1\,;\,\frac{1}{2}\right)$, $E(2\,;\,1)$ (car $\overrightarrow{DE} = 2\overrightarrow{DC}\begin{pmatrix} 2 \\ 0 \end{pmatrix}$).

    **2.** $\overrightarrow{AI}\begin{pmatrix} 1 \\ \frac{1}{2} \end{pmatrix}$, $\overrightarrow{AE}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ : $1 \times 1 - 2 \times \frac{1}{2} = 0$, alignés.

    **3.** $F\left(\frac{3}{2}\,;\,0\right)$, $\overrightarrow{DF}\begin{pmatrix} \frac{3}{2} \\ -1 \end{pmatrix}$ et $\overrightarrow{IE}\begin{pmatrix} 1 \\ \frac{1}{2} \end{pmatrix}$ : $\frac{3}{2} \times \frac{1}{2} - 1 \times (-1) = \frac{7}{4} \neq 0$, non parallèles.

    **4.** $AE = \sqrt{4 + 1} = \sqrt{5}$ et $AI = \sqrt{1 + \frac{1}{4}} = \frac{\sqrt{5}}{2}$ : $AE = 2AI$ ($I$ est le milieu de $[AE]$).
