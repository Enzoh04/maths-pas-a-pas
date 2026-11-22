# Méthodes — Calcul vectoriel et produit scalaire

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Choisir la bonne formule pour calculer un produit scalaire

**Les étapes**

1. **On a des coordonnées** (repère orthonormé) : $\vec{u} \cdot \vec{v} = xx' + yy'$.
2. **On a deux longueurs et l'angle entre elles** : $\vec{u} \cdot \vec{v} = \|\vec{u}\|\,\|\vec{v}\|\cos\theta$.
3. **On voit un angle droit** (hauteur, carré, rectangle) : on projette orthogonalement, $\overrightarrow{AB} \cdot \overrightarrow{AC} = \pm AB \times AH$.
4. **On a seulement des longueurs** : $\vec{u} \cdot \vec{v} = \frac{1}{2}\left(\|\vec{u}\|^2 + \|\vec{v}\|^2 - \|\vec{u} - \vec{v}\|^2\right)$.
5. **Les vecteurs ne partent pas du même point** : on utilise la relation de Chasles pour les décomposer, puis la bilinéarité.

**Exemple.** $ABCD$ est un carré de côté $4$ et $I$ le milieu de $[CD]$. Calculer $\overrightarrow{AB} \cdot \overrightarrow{AI}$.

Le projeté orthogonal de $I$ sur $(AB)$ est le milieu $K$ de $[AB]$, et $\overrightarrow{AK}$ a le même sens que $\overrightarrow{AB}$ : $\overrightarrow{AB} \cdot \overrightarrow{AI} = AB \times AK = 4 \times 2 = 8$.

*Vérification en coordonnées* : avec $A(0\,;\,0)$, $B(4\,;\,0)$, $I(2\,;\,4)$ : $4 \times 2 + 0 \times 4 = 8$.

---

## Méthode 2 — Démontrer que deux droites sont perpendiculaires ou parallèles

**Les étapes**

1. Choisir un vecteur directeur de chaque droite : $\overrightarrow{AB}$ et $\overrightarrow{CD}$.
2. **Perpendiculaires** : montrer que $\overrightarrow{AB} \cdot \overrightarrow{CD} = 0$.
3. **Parallèles** (ou points alignés) : montrer que $\det\left(\overrightarrow{AB}, \overrightarrow{CD}\right) = 0$.
4. Sans repère, décomposer les vecteurs avec la relation de Chasles sur des vecteurs dont on connaît les produits scalaires.

**Exemple.** $A(1\,;\,2)$, $B(4\,;\,3)$, $C(2\,;\,-1)$, $D(1\,;\,2)$. On a $\overrightarrow{AB}\begin{pmatrix} 3 \\ 1 \end{pmatrix}$ et $\overrightarrow{CD}\begin{pmatrix} -1 \\ 3 \end{pmatrix}$ : $\overrightarrow{AB} \cdot \overrightarrow{CD} = -3 + 3 = 0$. Les droites $(AB)$ et $(CD)$ sont perpendiculaires.

---

## Méthode 3 — Calculer une longueur ou un angle avec Al-Kashi

**Les étapes**

1. Repérer ce que l'on connaît : **deux côtés et l'angle compris** (on cherche le troisième côté), ou **les trois côtés** (on cherche un angle).
2. Écrire la formule avec, à gauche, le **côté opposé à l'angle** : $a^2 = b^2 + c^2 - 2bc\cos\widehat{A}$.
3. Pour un angle : $\cos\widehat{A} = \dfrac{b^2 + c^2 - a^2}{2bc}$, puis reconnaître une valeur remarquable.

**Exemple.** Un triangle a pour côtés $5$, $7$ et $8$. Son angle opposé au côté $7$ vérifie
$$\cos\theta = \frac{5^2 + 8^2 - 7^2}{2 \times 5 \times 8} = \frac{25 + 64 - 49}{80} = \frac{40}{80} = \frac{1}{2}, \qquad \text{donc } \theta = \frac{\pi}{3}.$$

---

## Méthode 4 — Calculer un angle avec les coordonnées

**Les étapes**

1. Calculer le produit scalaire avec les coordonnées : $\vec{u} \cdot \vec{v} = xx' + yy'$.
2. Calculer les normes $\|\vec{u}\|$ et $\|\vec{v}\|$.
3. En déduire $\cos\theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\|\,\|\vec{v}\|}$, puis $\theta \in [0\,;\,\pi]$.

**Exemple.** $\vec{u}\begin{pmatrix} 1 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 2 \\ -1 \end{pmatrix}$ : $\vec{u} \cdot \vec{v} = 2 - 3 = -1$, $\|\vec{u}\| = \sqrt{10}$, $\|\vec{v}\| = \sqrt{5}$. Donc
$$\cos\theta = \frac{-1}{\sqrt{50}} = -\frac{1}{5\sqrt{2}} = -\frac{\sqrt{2}}{10}.$$
L'angle est obtus (environ $98°$, à la calculatrice).

---

## Méthode 5 — Déterminer un ensemble de points

**Les étapes**

1. **$\overrightarrow{MA} \cdot \overrightarrow{MB} = 0$** : c'est le cercle de diamètre $[AB]$ (à citer directement).
2. **$\overrightarrow{MA} \cdot \overrightarrow{MB} = k$** : introduire le milieu $I$ de $[AB]$ et utiliser $\overrightarrow{MA} \cdot \overrightarrow{MB} = MI^2 - \frac{AB^2}{4}$. On obtient $MI^2 = k + \frac{AB^2}{4}$ : un cercle de centre $I$ si ce nombre est positif, le point $I$ s'il est nul, l'ensemble vide s'il est négatif.
3. **$\overrightarrow{AB} \cdot \overrightarrow{AM} = k$** : avec $H$ le projeté de $M$ sur $(AB)$, on a $\overrightarrow{AB} \cdot \overrightarrow{AH} = k$, ce qui fixe $H$ ; l'ensemble est la **droite perpendiculaire à $(AB)$** passant par $H$.
4. En repère, on peut aussi poser $M(x\,;\,y)$ et traduire la condition en équation.

**Exemple.** $AB = 6$. Ensemble des points $M$ tels que $\overrightarrow{MA} \cdot \overrightarrow{MB} = 16$ : $MI^2 = 16 + \frac{36}{4} = 25$, donc $MI = 5$. C'est le cercle de centre $I$ (milieu de $[AB]$) et de rayon $5$.
