# Méthodes — Continuité

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Justifier qu'une fonction est continue

**Cas général.** On invoque les théorèmes : « $f$ est continue sur $I$ comme somme, produit, quotient (dénominateur non nul) ou composée de fonctions continues ». En pratique : **toute fonction dérivable est continue**.

**Fonction définie par morceaux.** Il faut vérifier la continuité **au point de raccord** $a$ : la limite à gauche, la limite à droite et $f(a)$ doivent être égales.

**Exemple.** $f(x) = x^2$ si $x \leq 1$ et $f(x) = 2x - 1$ si $x > 1$.

- Sur $]-\infty \,;\, 1[$ et sur $]1 \,;\, +\infty[$, $f$ est polynomiale donc continue.
- En $1$ : $\displaystyle\lim_{x\to 1^-} x^2 = 1$, $\displaystyle\lim_{x\to 1^+} (2x - 1) = 1$ et $f(1) = 1$. Donc $f$ est continue en $1$.

$f$ est continue sur $\mathbb{R}$.

---

## Méthode 2 — Appliquer le TVI ou son corollaire

**Rédaction type** pour montrer que $f(x) = k$ a une unique solution sur $[a \,;\, b]$ :

1. $f$ est **continue** sur $[a \,;\, b]$ (justifier).
2. $f$ est **strictement monotone** sur $[a \,;\, b]$ (étude du signe de $f'$).
3. $k$ est **compris entre** $f(a)$ et $f(b)$ (calculer les deux valeurs).
4. Conclure : « D'après le corollaire du théorème des valeurs intermédiaires, l'équation $f(x) = k$ admet une unique solution $\alpha$ dans $[a \,;\, b]$. »

Sur un intervalle ouvert ou infini, on remplace $f(a)$ et $f(b)$ par les **limites** aux bornes.

!!! warning "Les trois hypothèses sont nécessaires"
    Sans continuité, pas de TVI. Sans stricte monotonie, il peut y avoir plusieurs solutions. Si $k$ n'est pas entre $f(a)$ et $f(b)$, on ne peut rien conclure.

---

## Méthode 3 — Compter les solutions sur tout le domaine

**Les étapes**

1. Dresser le **tableau de variations complet** (limites et extremums).
2. Sur **chaque intervalle** où $f$ est strictement monotone, regarder si $k$ est compris entre les valeurs (ou limites) aux bornes.
3. Appliquer le corollaire du TVI sur chaque intervalle concerné, puis additionner.

**Exemple.** $f(x) = x^3 - 3x + 1$ : $f'(x) = 3(x - 1)(x + 1)$.

| $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $-\infty$ | $\nearrow$ | $3$ | $\searrow$ | $-1$ | $\nearrow$ | $+\infty$ |

$0$ est atteint une fois sur chacun des trois intervalles : l'équation $f(x) = 0$ a **trois** solutions.

---

## Méthode 4 — Encadrer une solution

**À la calculatrice (balayage).** On utilise le tableau de valeurs avec un pas de $0{,}1$, puis $0{,}01$… en repérant le **changement de signe**.

**Rédaction.** « $f(0{,}6) \approx -0{,}18 < 0$ et $f(0{,}7) \approx 0{,}04 > 0$, donc $0{,}6 < \alpha < 0{,}7$. »

**En Python (dichotomie).** Voir le cours, § 4.2. Pour une précision $p$ sur un intervalle de longueur $L$, il faut $n$ étapes avec $\frac{L}{2^n} \leq p$.

---

## Méthode 5 — Calculer la limite d'une suite $u_{n+1} = f(u_n)$

**Les étapes**

1. **Prouver la convergence**, souvent par le théorème de convergence monotone (monotonie et encadrement par récurrence).
2. Justifier que $f$ est **continue** en la limite $\ell$, et que $\ell$ est dans l'intervalle de travail.
3. Résoudre l'équation $f(\ell) = \ell$.
4. **Choisir** la bonne solution grâce aux encadrements de l'étape 1.

**Exemple.** Si $0 \leq u_n \leq 2$ et $u_{n+1} = \sqrt{u_n + 2}$, la limite vérifie $\ell^2 - \ell - 2 = 0$, donc $\ell = 2$ ou $\ell = -1$. Comme $\ell \in [0 \,;\, 2]$, on a $\ell = 2$.

!!! warning "Erreur grave"
    On ne peut **pas** commencer par résoudre $f(\ell) = \ell$ pour « trouver la limite » sans avoir prouvé que la suite converge : une suite peut très bien ne pas converger, même si $f$ a un point fixe (par exemple $u_{n+1} = 2u_n$ avec $u_0 = 1$, alors que $0$ est un point fixe).
