# Exercices corrigés — Information chiffrée et statistiques

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions d'un devoir, va voir les [évaluations type](bac.md). Les exercices se font **sans calculatrice**, sauf mention contraire.

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Proportions | 1 à 5 |
| 2. Évolutions | 6 à 12 |
| 3. Médiane, quartiles, moyenne | 13 à 18 |
| 4. Dispersion, séries en classes | 19 à 23 |
| 5. Tableaux croisés et approfondissement | 24 à 28 |

---

## Thème 1 — Proportions

*Méthode associée : [Méthode 1](methodes.md#methode-1-calculer-avec-des-proportions).*

### Exercice 1 — Calculer une proportion <span class="etoiles">★</span>

Dans une classe de $32$ élèves, $12$ ont choisi l'option latin. Quelle est la proportion de latinistes, en fraction irréductible puis en pourcentage ?

??? success "Correction"
    $\frac{12}{32} = \frac{3}{8} = 0{,}375$, soit $37{,}5\,\%$.

### Exercice 2 — Calculer un effectif <span class="etoiles">★</span>

$15\,\%$ des $1\,240$ élèves d'un lycée sont internes. Combien y a-t-il d'internes ?

??? success "Correction"
    $0{,}15 \times 1\,240 = 186$.

### Exercice 3 — Retrouver le total <span class="etoiles">★</span>

$84$ élèves, soit $35\,\%$ des élèves de Seconde, prennent l'option SES. Combien y a-t-il d'élèves de Seconde ?

??? success "Correction"
    $\frac{84}{0{,}35} = 240$.

### Exercice 4 — Proportion de proportion <span class="etoiles">★★</span>

En France, environ $52\,\%$ des habitants sont des femmes, et $21\,\%$ des femmes ont plus de $65$ ans. Quelle proportion de la population est formée de femmes de plus de $65$ ans ?

??? success "Correction"
    $0{,}52 \times 0{,}21 = 0{,}1092$, soit environ $10{,}9\,\%$.

### Exercice 5 — Moyenne de pourcentages <span class="etoiles">★★★</span>

Un lycée compte $300$ filles et $200$ garçons. $30\,\%$ des filles et $45\,\%$ des garçons font du sport en club.

1. Quelle est la proportion d'élèves du lycée qui font du sport en club ?
2. Pourquoi n'est-ce pas $\frac{30 + 45}{2} = 37{,}5\,\%$ ?

??? success "Correction"
    1. $0{,}3 \times 300 + 0{,}45 \times 200 = 90 + 90 = 180$ élèves sur $500$ : $36\,\%$.
    2. Les deux groupes n'ont pas le même effectif : il faut une **moyenne pondérée** par les effectifs, $\frac{300 \times 30 + 200 \times 45}{500} = 36$.

---

## Thème 2 — Évolutions

*Méthode associée : [Méthode 2](methodes.md#methode-2-calculer-avec-des-evolutions).*

### Exercice 6 — Coefficients multiplicateurs <span class="etoiles">★</span>

Donner le coefficient multiplicateur associé à : une hausse de $7\,\%$ ; une baisse de $12\,\%$ ; une hausse de $150\,\%$ ; une baisse de $100\,\%$. Inversement, quel taux correspond à $CM = 0{,}65$ ? à $CM = 2$ ?

??? success "Correction"
    $1{,}07$ ; $0{,}88$ ; $2{,}5$ ; $0$. $CM = 0{,}65$ : baisse de $35\,\%$ ; $CM = 2$ : hausse de $100\,\%$.

### Exercice 7 — Taux d'évolution <span class="etoiles">★</span>

Calculer le taux d'évolution : de $50$ à $62$ ; de $80$ à $68$ ; de $1{,}20$ à $1{,}50$.

??? success "Correction"
    $\frac{12}{50} = +24\,\%$ ; $\frac{-12}{80} = -15\,\%$ ; $\frac{0{,}3}{1{,}2} = +25\,\%$.

### Exercice 8 — Appliquer une évolution <span class="etoiles">★</span>

Un vélo coûte $340$ €. Calculer son prix après une hausse de $5\,\%$, puis son prix s'il avait subi une baisse de $15\,\%$.

??? success "Correction"
    $340 \times 1{,}05 = 357$ € ; $340 \times 0{,}85 = 289$ €.

### Exercice 9 — Évolutions successives <span class="etoiles">★★</span>

Le prix d'une action augmente de $5\,\%$ le lundi, baisse de $10\,\%$ le mardi, puis augmente de $20\,\%$ le mercredi. Quelle est l'évolution globale sur les trois jours ?

??? success "Correction"
    $1{,}05 \times 0{,}9 \times 1{,}2 = 1{,}134$ : hausse de $13{,}4\,\%$.

### Exercice 10 — Évolution réciproque <span class="etoiles">★★</span>

1. Un article est soldé à $-15\,\%$. De quel pourcentage faut-il augmenter le prix soldé pour revenir au prix initial ?
2. Un article soldé à $-30\,\%$ coûte $56$ €. Quel était son prix initial ?

??? success "Correction"
    1. $\frac{1}{0{,}85} \approx 1{,}1765$ : hausse d'environ $17{,}6\,\%$.
    2. $\frac{56}{0{,}7} = 80$ €.

### Exercice 11 — Intérêts composés <span class="etoiles">★★</span>

On place $5\,000$ € à $3\,\%$ par an (intérêts composés).

1. Quel est le capital au bout de $2$ ans ?
2. Quel est le taux d'évolution global sur $2$ ans ? Pourquoi n'est-il pas égal à $6\,\%$ ?

??? success "Correction"
    1. $5\,000 \times 1{,}03^2 = 5\,000 \times 1{,}0609 = 5\,304{,}50$ €.
    2. $+6{,}09\,\%$ : la deuxième année, les intérêts portent aussi sur les intérêts de la première année.

### Exercice 12 — Taux moyen <span class="etoiles">★★★</span>

Une population augmente de $21\,\%$ en deux ans. On cherche le taux annuel **moyen** $t$, c'est-à-dire le taux qui, appliqué deux fois, donne la même évolution globale.

1. Montrer que $(1 + t)^2 = 1{,}21$.
2. En déduire $t$. Est-ce la moitié de $21\,\%$ ?

??? success "Correction"
    1. Deux hausses de taux $t$ donnent un coefficient $(1 + t)^2$, qui doit valoir $1{,}21$.
    2. $1 + t = \sqrt{1{,}21} = 1{,}1$ (positif), donc $t = 10\,\%$, et non $10{,}5\,\%$.

---

## Thème 3 — Médiane, quartiles, moyenne

*Méthodes associées : [Méthode 3](methodes.md#methode-3-calculer-la-mediane-et-les-quartiles) et [Méthode 4](methodes.md#methode-4-calculer-une-moyenne-et-un-ecart-type).*

### Exercice 13 — Une série simple <span class="etoiles">★</span>

Voici les notes de $8$ élèves : $12\,;\,15\,;\,8\,;\,11\,;\,14\,;\,9\,;\,13\,;\,10$. Calculer la moyenne, la médiane et l'étendue.

??? success "Correction"
    Rangées : $8\,;\,9\,;\,10\,;\,11\,;\,12\,;\,13\,;\,14\,;\,15$. Moyenne $\frac{92}{8} = 11{,}5$ ; médiane $\frac{11 + 12}{2} = 11{,}5$ ; étendue $7$.

### Exercice 14 — Tableau d'effectifs <span class="etoiles">★</span>

Nombre de frères et sœurs dans une classe :

| Valeur | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| Effectif | $4$ | $10$ | $8$ | $5$ | $3$ |

Calculer la moyenne, la médiane et les quartiles.

??? success "Correction"
    $N = 30$. Moyenne $\frac{0 + 10 + 16 + 15 + 12}{30} = \frac{53}{30} \approx 1{,}77$. Effectifs cumulés : $4, 14, 22, 27, 30$. Médiane : moyenne des rangs $15$ et $16$, qui valent $2$ : $Me = 2$. $Q_1$ : rang $\lceil 7{,}5 \rceil = 8$, valeur $1$. $Q_3$ : rang $\lceil 22{,}5 \rceil = 23$, valeur $3$.

### Exercice 15 — Moyenne pondérée <span class="etoiles">★</span>

Un élève a obtenu $12$ (coefficient $2$), $8$ (coefficient $1$) et $15$ (coefficient $3$). Calculer sa moyenne. Quelle note lui faudrait-il au prochain devoir (coefficient $2$) pour avoir $13$ de moyenne ?

??? success "Correction"
    $\frac{24 + 8 + 45}{6} = \frac{77}{6} \approx 12{,}83$. Avec une note $x$ : $\frac{77 + 2x}{8} = 13 \iff 2x = 27 \iff x = 13{,}5$.

### Exercice 16 — Effet d'une valeur extrême <span class="etoiles">★★</span>

Salaires mensuels (en €) dans une petite entreprise : $1\,800$, $1\,900$, $2\,000$, $2\,100$, $2\,200$ et $10\,000$ (le dirigeant).

1. Calculer la moyenne et la médiane.
2. Lequel de ces indicateurs décrit le mieux le salaire « typique » ?

??? success "Correction"
    1. Moyenne $\frac{20\,000}{6} \approx 3\,333$ € ; médiane $\frac{2\,000 + 2\,100}{2} = 2\,050$ €.
    2. La médiane : la moyenne est tirée vers le haut par le salaire du dirigeant, alors que cinq salariés sur six gagnent moins de $2\,300$ €.

### Exercice 17 — Linéarité de la moyenne <span class="etoiles">★★</span>

La moyenne d'une série de températures est $15$ °C. Quelle est la moyenne en degrés Fahrenheit ($F = 1{,}8C + 32$) ? Si l'écart type est $4$ °C, quel est-il en °F ?

??? success "Correction"
    $1{,}8 \times 15 + 32 = 59$ °F ; écart type $1{,}8 \times 4 = 7{,}2$ °F.

### Exercice 18 — Retrouver une valeur <span class="etoiles">★★★</span>

La moyenne de $5$ nombres est $12$. On ajoute un sixième nombre $x$ et la moyenne devient $13$. Trouver $x$. Peut-on dire comment évolue la médiane ?

??? success "Correction"
    Somme initiale $60$, nouvelle somme $78$ : $x = 18$. Pour la médiane, on ne peut rien dire sans connaître les valeurs : elle passe de la 3ᵉ valeur à la moyenne des 3ᵉ et 4ᵉ valeurs de la nouvelle série.

---

## Thème 4 — Dispersion, séries en classes

### Exercice 19 — Écart type <span class="etoiles">★</span>

Calculer la moyenne et l'écart type de la série $2\,;\,4\,;\,6\,;\,8$.

??? success "Correction"
    $\bar{x} = 5$ ; $V = \frac{9 + 1 + 1 + 9}{4} = 5$ ; $\sigma = \sqrt{5} \approx 2{,}24$.

### Exercice 20 — Comparer deux séries <span class="etoiles">★★</span>

Deux élèves ont les notes suivantes. Alice : $10\,;\,10\,;\,11\,;\,9\,;\,10$. Bilal : $4\,;\,16\,;\,8\,;\,14\,;\,8$. Comparer leurs moyennes, puis leurs écarts types (sans les calculer exactement pour Bilal). Commenter.

??? success "Correction"
    Moyennes : $10$ et $10$. Les notes d'Alice sont toutes proches de $10$ (écart type faible, $\sqrt{0{,}4} \approx 0{,}63$) ; celles de Bilal sont très dispersées ($V = \frac{36 + 36 + 4 + 16 + 4}{5} = 19{,}2$, $\sigma \approx 4{,}38$). Même moyenne, régularité très différente.

### Exercice 21 — Diagramme en boîte <span class="etoiles">★★</span>

Une série a pour minimum $2$, maximum $20$, $Q_1 = 6$, médiane $9$, $Q_3 = 14$.

1. Tracer le diagramme en boîte et calculer l'écart interquartile.
2. Peut-on affirmer qu'au moins la moitié des valeurs sont comprises entre $6$ et $14$ ?

??? success "Correction"
    1. Écart interquartile $14 - 6 = 8$.
    2. Oui, environ la moitié (au moins $75\,\% - 25\,\% = 50\,\%$ des valeurs, aux arrondis de rang près, sont dans $[Q_1\,;\,Q_3]$).

### Exercice 22 — Série en classes <span class="etoiles">★★</span>

Notes d'un examen, regroupées en classes :

| Classe | $[50\,;\,60[$ | $[60\,;\,70[$ | $[70\,;\,80[$ | $[80\,;\,90[$ |
|---|---|---|---|---|
| Effectif | $2$ | $6$ | $9$ | $3$ |

Calculer une valeur approchée de la moyenne, et la fréquence des notes d'au moins $70$.

??? success "Correction"
    Centres $55, 65, 75, 85$ : $\bar{x} \approx \frac{110 + 390 + 675 + 255}{20} = \frac{1\,430}{20} = 71{,}5$. Fréquence : $\frac{12}{20} = 60\,\%$.

### Exercice 23 — Calculs en Python <span class="etoiles">★★★</span>

1. Écrire une fonction `moyenne_ponderee(valeurs, effectifs)` qui prend deux listes de même longueur.
2. Écrire une fonction `quartile1(L)` qui renvoie le premier quartile d'une liste (avec la définition du cours).
3. Tester avec l'exercice 14.

??? success "Correction"
    ```python
    from math import ceil

    def moyenne_ponderee(valeurs, effectifs):
        total = sum(v * n for v, n in zip(valeurs, effectifs))
        return total / sum(effectifs)

    def quartile1(L):
        T = sorted(L)
        rang = ceil(len(T) / 4)      # premier entier >= N/4
        return T[rang - 1]           # les indices commencent à 0

    vals, effs = [0, 1, 2, 3, 4], [4, 10, 8, 5, 3]
    print(moyenne_ponderee(vals, effs))          # 1.766...
    serie = []
    for v, n in zip(vals, effs):
        serie = serie + [v] * n
    print(quartile1(serie))                      # 1
    ```

---

## Thème 5 — Tableaux croisés et approfondissement

*Méthode associée : [Méthode 5](methodes.md#methode-5-exploiter-un-tableau-croise).*

### Exercice 24 — Compléter et lire <span class="etoiles">★</span>

Dans un club de $200$ adhérents, $120$ sont des adultes. $45$ adultes et $50$ jeunes pratiquent la compétition.

1. Construire le tableau croisé (adulte/jeune, compétition/loisir).
2. Calculer la fréquence marginale des compétiteurs, puis la fréquence des compétiteurs parmi les jeunes et parmi les adultes.

??? success "Correction"
    1. Adultes : $45$ compétition, $75$ loisir ; jeunes : $50$ compétition, $30$ loisir ; totaux $95$ et $105$.
    2. $\frac{95}{200} = 47{,}5\,\%$ ; parmi les jeunes : $\frac{50}{80} = 62{,}5\,\%$ ; parmi les adultes : $\frac{45}{120} = 37{,}5\,\%$.

### Exercice 25 — Dans l'autre sens <span class="etoiles">★★</span>

Avec le tableau de l'exercice 24, quelle est la proportion de jeunes parmi les compétiteurs ? Comparer avec la proportion de jeunes dans le club.

??? success "Correction"
    $\frac{50}{95} \approx 52{,}6\,\%$, contre $\frac{80}{200} = 40\,\%$ dans le club : les jeunes sont sur-représentés parmi les compétiteurs.

### Exercice 26 — Un test de dépistage <span class="etoiles">★★</span>

On teste $1\,000$ personnes : $50$ sont malades. Le test est positif pour $45$ malades et pour $95$ personnes non malades.

1. Construire le tableau croisé.
2. Parmi les personnes testées positives, quelle proportion est malade ?

??? success "Correction"
    1. Malades : $45$ positifs, $5$ négatifs. Non malades : $95$ positifs, $855$ négatifs. Positifs : $140$.
    2. $\frac{45}{140} \approx 32\,\%$ : moins d'un tiers des positifs sont malades.

### Exercice 27 — Paradoxe de Simpson <span class="etoiles">★★★</span>

Deux hôpitaux soignent des patients « légers » et « graves ».

| | Légers soignés | Légers guéris | Graves soignés | Graves guéris |
|---|---|---|---|---|
| Hôpital A | $100$ | $90$ | $400$ | $200$ |
| Hôpital B | $400$ | $340$ | $100$ | $40$ |

1. Calculer le taux de guérison de chaque hôpital pour les cas légers, puis pour les cas graves.
2. Calculer le taux de guérison global de chaque hôpital. Commenter.

??? success "Correction"
    1. Légers : A $90\,\%$, B $85\,\%$. Graves : A $50\,\%$, B $40\,\%$. A est meilleur dans les deux catégories.
    2. Global : A $\frac{290}{500} = 58\,\%$, B $\frac{380}{500} = 76\,\%$. B paraît meilleur globalement, parce qu'il soigne surtout des cas légers. Les taux globaux mélangent des populations différentes : il faut comparer les taux conditionnels.

### Exercice 28 — Indices <span class="etoiles">★★★</span>

Le prix d'un panier de courses vaut $80$ € en 2020 (indice $100$), $86$ € en 2022 et $92$ € en 2024.

1. Calculer les indices de 2022 et 2024 (base $100$ en 2020).
2. Quel est le taux d'évolution entre 2022 et 2024 ? Est-ce $8$ points de pourcentage ?

??? success "Correction"
    1. $\frac{86}{80} \times 100 = 107{,}5$ ; $\frac{92}{80} \times 100 = 115$.
    2. $\frac{92 - 86}{86} \approx 6{,}98\,\%$. L'indice a gagné $7{,}5$ **points**, mais le taux d'évolution est d'environ $7\,\%$ : un écart de points d'indice n'est un pourcentage que par rapport à la base $100$.
