# Méthodes — Fonction logarithme népérien

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Simplifier une expression

**Les outils**

| Pour… | On utilise… |
|---|---|
| un produit | $\ln(ab) = \ln a + \ln b$ |
| un quotient | $\ln\frac{a}{b} = \ln a - \ln b$ |
| une puissance | $\ln(a^n) = n\ln a$ |
| une racine | $\ln\sqrt{a} = \frac{1}{2}\ln a$ |
| $\ln$ et $\exp$ ensemble | $e^{\ln x} = x$ et $\ln(e^x) = x$ |

**Astuce.** Pour exprimer un logarithme en fonction de $\ln 2$ et $\ln 3$, on **décompose en facteurs premiers** : $\ln 72 = \ln(2^3 \times 3^2) = 3\ln 2 + 2\ln 3$.

---

## Méthode 2 — Résoudre une équation ou une inéquation

**Les étapes**

1. **Déterminer l'ensemble de résolution** : tout ce qui est dans un $\ln$ doit être **strictement positif**.
2. Se ramener à la forme $\ln A = \ln B$ (ou $<$), en regroupant les logarithmes avec les propriétés algébriques.
3. Utiliser $\ln A = \ln B \iff A = B$ (ou $\ln A < \ln B \iff A < B$).
4. **Vérifier que les solutions trouvées sont dans l'ensemble de résolution.**

**Exemple.** $\ln x + \ln(x - 1) = \ln 6$.

- Il faut $x > 0$ et $x - 1 > 0$ : on résout sur $]1 \,;\, +\infty[$.
- $\ln\big(x(x - 1)\big) = \ln 6 \iff x^2 - x - 6 = 0 \iff x = 3$ ou $x = -2$.
- Seul $3$ est dans $]1 \,;\, +\infty[$ : $\mathcal{S} = \{3\}$.

!!! warning "Piège"
    Sans l'étape 1, on garderait la fausse solution $-2$, pour laquelle $\ln(-2)$ n'existe pas.

---

## Méthode 3 — Poser un changement de variable

**Quand ?** L'équation contient $e^{2x}$ et $e^x$, ou $(\ln x)^2$ et $\ln x$.

**Les étapes**

1. Poser $X = e^x$ (avec $X > 0$) ou $X = \ln x$.
2. Résoudre l'équation du second degré en $X$.
3. Revenir à $x$ : $x = \ln X$ (seulement si $X > 0$) ou $x = e^X$.

**Exemple.** $e^{2x} - 3e^x + 2 = 0$. Avec $X = e^x$ : $X^2 - 3X + 2 = 0$, donc $X = 1$ ou $X = 2$. D'où $e^x = 1$ ou $e^x = 2$, soit $x = 0$ ou $x = \ln 2$.

---

## Méthode 4 — Étudier une fonction contenant $\ln$

**Les étapes**

1. Domaine de définition : ce qui est dans le $\ln$ doit être $> 0$.
2. Dérivée, avec $(\ln x)' = \frac{1}{x}$ et $(\ln u)' = \frac{u'}{u}$.
3. Signe de la dérivée : souvent, on **réduit au même dénominateur**, qui est positif.
4. Limites aux bornes, avec les croissances comparées si besoin.

**Exemple.** $f(x) = x - \ln x$ sur $]0 \,;\, +\infty[$ : $f'(x) = 1 - \dfrac{1}{x} = \dfrac{x - 1}{x}$, du signe de $x - 1$. $f$ est décroissante sur $]0 \,;\, 1]$ et croissante sur $[1 \,;\, +\infty[$, de minimum $f(1) = 1$.

---

## Méthode 5 — Lever une forme indéterminée avec $\ln$

**Les étapes**

1. Repérer le terme « le plus fort » : en $+\infty$, $x^n$ l'emporte sur $\ln x$.
2. Factoriser par ce terme pour faire apparaître $\dfrac{\ln x}{x^n}$, ou $x^n \ln x$ en $0$.
3. Conclure avec les croissances comparées.

**Exemple.** En $+\infty$, $x - \ln x$ est une forme $\infty - \infty$. On factorise par $x$ :

$$x - \ln x = x\left(1 - \frac{\ln x}{x}\right) \longrightarrow +\infty, \quad \text{car } \frac{\ln x}{x} \to 0.$$

**Changement de variable.** Pour $\sqrt{x}\ln x$ en $0^+$, on pose $X = \sqrt{x}$ : $\sqrt{x}\ln x = X\ln(X^2) = 2X\ln X \to 0$.

---

## Méthode 6 — Résoudre un problème de seuil

**Quand ?** On cherche le plus petit entier $n$ tel que $q^n < a$ (ou $> a$), avec $q > 0$.

**Les étapes**

1. Isoler la puissance : $q^n < a$.
2. Appliquer $\ln$ (strictement croissante) : $n\ln q < \ln a$.
3. Diviser par $\ln q$ en faisant **attention à son signe** : si $0 < q < 1$, $\ln q < 0$ et l'inégalité change de sens.
4. Conclure par le plus petit entier qui convient.

**Exemple.** $u_n = 3 \times 0{,}8^n$. On cherche $n$ tel que $u_n < 0{,}01$ :

$$0{,}8^n < \frac{1}{300} \iff n\ln 0{,}8 < -\ln 300 \iff n > \frac{\ln 300}{-\ln 0{,}8} \approx 25{,}6.$$

Le plus petit entier est $n = 26$.
