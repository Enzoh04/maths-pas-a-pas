# Cours — Vecteurs, droites et plans de l'espace

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

Dans tout le chapitre, on illustre les notions sur le **cube $ABCDEFGH$** ci-dessous, où $ABCD$ est la face du bas et $E$, $F$, $G$, $H$ sont respectivement au-dessus de $A$, $B$, $C$, $D$.

![Le cube ABCDEFGH](img/cube.png){ width="45%" }

---

## 1. Positions relatives de droites et de plans

### 1.1 Les règles de base

!!! propriete "Règles d'incidence"
    - Par deux points distincts passe une **unique droite**.
    - Par trois points non alignés passe un **unique plan**.
    - Si deux points distincts $A$ et $B$ appartiennent à un plan, la droite $(AB)$ est contenue dans ce plan.
    - Dans chaque plan de l'espace, tous les résultats de la géométrie plane s'appliquent.

??? admis "Pourquoi ces règles sont admises"
    Ces règles ne se démontrent pas : ce sont des **axiomes**, c'est-à-dire les points de départ de la géométrie de l'espace. On les accepte parce qu'elles décrivent fidèlement l'espace qui nous entoure. Le mathématicien David Hilbert a donné en 1899 une liste complète d'axiomes pour la géométrie d'Euclide.

    Dans le supérieur, on adopte souvent un autre point de départ : on **définit** l'espace comme l'ensemble des triplets $(x, y, z)$ de réels, et les droites et les plans par des équations. Ces règles deviennent alors des théorèmes d'**algèbre linéaire** (L1).

### 1.2 Deux droites

Deux droites de l'espace sont :

- soit **coplanaires** (contenues dans un même plan) : elles sont alors **sécantes** (un point commun) ou **parallèles** (strictement parallèles ou confondues) ;
- soit **non coplanaires** : elles n'ont aucun point commun, sans être parallèles.

**Dans le cube.** $(AB)$ et $(HG)$ sont parallèles ; $(AC)$ et $(BD)$ sont sécantes ; $(AB)$ et $(CG)$ sont non coplanaires.

!!! warning "Une nouveauté par rapport au plan"
    Dans l'espace, deux droites sans point commun **ne sont pas forcément parallèles** : $(AB)$ et $(CG)$ ne se coupent pas, et pourtant elles ne sont pas parallèles.

### 1.3 Une droite et un plan, deux plans

Une droite $d$ et un plan $\mathcal{P}$ sont soit **sécants** (un seul point commun), soit **parallèles** ($d$ contenue dans $\mathcal{P}$, ou sans point commun avec lui).

Deux plans sont soit **sécants** (leur intersection est une droite), soit **parallèles** (confondus, ou sans point commun).

**Dans le cube.** $(EG)$ est parallèle au plan $(ABC)$ ; les plans $(ABF)$ et $(DCG)$ sont parallèles ; les plans $(ABC)$ et $(ABF)$ sont sécants selon la droite $(AB)$.

!!! propriete "Parallélisme"
    - Si une droite $d$ est parallèle à une droite $d'$ contenue dans un plan $\mathcal{P}$, alors $d$ est parallèle à $\mathcal{P}$.
    - Si deux plans sont parallèles, tout plan qui coupe l'un coupe l'autre, et les deux droites d'intersection sont parallèles.

!!! theoreme "Théorème du toit"
    Soit $d_1$ et $d_2$ deux droites parallèles, $\mathcal{P}_1$ un plan contenant $d_1$ et $\mathcal{P}_2$ un plan contenant $d_2$. Si $\mathcal{P}_1$ et $\mathcal{P}_2$ sont sécants, leur droite d'intersection $\Delta$ est parallèle à $d_1$ et à $d_2$.

*Image : les deux pans d'un toit contiennent des droites parallèles au faîtage, et se coupent selon le faîtage.* La démonstration, vectorielle, est donnée au § 3.

---

## 2. Vecteurs de l'espace

### 2.1 Définitions et opérations

La notion de vecteur s'étend à l'espace : un vecteur non nul est défini par une **direction**, un **sens** et une **longueur** (sa **norme**). Le vecteur $\overrightarrow{AB}$ est associé à la **translation** qui envoie $A$ sur $B$.

Toutes les règles de calcul du plan restent valables :

- **relation de Chasles** : $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ ;
- **règle du parallélogramme** : $\overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}$ si et seulement si $ABCD$ est un parallélogramme ;
- produit d'un vecteur par un réel, et propriétés habituelles du calcul.

**Dans le cube.** $\overrightarrow{AB} + \overrightarrow{AD} + \overrightarrow{AE} = \overrightarrow{AC} + \overrightarrow{CG} = \overrightarrow{AG}$.

!!! definition "Combinaison linéaire"
    Une **combinaison linéaire** des vecteurs $\vec{u}$, $\vec{v}$, $\vec{w}$ est un vecteur de la forme $a\vec{u} + b\vec{v} + c\vec{w}$, où $a$, $b$, $c$ sont des réels.

### 2.2 Colinéarité

!!! definition "Vecteurs colinéaires"
    Deux vecteurs $\vec{u}$ et $\vec{v}$ sont **colinéaires** si l'un est le produit de l'autre par un réel : $\vec{v} = k\vec{u}$ ou $\vec{u} = k\vec{v}$. Le vecteur nul est colinéaire à tout vecteur.

!!! propriete "Alignement et parallélisme"
    - Trois points $A$, $B$, $C$ sont **alignés** si et seulement si $\overrightarrow{AB}$ et $\overrightarrow{AC}$ sont colinéaires.
    - Deux droites $(AB)$ et $(CD)$ sont **parallèles** si et seulement si $\overrightarrow{AB}$ et $\overrightarrow{CD}$ sont colinéaires.

---

## 3. Caractérisation vectorielle des droites et des plans

### 3.1 Droites

!!! definition "Droite définie par un point et un vecteur"
    Soit $A$ un point et $\vec{u}$ un vecteur non nul. La **droite $d$ passant par $A$ et de vecteur directeur $\vec{u}$** est l'ensemble des points $M$ tels que $\overrightarrow{AM} = t\vec{u}$, avec $t \in \mathbb{R}$.

Deux droites sont parallèles si et seulement si leurs vecteurs directeurs sont colinéaires.

### 3.2 Plans

!!! definition "Plan défini par un point et deux vecteurs"
    Soit $A$ un point, et $\vec{u}$, $\vec{v}$ deux vecteurs **non colinéaires**. Le **plan $\mathcal{P}$ passant par $A$ et dirigé par $\vec{u}$ et $\vec{v}$** est l'ensemble des points $M$ tels que

    $$\overrightarrow{AM} = s\vec{u} + t\vec{v}, \qquad s, t \in \mathbb{R}.$$

    Le couple $(\vec{u}, \vec{v})$ est un **couple de vecteurs directeurs** de $\mathcal{P}$. L'ensemble des vecteurs $s\vec{u} + t\vec{v}$ s'appelle la **direction** du plan.

**Exemple.** Le plan $(ABC)$ passe par $A$ et est dirigé par $\overrightarrow{AB}$ et $\overrightarrow{AC}$.

!!! propriete "Parallélisme et vecteurs"
    - Une droite de vecteur directeur $\vec{w}$ est parallèle au plan dirigé par $(\vec{u}, \vec{v})$ si et seulement si $\vec{w}$ est une combinaison linéaire de $\vec{u}$ et $\vec{v}$.
    - Deux plans sont parallèles si et seulement s'ils ont la même direction, c'est-à-dire si deux vecteurs directeurs de l'un sont des combinaisons linéaires des vecteurs directeurs de l'autre.

### 3.3 Démonstration du théorème du toit

??? demoplus "Démonstration vectorielle du théorème du toit — pour aller plus loin"
    Soit $\vec{u}$ un vecteur directeur commun à $d_1$ et $d_2$, et $\vec{w}$ un vecteur directeur de $\Delta = \mathcal{P}_1 \cap \mathcal{P}_2$. Soit $M$ un point de $\Delta$.

    - $d_1 \subset \mathcal{P}_1$, donc $\vec{u}$ est dans la direction de $\mathcal{P}_1$. De même, $\vec{u}$ est dans la direction de $\mathcal{P}_2$.
    - $\Delta$ est contenue dans les deux plans, donc $\vec{w}$ est dans la direction de $\mathcal{P}_1$ et dans celle de $\mathcal{P}_2$.

    Supposons $\vec{u}$ et $\vec{w}$ **non colinéaires**. Alors ils dirigent chacun des deux plans, qui passent tous deux par $M$ : $\mathcal{P}_1$ et $\mathcal{P}_2$ sont égaux au plan passant par $M$ dirigé par $(\vec{u}, \vec{w})$. Ils seraient donc confondus, ce qui contredit le fait qu'ils sont sécants. Donc $\vec{w}$ est colinéaire à $\vec{u}$ : $\Delta$ est parallèle à $d_1$ et à $d_2$.

---

## 4. Vecteurs coplanaires

!!! definition "Vecteurs coplanaires"
    Trois vecteurs $\vec{u}$, $\vec{v}$, $\vec{w}$ sont **coplanaires** si, pour un point $O$ quelconque, les points $A$, $B$, $C$ définis par $\overrightarrow{OA} = \vec{u}$, $\overrightarrow{OB} = \vec{v}$, $\overrightarrow{OC} = \vec{w}$ sont dans un même plan avec $O$.

!!! theoreme "Caractérisation"
    Soit $\vec{u}$ et $\vec{v}$ deux vecteurs non colinéaires. Les vecteurs $\vec{u}$, $\vec{v}$, $\vec{w}$ sont coplanaires si et seulement s'il existe des réels $a$ et $b$ tels que

    $$\vec{w} = a\vec{u} + b\vec{v}.$$

??? demoplus "Démonstration — pour aller plus loin"
    Soit $O$ un point et $A$, $B$, $C$ définis comme ci-dessus. Comme $\vec{u}$ et $\vec{v}$ ne sont pas colinéaires, les points $O$, $A$, $B$ ne sont pas alignés : ils définissent un unique plan, le plan passant par $O$ et dirigé par $(\vec{u}, \vec{v})$. D'après le § 3.2 :

    $$C \in (OAB) \iff \overrightarrow{OC} = a\vec{u} + b\vec{v} \text{ pour des réels } a, b \iff \vec{w} = a\vec{u} + b\vec{v}.$$

**Exemple.** Dans le cube, $\overrightarrow{AG} = \overrightarrow{AC} + \overrightarrow{AE}$, donc $\overrightarrow{AC}$, $\overrightarrow{AE}$ et $\overrightarrow{AG}$ sont coplanaires : les points $A$, $C$, $E$, $G$ sont dans un même plan (le rectangle $ACGE$).

!!! propriete "Points coplanaires"
    Quatre points $A$, $B$, $C$, $D$ (avec $A$, $B$, $C$ non alignés) sont **coplanaires** si et seulement si $\overrightarrow{AD}$ est une combinaison linéaire de $\overrightarrow{AB}$ et $\overrightarrow{AC}$.

---

## 5. Bases et repères de l'espace

!!! definition "Base et repère"
    - Trois vecteurs **non coplanaires** $\vec{i}$, $\vec{j}$, $\vec{k}$ forment une **base** de l'espace.
    - Un **repère** $(O \,;\, \vec{i}, \vec{j}, \vec{k})$ est formé d'un point $O$ (l'origine) et d'une base.

!!! theoreme "Décomposition dans une base"
    Soit $(\vec{i}, \vec{j}, \vec{k})$ une base. Pour tout vecteur $\vec{w}$, il existe un **unique** triplet de réels $(x, y, z)$ tel que

    $$\vec{w} = x\vec{i} + y\vec{j} + z\vec{k}.$$

    Ce sont les **coordonnées** de $\vec{w}$ dans la base. Les coordonnées d'un point $M$ dans le repère $(O \,;\, \vec{i}, \vec{j}, \vec{k})$ sont celles du vecteur $\overrightarrow{OM}$.

??? demoplus "Démonstration — pour aller plus loin"
    **Existence.** Soit $M$ le point tel que $\overrightarrow{OM} = \vec{w}$, et $\mathcal{P}$ le plan passant par $O$ dirigé par $(\vec{i}, \vec{j})$. La droite passant par $M$ et dirigée par $\vec{k}$ n'est pas parallèle à $\mathcal{P}$, car $\vec{k}$ n'est pas combinaison linéaire de $\vec{i}$ et $\vec{j}$ (les trois vecteurs ne sont pas coplanaires). Elle coupe donc $\mathcal{P}$ en un point $N$ (règle d'incidence admise). Alors $\overrightarrow{ON} = x\vec{i} + y\vec{j}$ (car $N \in \mathcal{P}$) et $\overrightarrow{NM} = z\vec{k}$ (car $M$ et $N$ sont sur une droite dirigée par $\vec{k}$). Par Chasles, $\vec{w} = \overrightarrow{ON} + \overrightarrow{NM} = x\vec{i} + y\vec{j} + z\vec{k}$.

    **Unicité.** Si $x\vec{i} + y\vec{j} + z\vec{k} = x'\vec{i} + y'\vec{j} + z'\vec{k}$, alors $(z - z')\vec{k} = (x' - x)\vec{i} + (y' - y)\vec{j}$. Si $z \neq z'$, on pourrait diviser par $z - z'$ et $\vec{k}$ serait combinaison linéaire de $\vec{i}$ et $\vec{j}$ : contradiction. Donc $z = z'$, puis $(x' - x)\vec{i} + (y' - y)\vec{j} = \vec{0}$. Comme $\vec{i}$ et $\vec{j}$ ne sont pas colinéaires, $x = x'$ et $y = y'$ (sinon l'un serait multiple de l'autre).

**Dans le cube**, avec le repère $\left(A \,;\, \overrightarrow{AB}, \overrightarrow{AD}, \overrightarrow{AE}\right)$ :

| Point | $A$ | $B$ | $C$ | $D$ | $E$ | $F$ | $G$ | $H$ |
|---|---|---|---|---|---|---|---|---|
| Coordonnées | $(0, 0, 0)$ | $(1, 0, 0)$ | $(1, 1, 0)$ | $(0, 1, 0)$ | $(0, 0, 1)$ | $(1, 0, 1)$ | $(1, 1, 1)$ | $(0, 1, 1)$ |

!!! propriete "Calculs en coordonnées"
    Dans un repère, avec $A(x_A, y_A, z_A)$ et $B(x_B, y_B, z_B)$ :

    - $\overrightarrow{AB}$ a pour coordonnées $(x_B - x_A,\; y_B - y_A,\; z_B - z_A)$ ;
    - le milieu de $[AB]$ a pour coordonnées $\left(\frac{x_A + x_B}{2},\; \frac{y_A + y_B}{2},\; \frac{z_A + z_B}{2}\right)$ ;
    - les coordonnées de $\vec{u} + \vec{v}$ et de $k\vec{u}$ s'obtiennent coordonnée par coordonnée.

??? demoplus "Démonstration — pour aller plus loin"
    $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = (x_B - x_A)\vec{i} + (y_B - y_A)\vec{j} + (z_B - z_A)\vec{k}$, et l'on conclut par unicité de la décomposition. Le milieu $I$ vérifie $\overrightarrow{OI} = \frac{1}{2}\left(\overrightarrow{OA} + \overrightarrow{OB}\right)$. Les opérations se font terme à terme, grâce aux règles du calcul vectoriel.

!!! tip "Tester la colinéarité et la coplanarité en coordonnées"
    - $\vec{u}(x, y, z)$ et $\vec{v}(x', y', z')$ sont colinéaires s'il existe $k$ tel que $x' = kx$, $y' = ky$ et $z' = kz$ (ou l'inverse).
    - Pour savoir si $\vec{w}$ est combinaison linéaire de $\vec{u}$ et $\vec{v}$, on cherche $a$ et $b$ avec **deux** coordonnées (système de deux équations), puis on **vérifie** la troisième.

---

## 6. Pour aller plus loin

- **Dimension** : le plan a des bases de 2 vecteurs, l'espace des bases de 3 vecteurs. En **algèbre linéaire** (L1), on définit des espaces de toute dimension, et l'on démontre qu'une base a toujours le même nombre d'éléments.
- **Représentations paramétriques** : la caractérisation $\overrightarrow{AM} = t\vec{u}$ d'une droite donne, en coordonnées, un système d'équations très utile (chapitre 12).
- **Sections de solides** : le théorème du toit et la propriété des plans parallèles permettent de construire la section d'un cube ou d'une pyramide par un plan (méthode 6 et exercice 5).

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
