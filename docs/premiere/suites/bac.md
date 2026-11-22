# Sujets type épreuve anticipée — Suites numériques

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

L'épreuve anticipée de mathématiques dure **2 heures, sans calculatrice**. Elle comporte un **QCM d'automatismes** (6 points) et **deux ou trois exercices** (14 points). Chaque sujet ci-dessous reproduit ce format à l'échelle d'un chapitre : **six questions d'automatismes** (sur tout le programme et sur les suites), puis **un exercice** du type de la deuxième partie. Compte environ **45 minutes** par sujet, sans calculatrice.

| Sujet | Exercice | Durée conseillée |
|---|---|---|
| 1 | Deux plantes : croissance linéaire ou exponentielle | 45 min |
| 2 | Une suite définie par récurrence | 45 min |
| 3 | Somme d'entiers et gradins d'un stade | 40 min |
| 4 | Somme géométrique et rebonds d'une balle | 45 min |

## Sujet 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** Un prix augmente de $25\,\%$, puis baisse de $20\,\%$. Au total, le prix :

a. augmente de $5\,\%$ ; b. ne change pas ; c. baisse de $5\,\%$ ; d. augmente de $45\,\%$.

**Question 2.** $15\,\%$ de $80$ est égal à :

a. $1{,}2$ ; b. $8$ ; c. $12$ ; d. $15$.

**Question 3.** Soit $u_n = 3 - 2n$. Alors $u_{10}$ vaut :

a. $-17$ ; b. $-20$ ; c. $23$ ; d. $17$.

**Question 4.** $\dfrac{2^5 \times 2^3}{2^4}$ est égal à :

a. $2^{11}$ ; b. $2^{4}$ ; c. $2^{2}$ ; d. $8^{1}$.

**Question 5.** $(u_n)$ est géométrique de premier terme $u_0 = 5$ et de raison $-2$. Alors $u_3$ vaut :

a. $-40$ ; b. $40$ ; c. $-30$ ; d. $-1$.

**Question 6.** Le coefficient multiplicateur associé à une baisse de $8\,\%$ est :

a. $-0{,}08$ ; b. $0{,}08$ ; c. $0{,}92$ ; d. $1{,}08$.

### Partie 2 — Exercice

Une plante A mesure $10$ cm et grandit de $2$ cm par semaine. Une plante B mesure $1$ cm et sa taille double chaque semaine. On note $u_n$ et $v_n$ les tailles (en cm) des plantes A et B après $n$ semaines.

1. Préciser la nature des suites $(u_n)$ et $(v_n)$, et exprimer $u_n$ et $v_n$ en fonction de $n$.
2. Recopier et compléter le tableau.

    | $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
    |---|---|---|---|---|---|---|
    | $u_n$ | | | | | | |
    | $v_n$ | | | | | | |

3. Au bout de combien de semaines la plante B dépasse-t-elle la plante A ?
4. On pose $d_n = v_n - u_n$.  
   a. Montrer que $d_{n+1} - d_n = 2^n - 2$.  
   b. En déduire que la suite $(d_n)$ est croissante à partir du rang $1$.  
   c. Justifier que la plante B reste plus grande que la plante A à partir de la semaine trouvée à la question 3.
5. Compléter la fonction Python suivante pour qu'elle renvoie le nombre de semaines trouvé à la question 3.

    ```python
    def semaine():
        n = 0
        u = 10
        v = 1
        while ...:
            u = ...
            v = ...
            n = n + 1
        return n
    ```

??? success "Correction"
    **Partie 1**

    1. **b.** $1{,}25 \times 0{,}8 = 1$.
    2. **c.** $0{,}15 \times 80 = 12$.
    3. **a.** $3 - 20 = -17$.
    4. **b.** $2^{5 + 3 - 4} = 2^4$.
    5. **a.** $5 \times (-2)^3 = -40$.
    6. **c.** $1 - 0{,}08 = 0{,}92$.

    **Partie 2**

    **1.** $(u_n)$ est arithmétique de raison $2$ : $u_n = 10 + 2n$. $(v_n)$ est géométrique de raison $2$ : $v_n = 2^n$.

    **2.**

    | $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
    |---|---|---|---|---|---|---|
    | $u_n$ | $10$ | $12$ | $14$ | $16$ | $18$ | $20$ |
    | $v_n$ | $1$ | $2$ | $4$ | $8$ | $16$ | $32$ |

    **3.** $v_4 = 16 < 18 = u_4$ et $v_5 = 32 > 20 = u_5$ : au bout de $5$ semaines.

    **4. a.** $d_{n+1} - d_n = (v_{n+1} - v_n) - (u_{n+1} - u_n) = (2^{n+1} - 2^n) - 2 = 2^n - 2$.

    **b.** Pour $n \geq 1$, $2^n \geq 2$, donc $d_{n+1} - d_n \geq 0$ : la suite $(d_n)$ est croissante à partir du rang $1$.

    **c.** $d_5 = 32 - 20 = 12 > 0$. La suite $(d_n)$ étant croissante à partir du rang $1$, on a $d_n \geq d_5 > 0$ pour tout $n \geq 5$, c'est-à-dire $v_n > u_n$.

    **5.** La condition est `v <= u`, puis `u = u + 2` et `v = 2 * v`.

---

## Sujet 2

### Partie 1 — Automatismes (QCM)

**Question 1.** La solution de l'équation $3x - 7 = 2$ est :

a. $\frac{5}{3}$ ; b. $3$ ; c. $-3$ ; d. $9$.

**Question 2.** Pour tout réel $x$, $(x - 3)^2$ est égal à :

a. $x^2 - 9$ ; b. $x^2 + 9$ ; c. $x^2 - 6x + 9$ ; d. $x^2 - 3x + 9$.

**Question 3.** La somme $1 + 2 + 3 + \cdots + 20$ vaut :

a. $200$ ; b. $210$ ; c. $220$ ; d. $420$.

**Question 4.** $\dfrac{2}{3} + \dfrac{1}{4}$ est égal à :

a. $\frac{3}{7}$ ; b. $\frac{11}{12}$ ; c. $\frac{2}{12}$ ; d. $\frac{3}{12}$.

**Question 5.** Une suite vérifie $u_{n+1} - u_n = -2$ pour tout $n$. Elle est :

a. géométrique et croissante ; b. arithmétique et croissante ; c. arithmétique et décroissante ; d. géométrique et décroissante.

**Question 6.** Après une hausse de $20\,\%$, un article coûte $60$ €. Son prix avant la hausse était :

a. $40$ € ; b. $48$ € ; c. $50$ € ; d. $72$ €.

### Partie 2 — Exercice

On considère la suite $(u_n)$ définie par $u_0 = 10$ et, pour tout entier naturel $n$, $u_{n+1} = 0{,}5\,u_n + 3$.

1. Calculer $u_1$ et $u_2$. La suite $(u_n)$ est-elle arithmétique ? géométrique ?
2. On pose, pour tout $n$, $v_n = u_n - 6$.  
   a. Calculer $v_0$.  
   b. Montrer que $(v_n)$ est géométrique de raison $0{,}5$.  
   c. En déduire que, pour tout $n$, $u_n = 6 + 4 \times 0{,}5^n$.
3. Étudier le sens de variation de la suite $(u_n)$.
4. Quel semble être le comportement de $u_n$ quand $n$ devient grand ? Justifier brièvement.
5. Écrire un programme Python qui crée la liste des termes $u_0, u_1, \ldots, u_{10}$.

??? success "Correction"
    **Partie 1**

    1. **b.** $3x = 9$.
    2. **c.** Identité remarquable.
    3. **b.** $\frac{20 \times 21}{2} = 210$.
    4. **b.** $\frac{8}{12} + \frac{3}{12} = \frac{11}{12}$.
    5. **c.** La différence est constante et négative.
    6. **c.** $\frac{60}{1{,}2} = 50$.

    **Partie 2**

    **1.** $u_1 = 8$ et $u_2 = 7$. $u_1 - u_0 = -2 \neq -1 = u_2 - u_1$ : pas arithmétique. $\frac{u_1}{u_0} = 0{,}8 \neq \frac{7}{8} = \frac{u_2}{u_1}$ : pas géométrique.

    **2. a.** $v_0 = 4$.

    **b.** $v_{n+1} = u_{n+1} - 6 = 0{,}5\,u_n + 3 - 6 = 0{,}5\,u_n - 3 = 0{,}5\,(u_n - 6) = 0{,}5\,v_n$.

    **c.** $v_n = 4 \times 0{,}5^n$, donc $u_n = v_n + 6 = 6 + 4 \times 0{,}5^n$.

    **3.** $u_{n+1} - u_n = 4 \times 0{,}5^{n+1} - 4 \times 0{,}5^n = 4 \times 0{,}5^n \times (0{,}5 - 1) = -2 \times 0{,}5^n < 0$ : la suite est strictement décroissante.

    **4.** Comme $0 < 0{,}5 < 1$, $0{,}5^n$ se rapproche de $0$, donc $u_n$ semble se rapprocher de $6$ (en restant au-dessus de $6$).

    **5.**

    ```python
    u = [10]
    for n in range(10):
        u.append(0.5 * u[n] + 3)
    print(u)
    ```

---

## Sujet 3

### Partie 1 — Automatismes (QCM)

**Question 1.** Le quotient $\dfrac{1}{\frac{1}{2} + \frac{1}{3}}$ est égal à :

a. $5$ ; b. $\frac{5}{6}$ ; c. $\frac{6}{5}$ ; d. $6$.

**Question 2.** $-3^2$ est égal à :

a. $9$ ; b. $-9$ ; c. $6$ ; d. $-6$.

**Question 3.** Un article à $80$ € est soldé à $60$ €. Le pourcentage de réduction est :

a. $20\,\%$ ; b. $25\,\%$ ; c. $33\,\%$ ; d. $75\,\%$.

**Question 4.** Les trois premiers termes de la suite définie par $u_n = 2n^2 - 1$ sont :

a. $-1$, $1$, $7$ ; b. $1$, $3$, $7$ ; c. $-1$, $1$, $3$ ; d. $0$, $1$, $7$.

**Question 5.** $(u_n)$ est arithmétique, $u_0 = 1$ et $u_{10} = 31$. Sa raison est :

a. $3$ ; b. $3{,}1$ ; c. $30$ ; d. $\frac{1}{3}$.

**Question 6.** Le produit $0{,}3 \times 0{,}4$ vaut :

a. $1{,}2$ ; b. $0{,}12$ ; c. $0{,}7$ ; d. $0{,}012$.

### Partie 2 — Exercice

**A. Question de cours.** Démontrer que pour tout entier $n \geq 1$ :
$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}.$$

**B. Les gradins d'un stade.** Une tribune comporte $25$ rangées. La première rangée compte $20$ places, et chaque rangée compte $2$ places de plus que la précédente. On note $r_n$ le nombre de places de la $n$-ième rangée, avec $r_1 = 20$.

1. Exprimer $r_n$ en fonction de $n$. Combien de places compte la dernière rangée ?
2. Calculer le nombre total de places de la tribune.
3. On note $S_n$ le nombre de places des $n$ premières rangées. Montrer que $S_n = n^2 + 19n$.
4. Lors d'un match, on n'ouvre que les premières rangées. Combien de rangées faut-il ouvrir au minimum pour accueillir $500$ spectateurs ?

??? success "Correction"
    **Partie 1**

    1. **c.** $\frac{1}{2} + \frac{1}{3} = \frac{5}{6}$, dont l'inverse est $\frac{6}{5}$.
    2. **b.** Le carré porte sur $3$ seulement : $-(3^2) = -9$.
    3. **b.** $\frac{20}{80} = 25\,\%$.
    4. **a.** $u_0 = -1$, $u_1 = 1$, $u_2 = 7$.
    5. **a.** $10r = 30$.
    6. **b.** $3 \times 4 = 12$, avec deux décimales.

    **Partie 2**

    **A.** Voir le cours, § 3.3 : on écrit la somme dans les deux sens et l'on additionne, ce qui donne $2S = n(n+1)$.

    **B. 1.** $(r_n)$ est arithmétique de raison $2$ : $r_n = 20 + 2(n - 1) = 2n + 18$. Dernière rangée : $r_{25} = 68$ places.

    **2.** $25 \times \frac{20 + 68}{2} = 25 \times 44 = 1\,100$ places.

    **3.** $S_n = n \times \frac{r_1 + r_n}{2} = n \times \frac{20 + 2n + 18}{2} = n(n + 19) = n^2 + 19n$.

    **4.** $S_{14} = 196 + 266 = 462 < 500$ et $S_{15} = 225 + 285 = 510 \geq 500$. Comme $(S_n)$ est croissante, il faut ouvrir au moins $15$ rangées.

---

## Sujet 4

### Partie 1 — Automatismes (QCM)

**Question 1.** $\left(\dfrac{3}{4}\right)^2$ est égal à :

a. $\frac{6}{8}$ ; b. $\frac{9}{16}$ ; c. $\frac{9}{4}$ ; d. $\frac{3}{16}$.

**Question 2.** Deux hausses successives de $10\,\%$ correspondent à une hausse globale de :

a. $20\,\%$ ; b. $21\,\%$ ; c. $10\,\%$ ; d. $100\,\%$.

**Question 3.** La somme $1 + 3 + 9 + 27 + 81$ vaut :

a. $120$ ; b. $121$ ; c. $243$ ; d. $81$.

**Question 4.** L'écriture scientifique de $0{,}002\,5$ est :

a. $25 \times 10^{-4}$ ; b. $2{,}5 \times 10^{-3}$ ; c. $2{,}5 \times 10^{3}$ ; d. $0{,}25 \times 10^{-2}$.

**Question 5.** L'ensemble des solutions de l'inéquation $-2x + 3 > 7$ est :

a. $]-\infty\,;\,-2[$ ; b. $]-2\,;\,+\infty[$ ; c. $]-\infty\,;\,2[$ ; d. $]2\,;\,+\infty[$.

**Question 6.** Une suite géométrique de premier terme $u_0 = 4$ et de raison $\frac{1}{2}$ est :

a. croissante ; b. décroissante ; c. constante ; d. ni croissante ni décroissante.

### Partie 2 — Exercice

**A. Question de cours.** Démontrer que pour tout réel $q \neq 1$ et tout entier $n \geq 0$ :
$$1 + q + q^2 + \cdots + q^n = \frac{1 - q^{n+1}}{1 - q}.$$

**B. Les rebonds d'une balle.** On lâche une balle d'une hauteur de $2$ mètres. À chaque rebond, elle remonte aux $\frac{3}{4}$ de la hauteur d'où elle est tombée. On note $h_n$ la hauteur (en mètres) atteinte après le $n$-ième rebond, et $h_0 = 2$.

1. Calculer $h_1$ et $h_2$.
2. Justifier que $(h_n)$ est géométrique, et exprimer $h_n$ en fonction de $n$.
3. Étudier le sens de variation de $(h_n)$.
4. On note $D_n$ la distance totale parcourue par la balle, depuis le lâcher jusqu'au moment où elle touche le sol pour la $(n+1)$-ième fois. On admet que $D_n = 2 + 2\,(h_1 + h_2 + \cdots + h_n)$.  
   a. Justifier cette formule.  
   b. Montrer que $D_n = 14 - 12 \times \left(\frac{3}{4}\right)^n$.  
   c. Vérifier la formule pour $n = 1$.
5. La balle peut-elle parcourir plus de $14$ mètres ? Que semble-t-il se passer quand $n$ devient grand ?

??? success "Correction"
    **Partie 1**

    1. **b.** $\frac{3^2}{4^2}$.
    2. **b.** $1{,}1^2 = 1{,}21$.
    3. **b.** $\frac{1 - 3^5}{1 - 3} = \frac{242}{2} = 121$.
    4. **b.** La partie entière doit être comprise entre $1$ et $10$ (exclu).
    5. **a.** $-2x > 4 \iff x < -2$ (on divise par $-2 < 0$, l'inégalité change de sens).
    6. **b.** $u_0 > 0$ et $0 < q < 1$.

    **Partie 2**

    **A.** Voir le cours, § 4.3 : on calcule $S - qS = 1 - q^{n+1}$, puis on divise par $1 - q \neq 0$.

    **B. 1.** $h_1 = \frac{3}{4} \times 2 = 1{,}5$ et $h_2 = \frac{3}{4} \times 1{,}5 = 1{,}125$.

    **2.** On passe d'une hauteur à la suivante en multipliant par $\frac{3}{4}$ : $(h_n)$ est géométrique de raison $\frac{3}{4}$, et $h_n = 2 \times \left(\frac{3}{4}\right)^n$.

    **3.** $h_0 > 0$ et $0 < \frac{3}{4} < 1$ : la suite est strictement décroissante.

    **4. a.** La balle descend d'abord de $2$ m. Ensuite, à chaque rebond $k$ (de $1$ à $n$), elle monte à la hauteur $h_k$ puis redescend de $h_k$, soit $2h_k$.

    **b.** $h_1 + \cdots + h_n$ est la somme de $n$ termes d'une suite géométrique de premier terme $h_1 = 1{,}5$ et de raison $\frac{3}{4}$ :
    $$h_1 + \cdots + h_n = 1{,}5 \times \frac{1 - (3/4)^n}{1 - 3/4} = 6\left(1 - \left(\tfrac{3}{4}\right)^n\right).$$
    Donc $D_n = 2 + 12\left(1 - \left(\frac{3}{4}\right)^n\right) = 14 - 12\left(\frac{3}{4}\right)^n$.

    **c.** $D_1 = 2 + 2 \times 1{,}5 = 5$, et $14 - 12 \times \frac{3}{4} = 14 - 9 = 5$.

    **5.** $12\left(\frac{3}{4}\right)^n > 0$, donc $D_n < 14$ : la balle ne parcourt jamais $14$ mètres. Comme $\left(\frac{3}{4}\right)^n$ se rapproche de $0$, $D_n$ semble se rapprocher de $14$ mètres.
