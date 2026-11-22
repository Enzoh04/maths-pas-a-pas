# Sujets type bac — Suites : récurrence et limites

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Suite $u_{n+1} = f(u_n)$ et suite auxiliaire | récurrence, monotonie, suite géométrique, seuil |
| 2 | Modélisation : concentration d'un médicament | arithmético-géométrique, interprétation, Python |
| 3 | QCM | limites, convergence, algorithme |
| 4 | Suite qui oscille autour de sa limite | suite auxiliaire, majoration de l'écart, Python |

## Sujet 1 — Suite définie par une fonction

On considère la fonction $f$ définie sur $[0 \,;\, +\infty[$ par $f(x) = \dfrac{3x}{1 + 2x}$, et la suite $(u_n)$ définie par $u_0 = \dfrac{1}{2}$ et, pour tout $n \in \mathbb{N}$, $u_{n+1} = f(u_n)$.

**Partie A — Étude de la suite**

1. Calculer $u_1$ et $u_2$.
2. a) Montrer que $f$ est strictement croissante sur $[0 \,;\, +\infty[$.
   b) Démontrer par récurrence que pour tout $n \in \mathbb{N}$ : $0 < u_n < 1$.
3. Montrer que pour tout $n$ : $u_{n+1} - u_n = \dfrac{2u_n(1 - u_n)}{1 + 2u_n}$. En déduire le sens de variation de $(u_n)$.
4. Justifier que $(u_n)$ converge.

**Partie B — Expression explicite**

On pose, pour tout $n \in \mathbb{N}$, $v_n = \dfrac{u_n}{1 - u_n}$.

5. Montrer que $(v_n)$ est géométrique de raison $3$. Préciser $v_0$.
6. Exprimer $v_n$, puis $u_n$, en fonction de $n$.
7. Déterminer la limite de $(u_n)$.
8. Déterminer le plus petit entier $n$ tel que $u_n > 0{,}999$.

??? success "Correction"
    **1.** $u_1 = f\left(\tfrac{1}{2}\right) = \dfrac{3/2}{2} = \dfrac{3}{4}$, puis $u_2 = f\left(\tfrac{3}{4}\right) = \dfrac{9/4}{5/2} = \dfrac{9}{10}$.

    **2. a)** $f$ est dérivable sur $[0 \,;\, +\infty[$ et

    $$f'(x) = \frac{3(1 + 2x) - 3x \times 2}{(1 + 2x)^2} = \frac{3}{(1 + 2x)^2} > 0.$$

    Donc $f$ est strictement croissante sur $[0 \,;\, +\infty[$.

    **2. b)** Soit $\mathcal{P}(n)$ : « $0 < u_n < 1$ ».

    - Initialisation : $u_0 = \frac{1}{2}$ et $0 < \frac{1}{2} < 1$.
    - Hérédité : si $0 < u_n < 1$, comme $f$ est strictement croissante sur $[0 \,;\, 1]$, on a $f(0) < f(u_n) < f(1)$, c'est-à-dire $0 < u_{n+1} < 1$, puisque $f(0) = 0$ et $f(1) = \frac{3}{3} = 1$.
    - Conclusion : pour tout $n$, $0 < u_n < 1$.

    **3.**

    $$u_{n+1} - u_n = \frac{3u_n}{1 + 2u_n} - u_n = \frac{3u_n - u_n - 2u_n^2}{1 + 2u_n} = \frac{2u_n(1 - u_n)}{1 + 2u_n}.$$

    D'après 2. b), $u_n > 0$, $1 - u_n > 0$ et $1 + 2u_n > 0$. Donc $u_{n+1} - u_n > 0$ : la suite $(u_n)$ est strictement croissante.

    **4.** $(u_n)$ est croissante et majorée par $1$ : elle converge d'après le théorème de convergence monotone.

    **5.** $u_n \neq 1$, donc $v_n$ est bien défini. Pour tout $n$ :

    $$1 - u_{n+1} = 1 - \frac{3u_n}{1 + 2u_n} = \frac{1 - u_n}{1 + 2u_n},$$

    donc

    $$v_{n+1} = \frac{u_{n+1}}{1 - u_{n+1}} = \frac{3u_n}{1 + 2u_n} \times \frac{1 + 2u_n}{1 - u_n} = 3 \times \frac{u_n}{1 - u_n} = 3v_n.$$

    $(v_n)$ est géométrique de raison $3$, avec $v_0 = \dfrac{1/2}{1/2} = 1$.

    **6.** $v_n = 3^n$. De $v_n = \dfrac{u_n}{1 - u_n}$, on tire $v_n - v_n u_n = u_n$, soit $u_n(1 + v_n) = v_n$, d'où

    $$u_n = \frac{v_n}{1 + v_n} = \frac{3^n}{1 + 3^n}.$$

    *Vérification :* $u_1 = \frac{3}{4}$ et $u_2 = \frac{9}{10}$, comme à la question 1.

    **7.** En divisant numérateur et dénominateur par $3^n$ : $u_n = \dfrac{1}{3^{-n} + 1} = \dfrac{1}{\left(\frac{1}{3}\right)^n + 1}$. Comme $\lim \left(\frac{1}{3}\right)^n = 0$, on obtient $\lim u_n = 1$.

    **8.** $u_n > 0{,}999 \iff 3^n > 0{,}999\,(1 + 3^n) \iff 0{,}001 \times 3^n > 0{,}999 \iff 3^n > 999$.

    Or $3^6 = 729$ et $3^7 = 2187$. Le plus petit entier cherché est $n = 7$.

---

## Sujet 2 — Concentration d'un médicament

Un patient reçoit un médicament. On injecte $2$ mg de produit toutes les heures. Entre deux injections, l'organisme élimine $20\,\%$ de la quantité de médicament présente dans le sang.

On note $u_n$ la quantité de médicament (en mg) présente dans le sang juste après la $n$-ième injection, avec $u_0 = 0$ avant toute injection. On admet que, pour tout $n \in \mathbb{N}$ :

$$u_{n+1} = 0{,}8\,u_n + 2.$$

**Partie A — Étude de la suite**

1. Calculer $u_1$ et $u_2$.
2. Démontrer par récurrence que pour tout $n \in \mathbb{N}$ : $0 \leq u_n \leq u_{n+1} \leq 10$.
3. En déduire que la suite $(u_n)$ converge.

**Partie B — Expression explicite**

On pose $v_n = u_n - 10$ pour tout $n \in \mathbb{N}$.

4. Montrer que $(v_n)$ est une suite géométrique dont on précisera la raison et le premier terme.
5. En déduire que $u_n = 10 - 10 \times 0{,}8^n$, puis la limite de $(u_n)$.

**Partie C — Interprétation**

6. Le médicament devient dangereux au-delà de $12$ mg. Le traitement présente-t-il un risque ?
7. Le médicament est efficace quand la quantité atteint au moins $9{,}5$ mg. On considère la fonction Python ci-dessous. Recopier et compléter les lignes 3 et 4 pour qu'elle renvoie le nombre d'injections nécessaires.

    ```python
    def injections():
        n, u = 0, 0
        while ......:
            u = ......
            n = n + 1
        return n
    ```

8. Déterminer la valeur renvoyée par cette fonction.

??? success "Correction"
    **1.** $u_1 = 0{,}8 \times 0 + 2 = 2$ et $u_2 = 0{,}8 \times 2 + 2 = 3{,}6$.

    **2.** Soit $\mathcal{P}(n)$ : « $0 \leq u_n \leq u_{n+1} \leq 10$ ».

    - Initialisation : $u_0 = 0$ et $u_1 = 2$ : on a bien $0 \leq 0 \leq 2 \leq 10$.
    - Hérédité : supposons $0 \leq u_n \leq u_{n+1} \leq 10$. On multiplie par $0{,}8 > 0$ puis on ajoute $2$ :

    $$2 \leq 0{,}8\,u_n + 2 \leq 0{,}8\,u_{n+1} + 2 \leq 0{,}8 \times 10 + 2,$$

    c'est-à-dire $2 \leq u_{n+1} \leq u_{n+2} \leq 10$, donc $0 \leq u_{n+1} \leq u_{n+2} \leq 10$.

    - Conclusion : $\mathcal{P}(n)$ est vraie pour tout $n$.

    **3.** La suite est croissante et majorée par $10$ : elle converge.

    **4.** $v_{n+1} = u_{n+1} - 10 = 0{,}8\,u_n - 8 = 0{,}8\,(u_n - 10) = 0{,}8\,v_n$.

    $(v_n)$ est géométrique de raison $0{,}8$ et de premier terme $v_0 = -10$.

    **5.** $v_n = -10 \times 0{,}8^n$, donc $u_n = v_n + 10 = 10 - 10 \times 0{,}8^n$.

    Comme $-1 < 0{,}8 < 1$, $\lim 0{,}8^n = 0$ et donc $\lim u_n = 10$.

    **6.** D'après la question 2, $u_n \leq 10 < 12$ pour tout $n$ : la quantité ne dépasse jamais le seuil dangereux. Le traitement ne présente pas ce risque.

    **7.**

    ```python
    def injections():
        n, u = 0, 0
        while u < 9.5:
            u = 0.8 * u + 2
            n = n + 1
        return n
    ```

    **8.** $u_n \geq 9{,}5 \iff 10 \times 0{,}8^n \leq 0{,}5 \iff 0{,}8^n \leq 0{,}05$.

    À la calculatrice : $0{,}8^{13} \approx 0{,}0550 > 0{,}05$ et $0{,}8^{14} \approx 0{,}0440 < 0{,}05$. La suite $(0{,}8^n)$ étant décroissante, la fonction renvoie **14** : il faut 14 injections.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**. Une réponse sans justification ne rapporte aucun point.

**Question 1.** La limite de la suite $u_n = \dfrac{3^n - 2^n}{3^n + 1}$ est :

a) $0$ — b) $1$ — c) $+\infty$ — d) elle n'existe pas

**Question 2.** Pour $n \geq 1$, on pose $u_n = (-1)^n + \dfrac{1}{n}$. La suite $(u_n)$ :

a) converge vers $0$ — b) converge vers $1$ — c) tend vers $+\infty$ — d) n'a pas de limite

**Question 3.** La limite de $S_n = 1 + 0{,}5 + 0{,}5^2 + \dots + 0{,}5^n$ est :

a) $1$ — b) $1{,}5$ — c) $2$ — d) $+\infty$

**Question 4.** Une suite $(u_n)$ est croissante et vérifie $u_n \leq 3$ pour tout $n$. Alors :

a) $(u_n)$ converge vers $3$ — b) $(u_n)$ converge vers un réel $\ell \leq 3$ — c) $(u_n)$ tend vers $+\infty$ — d) $(u_n)$ peut ne pas converger

**Question 5.** On considère la fonction Python suivante.

```python
def mystere():
    u, n = 1, 0
    while u < 100:
        u = 2 * u + 1
        n = n + 1
    return n
```

La valeur renvoyée par `mystere()` est :

a) $5$ — b) $6$ — c) $7$ — d) $127$

??? success "Correction"
    **Question 1 : réponse b).** On divise par $3^n$ : $u_n = \dfrac{1 - \left(\frac{2}{3}\right)^n}{1 + \left(\frac{1}{3}\right)^n}$. Les deux puissances tendent vers $0$, donc $\lim u_n = 1$.

    **Question 2 : réponse d).** Pour $n \geq 3$ : si $n$ est pair, $u_n = 1 + \frac{1}{n} > 1$ ; si $n$ est impair, $u_n = -1 + \frac{1}{n} \leq -\frac{2}{3}$.

    Supposons que $(u_n)$ converge vers un réel $\ell$. L'intervalle $\left]\ell - \frac{1}{2} \,;\, \ell + \frac{1}{2}\right[$, de longueur $1$, devrait contenir tous les termes à partir d'un certain rang, donc des termes pairs et impairs. Il contiendrait alors un nombre supérieur à $1$ et un nombre inférieur à $-\frac{2}{3}$, distants de plus de $\frac{5}{3} > 1$ : c'est impossible. Enfin $|u_n| \leq 2$, donc la suite ne tend pas vers $\pm\infty$. Elle n'a pas de limite.

    **Question 3 : réponse c).** C'est une somme géométrique de raison $0{,}5$ : $S_n = \dfrac{1 - 0{,}5^{n+1}}{1 - 0{,}5} = 2\left(1 - 0{,}5^{n+1}\right) \to 2$.

    **Question 4 : réponse b).** Le théorème de convergence monotone assure la convergence. Par passage à la limite dans $u_n \leq 3$, on obtient $\ell \leq 3$. La réponse a) est fausse : $u_n = 1 - \frac{1}{n+1}$ est croissante, majorée par $3$, et converge vers $1$.

    **Question 5 : réponse b).** Les valeurs successives de `u` sont $1, 3, 7, 15, 31, 63, 127$. La boucle s'arrête quand `u` vaut $127$, après $6$ passages : la fonction renvoie $6$.

---

## Sujet 4 — Une suite qui oscille autour de sa limite

On définit la suite $(u_n)$ par $u_0 = 1$ et, pour tout $n \in \mathbb{N}$, $u_{n+1} = \dfrac{u_n + 6}{u_n + 2}$.

**Partie A — Premières observations**

1. Calculer $u_1$ et $u_2$. La suite $(u_n)$ est-elle monotone ?
2. Démontrer par récurrence que $u_n > 0$ pour tout $n \in \mathbb{N}$.

**Partie B — Une suite auxiliaire**

On pose, pour tout $n \in \mathbb{N}$, $v_n = \dfrac{u_n - 2}{u_n + 3}$.

3. Montrer que $(v_n)$ est géométrique de raison $-\dfrac{1}{4}$. Préciser $v_0$.
4. En déduire $v_n$ en fonction de $n$, puis montrer que $u_n = \dfrac{2 + 3v_n}{1 - v_n}$.
5. Déterminer la limite de $(u_n)$.

**Partie C — Vitesse de convergence**

6. Montrer que $u_n - 2 = \dfrac{5v_n}{1 - v_n}$, puis que $|u_n - 2| \leq \dfrac{20}{3} \times \left(\dfrac{1}{4}\right)^{n+1}$.
7. Écrire une fonction Python qui renvoie le plus petit entier $n$ tel que $|u_n - 2| < 10^{-3}$, en calculant les termes de la suite. Quelle valeur renvoie-t-elle ?

??? success "Correction"
    **1.** $u_1 = \dfrac{1 + 6}{1 + 2} = \dfrac{7}{3}$ et $u_2 = \dfrac{\frac{7}{3} + 6}{\frac{7}{3} + 2} = \dfrac{25/3}{13/3} = \dfrac{25}{13}$.

    $u_0 = 1 < u_1 \approx 2{,}33$ mais $u_2 \approx 1{,}92 < u_1$ : la suite n'est **pas monotone**.

    **2.** $u_0 = 1 > 0$. Si $u_n > 0$, alors $u_n + 6 > 0$ et $u_n + 2 > 0$, donc $u_{n+1} > 0$. Par récurrence, $u_n > 0$ pour tout $n$. En particulier, $u_n + 3 \neq 0$ et $v_n$ est bien défini.

    **3.** Calculons séparément :

    $$u_{n+1} - 2 = \frac{u_n + 6 - 2(u_n + 2)}{u_n + 2} = \frac{2 - u_n}{u_n + 2}, \qquad u_{n+1} + 3 = \frac{u_n + 6 + 3(u_n + 2)}{u_n + 2} = \frac{4(u_n + 3)}{u_n + 2}.$$

    Donc

    $$v_{n+1} = \frac{u_{n+1} - 2}{u_{n+1} + 3} = \frac{2 - u_n}{4(u_n + 3)} = -\frac{1}{4} \times \frac{u_n - 2}{u_n + 3} = -\frac{1}{4}\,v_n.$$

    $(v_n)$ est géométrique de raison $-\frac{1}{4}$, avec $v_0 = \dfrac{1 - 2}{1 + 3} = -\dfrac{1}{4}$.

    **4.** $v_n = -\dfrac{1}{4} \times \left(-\dfrac{1}{4}\right)^n = \left(-\dfrac{1}{4}\right)^{n+1}$.

    De $v_n(u_n + 3) = u_n - 2$, on tire $u_n(v_n - 1) = -2 - 3v_n$. Comme $|v_n| \leq \frac{1}{4}$, on a $v_n \neq 1$, d'où $u_n = \dfrac{2 + 3v_n}{1 - v_n}$.

    *Vérification :* $v_1 = \frac{1}{16}$ donne $u_1 = \dfrac{2 + \frac{3}{16}}{1 - \frac{1}{16}} = \dfrac{35}{15} = \dfrac{7}{3}$.

    **5.** $-1 < -\frac{1}{4} < 1$, donc $\lim v_n = 0$, et $\lim u_n = \dfrac{2 + 0}{1 - 0} = 2$.

    **6.** $u_n - 2 = \dfrac{2 + 3v_n - 2(1 - v_n)}{1 - v_n} = \dfrac{5v_n}{1 - v_n}$.

    Comme $|v_n| \leq \frac{1}{4}$, on a $1 - v_n \geq \frac{3}{4} > 0$. Donc

    $$|u_n - 2| = \frac{5|v_n|}{1 - v_n} \leq \frac{5|v_n|}{3/4} = \frac{20}{3}\,|v_n| = \frac{20}{3} \times \left(\frac{1}{4}\right)^{n+1}.$$

    L'écart à la limite est divisé par environ $4$ à chaque étape. Comme $v_n$ change de signe à chaque rang, $u_n$ est alternativement au-dessus et en dessous de $2$.

    **7.**

    ```python
    def seuil():
        n, u = 0, 1
        while abs(u - 2) >= 0.001:
            u = (u + 6) / (u + 2)
            n = n + 1
        return n
    ```

    On a $|u_5 - 2| = \dfrac{5}{4095} \approx 0{,}00122$ et $|u_6 - 2| = \dfrac{5}{16385} \approx 0{,}00031$. La fonction renvoie **6**.
