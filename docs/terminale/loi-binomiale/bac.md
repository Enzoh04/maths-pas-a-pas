# Sujets type bac — Succession d'épreuves indépendantes, loi binomiale

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets dans l'esprit de l'épreuve. Au bac, la loi binomiale apparaît presque toujours dans un exercice de probabilités qui commence par un arbre pondéré (probabilités conditionnelles de Première). Les résultats sont arrondis à $10^{-3}$ sauf mention contraire.

| Sujet | Thème | Durée conseillée |
|---|---|---|
| 1 | Contrôle de qualité : arbre, puis loi binomiale | 50 min |
| 2 | Un jeu de hasard | 40 min |
| 3 | QCM | 25 min |
| 4 | Vérifier une affirmation | 35 min |

## Sujet 1 — Contrôle de qualité

Une usine fabrique des pièces, dont $8\,\%$ sont défectueuses. Un test automatique est appliqué à chaque pièce :

- si la pièce est défectueuse, elle est rejetée par le test avec une probabilité de $0{,}95$ ;
- si la pièce n'est pas défectueuse, elle est rejetée par erreur avec une probabilité de $0{,}02$.

On note $D$ l'événement « la pièce est défectueuse » et $R$ l'événement « la pièce est rejetée ».

**Partie A**

1. Représenter la situation par un arbre pondéré.
2. Calculer $P(D \cap R)$, puis montrer que $P(R) = 0{,}0944$.
3. Une pièce est rejetée. Quelle est la probabilité qu'elle soit réellement défectueuse ?

**Partie B**

On prélève au hasard $50$ pièces dans la production (avant le test). La production est assez importante pour assimiler ce prélèvement à un tirage avec remise. On note $X$ le nombre de pièces défectueuses parmi elles.

1. Justifier que $X$ suit une loi binomiale, dont on précisera les paramètres.
2. Calculer $P(X = 0)$.
3. Calculer la probabilité qu'au moins $4$ pièces soient défectueuses.
4. Calculer $E(X)$ et interpréter ce résultat.
5. On prélève maintenant $n$ pièces. Déterminer la plus petite valeur de $n$ pour laquelle la probabilité qu'au moins une pièce soit défectueuse est supérieure ou égale à $0{,}99$.

??? success "Correction"
    **Partie A**

    **1.** Premier niveau : $D$ ($0{,}08$) et $\overline{D}$ ($0{,}92$). Après $D$ : $R$ ($0{,}95$) et $\overline{R}$ ($0{,}05$). Après $\overline{D}$ : $R$ ($0{,}02$) et $\overline{R}$ ($0{,}98$).

    **2.** $P(D \cap R) = 0{,}08 \times 0{,}95 = 0{,}076$. D'après la formule des probabilités totales :
    $$P(R) = P(D \cap R) + P(\overline{D} \cap R) = 0{,}076 + 0{,}92 \times 0{,}02 = 0{,}076 + 0{,}0184 = 0{,}0944.$$

    **3.** $P_R(D) = \dfrac{P(D \cap R)}{P(R)} = \dfrac{0{,}076}{0{,}0944} \approx 0{,}805$. Environ une pièce rejetée sur cinq est en fait bonne.

    **Partie B**

    **1.** On répète $50$ fois, de façon identique et indépendante (tirage assimilé à un tirage avec remise), l'épreuve « prélever une pièce », à deux issues, le succès « la pièce est défectueuse » ayant pour probabilité $0{,}08$. $X$ compte le nombre de succès : $X \sim \mathcal{B}(50\,;\,0{,}08)$.

    **2.** $P(X = 0) = 0{,}92^{50} \approx 0{,}015$.

    **3.** $P(X \geq 4) = 1 - P(X \leq 3) \approx 1 - 0{,}425 = 0{,}575$.

    **4.** $E(X) = 50 \times 0{,}08 = 4$ : sur un grand nombre de prélèvements de $50$ pièces, on trouve en moyenne $4$ pièces défectueuses par prélèvement.

    **5.** La probabilité qu'au moins une pièce soit défectueuse est $1 - 0{,}92^n$.
    $$1 - 0{,}92^n \geq 0{,}99 \iff 0{,}92^n \leq 0{,}01 \iff n\ln 0{,}92 \leq \ln 0{,}01 \iff n \geq \frac{\ln 0{,}01}{\ln 0{,}92} \approx 55{,}2,$$
    car $\ln 0{,}92 < 0$. La plus petite valeur est $n = 56$.

---

## Sujet 2 — Un jeu de hasard

Une urne contient $5$ boules indiscernables au toucher : $1$ rouge et $4$ blanches. Une partie consiste à tirer une boule, à noter sa couleur et à la remettre dans l'urne. Le joueur gagne la partie s'il tire la boule rouge.

Un joueur paie $1$ € par partie et joue $10$ parties. Il reçoit $4$ € pour chaque partie gagnée. On note $X$ le nombre de parties gagnées et $G$ son gain algébrique (en euros) à l'issue des $10$ parties.

1. Déterminer la loi de $X$.
2. Calculer la probabilité que le joueur ne gagne aucune partie, puis qu'il en gagne au moins $3$.
3. Montrer que $G = 4X - 10$. Calculer $E(G)$ et interpréter.
4. L'organisateur veut rendre le jeu équitable en modifiant uniquement la somme reçue par partie gagnée. Quelle somme doit-il proposer ?
5. On revient au jeu initial. Le joueur veut avoir une probabilité d'au moins $0{,}95$ de gagner au moins une partie.  
   a. Montrer que le nombre $n$ de parties à jouer doit vérifier $0{,}8^n \leq 0{,}05$.  
   b. En déduire le nombre minimal de parties.  
   c. Compléter la fonction Python suivante pour qu'elle renvoie ce nombre minimal.

    ```python
    def nombre_parties():
        n = 1
        while ...:
            n = n + 1
        return n
    ```

??? success "Correction"
    **1.** On répète $10$ fois, de façon identique et indépendante (tirage avec remise), une épreuve à deux issues dont le succès « tirer la boule rouge » a pour probabilité $\frac{1}{5} = 0{,}2$. $X$ compte les succès : $X \sim \mathcal{B}(10\,;\,0{,}2)$.

    **2.** $P(X = 0) = 0{,}8^{10} \approx 0{,}107$. $P(X \geq 3) = 1 - P(X \leq 2) \approx 1 - 0{,}678 = 0{,}322$.

    **3.** Il paie $10$ € et reçoit $4X$ € : $G = 4X - 10$. $E(G) = 4E(X) - 10 = 4 \times 2 - 10 = -2$. En moyenne, sur un grand nombre de séries de $10$ parties, le joueur perd $2$ € par série.

    **4.** Avec une somme $g$ par partie gagnée : $E(gX - 10) = 2g - 10 = 0 \iff g = 5$. L'organisateur doit proposer $5$ €.

    **5. a.** $P(\text{au moins une partie gagnée}) = 1 - 0{,}8^n \geq 0{,}95 \iff 0{,}8^n \leq 0{,}05$.

    **b.** $n \geq \dfrac{\ln 0{,}05}{\ln 0{,}8} \approx 13{,}4$ (division par $\ln 0{,}8 < 0$). Il faut jouer au moins $14$ parties. (Vérification : $0{,}8^{13} \approx 0{,}055$ et $0{,}8^{14} \approx 0{,}044$.)

    **c.** La condition de la boucle est `0.8**n > 0.05` : on continue tant que la probabilité de ne rien gagner est trop grande.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Justifier.

**Question 1.** Si $X \sim \mathcal{B}(6\,;\,0{,}5)$, alors $P(X = 3)$ vaut :

a. $\frac{1}{2}$ ; b. $\frac{5}{16}$ ; c. $\frac{3}{16}$ ; d. $\frac{1}{8}$.

**Question 2.** Une variable de loi binomiale a pour espérance $6$ et pour variance $4{,}2$. Ses paramètres sont :

a. $n = 20$, $p = 0{,}3$ ; b. $n = 30$, $p = 0{,}2$ ; c. $n = 10$, $p = 0{,}6$ ; d. $n = 60$, $p = 0{,}1$.

**Question 3.** Si $X \sim \mathcal{B}(4\,;\,0{,}1)$, alors $P(X \geq 1)$ vaut :

a. $0{,}4$ ; b. $0{,}3439$ ; c. $0{,}6561$ ; d. $0{,}0001$.

**Question 4.** Un événement a une probabilité $0{,}1$ à chaque épreuve. Le nombre minimal d'épreuves indépendantes pour qu'il se produise au moins une fois avec une probabilité d'au moins $0{,}9$ est :

a. $9$ ; b. $10$ ; c. $21$ ; d. $22$.

**Question 5.** Si $X \sim \mathcal{B}(2, p)$ et $P(X = 0) = 0{,}25$, alors $E(X)$ vaut :

a. $0{,}25$ ; b. $0{,}5$ ; c. $1$ ; d. $1{,}5$.

??? success "Correction"
    **Question 1 : b.** $\binom{6}{3} \times \frac{1}{2^6} = \frac{20}{64} = \frac{5}{16}$.

    **Question 2 : a.** $np = 6$ et $np(1 - p) = 4{,}2$ donnent $1 - p = 0{,}7$, soit $p = 0{,}3$ et $n = 20$.

    **Question 3 : b.** $1 - 0{,}9^4 = 1 - 0{,}6561 = 0{,}3439$.

    **Question 4 : d.** $0{,}9^n \leq 0{,}1 \iff n \geq \frac{\ln 0{,}1}{\ln 0{,}9} \approx 21{,}9$. Il faut $22$ épreuves.

    **Question 5 : c.** $(1 - p)^2 = 0{,}25$ donne $1 - p = 0{,}5$ (car $1 - p \geq 0$), donc $p = 0{,}5$ et $E(X) = 2 \times 0{,}5 = 1$.

---

## Sujet 4 — Vérifier une affirmation

Un fabricant d'électroménager affirme que $90\,\%$ de ses clients sont satisfaits. Une association de consommateurs interroge $100$ clients choisis au hasard ; le nombre de clients est assez grand pour assimiler ce choix à un tirage avec remise. Elle en trouve $82$ satisfaits.

On fait l'hypothèse que l'affirmation du fabricant est exacte, et l'on note $X$ le nombre de clients satisfaits dans un échantillon de $100$ clients.

1. Quelle est la loi de $X$ ? Calculer son espérance et son écart type.
2. À l'aide de la calculatrice, déterminer :  
   a. le plus petit entier $a$ tel que $P(X \leq a) > 0{,}025$ ;  
   b. le plus petit entier $b$ tel que $P(X \leq b) \geq 0{,}975$.
3. Justifier que $P(a \leq X \leq b) \geq 0{,}95$, puis donner une valeur approchée de cette probabilité.
4. Au vu du résultat de l'enquête, l'association peut-elle contester l'affirmation du fabricant ? Avec quel risque d'erreur ?
5. Calculer $P(X \leq 82)$ et commenter.
6. Comparer l'intervalle $[a, b]$ à l'intervalle $[E(X) - 2\sigma(X),\, E(X) + 2\sigma(X)]$.

??? success "Correction"
    **1.** Sous l'hypothèse, on répète $100$ fois de façon identique et indépendante une épreuve à deux issues, de succès « le client est satisfait » de probabilité $0{,}9$ : $X \sim \mathcal{B}(100\,;\,0{,}9)$. $E(X) = 90$ et $\sigma(X) = \sqrt{100 \times 0{,}9 \times 0{,}1} = 3$.

    **2. a.** $P(X \leq 83) \approx 0{,}021$ et $P(X \leq 84) \approx 0{,}040$ : $a = 84$.

    **b.** $P(X \leq 94) \approx 0{,}942$ et $P(X \leq 95) \approx 0{,}976$ : $b = 95$.

    **3.** $P(84 \leq X \leq 95) = P(X \leq 95) - P(X \leq 83) \geq 0{,}975 - 0{,}025 = 0{,}95$ (car $P(X \leq 83) \leq 0{,}025$ par définition de $a$). Valeur approchée : $0{,}976 - 0{,}021 \approx 0{,}956$.

    **4.** $82 \notin [84, 95]$. L'association peut contester l'affirmation, avec un risque d'erreur d'au plus $5\,\%$ environ : si le fabricant dit vrai, un résultat hors de cet intervalle se produit moins d'une fois sur vingt.

    **5.** $P(X \leq 82) \approx 0{,}010$ : si l'affirmation était vraie, observer $82$ clients satisfaits ou moins n'arriverait qu'environ une fois sur cent. Cela renforce la conclusion.

    **6.** $[E(X) - 2\sigma, E(X) + 2\sigma] = [84, 96]$, très proche de $[84, 95]$. C'est une règle pratique utile, que le chapitre 15 justifie partiellement avec l'inégalité de Bienaymé-Tchebychev.
