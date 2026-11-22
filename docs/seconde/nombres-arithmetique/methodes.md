# Méthodes — Nombres, ensembles et arithmétique

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Déterminer le plus petit ensemble auquel appartient un nombre

**Les étapes**

1. **Simplifier** le nombre : calculer, réduire la fraction, simplifier la racine.
2. Tester dans l'ordre : est-il entier naturel ? entier relatif ? décimal (fraction dont le dénominateur irréductible ne contient que des facteurs $2$ et $5$) ? rationnel ?
3. Une racine carrée d'un entier qui n'est pas un carré parfait est irrationnelle.

**Exemples.**

- $\frac{-36}{4} = -9 \in \mathbb{Z}$ (et $\notin \mathbb{N}$).
- $\frac{7}{20} = \frac{35}{100} = 0{,}35 \in \mathbb{D}$ : $20 = 2^2 \times 5$.
- $\frac{5}{12} \in \mathbb{Q}$ mais $\notin \mathbb{D}$ : $12 = 2^2 \times 3$ contient le facteur $3$.
- $\sqrt{49} = 7 \in \mathbb{N}$, mais $\sqrt{8} = 2\sqrt{2}$ est irrationnel.

---

## Méthode 2 — Utiliser les intervalles

**Les étapes**

1. Traduire chaque inégalité en intervalle (crochet tourné vers le nombre s'il est inclus).
2. Pour une **intersection**, garder la partie commune : on prend la plus grande des bornes de gauche et la plus petite des bornes de droite.
3. Pour une **réunion**, si les intervalles se chevauchent, on prend la plus petite borne de gauche et la plus grande de droite ; sinon on laisse le symbole $\cup$.
4. Faire un **schéma** sur une droite graduée en cas de doute.

**Exemple.** $I = ]-\infty\,;\,4]$ et $J = ]-1\,;\,6[$. $I \cap J = ]-1\,;\,4]$ et $I \cup J = ]-\infty\,;\,6[$.

---

## Méthode 3 — Utiliser la valeur absolue comme une distance

**Les étapes**

1. Écrire l'expression sous la forme $|x - a|$ (attention : $|x + 2| = |x - (-2)|$).
2. Interpréter : distance entre $x$ et $a$.
3. Conclure : $|x - a| \leq r \iff x \in [a - r\,;\,a + r]$ ; $|x - a| = r \iff x = a - r$ ou $x = a + r$ ; $|x - a| > r \iff x \in ]-\infty\,;\,a - r[ \cup ]a + r\,;\,+\infty[$.

**Exemple.** Résoudre $|x + 2| = 5$ : les réels à distance $5$ de $-2$ sont $-7$ et $3$.

**Exemple.** Écrire $[3\,;\,11]$ avec une valeur absolue : centre $\frac{3 + 11}{2} = 7$, rayon $\frac{11 - 3}{2} = 4$, donc $x \in [3\,;\,11] \iff |x - 7| \leq 4$.

---

## Méthode 4 — Démontrer une propriété sur les entiers

**Les étapes**

1. Traduire les hypothèses avec des **lettres** : « $n$ est pair » $\to$ $n = 2k$ ; « $n$ est impair » $\to$ $n = 2k + 1$ ; « $b$ est multiple de $a$ » $\to$ $b = ka$. Utiliser des lettres **différentes** pour des nombres différents.
2. Calculer l'expression demandée.
3. La mettre sous la forme voulue ($2 \times \text{entier}$, $2 \times \text{entier} + 1$, $a \times \text{entier}$) et **préciser que le facteur est un entier**.

**Exemple.** *La somme de deux entiers impairs est paire.* Soit $m = 2k + 1$ et $n = 2k' + 1$. Alors $m + n = 2k + 2k' + 2 = 2(k + k' + 1)$, et $k + k' + 1$ est un entier : $m + n$ est pair.

!!! warning "Un exemple n'est pas une démonstration"
    Vérifier que $3 + 5 = 8$ est pair ne prouve rien pour **tous** les impairs. En revanche, **un seul contre-exemple** suffit à montrer qu'une affirmation est fausse.

---

## Méthode 5 — Décomposer en facteurs premiers et simplifier

**Les étapes**

1. Diviser le nombre par $2$ autant que possible, puis par $3$, $5$, $7$, $11$… (on peut s'arrêter quand le carré du diviseur testé dépasse le quotient restant).
2. Écrire la décomposition avec des puissances.
3. Pour simplifier une fraction, décomposer numérateur et dénominateur et barrer les facteurs communs.

**Exemple.** $504 = 2 \times 252 = 2^2 \times 126 = 2^3 \times 63 = 2^3 \times 3^2 \times 7$. $\frac{504}{660}$ : $660 = 2^2 \times 3 \times 5 \times 11$, donc
$$\frac{504}{660} = \frac{2^3 \times 3^2 \times 7}{2^2 \times 3 \times 5 \times 11} = \frac{2 \times 3 \times 7}{5 \times 11} = \frac{42}{55}.$$
