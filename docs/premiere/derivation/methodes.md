# Méthodes — Dérivation

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Calculer un nombre dérivé avec la définition

**Les étapes**

1. Écrire le taux de variation $\dfrac{f(a + h) - f(a)}{h}$ pour $h \neq 0$.
2. Développer et réduire le numérateur, puis **simplifier par $h$**.
3. Faire tendre $h$ vers $0$ dans l'expression simplifiée.

**Exemple.** $f(x) = x^2 + 3x$, $a = 2$.
$$\frac{f(2 + h) - f(2)}{h} = \frac{(4 + 4h + h^2 + 6 + 3h) - 10}{h} = \frac{7h + h^2}{h} = 7 + h,$$
qui tend vers $7$ : $f'(2) = 7$.

---

## Méthode 2 — Déterminer l'équation d'une tangente

**Les étapes**

1. Calculer $f(a)$.
2. Calculer $f'(x)$, puis $f'(a)$.
3. Écrire $y = f'(a)(x - a) + f(a)$, puis réduire sous la forme $y = mx + p$.

**Exemple.** Tangente à la courbe de $f(x) = \dfrac{1}{x}$ au point d'abscisse $1$. $f(1) = 1$, $f'(x) = -\dfrac{1}{x^2}$ donc $f'(1) = -1$. Équation : $y = -(x - 1) + 1$, soit $y = -x + 2$.

---

## Méthode 3 — Lire un nombre dérivé sur un graphique

**Les étapes**

1. Repérer la tangente au point d'abscisse $a$.
2. Choisir deux points de la tangente **bien placés** (sur le quadrillage).
3. Calculer le coefficient directeur : $f'(a) = \dfrac{\Delta y}{\Delta x}$.
4. Rappel : tangente horizontale $\iff f'(a) = 0$ ; tangente qui « monte » $\iff f'(a) > 0$.

**Exemple.** La tangente en $A(1\,;\,2)$ passe aussi par $B(3\,;\,-2)$. Alors $f'(1) = \dfrac{-2 - 2}{3 - 1} = -2$, et la tangente a pour équation $y = -2(x - 1) + 2 = -2x + 4$.

---

## Méthode 4 — Calculer une fonction dérivée

**Les étapes**

1. Préciser l'intervalle où la fonction est dérivable.
2. Reconnaître la **structure** : somme, produit $uv$, quotient $\frac{u}{v}$, inverse $\frac{1}{v}$, ou $g(ax + b)$.
3. Écrire clairement $u$, $u'$, $v$, $v'$, puis appliquer la formule.
4. Simplifier (réduire au même dénominateur, factoriser) si l'on doit ensuite étudier un signe.

**Exemple.** $f(x) = x\sqrt{x}$ sur $]0\,;\,+\infty[$. Avec $u(x) = x$, $u'(x) = 1$, $v(x) = \sqrt{x}$, $v'(x) = \frac{1}{2\sqrt{x}}$ :
$$f'(x) = \sqrt{x} + x \times \frac{1}{2\sqrt{x}} = \sqrt{x} + \frac{\sqrt{x}}{2} = \frac{3}{2}\sqrt{x}.$$

**Exemple.** $g(x) = \dfrac{1}{x^2 + 1}$ sur $\mathbb{R}$. Avec $v(x) = x^2 + 1$ : $g'(x) = -\dfrac{2x}{(x^2 + 1)^2}$.

---

## Méthode 5 — Utiliser l'approximation linéaire

**Les étapes**

1. Choisir une fonction $f$ et un point $a$ « simple » proche de la valeur voulue.
2. Calculer $f(a)$ et $f'(a)$.
3. Écrire $f(a + h) \approx f(a) + f'(a)\,h$.

**Exemple.** Approcher $\dfrac{1}{1{,}03}$. Avec $f(x) = \dfrac{1}{x}$, $a = 1$, $h = 0{,}03$ : $f(1) = 1$, $f'(1) = -1$, donc $\dfrac{1}{1{,}03} \approx 1 - 0{,}03 = 0{,}97$. (Valeur exacte : $0{,}9709\ldots$)

---

## Méthode 6 — Résoudre un problème de tangente

**Les étapes**

1. **Tangente de coefficient directeur $m$ donné** : résoudre $f'(x) = m$. (Tangente horizontale : $m = 0$ ; tangente parallèle à une droite : même coefficient directeur.)
2. **Tangente passant par un point $P$** : écrire l'équation de la tangente en un point d'abscisse $a$ inconnue, puis écrire que $P$ vérifie cette équation ; on obtient une équation en $a$.

**Exemple.** Pour $f(x) = x^3 - 3x$ : $f'(x) = 3x^2 - 3 = 0 \iff x = 1$ ou $x = -1$. La courbe a des tangentes horizontales aux points $(1\,;\,-2)$ et $(-1\,;\,2)$.

**Exemple.** Tangentes à la parabole $y = x^2$ passant par $P(0\,;\,-1)$. La tangente au point d'abscisse $a$ est $y = 2a(x - a) + a^2 = 2ax - a^2$. Elle passe par $P$ si et seulement si $-1 = -a^2$, soit $a = 1$ ou $a = -1$. Les deux tangentes sont $y = 2x - 1$ et $y = -2x - 1$.
