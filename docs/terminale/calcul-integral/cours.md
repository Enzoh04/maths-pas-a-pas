# Cours — Calcul intégral

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

Dans tout le chapitre, on se place dans un repère **orthogonal** $(O \,;\, I \,;\, J)$. L'**unité d'aire** (notée u.a.) est l'aire du rectangle construit sur $OI$ et $OJ$.

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Intégrale d'une fonction continue et positive

### 1.1 Définition

!!! definition "Intégrale comme aire"
    Soit $f$ une fonction **continue et positive** sur un intervalle $[a \,;\, b]$, et $\mathcal{D}$ le domaine compris entre la courbe de $f$, l'axe des abscisses et les droites d'équations $x = a$ et $x = b$.

    L'**intégrale de $f$ de $a$ à $b$** est l'aire de $\mathcal{D}$, en unités d'aire. On la note

    $$\int_a^b f(x)\,\mathrm{d}x.$$

**Vocabulaire.** $a$ et $b$ sont les **bornes** de l'intégrale. La variable $x$ est **muette** : $\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t$. La notation vient de Leibniz : le signe $\int$ est un « S » allongé, pour « somme », et $f(x)\,\mathrm{d}x$ évoque l'aire d'un rectangle très fin, de hauteur $f(x)$ et de largeur $\mathrm{d}x$.

**Exemples.**

- $\int_1^4 3\,\mathrm{d}x = 9$ : c'est l'aire d'un rectangle de côtés $3$ et $3$.
- $\int_0^2 x\,\mathrm{d}x = 2$ : c'est l'aire d'un triangle rectangle de côtés $2$ et $2$.

??? admis "Ce que l'on admet sur les aires"
    Pour un domaine délimité par une courbe, la notion même d'**aire** demande une définition précise : c'est l'objet de l'**intégrale de Riemann** (L1) puis de l'**intégrale de Lebesgue** (L3). Au lycée, on admet que l'aire existe et qu'elle vérifie trois propriétés intuitives :

    1. l'aire d'un rectangle est le produit de ses côtés ;
    2. si un domaine est contenu dans un autre, son aire est plus petite ;
    3. si un domaine est découpé en deux morceaux, son aire est la somme des aires des morceaux.

    Toutes les démonstrations de ce chapitre n'utilisent que ces trois propriétés.

### 1.2 Le théorème fondamental

!!! theoreme "L'intégrale fonction de sa borne supérieure"
    Soit $f$ continue et positive sur $[a \,;\, b]$. La fonction $F$ définie sur $[a \,;\, b]$ par

    $$F(x) = \int_a^x f(t)\,\mathrm{d}t$$

    est **dérivable** sur $[a \,;\, b]$ et $F' = f$. Autrement dit, $F$ est la primitive de $f$ qui s'annule en $a$.

??? demo "Démonstration — au programme du bac (cas où $f$ est croissante)"
    Soit $x \in [a \,;\, b[$ et $h > 0$ tel que $x + h \leq b$. D'après la relation d'additivité des aires, $F(x + h) - F(x)$ est l'aire du domaine situé sous la courbe entre $x$ et $x + h$.

    Comme $f$ est croissante, pour $t \in [x \,;\, x + h]$ on a $f(x) \leq f(t) \leq f(x + h)$. Le domaine contient donc le rectangle de largeur $h$ et de hauteur $f(x)$, et il est contenu dans le rectangle de largeur $h$ et de hauteur $f(x + h)$ :

    $$h\,f(x) \leq F(x + h) - F(x) \leq h\,f(x + h), \quad \text{soit} \quad f(x) \leq \frac{F(x + h) - F(x)}{h} \leq f(x + h).$$

    Comme $f$ est continue en $x$, $f(x + h) \to f(x)$ quand $h \to 0$. Par les gendarmes, le taux d'accroissement tend vers $f(x)$ à droite.

    Pour $h < 0$ (avec $x + h \geq a$), le même raisonnement sur $[x + h \,;\, x]$ donne $f(x + h) \leq \dfrac{F(x) - F(x + h)}{-h} \leq f(x)$. Or $\dfrac{F(x) - F(x + h)}{-h} = \dfrac{F(x + h) - F(x)}{h}$, qui tend donc aussi vers $f(x)$.

    Ainsi $F$ est dérivable en $x$ et $F'(x) = f(x)$.

??? demoplus "Démonstration dans le cas général (f seulement continue) — pour aller plus loin"
    Soit $x \in [a \,;\, b]$ et $\varepsilon > 0$. Par continuité de $f$ en $x$, il existe $\delta > 0$ tel que, pour $|t - x| < \delta$, on a $f(x) - \varepsilon < f(t) < f(x) + \varepsilon$.

    Pour $0 < h < \delta$, le domaine sous la courbe entre $x$ et $x + h$ est contenu dans le rectangle de hauteur $f(x) + \varepsilon$, et il contient le rectangle de hauteur $\max\big(f(x) - \varepsilon,\, 0\big)$. On obtient

    $$f(x) - \varepsilon \leq \frac{F(x + h) - F(x)}{h} \leq f(x) + \varepsilon.$$

    Le même encadrement vaut pour $-\delta < h < 0$. Le taux d'accroissement est donc à moins de $\varepsilon$ de $f(x)$ dès que $|h| < \delta$ : il tend vers $f(x)$.

!!! propriete "Calcul d'une intégrale par une primitive"
    Soit $f$ continue et positive sur $[a \,;\, b]$, et $G$ **n'importe quelle** primitive de $f$. Alors

    $$\int_a^b f(x)\,\mathrm{d}x = G(b) - G(a).$$

??? demoplus "Démonstration — pour aller plus loin"
    $F(x) = \int_a^x f(t)\,\mathrm{d}t$ et $G$ sont deux primitives de $f$ sur l'intervalle $[a \,;\, b]$ : elles diffèrent d'une constante (chapitre 7), $G = F + C$. Donc $G(b) - G(a) = F(b) - F(a) = F(b) - 0 = \int_a^b f(t)\,\mathrm{d}t$.

**Exemple.** $\displaystyle\int_0^1 x^2\,\mathrm{d}x = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$ u.a.

---

## 2. Intégrale d'une fonction continue de signe quelconque

!!! theoreme "Existence de primitives"
    Toute fonction continue sur un intervalle admet des primitives.

??? demoplus "Démonstration sur un segment, en admettant le théorème des bornes — pour aller plus loin"
    On admet le **théorème des bornes** (chapitre 4, § 5) : une fonction continue sur $[a \,;\, b]$ est bornée. Il existe donc un réel $m$ tel que $f(x) \geq m$ pour tout $x \in [a \,;\, b]$.

    La fonction $g = f - m$ est continue et **positive** sur $[a \,;\, b]$ : d'après le théorème fondamental, elle admet une primitive $G$. Alors $F(x) = G(x) + mx$ vérifie $F' = g + m = f$ : c'est une primitive de $f$.

!!! definition "Intégrale d'une fonction continue"
    Soit $f$ continue sur un intervalle $I$, $a$ et $b$ deux réels de $I$, et $F$ une primitive de $f$ sur $I$. On définit

    $$\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a), \qquad \text{que l'on note aussi} \quad \big[F(x)\big]_a^b.$$

??? demoplus "Pourquoi cette définition a un sens — pour aller plus loin"
    Si $G$ est une autre primitive, $G = F + C$, donc $G(b) - G(a) = F(b) - F(a)$ : le résultat ne dépend pas de la primitive choisie. Pour $f$ positive et $a \leq b$, on retrouve l'aire (§ 1.2) : les deux définitions sont cohérentes.

**Conséquences immédiates.** $\int_a^a f = 0$, et $\int_b^a f = -\int_a^b f$.

!!! propriete "Interprétation : aire algébrique"
    Si $f$ est continue et **négative** sur $[a \,;\, b]$ (avec $a \leq b$), alors $\int_a^b f(x)\,\mathrm{d}x$ est l'**opposé** de l'aire du domaine compris entre la courbe et l'axe des abscisses.

    Pour une fonction qui change de signe, l'intégrale compte **positivement** les aires situées au-dessus de l'axe et **négativement** celles situées en dessous.

??? demoplus "Démonstration — pour aller plus loin"
    $-f$ est continue et positive, et sa courbe est la symétrique de celle de $f$ par rapport à l'axe des abscisses : les deux domaines ont la même aire $\mathcal{A}$. Si $F$ est une primitive de $f$, alors $-F$ en est une de $-f$, et $\mathcal{A} = \int_a^b (-f) = -F(b) + F(a) = -\int_a^b f$. Pour une fonction qui change de signe, on découpe $[a \,;\, b]$ aux points où elle s'annule et l'on utilise la relation de Chasles (§ 3).

**Exemple.** $\displaystyle\int_0^{2\pi} \sin x\,\mathrm{d}x = \big[-\cos x\big]_0^{2\pi} = -1 + 1 = 0$ : les deux « arches » de la sinusoïde, l'une au-dessus et l'autre en dessous de l'axe, ont la même aire.

!!! propriete "Fonction définie par une intégrale"
    Si $f$ est continue sur $I$ et $a \in I$, la fonction $x \mapsto \displaystyle\int_a^x f(t)\,\mathrm{d}t$ est **l'unique primitive de $f$ sur $I$ qui s'annule en $a$**.

??? demoplus "Démonstration — pour aller plus loin"
    Si $F$ est une primitive de $f$, alors $\int_a^x f(t)\,\mathrm{d}t = F(x) - F(a)$, qui est une primitive (elle diffère de $F$ d'une constante) et qui vaut $0$ en $a$. L'unicité est celle du chapitre 7.

---

## 3. Propriétés de l'intégrale

Dans ce paragraphe, $f$ et $g$ sont continues sur un intervalle $I$, et $a$, $b$, $c$ sont des réels de $I$.

!!! propriete "Linéarité"
    Pour tous réels $\alpha$ et $\beta$ :

    $$\int_a^b \big(\alpha f(x) + \beta g(x)\big)\,\mathrm{d}x = \alpha\int_a^b f(x)\,\mathrm{d}x + \beta\int_a^b g(x)\,\mathrm{d}x.$$

!!! propriete "Relation de Chasles"
    $$\int_a^c f(x)\,\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x + \int_b^c f(x)\,\mathrm{d}x.$$

??? demoplus "Démonstration de la linéarité et de la relation de Chasles — pour aller plus loin"
    Si $F$ et $G$ sont des primitives de $f$ et $g$, alors $\alpha F + \beta G$ est une primitive de $\alpha f + \beta g$, et

    $$(\alpha F + \beta G)(b) - (\alpha F + \beta G)(a) = \alpha\big(F(b) - F(a)\big) + \beta\big(G(b) - G(a)\big).$$

    Pour Chasles : $\big(F(b) - F(a)\big) + \big(F(c) - F(b)\big) = F(c) - F(a)$.

!!! propriete "Positivité et ordre"
    On suppose $a \leq b$.

    - **Positivité** : si $f \geq 0$ sur $[a \,;\, b]$, alors $\displaystyle\int_a^b f(x)\,\mathrm{d}x \geq 0$.
    - **Ordre** : si $f \leq g$ sur $[a \,;\, b]$, alors $\displaystyle\int_a^b f(x)\,\mathrm{d}x \leq \int_a^b g(x)\,\mathrm{d}x$.

??? demoplus "Démonstration — pour aller plus loin"
    **Positivité.** Si $F$ est une primitive de $f$, alors $F' = f \geq 0$ : $F$ est croissante sur $[a \,;\, b]$ (chapitre 3, théorème admis), donc $F(b) \geq F(a)$.

    **Ordre.** $g - f \geq 0$, donc $\int_a^b (g - f) \geq 0$, et l'on conclut par linéarité.

!!! warning "Attention à l'ordre des bornes"
    Ces propriétés supposent $a \leq b$. Si $a > b$, les inégalités sont inversées, car $\int_a^b = -\int_b^a$.

!!! propriete "Inégalité de la moyenne"
    Si $a \leq b$ et si $m \leq f(x) \leq M$ pour tout $x \in [a \,;\, b]$, alors

    $$m(b - a) \leq \int_a^b f(x)\,\mathrm{d}x \leq M(b - a).$$

??? demoplus "Démonstration — pour aller plus loin"
    On applique la propriété d'ordre aux fonctions constantes $m$ et $M$ : $\int_a^b m\,\mathrm{d}x = m(b - a)$ et $\int_a^b M\,\mathrm{d}x = M(b - a)$.

---

## 4. Valeur moyenne

!!! definition "Valeur moyenne"
    Soit $f$ continue sur $[a \,;\, b]$ avec $a < b$. La **valeur moyenne** de $f$ sur $[a \,;\, b]$ est le réel

    $$\mu = \frac{1}{b - a}\int_a^b f(x)\,\mathrm{d}x.$$

**Interprétation.** Si $f$ est positive, $\mu$ est la hauteur du rectangle de base $[a \,;\, b]$ qui a la **même aire** que le domaine sous la courbe. En physique, la vitesse moyenne sur un trajet est la valeur moyenne de la vitesse instantanée.

**Exemple.** La valeur moyenne de $\sin$ sur $[0 \,;\, \pi]$ vaut $\dfrac{1}{\pi}\displaystyle\int_0^\pi \sin x\,\mathrm{d}x = \dfrac{2}{\pi} \approx 0{,}64$.

---

## 5. Aire entre deux courbes

!!! propriete "Aire entre deux courbes"
    Si $f$ et $g$ sont continues sur $[a \,;\, b]$ et si $f \geq g$ sur cet intervalle, l'aire du domaine compris entre les deux courbes et les droites $x = a$ et $x = b$ vaut

    $$\mathcal{A} = \int_a^b \big(f(x) - g(x)\big)\,\mathrm{d}x \text{ u.a.}$$

??? demoplus "Démonstration — pour aller plus loin"
    Une fonction continue sur un segment est minorée (théorème des bornes, admis) : il existe $m$ tel que $g + m \geq 0$ sur $[a \,;\, b]$. Translater les deux courbes de $m$ vers le haut ne change pas l'aire entre elles. Les courbes de $f + m$ et $g + m$ sont alors au-dessus de l'axe, et le domaine entre elles est la différence des domaines situés sous chacune d'elles. Son aire vaut donc $\int_a^b (f + m) - \int_a^b (g + m) = \int_a^b (f - g)$.

!!! tip "Méthode"
    On étudie d'abord le **signe de $f - g$** pour savoir quelle courbe est au-dessus. Si elles se croisent, on découpe l'intervalle avec la relation de Chasles.

---

## 6. Intégration par parties

!!! theoreme "Intégration par parties"
    Soit $u$ et $v$ deux fonctions dérivables sur $[a \,;\, b]$, de dérivées $u'$ et $v'$ continues. Alors

    $$\int_a^b u(x)\,v'(x)\,\mathrm{d}x = \big[u(x)\,v(x)\big]_a^b - \int_a^b u'(x)\,v(x)\,\mathrm{d}x.$$

??? demoplus "Démonstration — pour aller plus loin"
    $(uv)' = u'v + uv'$, donc $uv$ est une primitive de $u'v + uv'$, qui est continue. Ainsi

    $$\int_a^b \big(u'v + uv'\big) = \big[uv\big]_a^b, \quad \text{soit, par linéarité,} \quad \int_a^b uv' = \big[uv\big]_a^b - \int_a^b u'v.$$

!!! tip "Bien choisir $u$ et $v'$"
    On choisit pour $u$ la fonction qui **se simplifie en la dérivant** (un polynôme, $\ln x$), et pour $v'$ une fonction dont on connaît une primitive ($e^x$, $\sin x$, $\cos x$, $1$…).

**Exemple.** $\displaystyle\int_0^1 xe^x\,\mathrm{d}x$. On pose $u(x) = x$, $v'(x) = e^x$, donc $u'(x) = 1$ et $v(x) = e^x$ :

$$\int_0^1 xe^x\,\mathrm{d}x = \big[xe^x\big]_0^1 - \int_0^1 e^x\,\mathrm{d}x = e - (e - 1) = 1.$$

---

## 7. Méthode des rectangles

Quand on ne connaît pas de primitive, on approche l'intégrale par des sommes d'aires de rectangles. On découpe $[a \,;\, b]$ en $n$ intervalles de même largeur $h = \frac{b - a}{n}$, avec $x_k = a + kh$.

- **Rectangles à gauche** : $s_n = h\displaystyle\sum_{k=0}^{n-1} f(x_k)$.
- **Rectangles à droite** : $S_n = h\displaystyle\sum_{k=1}^{n} f(x_k)$.

!!! propriete "Encadrement pour une fonction monotone"
    Si $f$ est continue et **croissante** sur $[a \,;\, b]$, alors

    $$s_n \leq \int_a^b f(x)\,\mathrm{d}x \leq S_n \qquad \text{et} \qquad S_n - s_n = \frac{(b - a)\big(f(b) - f(a)\big)}{n}.$$

    En particulier, $s_n$ et $S_n$ tendent vers l'intégrale quand $n \to +\infty$.

??? demoplus "Démonstration — pour aller plus loin"
    Sur $[x_k \,;\, x_{k+1}]$, $f$ croissante donne $f(x_k) \leq f(t) \leq f(x_{k+1})$, donc, par l'inégalité de la moyenne, $h\,f(x_k) \leq \int_{x_k}^{x_{k+1}} f \leq h\,f(x_{k+1})$. On additionne pour $k$ de $0$ à $n - 1$, avec Chasles. La différence $S_n - s_n$ est télescopique : $h\big(f(x_n) - f(x_0)\big) = \frac{b - a}{n}\big(f(b) - f(a)\big)$, qui tend vers $0$. L'intégrale étant comprise entre $s_n$ et $S_n$, les deux sommes s'en rapprochent : par les gendarmes, elles tendent vers l'intégrale.

```python
def rectangles(f, a, b, n):
    h = (b - a) / n
    s = 0
    for k in range(n):
        s = s + f(a + k * h)    # rectangles à gauche
    return h * s
```

---

## 8. Pour aller plus loin

- **Le logarithme comme intégrale** : pour $x > 0$, $\ln x = \displaystyle\int_1^x \frac{\mathrm{d}t}{t}$. Dans le supérieur, c'est souvent la **définition** du logarithme, dont on déduit l'exponentielle comme fonction réciproque (exercice 27).
- **Sommes de Riemann** : pour toute fonction continue (pas seulement monotone), $s_n$ tend vers l'intégrale. C'est la base de la construction de l'intégrale en L1.
- **Probabilités** : au-delà du lycée, les intégrales servent à décrire des lois de probabilité « continues », comme la loi normale, de densité $x \mapsto \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
