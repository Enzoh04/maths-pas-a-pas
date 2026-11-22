# Exercices corrigés — Probabilités

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf les exercices Python.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Lois de probabilité, équiprobabilité | 1 à 6 |
| 2. Contraire, réunion, intersection | 7 à 11 |
| 3. Tableaux et arbres | 12 à 17 |
| 4. Probabilités conditionnelles | 18 à 23 |
| 5. Simulation et approfondissement | 24 à 28 |

---

## Thème 1 — Lois de probabilité, équiprobabilité

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-une-probabilite-en-situation-dequiprobabilite).*

### Exercice 1 — Un dé <span class="etoiles">★</span>

On lance un dé équilibré à six faces. Calculer la probabilité des événements : $A$ « obtenir $5$ » ; $B$ « obtenir un nombre premier » ; $C$ « obtenir au moins $3$ ».

??? success "Correction"
    $P(A) = \frac{1}{6}$ ; $B = \{2, 3, 5\}$, $P(B) = \frac{1}{2}$ ; $C = \{3, 4, 5, 6\}$, $P(C) = \frac{2}{3}$.

### Exercice 2 — Une urne <span class="etoiles">★</span>

Une urne contient $4$ boules rouges, $5$ vertes et $3$ bleues. On tire une boule au hasard. Calculer la probabilité de tirer une boule rouge, puis une boule qui n'est pas verte.

??? success "Correction"
    $\frac{4}{12} = \frac{1}{3}$ ; $\frac{7}{12}$.

### Exercice 3 — Compléter une loi <span class="etoiles">★</span>

Une roue est partagée en secteurs jaune, rouge, bleu et vert. Les probabilités d'obtenir jaune, rouge et bleu sont $0{,}15$, $0{,}3$ et $0{,}25$. Quelle est la probabilité d'obtenir vert ? Les issues sont-elles équiprobables ?

??? success "Correction"
    $1 - 0{,}15 - 0{,}3 - 0{,}25 = 0{,}3$. Non, les probabilités sont différentes.

### Exercice 4 — Un dé truqué <span class="etoiles">★★</span>

Un dé est truqué : la probabilité d'obtenir une face est proportionnelle au numéro de cette face ($P(k) = c \times k$).

1. Déterminer $c$.
2. Calculer la probabilité d'obtenir un nombre pair.

??? success "Correction"
    1. $c(1 + 2 + \cdots + 6) = 21c = 1$, donc $c = \frac{1}{21}$.
    2. $\frac{2 + 4 + 6}{21} = \frac{12}{21} = \frac{4}{7}$.

### Exercice 5 — Choisir un nombre <span class="etoiles">★★</span>

On choisit au hasard un entier entre $1$ et $100$. Calculer la probabilité qu'il soit : un multiple de $6$ ; un carré parfait ; un multiple de $6$ et un carré parfait.

??? success "Correction"
    Multiples de $6$ : $6, \ldots, 96$, soit $16$ nombres : $0{,}16$. Carrés : $1, 4, \ldots, 100$, soit $10$ nombres : $0{,}1$. Les deux : un carré parfait multiple de $6$ est le carré d'un multiple de $6$ (car $2$ et $3$ doivent diviser $n$) ; seul $36$ convient ($12^2 = 144 > 100$) : $0{,}01$.

### Exercice 6 — Le loto simplifié <span class="etoiles">★★★</span>

On choisit au hasard $2$ numéros **différents** parmi $1, 2, 3, 4, 5$ (l'ordre ne compte pas).

1. Lister toutes les paires possibles. Combien y en a-t-il ?
2. Quelle est la probabilité que la paire contienne le $5$ ? que la somme des deux numéros soit paire ?

??? success "Correction"
    1. $\{1,2\}, \{1,3\}, \{1,4\}, \{1,5\}, \{2,3\}, \{2,4\}, \{2,5\}, \{3,4\}, \{3,5\}, \{4,5\}$ : $10$ paires.
    2. Avec le $5$ : $4$ paires, $P = 0{,}4$. Somme paire (deux impairs ou deux pairs) : $\{1,3\}, \{1,5\}, \{3,5\}, \{2,4\}$, $P = 0{,}4$.

---

## Thème 2 — Contraire, réunion, intersection

*Méthode associée : [Méthode 2](methodes.md#methode-2-utiliser-le-contraire-la-reunion-et-lintersection).*

### Exercice 7 — Avec la formule <span class="etoiles">★</span>

On sait que $P(A) = 0{,}5$, $P(B) = 0{,}4$ et $P(A \cap B) = 0{,}15$. Calculer $P(A \cup B)$, $P\left(\overline{A}\right)$ et $P\left(\overline{A \cup B}\right)$.

??? success "Correction"
    $0{,}75$ ; $0{,}5$ ; $0{,}25$.

### Exercice 8 — Des cartes <span class="etoiles">★</span>

On tire une carte d'un jeu de $32$ cartes. $F$ : « c'est une figure » (valet, dame, roi), $P$ : « c'est un pique ». Calculer $P(F)$, $P(P)$, $P(F \cap P)$ et $P(F \cup P)$.

??? success "Correction"
    $\frac{12}{32} = \frac{3}{8}$ ; $\frac{8}{32} = \frac{1}{4}$ ; $\frac{3}{32}$ ; $\frac{12 + 8 - 3}{32} = \frac{17}{32}$.

### Exercice 9 — Incompatibles ? <span class="etoiles">★</span>

On lance un dé. $A$ : « obtenir $1$ ou $2$ », $B$ : « obtenir un nombre pair », $C$ : « obtenir $5$ ». Quels couples d'événements sont incompatibles ? Calculer $P(A \cup C)$.

??? success "Correction"
    $A \cap B = \{2\}$ : pas incompatibles. $A \cap C = \varnothing$ et $B \cap C = \varnothing$ : incompatibles. $P(A \cup C) = \frac{2}{6} + \frac{1}{6} = \frac{1}{2}$.

### Exercice 10 — Retrouver une probabilité <span class="etoiles">★★</span>

On sait que $P(A) = 0{,}6$, $P(B) = 0{,}5$ et $P(A \cup B) = 0{,}8$. Calculer $P(A \cap B)$. Les événements $A$ et $B$ sont-ils incompatibles ?

??? success "Correction"
    $P(A \cap B) = 0{,}6 + 0{,}5 - 0{,}8 = 0{,}3 \neq 0$ : non incompatibles.

### Exercice 11 — Langues vivantes <span class="etoiles">★★★</span>

Dans un lycée, $70\,\%$ des élèves étudient l'espagnol, $45\,\%$ l'allemand, et chaque élève étudie au moins l'une des deux langues.

1. Quelle est la proportion d'élèves qui étudient les deux langues ?
2. Quelle est la probabilité qu'un élève choisi au hasard étudie l'espagnol mais pas l'allemand ?

??? success "Correction"
    1. $P(E \cup A) = 1$, donc $P(E \cap A) = 0{,}7 + 0{,}45 - 1 = 0{,}15$.
    2. $P(E) - P(E \cap A) = 0{,}7 - 0{,}15 = 0{,}55$.

---

## Thème 3 — Tableaux et arbres

*Méthode associée : [Méthode 3](methodes.md#methode-3-utiliser-un-tableau-a-double-entree-ou-un-arbre).*

### Exercice 12 — Somme de deux dés <span class="etoiles">★</span>

On lance deux dés équilibrés et on note la somme. Construire le tableau des $36$ sommes, puis calculer la probabilité d'obtenir $8$, une somme d'au plus $4$, et un double.

??? success "Correction"
    Somme $8$ : $(2,6), (3,5), (4,4), (5,3), (6,2)$, soit $\frac{5}{36}$. Au plus $4$ : sommes $2$ (1 case), $3$ (2 cases), $4$ (3 cases), soit $\frac{6}{36} = \frac{1}{6}$. Double : $\frac{6}{36} = \frac{1}{6}$.

### Exercice 13 — Somme la plus fréquente <span class="etoiles">★★</span>

Avec le tableau de l'exercice 12, quelle est la somme la plus probable ? Quelle est la probabilité que la somme soit au moins égale à $10$ ?

??? success "Correction"
    La somme $7$ ($6$ cases, probabilité $\frac{1}{6}$). Au moins $10$ : $10$ ($3$), $11$ ($2$), $12$ ($1$), soit $\frac{6}{36} = \frac{1}{6}$.

### Exercice 14 — Deux tirages avec remise <span class="etoiles">★</span>

Une urne contient $3$ boules blanches et $2$ noires. On tire une boule, on la remet, puis on en tire une seconde. Calculer la probabilité de tirer deux boules blanches, puis deux boules de couleurs différentes.

??? success "Correction"
    $5 \times 5 = 25$ couples équiprobables. Deux blanches : $3 \times 3 = 9$, soit $\frac{9}{25}$. Couleurs différentes : $3 \times 2 + 2 \times 3 = 12$, soit $\frac{12}{25}$.

### Exercice 15 — Sans remise <span class="etoiles">★★</span>

Même urne, mais sans remise. Calculer les mêmes probabilités.

??? success "Correction"
    $5 \times 4 = 20$ couples ordonnés équiprobables. Deux blanches : $3 \times 2 = 6$, soit $\frac{6}{20} = \frac{3}{10}$. Couleurs différentes : $3 \times 2 + 2 \times 3 = 12$, soit $\frac{12}{20} = \frac{3}{5}$.

### Exercice 16 — Code à trois chiffres <span class="etoiles">★★</span>

Un code est formé de $3$ chiffres, chacun étant $0$ ou $1$, choisis au hasard. Construire l'arbre. Quelle est la probabilité que le code contienne exactement deux « $1$ » ? au moins un « $1$ » ?

??? success "Correction"
    $8$ codes équiprobables. Exactement deux $1$ : $011$, $101$, $110$, soit $\frac{3}{8}$. Au moins un $1$ : $1 - P(000) = \frac{7}{8}$.

### Exercice 17 — Menu au restaurant <span class="etoiles">★★★</span>

Un restaurant propose $3$ entrées, $4$ plats et $2$ desserts. Un client choisit un menu complet au hasard.

1. Combien y a-t-il de menus possibles ?
2. Le client est végétarien : une seule entrée et un seul plat lui conviennent. Quelle est la probabilité que le menu tiré au hasard lui convienne entièrement ?

??? success "Correction"
    1. $3 \times 4 \times 2 = 24$.
    2. Menus convenables : $1 \times 1 \times 2 = 2$, soit $\frac{2}{24} = \frac{1}{12}$.

---

## Thème 4 — Probabilités conditionnelles

*Méthodes associées : [Méthode 4](methodes.md#methode-4-calculer-une-probabilite-conditionnelle-avec-un-tableau) et [Méthode 5](methodes.md#methode-5-construire-et-utiliser-un-arbre-pondere).*

### Exercice 18 — Lire un tableau <span class="etoiles">★</span>

| | Interne ($I$) | Externe | Total |
|---|---|---|---|
| Seconde ($S$) | $40$ | $160$ | $200$ |
| Première | $60$ | $140$ | $200$ |
| Total | $100$ | $300$ | $400$ |

On choisit un élève au hasard. Calculer $P(I)$, $P(S \cap I)$, $P_S(I)$ et $P_I(S)$.

??? success "Correction"
    $\frac{100}{400} = 0{,}25$ ; $\frac{40}{400} = 0{,}1$ ; $\frac{40}{200} = 0{,}2$ ; $\frac{40}{100} = 0{,}4$.

### Exercice 19 — Construire un tableau <span class="etoiles">★★</span>

$55\,\%$ des adhérents d'une médiathèque sont des femmes. $60\,\%$ des femmes et $40\,\%$ des hommes empruntent des romans. On choisit un adhérent au hasard. En construisant un tableau pour $1\,000$ adhérents, calculer la probabilité qu'il emprunte des romans, puis la probabilité que ce soit une femme sachant qu'il emprunte des romans.

??? success "Correction"
    Femmes $550$, dont $330$ lectrices de romans ; hommes $450$, dont $180$. Total : $510$, $P = 0{,}51$. $P_R(F) = \frac{330}{510} = \frac{11}{17} \approx 0{,}65$.

### Exercice 20 — Arbre pondéré <span class="etoiles">★★</span>

On reprend l'exercice 19. Construire l'arbre pondéré (premier niveau : femme/homme) et retrouver $P(F \cap R)$ et $P(R)$.

??? success "Correction"
    Branches $0{,}55$ et $0{,}45$, puis $0{,}6$ / $0{,}4$ et $0{,}4$ / $0{,}6$. $P(F \cap R) = 0{,}55 \times 0{,}6 = 0{,}33$ ; $P(R) = 0{,}33 + 0{,}45 \times 0{,}4 = 0{,}33 + 0{,}18 = 0{,}51$.

### Exercice 21 — Test de dépistage <span class="etoiles">★★</span>

Une maladie touche $5\,\%$ d'une population. Un test a une sensibilité de $90\,\%$ et une spécificité de $80\,\%$. On considère $1\,000$ personnes.

1. Compléter un tableau croisé (malade ou non, test positif ou non).
2. Calculer la valeur prédictive positive $P_T(M)$.

??? success "Correction"
    1. Malades $50$ : $45$ positifs, $5$ négatifs. Non malades $950$ : $190$ positifs ($20\,\%$), $760$ négatifs. Positifs : $235$.
    2. $\frac{45}{235} = \frac{9}{47} \approx 0{,}19$.

### Exercice 22 — Sans remise et conditionnement <span class="etoiles">★★</span>

Une urne contient $4$ boules rouges et $6$ vertes. On tire deux boules sans remise. Construire l'arbre pondéré et calculer la probabilité d'obtenir deux boules rouges, puis la probabilité que la seconde soit rouge.

??? success "Correction"
    $P(R_1 \cap R_2) = \frac{4}{10} \times \frac{3}{9} = \frac{2}{15}$. Seconde rouge : $\frac{4}{10} \times \frac{3}{9} + \frac{6}{10} \times \frac{4}{9} = \frac{12 + 24}{90} = \frac{2}{5}$.

### Exercice 23 — Faux positifs <span class="etoiles">★★★</span>

Une maladie rare touche $1$ personne sur $1\,000$. Un test a une sensibilité de $99\,\%$ et une spécificité de $99\,\%$.

1. Sur $100\,000$ personnes, combien de malades sont détectés ? Combien de personnes saines ont un test positif ?
2. En déduire la probabilité qu'une personne testée positive soit malade. Commenter.

??? success "Correction"
    1. $100$ malades, dont $99$ détectés. $99\,900$ personnes saines, dont $1\,\%$, soit $999$, ont un test positif.
    2. $\frac{99}{99 + 999} = \frac{99}{1\,098} \approx 0{,}09$. Moins de $10\,\%$ ! Pour une maladie rare, même un excellent test donne surtout des faux positifs : il faut confirmer par un second examen.

---

## Thème 5 — Simulation et approfondissement

### Exercice 24 — Simuler une pièce <span class="etoiles">★★</span>

Écrire une fonction `frequence_pile(n)` qui simule $n$ lancers d'une pièce équilibrée et renvoie la fréquence de « pile ». Que constate-t-on pour $n = 10$, $100$, $10\,000$ ?

??? success "Correction"
    ```python
    from random import randint

    def frequence_pile(n):
        nb = 0
        for i in range(n):
            if randint(0, 1) == 1:
                nb = nb + 1
        return nb / n
    ```

    Pour $n = 10$, la fréquence varie beaucoup d'une simulation à l'autre ; pour $n = 10\,000$, elle est très proche de $0{,}5$.

### Exercice 25 — Simuler deux dés <span class="etoiles">★★</span>

Écrire une fonction qui simule $n$ lancers de deux dés et renvoie la fréquence de la somme $7$. Comparer avec la probabilité théorique.

??? success "Correction"
    ```python
    from random import randint

    def frequence_7(n):
        nb = 0
        for i in range(n):
            if randint(1, 6) + randint(1, 6) == 7:
                nb = nb + 1
        return nb / n

    print(frequence_7(100000))   # proche de 1/6 = 0.1667
    ```

### Exercice 26 — Estimer une probabilité <span class="etoiles">★★</span>

On lance $2\,000$ fois une punaise : elle tombe $1\,240$ fois sur la tête. Proposer une estimation de la probabilité qu'elle tombe sur la tête. Peut-on calculer cette probabilité exactement ?

??? success "Correction"
    $\frac{1\,240}{2\,000} = 0{,}62$. On ne peut pas la calculer par un raisonnement (pas d'équiprobabilité) : on l'**estime** par la fréquence observée sur un grand nombre de lancers.

### Exercice 27 — Le jeu de Franc-Carreau <span class="etoiles">★★★</span>

On lance au hasard une pièce de rayon $1$ cm sur un carrelage de carreaux carrés de $6$ cm de côté. On gagne si la pièce tombe entièrement à l'intérieur d'un carreau. On admet que le centre de la pièce tombe au hasard dans un carreau, avec une probabilité proportionnelle aux aires.

1. Où doit tomber le centre pour gagner ?
2. En déduire la probabilité de gagner.

??? success "Correction"
    1. À plus de $1$ cm de chaque bord : dans le carré central de côté $6 - 2 = 4$ cm.
    2. $\frac{4^2}{6^2} = \frac{16}{36} = \frac{4}{9}$.

### Exercice 28 — Le problème des anniversaires <span class="etoiles">★★★</span>

On considère un groupe de $4$ personnes, dont les mois de naissance sont supposés équiprobables et indépendants (parmi $12$ mois).

1. Combien y a-t-il de suites possibles de $4$ mois de naissance ?
2. Combien de ces suites comportent $4$ mois tous différents ? En déduire la probabilité qu'au moins deux personnes soient nées le même mois.
3. Écrire un programme Python qui simule cette situation et estime la probabilité. *(On admettra que pour $23$ personnes et $365$ jours, la probabilité qu'au moins deux personnes aient le même anniversaire dépasse $\frac{1}{2}$.)*

??? success "Correction"
    1. $12^4 = 20\,736$.
    2. $12 \times 11 \times 10 \times 9 = 11\,880$. Probabilité que tous les mois soient différents : $\frac{11\,880}{20\,736} = \frac{55}{96}$. Au moins deux le même mois : $1 - \frac{55}{96} = \frac{41}{96} \approx 0{,}43$.
    3. Programme de simulation :

    ```python
    from random import randint

    def meme_mois():
        mois = [randint(1, 12) for i in range(4)]
        for i in range(4):
            for j in range(i + 1, 4):
                if mois[i] == mois[j]:
                    return True
        return False

    N = 100000
    print(sum(meme_mois() for k in range(N)) / N)   # environ 0.43
    ```
