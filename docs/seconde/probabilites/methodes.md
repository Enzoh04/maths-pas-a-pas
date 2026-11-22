# Méthodes — Probabilités

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Calculer une probabilité en situation d'équiprobabilité

**Les étapes**

1. Justifier l'équiprobabilité (dé équilibré, tirage au hasard…).
2. Compter le nombre total d'issues.
3. Compter les issues favorables à l'événement.
4. $P(A) = \frac{\text{favorables}}{\text{total}}$, à simplifier.

**Exemple.** On choisit au hasard un nombre entier entre $1$ et $50$. Probabilité qu'il soit multiple de $7$ : les multiples sont $7, 14, \ldots, 49$, soit $7$ nombres. $P = \frac{7}{50} = 0{,}14$.

---

## Méthode 2 — Utiliser le contraire, la réunion et l'intersection

**Les étapes**

1. Traduire l'énoncé : « au moins un » $\to$ souvent le **contraire** de « aucun » ; « ou » $\to$ **réunion** ; « et » $\to$ **intersection**.
2. Appliquer $P\left(\overline{A}\right) = 1 - P(A)$ ou $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
3. Vérifier que le résultat est entre $0$ et $1$.

**Exemple.** Dans une classe, $60\,\%$ des élèves font de l'anglais renforcé ($A$), $30\,\%$ du théâtre ($T$), et $15\,\%$ les deux. Probabilité qu'un élève choisi au hasard fasse l'un ou l'autre : $0{,}6 + 0{,}3 - 0{,}15 = 0{,}75$. Probabilité qu'il ne fasse aucun des deux : $1 - 0{,}75 = 0{,}25$.

---

## Méthode 3 — Utiliser un tableau à double entrée ou un arbre

**Les étapes**

1. Pour deux épreuves, construire un **tableau** (si les deux épreuves sont du même type, comme deux dés) ou un **arbre** (si l'ordre ou le « sans remise » compte).
2. S'assurer que les cases ou les chemins sont **équiprobables** (numéroter les objets identiques si besoin).
3. Compter les cases ou chemins favorables.

**Exemple.** On lance deux pièces équilibrées. Arbre : $PP$, $PF$, $FP$, $FF$, quatre chemins équiprobables. $P(\text{« au moins un pile »}) = \frac{3}{4}$ (ou $1 - P(FF) = 1 - \frac{1}{4}$).

!!! warning "Attention à l'équiprobabilité"
    Les résultats « deux piles », « un pile », « zéro pile » ne sont **pas** équiprobables : « un pile » a deux chemins ($PF$ et $FP$), donc une probabilité $\frac{1}{2}$.

---

## Méthode 4 — Calculer une probabilité conditionnelle avec un tableau

**Les étapes**

1. Repérer l'événement **connu** (« sachant que », « parmi », « si ») : c'est la nouvelle population de référence.
2. Diviser l'effectif de la case « les deux » par le **total de la ligne ou de la colonne** de l'événement connu.
3. Si le tableau n'est pas donné, en construire un avec un effectif total commode ($1\,000$ ou $10\,000$).

**Exemple.** $30\,\%$ des clients d'un magasin ont une carte de fidélité ; $40\,\%$ d'entre eux achètent en promotion, contre $20\,\%$ des autres. Sur $1\,000$ clients : $300$ avec carte, dont $120$ en promotion ; $700$ sans carte, dont $140$ en promotion. Probabilité qu'un client achetant en promotion ait une carte : $\frac{120}{260} = \frac{6}{13} \approx 0{,}46$.

---

## Méthode 5 — Construire et utiliser un arbre pondéré

**Les étapes**

1. Au premier niveau, l'événement dont la probabilité est donnée **sans condition**.
2. Au second niveau, les probabilités **conditionnelles** (« parmi les … »).
3. Les branches issues d'un même nœud ont une somme égale à $1$.
4. La probabilité d'un chemin est le **produit** des probabilités de ses branches ; la probabilité d'un événement s'obtient en **additionnant** les chemins qui y mènent.

**Exemple (suite).** $P(\text{carte et promotion}) = 0{,}3 \times 0{,}4 = 0{,}12$ ; $P(\text{sans carte et promotion}) = 0{,}7 \times 0{,}2 = 0{,}14$. Probabilité qu'un client achète en promotion : $0{,}12 + 0{,}14 = 0{,}26$.
