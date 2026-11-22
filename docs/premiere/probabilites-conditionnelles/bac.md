# Sujets type épreuve anticipée — Probabilités conditionnelles et indépendance

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

L'épreuve anticipée de mathématiques dure **2 heures, sans calculatrice**, avec un **QCM d'automatismes** (6 points) et **deux ou trois exercices** (14 points). Chaque sujet ci-dessous comporte **six questions d'automatismes** puis **un exercice**. Compte environ **40 minutes** par sujet.

| Sujet | Exercice | Durée conseillée |
|---|---|---|
| 1 | Abonnements et arbre pondéré | 35 min |
| 2 | Tableau croisé et indépendance | 35 min |
| 3 | Tirs au but : épreuves répétées | 40 min |
| 4 | Test de dépistage | 40 min |

## Sujet 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** Si $P(A) = 0{,}5$ et $P(A \cap B) = 0{,}2$, alors $P_A(B)$ vaut :

a. $0{,}1$ ; b. $0{,}4$ ; c. $0{,}7$ ; d. $2{,}5$.

**Question 2.** $0{,}3 \times 0{,}6 + 0{,}7 \times 0{,}2$ est égal à :

a. $0{,}32$ ; b. $0{,}18$ ; c. $0{,}8$ ; d. $0{,}5$.

**Question 3.** $15\,\%$ de $40\,\%$ correspond à :

a. $55\,\%$ ; b. $6\,\%$ ; c. $0{,}6\,\%$ ; d. $25\,\%$.

**Question 4.** $\dfrac{0{,}12}{0{,}3}$ est égal à :

a. $0{,}04$ ; b. $4$ ; c. $0{,}4$ ; d. $0{,}36$.

**Question 5.** Une quantité diminue de $20\,\%$. Elle est multipliée par :

a. $0{,}2$ ; b. $1{,}2$ ; c. $0{,}8$ ; d. $-0{,}2$.

**Question 6.** L'équation $2x^2 = 18$ a pour solutions :

a. $3$ seulement ; b. $-3$ et $3$ ; c. $9$ ; d. $-9$ et $9$.

### Partie 2 — Exercice

Une plateforme de vidéos propose un abonnement « premium ». $40\,\%$ des utilisateurs sont abonnés premium ($A$). Parmi eux, $80\,\%$ regardent des séries ($S$) chaque semaine, contre $50\,\%$ des autres utilisateurs. On choisit un utilisateur au hasard.

1. Construire un arbre pondéré décrivant la situation.
2. Calculer la probabilité que l'utilisateur soit abonné premium et regarde des séries.
3. Montrer que $P(S) = 0{,}62$.
4. L'utilisateur regarde des séries. Quelle est la probabilité qu'il soit abonné premium ?
5. Les événements $A$ et $S$ sont-ils indépendants ?

??? success "Correction"
    **Partie 1**

    1. **b.** $\frac{0{,}2}{0{,}5}$. 2. **a.** $0{,}18 + 0{,}14$. 3. **b.** $0{,}15 \times 0{,}4 = 0{,}06$. 4. **c.** 5. **c.** 6. **b.** $x^2 = 9$.

    **Partie 2**

    **1.** $P(A) = 0{,}4$, $P\left(\overline{A}\right) = 0{,}6$ ; $P_A(S) = 0{,}8$, $P_A\left(\overline{S}\right) = 0{,}2$ ; $P_{\overline{A}}(S) = 0{,}5$, $P_{\overline{A}}\left(\overline{S}\right) = 0{,}5$.

    **2.** $P(A \cap S) = 0{,}4 \times 0{,}8 = 0{,}32$.

    **3.** $P(S) = 0{,}32 + 0{,}6 \times 0{,}5 = 0{,}32 + 0{,}3 = 0{,}62$.

    **4.** $P_S(A) = \frac{0{,}32}{0{,}62} = \frac{32}{62} = \frac{16}{31}$.

    **5.** $P(A)P(S) = 0{,}4 \times 0{,}62 = 0{,}248 \neq 0{,}32$ : non indépendants. (Ou : $P_A(S) = 0{,}8 \neq P(S)$.)

---

## Sujet 2

### Partie 1 — Automatismes (QCM)

**Question 1.** Deux événements $A$ et $B$ sont indépendants si :

a. $A \cap B = \varnothing$ ; b. $P(A \cap B) = P(A) \times P(B)$ ; c. $P(A \cup B) = P(A) + P(B)$ ; d. $P(A) = P(B)$.

**Question 2.** Si $P(A) = 0{,}3$, $P(B) = 0{,}4$ et $A$, $B$ indépendants, alors $P(A \cup B)$ vaut :

a. $0{,}7$ ; b. $0{,}12$ ; c. $0{,}58$ ; d. $0{,}82$.

**Question 3.** La proportion de $60$ dans $400$ est :

a. $6\,\%$ ; b. $15\,\%$ ; c. $24\,\%$ ; d. $66\,\%$.

**Question 4.** $\dfrac{40}{160}$ est égal à :

a. $0{,}4$ ; b. $0{,}25$ ; c. $4$ ; d. $0{,}16$.

**Question 5.** La fonction $f(x) = -2x + 7$ est :

a. croissante ; b. décroissante ; c. constante ; d. ni croissante ni décroissante.

**Question 6.** L'expression développée de $(2x - 3)^2$ est :

a. $4x^2 - 9$ ; b. $4x^2 - 12x + 9$ ; c. $2x^2 - 12x + 9$ ; d. $4x^2 + 9$.

### Partie 2 — Exercice

Une enquête porte sur $400$ personnes. $160$ d'entre elles pratiquent un sport ($S$). Parmi les sportifs, $40$ lisent régulièrement ($L$) ; parmi les non-sportifs, $60$ lisent régulièrement. On choisit une personne au hasard.

1. Recopier et compléter le tableau d'effectifs.

    | | $L$ | $\overline{L}$ | Total |
    |---|---|---|---|
    | $S$ | | | |
    | $\overline{S}$ | | | |
    | Total | | | $400$ |

2. Calculer $P(S)$, $P(L)$ et $P(S \cap L)$.
3. Calculer $P_S(L)$ et $P_{\overline{S}}(L)$. Interpréter.
4. Les événements $S$ et $L$ sont-ils indépendants ?
5. Que vaut $P_L\left(\overline{S}\right)$ ?

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **c.** $0{,}7 - 0{,}12$. 3. **b.** 4. **b.** 5. **b.** 6. **b.**

    **Partie 2**

    **1.** $S$ : $40$, $120$, total $160$ ; $\overline{S}$ : $60$, $180$, total $240$ ; totaux : $100$, $300$, $400$.

    **2.** $P(S) = 0{,}4$ ; $P(L) = \frac{100}{400} = 0{,}25$ ; $P(S \cap L) = \frac{40}{400} = 0{,}1$.

    **3.** $P_S(L) = \frac{40}{160} = 0{,}25$ et $P_{\overline{S}}(L) = \frac{60}{240} = 0{,}25$ : la proportion de lecteurs est la même chez les sportifs et les non-sportifs.

    **4.** $P(S)P(L) = 0{,}4 \times 0{,}25 = 0{,}1 = P(S \cap L)$ : oui, ils sont indépendants.

    **5.** $P_L\left(\overline{S}\right) = \frac{60}{100} = 0{,}6$, ce qui est aussi $P\left(\overline{S}\right)$, comme le prévoit l'indépendance de $\overline{S}$ et $L$.

---

## Sujet 3

### Partie 1 — Automatismes (QCM)

**Question 1.** $0{,}3^3$ est égal à :

a. $0{,}9$ ; b. $0{,}027$ ; c. $0{,}09$ ; d. $0{,}0027$.

**Question 2.** $0{,}7^2$ est égal à :

a. $0{,}49$ ; b. $1{,}4$ ; c. $0{,}14$ ; d. $4{,}9$.

**Question 3.** On lance deux fois une pièce équilibrée. La probabilité d'obtenir au moins un « pile » est :

a. $\frac{1}{2}$ ; b. $\frac{1}{4}$ ; c. $\frac{3}{4}$ ; d. $1$.

**Question 4.** Dans un arbre de $3$ épreuves à deux issues, le nombre de chemins est :

a. $3$ ; b. $6$ ; c. $8$ ; d. $9$.

**Question 5.** $1 - 0{,}0081$ est égal à :

a. $0{,}9919$ ; b. $0{,}919$ ; c. $0{,}1919$ ; d. $0{,}9819$.

**Question 6.** La suite définie par $u_n = 5 \times 0{,}3^n$ est :

a. arithmétique de raison $0{,}3$ ; b. géométrique de raison $5$ ; c. géométrique de raison $0{,}3$ ; d. croissante.

### Partie 2 — Exercice

Un joueur réussit un tir au but avec la probabilité $0{,}7$. Il tire $3$ fois ; les tirs sont indépendants.

1. Construire l'arbre pondéré de l'expérience (succès $S$ : le tir est réussi).
2. Calculer la probabilité que les trois tirs soient réussis.
3. Calculer la probabilité qu'exactement deux tirs soient réussis.
4. Calculer la probabilité qu'au moins un tir soit réussi.
5. Le joueur tire maintenant $n$ fois, avec $n \leq 4$. Quel est le plus petit $n$ pour lequel la probabilité de réussir au moins un tir dépasse $0{,}99$ ?

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **a.** 3. **c.** $1 - \frac{1}{4}$. 4. **c.** $2^3$. 5. **a.** 6. **c.**

    **Partie 2**

    **1.** Arbre à trois niveaux : chaque nœud a deux branches, $S$ ($0{,}7$) et $E$ ($0{,}3$).

    **2.** $0{,}7^3 = 0{,}343$.

    **3.** Trois chemins ($SSE$, $SES$, $ESS$), chacun de probabilité $0{,}7^2 \times 0{,}3 = 0{,}147$ : $3 \times 0{,}147 = 0{,}441$.

    **4.** $1 - 0{,}3^3 = 1 - 0{,}027 = 0{,}973$.

    **5.** On veut $1 - 0{,}3^n > 0{,}99$, soit $0{,}3^n < 0{,}01$. $0{,}3^3 = 0{,}027 > 0{,}01$ et $0{,}3^4 = 0{,}0081 < 0{,}01$ : $n = 4$.

---

## Sujet 4

### Partie 1 — Automatismes (QCM)

**Question 1.** $0{,}05 \times 0{,}9$ est égal à :

a. $0{,}45$ ; b. $0{,}045$ ; c. $0{,}0045$ ; d. $0{,}95$.

**Question 2.** $0{,}95 \times 0{,}1$ est égal à :

a. $0{,}095$ ; b. $0{,}95$ ; c. $0{,}0095$ ; d. $0{,}105$.

**Question 3.** $\dfrac{0{,}045}{0{,}14}$ est égal à :

a. $\frac{9}{28}$ ; b. $\frac{45}{14}$ ; c. $\frac{9}{14}$ ; d. $\frac{1}{3}$.

**Question 4.** Si $P_A(B) = 0{,}9$, alors $P_A\left(\overline{B}\right)$ vaut :

a. $0{,}9$ ; b. $0{,}1$ ; c. $0{,}09$ ; d. on ne peut pas savoir.

**Question 5.** Un capital de $2\,000$ € placé à $3\,\%$ par an pendant deux ans (intérêts composés) devient :

a. $2\,120$ € ; b. $2\,121{,}80$ € ; c. $2\,060$ € ; d. $2\,180$ €.

**Question 6.** Le nombre dérivé de $x \mapsto x^2$ en $x = 3$ est :

a. $9$ ; b. $3$ ; c. $6$ ; d. $2$.

### Partie 2 — Exercice

Une maladie touche $5\,\%$ d'une population. Un test de dépistage est positif chez $90\,\%$ des malades et chez $10\,\%$ des personnes non malades. On choisit une personne au hasard ; $M$ : « la personne est malade », $T$ : « le test est positif ».

1. Construire un arbre pondéré.
2. Montrer que $P(T) = 0{,}14$.
3. Le test est positif. Quelle est la probabilité que la personne soit malade ? Commenter.
4. Le test est négatif. Montrer que la probabilité que la personne ne soit pas malade est $\frac{171}{172}$.
5. On fait passer à une personne malade deux tests successifs, dont les résultats sont indépendants. Quelle est la probabilité qu'au moins un des deux tests soit positif ?

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **a.** 3. **a.** $\frac{45}{140}$. 4. **b.** 5. **b.** $2\,000 \times 1{,}03^2 = 2\,000 \times 1{,}0609$. 6. **c.** $2 \times 3$.

    **Partie 2**

    **1.** $P(M) = 0{,}05$, $P\left(\overline{M}\right) = 0{,}95$ ; $P_M(T) = 0{,}9$, $P_M\left(\overline{T}\right) = 0{,}1$ ; $P_{\overline{M}}(T) = 0{,}1$, $P_{\overline{M}}\left(\overline{T}\right) = 0{,}9$.

    **2.** $P(T) = 0{,}05 \times 0{,}9 + 0{,}95 \times 0{,}1 = 0{,}045 + 0{,}095 = 0{,}14$.

    **3.** $P_T(M) = \frac{0{,}045}{0{,}14} = \frac{9}{28} \approx 0{,}32$. Moins d'un tiers des personnes testées positives sont malades : le test seul ne suffit pas à poser un diagnostic, car la maladie est assez rare.

    **4.** $P\left(\overline{T}\right) = 0{,}86$ et $P\left(\overline{M} \cap \overline{T}\right) = 0{,}95 \times 0{,}9 = 0{,}855$, donc $P_{\overline{T}}\left(\overline{M}\right) = \frac{0{,}855}{0{,}86} = \frac{855}{860} = \frac{171}{172}$. Un test négatif est très rassurant.

    **5.** Pour une personne malade, chaque test est négatif avec la probabilité $0{,}1$ : $1 - 0{,}1^2 = 0{,}99$.
