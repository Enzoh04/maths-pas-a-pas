# Méthodes — Sommes de variables aléatoires

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Calculer l'espérance d'une somme

**Les étapes**

1. Écrire la variable étudiée comme une **somme** (ou une combinaison linéaire) de variables plus simples.
2. Calculer l'espérance de chacune.
3. Additionner grâce à la **linéarité** : $E(aX + bY + c) = aE(X) + bE(Y) + c$. Aucune hypothèse d'indépendance n'est nécessaire.

**Exemple.** Un joueur joue à deux jeux. Au premier, son gain $X$ a pour espérance $1{,}5$ € ; au second, son gain $Y$ a pour espérance $-0{,}5$ €. Il paie $2$ € de droit d'entrée. Son gain total $G = X + Y - 2$ a pour espérance $E(G) = 1{,}5 - 0{,}5 - 2 = -1$ €.

---

## Méthode 2 — Déterminer la loi d'une somme de deux variables indépendantes

**Les étapes**

1. Justifier l'**indépendance** de $X$ et $Y$.
2. Construire un **tableau à double entrée** : en ligne les valeurs de $X$, en colonne celles de $Y$ ; dans chaque case, la somme $x + y$ et la probabilité $P(X = x)P(Y = y)$.
3. Regrouper les cases de même somme et additionner leurs probabilités.
4. Vérifier que la somme des probabilités vaut $1$, et contrôler l'espérance avec la linéarité.

**Exemple.** $X$ vaut $0$ ou $1$ avec probabilités $0{,}4$ et $0{,}6$ ; $Y$ vaut $0$, $1$ ou $2$ avec probabilités $0{,}5$, $0{,}3$, $0{,}2$ ; elles sont indépendantes.

| | $Y = 0$ ($0{,}5$) | $Y = 1$ ($0{,}3$) | $Y = 2$ ($0{,}2$) |
|---|---|---|---|
| $X = 0$ ($0{,}4$) | $0$ : $0{,}20$ | $1$ : $0{,}12$ | $2$ : $0{,}08$ |
| $X = 1$ ($0{,}6$) | $1$ : $0{,}30$ | $2$ : $0{,}18$ | $3$ : $0{,}12$ |

Donc $P(S = 0) = 0{,}20$, $P(S = 1) = 0{,}42$, $P(S = 2) = 0{,}26$, $P(S = 3) = 0{,}12$ (total $1$). Contrôle : $E(S) = 0{,}42 + 0{,}52 + 0{,}36 = 1{,}3 = E(X) + E(Y) = 0{,}6 + 0{,}7$.

---

## Méthode 3 — Calculer la variance d'une somme

**Les étapes**

1. **Vérifier l'indépendance** : c'est indispensable.
2. Utiliser $V(aX + bY + c) = a^2V(X) + b^2V(Y)$ (les constantes disparaissent, les coefficients sont **au carré**).
3. Pour l'écart type, calculer la variance d'abord, puis prendre la racine : les écarts types ne s'ajoutent pas.

**Exemple.** $X$ et $Y$ indépendantes, $V(X) = 4$, $V(Y) = 9$. Alors $V(X + Y) = 13$, $V(X - Y) = 13$, $V(2X - Y + 5) = 4 \times 4 + 9 = 25$, et $\sigma(2X - Y + 5) = 5$.

---

## Méthode 4 — Décomposer une variable de comptage

**Les étapes**

1. Pour une variable qui **compte** des événements $A_1, \ldots, A_n$, introduire les variables $X_i$ qui valent $1$ si $A_i$ est réalisé et $0$ sinon (variables **indicatrices**).
2. Écrire $X = X_1 + \cdots + X_n$.
3. $E(X_i) = P(A_i)$, donc par linéarité $E(X) = P(A_1) + \cdots + P(A_n)$.
4. Pour la variance, il faut en plus que les $X_i$ soient indépendantes ; alors $V(X) = \sum P(A_i)\big(1 - P(A_i)\big)$.

**Exemple.** On lance $6$ fois un dé et $X$ compte les faces qui ne sont **jamais** apparues. Pour chaque face $j$, $P(\text{la face } j \text{ n'apparaît pas}) = \left(\frac{5}{6}\right)^6$. Donc $E(X) = 6 \times \left(\frac{5}{6}\right)^6 \approx 2{,}01$. Ici les indicatrices ne sont pas indépendantes, mais la linéarité suffit pour l'espérance.

---

## Méthode 5 — Étudier un échantillon

**Les étapes**

1. Identifier la loi commune, $E(X)$ et $\sigma(X)$, et justifier l'indépendance.
2. Somme : $E(S_n) = nE(X)$ et $\sigma(S_n) = \sqrt{n}\,\sigma(X)$.
3. Moyenne : $E(M_n) = E(X)$ et $\sigma(M_n) = \dfrac{\sigma(X)}{\sqrt{n}}$.
4. Pour une précision voulue : résoudre $\dfrac{\sigma(X)}{\sqrt{n}} \leq \varepsilon$, soit $n \geq \left(\dfrac{\sigma(X)}{\varepsilon}\right)^2$.

**Exemple.** La masse d'un paquet de café a pour espérance $250$ g et pour écart type $4$ g, indépendamment d'un paquet à l'autre. Pour un carton de $25$ paquets : $E(S_{25}) = 6\,250$ g et $\sigma(S_{25}) = 5 \times 4 = 20$ g. La masse moyenne d'un paquet du carton a pour écart type $\frac{4}{5} = 0{,}8$ g.
