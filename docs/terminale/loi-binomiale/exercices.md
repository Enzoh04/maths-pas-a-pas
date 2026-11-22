# Exercices corrigés — Succession d'épreuves indépendantes, loi binomiale

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché. Les valeurs décimales sont arrondies à $10^{-3}$ (ou $10^{-4}$ quand c'est utile) ; celles qui demandent une calculatrice sont signalées.

| Thème | Exercices |
|---|---|
| 1. Épreuves indépendantes et arbres | 1 à 5 |
| 2. Reconnaître et calculer une loi binomiale | 6 à 12 |
| 3. Espérance et variance | 13 à 17 |
| 4. Seuils et intervalles | 18 à 24 |
| 5. Approfondissement | 25 à 28 |

---

## Thème 1 — Épreuves indépendantes et arbres

*Méthode associée : [Méthode 5](methodes.md#methode-5-calculer-avec-des-epreuves-independantes-non-identiques).*

### Exercice 1 — Un dé puis une pièce <span class="etoiles">★</span>

On lance un dé équilibré à six faces, puis une pièce équilibrée. Calculer la probabilité d'obtenir : un $6$ puis Pile ; un nombre pair puis Face ; un nombre au moins égal à $5$ ou Pile.

??? success "Correction"
    Les deux épreuves sont indépendantes.

    - $P(\text{6 et Pile}) = \frac{1}{6} \times \frac{1}{2} = \frac{1}{12}$.
    - $P(\text{pair et Face}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
    - Contraire : « au plus $4$ et Face », de probabilité $\frac{4}{6} \times \frac{1}{2} = \frac{1}{3}$. Donc la probabilité cherchée vaut $\frac{2}{3}$.

### Exercice 2 — Tirages avec remise <span class="etoiles">★</span>

Une urne contient $3$ boules rouges et $2$ boules vertes. On tire une boule, on note sa couleur, on la remet, puis on en tire une seconde. Calculer la probabilité d'obtenir deux boules rouges, puis une boule de chaque couleur.

??? success "Correction"
    Avec remise, les tirages sont indépendants. $P(RR) = \frac{3}{5} \times \frac{3}{5} = \frac{9}{25}$. Une de chaque couleur : $P(RV) + P(VR) = 2 \times \frac{3}{5} \times \frac{2}{5} = \frac{12}{25}$.

### Exercice 3 — Montage en série, montage en parallèle <span class="etoiles">★★</span>

Trois composants tombent en panne, indépendamment, avec les probabilités $0{,}1$, $0{,}05$ et $0{,}02$.

1. Montés **en série**, le système fonctionne si les trois fonctionnent. Calculer la probabilité qu'il fonctionne.
2. Montés **en parallèle**, il fonctionne si au moins un composant fonctionne. Même question.

??? success "Correction"
    **1.** $0{,}9 \times 0{,}95 \times 0{,}98 = 0{,}8379$.

    **2.** Le système est en panne si les trois le sont : $0{,}1 \times 0{,}05 \times 0{,}02 = 0{,}0001$. Il fonctionne avec probabilité $0{,}9999$.

### Exercice 4 — Avec ou sans remise ? <span class="etoiles">★★</span>

On reprend l'urne de l'exercice 2, mais on tire deux boules **sans remise**. Calculer la probabilité d'obtenir deux boules rouges. Pourquoi ne peut-on pas utiliser le modèle des épreuves indépendantes ?

??? success "Correction"
    Avec les probabilités conditionnelles : $P(RR) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$, différent de $\frac{9}{25}$. Le résultat du premier tirage modifie la composition de l'urne, donc les probabilités du second : les épreuves ne sont pas indépendantes.

### Exercice 5 — Un archer <span class="etoiles">★★</span>

Un archer tire trois flèches. Il atteint la cible avec probabilité $0{,}5$ au premier tir, $0{,}6$ au deuxième et $0{,}7$ au troisième, indépendamment.

1. Calculer la probabilité qu'il atteigne la cible exactement deux fois.
2. Calculer la probabilité qu'il l'atteigne au moins une fois.
3. Le nombre de tirs réussis suit-il une loi binomiale ?

??? success "Correction"
    **1.** Trois chemins (l'échec est au 3ᵉ, au 2ᵉ ou au 1ᵉʳ tir) :
    $$0{,}5 \times 0{,}6 \times 0{,}3 + 0{,}5 \times 0{,}4 \times 0{,}7 + 0{,}5 \times 0{,}6 \times 0{,}7 = 0{,}09 + 0{,}14 + 0{,}21 = 0{,}44.$$

    **2.** $1 - 0{,}5 \times 0{,}4 \times 0{,}3 = 0{,}94$.

    **3.** Non : les épreuves sont indépendantes, mais pas **identiques** (la probabilité de succès change).

---

## Thème 2 — Reconnaître et calculer une loi binomiale

*Méthodes associées : [Méthode 1](methodes.md#methode-1-justifier-quune-variable-suit-une-loi-binomiale) et [Méthode 2](methodes.md#methode-2-calculer-des-probabilites-binomiales).*

### Exercice 6 — Binomiale ou non ? <span class="etoiles">★</span>

Dans chaque cas, dire si $X$ suit une loi binomiale, et préciser ses paramètres le cas échéant.

1. On lance $10$ fois un dé équilibré ; $X$ est le nombre de $6$.
2. On tire sans remise $3$ cartes dans un jeu de $32$ ; $X$ est le nombre d'as.
3. On lance un dé jusqu'à obtenir un $6$ ; $X$ est le nombre de lancers.
4. Dans une maternité, on considère $4$ naissances indépendantes ; la probabilité d'un garçon est $0{,}51$ ; $X$ est le nombre de garçons.

??? success "Correction"
    1. Oui : $\mathcal{B}\left(10, \frac{1}{6}\right)$.
    2. Non : sans remise dans un petit jeu, les tirages ne sont pas indépendants.
    3. Non : $X$ ne compte pas des succès parmi un nombre fixé d'épreuves, et il n'est pas borné (c'est une loi géométrique).
    4. Oui : $\mathcal{B}(4\,;\,0{,}51)$.

### Exercice 7 — Calculs à la main <span class="etoiles">★</span>

Soit $X \sim \mathcal{B}(5\,;\,0{,}3)$. Calculer $P(X = 2)$, $P(X = 0)$ et $P(X \geq 1)$.

??? success "Correction"
    $P(X = 2) = \binom{5}{2} \times 0{,}3^2 \times 0{,}7^3 = 10 \times 0{,}09 \times 0{,}343 = 0{,}3087$.

    $P(X = 0) = 0{,}7^5 = 0{,}16807$, et $P(X \geq 1) = 1 - 0{,}16807 = 0{,}83193$.

### Exercice 8 — Répondre au hasard <span class="etoiles">★★</span>

Un QCM comporte $10$ questions, chacune avec $4$ réponses dont une seule est juste. Un candidat répond au hasard à toutes les questions.

1. Quelle est la loi du nombre $X$ de bonnes réponses ?
2. Calculer la probabilité exacte d'avoir exactement $5$ bonnes réponses.
3. Calculer (calculatrice) la probabilité d'avoir au moins $5$ bonnes réponses.

??? success "Correction"
    **1.** Dix questions, réponses au hasard de façon identique et indépendante, succès « bonne réponse » de probabilité $\frac{1}{4}$ : $X \sim \mathcal{B}\left(10, \frac{1}{4}\right)$.

    **2.** $P(X = 5) = \binom{10}{5}\left(\frac{1}{4}\right)^5\left(\frac{3}{4}\right)^5 = \frac{252 \times 243}{4^{10}} = \frac{61\,236}{1\,048\,576} \approx 0{,}058$.

    **3.** $P(X \geq 5) = 1 - P(X \leq 4) \approx 0{,}078$. Répondre au hasard ne permet pas d'avoir la moyenne !

### Exercice 9 — Loi complète <span class="etoiles">★</span>

On lance $4$ fois une pièce équilibrée et $X$ compte le nombre de Pile. Donner la loi de $X$ sous forme de tableau, puis son espérance.

??? success "Correction"
    $X \sim \mathcal{B}\left(4, \frac{1}{2}\right)$, donc $P(X = k) = \binom{4}{k} \times \frac{1}{16}$ :

    | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
    |---|---|---|---|---|---|
    | $P(X = k)$ | $\frac{1}{16}$ | $\frac{4}{16}$ | $\frac{6}{16}$ | $\frac{4}{16}$ | $\frac{1}{16}$ |

    $E(X) = 4 \times \frac{1}{2} = 2$. On retrouve les coefficients de la ligne $4$ du triangle de Pascal.

### Exercice 10 — Séance de penalties <span class="etoiles">★</span>

Un joueur réussit un penalty avec probabilité $0{,}8$, indépendamment d'un tir à l'autre. Il en tire $5$. Calculer la probabilité qu'il les réussisse tous, puis qu'il en réussisse au moins $4$.

??? success "Correction"
    $X \sim \mathcal{B}(5\,;\,0{,}8)$. $P(X = 5) = 0{,}8^5 = 0{,}32768$. $P(X = 4) = 5 \times 0{,}8^4 \times 0{,}2 = 0{,}4096$. Donc $P(X \geq 4) = 0{,}73728$.

### Exercice 11 — Contrôle de qualité <span class="etoiles">★★</span>

Une usine produit des pièces dont $3\,\%$ sont défectueuses. On prélève $50$ pièces dans une production très importante, ce qui revient à un tirage avec remise. Calculer (calculatrice) la probabilité qu'il n'y ait aucune pièce défectueuse, au plus $2$, puis plus de $2$.

??? success "Correction"
    $X \sim \mathcal{B}(50\,;\,0{,}03)$. $P(X = 0) = 0{,}97^{50} \approx 0{,}218$. $P(X \leq 2) \approx 0{,}811$. $P(X > 2) = 1 - P(X \leq 2) \approx 0{,}189$.

### Exercice 12 — Symétrie <span class="etoiles">★★</span>

Soit $X \sim \mathcal{B}(n, p)$ et $Y = n - X$.

1. Interpréter $Y$ et en déduire sa loi.
2. Le retrouver par le calcul.
3. Application : si $X \sim \mathcal{B}(12\,;\,0{,}9)$, exprimer $P(X \geq 10)$ à l'aide d'une variable de loi $\mathcal{B}(12\,;\,0{,}1)$.

??? success "Correction"
    **1.** $Y$ compte les échecs, c'est-à-dire les succès quand on échange les rôles : $Y \sim \mathcal{B}(n, 1 - p)$.

    **2.** $P(Y = k) = P(X = n - k) = \binom{n}{n-k}p^{n-k}(1-p)^{k} = \binom{n}{k}(1-p)^k p^{n-k}$.

    **3.** $P(X \geq 10) = P(Y \leq 2)$ avec $Y = 12 - X \sim \mathcal{B}(12\,;\,0{,}1)$.

---

## Thème 3 — Espérance et variance

*Méthode associée : [Méthode 3](methodes.md#methode-3-utiliser-lesperance-et-la-variance).*

### Exercice 13 — Paramètres <span class="etoiles">★</span>

Soit $X \sim \mathcal{B}(50\,;\,0{,}4)$. Calculer $E(X)$, $V(X)$ et $\sigma(X)$.

??? success "Correction"
    $E(X) = 20$, $V(X) = 50 \times 0{,}4 \times 0{,}6 = 12$, $\sigma(X) = \sqrt{12} = 2\sqrt{3} \approx 3{,}46$.

### Exercice 14 — Un jeu équitable ? <span class="etoiles">★★</span>

On paie $3$ € pour lancer $3$ fois une pièce équilibrée ; on reçoit $2$ € par Pile obtenu. Soit $G$ le gain algébrique. Exprimer $G$ en fonction du nombre $X$ de Pile, puis calculer $E(G)$. Le jeu est-il équitable ? Calculer $P(G > 0)$.

??? success "Correction"
    $G = 2X - 3$ avec $X \sim \mathcal{B}\left(3, \frac{1}{2}\right)$. $E(G) = 2 \times 1{,}5 - 3 = 0$ : le jeu est **équitable**. $G > 0 \iff X \geq 2$, de probabilité $\frac{3 + 1}{8} = \frac{1}{2}$.

### Exercice 15 — Retrouver les paramètres <span class="etoiles">★★</span>

Une variable $X$ suit une loi binomiale d'espérance $12$ et de variance $8{,}4$. Déterminer ses paramètres.

??? success "Correction"
    $np = 12$ et $np(1 - p) = 8{,}4$. En divisant : $1 - p = 0{,}7$, donc $p = 0{,}3$ et $n = \frac{12}{0{,}3} = 40$.

### Exercice 16 — Points négatifs au QCM <span class="etoiles">★★</span>

Un QCM a $20$ questions à $4$ réponses. Une bonne réponse rapporte $1$ point, une mauvaise en retire $\frac{1}{3}$. Un candidat répond au hasard ; $X$ est le nombre de bonnes réponses et $N$ sa note.

1. Exprimer $N$ en fonction de $X$.
2. Calculer $E(N)$. Pourquoi le concepteur a-t-il choisi la pénalité $\frac{1}{3}$ ?

??? success "Correction"
    **1.** $N = X - \frac{1}{3}(20 - X) = \frac{4X - 20}{3}$.

    **2.** $X \sim \mathcal{B}\left(20, \frac{1}{4}\right)$, $E(X) = 5$, donc $E(N) = \frac{20 - 20}{3} = 0$. Avec cette pénalité, répondre au hasard rapporte en moyenne $0$ point : le hasard n'est ni récompensé ni sanctionné.

### Exercice 17 — Variance maximale <span class="etoiles">★</span>

$n$ étant fixé, pour quelle valeur de $p$ la variance de $\mathcal{B}(n, p)$ est-elle maximale ?

??? success "Correction"
    $p \mapsto np(1 - p) = n(p - p^2)$ est un trinôme maximal en $p = \frac{1}{2}$, où il vaut $\frac{n}{4}$. Les résultats sont le plus dispersés quand succès et échec sont équiprobables.

---

## Thème 4 — Seuils et intervalles

*Méthodes associées : [Méthode 4](methodes.md#methode-4-resoudre-un-probleme-de-seuil) et [Méthode 6](methodes.md#methode-6-determiner-un-intervalle-et-prendre-une-decision).*

### Exercice 18 — Le problème du chevalier de Méré <span class="etoiles">★★</span>

Au XVIIᵉ siècle, le chevalier de Méré se demandait combien de fois il faut lancer deux dés pour avoir plus d'une chance sur deux d'obtenir au moins un double six. Répondre à sa question.

??? success "Correction"
    À chaque lancer, $P(\text{double six}) = \frac{1}{36}$. On veut $1 - \left(\frac{35}{36}\right)^n > \frac{1}{2}$, soit $\left(\frac{35}{36}\right)^n < \frac{1}{2}$, c'est-à-dire $n > \dfrac{\ln 0{,}5}{\ln(35/36)} \approx 24{,}6$. Il faut **$25$ lancers**. (Avec $24$ lancers, la probabilité vaut environ $0{,}491$ ; avec $25$, environ $0{,}506$.) Cette question, posée à Pascal, est à l'origine de sa correspondance avec Fermat, qui a fondé le calcul des probabilités.

### Exercice 19 — Combien de pièces contrôler ? <span class="etoiles">★</span>

Avec $3\,\%$ de pièces défectueuses, combien de pièces faut-il contrôler pour que la probabilité d'en trouver au moins une défectueuse soit supérieure ou égale à $0{,}5$ ?

??? success "Correction"
    $1 - 0{,}97^n \geq 0{,}5 \iff 0{,}97^n \leq 0{,}5 \iff n \geq \dfrac{\ln 0{,}5}{\ln 0{,}97} \approx 22{,}8$. Il faut au moins $23$ pièces.

### Exercice 20 — Une pièce lancée $100$ fois <span class="etoiles">★★</span>

On lance $100$ fois une pièce équilibrée. Calculer (calculatrice) la probabilité d'obtenir au plus $40$ Pile, puis entre $40$ et $60$ Pile (inclus).

??? success "Correction"
    $X \sim \mathcal{B}(100\,;\,0{,}5)$. $P(X \leq 40) \approx 0{,}028$. $P(40 \leq X \leq 60) = P(X \leq 60) - P(X \leq 39) \approx 0{,}982 - 0{,}018 \approx 0{,}965$.

### Exercice 21 — Construire un intervalle <span class="etoiles">★★</span>

Soit $X \sim \mathcal{B}(40\,;\,0{,}25)$. À l'aide du tableau des probabilités cumulées, déterminer l'intervalle $[a, b]$ défini dans le cours pour $\alpha = 0{,}05$, et calculer $P(a \leq X \leq b)$.

??? success "Correction"
    La calculatrice donne $P(X \leq 4) \approx 0{,}016$ et $P(X \leq 5) \approx 0{,}043$ : $a = 5$. Puis $P(X \leq 15) \approx 0{,}974$ et $P(X \leq 16) \approx 0{,}988$ : $b = 16$. Alors $P(5 \leq X \leq 16) = P(X \leq 16) - P(X \leq 4) \approx 0{,}972 \geq 0{,}95$.

### Exercice 22 — La pièce est-elle truquée ? <span class="etoiles">★★★</span>

On lance $100$ fois une pièce et l'on obtient $65$ Pile. On veut savoir si l'on peut considérer la pièce comme équilibrée.

1. Sous l'hypothèse « la pièce est équilibrée », déterminer l'intervalle $[a, b]$ à $95\,\%$ du cours.
2. Conclure.
3. Calculer (calculatrice) $P(X \geq 65)$ sous la même hypothèse, et commenter.

??? success "Correction"
    **1.** $X \sim \mathcal{B}(100\,;\,0{,}5)$. $P(X \leq 39) \approx 0{,}018$ et $P(X \leq 40) \approx 0{,}028$ : $a = 40$. $P(X \leq 59) \approx 0{,}972$ et $P(X \leq 60) \approx 0{,}982$ : $b = 60$.

    **2.** $65 \notin [40, 60]$ : on rejette l'hypothèse, au risque de $5\,\%$. La pièce semble truquée.

    **3.** $P(X \geq 65) = 1 - P(X \leq 64) \approx 0{,}0018$. Avec une pièce équilibrée, un résultat aussi extrême n'arrive qu'environ deux fois sur mille.

### Exercice 23 — Surréservation <span class="etoiles">★★★</span>

Un avion a $200$ places. La compagnie sait que chaque passager ayant réservé se présente avec probabilité $0{,}95$, indépendamment des autres. Elle vend $206$ billets.

1. Quelle est la loi du nombre $X$ de passagers qui se présentent ? Son espérance ?
2. Calculer (calculatrice) la probabilité que des passagers se présentent sans avoir de place.
3. La compagnie juge ce risque acceptable s'il est inférieur à $5\,\%$. Que penser de ce choix ?

??? success "Correction"
    **1.** $X \sim \mathcal{B}(206\,;\,0{,}95)$, $E(X) = 195{,}7$.

    **2.** $P(X > 200) = 1 - P(X \leq 200) \approx 0{,}052$.

    **3.** Le risque est d'environ $5{,}2\,\%$, juste au-dessus du seuil : il faudrait vendre un billet de moins. (Avec $205$ billets, on trouve environ $2{,}2\,\%$.)

### Exercice 24 — La valeur la plus probable <span class="etoiles">★★★</span>

Soit $X \sim \mathcal{B}(n, p)$ avec $0 < p < 1$ et $q = 1 - p$.

1. Montrer que pour $0 \leq k \leq n - 1$ : $\dfrac{P(X = k + 1)}{P(X = k)} = \dfrac{(n - k)\,p}{(k + 1)\,q}$.
2. En déduire que $P(X = k + 1) \geq P(X = k)$ si et seulement si $k \leq (n + 1)p - 1$.
3. Application : quelle est la valeur la plus probable de $X \sim \mathcal{B}(10\,;\,0{,}3)$ ? Comparer au diagramme du cours.

??? success "Correction"
    **1.** $\dfrac{\binom{n}{k+1}}{\binom{n}{k}} = \dfrac{n!}{(k+1)!\,(n-k-1)!} \times \dfrac{k!\,(n-k)!}{n!} = \dfrac{n - k}{k + 1}$, et les puissances donnent $\dfrac{p^{k+1}q^{n-k-1}}{p^k q^{n-k}} = \dfrac{p}{q}$.

    **2.** Le rapport est $\geq 1$ si et seulement si $(n - k)p \geq (k + 1)q$, soit $np - kp \geq kq + q$, soit $k \leq np - q = (n + 1)p - 1$ (car $p + q = 1$).

    **3.** $(n + 1)p - 1 = 2{,}3$. Les probabilités augmentent tant que $k \leq 2$, c'est-à-dire jusqu'à $P(X = 3)$, puis diminuent. La valeur la plus probable est $3$, avec $P(X = 3) \approx 0{,}267$, conforme au diagramme.

---

## Thème 5 — Approfondissement

### Exercice 25 — L'identité du comité <span class="etoiles">★★★</span>

Démontrer, en dénombrant de deux façons, que pour $1 \leq k \leq n$ : $k\binom{n}{k} = n\binom{n-1}{k-1}$. *On pourra compter les façons de former, dans un groupe de $n$ personnes, un comité de $k$ membres dont l'un est président.* Quel rôle joue cette identité dans le cours ?

??? success "Correction"
    **Première façon :** on choisit le comité ($\binom{n}{k}$ façons), puis son président parmi ses $k$ membres ($k$ façons) : $k\binom{n}{k}$.

    **Seconde façon :** on choisit d'abord le président parmi les $n$ personnes ($n$ façons), puis les $k - 1$ autres membres parmi les $n - 1$ restants : $n\binom{n-1}{k-1}$.

    On a compté la même chose : les deux nombres sont égaux. Cette identité est la clé de la démonstration directe de $E(X) = np$ (§ 4 du cours).

### Exercice 26 — Un match en trois sets gagnants <span class="etoiles">★★★</span>

Deux joueurs disputent un match : le premier qui gagne $3$ sets l'emporte (il y a donc au plus $5$ sets). Le joueur A gagne chaque set avec probabilité $0{,}6$, indépendamment.

1. On imagine que les $5$ sets sont toujours joués, même quand le match est déjà gagné. Justifier que A gagne le match si et seulement s'il gagne au moins $3$ des $5$ sets.
2. En déduire la probabilité que A gagne le match.

??? success "Correction"
    **1.** Si A gagne au moins $3$ sets sur $5$, B en gagne au plus $2$ : A atteint $3$ victoires le premier. Réciproquement, si A gagne le match, il a $3$ victoires à un moment, et les sets « fictifs » suivants n'y changent rien : il en a au moins $3$ sur $5$. Les sets fictifs ne modifient pas le vainqueur.

    **2.** Le nombre de sets gagnés sur $5$ suit $\mathcal{B}(5\,;\,0{,}6)$ :
    $$P(X \geq 3) = \binom{5}{3}0{,}6^3 \times 0{,}4^2 + \binom{5}{4}0{,}6^4 \times 0{,}4 + 0{,}6^5 = 0{,}3456 + 0{,}2592 + 0{,}07776 = 0{,}68256.$$
    Un léger avantage par set ($0{,}6$) devient un avantage plus net sur le match ($0{,}68$).

### Exercice 27 — Simuler une loi binomiale <span class="etoiles">★★</span>

1. Écrire une fonction Python `simule(n, p)` qui simule un schéma de Bernoulli et renvoie le nombre de succès.
2. Écrire un programme qui répète $10\,000$ fois la simulation pour $n = 10$, $p = 0{,}3$, et calcule la fréquence des résultats égaux à $3$. Comparer à $P(X = 3)$.

??? success "Correction"
    ```python
    from random import random

    def simule(n, p):
        succes = 0
        for i in range(n):
            if random() < p:      # succès avec probabilité p
                succes += 1
        return succes

    N = 10000
    compte = 0
    for i in range(N):
        if simule(10, 0.3) == 3:
            compte += 1
    print(compte / N)    # proche de 0.267
    ```

    $P(X = 3) = \binom{10}{3} \times 0{,}3^3 \times 0{,}7^7 \approx 0{,}267$. La fréquence observée en est proche, et s'en rapproche quand $N$ augmente : c'est la loi des grands nombres (chapitre 15).

### Exercice 28 — Un algorithme de seuil <span class="etoiles">★★</span>

Écrire une fonction Python `seuil(p, alpha)` qui renvoie le plus petit entier $n$ tel que la probabilité d'au moins un succès en $n$ épreuves soit au moins $1 - \alpha$, **sans utiliser le logarithme**. Vérifier avec l'exemple du dé du cours.

??? success "Correction"
    ```python
    def seuil(p, alpha):
        n = 1
        while (1 - p)**n > alpha:   # tant que P(aucun succès) est trop grande
            n += 1
        return n

    print(seuil(1/6, 0.01))   # 26
    ```

    La boucle s'arrête, car $(1 - p)^n$ tend vers $0$ quand $0 < p < 1$ (chapitre 1, suites géométriques).
