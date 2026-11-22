# Vocabulaire ensembliste et logique

Cette partie du programme n'est pas un chapitre à part : elle se travaille **tout au long de l'année**, dans tous les chapitres. Cette page rassemble l'essentiel, avec des exemples tirés du programme de Première et quelques exercices corrigés.

---

## 1. Ensembles

| Notation | Se lit | Exemple |
|---|---|---|
| $x \in E$ | $x$ appartient à $E$ | $\sqrt{2} \in \mathbb{R}$, $\sqrt{2} \notin \mathbb{Q}$ |
| $A \subset B$ | $A$ est inclus dans $B$ | $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ |
| $A \cap B$ | $A$ inter $B$ : les éléments **communs** | $[0\,;\,5] \cap [3\,;\,8] = [3\,;\,5]$ |
| $A \cup B$ | $A$ union $B$ : les éléments de $A$ **ou** de $B$ | $[0\,;\,5] \cup [3\,;\,8] = [0\,;\,8]$ |
| $\overline{A}$ | complémentaire de $A$ (dans un ensemble $E$) | dans $\mathbb{R}$, $\overline{[0\,;\,+\infty[} = ]-\infty\,;\,0[$ |
| $\varnothing$ | ensemble vide | $[0\,;\,1] \cap [2\,;\,3] = \varnothing$ |
| $E \times F$ | produit cartésien : les couples $(x\,;\,y)$ | les issues de deux lancers de dé forment $\{1, \ldots, 6\} \times \{1, \ldots, 6\}$ |

!!! tip "Le « ou » des mathématiciens"
    En mathématiques, « $A$ ou $B$ » est **inclusif** : il est vrai quand l'un des deux est vrai, **ou les deux**. C'est pourquoi $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ : on retire ce qui est compté deux fois.

Le **cardinal** d'un ensemble fini $E$, noté $\operatorname{card}(E)$, est son nombre d'éléments. On a $\operatorname{card}(E \times F) = \operatorname{card}(E) \times \operatorname{card}(F)$.

---

## 2. Propositions, implication, équivalence

Une **proposition** est un énoncé qui est soit vrai, soit faux.

!!! definition "Implication"
    « $P \Rightarrow Q$ » (« si $P$, alors $Q$ ») est vraie lorsque, **chaque fois** que $P$ est vraie, $Q$ l'est aussi. On dit que $P$ est une **condition suffisante** pour $Q$, et que $Q$ est une **condition nécessaire** pour $P$.

!!! definition "Réciproque, contraposée"
    - La **réciproque** de $P \Rightarrow Q$ est $Q \Rightarrow P$. Elle peut être fausse même si l'implication est vraie.
    - La **contraposée** de $P \Rightarrow Q$ est $\text{non}\,Q \Rightarrow \text{non}\,P$. Elle a **toujours** la même valeur de vérité que l'implication.

**Exemple.** « Si $f$ est dérivable en $a$, alors $f$ est continue en $a$ » est vraie. Sa réciproque est fausse : la fonction valeur absolue est continue en $0$ sans y être dérivable. Sa contraposée : « si $f$ n'est pas continue en $a$, elle n'y est pas dérivable ».

!!! definition "Équivalence"
    « $P \iff Q$ » signifie que $P \Rightarrow Q$ **et** $Q \Rightarrow P$ : $P$ est une condition **nécessaire et suffisante** pour $Q$.

**Exemple.** Pour des vecteurs : $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$ ([chapitre 7](../produit-scalaire/cours.md)).

!!! warning "Attention aux équivalences abusives"
    $x^2 = 4 \Rightarrow x = 2$ est **faux** ($x$ peut valoir $-2$). On écrit $x^2 = 4 \iff (x = 2 \text{ ou } x = -2)$. Avant d'écrire $\iff$, vérifier les deux sens !

**Négations.** La négation de « $P$ et $Q$ » est « non $P$ ou non $Q$ » ; la négation de « $P$ ou $Q$ » est « non $P$ et non $Q$ ». La négation de « $x \geq 3$ » est « $x < 3$ ».

---

## 3. Quantificateurs

- « **Pour tout** $x$ » se note $\forall x$ : la propriété doit être vraie pour chaque $x$.
- « **Il existe** $x$ » se note $\exists x$ : il suffit d'un $x$ qui convient.

**Exemples.** « Pour tout réel $x$, $e^x > 0$ » est vraie. « Il existe un réel $x$ tel que $x^2 = -1$ » est fausse.

!!! tip "Nier une phrase quantifiée"
    La négation de « pour tout $x$, $P(x)$ » est « il existe $x$ tel que non $P(x)$ ». Pour montrer qu'une phrase « pour tout » est fausse, **un seul contre-exemple** suffit.

---

## 4. Types de raisonnement

!!! definition "Raisonnement par disjonction des cas"
    On sépare l'étude en plusieurs cas qui recouvrent toutes les possibilités, et on démontre le résultat dans chaque cas.

**Exemple.** *Pour tout entier $n$, $n(n + 1)$ est pair.* Si $n$ est pair, $n(n + 1)$ est un multiple de $n$, donc pair. Si $n$ est impair, $n + 1$ est pair, donc le produit aussi.

!!! definition "Raisonnement par contraposée"
    Pour démontrer $P \Rightarrow Q$, on démontre $\text{non}\,Q \Rightarrow \text{non}\,P$, parfois plus facile.

**Exemple.** *Si $n^2$ est pair, alors $n$ est pair.* Contraposée : si $n$ est impair, $n = 2k + 1$, alors $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$ est impair.

!!! definition "Raisonnement par l'absurde"
    On suppose que le résultat est faux et on aboutit à une contradiction.

**Exemple.** *$\sqrt{2}$ n'est pas rationnel.* Supposons $\sqrt{2} = \frac{p}{q}$ avec une fraction **irréductible**. Alors $p^2 = 2q^2$ est pair, donc $p$ est pair (exemple précédent) : $p = 2k$. Alors $4k^2 = 2q^2$, $q^2 = 2k^2$ est pair, donc $q$ est pair. $p$ et $q$ sont tous deux pairs : la fraction n'était pas irréductible. Contradiction.

!!! definition "Contre-exemple"
    Pour montrer qu'une affirmation générale est fausse, il suffit d'exhiber **un** cas où elle ne marche pas.

**Exemple.** « Toute suite croissante tend vers $+\infty$ » est fausse : $u_n = 1 - \frac{1}{n + 1}$ est croissante et reste inférieure à $1$.

---

## 5. Exercices corrigés

### Exercice 1 — Intervalles <span class="etoiles">★</span>

Écrire plus simplement : $[-2\,;\,4] \cap ]1\,;\,7]$ ; $[-2\,;\,4] \cup ]1\,;\,7]$ ; $\mathbb{R} \setminus [0\,;\,3[$ (les réels qui ne sont pas dans $[0\,;\,3[$).

??? success "Correction"
    $]1\,;\,4]$ ; $[-2\,;\,7]$ ; $]-\infty\,;\,0[ \cup [3\,;\,+\infty[$.

### Exercice 2 — Vrai ou faux ? <span class="etoiles">★</span>

Dire si chaque proposition est vraie ou fausse, et écrire sa réciproque. La réciproque est-elle vraie ?

1. Si $x = 3$, alors $x^2 = 9$.
2. Si un quadrilatère est un carré, alors ses diagonales sont perpendiculaires.
3. Si $u_{n+1} - u_n = 2$ pour tout $n$, alors $(u_n)$ est arithmétique.

??? success "Correction"
    1. Vraie. Réciproque « si $x^2 = 9$, alors $x = 3$ » : fausse ($x = -3$).
    2. Vraie. Réciproque fausse : un losange non carré a des diagonales perpendiculaires.
    3. Vraie. Réciproque « si $(u_n)$ est arithmétique, alors $u_{n+1} - u_n = 2$ » : fausse (la raison peut être différente de $2$).

### Exercice 3 — Condition nécessaire, suffisante <span class="etoiles">★★</span>

Compléter par « nécessaire », « suffisante » ou « nécessaire et suffisante ».

1. Pour qu'un entier soit divisible par $6$, il est … qu'il soit pair.
2. Pour que $\Delta > 0$, il est … que l'équation $ax^2 + bx + c = 0$ ait deux solutions distinctes.
3. Pour que $x > 2$, il est … que $x > 5$.

??? success "Correction"
    1. Nécessaire (mais pas suffisante : $4$ est pair et non divisible par $6$).
    2. Nécessaire et suffisante.
    3. Suffisante ($x > 5 \Rightarrow x > 2$).

### Exercice 4 — Négations <span class="etoiles">★★</span>

Écrire la négation de chaque phrase, puis dire laquelle est vraie.

1. « Pour tout réel $x$, $x^2 > 0$. »
2. « Il existe un entier $n$ tel que $n^2 = 2$. »
3. « Pour tout $n$, $u_n \leq 10$. »

??? success "Correction"
    1. « Il existe un réel $x$ tel que $x^2 \leq 0$ » : vraie ($x = 0$). La phrase initiale est fausse.
    2. « Pour tout entier $n$, $n^2 \neq 2$ » : vraie.
    3. « Il existe $n$ tel que $u_n > 10$ » : cela dépend de la suite.

### Exercice 5 — Raisonnements <span class="etoiles">★★★</span>

1. Par disjonction des cas, montrer que pour tout entier $n$, $n^2 + n + 1$ est impair.
2. Par contraposée, montrer que si $n^2$ est multiple de $3$, alors $n$ est multiple de $3$. *(On écrira $n = 3k + 1$ ou $n = 3k + 2$.)*
3. Par l'absurde, montrer que $\sqrt{3}$ n'est pas rationnel.

??? success "Correction"
    1. $n^2 + n = n(n + 1)$ est pair (voir le cours), donc $n^2 + n + 1$ est impair.
    2. Si $n$ n'est pas multiple de $3$ : $n = 3k + 1$ donne $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$ ; $n = 3k + 2$ donne $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. Dans les deux cas, $n^2$ n'est pas multiple de $3$.
    3. Si $\sqrt{3} = \frac{p}{q}$ irréductible, $p^2 = 3q^2$ est multiple de $3$, donc $p = 3k$ (question 2) ; alors $9k^2 = 3q^2$, $q^2 = 3k^2$, donc $q$ est multiple de $3$ : contradiction avec l'irréductibilité.

[Retour à la page Première](../index.md)
