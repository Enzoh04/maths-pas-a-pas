# Évaluations type — Probabilités

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Chaque évaluation dure environ **40 minutes**, **sans calculatrice**. Elle commence par **six questions d'automatismes** (comme dans l'épreuve anticipée de Première), puis comporte **un exercice** sur le chapitre.

| Évaluation | Exercice | Durée conseillée |
|---|---|---|
| 1 | Une loterie | 35 min |
| 2 | Deux dés | 35 min |
| 3 | Tableau croisé et probabilités conditionnelles | 40 min |
| 4 | Test de dépistage et arbre pondéré | 40 min |

## Évaluation 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** On tire une carte dans un jeu de $32$ cartes. La probabilité de tirer un as est :

a. $\frac{1}{32}$ ; b. $\frac{1}{8}$ ; c. $\frac{1}{4}$ ; d. $\frac{4}{52}$.

**Question 2.** Si $P(A) = 0{,}35$, alors $P\left(\overline{A}\right)$ vaut :

a. $0{,}35$ ; b. $0{,}65$ ; c. $0{,}75$ ; d. $1{,}35$.

**Question 3.** $P(A) = 0{,}4$, $P(B) = 0{,}3$ et $P(A \cap B) = 0{,}1$. Alors $P(A \cup B)$ vaut :

a. $0{,}7$ ; b. $0{,}6$ ; c. $0{,}8$ ; d. $0{,}12$.

**Question 4.** $\frac{3}{20}$ est égal à :

a. $0{,}3$ ; b. $0{,}15$ ; c. $0{,}6$ ; d. $0{,}23$.

**Question 5.** Une augmentation de $40\,\%$ correspond à un coefficient multiplicateur de :

a. $0{,}4$ ; b. $1{,}04$ ; c. $1{,}4$ ; d. $40$.

**Question 6.** La moyenne de $5\,;\,9\,;\,10$ est :

a. $9$ ; b. $8$ ; c. $24$ ; d. $7$.

### Partie 2 — Exercice

Une loterie comporte $200$ billets. Parmi eux, $2$ billets font gagner $50$ €, $10$ billets font gagner $10$ €, $40$ billets font gagner un billet gratuit pour le tirage suivant ; les autres sont perdants. On achète un billet au hasard.

1. Quelle est la probabilité de gagner $50$ € ? de gagner de l'argent ?
2. Quelle est la probabilité de ne rien gagner du tout ?
3. Soit $A$ : « gagner quelque chose » et $B$ : « gagner au moins $10$ € ». Calculer $P(A)$, $P(B)$, $P(A \cap B)$ et $P(A \cup B)$.

??? success "Correction"
    **Partie 1**

    1. **b.** $\frac{4}{32}$. 2. **b.** 3. **b.** $0{,}4 + 0{,}3 - 0{,}1$. 4. **b.** 5. **c.** 6. **b.**

    **Partie 2**

    **1.** $\frac{2}{200} = 0{,}01$ ; $\frac{12}{200} = 0{,}06$.

    **2.** Perdants : $200 - 52 = 148$, soit $\frac{148}{200} = 0{,}74$.

    **3.** $P(A) = \frac{52}{200} = 0{,}26$ ; $P(B) = 0{,}06$ ; $B \subset A$, donc $P(A \cap B) = 0{,}06$ et $P(A \cup B) = P(A) = 0{,}26$.

---

## Évaluation 2

### Partie 1 — Automatismes (QCM)

**Question 1.** On lance deux dés. Le nombre d'issues possibles (couples) est :

a. $12$ ; b. $36$ ; c. $11$ ; d. $6$.

**Question 2.** On lance deux pièces. La probabilité d'obtenir deux « face » est :

a. $\frac{1}{2}$ ; b. $\frac{1}{3}$ ; c. $\frac{1}{4}$ ; d. $\frac{2}{3}$.

**Question 3.** Deux événements incompatibles $A$ et $B$ vérifient :

a. $P(A) + P(B) = 1$ ; b. $P(A \cap B) = 0$ ; c. $P(A) = P(B)$ ; d. $P(A \cup B) = 0$.

**Question 4.** $\frac{6}{36}$ est égal à :

a. $\frac{1}{5}$ ; b. $\frac{1}{6}$ ; c. $\frac{1}{3}$ ; d. $\frac{2}{9}$.

**Question 5.** $1 - \frac{5}{12}$ est égal à :

a. $\frac{7}{12}$ ; b. $\frac{4}{12}$ ; c. $\frac{5}{12}$ ; d. $\frac{1}{12}$.

**Question 6.** La solution de $2x - 3 = 7$ est :

a. $2$ ; b. $5$ ; c. $10$ ; d. $-5$.

### Partie 2 — Exercice

On lance deux dés équilibrés, un rouge et un bleu, et on note le **produit** des deux résultats.

1. Construire le tableau des $36$ produits.
2. Calculer la probabilité que le produit soit égal à $12$.
3. Calculer la probabilité que le produit soit pair. *On pourra passer par l'événement contraire.*
4. Calculer la probabilité que le produit soit un carré parfait.
5. Calculer la probabilité que le produit soit pair **ou** supérieur à $20$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **c.** 3. **b.** 4. **b.** 5. **a.** 6. **b.**

    **Partie 2**

    **2.** Produit $12$ : $(2,6), (3,4), (4,3), (6,2)$ : $\frac{4}{36} = \frac{1}{9}$.

    **3.** Produit impair si les deux résultats sont impairs : $3 \times 3 = 9$ cases. $P = 1 - \frac{9}{36} = \frac{3}{4}$.

    **4.** Carrés : $1$ ($(1,1)$), $4$ ($(1,4), (2,2), (4,1)$), $9$ ($(3,3)$), $16$ ($(4,4)$), $25$ ($(5,5)$), $36$ ($(6,6)$) : $8$ cases, $\frac{8}{36} = \frac{2}{9}$.

    **5.** Produits supérieurs à $20$ : $24$ ($(4,6)$ et $(6,4)$), $25$ ($(5,5)$), $30$ ($(5,6)$ et $(6,5)$) et $36$ ($(6,6)$), soit $6$ cases, dont $5$ à produit pair. Avec la formule de la réunion : $\frac{27}{36} + \frac{6}{36} - \frac{5}{36} = \frac{28}{36} = \frac{7}{9}$.

---

## Évaluation 3

### Partie 1 — Automatismes (QCM)

**Question 1.** Dans un tableau croisé, la proportion de sportifs **parmi les filles** se calcule en divisant par :

a. l'effectif total ; b. le nombre de filles ; c. le nombre de sportifs ; d. le nombre de sportives.

**Question 2.** $\frac{48}{120}$ est égal à :

a. $0{,}48$ ; b. $0{,}4$ ; c. $0{,}25$ ; d. $0{,}6$.

**Question 3.** $45\,\%$ de $60\,\%$ font :

a. $27\,\%$ ; b. $105\,\%$ ; c. $15\,\%$ ; d. $2{,}7\,\%$.

**Question 4.** Si $P_A(B) = 0{,}3$, alors $P_A\left(\overline{B}\right)$ vaut :

a. $0{,}3$ ; b. $0{,}7$ ; c. $0{,}09$ ; d. on ne peut pas savoir.

**Question 5.** La factorisation de $x^2 - 25$ est :

a. $(x - 5)^2$ ; b. $(x - 5)(x + 5)$ ; c. $(x - 25)(x + 1)$ ; d. $x(x - 25)$.

**Question 6.** Un train parcourt $240$ km en $1$ h $36$ min. Sa vitesse moyenne est :

a. $150$ km/h ; b. $176$ km/h ; c. $240$ km/h ; d. $136$ km/h.

### Partie 2 — Exercice

Une enquête auprès de $500$ personnes porte sur la possession d'un animal de compagnie.

| | Chien ($C$) | Pas de chien | Total |
|---|---|---|---|
| Maison ($M$) | $120$ | $180$ | $300$ |
| Appartement | $30$ | $170$ | $200$ |
| Total | $150$ | $350$ | $500$ |

On choisit une personne au hasard.

1. Calculer $P(C)$, $P(M)$ et $P(M \cap C)$.
2. Calculer $P(M \cup C)$.
3. Calculer $P_M(C)$ et $P_{\overline{M}}(C)$. Interpréter.
4. Calculer $P_C(M)$. Interpréter.
5. Vérifier que $P(M \cap C) = P(M) \times P_M(C)$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **b.** 3. **a.** 4. **b.** 5. **b.** 6. **a.** $\frac{240}{1{,}6}$.

    **Partie 2**

    **1.** $P(C) = 0{,}3$ ; $P(M) = 0{,}6$ ; $P(M \cap C) = \frac{120}{500} = 0{,}24$.

    **2.** $0{,}6 + 0{,}3 - 0{,}24 = 0{,}66$.

    **3.** $P_M(C) = \frac{120}{300} = 0{,}4$ ; $P_{\overline{M}}(C) = \frac{30}{200} = 0{,}15$. On a beaucoup plus souvent un chien quand on vit en maison.

    **4.** $P_C(M) = \frac{120}{150} = 0{,}8$ : $80\,\%$ des propriétaires de chien vivent en maison.

    **5.** $0{,}6 \times 0{,}4 = 0{,}24$. ✓

---

## Évaluation 4

### Partie 1 — Automatismes (QCM)

**Question 1.** $0{,}04 \times 0{,}9$ est égal à :

a. $0{,}36$ ; b. $0{,}036$ ; c. $0{,}0036$ ; d. $0{,}94$.

**Question 2.** $0{,}96 \times 0{,}05$ est égal à :

a. $0{,}48$ ; b. $0{,}048$ ; c. $0{,}0048$ ; d. $0{,}91$.

**Question 3.** $\frac{36}{84}$ est égal à :

a. $\frac{3}{7}$ ; b. $\frac{4}{7}$ ; c. $\frac{1}{2}$ ; d. $\frac{6}{14}$ et ne se simplifie plus.

**Question 4.** La spécificité d'un test est la probabilité :

a. d'être malade ; b. qu'un malade ait un test positif ; c. qu'une personne non malade ait un test négatif ; d. d'avoir un test positif.

**Question 5.** $(-2)^3$ est égal à :

a. $-6$ ; b. $8$ ; c. $-8$ ; d. $6$.

**Question 6.** Le milieu du segment d'extrémités $A(-1\,;\,4)$ et $B(5\,;\,0)$ est :

a. $(2\,;\,2)$ ; b. $(3\,;\,2)$ ; c. $(4\,;\,4)$ ; d. $(2\,;\,4)$.

### Partie 2 — Exercice

Une maladie touche $4\,\%$ d'une population. Un test a une sensibilité de $90\,\%$ (il est positif pour $90\,\%$ des malades) et une spécificité de $95\,\%$ (il est négatif pour $95\,\%$ des personnes non malades). On choisit une personne au hasard ; $M$ : « la personne est malade », $T$ : « le test est positif ».

1. Construire l'arbre pondéré de la situation.
2. Calculer $P(M \cap T)$ et $P\left(\overline{M} \cap T\right)$.
3. En déduire $P(T)$.
4. Pour $10\,000$ personnes, compléter un tableau croisé (malade ou non, test positif ou non), puis calculer $P_T(M)$.
5. Commenter ce résultat.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **b.** 3. **a.** 4. **c.** 5. **c.** 6. **a.**

    **Partie 2**

    **1.** $P(M) = 0{,}04$, $P\left(\overline{M}\right) = 0{,}96$ ; $P_M(T) = 0{,}9$, $P_M\left(\overline{T}\right) = 0{,}1$ ; $P_{\overline{M}}(T) = 0{,}05$, $P_{\overline{M}}\left(\overline{T}\right) = 0{,}95$.

    **2.** $P(M \cap T) = 0{,}04 \times 0{,}9 = 0{,}036$ ; $P\left(\overline{M} \cap T\right) = 0{,}96 \times 0{,}05 = 0{,}048$.

    **3.** $P(T) = 0{,}036 + 0{,}048 = 0{,}084$.

    **4.** Malades $400$ : $360$ positifs, $40$ négatifs. Non malades $9\,600$ : $480$ positifs, $9\,120$ négatifs. Positifs : $840$. $P_T(M) = \frac{360}{840} = \frac{3}{7} \approx 0{,}43$.

    **5.** Moins d'une personne testée positive sur deux est malade : le test est utile pour dépister, mais un résultat positif doit être confirmé par un autre examen.
