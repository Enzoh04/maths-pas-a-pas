# Sujets type bac — Dérivation et convexité

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Étude de $x e^{-x}$ | variations, convexité, tangente, inégalité |
| 2 | Une fonction avec racine carrée | dérivée de composée, convexité, asymptotes obliques |
| 3 | QCM | dérivées, convexité, inflexion |
| 4 | Modélisation : coût de production | dérivée seconde, point d'inflexion, interprétation |

## Sujet 1 — Étude de $x e^{-x}$

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x\,e^{-x}$, et $\mathcal{C}$ sa courbe.

**Partie A — Variations**

1. Déterminer les limites de $f$ en $-\infty$ et en $+\infty$.
2. Montrer que $f'(x) = (1 - x)e^{-x}$ et dresser le tableau de variations de $f$.

**Partie B — Convexité**

3. Montrer que $f''(x) = (x - 2)e^{-x}$.
4. Étudier la convexité de $f$ et montrer que $\mathcal{C}$ admet un point d'inflexion $I$, dont on donnera les coordonnées.
5. Déterminer une équation de la tangente $T$ à $\mathcal{C}$ au point d'abscisse $0$.
6. En déduire que pour tout $x \leq 2$ : $x\,e^{-x} \leq x$.

??? success "Correction"
    **1.** En $-\infty$ : $x \to -\infty$ et $e^{-x} \to +\infty$, donc $f(x) \to -\infty$. En $+\infty$ : $f(x) = \dfrac{x}{e^x} \to 0$ par croissance comparée.

    **2.** $f'(x) = e^{-x} - x e^{-x} = (1 - x)e^{-x}$, du signe de $1 - x$.

    | $x$ | $-\infty$ | | $1$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $-\infty$ | $\nearrow$ | $\frac{1}{e}$ | $\searrow$ | $0$ |

    **3.** $f''(x) = -e^{-x} - (1 - x)e^{-x} = (-1 - 1 + x)e^{-x} = (x - 2)e^{-x}$.

    **4.** $f''(x)$ a le signe de $x - 2$ : $f$ est concave sur $]-\infty \,;\, 2]$ et convexe sur $[2 \,;\, +\infty[$. $f''$ s'annule en changeant de signe en $2$ : $I\left(2 \,;\, 2e^{-2}\right)$ est un point d'inflexion.

    **5.** $f(0) = 0$ et $f'(0) = 1$ : $T : y = x$.

    **6.** Sur $]-\infty \,;\, 2]$, $f$ est concave, donc $\mathcal{C}$ est en dessous de ses tangentes sur cet intervalle, en particulier de $T$ (car $0 \in \,]-\infty \,;\, 2]$). Donc $f(x) \leq x$ pour tout $x \leq 2$.

---

## Sujet 2 — Une fonction avec racine carrée

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = \sqrt{x^2 + 1}$, et $\mathcal{C}$ sa courbe.

1. Montrer que $f$ est paire. Que peut-on en déduire pour $\mathcal{C}$ ?
2. Montrer que $f'(x) = \dfrac{x}{\sqrt{x^2 + 1}}$ et dresser le tableau de variations de $f$.
3. Montrer que $f''(x) = \dfrac{1}{(x^2 + 1)\sqrt{x^2 + 1}}$. En déduire la convexité de $f$.
4. En déduire que pour tout réel $x$, $\sqrt{x^2 + 1} \geq 1$, en utilisant une tangente.
5. Montrer que $\displaystyle\lim_{x\to+\infty} \left(f(x) - x\right) = 0$. Interpréter graphiquement. Que se passe-t-il en $-\infty$ ?

??? success "Correction"
    **1.** $f(-x) = \sqrt{(-x)^2 + 1} = f(x)$ : $f$ est paire, $\mathcal{C}$ est symétrique par rapport à l'axe des ordonnées.

    **2.** $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$ avec $u = x^2 + 1 > 0$ : $f'(x) = \dfrac{2x}{2\sqrt{x^2 + 1}} = \dfrac{x}{\sqrt{x^2 + 1}}$, du signe de $x$. En $\pm\infty$, $f(x) \to +\infty$.

    | $x$ | $-\infty$ | | $0$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $-$ | $0$ | $+$ | |
    | $f(x)$ | $+\infty$ | $\searrow$ | $1$ | $\nearrow$ | $+\infty$ |

    **3.** On écrit $f'(x) = x\,(x^2 + 1)^{-1/2}$ et on dérive le produit :

    $$f''(x) = (x^2 + 1)^{-1/2} + x \times \left(-\tfrac{1}{2}\right)(2x)(x^2 + 1)^{-3/2} = \frac{(x^2 + 1) - x^2}{(x^2 + 1)^{3/2}} = \frac{1}{(x^2 + 1)\sqrt{x^2 + 1}}.$$

    *Variante sans exposant fractionnaire :* on dérive $f' = \dfrac{x}{\sqrt{x^2+1}}$ comme un quotient, avec $(\sqrt{x^2+1})' = \dfrac{x}{\sqrt{x^2+1}}$, et l'on obtient le même résultat.

    $f''(x) > 0$ : $f$ est convexe sur $\mathbb{R}$.

    **4.** La tangente en $0$ est horizontale : $y = f'(0)(x - 0) + f(0) = 1$. $f$ étant convexe, $\mathcal{C}$ est au-dessus de cette tangente : $f(x) \geq 1$.

    **5.** Avec la quantité conjuguée, pour $x > 0$ :

    $$f(x) - x = \frac{(x^2 + 1) - x^2}{\sqrt{x^2 + 1} + x} = \frac{1}{\sqrt{x^2 + 1} + x} \longrightarrow 0.$$

    La droite $y = x$ est asymptote oblique à $\mathcal{C}$ en $+\infty$. Par symétrie (parité), la droite $y = -x$ est asymptote oblique en $-\infty$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** La dérivée de $x \mapsto e^{x^2 + 1}$ est :

a) $e^{x^2 + 1}$ — b) $2x\,e^{x^2 + 1}$ — c) $(x^2 + 1)e^{x^2}$ — d) $2x\,e^{2x}$

**Question 2.** La fonction $x \mapsto x^3 - 3x$ est convexe sur :

a) $\mathbb{R}$ — b) $]-\infty \,;\, 0]$ — c) $[0 \,;\, +\infty[$ — d) $[-1 \,;\, 1]$

**Question 3.** L'abscisse du point d'inflexion de la courbe de $x \mapsto x\,e^x$ est :

a) $-2$ — b) $-1$ — c) $0$ — d) il n'y en a pas

**Question 4.** $f$ est une fonction convexe sur $\mathbb{R}$ dont la tangente au point d'abscisse $0$ a pour équation $y = 2x + 1$. Alors :

a) $f(1) = 3$ — b) $f(1) \geq 3$ — c) $f(1) \leq 3$ — d) on ne peut rien dire de $f(1)$

**Question 5.** La dérivée de $x \mapsto \sqrt{1 - 2x}$ sur $\left]-\infty \,;\, \frac{1}{2}\right[$ est :

a) $\dfrac{1}{2\sqrt{1 - 2x}}$ — b) $-\dfrac{1}{\sqrt{1 - 2x}}$ — c) $-\dfrac{2}{\sqrt{1 - 2x}}$ — d) $\dfrac{-2x}{\sqrt{1 - 2x}}$

??? success "Correction"
    **Question 1 : b).** $(e^u)' = u'e^u$ avec $u = x^2 + 1$ et $u' = 2x$.

    **Question 2 : c).** $f''(x) = 6x \geq 0 \iff x \geq 0$.

    **Question 3 : a).** $f''(x) = (x + 2)e^x$ change de signe en $-2$.

    **Question 4 : b).** La courbe d'une fonction convexe est au-dessus de ses tangentes : $f(1) \geq 2 \times 1 + 1 = 3$. L'égalité n'est pas garantie : par exemple, $f(x) = x^2 + 2x + 1$ convient et donne $f(1) = 4$.

    **Question 5 : b).** $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$ avec $u' = -2$ : $\dfrac{-2}{2\sqrt{1 - 2x}} = -\dfrac{1}{\sqrt{1 - 2x}}$.

---

## Sujet 4 — Coût de production

Une entreprise fabrique entre 0 et 10 tonnes d'un produit par jour. Le coût total de production, en centaines d'euros, pour $q$ tonnes, est modélisé par :

$$C(q) = q^3 - 12q^2 + 60q + 10, \qquad q \in [0 \,;\, 10].$$

On appelle **coût marginal** la dérivée $C'(q)$ : elle mesure approximativement le coût de production d'une tonne supplémentaire.

1. Calculer $C'(q)$. Montrer que $C'(q) > 0$ pour tout $q$, et interpréter.
2. Calculer $C''(q)$. Étudier la convexité de $C$ sur $[0 \,;\, 10]$.
3. Montrer que la courbe de $C$ admet un point d'inflexion $I$. Donner ses coordonnées.
4. Montrer que le coût marginal est minimal pour $q = 4$, et donner ce coût marginal minimal.
5. Interpréter les résultats : comment évolue le coût d'une tonne supplémentaire avant et après 4 tonnes ?

??? success "Correction"
    **1.** $C'(q) = 3q^2 - 24q + 60 = 3(q^2 - 8q + 20)$. Le discriminant de $q^2 - 8q + 20$ vaut $64 - 80 = -16 < 0$ : ce trinôme est toujours du signe de son coefficient dominant, positif. Donc $C'(q) > 0$ : le coût total augmente avec la quantité produite, ce qui est logique.

    **2.** $C''(q) = 6q - 24 = 6(q - 4)$. $C$ est concave sur $[0 \,;\, 4]$ et convexe sur $[4 \,;\, 10]$.

    **3.** $C''$ s'annule en changeant de signe en $q = 4$. Comme $C(4) = 64 - 192 + 240 + 10 = 122$, le point d'inflexion est $I(4 \,;\, 122)$.

    **4.** Le coût marginal $C'$ a pour dérivée $C''$, négative sur $[0 \,;\, 4]$ et positive sur $[4 \,;\, 10]$. Donc $C'$ est décroissante puis croissante : elle est minimale en $q = 4$, et $C'(4) = 48 - 96 + 60 = 12$, soit 1 200 € par tonne supplémentaire.

    **5.** Jusqu'à 4 tonnes, chaque tonne supplémentaire coûte de moins en moins cher : c'est la zone d'**économies d'échelle**, où le coût total est concave. Au-delà de 4 tonnes, chaque tonne supplémentaire coûte de plus en plus cher, par exemple à cause de la saturation des machines ou des heures supplémentaires : le coût total est convexe.
