# Cours — Fonctions sinus et cosinus

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Rappels de Première

### 1.1 Le cercle trigonométrique

Dans un repère orthonormé, le **cercle trigonométrique** est le cercle de centre $O$ et de rayon $1$, parcouru dans le sens inverse des aiguilles d'une montre. À tout réel $x$, on associe le point $M$ du cercle obtenu en « enroulant » la droite des réels autour du cercle à partir du point $I(1 \,;\, 0)$ : l'arc $\overset{\frown}{IM}$ a pour longueur $|x|$.

!!! definition "Cosinus et sinus"
    Le **cosinus** et le **sinus** de $x$ sont les coordonnées du point $M$ associé à $x$ :

    $$M(\cos x \,;\, \sin x).$$

??? admis "Pourquoi cette définition est admise"
    Cette définition repose sur la notion de **longueur d'un arc de cercle**, que l'on accepte intuitivement depuis le collège (le périmètre du cercle de rayon $1$ vaut $2\pi$). Définir rigoureusement la longueur d'une courbe demande le **calcul intégral** (L1). Dans le supérieur, on définit souvent $\cos$ et $\sin$ autrement, par exemple comme sommes de séries, $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$ (L2), ou comme solutions de l'équation $y'' + y = 0$. On retrouve ensuite toutes les propriétés géométriques.

!!! propriete "Propriétés fondamentales"
    Pour tout réel $x$ et tout entier $k$ :

    - $-1 \leq \cos x \leq 1$ et $-1 \leq \sin x \leq 1$ ;
    - $\cos^2 x + \sin^2 x = 1$ (car $OM = 1$) ;
    - $\cos(x + 2k\pi) = \cos x$ et $\sin(x + 2k\pi) = \sin x$ (un tour complet ramène au même point).

**Valeurs remarquables.**

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\cos x$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ |
| $\sin x$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ |

### 1.2 Angles associés

!!! propriete "Angles associés"
    Pour tout réel $x$ (lecture par symétries sur le cercle) :

    | | $-x$ | $\pi - x$ | $\pi + x$ | $\frac{\pi}{2} - x$ | $\frac{\pi}{2} + x$ |
    |---|---|---|---|---|---|
    | $\cos$ | $\cos x$ | $-\cos x$ | $-\cos x$ | $\sin x$ | $-\sin x$ |
    | $\sin$ | $-\sin x$ | $\sin x$ | $-\sin x$ | $\cos x$ | $\cos x$ |

### 1.3 Équations $\cos x = \cos a$ et $\sin x = \sin a$

!!! propriete "Résolution"
    Pour tous réels $x$ et $a$ :

    - $\cos x = \cos a \iff x = a + 2k\pi$ ou $x = -a + 2k\pi$, avec $k \in \mathbb{Z}$ ;
    - $\sin x = \sin a \iff x = a + 2k\pi$ ou $x = \pi - a + 2k\pi$, avec $k \in \mathbb{Z}$.

??? demoplus "Démonstration — pour aller plus loin"
    Deux points du cercle ont la même abscisse si et seulement s'ils sont confondus ou symétriques par rapport à l'axe des abscisses. Le point associé à $a$ a pour symétrique celui associé à $-a$. Les réels associés au même point que $a$ sont les $a + 2k\pi$. Pour le sinus, on raisonne de même avec la symétrie par rapport à l'axe des ordonnées, qui associe $\pi - a$ à $a$.

---

## 2. Formules d'addition

!!! theoreme "Formules d'addition"
    Pour tous réels $a$ et $b$ :

    $$\cos(a - b) = \cos a \cos b + \sin a \sin b, \qquad \cos(a + b) = \cos a \cos b - \sin a \sin b,$$

    $$\sin(a + b) = \sin a \cos b + \cos a \sin b, \qquad \sin(a - b) = \sin a \cos b - \cos a \sin b.$$

    En particulier (**formules de duplication**) : $\sin(2a) = 2\sin a \cos a$ et $\cos(2a) = \cos^2 a - \sin^2 a = 1 - 2\sin^2 a = 2\cos^2 a - 1$.

??? demoplus "Démonstration par le produit scalaire — pour aller plus loin"
    Soit $\vec{u}(\cos a \,;\, \sin a)$ et $\vec{v}(\cos b \,;\, \sin b)$, vecteurs de norme $1$ (car $\cos^2 + \sin^2 = 1$), qui font avec l'axe des abscisses des angles $a$ et $b$. L'angle de $\vec{v}$ à $\vec{u}$ mesure donc $a - b$. On calcule le produit scalaire de deux façons (Première) :

    - avec l'angle : $\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(a - b) = \cos(a - b)$ ;
    - avec les coordonnées, dans un repère orthonormé : $\vec{u} \cdot \vec{v} = \cos a \cos b + \sin a \sin b$.

    D'où la première formule. On remplace $b$ par $-b$ pour obtenir $\cos(a + b)$, car $\cos(-b) = \cos b$ et $\sin(-b) = -\sin b$. Pour le sinus :

    $$\sin(a + b) = \cos\left(\tfrac{\pi}{2} - a - b\right) = \cos\left(\left(\tfrac{\pi}{2} - a\right) - b\right) = \sin a \cos b + \cos a \sin b,$$

    en utilisant $\cos\left(\frac{\pi}{2} - a\right) = \sin a$ et $\sin\left(\frac{\pi}{2} - a\right) = \cos a$. Les formules de duplication s'obtiennent avec $b = a$ et $\cos^2 a + \sin^2 a = 1$.

---

## 3. Les fonctions sinus et cosinus

### 3.1 Périodicité et parité

!!! propriete "Périodicité et parité"
    - $\sin$ et $\cos$ sont définies sur $\mathbb{R}$ et **périodiques de période $2\pi$** : pour tout $x$, $\cos(x + 2\pi) = \cos x$ et $\sin(x + 2\pi) = \sin x$.
    - $\cos$ est **paire** : $\cos(-x) = \cos x$. Sa courbe est symétrique par rapport à l'axe des ordonnées.
    - $\sin$ est **impaire** : $\sin(-x) = -\sin x$. Sa courbe est symétrique par rapport à l'origine.

!!! tip "Réduire l'intervalle d'étude"
    Grâce à la périodicité, il suffit d'étudier ces fonctions sur un intervalle de longueur $2\pi$, par exemple $[-\pi \,;\, \pi]$. Grâce à la parité, il suffit même d'étudier sur $[0 \,;\, \pi]$, puis de compléter par symétrie.

### 3.2 Une inégalité et une limite fondamentales

!!! propriete "Inégalités de base"
    - Pour tout $x \in \left]0 \,;\, \frac{\pi}{2}\right[$ : $\sin x < x < \tan x$, où $\tan x = \dfrac{\sin x}{\cos x}$.
    - Pour tout réel $x$ : $|\sin x| \leq |x|$.

??? demoplus "Démonstration par les aires — pour aller plus loin"
    Soit $x \in \left]0 \,;\, \frac{\pi}{2}\right[$, $M(\cos x \,;\, \sin x)$ le point associé, $I(1 \,;\, 0)$, et $T(1 \,;\, \tan x)$ le point où la droite $(OM)$ coupe la tangente au cercle en $I$ (théorème de Thalès).

    On compare les aires de trois figures emboîtées : le triangle $OIM$ est contenu dans le secteur angulaire $OIM$, lui-même contenu dans le triangle $OIT$.

    - Aire du triangle $OIM$ : $\frac{1}{2} \times OI \times (\text{hauteur}) = \frac{1}{2}\sin x$.
    - Aire du secteur : elle est proportionnelle à l'angle, et vaut $\pi$ pour un tour complet ($2\pi$). Elle vaut donc $\frac{x}{2}$.
    - Aire du triangle $OIT$ : $\frac{1}{2} \times 1 \times \tan x$.

    D'où $\frac{1}{2}\sin x < \frac{x}{2} < \frac{1}{2}\tan x$.

    **Pour tout réel $x$.** Si $0 < x < \frac{\pi}{2}$, c'est la première inégalité. Si $x \geq \frac{\pi}{2} > 1$, alors $|\sin x| \leq 1 < x$. Si $x = 0$, c'est une égalité. Pour $x < 0$, on utilise l'imparité : $|\sin x| = |\sin(-x)| \leq |-x| = |x|$.

!!! theoreme "Limite fondamentale"
    $$\lim_{x \to 0} \frac{\sin x}{x} = 1 \qquad\qquad \lim_{x \to 0} \frac{\cos x - 1}{x} = 0$$

??? demoplus "Démonstration — pour aller plus loin"
    **Continuité en $0$.** D'après $|\sin x| \leq |x|$, on a $\sin x \to 0$ quand $x \to 0$ (gendarmes). Par la formule de duplication, $0 \leq 1 - \cos x = 2\sin^2\frac{x}{2} \leq 2\left(\frac{x}{2}\right)^2 = \frac{x^2}{2}$, donc $\cos x \to 1$.

    **Limite de $\frac{\sin x}{x}$.** Pour $0 < x < \frac{\pi}{2}$, on a $\sin x < x$, donc $\frac{\sin x}{x} < 1$. On a aussi $x < \frac{\sin x}{\cos x}$, et comme $\cos x > 0$ : $\cos x < \frac{\sin x}{x}$. Ainsi

    $$\cos x < \frac{\sin x}{x} < 1.$$

    Quand $x \to 0^+$, $\cos x \to 1$ : par les gendarmes, $\frac{\sin x}{x} \to 1$. Comme $\frac{\sin x}{x}$ est une fonction paire (quotient de deux fonctions impaires), la limite à gauche est la même.

    **Limite de $\frac{\cos x - 1}{x}$.** D'après ce qui précède, $\left|\dfrac{\cos x - 1}{x}\right| \leq \dfrac{x^2/2}{|x|} = \dfrac{|x|}{2} \to 0$.

### 3.3 Continuité et dérivées

!!! theoreme "Dérivées"
    $\sin$ et $\cos$ sont continues et dérivables sur $\mathbb{R}$, et :

    $$\sin' = \cos \qquad\qquad \cos' = -\sin$$

??? demoplus "Démonstration — pour aller plus loin"
    Soit $x$ un réel. Par la formule d'addition, pour $h \neq 0$ :

    $$\frac{\sin(x + h) - \sin x}{h} = \frac{\sin x \cos h + \cos x \sin h - \sin x}{h} = \sin x \times \frac{\cos h - 1}{h} + \cos x \times \frac{\sin h}{h}.$$

    Quand $h \to 0$, d'après les limites fondamentales, ce taux tend vers $\sin x \times 0 + \cos x \times 1 = \cos x$.

    De même, $\dfrac{\cos(x + h) - \cos x}{h} = \cos x \times \dfrac{\cos h - 1}{h} - \sin x \times \dfrac{\sin h}{h} \to -\sin x$.

    Les deux fonctions étant dérivables, elles sont continues (chapitre 3).

!!! propriete "Dérivées de composées"
    Si $u$ est dérivable sur $I$, et $a$, $b$ sont des réels :

    $$\big(\sin(ax + b)\big)' = a\cos(ax + b), \qquad \big(\cos(ax + b)\big)' = -a\sin(ax + b),$$

    $$\big(\sin u\big)' = u'\cos u, \qquad \big(\cos u\big)' = -u'\sin u.$$

??? demoplus "Démonstration — pour aller plus loin"
    C'est la formule de dérivation d'une composée (chapitre 3) appliquée avec $v = \sin$ ou $v = \cos$.

!!! tip "Remarque"
    La limite fondamentale $\frac{\sin x}{x} \to 1$ n'est autre que $\sin'(0) = \cos 0 = 1$. Graphiquement, la tangente à la courbe du sinus en $0$ est la droite $y = x$.

### 3.4 Variations et courbes

Sur $[0 \,;\, \pi]$ : $\cos' = -\sin \leq 0$, et $\sin' = \cos$ est positif sur $\left[0 \,;\, \frac{\pi}{2}\right]$, négatif sur $\left[\frac{\pi}{2} \,;\, \pi\right]$.

| $x$ | $0$ | | $\frac{\pi}{2}$ | | $\pi$ |
|---|---|---|---|---|---|
| $\cos x$ | $1$ | $\searrow$ | $0$ | $\searrow$ | $-1$ |
| $\sin x$ | $0$ | $\nearrow$ | $1$ | $\searrow$ | $0$ |

On complète par parité sur $[-\pi \,;\, 0]$, puis par périodicité sur $\mathbb{R}$. Les courbes obtenues s'appellent des **sinusoïdes**. Comme $\cos x = \sin\left(x + \frac{\pi}{2}\right)$, la courbe du cosinus est celle du sinus translatée de $\frac{\pi}{2}$ vers la gauche.

**Convexité.** $\sin'' = -\sin$ et $\cos'' = -\cos$. Par exemple, $\sin$ est concave sur $[0 \,;\, \pi]$ (où $\sin \geq 0$) et convexe sur $[\pi \,;\, 2\pi]$ : ses points d'inflexion sont les points d'abscisse $k\pi$.

---

## 4. Applications

### 4.1 Signaux sinusoïdaux

En physique, un signal sinusoïdal s'écrit $f(t) = A\cos(\omega t + \varphi)$, avec :

- $A > 0$ l'**amplitude** ;
- $\omega > 0$ la **pulsation**, et $T = \dfrac{2\pi}{\omega}$ la **période** ;
- $\varphi$ la **phase** à l'origine.

!!! propriete "Période"
    Pour $\omega > 0$, la fonction $t \mapsto \cos(\omega t + \varphi)$ est périodique de période $\dfrac{2\pi}{\omega}$.

??? demoplus "Démonstration — pour aller plus loin"
    $\cos\left(\omega\left(t + \frac{2\pi}{\omega}\right) + \varphi\right) = \cos(\omega t + \varphi + 2\pi) = \cos(\omega t + \varphi)$.

**Exemple.** Le courant électrique domestique a une fréquence de 50 Hz : $u(t) = U\cos(100\pi t)$, de période $\frac{2\pi}{100\pi} = 0{,}02$ s.

### 4.2 Oscillations amorties

Les fonctions du type $f(t) = e^{-kt}\cos(\omega t)$ (avec $k > 0$) modélisent des oscillations qui s'atténuent : ressort freiné, corde de guitare… Comme $-e^{-kt} \leq f(t) \leq e^{-kt}$, la courbe reste entre les deux courbes « enveloppes » $\pm e^{-kt}$, et $f(t) \to 0$ (gendarmes).

---

## 5. Pour aller plus loin

- **L'équation $y'' + y = 0$** : $\sin$ et $\cos$ en sont solutions, et ce sont « les seules » au sens de l'exercice 27. C'est l'équation du ressort sans frottement.
- **Encadrements polynomiaux** : le sujet type bac 4 montre que $x - \frac{x^3}{6} \leq \sin x \leq x$ pour $x \geq 0$. En continuant, on obtient le **développement en série** de $\sin$, vu dans le supérieur.
- **Nombres complexes** (option maths expertes) : la formule $e^{ix} = \cos x + i\sin x$ relie l'exponentielle et la trigonométrie, et donne les formules d'addition en une ligne.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
