# Méthodes — Dérivation et convexité

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Dériver une fonction composée

**Les étapes**

1. Repérer la fonction « intérieure » $u$ et la fonction « extérieure » : $e^{\square}$, $\square^n$, $\sqrt{\square}$…
2. Calculer $u'$.
3. Appliquer la formule adaptée : $(e^u)' = u'e^u$, $(u^n)' = nu'u^{n-1}$, $(\sqrt{u})' = \dfrac{u'}{2\sqrt{u}}$.
4. Simplifier et **factoriser** : on veut le signe de la dérivée.

**Exemple.** $f(x) = x\,e^{-x^2}$. C'est un produit, dont le second facteur est une composée.

- $(e^{-x^2})' = -2x\,e^{-x^2}$ (avec $u = -x^2$, $u' = -2x$).
- $f'(x) = 1 \times e^{-x^2} + x \times (-2x\,e^{-x^2}) = (1 - 2x^2)\,e^{-x^2}$.

!!! warning "Erreur fréquente"
    $(e^{-x^2})' \neq e^{-x^2}$ ! On n'oublie pas de multiplier par $u'$.

---

## Méthode 2 — Étudier la convexité d'une fonction

**Les étapes**

1. Calculer $f'$, puis $f''$, en factorisant au maximum.
2. Étudier le **signe de $f''$** (tableau de signes).
3. Conclure : $f$ est convexe là où $f'' \geq 0$ et concave là où $f'' \leq 0$.

**Exemple.** $f(x) = x\,e^x$ sur $\mathbb{R}$.

- $f'(x) = (x + 1)e^x$, puis $f''(x) = e^x + (x + 1)e^x = (x + 2)e^x$.
- $e^x > 0$, donc $f''(x)$ a le signe de $x + 2$.
- $f$ est concave sur $]-\infty \,;\, -2]$ et convexe sur $[-2 \,;\, +\infty[$.

---

## Méthode 3 — Trouver les points d'inflexion

**Les étapes**

1. Résoudre $f''(x) = 0$.
2. Vérifier que $f''$ **change de signe** en chacune de ces valeurs (tableau de signes).
3. Calculer l'ordonnée $f(a)$ du point d'inflexion.

**Exemple (suite).** $f''(x) = (x + 2)e^x$ s'annule en $-2$ en changeant de signe. Le point $\left(-2 \,;\, -2e^{-2}\right)$ est un point d'inflexion.

!!! warning "Piège"
    Si $f''$ s'annule **sans changer de signe** (comme $12x^2$ en $0$ pour $x^4$), ce n'est pas un point d'inflexion.

---

## Méthode 4 — Position d'une courbe par rapport à une tangente

**Méthode A : par la convexité** (rapide). Si $f$ est convexe sur $I$, la courbe est au-dessus de toutes ses tangentes sur $I$. Si $f$ est concave, elle est en dessous.

**Méthode B : par l'étude du signe** (quand $f$ change de convexité). On étudie le signe de $d(x) = f(x) - \big(f'(a)(x - a) + f(a)\big)$, souvent en factorisant par $(x - a)^2$.

**Exemple.** Courbe de $x^3$ et tangente en $1$, d'équation $y = 3x - 2$ :

$$d(x) = x^3 - 3x + 2 = (x - 1)^2(x + 2).$$

La courbe est au-dessus de la tangente pour $x \geq -2$, en dessous pour $x \leq -2$. Ceci est cohérent avec la convexité de $x^3$ sur $[0 \,;\, +\infty[$, mais montre que la position peut changer **en dehors** de l'intervalle de convexité.

---

## Méthode 5 — Démontrer une inégalité par convexité

**Les étapes**

1. Reconnaître une fonction $f$ convexe (ou concave) dans l'inégalité.
2. Choisir le bon **point de tangence** $a$ : souvent celui où il y a égalité.
3. Écrire la tangente, puis la position de la courbe.

**Exemple.** Montrer que $e^x \geq e\,x$ pour tout réel $x$.

- $\exp$ est convexe sur $\mathbb{R}$ (car $\exp'' = \exp > 0$).
- La tangente en $1$ a pour équation $y = e(x - 1) + e = e\,x$.
- La courbe est au-dessus de cette tangente : $e^x \geq e\,x$ pour tout $x$.

---

## Méthode 6 — Lire la convexité sur un graphique

| On voit la courbe de… | $f$ est convexe là où… |
|---|---|
| $f$ | la courbe est au-dessus de ses tangentes (elle « sourit ») |
| $f'$ | la courbe de $f'$ **monte** ($f'$ croissante) |
| $f''$ | la courbe de $f''$ est **au-dessus de l'axe** des abscisses |

Les points d'inflexion de $f$ correspondent aux **extremums locaux de $f'$**, et aux points où $f''$ change de signe.

!!! warning "Ne pas confondre"
    Le signe de $f'$ donne les **variations** de $f$ ; le signe de $f''$ donne sa **convexité**.
