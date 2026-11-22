# Sujets type épreuve anticipée — Calcul vectoriel et produit scalaire

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

L'épreuve anticipée de mathématiques dure **2 heures, sans calculatrice**, avec un **QCM d'automatismes** (6 points) et **deux ou trois exercices** (14 points). Chaque sujet ci-dessous comporte **six questions d'automatismes** puis **un exercice**. Compte environ **40 minutes** par sujet. Les repères sont orthonormés.

| Sujet | Exercice | Durée conseillée |
|---|---|---|
| 1 | Question de cours : formule d'Al-Kashi | 35 min |
| 2 | Question de cours : cercle de diamètre $[AB]$ | 40 min |
| 3 | Dans un carré | 40 min |
| 4 | Triangle en coordonnées et ligne de niveau | 45 min |

## Sujet 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** Si $\vec{u}\begin{pmatrix} 2 \\ -3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 4 \\ 1 \end{pmatrix}$, alors $\vec{u} \cdot \vec{v}$ vaut :

a. $11$ ; b. $5$ ; c. $\begin{pmatrix} 8 \\ -3 \end{pmatrix}$ ; d. $-1$.

**Question 2.** La norme de $\vec{w}\begin{pmatrix} -6 \\ 8 \end{pmatrix}$ vaut :

a. $2$ ; b. $14$ ; c. $10$ ; d. $100$.

**Question 3.** $\cos\frac{2\pi}{3}$ est égal à :

a. $\frac{1}{2}$ ; b. $-\frac{1}{2}$ ; c. $\frac{\sqrt{3}}{2}$ ; d. $-\frac{\sqrt{3}}{2}$.

**Question 4.** $\sqrt{48}$ est égal à :

a. $4\sqrt{3}$ ; b. $3\sqrt{4}$ ; c. $16\sqrt{3}$ ; d. $6\sqrt{2}$.

**Question 5.** Un prix augmente de $10\,\%$ puis de $10\,\%$. Au total, il a augmenté de :

a. $20\,\%$ ; b. $21\,\%$ ; c. $19\,\%$ ; d. $1\,\%$.

**Question 6.** La fonction $x \mapsto x^2 - 4x + 1$ atteint son minimum en :

a. $x = -2$ ; b. $x = 4$ ; c. $x = 2$ ; d. $x = 1$.

### Partie 2 — Exercice

**A. Question de cours.** Soit $ABC$ un triangle, avec $a = BC$, $b = CA$ et $c = AB$. Démontrer que $a^2 = b^2 + c^2 - 2bc\cos\widehat{A}$.

**B. Application.** Dans un triangle $ABC$, $AB = 8$, $AC = 5$ et $\widehat{BAC} = \frac{\pi}{3}$.

1. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$.
2. Calculer $BC$.
3. Calculer $\cos\widehat{ABC}$.
4. Soit $H$ le projeté orthogonal de $C$ sur $(AB)$. Calculer $AH$, puis $CH$.

??? success "Correction"
    **Partie 1**

    1. **b.** $8 - 3$. 2. **c.** $\sqrt{36 + 64}$. 3. **b.** 4. **a.** $\sqrt{16 \times 3}$. 5. **b.** $1{,}1^2 = 1{,}21$. 6. **c.** $-\frac{b}{2a} = 2$.

    **Partie 2**

    **A.** $\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB}$, donc $a^2 = \left\|\overrightarrow{AC} - \overrightarrow{AB}\right\|^2 = AC^2 - 2\,\overrightarrow{AB} \cdot \overrightarrow{AC} + AB^2 = b^2 + c^2 - 2bc\cos\widehat{A}$, car $\overrightarrow{AB} \cdot \overrightarrow{AC} = AB \times AC \times \cos\widehat{A}$.

    **B. 1.** $8 \times 5 \times \frac{1}{2} = 20$.

    **2.** $BC^2 = 64 + 25 - 2 \times 20 = 49$, donc $BC = 7$.

    **3.** Al-Kashi en $B$ : $\cos\widehat{B} = \dfrac{BA^2 + BC^2 - AC^2}{2 \times BA \times BC} = \dfrac{64 + 49 - 25}{112} = \dfrac{88}{112} = \dfrac{11}{14}$.

    **4.** L'angle en $A$ est aigu, donc $\overrightarrow{AH}$ a le sens de $\overrightarrow{AB}$ : $\overrightarrow{AB} \cdot \overrightarrow{AC} = AB \times AH$, soit $20 = 8 \times AH$, donc $AH = \frac{5}{2}$. Pythagore dans $ACH$ : $CH^2 = 25 - \frac{25}{4} = \frac{75}{4}$, donc $CH = \frac{5\sqrt{3}}{2}$.

---

## Sujet 2

### Partie 1 — Automatismes (QCM)

**Question 1.** Les vecteurs $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\begin{pmatrix} -6 \\ m \end{pmatrix}$ sont orthogonaux lorsque $m$ vaut :

a. $-9$ ; b. $4$ ; c. $9$ ; d. $-4$.

**Question 2.** Les vecteurs $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\begin{pmatrix} -6 \\ m \end{pmatrix}$ sont colinéaires lorsque $m$ vaut :

a. $-9$ ; b. $4$ ; c. $9$ ; d. $-4$.

**Question 3.** Le milieu de $[AB]$ avec $A(-2\,;\,1)$ et $B(4\,;\,3)$ est :

a. $(3\,;\,1)$ ; b. $(1\,;\,2)$ ; c. $(6\,;\,2)$ ; d. $(2\,;\,4)$.

**Question 4.** $(x - 1)^2 + (y - 2)^2 = 10$ est l'équation d'un cercle de rayon :

a. $10$ ; b. $5$ ; c. $\sqrt{10}$ ; d. $100$.

**Question 5.** L'équation $x^2 = 2x$ a pour solutions :

a. $2$ seulement ; b. $0$ et $2$ ; c. $0$ seulement ; d. $-2$ et $2$.

**Question 6.** La moyenne de la série $4 \,;\, 8 \,;\, 9 \,;\, 11$ est :

a. $8$ ; b. $8{,}5$ ; c. $9$ ; d. $32$.

### Partie 2 — Exercice

**A. Question de cours.** Soit $A$ et $B$ deux points distincts et $I$ le milieu de $[AB]$.

1. Démontrer que pour tout point $M$, $\overrightarrow{MA} \cdot \overrightarrow{MB} = MI^2 - IA^2$.
2. En déduire l'ensemble des points $M$ tels que $\overrightarrow{MA} \cdot \overrightarrow{MB} = 0$.

**B. Application.** On donne $A(-2\,;\,1)$ et $B(4\,;\,3)$.

1. Soit $M(x\,;\,y)$. Montrer que $\overrightarrow{MA} \cdot \overrightarrow{MB} = 0$ équivaut à $(x - 1)^2 + (y - 2)^2 = 10$.
2. Le point $C(0\,;\,5)$ appartient-il à ce cercle ? Que peut-on en déduire pour le triangle $ABC$ ? Le vérifier par un calcul de produit scalaire.
3. Calculer l'aire du triangle $ABC$.

??? success "Correction"
    **Partie 1**

    1. **b.** $-12 + 3m = 0$. 2. **a.** $2m + 18 = 0$. 3. **b.** 4. **c.** 5. **b.** $x(x - 2) = 0$. 6. **a.** $\frac{32}{4}$.

    **Partie 2**

    **A. 1.** $\overrightarrow{MA} \cdot \overrightarrow{MB} = \left(\overrightarrow{MI} + \overrightarrow{IA}\right) \cdot \left(\overrightarrow{MI} + \overrightarrow{IB}\right)$ et $\overrightarrow{IB} = -\overrightarrow{IA}$, donc $\overrightarrow{MA} \cdot \overrightarrow{MB} = \left(\overrightarrow{MI} + \overrightarrow{IA}\right) \cdot \left(\overrightarrow{MI} - \overrightarrow{IA}\right) = MI^2 - IA^2$.

    **2.** $\overrightarrow{MA} \cdot \overrightarrow{MB} = 0 \iff MI = IA$ : c'est le cercle de centre $I$ et de rayon $IA = \frac{AB}{2}$, c'est-à-dire le cercle de diamètre $[AB]$.

    **B. 1.** $(-2 - x)(4 - x) + (1 - y)(3 - y) = 0 \iff x^2 - 2x - 8 + y^2 - 4y + 3 = 0$. Or $x^2 - 2x = (x - 1)^2 - 1$ et $y^2 - 4y = (y - 2)^2 - 4$ : l'équation devient $(x - 1)^2 + (y - 2)^2 - 10 = 0$.

    **2.** $(0 - 1)^2 + (5 - 2)^2 = 1 + 9 = 10$ : oui. $C$ est sur le cercle de diamètre $[AB]$, donc le triangle $ABC$ est rectangle en $C$. Vérification : $\overrightarrow{CA}\begin{pmatrix} -2 \\ -4 \end{pmatrix}$, $\overrightarrow{CB}\begin{pmatrix} 4 \\ -2 \end{pmatrix}$, et $\overrightarrow{CA} \cdot \overrightarrow{CB} = -8 + 8 = 0$.

    **3.** $CA = \sqrt{20} = 2\sqrt{5}$ et $CB = \sqrt{20} = 2\sqrt{5}$ : aire $= \frac{1}{2} \times 2\sqrt{5} \times 2\sqrt{5} = 10$.

---

## Sujet 3

### Partie 1 — Automatismes (QCM)

**Question 1.** $ABCD$ est un carré de côté $5$. $\overrightarrow{AB} \cdot \overrightarrow{AC}$ vaut :

a. $0$ ; b. $25$ ; c. $25\sqrt{2}$ ; d. $5\sqrt{2}$.

**Question 2.** Si $\|\vec{u}\| = 2$, $\|\vec{v}\| = 3$ et $\vec{u} \cdot \vec{v} = 1$, alors $\|\vec{u} + \vec{v}\|^2$ vaut :

a. $13$ ; b. $15$ ; c. $25$ ; d. $14$.

**Question 3.** Si $\vec{u} \cdot \vec{v} < 0$, l'angle entre $\vec{u}$ et $\vec{v}$ est :

a. nul ; b. aigu ; c. droit ; d. obtus.

**Question 4.** $\dfrac{2}{\sqrt{5}}$ est égal à :

a. $\frac{2\sqrt{5}}{5}$ ; b. $\frac{\sqrt{10}}{5}$ ; c. $\frac{2}{5}$ ; d. $\frac{\sqrt{5}}{2}$.

**Question 5.** La droite d'équation $y = -2x + 3$ passe par le point :

a. $(1\,;\,1)$ ; b. $(2\,;\,1)$ ; c. $(0\,;\,-2)$ ; d. $(3\,;\,0)$.

**Question 6.** On lance deux fois une pièce équilibrée. La probabilité d'obtenir deux fois « pile » est :

a. $\frac{1}{2}$ ; b. $\frac{1}{3}$ ; c. $\frac{1}{4}$ ; d. $1$.

### Partie 2 — Exercice

$ABCD$ est un carré de côté $4$. $E$ est le milieu de $[AB]$ et $F$ est le point de $[BC]$ tel que $BF = 1$. On se place dans le repère orthonormé d'origine $A$ tel que $B(4\,;\,0)$ et $D(0\,;\,4)$.

1. Donner les coordonnées de $C$, $E$ et $F$.
2. Calculer $\overrightarrow{ED} \cdot \overrightarrow{EF}$. Que peut-on en déduire pour le triangle $DEF$ ?
3. Calculer $DE$, $EF$ et $DF$, et vérifier le résultat avec le théorème de Pythagore.
4. Calculer $\cos\widehat{EDF}$.
5. Calculer $\overrightarrow{AC} \cdot \overrightarrow{DE}$. Les droites $(AC)$ et $(DE)$ sont-elles perpendiculaires ?

??? success "Correction"
    **Partie 1**

    1. **b.** Projection de $C$ sur $(AB)$ : $B$. 2. **b.** $4 + 2 + 9$. 3. **d.** 4. **a.** 5. **a.** $-2 + 3 = 1$. 6. **c.**

    **Partie 2**

    **1.** $C(4\,;\,4)$, $E(2\,;\,0)$, $F(4\,;\,1)$.

    **2.** $\overrightarrow{ED}\begin{pmatrix} -2 \\ 4 \end{pmatrix}$ et $\overrightarrow{EF}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ : $\overrightarrow{ED} \cdot \overrightarrow{EF} = -4 + 4 = 0$. Le triangle $DEF$ est rectangle en $E$.

    **3.** $DE = \sqrt{4 + 16} = 2\sqrt{5}$ ; $EF = \sqrt{4 + 1} = \sqrt{5}$ ; $\overrightarrow{DF}\begin{pmatrix} 4 \\ -3 \end{pmatrix}$, donc $DF = 5$. Pythagore : $20 + 5 = 25$. ✓

    **4.** $\overrightarrow{DE}\begin{pmatrix} 2 \\ -4 \end{pmatrix}$ : $\overrightarrow{DE} \cdot \overrightarrow{DF} = 8 + 12 = 20$, donc $\cos\widehat{EDF} = \dfrac{20}{2\sqrt{5} \times 5} = \dfrac{2}{\sqrt{5}} = \dfrac{2\sqrt{5}}{5}$. *(On retrouve $\frac{DE}{DF}$, le cosinus dans le triangle rectangle.)*

    **5.** $\overrightarrow{AC}\begin{pmatrix} 4 \\ 4 \end{pmatrix}$ : $\overrightarrow{AC} \cdot \overrightarrow{DE} = 8 - 16 = -8 \neq 0$. Les droites ne sont pas perpendiculaires.

---

## Sujet 4

### Partie 1 — Automatismes (QCM)

**Question 1.** $\overrightarrow{AB} + \overrightarrow{BC} - \overrightarrow{AC}$ est égal à :

a. $2\overrightarrow{AC}$ ; b. $\vec{0}$ ; c. $\overrightarrow{CA}$ ; d. $2\overrightarrow{BC}$.

**Question 2.** Dans un triangle de côtés $2$, $3$ et $4$, l'angle opposé au côté $4$ a pour cosinus :

a. $\frac{1}{4}$ ; b. $-\frac{1}{4}$ ; c. $\frac{7}{8}$ ; d. $-\frac{11}{16}$.

**Question 3.** $\frac{10}{\sqrt{200}}$ est égal à :

a. $\frac{1}{2}$ ; b. $\frac{\sqrt{2}}{2}$ ; c. $\frac{1}{20}$ ; d. $\sqrt{2}$.

**Question 4.** Les solutions de l'inéquation $3 - 2x > 7$ sont les réels :

a. $x > -2$ ; b. $x < 2$ ; c. $x < -2$ ; d. $x > 5$.

**Question 5.** Sur $10\,000$ personnes, $3\,\%$ sont gauchères. Cela représente :

a. $30$ personnes ; b. $300$ personnes ; c. $3\,000$ personnes ; d. $333$ personnes.

**Question 6.** Une suite géométrique a pour premier terme $u_0 = 3$ et pour raison $2$. Alors $u_4$ vaut :

a. $24$ ; b. $11$ ; c. $48$ ; d. $96$.

### Partie 2 — Exercice

On donne $A(1\,;\,1)$, $B(5\,;\,3)$ et $C(2\,;\,4)$.

1. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$, puis la mesure de l'angle $\widehat{BAC}$.
2. Calculer $BC$ de deux façons : avec les coordonnées, puis avec la formule d'Al-Kashi.
3. Démontrer que le triangle $ABC$ est rectangle isocèle en $C$.
4. Soit $M(x\,;\,y)$. Montrer que $\overrightarrow{AB} \cdot \overrightarrow{AM} = 10 \iff 2x + y = 8$.
5. Vérifier que $C$ appartient à l'ensemble $\mathcal{D}$ des points $M$ tels que $\overrightarrow{AB} \cdot \overrightarrow{AM} = 10$. Quelle est la nature de $\mathcal{D}$ ?

??? success "Correction"
    **Partie 1**

    1. **b.** Chasles : $\overrightarrow{AC} - \overrightarrow{AC}$. 2. **b.** $\frac{4 + 9 - 16}{12}$. 3. **b.** $\sqrt{200} = 10\sqrt{2}$. 4. **c.** $-2x > 4$. 5. **b.** 6. **c.** $3 \times 2^4$.

    **Partie 2**

    **1.** $\overrightarrow{AB}\begin{pmatrix} 4 \\ 2 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$ : produit $4 + 6 = 10$ ; $AB = \sqrt{20}$, $AC = \sqrt{10}$. $\cos\widehat{BAC} = \dfrac{10}{\sqrt{200}} = \dfrac{\sqrt{2}}{2}$, donc $\widehat{BAC} = \frac{\pi}{4}$.

    **2.** $\overrightarrow{BC}\begin{pmatrix} -3 \\ 1 \end{pmatrix}$ : $BC = \sqrt{10}$. Avec Al-Kashi : $BC^2 = 20 + 10 - 2 \times 10 = 10$ (car $2 \times AB \times AC \times \cos\widehat{A} = 2\,\overrightarrow{AB} \cdot \overrightarrow{AC}$).

    **3.** $AC = BC = \sqrt{10}$ : le triangle est isocèle en $C$. $\overrightarrow{CA}\begin{pmatrix} -1 \\ -3 \end{pmatrix}$, $\overrightarrow{CB}\begin{pmatrix} 3 \\ -1 \end{pmatrix}$ : $\overrightarrow{CA} \cdot \overrightarrow{CB} = -3 + 3 = 0$. Il est rectangle en $C$.

    **4.** $\overrightarrow{AM}\begin{pmatrix} x - 1 \\ y - 1 \end{pmatrix}$ : $\overrightarrow{AB} \cdot \overrightarrow{AM} = 4(x - 1) + 2(y - 1) = 4x + 2y - 6$. Donc $\overrightarrow{AB} \cdot \overrightarrow{AM} = 10 \iff 4x + 2y = 16 \iff 2x + y = 8$.

    **5.** $2 \times 2 + 4 = 8$ : $C \in \mathcal{D}$. $\mathcal{D}$ est une droite ; comme $\overrightarrow{AB} \cdot \overrightarrow{AM} = \overrightarrow{AB} \cdot \overrightarrow{AC}$ équivaut à $\overrightarrow{AB} \cdot \overrightarrow{CM} = 0$, c'est la **droite perpendiculaire à $(AB)$ passant par $C$**. C'est la hauteur issue de $C$ du triangle $ABC$ (et aussi la médiatrice de $[AB]$, puisque le triangle est isocèle en $C$).
