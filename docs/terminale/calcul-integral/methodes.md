# Méthodes — Calcul intégral

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Calculer une intégrale avec une primitive

**Les étapes**

1. Trouver une primitive $F$ de $f$ (chapitre 7), en reconnaissant au besoin une forme $u'e^u$, $\frac{u'}{u}$…
2. Écrire $\displaystyle\int_a^b f(x)\,\mathrm{d}x = \big[F(x)\big]_a^b = F(b) - F(a)$.
3. Simplifier (avec $\ln$, $e$… si besoin).

**Exemple.**

$$\int_0^1 \frac{2x}{x^2 + 1}\,\mathrm{d}x = \Big[\ln(x^2 + 1)\Big]_0^1 = \ln 2 - \ln 1 = \ln 2.$$

!!! warning "Erreur fréquente"
    On écrit bien $F(b) - F(a)$, **dans cet ordre**. Et on n'oublie pas $F(a)$, même quand il semble nul : ici $\ln 1 = 0$, mais pour $e^x$, $F(0) = 1$.

---

## Méthode 2 — Calculer une aire

**Les étapes**

1. Étudier le **signe** de $f$ (ou de $f - g$ pour une aire entre deux courbes) sur l'intervalle.
2. Découper l'intervalle aux points où le signe change (relation de Chasles).
3. Sur chaque morceau, l'aire vaut $\int f$ si $f \geq 0$, et $-\int f$ si $f \leq 0$.
4. Additionner et donner le résultat **en unités d'aire**.

**Exemple.** Aire entre les courbes de $y = x$ et $y = x^2$ sur $[0 \,;\, 1]$. Sur cet intervalle, $x - x^2 = x(1 - x) \geq 0$, donc la droite est au-dessus :

$$\mathcal{A} = \int_0^1 (x - x^2)\,\mathrm{d}x = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{6} \text{ u.a.}$$

**Conversion.** Si l'unité est de $2$ cm sur l'axe des abscisses et $3$ cm sur l'axe des ordonnées, 1 u.a. vaut $6$ cm².

---

## Méthode 3 — Intégrer par parties

**Quand ?** L'intégrande est un **produit** dont on ne reconnaît pas une forme $u'v'(u)$ : $xe^x$, $x\sin x$, $\ln x$ (vu comme $1 \times \ln x$)…

**Les étapes**

1. Choisir $u$ (qui se simplifie en dérivant) et $v'$ (dont on connaît une primitive).
2. Calculer $u'$ et $v$, et les écrire clairement.
3. Appliquer la formule et calculer la nouvelle intégrale.

**Exemple.** $\displaystyle\int_1^e \ln x\,\mathrm{d}x$. On pose $u(x) = \ln x$, $v'(x) = 1$, donc $u'(x) = \frac{1}{x}$ et $v(x) = x$ :

$$\int_1^e \ln x\,\mathrm{d}x = \big[x\ln x\big]_1^e - \int_1^e \frac{1}{x} \times x\,\mathrm{d}x = e - (e - 1) = 1.$$

---

## Méthode 4 — Encadrer une intégrale sans la calculer

**Quand ?** On ne connaît pas de primitive (par exemple de $e^{-x^2}$), ou on veut seulement le **signe** ou un **ordre de grandeur**.

**Les étapes**

1. Encadrer la fonction : $g(x) \leq f(x) \leq h(x)$ sur $[a \,;\, b]$, avec $g$ et $h$ simples (souvent des constantes, ou des polynômes).
2. Intégrer l'encadrement (propriété d'ordre, avec **$a \leq b$**).

**Exemple.** Pour $x \in [0 \,;\, 1]$, $1 \leq 1 + x^2 \leq 2$, donc $\frac{1}{2} \leq \frac{1}{1 + x^2} \leq 1$. D'où $\frac{1}{2} \leq \displaystyle\int_0^1 \frac{\mathrm{d}x}{1 + x^2} \leq 1$.

---

## Méthode 5 — Étudier une suite d'intégrales

**Exemple type.** $I_n = \displaystyle\int_0^1 x^n e^{-x}\,\mathrm{d}x$.

1. **Signe** : l'intégrande est positive et $0 \leq 1$, donc $I_n \geq 0$.
2. **Sens de variation** : on étudie $I_{n+1} - I_n = \displaystyle\int_0^1 x^n(x - 1)e^{-x}\,\mathrm{d}x$. Sur $[0 \,;\, 1]$, $x - 1 \leq 0$, donc $I_{n+1} - I_n \leq 0$ : la suite est décroissante.
3. **Limite** : on encadre l'intégrande. Comme $e^{-x} \leq 1$, on a $0 \leq I_n \leq \displaystyle\int_0^1 x^n\,\mathrm{d}x = \frac{1}{n + 1}$, d'où $I_n \to 0$ par les gendarmes.
4. **Relation de récurrence** : souvent par une intégration par parties (voir l'exercice 24).

---

## Méthode 6 — Valeur moyenne et méthode des rectangles

**Valeur moyenne.** On calcule $\mu = \dfrac{1}{b - a}\displaystyle\int_a^b f(x)\,\mathrm{d}x$ et on **interprète** dans le contexte : température moyenne, vitesse moyenne…

**Méthode des rectangles (Python).** Pour une fonction croissante, la somme des rectangles à gauche donne une **valeur par défaut**, et celle à droite une **valeur par excès**. L'écart entre les deux vaut $\frac{(b - a)(f(b) - f(a))}{n}$ : il suffit de choisir $n$ assez grand pour obtenir la précision voulue.
