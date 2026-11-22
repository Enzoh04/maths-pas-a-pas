# Sujets type bac — Représentations paramétriques et équations cartésiennes

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets dans l'esprit de l'épreuve : c'est le format le plus fréquent de l'exercice de géométrie au bac, qui mélange les chapitres 10, 11 et 12. Dans tous les sujets, le repère est **orthonormé**.

| Sujet | Thème | Durée conseillée |
|---|---|---|
| 1 | Plan, projeté et volume d'un tétraèdre | 50 min |
| 2 | Section d'un cube par un plan | 45 min |
| 3 | QCM | 25 min |
| 4 | Distance entre deux droites non coplanaires | 50 min |

## Sujet 1 — Volume d'un tétraèdre

On considère les points $A(1, 0, 2)$, $B(2, 1, 0)$, $C(0, 1, 1)$ et $D(4, 5, 7)$.

1. Montrer que les points $A$, $B$, $C$ ne sont pas alignés.
2. a. Montrer que le vecteur $\vec{n}(1, 3, 2)$ est normal au plan $(ABC)$.  
   b. En déduire une équation cartésienne du plan $(ABC)$.
3. a. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AC}$, puis $\cos\widehat{BAC}$.  
   b. En déduire $\sin\widehat{BAC}$, puis montrer que l'aire du triangle $ABC$ vaut $\dfrac{\sqrt{14}}{2}$.
4. Soit $\Delta$ la droite passant par $D$ et orthogonale au plan $(ABC)$.  
   a. Donner une représentation paramétrique de $\Delta$.  
   b. Déterminer les coordonnées du point $H$, intersection de $\Delta$ et du plan $(ABC)$.
5. a. Calculer la distance $DH$. Vérifier le résultat avec la formule de la distance d'un point à un plan.  
   b. En déduire le volume du tétraèdre $ABCD$.

??? success "Correction"
    **1.** $\overrightarrow{AB}(1, 1, -2)$ et $\overrightarrow{AC}(-1, 1, -1)$. Les deux premières coordonnées donneraient $k = -1$ et $k = 1$ : ces vecteurs ne sont pas colinéaires, donc les points ne sont pas alignés.

    **2. a.** $\vec{n} \cdot \overrightarrow{AB} = 1 + 3 - 4 = 0$ et $\vec{n} \cdot \overrightarrow{AC} = -1 + 3 - 2 = 0$ : $\vec{n}$ est orthogonal à deux vecteurs non colinéaires du plan.

    **b.** $x + 3y + 2z + d = 0$ avec $A$ : $1 + 0 + 4 + d = 0$, donc $(ABC)$ : $x + 3y + 2z - 5 = 0$. Vérification : $B$ donne $2 + 3 + 0 - 5 = 0$, $C$ donne $0 + 3 + 2 - 5 = 0$.

    **3. a.** $\overrightarrow{AB} \cdot \overrightarrow{AC} = -1 + 1 + 2 = 2$, $AB = \sqrt{6}$, $AC = \sqrt{3}$. Donc $\cos\widehat{BAC} = \dfrac{2}{\sqrt{18}} = \dfrac{2}{3\sqrt{2}} = \dfrac{\sqrt{2}}{3}$.

    **b.** L'angle est entre $0$ et $\pi$, donc son sinus est positif : $\sin\widehat{BAC} = \sqrt{1 - \dfrac{2}{9}} = \dfrac{\sqrt{7}}{3}$. L'aire vaut
    $$\frac{1}{2} \times AB \times AC \times \sin\widehat{BAC} = \frac{1}{2} \times \sqrt{6} \times \sqrt{3} \times \frac{\sqrt{7}}{3} = \frac{\sqrt{126}}{6} = \frac{3\sqrt{14}}{6} = \frac{\sqrt{14}}{2}.$$

    **4. a.** $\Delta$ est dirigée par $\vec{n}$ : $x = 4 + t$, $y = 5 + 3t$, $z = 7 + 2t$, $t \in \mathbb{R}$.

    **b.** $(4 + t) + 3(5 + 3t) + 2(7 + 2t) - 5 = 0$, soit $28 + 14t = 0$, donc $t = -2$ et $H(2, -1, 3)$.

    **5. a.** $\overrightarrow{DH} = -2\vec{n}$, donc $DH = 2\sqrt{14}$. Avec la formule : $\dfrac{|4 + 15 + 14 - 5|}{\sqrt{1 + 9 + 4}} = \dfrac{28}{\sqrt{14}} = 2\sqrt{14}$.

    **b.** $H$ est le projeté orthogonal de $D$ sur le plan de la base, donc $DH$ est la hauteur :
    $$V = \frac{1}{3} \times \frac{\sqrt{14}}{2} \times 2\sqrt{14} = \frac{14}{3}.$$

---

## Sujet 2 — Section d'un cube

![Le cube ABCDEFGH](img/cube.png){ width="40%" }

$ABCDEFGH$ est un cube d'arête $1$, muni du repère $\left(A \,;\, \overrightarrow{AB}, \overrightarrow{AD}, \overrightarrow{AE}\right)$. On note $I$ le milieu de $[BF]$ et $J$ le milieu de $[DH]$.

1. Donner les coordonnées des points $C$, $E$, $I$ et $J$.
2. Montrer que $\vec{n}(1, 1, 2)$ est normal au plan $(EIJ)$, et en déduire une équation de ce plan.
3. a. Montrer que le point $C$ appartient au plan $(EIJ)$.  
   b. Montrer que le quadrilatère $EICJ$ est un losange. Est-ce un carré ?
4. Donner une représentation paramétrique de la droite $(AG)$, puis déterminer son point d'intersection $K$ avec le plan $(EIJ)$. Que représente $K$ pour le losange ?
5. Calculer la distance du point $A$ au plan $(EIJ)$.
6. Calculer le volume de la pyramide de sommet $A$ et de base $EICJ$.

??? success "Correction"
    **1.** $C(1, 1, 0)$, $E(0, 0, 1)$, $I\left(1, 0, \frac{1}{2}\right)$, $J\left(0, 1, \frac{1}{2}\right)$.

    **2.** $\overrightarrow{EI}\left(1, 0, -\frac{1}{2}\right)$ et $\overrightarrow{EJ}\left(0, 1, -\frac{1}{2}\right)$ ne sont pas colinéaires. $\vec{n} \cdot \overrightarrow{EI} = 1 - 1 = 0$ et $\vec{n} \cdot \overrightarrow{EJ} = 1 - 1 = 0$. Équation $x + y + 2z + d = 0$, avec $E$ : $2 + d = 0$. Donc $(EIJ)$ : $x + y + 2z - 2 = 0$.

    **3. a.** $1 + 1 + 0 - 2 = 0$ : $C \in (EIJ)$.

    **b.** $\overrightarrow{JC}\left(1, 0, -\frac{1}{2}\right) = \overrightarrow{EI}$ : $EICJ$ est un parallélogramme. De plus $EI = \sqrt{1 + \frac{1}{4}} = \frac{\sqrt{5}}{2}$ et $\overrightarrow{IC}\left(0, 1, -\frac{1}{2}\right)$ donne $IC = \frac{\sqrt{5}}{2}$ : deux côtés consécutifs égaux, c'est un **losange**. Ce n'est pas un carré : $\overrightarrow{EI} \cdot \overrightarrow{IC} = 0 + 0 + \frac{1}{4} \neq 0$.

    **4.** $(AG)$ : $x = t$, $y = t$, $z = t$. En remplaçant : $4t - 2 = 0$, donc $t = \frac{1}{2}$ et $K\left(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right)$. C'est le milieu de $[EC]$ (et de $[IJ]$) : le **centre du losange**, qui est aussi le centre du cube.

    **5.** $d(A, (EIJ)) = \dfrac{|0 + 0 + 0 - 2|}{\sqrt{1 + 1 + 4}} = \dfrac{2}{\sqrt{6}} = \dfrac{\sqrt{6}}{3}$.

    **6.** Aire du losange : $\dfrac{EC \times IJ}{2} = \dfrac{\sqrt{3} \times \sqrt{2}}{2} = \dfrac{\sqrt{6}}{2}$. Volume : $\dfrac{1}{3} \times \dfrac{\sqrt{6}}{2} \times \dfrac{\sqrt{6}}{3} = \dfrac{1}{3}$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Justifier.

**Question 1.** Un point de la droite $x = 1 + 2t$, $y = -t$, $z = 3$ ($t \in \mathbb{R}$) est :

a. $(3, 1, 3)$ ; b. $(5, -2, 3)$ ; c. $(1, 0, 0)$ ; d. $(3, -1, 4)$.

**Question 2.** Une équation du plan passant par $(1, 1, 1)$ et de vecteur normal $(1, -2, 3)$ est :

a. $x - 2y + 3z - 2 = 0$ ; b. $x - 2y + 3z + 2 = 0$ ; c. $x + y + z - 3 = 0$ ; d. $3x - 2y + z - 2 = 0$.

**Question 3.** La droite $x = t$, $y = 1 + t$, $z = 2 - t$ et le plan $x + y + 2z - 5 = 0$ sont :

a. sécants ; b. strictement parallèles ; c. tels que la droite est contenue dans le plan ; d. orthogonaux.

**Question 4.** Les plans $2x - y + z = 1$ et $-4x + 2y - 2z + 3 = 0$ sont :

a. sécants ; b. perpendiculaires ; c. strictement parallèles ; d. confondus.

**Question 5.** La distance de l'origine $O$ au plan $x + 2y + 2z - 6 = 0$ vaut :

a. $6$ ; b. $3$ ; c. $2$ ; d. $\dfrac{6}{5}$.

??? success "Correction"
    **Question 1 : b.** Pour $t = 2$. (Pour a., $x = 3$ impose $t = 1$, et $y = -1 \neq 1$.)

    **Question 2 : a.** Le vecteur normal impose a. ou b. ; le point $(1, 1, 1)$ donne $1 - 2 + 3 - 2 = 0$. (c. contient le point, mais n'a pas le bon vecteur normal.)

    **Question 3 : c.** $t + (1 + t) + 2(2 - t) - 5 = 0$ se réduit à $0 = 0$.

    **Question 4 : c.** Les vecteurs normaux $(2, -1, 1)$ et $(-4, 2, -2)$ sont colinéaires. La seconde équation s'écrit $2x - y + z = \frac{3}{2}$, incompatible avec la première : aucun point commun.

    **Question 5 : c.** $\dfrac{|-6|}{\sqrt{1 + 4 + 4}} = \dfrac{6}{3} = 2$.

---

## Sujet 4 — Distance entre deux droites non coplanaires

On considère les droites
$$d_1 : \begin{cases} x = 1 + t \\ y = 2t \\ z = 3 - t \end{cases} \ (t \in \mathbb{R}) \qquad \text{et} \qquad d_2 : \begin{cases} x = 2 + s \\ y = 1 - s \\ z = s \end{cases} \ (s \in \mathbb{R}).$$

1. Montrer que $d_1$ et $d_2$ sont non coplanaires.
2. Montrer que le vecteur $\vec{n}(1, -2, -3)$ est orthogonal à un vecteur directeur de $d_1$ et à un vecteur directeur de $d_2$.
3. Soit $\mathcal{P}$ le plan contenant $d_1$ et de vecteur normal $\vec{n}$. Montrer qu'il a pour équation $x - 2y - 3z + 8 = 0$.
4. Montrer que $d_2$ est parallèle à $\mathcal{P}$, puis calculer la distance d'un point de $d_2$ au plan $\mathcal{P}$.
5. On note $M_1$ le point de $d_1$ de paramètre $t$ et $M_2$ le point de $d_2$ de paramètre $s$.  
   a. Montrer que $(M_1M_2)$ est orthogonale à $d_1$ et à $d_2$ si et seulement si $s + 3t = 3$ et $3s + 2t = 3$.  
   b. En déduire les points $M_1$ et $M_2$ correspondants et la longueur $M_1M_2$.
6. Montrer que pour tout point $M$ de $d_1$ et tout point $N$ de $d_2$, $MN \geq M_1M_2$.

??? success "Correction"
    **1.** $\vec{u}_1(1, 2, -1)$ et $\vec{u}_2(1, -1, 1)$ ne sont pas colinéaires. Le système $1 + t = 2 + s$, $2t = 1 - s$, $3 - t = s$ : la troisième donne $s = 3 - t$, la première $1 + t = 5 - t$, donc $t = 2$ et $s = 1$. Mais la deuxième devient $4 = 0$ : impossible. Les droites ne sont ni parallèles ni sécantes : elles sont non coplanaires.

    **2.** $\vec{n} \cdot \vec{u}_1 = 1 - 4 + 3 = 0$ et $\vec{n} \cdot \vec{u}_2 = 1 + 2 - 3 = 0$.

    **3.** Le plan passe par $A_1(1, 0, 3)$ : $x - 2y - 3z + d = 0$ avec $1 - 9 + d = 0$, soit $d = 8$. Il contient bien $d_1$ : $(1 + t) - 4t - 3(3 - t) + 8 = 0$ pour tout $t$. (On pouvait aussi dire : $\vec{u}_1 \cdot \vec{n} = 0$ et $A_1 \in \mathcal{P}$.)

    **4.** $\vec{u}_2 \cdot \vec{n} = 0$ : $d_2$ est parallèle à $\mathcal{P}$. Tous ses points sont donc à la même distance de $\mathcal{P}$ ; avec $A_2(2, 1, 0)$ :
    $$d(A_2, \mathcal{P}) = \frac{|2 - 2 - 0 + 8|}{\sqrt{1 + 4 + 9}} = \frac{8}{\sqrt{14}} = \frac{4\sqrt{14}}{7}.$$
    (Pour un point quelconque de $d_2$, on trouve aussi $|8|$ au numérateur : $(2 + s) - 2(1 - s) - 3s + 8 = 8$.)

    **5. a.** $\overrightarrow{M_1M_2}(1 + s - t,\; 1 - s - 2t,\; s - 3 + t)$. On calcule :

    - $\overrightarrow{M_1M_2} \cdot \vec{u}_1 = (1 + s - t) + 2(1 - s - 2t) - (s - 3 + t) = 6 - 2s - 6t$ ;
    - $\overrightarrow{M_1M_2} \cdot \vec{u}_2 = (1 + s - t) - (1 - s - 2t) + (s - 3 + t) = 3s + 2t - 3$.

    Les deux sont nuls si et seulement si $s + 3t = 3$ et $3s + 2t = 3$.

    **b.** La première donne $s = 3 - 3t$ ; la seconde devient $9 - 9t + 2t = 3$, donc $t = \frac{6}{7}$ et $s = \frac{3}{7}$. Alors
    $$M_1\left(\frac{13}{7}, \frac{12}{7}, \frac{15}{7}\right), \quad M_2\left(\frac{17}{7}, \frac{4}{7}, \frac{3}{7}\right), \quad \overrightarrow{M_1M_2}\left(\frac{4}{7}, -\frac{8}{7}, -\frac{12}{7}\right) = \frac{4}{7}\vec{n}.$$
    Donc $M_1M_2 = \frac{4}{7}\sqrt{14} = \frac{4\sqrt{14}}{7}$ : on retrouve la distance de la question 4.

    **6.** Soit $M \in d_1$ et $N \in d_2$. Le point $M$ est dans $\mathcal{P}$ (qui contient $d_1$), et la distance de $N$ à $\mathcal{P}$ est la plus petite distance entre $N$ et un point de $\mathcal{P}$ (chapitre 11). Donc $MN \geq d(N, \mathcal{P}) = \frac{4\sqrt{14}}{7} = M_1M_2$.

    *La droite $(M_1M_2)$ est la **perpendiculaire commune** aux deux droites, et $M_1M_2$ est la distance entre $d_1$ et $d_2$.*
