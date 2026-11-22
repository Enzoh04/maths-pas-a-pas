# Méthodes — Suites numériques, modèles discrets

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**. Les exemples se font sans calculatrice, comme à l'épreuve anticipée.

---

## Méthode 1 — Calculer des termes

**Les étapes**

1. **Suite explicite** $u_n = f(n)$ : remplacer $n$ par la valeur voulue. Pour $u_{n+1}$, remplacer $n$ par $n + 1$ **partout**, avec des parenthèses.
2. **Suite récurrente** $u_{n+1} = f(u_n)$ : calculer les termes un par un à partir du premier.
3. En Python, stocker les termes dans une **liste**.

**Exemple.** $u_n = \dfrac{2n + 1}{n + 3}$. Alors $u_0 = \dfrac{1}{3}$, $u_2 = 1$, et
$$u_{n+1} = \frac{2(n+1) + 1}{(n+1) + 3} = \frac{2n + 3}{n + 4}.$$

**Exemple.** $v_0 = 1$ et $v_{n+1} = 2v_n + 3$. Alors $v_1 = 5$, $v_2 = 13$, $v_3 = 29$.

---

## Méthode 2 — Étudier le sens de variation

**Les étapes**

1. **Calculer $u_{n+1} - u_n$**, simplifier, puis étudier son signe (méthode la plus sûre).
2. Si tous les termes sont **strictement positifs** et s'écrivent avec des produits ou des puissances, comparer $\dfrac{u_{n+1}}{u_n}$ à $1$.
3. Si $u_n = f(n)$ avec $f$ dont on connaît les variations, utiliser $f$ sur $[0\,;\,+\infty[$.

**Exemple.** $u_n = n^2 - 6n$. On calcule $u_{n+1} - u_n = (n+1)^2 - 6(n+1) - n^2 + 6n = 2n - 5$. Ce nombre est négatif pour $n \leq 2$ et positif pour $n \geq 3$ : la suite décroît jusqu'au rang $3$, puis croît. Elle est croissante **à partir du rang $3$**.

**Exemple.** $w_n = \dfrac{3^n}{n + 1}$, à termes strictement positifs. $\dfrac{w_{n+1}}{w_n} = \dfrac{3^{n+1}}{n+2} \times \dfrac{n+1}{3^n} = \dfrac{3(n+1)}{n+2}$. Or $3(n + 1) \geq n + 2$ (car $2n + 1 \geq 0$), donc ce quotient est supérieur ou égal à $1$ : la suite est croissante.

---

## Méthode 3 — Montrer qu'une suite est arithmétique ou géométrique

**Les étapes**

1. **Arithmétique** : calculer $u_{n+1} - u_n$ et montrer que le résultat **ne dépend pas de $n$**. Ce nombre est la raison.
2. **Géométrique** : écrire $u_{n+1}$ sous la forme $q \times u_n$, avec $q$ qui ne dépend pas de $n$.
3. **Pour montrer qu'une suite n'est pas** arithmétique (ou géométrique), un **contre-exemple** suffit : trois termes consécutifs dont les différences (ou les quotients) ne sont pas égales.

**Exemple.** $u_n = 4 - 3n$ : $u_{n+1} - u_n = -3$, donc $(u_n)$ est arithmétique de raison $-3$.

**Exemple.** $v_n = 5 \times 2^{n+1}$ : $v_{n+1} = 5 \times 2^{n+2} = 2 \times 5 \times 2^{n+1} = 2\,v_n$, donc $(v_n)$ est géométrique de raison $2$, de premier terme $v_0 = 10$.

**Exemple.** $w_n = n^2$ : $w_0 = 0$, $w_1 = 1$, $w_2 = 4$, et $w_1 - w_0 = 1 \neq 3 = w_2 - w_1$ : $(w_n)$ n'est pas arithmétique.

---

## Méthode 4 — Exprimer $u_n$ en fonction de $n$

**Les étapes**

1. Identifier la nature de la suite (méthode 3), sa raison et un terme connu.
2. Appliquer $u_n = u_p + (n - p)\,r$ (arithmétique) ou $u_n = u_p \times q^{\,n-p}$ (géométrique).
3. Si l'on connaît deux termes, en déduire d'abord la raison.

**Exemple.** $(u_n)$ est géométrique, $u_2 = 12$ et $u_5 = 96$. Alors $u_5 = u_2 \times q^3$, donc $q^3 = 8$ et $q = 2$. Puis $u_0 = \dfrac{u_2}{q^2} = 3$, d'où $u_n = 3 \times 2^n$.

---

## Méthode 5 — Calculer une somme de termes

**Les étapes**

1. Identifier la suite et **compter les termes** : de $u_p$ à $u_n$, il y a $n - p + 1$ termes.
2. **Arithmétique** : nombre de termes $\times \dfrac{\text{premier} + \text{dernier}}{2}$.
3. **Géométrique** ($q \neq 1$) : premier terme $\times \dfrac{1 - q^{\text{nombre de termes}}}{1 - q}$.

**Exemple.** $S = 7 + 10 + 13 + \cdots + 61$. C'est une suite arithmétique de raison $3$, de premier terme $7$ ; $61 = 7 + 18 \times 3$, donc il y a $19$ termes. $S = 19 \times \dfrac{7 + 61}{2} = 19 \times 34 = 646$.

**Exemple.** $T = 3 + 6 + 12 + \cdots + 3 \times 2^9$ : suite géométrique de raison $2$, $10$ termes. $T = 3 \times \dfrac{1 - 2^{10}}{1 - 2} = 3 \times 1\,023 = 3\,069$.

---

## Méthode 6 — Modéliser une évolution et chercher un seuil

**Les étapes**

1. Repérer le type d'évolution : **même quantité ajoutée** (arithmétique) ou **même pourcentage** (géométrique, $q = 1 + t$).
2. Définir la suite : premier terme, relation de récurrence, puis formule explicite.
3. Pour un **seuil** (« à partir de quand… ? ») : calculer les termes successifs, ou écrire une boucle `while` en Python.

**Exemple.** Une ville compte $20\,000$ habitants et perd $2\,\%$ de sa population chaque année. On note $p_n$ la population l'année $n$. Chaque année, on multiplie par $1 - 0{,}02 = 0{,}98$ : $(p_n)$ est géométrique de raison $0{,}98$, et $p_n = 20\,000 \times 0{,}98^n$. Comme $0 < 0{,}98 < 1$, la population diminue.

Pour savoir quand elle passera sous $15\,000$ habitants :

```python
n = 0
p = 20000
while p >= 15000:
    p = 0.98 * p
    n = n + 1
print(n)    # 15
```
