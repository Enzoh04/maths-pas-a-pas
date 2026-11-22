# Méthodes — Primitives et équations différentielles

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Vérifier qu'une fonction est solution

**Les étapes**

1. Calculer $f'$ (et $f''$ si besoin).
2. Remplacer $y$ par $f(x)$ et $y'$ par $f'(x)$ dans **chaque membre** de l'équation.
3. Montrer que les deux membres sont égaux **pour tout $x$**.

**Exemple.** $f(x) = e^x - x - 1$ est-elle solution de $y' = y + x$ ?

- $f'(x) = e^x - 1$.
- $f(x) + x = e^x - x - 1 + x = e^x - 1$.

Les deux membres sont égaux : $f$ est solution.

---

## Méthode 2 — Trouver une primitive

**Les étapes**

1. Chercher dans le tableau une **forme** : $u'e^u$, $u'u^n$, $\frac{u'}{u}$, $\frac{u'}{u^2}$, $\frac{u'}{\sqrt{u}}$…
2. Identifier $u$, calculer $u'$, et **ajuster le coefficient** constant qui manque.
3. **Vérifier en dérivant.**

**Exemple.** $f(x) = x(x^2 + 1)^3$. Avec $u = x^2 + 1$, $u' = 2x$, on a $f = \frac{1}{2}u'u^3$. Une primitive est $F(x) = \frac{1}{2} \times \frac{u^4}{4} = \frac{(x^2 + 1)^4}{8}$.

*Vérification* : $F'(x) = \frac{4 \times 2x\,(x^2 + 1)^3}{8} = x(x^2 + 1)^3$.

!!! warning "Ce qu'on ne peut pas faire"
    On ne peut ajuster que des **constantes** multiplicatives. Par exemple, $e^{x^2}$ n'est pas de la forme $u'e^u$ (il manque un facteur $2x$, qui n'est pas constant), et l'on ne sait pas en écrire de primitive avec les fonctions usuelles.

---

## Méthode 3 — Primitive vérifiant une condition

**Les étapes**

1. Écrire la forme générale $F(x) = G(x) + C$.
2. Utiliser la condition $F(x_0) = y_0$ pour calculer $C$.

**Exemple.** Primitive de $f(x) = 3x^2 - 4x$ telle que $F(1) = 2$ : $F(x) = x^3 - 2x^2 + C$ et $F(1) = -1 + C = 2$, donc $C = 3$.

---

## Méthode 4 — Résoudre $y' = ay + b$ avec une condition initiale

**Les étapes**

1. Mettre l'équation sous la forme $y' = ay + b$ (diviser si besoin par le coefficient de $y'$).
2. Écrire les solutions : $f(x) = Ce^{ax} - \frac{b}{a}$.
3. Calculer $C$ avec la condition initiale.

**Exemple.** $2y' + y = 4$ avec $y(0) = 0$.

- $y' = -\frac{1}{2}y + 2$, donc $a = -\frac{1}{2}$, $b = 2$ et $-\frac{b}{a} = 4$.
- $f(x) = Ce^{-x/2} + 4$, et $f(0) = C + 4 = 0$ donne $C = -4$.
- $f(x) = 4 - 4e^{-x/2}$.

---

## Méthode 5 — Résoudre $y' = ay + f$

**Les étapes**

1. Trouver une **solution particulière** $p$ : elle est souvent donnée, ou on la cherche sous une forme imposée (voir le tableau du cours) en **identifiant les coefficients**.
2. Résoudre l'équation **homogène** $y' = ay$ : $Ce^{ax}$.
3. Solutions : $p(x) + Ce^{ax}$. Utiliser la condition initiale s'il y en a une.

**Exemple.** $y' + y = e^{-x}$. On vérifie que $p(x) = xe^{-x}$ est solution : $p'(x) + p(x) = e^{-x} - xe^{-x} + xe^{-x} = e^{-x}$. L'équation homogène $y' = -y$ a pour solutions $Ce^{-x}$. Solutions : $f(x) = (x + C)e^{-x}$.

!!! warning "Ne pas oublier la condition initiale à la fin"
    On applique la condition initiale à la **solution générale** $p + Ce^{ax}$, et non à la seule partie $Ce^{ax}$.

---

## Méthode 6 — Modéliser une situation

**Les étapes**

1. Repérer la phrase qui décrit la **vitesse de variation** : « proportionnelle à… », « diminue de … % par … ».
2. La traduire en équation : « la vitesse est proportionnelle à la quantité » donne $y' = ky$.
3. Résoudre, puis **interpréter** : limite à l'infini, temps pour atteindre un seuil (avec $\ln$).

**Exemple.** « Un objet refroidit à une vitesse proportionnelle à l'écart entre sa température et celle de la pièce (20 °C). » On écrit $\theta' = -k(\theta - 20)$, avec $k > 0$ : la température baisse quand $\theta > 20$.
