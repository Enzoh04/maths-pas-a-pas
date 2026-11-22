# Exercices corrigés — Combinatoire et dénombrement

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Principes additif et multiplicatif | 1 à 6 |
| 2. $k$-uplets, arrangements, permutations | 7 à 12 |
| 3. Combinaisons | 13 à 19 |
| 4. Propriétés des coefficients binomiaux | 20 à 24 |
| 5. Synthèse | 25 à 28 |

---

## Thème 1 — Principes additif et multiplicatif

*Méthodes associées : [Méthode 2](methodes.md#methode-2-utiliser-le-principe-multiplicatif) et [Méthode 3](methodes.md#methode-3-passer-par-le-complementaire).*

### Exercice 1 — Menus <span class="etoiles">★</span>

Un restaurant propose 3 entrées, 4 plats et 2 desserts. Combien de menus « entrée + plat + dessert » peut-on composer ? Et de menus « entrée + plat » ou « plat + dessert » ?

??? success "Correction"
    $3 \times 4 \times 2 = 24$ menus complets. Les menus « entrée + plat » ($12$) et « plat + dessert » ($8$) forment deux ensembles disjoints : $12 + 8 = 20$ menus.

### Exercice 2 — Codes <span class="etoiles">★</span>

1. Combien y a-t-il de codes à 4 chiffres (de 0000 à 9999) ?
2. Combien ont leurs 4 chiffres tous différents ?

??? success "Correction"
    **1.** $10^4 = 10\,000$ ($4$-uplets de $\{0, \dots, 9\}$).

    **2.** $10 \times 9 \times 8 \times 7 = 5\,040$ (arrangements).

### Exercice 3 — Mots de passe <span class="etoiles">★</span>

Un mot de passe est formé de 6 caractères, chacun étant une lettre minuscule ou un chiffre. Combien y a-t-il de mots de passe ? Un ordinateur en teste un milliard par seconde : combien de temps lui faut-il pour tous les essayer ?

??? success "Correction"
    $36$ caractères possibles, donc $36^6 = 2\,176\,782\,336$ mots de passe. À $10^9$ essais par seconde : environ $2{,}2$ secondes. *D'où l'intérêt des mots de passe longs : avec 12 caractères, il faudrait près de 150 ans.*

### Exercice 4 — Langues vivantes <span class="etoiles">★★</span>

Dans une classe de 30 élèves, 18 étudient l'anglais, 15 l'espagnol, et 7 étudient les deux langues. Combien d'élèves étudient au moins une de ces langues ? aucune ?

??? success "Correction"
    $\operatorname{Card}(A \cup E) = 18 + 15 - 7 = 26$ élèves étudient au moins une langue, donc $30 - 26 = 4$ n'en étudient aucune.

### Exercice 5 — Multiples <span class="etoiles">★★</span>

Combien d'entiers compris entre 1 et 1 000 sont divisibles par 2 ou par 5 ?

??? success "Correction"
    $500$ multiples de 2, $200$ multiples de 5, et $100$ multiples de 10 (divisibles par les deux). Donc $500 + 200 - 100 = 600$.

### Exercice 6 — Nombre de diviseurs <span class="etoiles">★★</span>

On a $360 = 2^3 \times 3^2 \times 5$. Combien $360$ a-t-il de diviseurs positifs ?

??? success "Correction"
    Un diviseur s'écrit $2^a \times 3^b \times 5^c$ avec $a \in \{0, 1, 2, 3\}$, $b \in \{0, 1, 2\}$ et $c \in \{0, 1\}$. Par le principe multiplicatif : $4 \times 3 \times 2 = 24$ diviseurs.

---

## Thème 2 — $k$-uplets, arrangements, permutations

*Méthode associée : [Méthode 1](methodes.md#methode-1-choisir-le-bon-modele).*

### Exercice 7 — Podium <span class="etoiles">★</span>

Dix coureurs disputent une course. Combien y a-t-il de podiums possibles (or, argent, bronze) ?

??? success "Correction"
    L'ordre compte et un coureur ne peut pas avoir deux médailles : $10 \times 9 \times 8 = 720$.

### Exercice 8 — Anagrammes <span class="etoiles">★</span>

1. Combien le mot MATHS a-t-il d'anagrammes ?
2. Combien le mot ANANAS en a-t-il ? *Indication : si l'on numérote les A et les N, on obtient $6!$ mots ; combien de fois chaque anagramme est-il compté ?*

??? success "Correction"
    **1.** $5! = 120$.

    **2.** En distinguant $A_1, A_2, A_3$ et $N_1, N_2$, on a $6! = 720$ mots. Chaque anagramme est obtenu $3! \times 2! = 12$ fois (en permutant les A entre eux et les N entre eux). Il y a donc $\frac{720}{12} = 60$ anagrammes.

### Exercice 9 — Autour d'une table <span class="etoiles">★★</span>

1. De combien de façons peut-on asseoir 5 personnes sur un banc de 5 places ?
2. Même question si Alice et Bob veulent être côte à côte.

??? success "Correction"
    **1.** $5! = 120$.

    **2.** On « colle » Alice et Bob en un bloc. On range alors 4 objets (le bloc et les 3 autres) : $4! = 24$ façons, et dans le bloc, $2$ ordres (Alice-Bob ou Bob-Alice). Total : $2 \times 24 = 48$.

### Exercice 10 — Nombres de 4 chiffres <span class="etoiles">★★</span>

1. Combien y a-t-il de nombres de 4 chiffres (de 1000 à 9999) ?
2. Combien ont leurs chiffres tous distincts ?
3. Combien sont pairs et à chiffres distincts ?

??? success "Correction"
    **1.** $9 \times 10^3 = 9\,000$.

    **2.** $9 \times 9 \times 8 \times 7 = 4\,536$ (premier chiffre non nul, puis les autres distincts).

    **3.** On commence par le dernier chiffre, qui est contraint.

    - S'il vaut $0$ : $9$ choix pour le premier chiffre, puis $8$ et $7$ : $504$.
    - S'il vaut $2$, $4$, $6$ ou $8$ ($4$ choix) : le premier chiffre est non nul et différent du dernier ($8$ choix), puis $8$ et $7$ : $4 \times 8 \times 8 \times 7 = 1\,792$.

    Total : $504 + 1\,792 = 2\,296$.

### Exercice 11 — Ranger des livres <span class="etoiles">★★</span>

On range sur une étagère 3 livres de maths et 4 livres de physique, tous différents, de sorte que les livres d'une même matière soient regroupés. Combien de rangements possibles ?

??? success "Correction"
    On choisit l'ordre des deux blocs ($2!$), puis l'ordre dans chaque bloc ($3!$ et $4!$) : $2 \times 6 \times 24 = 288$.

### Exercice 12 — Tirages avec remise <span class="etoiles">★★★</span>

Une urne contient 5 boules rouges et 3 boules vertes, numérotées de 1 à 8. On tire successivement 3 boules **avec remise**.

1. Combien y a-t-il de tirages possibles ?
2. Combien contiennent au moins une boule verte ?
3. Combien contiennent exactement une boule verte ?

??? success "Correction"
    **1.** $8^3 = 512$.

    **2.** Sans boule verte : $5^3 = 125$. Donc $512 - 125 = 387$.

    **3.** On choisit la position de la boule verte ($3$ choix), son numéro ($3$), et les deux boules rouges ($5^2$) : $3 \times 3 \times 25 = 225$.

---

## Thème 3 — Combinaisons

*Méthode associée : [Méthode 4](methodes.md#methode-4-combinaisons-avec-conditions).*

### Exercice 13 — Calculs <span class="etoiles">★</span>

Calculer $\binom{5}{2}$, $\binom{10}{3}$, $\binom{8}{6}$ et $\binom{52}{5}$ (à la calculatrice pour le dernier).

??? success "Correction"
    $\binom{5}{2} = \frac{5 \times 4}{2} = 10$ ; $\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$ ; $\binom{8}{6} = \binom{8}{2} = 28$ ; $\binom{52}{5} = 2\,598\,960$.

### Exercice 14 — Comités et poignées de main <span class="etoiles">★</span>

1. Combien de comités de 3 personnes peut-on former dans un groupe de 12 ?
2. Dix personnes se serrent toutes la main deux à deux. Combien de poignées de main ?

??? success "Correction"
    **1.** $\binom{12}{3} = 220$.

    **2.** Une poignée de main correspond à une paire de personnes : $\binom{10}{2} = 45$.

### Exercice 15 — Comité mixte <span class="etoiles">★★</span>

On forme un comité de 4 personnes parmi 6 femmes et 5 hommes.

1. Combien de comités possibles ?
2. Combien avec exactement 2 femmes ?
3. Combien avec au moins une femme ?

??? success "Correction"
    **1.** $\binom{11}{4} = 330$.

    **2.** $\binom{6}{2}\binom{5}{2} = 15 \times 10 = 150$.

    **3.** Comités sans femme : $\binom{5}{4} = 5$. Donc $330 - 5 = 325$.

### Exercice 16 — Loto <span class="etoiles">★★</span>

Au Loto, on choisit 5 numéros parmi 49, et un « numéro chance » parmi 10. Combien de grilles différentes existe-t-il ?

??? success "Correction"
    $\binom{49}{5} \times 10 = 1\,906\,884 \times 10 = 19\,068\,840$. Une grille a donc environ une chance sur 19 millions de gagner le gros lot.

### Exercice 17 — Poker <span class="etoiles">★★★</span>

Une main de poker est formée de 5 cartes d'un jeu de 52 (13 hauteurs, 4 couleurs).

1. Combien de mains contiennent un **carré** (4 cartes de même hauteur) ?
2. Combien de mains contiennent **exactement une paire** (deux cartes de même hauteur, les trois autres de hauteurs différentes entre elles et de la paire) ?

??? success "Correction"
    **1.** On choisit la hauteur du carré ($13$), puis la 5ᵉ carte parmi les $48$ restantes : $13 \times 48 = 624$.

    **2.** Hauteur de la paire : $13$. Couleurs de la paire : $\binom{4}{2} = 6$. Les trois autres hauteurs, distinctes, parmi les $12$ restantes : $\binom{12}{3} = 220$. Une couleur pour chacune : $4^3 = 64$. Total : $13 \times 6 \times 220 \times 64 = 1\,098\,240$, soit environ 42 % des mains.

### Exercice 18 — Chemins sur un quadrillage <span class="etoiles">★★</span>

Sur un quadrillage, on va du point $(0 \,;\, 0)$ au point $(5 \,;\, 3)$ en faisant uniquement des pas d'une unité vers la droite ou vers le haut. Combien y a-t-il de chemins ?

??? success "Correction"
    Un chemin comporte $8$ pas : $5$ vers la droite et $3$ vers le haut. Il est entièrement déterminé par la position des $3$ pas vers le haut parmi les $8$ : $\binom{8}{3} = 56$ chemins.

### Exercice 19 — Diagonales d'un polygone <span class="etoiles">★★</span>

Combien un polygone convexe à $n$ côtés a-t-il de diagonales ? Application : $n = 10$.

??? success "Correction"
    Un segment joignant deux sommets est soit un côté, soit une diagonale. Il y a $\binom{n}{2}$ segments et $n$ côtés, donc $\binom{n}{2} - n = \frac{n(n - 1)}{2} - n = \frac{n(n - 3)}{2}$ diagonales. Pour $n = 10$ : $35$.

---

## Thème 4 — Propriétés des coefficients binomiaux

*Méthode associée : [Méthode 5](methodes.md#methode-5-demontrer-une-identite-par-double-denombrement).*

### Exercice 20 — Triangle de Pascal <span class="etoiles">★</span>

Construire le triangle de Pascal jusqu'à la ligne $n = 7$ et vérifier sur chaque ligne que la somme vaut $2^n$.

??? success "Correction"
    | $n$ | coefficients | somme |
    |---|---|---|
    | $6$ | $1 \; 6 \; 15 \; 20 \; 15 \; 6 \; 1$ | $64$ |
    | $7$ | $1 \; 7 \; 21 \; 35 \; 35 \; 21 \; 7 \; 1$ | $128$ |

    Les lignes $0$ à $5$ figurent dans le cours.

### Exercice 21 — Symétrie <span class="etoiles">★★</span>

Démontrer que $\binom{n}{k} = \binom{n}{n - k}$ de deux façons : par la formule, et par un raisonnement de dénombrement.

??? success "Correction"
    **Par la formule.** $\binom{n}{n - k} = \frac{n!}{(n - k)!\,(n - (n - k))!} = \frac{n!}{(n - k)!\,k!} = \binom{n}{k}$.

    **Par dénombrement.** Choisir les $k$ éléments qu'on garde revient à choisir les $n - k$ éléments qu'on laisse : l'application $A \mapsto \overline{A}$ est une bijection entre les parties à $k$ éléments et celles à $n - k$ éléments.

### Exercice 22 — Formule du président <span class="etoiles">★★</span>

Démontrer que $k\binom{n}{k} = n\binom{n - 1}{k - 1}$ pour $1 \leq k \leq n$, par le calcul puis par dénombrement.

??? success "Correction"
    **Par le calcul.** $k\binom{n}{k} = \frac{k\,n!}{k!\,(n - k)!} = \frac{n!}{(k - 1)!\,(n - k)!} = n \times \frac{(n - 1)!}{(k - 1)!\,(n - k)!} = n\binom{n - 1}{k - 1}$.

    **Par dénombrement.** Voir la méthode 5 (comités avec un président).

### Exercice 23 — Somme des carrés <span class="etoiles">★★★</span>

Démontrer que $\displaystyle\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}$. *Indication : choisir $n$ personnes dans un groupe de $n$ filles et $n$ garçons.*

??? success "Correction"
    On compte les groupes de $n$ personnes parmi $2n$ : il y en a $\binom{2n}{n}$.

    On les classe selon le nombre $k$ de filles choisies ($0 \leq k \leq n$). On choisit $k$ filles parmi $n$, et $n - k$ garçons parmi $n$ : $\binom{n}{k}\binom{n}{n - k} = \binom{n}{k}^2$ groupes. En sommant sur $k$ (principe additif), on obtient l'égalité.

    *Vérification pour $n = 6$ : $1 + 36 + 225 + 400 + 225 + 36 + 1 = 924 = \binom{12}{6}$.*

### Exercice 24 — Parties de cardinal pair <span class="etoiles">★★★</span>

1. À l'aide de la formule du binôme avec $a = -1$ et $b = 1$, montrer que pour $n \geq 1$ : $\displaystyle\sum_{k=0}^{n} (-1)^k\binom{n}{k} = 0$.
2. En déduire que, pour $n \geq 1$, un ensemble à $n$ éléments a autant de parties de cardinal pair que de parties de cardinal impair, et que chacune de ces catégories compte $2^{n-1}$ parties.

??? success "Correction"
    **1.** $(-1 + 1)^n = 0^n = 0$ pour $n \geq 1$, et la formule du binôme donne $\sum_{k} \binom{n}{k}(-1)^k 1^{n-k}$.

    **2.** La somme de la question 1 vaut $P - I$, où $P$ (resp. $I$) est le nombre de parties de cardinal pair (resp. impair). Donc $P = I$. Comme $P + I = 2^n$, on obtient $P = I = 2^{n-1}$.

---

## Thème 5 — Synthèse

### Exercice 25 — Mots binaires <span class="etoiles">★★</span>

On considère les mots de 8 caractères formés de 0 et de 1 (octets).

1. Combien y en a-t-il ?
2. Combien contiennent exactement trois 1 ?
3. Combien contiennent au moins deux 1 ?

??? success "Correction"
    **1.** $2^8 = 256$.

    **2.** On choisit les positions des trois 1 : $\binom{8}{3} = 56$.

    **3.** Le contraire est « aucun 1 » ($1$ mot) ou « exactement un 1 » ($8$ mots) : $256 - 1 - 8 = 247$.

### Exercice 26 — Le paradoxe des anniversaires <span class="etoiles">★★★</span>

On considère un groupe de 23 personnes, et on suppose que les 365 jours de l'année sont équiprobables pour les anniversaires (on ignore le 29 février).

1. Combien y a-t-il de listes possibles de 23 dates d'anniversaire ? Combien de listes où les 23 dates sont toutes différentes ?
2. En déduire la probabilité que deux personnes au moins aient le même anniversaire. Écrire un programme Python pour la calculer.

??? success "Correction"
    **1.** $365^{23}$ listes ($23$-uplets). Listes de dates distinctes : $365 \times 364 \times \dots \times 343 = \frac{365!}{342!}$ (arrangements).

    **2.** La probabilité que toutes les dates soient différentes est le quotient $\frac{365 \times 364 \times \dots \times 343}{365^{23}}$. Celle d'au moins une coïncidence en est le complément.

    ```python
    p = 1
    for i in range(23):
        p = p * (365 - i) / 365
    print(1 - p)   # environ 0.507
    ```

    Il y a donc plus d'une chance sur deux qu'au moins deux personnes partagent leur anniversaire, alors qu'il n'y a que 23 personnes ! C'est le « paradoxe » des anniversaires.

### Exercice 27 — Principe des tiroirs <span class="etoiles">★★</span>

1. Montrer que dans un groupe de 13 personnes, deux au moins sont nées le même mois.
2. On choisit 6 nombres entiers distincts entre 1 et 10. Montrer que deux d'entre eux ont pour somme 11.

??? success "Correction"
    **1.** 13 personnes, 12 mois (« tiroirs ») : deux personnes au moins sont dans le même tiroir.

    **2.** On forme les 5 paires $\{1, 10\}$, $\{2, 9\}$, $\{3, 8\}$, $\{4, 7\}$, $\{5, 6\}$, dont chacune a pour somme 11. Les 6 nombres choisis sont répartis dans ces 5 « tiroirs » : deux d'entre eux sont dans la même paire, et leur somme vaut 11.

### Exercice 28 — Vérifier en Python <span class="etoiles">★★★</span>

1. Combien le mot BANANE a-t-il d'anagrammes ? Justifier par le calcul.
2. Écrire un programme Python qui vérifie ce résultat en énumérant les anagrammes.
3. Écrire un programme qui énumère toutes les parties de $\{1, 2, 3, 4\}$ et vérifie qu'il y en a $2^4$.

??? success "Correction"
    **1.** 6 lettres, dont deux A et deux N : $\frac{6!}{2!\,2!} = \frac{720}{4} = 180$.

    **2.**

    ```python
    from itertools import permutations
    print(len(set(permutations("BANANE"))))   # 180
    ```

    `set` supprime les doublons, qui proviennent des permutations des lettres identiques.

    **3.**

    ```python
    from itertools import combinations
    E = [1, 2, 3, 4]
    parties = []
    for k in range(len(E) + 1):
        parties = parties + list(combinations(E, k))
    print(len(parties))   # 16 = 2**4
    ```
