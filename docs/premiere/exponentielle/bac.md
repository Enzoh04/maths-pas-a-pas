# Sujets type épreuve anticipée — Fonction exponentielle

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

L'épreuve anticipée de mathématiques dure **2 heures, sans calculatrice**, avec un **QCM d'automatismes** (6 points) et **deux ou trois exercices** (14 points). Chaque sujet ci-dessous comporte **six questions d'automatismes** puis **un exercice**. Compte environ **45 minutes** par sujet.

| Sujet | Exercice | Durée conseillée |
|---|---|---|
| 1 | Étude de $(2x - 1)e^x$ | 45 min |
| 2 | Équations et inéquations | 40 min |
| 3 | Concentration d'un médicament | 45 min |
| 4 | Démontrer les propriétés de l'exponentielle | 45 min |

## Sujet 1

### Partie 1 — Automatismes (QCM)

Pour chaque question, une seule réponse est exacte. Aucune justification n'est demandée.

**Question 1.** $e^3 \times e^{-5}$ est égal à :

a. $e^{-15}$ ; b. $e^{-2}$ ; c. $e^{8}$ ; d. $-e^{2}$.

**Question 2.** La dérivée de $x \mapsto e^{-3x}$ est :

a. $e^{-3x}$ ; b. $-3e^{-3x}$ ; c. $-3xe^{-3x}$ ; d. $3e^{-3x}$.

**Question 3.** L'équation $e^{2x} = e$ a pour solution :

a. $0$ ; b. $\frac{1}{2}$ ; c. $1$ ; d. $2$.

**Question 4.** Pour tout réel $x$, $e^x$ est :

a. positif ou négatif selon $x$ ; b. strictement positif ; c. strictement négatif ; d. nul en $0$.

**Question 5.** $20\,\%$ de $35$ vaut :

a. $3{,}5$ ; b. $7$ ; c. $15$ ; d. $70$.

**Question 6.** Le trinôme $x^2 - 4x + 4$ :

a. est toujours positif ou nul ; b. change de signe en $2$ ; c. a deux racines ; d. est toujours strictement positif.

### Partie 2 — Exercice

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (2x - 1)\,e^x$.

1. Résoudre l'équation $f(x) = 0$, puis étudier le signe de $f(x)$.
2. Montrer que $f'(x) = (2x + 1)\,e^x$.
3. Dresser le tableau de variations de $f$ et préciser son minimum sous forme exacte.
4. Déterminer l'équation de la tangente à la courbe de $f$ au point d'abscisse $0$.
5. Montrer que pour tout réel $x$, $f(x) \geq -\dfrac{2}{\sqrt{e}}$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **b.** 3. **b.** $2x = 1$. 4. **b.** 5. **b.** 6. **a.** C'est $(x - 2)^2$.

    **Partie 2**

    **1.** $e^x \neq 0$, donc $f(x) = 0 \iff x = \frac{1}{2}$. Comme $e^x > 0$, $f(x)$ a le signe de $2x - 1$ : négatif sur $\left]-\infty\,;\,\frac{1}{2}\right[$, positif sur $\left]\frac{1}{2}\,;\,+\infty\right[$.

    **2.** $f'(x) = 2e^x + (2x - 1)e^x = (2x + 1)e^x$.

    **3.** $f'(x)$ a le signe de $2x + 1$. $f$ est décroissante sur $\left]-\infty\,;\,-\frac{1}{2}\right]$, croissante sur $\left[-\frac{1}{2}\,;\,+\infty\right[$. Minimum : $f\left(-\frac{1}{2}\right) = -2e^{-1/2}$.

    **4.** $f(0) = -1$, $f'(0) = 1$ : $y = x - 1$.

    **5.** $e^{-1/2} = \frac{1}{e^{1/2}} = \frac{1}{\sqrt{e}}$ (car $(e^{1/2})^2 = e$ et $e^{1/2} > 0$). Le minimum vaut donc $-\frac{2}{\sqrt{e}}$, et $f(x) \geq -\frac{2}{\sqrt{e}}$ pour tout $x$.

---

## Sujet 2

### Partie 1 — Automatismes (QCM)

**Question 1.** $\dfrac{e^{2x}}{e^{x - 1}}$ est égal à :

a. $e^{x - 1}$ ; b. $e^{x + 1}$ ; c. $e^{3x - 1}$ ; d. $e^{2}$.

**Question 2.** $(e^x)^3$ est égal à :

a. $e^{x + 3}$ ; b. $e^{3x}$ ; c. $3e^x$ ; d. $e^{x^3}$.

**Question 3.** L'inéquation $e^x < 1$ a pour ensemble de solutions :

a. $]-\infty\,;\,0[$ ; b. $]0\,;\,+\infty[$ ; c. $]-\infty\,;\,1[$ ; d. $\varnothing$.

**Question 4.** Les racines de $X^2 - 3X + 2$ sont :

a. $-1$ et $-2$ ; b. $1$ et $2$ ; c. $1$ et $3$ ; d. $2$ et $3$.

**Question 5.** $\dfrac{3}{4} - \dfrac{2}{3}$ est égal à :

a. $\frac{1}{12}$ ; b. $\frac{1}{7}$ ; c. $\frac{5}{12}$ ; d. $1$.

**Question 6.** Une suite géométrique de raison $e^{-1}$ et de premier terme $2$ est :

a. croissante ; b. décroissante ; c. constante ; d. non monotone.

### Partie 2 — Exercice

Les questions sont indépendantes.

1. Résoudre l'équation $e^{2x + 1} = e^{-x + 7}$.
2. Résoudre l'inéquation $e^{x^2} \leq e^{3x - 2}$.
3. a. Montrer que $1$ et $e^{-1}$ sont les solutions de l'équation $X^2 - (1 + e^{-1})X + e^{-1} = 0$.  
   b. En déduire les solutions de l'équation $e^{2x} - (1 + e^{-1})\,e^x + e^{-1} = 0$.
4. Résoudre l'inéquation $(x^2 - 1)\,e^{-x} \leq 0$.
5. Montrer que pour tout réel $x$, $\dfrac{e^x - 1}{e^x + 1} = \dfrac{1 - e^{-x}}{1 + e^{-x}}$.

??? success "Correction"
    **Partie 1**

    1. **b.** $e^{2x - (x - 1)}$. 2. **b.** 3. **a.** $e^x < e^0$. 4. **b.** 5. **a.** $\frac{9}{12} - \frac{8}{12}$. 6. **b.** $0 < e^{-1} < 1$.

    **Partie 2**

    **1.** $2x + 1 = -x + 7 \iff x = 2$.

    **2.** $x^2 \leq 3x - 2 \iff x^2 - 3x + 2 \leq 0 \iff (x - 1)(x - 2) \leq 0 \iff x \in [1\,;\,2]$.

    **3. a.** Somme $1 + e^{-1}$, produit $e^{-1}$ : ce sont bien les racines. (On peut aussi vérifier en remplaçant.)

    **b.** Avec $X = e^x$ : $e^x = 1$ ou $e^x = e^{-1}$, soit $x = 0$ ou $x = -1$.

    **4.** $e^{-x} > 0$ : l'inéquation équivaut à $x^2 - 1 \leq 0$, soit $x \in [-1\,;\,1]$.

    **5.** On multiplie numérateur et dénominateur du membre de droite par $e^x$ : $\dfrac{e^x - 1}{e^x + 1}$.

---

## Sujet 3

### Partie 1 — Automatismes (QCM)

**Question 1.** La dérivée de $t \mapsto e^{-0{,}5t}$ est :

a. $-0{,}5\,e^{-0{,}5t}$ ; b. $e^{-0{,}5t}$ ; c. $0{,}5\,e^{-0{,}5t}$ ; d. $-0{,}5t\,e^{-0{,}5t}$.

**Question 2.** Si $u$ et $v$ sont dérivables, $(uv)'$ vaut :

a. $u'v'$ ; b. $u'v + uv'$ ; c. $u'v - uv'$ ; d. $uv' - u'v$.

**Question 3.** Sachant que $e^{-1} \approx 0{,}37$, une valeur approchée de $10\,e^{-1}$ est :

a. $0{,}037$ ; b. $3{,}7$ ; c. $37$ ; d. $1{,}37$.

**Question 4.** Le signe de $1 - 0{,}5t$ pour $t \geq 0$ est positif sur :

a. $[0\,;\,2[$ ; b. $]2\,;\,+\infty[$ ; c. $[0\,;\,0{,}5[$ ; d. $[0\,;\,+\infty[$.

**Question 5.** Une quantité diminue de $10\,\%$ par heure. Le coefficient multiplicateur horaire est :

a. $0{,}1$ ; b. $0{,}9$ ; c. $1{,}1$ ; d. $-0{,}1$.

**Question 6.** L'expression $5t\,e^{-0{,}5t}$ s'annule pour :

a. $t = 0$ seulement ; b. $t = 2$ ; c. $t = 0$ et $t = 2$ ; d. aucune valeur.

### Partie 2 — Exercice

On injecte un médicament à un patient. La concentration du médicament dans le sang (en mg/L), $t$ heures après l'injection, est modélisée par
$$C(t) = 5t\,e^{-0{,}5t}, \qquad t \in [0\,;\,10].$$

1. Calculer $C(0)$ et interpréter.
2. Montrer que $C'(t) = 5(1 - 0{,}5t)\,e^{-0{,}5t}$.
3. Dresser le tableau de variations de $C$ sur $[0\,;\,10]$.
4. À quel instant la concentration est-elle maximale ? Donner sa valeur exacte, puis une valeur approchée sachant que $e^{-1} \approx 0{,}37$.
5. Le médicament est efficace tant que la concentration dépasse $2$ mg/L. On admet que $C(1) \approx 3{,}0$ et $C(6) \approx 1{,}5$. Le médicament est-il efficace $6$ heures après l'injection ? Justifier à l'aide du sens de variation.

??? success "Correction"
    **Partie 1**

    1. **a.** 2. **b.** 3. **b.** 4. **a.** 5. **b.** 6. **a.** $e^{-0{,}5t} > 0$.

    **Partie 2**

    **1.** $C(0) = 0$ : au moment de l'injection, le médicament n'est pas encore dans le sang.

    **2.** $C'(t) = 5\,e^{-0{,}5t} + 5t \times (-0{,}5)\,e^{-0{,}5t} = 5(1 - 0{,}5t)\,e^{-0{,}5t}$.

    **3.** $C'(t)$ a le signe de $1 - 0{,}5t$ : positif sur $[0\,;\,2[$, négatif sur $]2\,;\,10]$. $C$ est croissante sur $[0\,;\,2]$ et décroissante sur $[2\,;\,10]$.

    **4.** Maximum en $t = 2$ h : $C(2) = 10\,e^{-1} \approx 3{,}7$ mg/L.

    **5.** $C$ est décroissante sur $[2\,;\,10]$, et $C(6) \approx 1{,}5 < 2$ : six heures après l'injection, le médicament n'est plus efficace.

---

## Sujet 4

### Partie 1 — Automatismes (QCM)

**Question 1.** La fonction exponentielle est définie comme l'unique fonction dérivable sur $\mathbb{R}$ telle que :

a. $f' = f$ et $f(0) = 0$ ; b. $f' = f$ et $f(0) = 1$ ; c. $f' = 1$ et $f(0) = 1$ ; d. $f' = -f$ et $f(0) = 1$.

**Question 2.** La dérivée de $x \mapsto e^{-x}$ est :

a. $e^{-x}$ ; b. $-e^{-x}$ ; c. $-e^{x}$ ; d. $\frac{1}{e^x}$.

**Question 3.** Une fonction dont la dérivée est nulle sur $\mathbb{R}$ est :

a. nulle ; b. constante ; c. croissante ; d. égale à l'exponentielle.

**Question 4.** La tangente à la courbe de l'exponentielle au point d'abscisse $0$ a pour équation :

a. $y = x$ ; b. $y = x + 1$ ; c. $y = ex$ ; d. $y = 1$.

**Question 5.** $(a + b)^2 - (a - b)^2$ est égal à :

a. $0$ ; b. $2b^2$ ; c. $4ab$ ; d. $2a^2 + 2b^2$.

**Question 6.** $10^{-2} \times 10^5$ est égal à :

a. $10^{-10}$ ; b. $10^{3}$ ; c. $10^{7}$ ; d. $10^{-3}$.

### Partie 2 — Exercice

On note $\exp$ la fonction exponentielle, et l'on utilise le résultat suivant : une fonction dont la dérivée est nulle sur $\mathbb{R}$ est constante.

1. On pose $\varphi(x) = \exp(x)\exp(-x)$.  
   a. Montrer que $\varphi'(x) = 0$ pour tout réel $x$.  
   b. En déduire que $\exp(x)\exp(-x) = 1$ pour tout réel $x$, puis que $\exp$ ne s'annule pas.
2. Soit $b$ un réel fixé. On pose $g(x) = \exp(x + b)\exp(-x)$.  
   a. Montrer que $g$ est constante, égale à $\exp(b)$.  
   b. En déduire que $\exp(x + b) = \exp(x)\exp(b)$ pour tout réel $x$.
3. En écrivant $\exp(x) = \exp\left(\frac{x}{2}\right)^2$, montrer que $\exp(x) > 0$ pour tout réel $x$.
4. Montrer que pour tout réel $x$, $\exp(x) \geq 1 + x$.

??? success "Correction"
    **Partie 1**

    1. **b.** 2. **b.** 3. **b.** 4. **b.** 5. **c.** 6. **b.**

    **Partie 2**

    **1. a.** $\varphi'(x) = \exp(x)\exp(-x) + \exp(x) \times (-\exp(-x)) = 0$.

    **b.** $\varphi$ est constante, égale à $\varphi(0) = 1$. Si $\exp(x)$ était nul, le produit le serait aussi.

    **2. a.** $g'(x) = \exp(x + b)\exp(-x) - \exp(x + b)\exp(-x) = 0$ : $g$ est constante, égale à $g(0) = \exp(b)$.

    **b.** $\exp(x + b)\exp(-x) = \exp(b)$ ; en multipliant par $\exp(x)$ et en utilisant $\exp(-x)\exp(x) = 1$ : $\exp(x + b) = \exp(x)\exp(b)$.

    **3.** D'après la question 2 avec $x = b = \frac{x}{2}$ : $\exp(x) = \exp\left(\frac{x}{2}\right)^2 \geq 0$, et $\exp(x) \neq 0$ : donc $\exp(x) > 0$.

    **4.** $h(x) = \exp(x) - 1 - x$ ; $h'(x) = \exp(x) - 1$. Comme $\exp$ est strictement croissante (sa dérivée $\exp$ est strictement positive) et $\exp(0) = 1$, $h'(x) < 0$ pour $x < 0$ et $h'(x) > 0$ pour $x > 0$. Minimum $h(0) = 0$, donc $h \geq 0$.
