# Méthodes — Succession d'épreuves indépendantes, loi binomiale

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Justifier qu'une variable suit une loi binomiale

**Les étapes**

1. Identifier l'**épreuve** répétée et ses **deux issues** : préciser ce qu'est le succès.
2. Donner la **probabilité $p$** du succès.
3. Justifier que les répétitions sont **identiques et indépendantes** (tirage avec remise, ou population assez grande pour assimiler le tirage à un tirage avec remise, ou hypothèse de l'énoncé).
4. Préciser que $X$ **compte le nombre de succès** parmi les $n$ répétitions.
5. Conclure : $X \sim \mathcal{B}(n, p)$.

**Exemple.** Un tireur atteint la cible avec probabilité $0{,}7$, indépendamment d'un tir à l'autre. Il tire $8$ fois et $X$ est le nombre de tirs réussis. « Chaque tir est une épreuve à deux issues, le succès "la cible est atteinte" ayant pour probabilité $0{,}7$. On répète $8$ fois cette épreuve de façon identique et indépendante, et $X$ compte le nombre de succès : $X$ suit la loi $\mathcal{B}(8\,;\,0{,}7)$. »

!!! warning "Les pièges"
    - Tirage **sans remise** dans une petite urne : les épreuves ne sont pas indépendantes, ce n'est pas une loi binomiale.
    - Probabilité de succès **différente** d'une épreuve à l'autre : pas de loi binomiale (on revient à l'arbre, méthode 5).
    - Variable qui ne compte pas des succès (par exemple, le rang du premier succès) : pas de loi binomiale.

---

## Méthode 2 — Calculer des probabilités binomiales

**Les étapes**

1. Traduire l'événement avec $X$ : « exactement », « au plus » ($\leq$), « au moins » ($\geq$), « moins de » ($<$), « plus de » ($>$).
2. Se ramener à $P(X = k)$ ou $P(X \leq k)$, seules quantités données par la calculatrice :
   - $P(X \geq k) = 1 - P(X \leq k - 1)$ ;
   - $P(a \leq X \leq b) = P(X \leq b) - P(X \leq a - 1)$.
3. Pour $P(X = k)$ à la main : $\binom{n}{k}p^k(1 - p)^{n-k}$.
4. Arrondir comme demandé (souvent à $10^{-3}$).

**Exemple.** $X \sim \mathcal{B}(8\,;\,0{,}7)$. Probabilité d'au moins $6$ réussites :
$$P(X \geq 6) = 1 - P(X \leq 5) \approx 1 - 0{,}448 = 0{,}552.$$
Probabilité d'exactement $8$ réussites : $0{,}7^8 \approx 0{,}058$.

---

## Méthode 3 — Utiliser l'espérance et la variance

**Les étapes**

1. Appliquer $E(X) = np$ et $V(X) = np(1 - p)$, $\sigma(X) = \sqrt{V(X)}$.
2. **Interpréter** $E(X)$ : « en moyenne, sur un grand nombre de répétitions, on obtient environ $np$ succès ».
3. Si une autre grandeur s'écrit $Y = aX + b$ (un gain, un score), utiliser les règles de Première : $E(Y) = aE(X) + b$ et $V(Y) = a^2V(X)$.

**Exemple.** Un jeu consiste à lancer $10$ fois une pièce équilibrée. On gagne $2$ € par Pile, et l'on a payé $12$ € pour jouer. Le gain est $G = 2X - 12$ avec $X \sim \mathcal{B}(10\,;\,0{,}5)$. Alors $E(G) = 2 \times 5 - 12 = -2$ : en moyenne, on perd $2$ € par partie. Le jeu est défavorable au joueur.

---

## Méthode 4 — Résoudre un problème de seuil

**Les étapes**

1. Écrire la probabilité de **l'événement contraire** : « au moins un succès » a pour contraire « aucun succès », de probabilité $(1 - p)^n$.
2. Écrire l'inéquation en $n$.
3. Résoudre avec le logarithme, **en changeant le sens** de l'inégalité quand on divise par $\ln(1 - p) < 0$.
4. Conclure avec un **entier** (le plus petit qui convient).

**Exemple.** Chaque article a une probabilité $0{,}03$ d'être défectueux, indépendamment des autres. Combien faut-il en contrôler pour que la probabilité d'en trouver au moins un défectueux dépasse $0{,}9$ ?
$$1 - 0{,}97^n \geq 0{,}9 \iff 0{,}97^n \leq 0{,}1 \iff n\ln 0{,}97 \leq \ln 0{,}1 \iff n \geq \frac{\ln 0{,}1}{\ln 0{,}97} \approx 75{,}6.$$
Il faut contrôler **au moins $76$ articles**.

---

## Méthode 5 — Calculer avec des épreuves indépendantes non identiques

**Les étapes**

1. Faire un **arbre** (ou lister les issues utiles).
2. Multiplier les probabilités le long de chaque chemin (indépendance).
3. Additionner les chemins qui réalisent l'événement.
4. Pour « au moins un », passer par le contraire.

**Exemple.** Trois feux successifs sont verts avec les probabilités $0{,}5$, $0{,}6$ et $0{,}8$, indépendamment. Probabilité qu'**exactement un** feu soit vert :
$$0{,}5 \times 0{,}4 \times 0{,}2 + 0{,}5 \times 0{,}6 \times 0{,}2 + 0{,}5 \times 0{,}4 \times 0{,}8 = 0{,}04 + 0{,}06 + 0{,}16 = 0{,}26.$$
Probabilité qu'au moins un soit vert : $1 - 0{,}5 \times 0{,}4 \times 0{,}2 = 0{,}96$.

---

## Méthode 6 — Déterminer un intervalle et prendre une décision

**Les étapes**

1. Préciser l'hypothèse : $X \sim \mathcal{B}(n, p)$.
2. Afficher le tableau de $P(X \leq k)$ à la calculatrice.
3. $a$ est le plus petit entier tel que $P(X \leq a) > 0{,}025$ ; $b$ est le plus petit entier tel que $P(X \leq b) \geq 0{,}975$. Alors $P(a \leq X \leq b) \geq 0{,}95$.
4. Comparer la valeur observée à $[a, b]$ : si elle est **hors** de l'intervalle, on rejette l'hypothèse au risque de $5\,\%$ ; sinon, on ne peut pas la rejeter.

**Exemple.** Un laboratoire affirme que $20\,\%$ des personnes sont porteuses d'un certain gène. Dans un échantillon de $50$ personnes, assimilé à un tirage avec remise, on en compte $18$. Sous l'hypothèse, $X \sim \mathcal{B}(50\,;\,0{,}2)$. La calculatrice donne $P(X \leq 4) \approx 0{,}018$ et $P(X \leq 5) \approx 0{,}048$, donc $a = 5$ ; $P(X \leq 15) \approx 0{,}969$ et $P(X \leq 16) \approx 0{,}986$, donc $b = 16$. Comme $18 \notin [5, 16]$, on rejette l'affirmation du laboratoire, au risque de $5\,\%$.

!!! warning "Ne pas sur-interpréter"
    Si la valeur observée est **dans** l'intervalle, on ne « prouve » pas que l'hypothèse est vraie : on dit seulement que l'observation ne permet pas de la rejeter.
