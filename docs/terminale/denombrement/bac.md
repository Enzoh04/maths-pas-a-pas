# Sujets type bac — Combinatoire et dénombrement

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours. Au bac, le dénombrement apparaît souvent à l'intérieur d'un exercice de probabilités.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Digicode | $k$-uplets, arrangements, complémentaire, combinaisons, Python |
| 2 | Délégation d'élèves | combinaisons avec conditions, identité par dénombrement |
| 3 | QCM | formules, choix du modèle |
| 4 | Mains de cartes et probabilités | combinaisons, complémentaire, équiprobabilité |

## Sujet 1 — Digicode

Le code d'un digicode est formé de 4 chiffres (de 0 à 9) suivis d'une lettre parmi A, B et C. Par exemple : 0472B.

1. Combien de codes différents peut-on former ?
2. Combien de codes ont leurs 4 chiffres deux à deux distincts ?
3. Combien de codes contiennent au moins un chiffre 0 ?
4. Combien de codes ont leurs 4 chiffres rangés dans l'ordre strictement croissant (comme 1358A) ?
5. Écrire un programme Python qui vérifie le résultat de la question 3 en parcourant tous les codes.

??? success "Correction"
    **1.** $4$-uplet de chiffres, puis une lettre : $10^4 \times 3 = 30\,000$ codes.

    **2.** $10 \times 9 \times 8 \times 7 \times 3 = 15\,120$ codes.

    **3.** Codes sans aucun $0$ : $9^4 \times 3 = 19\,683$. Donc $30\,000 - 19\,683 = 10\,317$ codes contiennent au moins un $0$.

    **4.** Choisir 4 chiffres distincts, sans ordre, détermine un unique rangement croissant : il y a $\binom{10}{4} = 210$ choix de chiffres, puis $3$ lettres : $630$ codes.

    **5.**

    ```python
    compteur = 0
    for n in range(10000):              # les 4 chiffres, de 0000 à 9999
        if "0" in str(n).zfill(4):      # zfill complète à 4 chiffres
            compteur = compteur + 1
    print(compteur * 3)                 # 3 lettres possibles : 10317
    ```

---

## Sujet 2 — Délégation d'élèves

Une classe compte 18 filles et 12 garçons. On forme une délégation de 5 élèves.

1. Combien de délégations différentes peut-on former ?
2. Combien de délégations comportent exactement 3 filles ?
3. Combien de délégations comportent au moins un garçon ?
4. On désigne maintenant un président de la délégation, choisi parmi ses 5 membres. En comptant de deux façons différentes le nombre de délégations avec président, montrer que $5\binom{30}{5} = 30\binom{29}{4}$.
5. Généraliser : démontrer que pour $1 \leq k \leq n$, $k\binom{n}{k} = n\binom{n - 1}{k - 1}$.

??? success "Correction"
    **1.** $\binom{30}{5} = 142\,506$.

    **2.** $\binom{18}{3} \times \binom{12}{2} = 816 \times 66 = 53\,856$.

    **3.** Délégations sans garçon (que des filles) : $\binom{18}{5} = 8\,568$. Donc $142\,506 - 8\,568 = 133\,938$.

    **4.** *Première façon* : on choisit la délégation ($\binom{30}{5}$), puis le président parmi ses 5 membres : $5\binom{30}{5}$.

    *Seconde façon* : on choisit d'abord le président parmi les 30 élèves, puis les 4 autres membres parmi les 29 restants : $30\binom{29}{4}$.

    Les deux nombres comptent le même ensemble : ils sont égaux (ils valent $712\,530$).

    **5.** Même raisonnement, avec un groupe de $n$ personnes et des comités de $k$ membres. Par le calcul : $k\binom{n}{k} = \frac{n!}{(k - 1)!\,(n - k)!} = n\binom{n - 1}{k - 1}$.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** $\binom{7}{3}$ est égal à :

a) $21$ — b) $35$ — c) $210$ — d) $343$

**Question 2.** Le nombre d'anagrammes du mot LYCEE est :

a) $24$ — b) $60$ — c) $120$ — d) $3\,125$

**Question 3.** Le nombre de parties d'un ensemble à 6 éléments est :

a) $6$ — b) $36$ — c) $64$ — d) $720$

**Question 4.** Huit coureurs disputent une course. Le nombre de podiums (or, argent, bronze) possibles est :

a) $24$ — b) $56$ — c) $336$ — d) $512$

**Question 5.** Un entier $n \geq 2$ vérifie $\binom{n}{2} = 45$. Alors $n$ vaut :

a) $9$ — b) $10$ — c) $15$ — d) $45$

??? success "Correction"
    **Question 1 : b).** $\frac{7 \times 6 \times 5}{6} = 35$.

    **Question 2 : b).** 5 lettres, dont deux E : $\frac{5!}{2!} = 60$.

    **Question 3 : c).** $2^6 = 64$.

    **Question 4 : c).** Arrangements : $8 \times 7 \times 6 = 336$.

    **Question 5 : b).** $\frac{n(n - 1)}{2} = 45 \iff n^2 - n - 90 = 0 \iff (n - 10)(n + 9) = 0$, et $n \geq 2$ donne $n = 10$.

---

## Sujet 4 — Mains de cartes

On tire simultanément 5 cartes d'un jeu de 32 cartes (8 hauteurs : 7, 8, 9, 10, valet, dame, roi, as ; 4 couleurs : cœur, carreau, trèfle, pique). Chaque main a la même probabilité d'être tirée.

1. Combien y a-t-il de mains possibles ?
2. Combien de mains contiennent exactement deux as ?
3. Combien de mains ne contiennent aucun cœur ? En déduire le nombre de mains contenant au moins un cœur.
4. Combien de mains contiennent 5 cartes de la même couleur ?
5. En situation d'équiprobabilité, la probabilité d'un événement est le quotient du nombre de cas favorables par le nombre de cas possibles. Calculer, à $10^{-3}$ près, la probabilité d'obtenir au moins un cœur, puis celle d'obtenir exactement deux as.

??? success "Correction"
    **1.** $\binom{32}{5} = 201\,376$ mains.

    **2.** On choisit 2 as parmi 4, et 3 cartes parmi les 28 qui ne sont pas des as : $\binom{4}{2}\binom{28}{3} = 6 \times 3\,276 = 19\,656$.

    **3.** Sans cœur, on choisit parmi les 24 autres cartes : $\binom{24}{5} = 42\,504$. Au moins un cœur : $201\,376 - 42\,504 = 158\,872$.

    **4.** On choisit la couleur ($4$), puis 5 cartes parmi les 8 de cette couleur : $4\binom{8}{5} = 4 \times 56 = 224$.

    **5.** $P(\text{au moins un cœur}) = \frac{158\,872}{201\,376} \approx 0{,}789$. $P(\text{exactement deux as}) = \frac{19\,656}{201\,376} \approx 0{,}098$.
