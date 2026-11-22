# Cours — Combinatoire et dénombrement

[📄 Cours en PDF (version classique)](pdf/cours.pdf){ .md-button }
[📄 Cours complet avec toutes les démonstrations (PDF)](pdf/cours-complet.pdf){ .md-button }

!!! lecture "Comment lire les démonstrations"
    Chaque résultat est démontré dès que c'est possible avec les outils de Terminale.

    Sur le site, clique sur un bloc pour l'ouvrir.

    - **Démonstration — au programme du bac** : à savoir refaire, elle peut être demandée à l'examen.
    - **Démonstration — pour aller plus loin** : à comprendre, inutile de l'apprendre par cœur. Indispensable si tu vises des études de maths.
    - **Pourquoi ce résultat est admis** : la preuve demande une notion du supérieur, qui est indiquée.

---

## 1. Ensembles finis et principe additif

!!! definition "Cardinal"
    Un ensemble $E$ est **fini** s'il a un nombre fini d'éléments. Ce nombre s'appelle le **cardinal** de $E$, noté $\operatorname{Card}(E)$ ou $|E|$. Par convention, $\operatorname{Card}(\varnothing) = 0$.

**Exemple.** $E = \{a \,;\, b \,;\, c\}$ a pour cardinal $3$.

!!! propriete "Principe additif"
    Si $A$ et $B$ sont deux ensembles finis **disjoints** ($A \cap B = \varnothing$), alors

    $$\operatorname{Card}(A \cup B) = \operatorname{Card}(A) + \operatorname{Card}(B).$$

    Plus généralement, si $A_1, \dots, A_p$ sont deux à deux disjoints, le cardinal de leur réunion est la somme de leurs cardinaux.

??? admis "Pourquoi les principes de base sont admis"
    Compter, c'est mettre les éléments d'un ensemble en correspondance avec $\{1 \,;\, 2 \,;\, \dots \,;\, n\}$ : $E$ a $n$ éléments s'il existe une **bijection** entre $E$ et $\{1, \dots, n\}$. Avec cette définition, le principe additif et le principe multiplicatif (§ 2) se démontrent par récurrence, en L1. Au lycée, on les considère comme évidents : ils traduisent simplement ce que veut dire « compter ».

!!! propriete "Complémentaire et réunion quelconque"
    Soit $A$ et $B$ deux parties d'un ensemble fini $E$, et $\overline{A}$ le complémentaire de $A$ dans $E$.

    - $\operatorname{Card}(\overline{A}) = \operatorname{Card}(E) - \operatorname{Card}(A)$.
    - $\operatorname{Card}(A \cup B) = \operatorname{Card}(A) + \operatorname{Card}(B) - \operatorname{Card}(A \cap B)$.

??? demoplus "Démonstration — pour aller plus loin"
    $E$ est la réunion disjointe de $A$ et $\overline{A}$ : par le principe additif, $\operatorname{Card}(E) = \operatorname{Card}(A) + \operatorname{Card}(\overline{A})$.

    $A \cup B$ est la réunion disjointe de $A$ et de $B \setminus A$ (les éléments de $B$ qui ne sont pas dans $A$). Et $B$ est la réunion disjointe de $B \setminus A$ et de $A \cap B$. Donc $\operatorname{Card}(B \setminus A) = \operatorname{Card}(B) - \operatorname{Card}(A \cap B)$, puis $\operatorname{Card}(A \cup B) = \operatorname{Card}(A) + \operatorname{Card}(B) - \operatorname{Card}(A \cap B)$.

    *On soustrait $\operatorname{Card}(A \cap B)$ parce que les éléments communs ont été comptés deux fois.*

---

## 2. Produit cartésien et principe multiplicatif

!!! definition "Produit cartésien"
    Le **produit cartésien** $A \times B$ est l'ensemble des **couples** $(a, b)$ avec $a \in A$ et $b \in B$. Plus généralement, $A_1 \times \dots \times A_p$ est l'ensemble des **$p$-uplets** $(a_1, \dots, a_p)$, avec $a_i \in A_i$.

    On note $E^k = E \times \dots \times E$ ($k$ fois).

!!! propriete "Principe multiplicatif"
    $$\operatorname{Card}(A_1 \times \dots \times A_p) = \operatorname{Card}(A_1) \times \dots \times \operatorname{Card}(A_p).$$

**Interprétation.** Si un choix se fait en plusieurs étapes indépendantes, avec $n_1$ possibilités pour la première, $n_2$ pour la deuxième…, le nombre total de choix est $n_1 \times n_2 \times \dots$ On le visualise avec un **arbre**.

**Exemple.** Un menu avec 3 entrées, 4 plats et 2 desserts : $3 \times 4 \times 2 = 24$ menus.

!!! theoreme "Nombre de $k$-uplets"
    Si $\operatorname{Card}(E) = n$, le nombre de $k$-uplets d'éléments de $E$ (avec répétitions possibles) est

    $$\operatorname{Card}(E^k) = n^k.$$

??? demoplus "Démonstration — pour aller plus loin"
    C'est le principe multiplicatif avec $A_1 = \dots = A_k = E$. On peut aussi le démontrer par récurrence sur $k$ : $E^{k+1}$ est en bijection avec $E^k \times E$, donc $\operatorname{Card}(E^{k+1}) = n^k \times n = n^{k+1}$.

**Exemple.** Un code de carte bancaire (4 chiffres) : $10^4 = 10\,000$ codes possibles.

!!! theoreme "Nombre de parties d'un ensemble"
    Un ensemble à $n$ éléments possède exactement $2^n$ parties (sous-ensembles), en comptant $\varnothing$ et l'ensemble lui-même.

??? demoplus "Démonstration — pour aller plus loin"
    Numérotons les éléments $e_1, \dots, e_n$. À chaque partie $A$, on associe le $n$-uplet $(x_1, \dots, x_n)$ de $\{0 \,;\, 1\}^n$ défini par $x_i = 1$ si $e_i \in A$ et $x_i = 0$ sinon. Cette correspondance est une bijection : chaque partie donne un unique $n$-uplet, et chaque $n$-uplet de $0$ et de $1$ décrit une unique partie. Il y a donc autant de parties que de $n$-uplets de $\{0 \,;\, 1\}$, soit $2^n$.

    *Pour construire une partie, on décide, pour chaque élément, de le prendre ou non : deux choix, $n$ fois.*

---

## 3. Arrangements et permutations

!!! definition "Factorielle"
    Pour tout entier $n \geq 1$, on note $n! = 1 \times 2 \times \dots \times n$ (« factorielle $n$ »), et par convention $0! = 1$.

    $1! = 1$, $2! = 2$, $3! = 6$, $4! = 24$, $5! = 120$, $10! = 3\,628\,800$.

!!! theoreme "$k$-uplets d'éléments distincts (arrangements)"
    Si $\operatorname{Card}(E) = n$ et $0 \leq k \leq n$, le nombre de $k$-uplets d'éléments **deux à deux distincts** de $E$ est

    $$n \times (n - 1) \times \dots \times (n - k + 1) = \frac{n!}{(n - k)!}.$$

??? demoplus "Démonstration — pour aller plus loin"
    Pour construire un tel $k$-uplet, on a $n$ choix pour le premier élément, puis $n - 1$ pour le deuxième (il doit être différent du premier)… et $n - k + 1$ pour le $k$-ième. Par le principe multiplicatif, il y en a $n(n - 1)\cdots(n - k + 1)$. En multipliant et divisant par $(n - k)! = (n - k)(n - k - 1)\cdots 1$, on obtient $\frac{n!}{(n - k)!}$.

**Exemple.** Podium d'une course à 10 coureurs (or, argent, bronze) : $10 \times 9 \times 8 = 720$ podiums.

!!! theoreme "Permutations"
    Une **permutation** de $E$ est un $n$-uplet de ses $n$ éléments, tous distincts : c'est une façon de les **ranger**. Il y en a

    $$n!.$$

??? demoplus "Démonstration — pour aller plus loin"
    C'est le théorème précédent avec $k = n$ : $\frac{n!}{0!} = n!$.

**Exemple.** Les anagrammes du mot MATHS (lettres toutes différentes) : $5! = 120$.

---

## 4. Combinaisons

### 4.1 Définition et formule

!!! definition "Combinaison"
    Soit $E$ un ensemble à $n$ éléments et $k$ un entier avec $0 \leq k \leq n$. Une **combinaison** de $k$ éléments de $E$ est une **partie** de $E$ à $k$ éléments : l'**ordre ne compte pas**, et il n'y a pas de répétition.

    Leur nombre est noté $\displaystyle\binom{n}{k}$ (« $k$ parmi $n$ »). On l'appelle **coefficient binomial**.

**Exemple.** Les parties à 2 éléments de $\{a \,;\, b \,;\, c\}$ sont $\{a, b\}$, $\{a, c\}$ et $\{b, c\}$ : $\binom{3}{2} = 3$.

!!! theoreme "Formule des coefficients binomiaux"
    $$\binom{n}{k} = \frac{n!}{k!\,(n - k)!} = \frac{n(n - 1)\cdots(n - k + 1)}{k!}.$$

??? demoplus "Démonstration — pour aller plus loin"
    On compte les $k$-uplets d'éléments distincts de deux façons.

    - Directement : il y en a $\frac{n!}{(n - k)!}$ (§ 3).
    - En deux étapes : on choisit d'abord la **partie** formée des $k$ éléments ($\binom{n}{k}$ choix), puis l'**ordre** dans lequel on les range ($k!$ choix). Par le principe multiplicatif, il y en a $\binom{n}{k} \times k!$.

    Donc $\binom{n}{k} \times k! = \frac{n!}{(n - k)!}$, d'où la formule.

**Exemples.** $\binom{5}{2} = \frac{5 \times 4}{2} = 10$ ; $\binom{52}{5} = 2\,598\,960$ mains de 5 cartes dans un jeu de 52.

### 4.2 Propriétés

!!! propriete "Valeurs particulières et symétrie"
    Pour $0 \leq k \leq n$ :

    $$\binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{1} = n, \qquad \binom{n}{k} = \binom{n}{n - k}.$$

??? demoplus "Démonstration — pour aller plus loin"
    Il y a une seule partie à $0$ élément ($\varnothing$), une seule à $n$ éléments ($E$), et $n$ parties à un élément (les singletons).

    **Symétrie.** À chaque partie $A$ à $k$ éléments, on associe son complémentaire $\overline{A}$, qui a $n - k$ éléments. Cette correspondance est une bijection (on retrouve $A$ comme complémentaire de $\overline{A}$) : il y a donc autant de parties à $k$ éléments que de parties à $n - k$ éléments. *On peut aussi le voir sur la formule, qui est symétrique en $k$ et $n - k$.*

!!! theoreme "Relation de Pascal"
    Pour $1 \leq k \leq n - 1$ :

    $$\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}.$$

??? demo "Démonstration — au programme du bac (par le calcul)"
    On met au même dénominateur $k!\,(n - k)!$ :

    $$\binom{n - 1}{k - 1} + \binom{n - 1}{k} = \frac{(n - 1)!}{(k - 1)!\,(n - k)!} + \frac{(n - 1)!}{k!\,(n - 1 - k)!} = \frac{(n - 1)!\,k}{k!\,(n - k)!} + \frac{(n - 1)!\,(n - k)}{k!\,(n - k)!}.$$

    La somme vaut $\dfrac{(n - 1)!\,\big(k + (n - k)\big)}{k!\,(n - k)!} = \dfrac{n!}{k!\,(n - k)!} = \dbinom{n}{k}$.

??? demo "Démonstration — au programme du bac (par dénombrement)"
    Soit $E$ un ensemble à $n$ éléments et $a$ un élément fixé de $E$. Les parties de $E$ à $k$ éléments se répartissent en deux catégories disjointes :

    - celles qui **contiennent** $a$ : il reste à choisir $k - 1$ éléments parmi les $n - 1$ autres, soit $\binom{n - 1}{k - 1}$ parties ;
    - celles qui **ne contiennent pas** $a$ : on choisit les $k$ éléments parmi les $n - 1$ autres, soit $\binom{n - 1}{k}$ parties.

    Par le principe additif, $\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}$.

**Le triangle de Pascal.** La relation de Pascal permet de calculer les coefficients ligne par ligne : chaque nombre est la somme des deux nombres situés au-dessus de lui (au-dessus et au-dessus à gauche).

| $n \backslash k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $0$ | $1$ | | | | | |
| $1$ | $1$ | $1$ | | | | |
| $2$ | $1$ | $2$ | $1$ | | | |
| $3$ | $1$ | $3$ | $3$ | $1$ | | |
| $4$ | $1$ | $4$ | $6$ | $4$ | $1$ | |
| $5$ | $1$ | $5$ | $10$ | $10$ | $5$ | $1$ |

!!! theoreme "Somme des coefficients binomiaux"
    $$\sum_{k=0}^{n} \binom{n}{k} = \binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{n} = 2^n.$$

??? demo "Démonstration — au programme du bac (par dénombrement)"
    On compte les parties d'un ensemble $E$ à $n$ éléments de deux façons.

    - On sait qu'il y en a $2^n$ (§ 2).
    - On les classe selon leur nombre d'éléments $k$, de $0$ à $n$ : ces catégories sont disjointes, et la catégorie $k$ contient $\binom{n}{k}$ parties. Par le principe additif, il y a $\sum_{k=0}^{n}\binom{n}{k}$ parties.

    Les deux nombres sont égaux. *Ce type de raisonnement, où l'on compte le même ensemble de deux façons, s'appelle un **double dénombrement**.*

---

## 5. Choisir le bon modèle

On tire $k$ objets parmi $n$. Deux questions décident du modèle : **l'ordre compte-t-il ?** **Peut-on reprendre le même objet ?**

| Situation | Ordre | Répétition | Modèle | Nombre |
|---|---|---|---|---|
| Tirages successifs **avec remise** | oui | oui | $k$-uplets | $n^k$ |
| Tirages successifs **sans remise** | oui | non | arrangements | $\dfrac{n!}{(n - k)!}$ |
| Tirage **simultané** | non | non | combinaisons | $\dbinom{n}{k}$ |
| Rangement de $n$ objets | oui | non | permutations | $n!$ |

**Exemples.**

- Un mot de passe de 6 lettres minuscules : $26^6$ (ordre et répétitions).
- Le podium d'une course : $\frac{10!}{7!}$ (ordre, pas de répétition).
- Une main de cartes, une équipe, un comité : $\binom{n}{k}$ (pas d'ordre).

---

## 6. Pour aller plus loin

!!! propriete "Formule du binôme de Newton"
    Pour tous nombres $a$ et $b$ et tout entier $n \geq 0$ :

    $$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n - k}.$$

??? demoplus "Démonstration — pour aller plus loin"
    En développant $(a + b)^n = (a + b)(a + b)\cdots(a + b)$, on obtient une somme de produits : dans chacun des $n$ facteurs, on choisit soit $a$, soit $b$. Le produit vaut $a^kb^{n-k}$ quand on a choisi $a$ dans exactement $k$ facteurs. Il y a $\binom{n}{k}$ façons de choisir ces $k$ facteurs. Le terme $a^kb^{n-k}$ apparaît donc $\binom{n}{k}$ fois.

    *Avec $a = b = 1$, on retrouve $\sum \binom{n}{k} = 2^n$.*

- **Principe des tiroirs** : si l'on range $n + 1$ objets dans $n$ tiroirs, un tiroir contient au moins deux objets. Ce principe, évident, permet des démonstrations surprenantes (exercice 27).
- **Lien avec les probabilités** : dans une situation d'équiprobabilité, une probabilité se calcule comme le quotient de deux dénombrements (chapitre 13), et les coefficients $\binom{n}{k}$ apparaissent dans la **loi binomiale**.

!!! success "Tu as fini le cours"
    Passe aux [méthodes](methodes.md), puis entraîne-toi avec les [exercices corrigés](exercices.md).
