# Exercices corrigés — Concentration, loi des grands nombres

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Markov et Bienaymé-Tchebychev | 1 à 8 |
| 2. Inégalité de concentration et taille d'échantillon | 9 à 15 |
| 3. Loi des grands nombres | 16 à 21 |
| 4. Simulations en Python | 22 à 25 |
| 5. Approfondissement | 26 à 28 |

---

## Thème 1 — Markov et Bienaymé-Tchebychev

*Méthode associée : [Méthode 1](methodes.md#methode-1-appliquer-linegalite-de-bienayme-tchebychev).*

### Exercice 1 — Application directe <span class="etoiles">★</span>

$X$ a pour espérance $10$ et pour variance $4$.

1. Majorer $P\big(|X - 10| \geq 5\big)$.
2. Minorer $P(6 < X < 14)$.

??? success "Correction"
    **1.** $P\big(|X - 10| \geq 5\big) \leq \frac{4}{25} = 0{,}16$.

    **2.** $6 < X < 14 \iff |X - 10| < 4$, donc $P(6 < X < 14) \geq 1 - \frac{4}{16} = 0{,}75$.

### Exercice 2 — Inégalité de Markov <span class="etoiles">★</span>

Le nombre de clients d'un magasin un jour donné est une variable aléatoire $N$ d'espérance $120$. Majorer la probabilité qu'au moins $300$ clients viennent un jour donné.

??? success "Correction"
    $N$ est positive : $P(N \geq 300) \leq \frac{120}{300} = 0{,}4$. C'est une majoration grossière, mais elle n'utilise que l'espérance.

### Exercice 3 — En nombre d'écarts types <span class="etoiles">★</span>

Quelle que soit la loi de $X$, majorer la probabilité que $X$ s'écarte de son espérance d'au moins $3$ écarts types, puis d'au moins $10$ écarts types.

??? success "Correction"
    Avec $\delta = k\sigma$ : $P\big(|X - \mu| \geq k\sigma\big) \leq \frac{\sigma^2}{k^2\sigma^2} = \frac{1}{k^2}$. Pour $k = 3$ : $\frac{1}{9} \approx 0{,}111$ ; pour $k = 10$ : $0{,}01$.

### Exercice 4 — Comparer avec la valeur exacte <span class="etoiles">★★</span>

$X \sim \mathcal{B}(100\,;\,0{,}5)$.

1. Majorer $P\big(|X - 50| \geq 10\big)$ avec l'inégalité de Bienaymé-Tchebychev.
2. Calculer cette probabilité à la calculatrice et comparer.

??? success "Correction"
    **1.** $V = 25$ : $P\big(|X - 50| \geq 10\big) \leq \frac{25}{100} = 0{,}25$.

    **2.** $P(X \leq 40) + P(X \geq 60) = 2P(X \leq 40) \approx 0{,}057$ (par symétrie). Le majorant est environ quatre fois trop grand : l'inégalité est vraie, mais grossière.

### Exercice 5 — Une inégalité parfois atteinte <span class="etoiles">★★★</span>

$X$ prend les valeurs $-1$, $0$, $1$ avec les probabilités $\frac{1}{8}$, $\frac{3}{4}$, $\frac{1}{8}$.

1. Calculer $E(X)$ et $V(X)$.
2. Comparer $P\big(|X| \geq 1\big)$ et le majorant de Bienaymé-Tchebychev avec $\delta = 1$. Conclure.

??? success "Correction"
    **1.** $E(X) = 0$ par symétrie, $V(X) = E(X^2) = \frac{1}{8} + \frac{1}{8} = \frac{1}{4}$.

    **2.** $P\big(|X| \geq 1\big) = \frac{1}{4}$, et le majorant vaut $\frac{V}{1^2} = \frac{1}{4}$. Il y a égalité : on ne peut pas améliorer l'inégalité **en général**, même si elle est grossière pour la plupart des lois.

### Exercice 6 — Un dé <span class="etoiles">★★</span>

$X$ est le résultat d'un dé équilibré ($\mu = 3{,}5$, $V = \frac{35}{12}$). Comparer la valeur exacte de $P\big(|X - 3{,}5| \geq 2{,}5\big)$ et son majorant de Bienaymé-Tchebychev.

??? success "Correction"
    $|X - 3{,}5| \geq 2{,}5 \iff X \in \{1, 6\}$ : probabilité exacte $\frac{1}{3} \approx 0{,}333$. Majorant : $\frac{35/12}{6{,}25} \approx 0{,}467$.

### Exercice 7 — Trouver $\delta$ <span class="etoiles">★★</span>

$X$ a pour variance $9$. Déterminer un réel $\delta$ tel que $P\big(|X - \mu| \geq \delta\big) \leq 0{,}05$.

??? success "Correction"
    Il suffit que $\frac{9}{\delta^2} \leq 0{,}05$, soit $\delta^2 \geq 180$, c'est-à-dire $\delta \geq \sqrt{180} = 6\sqrt{5} \approx 13{,}4$. Par exemple $\delta = 13{,}5$.

### Exercice 8 — Quand l'inégalité ne dit rien <span class="etoiles">★</span>

$X$ a pour écart type $\sigma = 2$. Que donne l'inégalité de Bienaymé-Tchebychev pour $\delta = 1$ ? Pour quelles valeurs de $\delta$ apporte-t-elle une information ?

??? success "Correction"
    Pour $\delta = 1$ : le majorant vaut $4$, et toute probabilité est inférieure à $1$ : l'inégalité n'apporte rien. Elle n'est utile que si $\frac{4}{\delta^2} < 1$, soit $\delta > 2 = \sigma$.

---

## Thème 2 — Inégalité de concentration et taille d'échantillon

*Méthodes associées : [Méthode 2](methodes.md#methode-2-appliquer-linegalite-de-concentration) et [Méthode 3](methodes.md#methode-3-determiner-une-taille-dechantillon).*

### Exercice 9 — Application directe <span class="etoiles">★</span>

$(X_1, \ldots, X_{100})$ est un échantillon d'une loi de variance $4$ et d'espérance $\mu$. Majorer $P\big(|M_{100} - \mu| \geq 0{,}5\big)$.

??? success "Correction"
    $\frac{4}{100 \times 0{,}25} = 0{,}16$.

### Exercice 10 — Taille d'échantillon <span class="etoiles">★★</span>

Avec la même loi qu'à l'exercice 9, quelle taille $n$ suffit pour que $P\big(|M_n - \mu| \geq 0{,}5\big) \leq 0{,}05$ ?

??? success "Correction"
    $n \geq \frac{4}{0{,}05 \times 0{,}25} = 320$. Un échantillon de $320$ observations suffit.

### Exercice 11 — Une pièce lancée $500$ fois <span class="etoiles">★</span>

On lance $500$ fois une pièce équilibrée. Majorer la probabilité que la fréquence de Pile s'écarte de $0{,}5$ d'au moins $0{,}05$.

??? success "Correction"
    $\frac{0{,}25}{500 \times 0{,}05^2} = 0{,}2$.

### Exercice 12 — Taille d'un sondage <span class="etoiles">★★</span>

Quelle taille d'échantillon suffit pour estimer une proportion inconnue $p$ à $0{,}03$ près avec un risque d'au plus $5\,\%$ ?

??? success "Correction"
    Avec $V = p(1 - p) \leq \frac{1}{4}$, il suffit que $\frac{1}{4n \times 0{,}03^2} \leq 0{,}05$, soit $n \geq \frac{1}{4 \times 0{,}05 \times 0{,}0009} \approx 5\,555{,}6$. Il suffit d'interroger $5\,556$ personnes. (Les instituts de sondage en interrogent environ $1\,000$, en s'appuyant sur des résultats plus fins.)

### Exercice 13 — La moyenne de lancers de dé <span class="etoiles">★★</span>

Combien de lancers d'un dé suffisent pour que la moyenne des résultats soit à moins de $0{,}2$ de $3{,}5$ avec une probabilité d'au moins $0{,}9$ ?

??? success "Correction"
    On veut $P\big(|M_n - 3{,}5| \geq 0{,}2\big) \leq 0{,}1$. Il suffit que $n \geq \dfrac{35/12}{0{,}1 \times 0{,}04} \approx 729{,}2$, soit $730$ lancers.

### Exercice 14 — Version « somme » <span class="etoiles">★★</span>

1. Montrer que $P\big(|S_n - n\mu| \geq n\delta\big) = P\big(|M_n - \mu| \geq \delta\big)$.
2. On lance $100$ dés. Majorer la probabilité que la somme des résultats s'écarte de $350$ d'au moins $50$.

??? success "Correction"
    **1.** $|S_n - n\mu| = n|M_n - \mu|$, et $n > 0$ : les deux événements sont les mêmes.

    **2.** Avec $\delta = 0{,}5$ : $P \leq \dfrac{35/12}{100 \times 0{,}25} \approx 0{,}117$. On peut aussi appliquer Bienaymé-Tchebychev à $S_{100}$, de variance $\frac{3500}{12}$ : $\frac{3500/12}{2500} \approx 0{,}117$.

### Exercice 15 — La qualité de la majoration <span class="etoiles">★★</span>

On lance $1\,000$ fois une pièce équilibrée. La méthode 2 donne $P\big(|F_{1000} - 0{,}5| \geq 0{,}05\big) \leq 0{,}1$. Calculer la valeur exacte avec la loi binomiale (calculatrice) et commenter.

??? success "Correction"
    L'événement s'écrit $|X - 500| \geq 50$, avec $X \sim \mathcal{B}(1\,000\,;\,0{,}5)$. Par symétrie, sa probabilité vaut $2P(X \leq 450) \approx 0{,}0017$. Le majorant $0{,}1$ est environ soixante fois trop grand.

---

## Thème 3 — Loi des grands nombres

### Exercice 16 — La démonstration <span class="etoiles">★</span>

Démontrer la loi faible des grands nombres à partir de l'inégalité de concentration, en citant le théorème utilisé sur les limites.

??? success "Correction"
    Voir le cours, § 4 : on encadre la probabilité entre $0$ et $\frac{V}{n\delta^2}$, qui tend vers $0$, et l'on conclut avec le théorème des gendarmes.

### Exercice 17 — « Le rouge va forcément sortir » <span class="etoiles">★</span>

À la roulette, le noir est sorti dix fois de suite. Un joueur affirme : « D'après la loi des grands nombres, le rouge doit maintenant sortir plus souvent pour rétablir l'équilibre. » Qu'en penser ?

??? success "Correction"
    C'est faux. Les tirages sont indépendants : la probabilité du rouge au prochain tirage est toujours $\frac{18}{37}$. La loi des grands nombres ne dit pas que le hasard compense les écarts passés ; les dix noirs sont simplement **noyés** dans un grand nombre de tirages futurs, ce qui suffit à ramener la fréquence vers $\frac{18}{37}$. Cette erreur s'appelle le « sophisme du joueur ».

### Exercice 18 — La somme s'éloigne, la moyenne se rapproche <span class="etoiles">★★</span>

On lance $n$ fois une pièce équilibrée ; $S_n$ est le nombre de Pile et $F_n = \frac{S_n}{n}$.

1. Calculer $\sigma(S_n - \frac{n}{2})$ et $\sigma(F_n - \frac{1}{2})$.
2. Commenter pour $n = 100$ et $n = 1\,000\,000$.

??? success "Correction"
    **1.** $\sigma(S_n) = \frac{\sqrt{n}}{2}$ et $\sigma(F_n) = \frac{1}{2\sqrt{n}}$ ; les constantes ne changent pas l'écart type.

    **2.** Pour $n = 100$ : $5$ et $0{,}05$. Pour $n = 1\,000\,000$ : $500$ et $0{,}0005$. L'écart typique entre le nombre de Pile et $\frac{n}{2}$ **augmente**, mais l'écart entre la fréquence et $\frac{1}{2}$ **diminue**. C'est précisément ce que dit la loi des grands nombres, et pourquoi elle ne prévoit aucune « compensation ».

### Exercice 19 — Estimer une probabilité par simulation <span class="etoiles">★★</span>

On veut estimer une probabilité inconnue $p$ par la fréquence observée sur $n$ simulations, à $0{,}01$ près, avec un risque d'au plus $5\,\%$. Combien de simulations suffisent ?

??? success "Correction"
    $\frac{1}{4n \times 0{,}01^2} \leq 0{,}05 \iff n \geq \frac{1}{4 \times 0{,}05 \times 0{,}0001} = 50\,000$.

### Exercice 20 — Deux dés <span class="etoiles">★</span>

On lance un grand nombre de fois deux dés et l'on note la fréquence $F_n$ des lancers dont la somme vaut $7$. Vers quelle valeur $F_n$ se rapproche-t-elle ? Justifier.

??? success "Correction"
    Les lancers sont indépendants et $P(S = 7) = \frac{6}{36} = \frac{1}{6}$. $F_n$ est la moyenne d'un échantillon de la loi de Bernoulli de paramètre $\frac{1}{6}$ : d'après la loi des grands nombres, elle se rapproche de $\frac{1}{6}$.

### Exercice 21 — Mesures et biais <span class="etoiles">★★</span>

On mesure $n$ fois une longueur $\ell$ avec un instrument. Chaque mesure est une variable aléatoire d'écart type $0{,}5$ mm, les mesures étant indépendantes.

1. Si l'espérance de chaque mesure est $\ell$, que dit la loi des grands nombres de la moyenne des mesures ?
2. Si l'instrument est mal réglé, l'espérance de chaque mesure est $\ell + 0{,}2$ mm. Qu'est-ce qui change ? Peut-on corriger ce défaut en faisant plus de mesures ?

??? success "Correction"
    **1.** La moyenne se rapproche de $\ell$ : répéter les mesures réduit l'erreur **aléatoire**.

    **2.** La moyenne se rapproche alors de $\ell + 0{,}2$ : l'erreur **systématique** (le biais) n'est pas réduite par la répétition. Il faut régler l'instrument.

---

## Thème 4 — Simulations en Python

*Méthode associée : [Méthode 4](methodes.md#methode-4-estimer-une-probabilite-par-simulation).*

### Exercice 22 — La fréquence de Pile <span class="etoiles">★</span>

Écrire un programme qui simule $n$ lancers d'une pièce équilibrée et affiche la fréquence de Pile, pour $n = 10$, $100$, $1\,000$, $10\,000$ et $100\,000$.

??? success "Correction"
    ```python
    from random import random

    for n in [10, 100, 1000, 10000, 100000]:
        piles = sum(1 for i in range(n) if random() < 0.5)
        print(n, piles / n)
    ```

    Les fréquences se rapprochent de $0{,}5$ quand $n$ grandit, comme sur la figure du cours.

### Exercice 23 — Estimer $\pi$ <span class="etoiles">★★★</span>

On choisit un point $M(x, y)$ au hasard dans le carré $[0, 1] \times [0, 1]$ ($x$ et $y$ donnés par `random()`). On admet que la probabilité que $x^2 + y^2 \leq 1$ est égale à l'aire du quart de disque, soit $\frac{\pi}{4}$.

1. Écrire un programme qui estime $\pi$ à partir de $n$ points.
2. Combien de points suffisent pour que l'estimation de $\pi$ soit à moins de $0{,}01$ de la valeur exacte, avec un risque d'au plus $5\,\%$ ?

??? success "Correction"
    **1.**

    ```python
    from random import random

    def estime_pi(n):
        dedans = 0
        for i in range(n):
            x, y = random(), random()
            if x**2 + y**2 <= 1:
                dedans += 1
        return 4 * dedans / n

    print(estime_pi(1000000))   # environ 3.14
    ```

    **2.** L'estimation vaut $4F_n$, et $|4F_n - \pi| < 0{,}01 \iff |F_n - \frac{\pi}{4}| < 0{,}0025$. Il suffit que $\frac{1}{4n \times 0{,}0025^2} \leq 0{,}05$, soit $n \geq 800\,000$ points. C'est beaucoup : la méthode de Monte-Carlo converge lentement, mais elle s'applique à des problèmes où aucune formule n'existe.

### Exercice 24 — Vérifier l'inégalité de concentration <span class="etoiles">★★</span>

Écrire un programme qui, pour $n = 100$ lancers de dé, répète $10\,000$ fois l'expérience et calcule la proportion des expériences où $|M_n - 3{,}5| \geq 0{,}3$. Comparer avec le majorant de l'inégalité de concentration.

??? success "Correction"
    ```python
    from random import randint

    N, n, delta = 10000, 100, 0.3
    ecarts = 0
    for k in range(N):
        M = sum(randint(1, 6) for i in range(n)) / n
        if abs(M - 3.5) >= delta:
            ecarts += 1
    print(ecarts / N)                     # environ 0.08
    print((35 / 12) / (n * delta**2))     # majorant : environ 0.324
    ```

    La proportion observée (environ $0{,}08$) est bien inférieure au majorant ($0{,}32$).

### Exercice 25 — Une fonction « taille » <span class="etoiles">★</span>

Écrire une fonction `taille(V, delta, alpha)` qui renvoie la plus petite taille $n$ donnée par l'inégalité de concentration. Retrouver le résultat de l'exercice 12.

??? success "Correction"
    ```python
    from math import ceil

    def taille(V, delta, alpha):
        return ceil(V / (alpha * delta**2))

    print(taille(0.25, 0.03, 0.05))   # 5556
    ```

    *Attention aux arrondis en virgule flottante : quand $\frac{V}{\alpha\delta^2}$ est un entier, `ceil` peut renvoyer l'entier suivant. Une boucle `while` qui teste l'inégalité est plus sûre.*

---

## Thème 5 — Approfondissement

### Exercice 26 — Démontrer Bienaymé-Tchebychev <span class="etoiles">★★★</span>

1. Démontrer l'inégalité de Markov.
2. En déduire l'inégalité de Bienaymé-Tchebychev.
3. Démontrer directement l'inégalité de Bienaymé-Tchebychev à partir de la définition $V = \sum_i P(X = x_i)(x_i - \mu)^2$, sans passer par Markov.

??? success "Correction"
    **1 et 2.** Voir le cours, § 1 et § 2.

    **3.** Tous les termes de la somme sont positifs ; on ne garde que ceux pour lesquels $|x_i - \mu| \geq \delta$, et pour eux $(x_i - \mu)^2 \geq \delta^2$ :
    $$V \geq \sum_{|x_i - \mu| \geq \delta} P(X = x_i)(x_i - \mu)^2 \geq \delta^2 \sum_{|x_i - \mu| \geq \delta} P(X = x_i) = \delta^2\,P\big(|X - \mu| \geq \delta\big).$$

### Exercice 27 — Des variables de lois différentes <span class="etoiles">★★★</span>

$X_1, \ldots, X_n$ sont indépendantes, de même espérance $\mu$, mais de lois différentes ; on sait seulement que $V(X_i) \leq C$ pour tout $i$, où $C$ est une constante. Montrer que la loi des grands nombres reste vraie pour $M_n = \frac{X_1 + \cdots + X_n}{n}$.

??? success "Correction"
    $E(M_n) = \mu$ par linéarité. Par indépendance, $V(M_n) = \frac{1}{n^2}\sum V(X_i) \leq \frac{nC}{n^2} = \frac{C}{n}$. Bienaymé-Tchebychev donne $0 \leq P\big(|M_n - \mu| \geq \delta\big) \leq \frac{C}{n\delta^2}$, qui tend vers $0$. On conclut par le théorème des gendarmes. L'hypothèse « même loi » n'était pas nécessaire : seules comptent l'indépendance, l'espérance commune et des variances bornées.

### Exercice 28 — Un intervalle pour une proportion inconnue <span class="etoiles">★★★</span>

Dans un schéma de Bernoulli de paramètre $p$ inconnu, on observe la fréquence $F_n$.

1. Montrer que $P\left(|F_n - p| < \dfrac{\sqrt{5}}{\sqrt{n}}\right) \geq 0{,}95$.
2. En déduire que l'intervalle $\left]F_n - \frac{\sqrt{5}}{\sqrt{n}},\, F_n + \frac{\sqrt{5}}{\sqrt{n}}\right[$ contient $p$ avec une probabilité d'au moins $0{,}95$.
3. Application : sur $10\,000$ personnes, $5\,200$ sont favorables à un projet. Donner l'intervalle obtenu.

??? success "Correction"
    **1.** Avec $\delta = \frac{\sqrt{5}}{\sqrt{n}}$ : $\frac{1}{4n\delta^2} = \frac{1}{4n \times 5/n} = \frac{1}{20} = 0{,}05$. Donc $P\big(|F_n - p| \geq \delta\big) \leq 0{,}05$, et l'on passe au contraire.

    **2.** $|F_n - p| < \delta \iff F_n - \delta < p < F_n + \delta$ : c'est le même événement.

    **3.** $F_n = 0{,}52$ et $\delta = \frac{\sqrt{5}}{100} \approx 0{,}022$ : $]0{,}497\,;\,0{,}543[$ (bornes arrondies vers l'extérieur). On ne peut pas affirmer, à ce niveau de garantie, que la majorité est favorable. *Dans le supérieur, on remplace $\sqrt{5} \approx 2{,}24$ par $1$ (intervalle de confiance usuel $F_n \pm \frac{1}{\sqrt{n}}$), grâce au théorème central limite.*
