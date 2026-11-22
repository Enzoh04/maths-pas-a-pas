# Exercices corrigés — Probabilités conditionnelles et indépendance

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'épreuve, va voir les [sujets type épreuve anticipée](bac.md). Tous les exercices se font **sans calculatrice**, sauf l'exercice Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Probabilités conditionnelles et tableaux | 1 à 5 |
| 2. Arbres pondérés | 6 à 11 |
| 3. Probabilités totales et inversion | 12 à 17 |
| 4. Indépendance | 18 à 22 |
| 5. Épreuves répétées et approfondissement | 23 à 28 |

---

## Thème 1 — Probabilités conditionnelles et tableaux

*Méthode associée : [Méthode 1](methodes.md#methode-1-lire-une-probabilite-conditionnelle-dans-un-tableau-croise).*

### Exercice 1 — Lunettes <span class="etoiles">★</span>

Dans un groupe de $500$ personnes, il y a $300$ adultes, dont $180$ portent des lunettes, et $200$ enfants, dont $40$ portent des lunettes. On choisit une personne au hasard. On note $A$ : « c'est un adulte » et $L$ : « elle porte des lunettes ».

1. Construire le tableau croisé des effectifs.
2. Calculer $P(L)$, $P(A \cap L)$, $P_A(L)$ et $P_L(A)$.

??? success "Correction"
    **1.** Tableau des effectifs :

    | | $L$ | $\overline{L}$ | Total |
    |---|---|---|---|
    | $A$ | $180$ | $120$ | $300$ |
    | $\overline{A}$ | $40$ | $160$ | $200$ |
    | Total | $220$ | $280$ | $500$ |

    **2.** $P(L) = \frac{220}{500} = 0{,}44$ ; $P(A \cap L) = \frac{180}{500} = 0{,}36$ ; $P_A(L) = \frac{180}{300} = 0{,}6$ ; $P_L(A) = \frac{180}{220} = \frac{9}{11}$.

### Exercice 2 — Avec la formule <span class="etoiles">★</span>

On sait que $P(A) = 0{,}4$, $P(B) = 0{,}5$ et $P(A \cap B) = 0{,}1$. Calculer $P_A(B)$, $P_A\left(\overline{B}\right)$ et $P_B(A)$.

??? success "Correction"
    $P_A(B) = \frac{0{,}1}{0{,}4} = 0{,}25$ ; $P_A\left(\overline{B}\right) = 1 - 0{,}25 = 0{,}75$ ; $P_B(A) = \frac{0{,}1}{0{,}5} = 0{,}2$.

### Exercice 3 — Un dé <span class="etoiles">★</span>

On lance un dé équilibré à six faces. $A$ : « le résultat est pair » ; $B$ : « le résultat est supérieur ou égal à $4$ ». Calculer $P(B)$, $P_A(B)$ et $P_B(A)$.

??? success "Correction"
    $A = \{2, 4, 6\}$, $B = \{4, 5, 6\}$, $A \cap B = \{4, 6\}$. $P(B) = \frac{1}{2}$. Sachant $A$, il reste $3$ issues équiprobables, dont $2$ dans $B$ : $P_A(B) = \frac{2}{3}$. De même $P_B(A) = \frac{2}{3}$.

### Exercice 4 — Compléter un tableau à partir de pourcentages <span class="etoiles">★★</span>

Un lycée compte $1\,200$ élèves, dont $55\,\%$ de filles. $40\,\%$ des filles et $30\,\%$ des garçons suivent une option ($O$). On choisit un élève au hasard.

1. Construire le tableau croisé des effectifs.
2. Quelle est la probabilité que l'élève suive l'option ?
3. Sachant que l'élève suit l'option, quelle est la probabilité que ce soit une fille ?

??? success "Correction"
    1. Filles : $660$, dont $264$ avec l'option ; garçons : $540$, dont $162$ avec l'option. Total option : $426$.
    2. $P(O) = \frac{426}{1\,200} = 0{,}355$.
    3. $P_O(F) = \frac{264}{426} = \frac{44}{71}$.

### Exercice 5 — Traduire un énoncé <span class="etoiles">★★</span>

On note $M$ : « la personne est malade » et $F$ : « la personne a de la fièvre ». Traduire chaque phrase par une probabilité.

1. « Parmi les malades, $90\,\%$ ont de la fièvre. »
2. « $10\,\%$ des personnes ayant de la fièvre sont malades. »
3. « $5\,\%$ de la population est malade et a de la fièvre. »

En déduire $P(M)$ et $P(F)$.

??? success "Correction"
    1. $P_M(F) = 0{,}9$. 2. $P_F(M) = 0{,}1$. 3. $P(M \cap F) = 0{,}05$.

    $P(M) = \frac{P(M \cap F)}{P_M(F)} = \frac{0{,}05}{0{,}9} = \frac{1}{18}$ et $P(F) = \frac{P(M \cap F)}{P_F(M)} = \frac{0{,}05}{0{,}1} = 0{,}5$.

---

## Thème 2 — Arbres pondérés

*Méthode associée : [Méthode 2](methodes.md#methode-2-construire-et-exploiter-un-arbre-pondere).*

### Exercice 6 — Compléter un arbre <span class="etoiles">★</span>

On sait que $P(A) = 0{,}3$, $P_A(B) = 0{,}6$ et $P_{\overline{A}}(B) = 0{,}2$. Construire l'arbre pondéré complet, puis calculer $P(A \cap B)$, $P\left(\overline{A} \cap B\right)$ et $P(B)$.

??? success "Correction"
    Branches : $P(A) = 0{,}3$, $P\left(\overline{A}\right) = 0{,}7$ ; $P_A(B) = 0{,}6$, $P_A\left(\overline{B}\right) = 0{,}4$ ; $P_{\overline{A}}(B) = 0{,}2$, $P_{\overline{A}}\left(\overline{B}\right) = 0{,}8$.

    $P(A \cap B) = 0{,}18$ ; $P\left(\overline{A} \cap B\right) = 0{,}14$ ; $P(B) = 0{,}18 + 0{,}14 = 0{,}32$.

### Exercice 7 — Tirages sans remise <span class="etoiles">★</span>

Une urne contient $3$ boules rouges et $2$ boules vertes. On tire successivement deux boules **sans remise**.

1. Construire l'arbre pondéré.
2. Calculer la probabilité de tirer deux boules rouges, puis deux boules de même couleur.
3. Calculer la probabilité que la seconde boule soit rouge.

??? success "Correction"
    1. Premier tirage : $R$ ($\frac{3}{5}$), $V$ ($\frac{2}{5}$). Après $R$ : $R$ ($\frac{2}{4}$), $V$ ($\frac{2}{4}$). Après $V$ : $R$ ($\frac{3}{4}$), $V$ ($\frac{1}{4}$).
    2. $P(RR) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$ ; $P(VV) = \frac{2}{5} \times \frac{1}{4} = \frac{1}{10}$ ; même couleur : $\frac{4}{10} = \frac{2}{5}$.
    3. $\frac{3}{5} \times \frac{2}{4} + \frac{2}{5} \times \frac{3}{4} = \frac{6}{20} + \frac{6}{20} = \frac{3}{5}$. *C'est la même probabilité qu'au premier tirage : sans information sur le premier tirage, les deux tirages jouent des rôles symétriques.*

### Exercice 8 — Deux machines <span class="etoiles">★★</span>

Une usine fabrique des pièces sur deux machines. La machine $M_1$ produit $60\,\%$ des pièces, dont $3\,\%$ sont défectueuses ; la machine $M_2$ produit le reste, dont $5\,\%$ sont défectueuses. On prélève une pièce au hasard ; $D$ : « la pièce est défectueuse ».

1. Construire l'arbre pondéré et calculer $P(D)$.
2. La pièce est défectueuse. Quelle est la probabilité qu'elle vienne de $M_1$ ?

??? success "Correction"
    1. $P(D) = 0{,}6 \times 0{,}03 + 0{,}4 \times 0{,}05 = 0{,}018 + 0{,}02 = 0{,}038$.
    2. $P_D(M_1) = \frac{0{,}018}{0{,}038} = \frac{18}{38} = \frac{9}{19}$.

### Exercice 9 — Trois fournisseurs <span class="etoiles">★★</span>

Un magasin achète ses ampoules à trois fournisseurs : $A$ ($50\,\%$), $B$ ($30\,\%$) et $C$ ($20\,\%$). Les proportions d'ampoules défectueuses sont respectivement $2\,\%$, $4\,\%$ et $5\,\%$.

1. Calculer la probabilité qu'une ampoule choisie au hasard soit défectueuse.
2. Sachant qu'elle est défectueuse, quelle est la probabilité qu'elle vienne de $C$ ?

??? success "Correction"
    1. $P(D) = 0{,}5 \times 0{,}02 + 0{,}3 \times 0{,}04 + 0{,}2 \times 0{,}05 = 0{,}01 + 0{,}012 + 0{,}01 = 0{,}032$.
    2. $P_D(C) = \frac{0{,}01}{0{,}032} = \frac{10}{32} = \frac{5}{16}$.

### Exercice 10 — Une branche inconnue <span class="etoiles">★★</span>

On sait que $P(A) = 0{,}4$, $P_A(B) = 0{,}5$ et $P(B) = 0{,}38$. Calculer $P_{\overline{A}}(B)$.

??? success "Correction"
    Probabilités totales : $0{,}4 \times 0{,}5 + 0{,}6 \times x = 0{,}38$, soit $0{,}6x = 0{,}18$, donc $P_{\overline{A}}(B) = x = 0{,}3$.

### Exercice 11 — Météo sur trois jours <span class="etoiles">★★★</span>

Dans une région, s'il fait beau un jour ($S$), il fait beau le lendemain avec la probabilité $0{,}8$ ; s'il pleut ($P$), il fait beau le lendemain avec la probabilité $0{,}4$. Il fait beau aujourd'hui (jour 1).

1. Construire l'arbre des jours 2 et 3.
2. Calculer la probabilité qu'il fasse beau le jour 3.
3. Sachant qu'il fait beau le jour 3, quelle est la probabilité qu'il ait plu le jour 2 ?

??? success "Correction"
    1. Jour 2 : $S$ ($0{,}8$), $P$ ($0{,}2$). Après $S$ : $S$ ($0{,}8$), $P$ ($0{,}2$). Après $P$ : $S$ ($0{,}4$), $P$ ($0{,}6$).
    2. $0{,}8 \times 0{,}8 + 0{,}2 \times 0{,}4 = 0{,}64 + 0{,}08 = 0{,}72$.
    3. $\frac{0{,}08}{0{,}72} = \frac{1}{9}$.

---

## Thème 3 — Probabilités totales et inversion

*Méthode associée : [Méthode 3](methodes.md#methode-3-probabilites-totales-et-inversion-du-conditionnement).*

### Exercice 12 — Test de dépistage <span class="etoiles">★</span>

Une maladie touche $1\,\%$ de la population. Un test est positif chez $99\,\%$ des malades et chez $2\,\%$ des personnes saines.

1. Calculer la probabilité qu'un test soit positif.
2. Une personne a un test positif. Quelle est la probabilité qu'elle soit malade ?

??? success "Correction"
    1. $P(T) = 0{,}01 \times 0{,}99 + 0{,}99 \times 0{,}02 = 0{,}0099 + 0{,}0198 = 0{,}0297$.
    2. $P_T(M) = \frac{0{,}0099}{0{,}0297} = \frac{1}{3}$. Deux tests positifs sur trois sont des faux positifs !

### Exercice 13 — Retards <span class="etoiles">★★</span>

$70\,\%$ des élèves d'un lycée viennent en bus, les autres à pied. $10\,\%$ des élèves venant en bus arrivent en retard, contre $5\,\%$ des élèves venant à pied.

1. Calculer la probabilité qu'un élève arrive en retard.
2. Un élève est en retard. Quelle est la probabilité qu'il soit venu en bus ?

??? success "Correction"
    1. $P(R) = 0{,}7 \times 0{,}1 + 0{,}3 \times 0{,}05 = 0{,}07 + 0{,}015 = 0{,}085$.
    2. $P_R(B) = \frac{0{,}07}{0{,}085} = \frac{70}{85} = \frac{14}{17}$.

### Exercice 14 — QCM et hasard <span class="etoiles">★★</span>

À une question de QCM à $4$ réponses, un élève connaît la réponse avec la probabilité $0{,}6$. Sinon, il répond au hasard.

1. Calculer la probabilité qu'il réponde correctement.
2. Il a répondu correctement. Quelle est la probabilité qu'il connaissait la réponse ?

??? success "Correction"
    1. $0{,}6 \times 1 + 0{,}4 \times \frac{1}{4} = 0{,}6 + 0{,}1 = 0{,}7$.
    2. $\frac{0{,}6}{0{,}7} = \frac{6}{7}$.

### Exercice 15 — Retrouver la racine de l'arbre <span class="etoiles">★★</span>

On note $x = P(A)$. On sait que $P_A(B) = 0{,}7$, $P_{\overline{A}}(B) = 0{,}2$ et $P(B) = 0{,}45$.

1. Calculer $x$.
2. En déduire $P_B(A)$.

??? success "Correction"
    1. $0{,}7x + 0{,}2(1 - x) = 0{,}45 \iff 0{,}5x = 0{,}25 \iff x = 0{,}5$.
    2. $P_B(A) = \frac{0{,}5 \times 0{,}7}{0{,}45} = \frac{0{,}35}{0{,}45} = \frac{7}{9}$.

### Exercice 16 — Internes <span class="etoiles">★★</span>

Un lycée accueille $40\,\%$ d'élèves de Seconde, $35\,\%$ de Première et $25\,\%$ de Terminale. Les proportions d'internes ($I$) sont respectivement $10\,\%$, $20\,\%$ et $40\,\%$.

1. Calculer $P(I)$.
2. Un élève est interne. Quelle est la probabilité qu'il soit en Terminale ?

??? success "Correction"
    1. $0{,}4 \times 0{,}1 + 0{,}35 \times 0{,}2 + 0{,}25 \times 0{,}4 = 0{,}04 + 0{,}07 + 0{,}1 = 0{,}21$.
    2. $\frac{0{,}1}{0{,}21} = \frac{10}{21}$.

### Exercice 17 — Maladie rare : une fonction <span class="etoiles">★★★</span>

Une maladie touche une proportion $p$ de la population ($0 < p < 1$). Un test est positif chez $99\,\%$ des malades et chez $1\,\%$ des personnes saines.

1. Montrer que la probabilité qu'une personne testée positive soit malade est $f(p) = \dfrac{99p}{98p + 1}$.
2. Calculer $f(0{,}5)$. Donner une valeur approchée de $f(0{,}001)$ (on admettra que $\frac{0{,}099}{1{,}098} \approx 0{,}09$).
3. Étudier les variations de $f$ sur $]0\,;\,1[$. Interpréter.

??? success "Correction"
    1. $P(T) = 0{,}99p + 0{,}01(1 - p) = 0{,}98p + 0{,}01$, donc $P_T(M) = \dfrac{0{,}99p}{0{,}98p + 0{,}01} = \dfrac{99p}{98p + 1}$ (en multipliant par $100$).
    2. $f(0{,}5) = \frac{49{,}5}{50} = 0{,}99$. $f(0{,}001) = \frac{0{,}099}{1{,}098} \approx 0{,}09$ : pour une maladie très rare, à peine $9\,\%$ des positifs sont malades.
    3. $f'(p) = \dfrac{99(98p + 1) - 99p \times 98}{(98p + 1)^2} = \dfrac{99}{(98p + 1)^2} > 0$ : $f$ est croissante. Plus la maladie est fréquente, plus un test positif est fiable.

---

## Thème 4 — Indépendance

*Méthode associée : [Méthode 4](methodes.md#methode-4-demontrer-que-deux-evenements-sont-independants-ou-non).*

### Exercice 18 — Vérifier l'indépendance <span class="etoiles">★</span>

On sait que $P(A) = 0{,}3$, $P(B) = 0{,}5$ et $P(A \cap B) = 0{,}15$. Les événements $A$ et $B$ sont-ils indépendants ? Calculer $P(A \cup B)$.

??? success "Correction"
    $P(A)P(B) = 0{,}15 = P(A \cap B)$ : ils sont indépendants. $P(A \cup B) = 0{,}3 + 0{,}5 - 0{,}15 = 0{,}65$.

### Exercice 19 — Avec un dé <span class="etoiles">★</span>

On lance un dé équilibré. $A$ : « résultat pair » ; $B$ : « résultat inférieur ou égal à $2$ » ; $C$ : « résultat inférieur ou égal à $3$ ». $A$ et $B$ sont-ils indépendants ? Et $A$ et $C$ ?

??? success "Correction"
    $A \cap B = \{2\}$ : $P(A \cap B) = \frac{1}{6}$ et $P(A)P(B) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$. Indépendants.

    $A \cap C = \{2\}$ : $\frac{1}{6} \neq \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$. Non indépendants.

### Exercice 20 — Rendre deux caractères indépendants <span class="etoiles">★★</span>

On complète le tableau d'effectifs suivant, où $x$ est un entier :

| | $B$ | $\overline{B}$ |
|---|---|---|
| $A$ | $12$ | $18$ |
| $\overline{A}$ | $x$ | $42$ |

Déterminer $x$ pour que les événements $A$ et $B$ soient indépendants (pour un individu choisi au hasard).

??? success "Correction"
    Indépendance $\iff P_A(B) = P_{\overline{A}}(B)$ (la proportion de $B$ est la même dans les deux lignes, donc égale à $P(B)$) : $\frac{12}{30} = \frac{x}{x + 42} \iff 12x + 504 = 30x \iff x = 28$.

    Vérification : effectif total $100$, $P(A) = 0{,}3$, $P(B) = 0{,}4$, $P(A \cap B) = 0{,}12 = 0{,}3 \times 0{,}4$. ✓

### Exercice 21 — Calculs avec des événements indépendants <span class="etoiles">★★</span>

$A$ et $B$ sont indépendants, avec $P(A) = 0{,}4$ et $P(B) = 0{,}25$. Calculer $P(A \cap B)$, $P(A \cup B)$ et $P\left(\overline{A} \cap \overline{B}\right)$ de deux façons.

??? success "Correction"
    $P(A \cap B) = 0{,}1$ ; $P(A \cup B) = 0{,}4 + 0{,}25 - 0{,}1 = 0{,}55$.

    $P\left(\overline{A} \cap \overline{B}\right) = 1 - P(A \cup B) = 0{,}45$ ; ou, par indépendance de $\overline{A}$ et $\overline{B}$ : $0{,}6 \times 0{,}75 = 0{,}45$.

### Exercice 22 — Fiabilité d'un circuit <span class="etoiles">★★★</span>

Un appareil contient deux composants qui fonctionnent indépendamment l'un de l'autre, avec les probabilités $0{,}9$ et $0{,}8$.

1. Montés **en série**, l'appareil fonctionne si les deux composants fonctionnent. Calculer cette probabilité.
2. Montés **en parallèle**, l'appareil fonctionne si au moins un composant fonctionne. Calculer cette probabilité.
3. Montrer que deux événements à la fois incompatibles et indépendants ont l'un une probabilité nulle.

??? success "Correction"
    1. $0{,}9 \times 0{,}8 = 0{,}72$.
    2. Les pannes sont indépendantes : $P(\text{deux pannes}) = 0{,}1 \times 0{,}2 = 0{,}02$, donc la probabilité de fonctionnement est $1 - 0{,}02 = 0{,}98$.
    3. Incompatibles : $P(A \cap B) = 0$ ; indépendants : $P(A \cap B) = P(A)P(B)$. Donc $P(A)P(B) = 0$, et un produit est nul si et seulement si l'un des facteurs l'est.

---

## Thème 5 — Épreuves répétées et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-repeter-une-epreuve-de-bernoulli).*

### Exercice 23 — Pièce puis dé <span class="etoiles">★</span>

On lance une pièce équilibrée, puis un dé équilibré à six faces. Calculer la probabilité d'obtenir « face » puis un résultat supérieur ou égal à $5$, puis la probabilité d'obtenir « pile » ou un $6$ (au moins l'un des deux).

??? success "Correction"
    Épreuves indépendantes : $\frac{1}{2} \times \frac{2}{6} = \frac{1}{6}$.

    « Pile ou $6$ » : contraire de « face et pas de $6$ », de probabilité $\frac{1}{2} \times \frac{5}{6} = \frac{5}{12}$. Réponse : $1 - \frac{5}{12} = \frac{7}{12}$.

### Exercice 24 — Répondre au hasard <span class="etoiles">★★</span>

Un QCM comporte $3$ questions, chacune avec $4$ réponses dont une seule est juste. Un élève répond au hasard à chaque question. On note $k$ le nombre de bonnes réponses.

1. Construire l'arbre (succès $S$ : bonne réponse).
2. Calculer la probabilité de chaque valeur de $k$ de $0$ à $3$.
3. Calculer la probabilité d'avoir au moins $2$ bonnes réponses.

??? success "Correction"
    1. Arbre à $3$ niveaux, $p = \frac{1}{4}$, $q = \frac{3}{4}$ sur chaque branche.
    2. $P(k = 0) = \left(\frac{3}{4}\right)^3 = \frac{27}{64}$ ; $P(k = 1) = 3 \times \frac{1}{4} \times \frac{9}{16} = \frac{27}{64}$ ; $P(k = 2) = 3 \times \frac{1}{16} \times \frac{3}{4} = \frac{9}{64}$ ; $P(k = 3) = \frac{1}{64}$. La somme vaut bien $1$.
    3. $\frac{9}{64} + \frac{1}{64} = \frac{10}{64} = \frac{5}{32}$.

### Exercice 25 — Quatre lancers de pièce <span class="etoiles">★★</span>

On lance $4$ fois une pièce équilibrée.

1. Combien l'arbre comporte-t-il de chemins ? Quelle est la probabilité de chacun ?
2. Compter les chemins comportant exactement $0$, $1$, $2$, $3$, $4$ fois « pile ».
3. En déduire la probabilité d'obtenir exactement deux fois « pile ».

??? success "Correction"
    1. $2^4 = 16$ chemins, chacun de probabilité $\frac{1}{16}$.
    2. $1$, $4$, $6$, $4$, $1$ (pour $2$ piles : PPFF, PFPF, PFFP, FPPF, FPFP, FFPP).
    3. $\frac{6}{16} = \frac{3}{8}$.

### Exercice 26 — Contrôle qualité <span class="etoiles">★★</span>

$10\,\%$ des pièces d'une production sont défectueuses. On prélève $4$ pièces, et on admet que les prélèvements sont indépendants.

1. Calculer la probabilité qu'aucune pièce ne soit défectueuse.
2. Calculer la probabilité qu'au moins une pièce soit défectueuse.
3. Calculer la probabilité qu'exactement une pièce soit défectueuse.

??? success "Correction"
    1. $0{,}9^4 = 0{,}6561$.
    2. $1 - 0{,}6561 = 0{,}3439$.
    3. $4$ chemins : $4 \times 0{,}1 \times 0{,}9^3 = 4 \times 0{,}1 \times 0{,}729 = 0{,}2916$.

### Exercice 27 — Simulation en Python <span class="etoiles">★★★</span>

1. Écrire une fonction `experience(n, p)` qui simule $n$ épreuves de Bernoulli de paramètre $p$ et renvoie la **liste** des résultats ($1$ pour un succès, $0$ pour un échec).
2. Écrire une fonction `frequence(N, n, p, k)` qui répète $N$ fois l'expérience et renvoie la fréquence des expériences ayant donné exactement $k$ succès.
3. Comparer `frequence(10000, 3, 0.25, 2)` avec la probabilité exacte de l'exercice 24.

??? success "Correction"
    ```python
    from random import random

    def experience(n, p):
        resultats = []
        for i in range(n):
            if random() < p:
                resultats.append(1)
            else:
                resultats.append(0)
        return resultats

    def frequence(N, n, p, k):
        compteur = 0
        for j in range(N):
            if sum(experience(n, p)) == k:
                compteur = compteur + 1
        return compteur / N

    print(frequence(10000, 3, 0.25, 2))   # environ 0.14
    ```

    La valeur exacte est $\frac{9}{64} \approx 0{,}1406$. La fréquence observée en est proche, et s'en rapproche quand $N$ augmente (c'est la loi des grands nombres, vue en Terminale).

### Exercice 28 — Le problème de Monty Hall <span class="etoiles">★★★</span>

Un candidat fait face à trois portes : une voiture est cachée derrière l'une d'elles, des chèvres derrière les deux autres. Il choisit une porte. Le présentateur, qui sait où est la voiture, ouvre alors une **autre** porte, derrière laquelle se trouve une chèvre, et propose au candidat de **changer** de porte.

Le candidat a-t-il intérêt à changer ? Justifier à l'aide d'un arbre.

??? success "Correction"
    Premier niveau : le premier choix est la bonne porte ($V$) avec la probabilité $\frac{1}{3}$, une mauvaise porte ($\overline{V}$) avec la probabilité $\frac{2}{3}$.

    - Si le candidat avait choisi la voiture, changer le fait perdre à coup sûr.
    - S'il avait choisi une chèvre, le présentateur est **obligé** d'ouvrir l'autre porte à chèvre : la porte restante cache la voiture, et changer le fait gagner à coup sûr.

    Donc $P(\text{gagner en changeant}) = \frac{2}{3} \times 1 = \frac{2}{3}$, contre $\frac{1}{3}$ en gardant sa porte. Il a intérêt à changer !
