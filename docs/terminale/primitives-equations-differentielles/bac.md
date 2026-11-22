# Sujets type bac — Primitives et équations différentielles

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Équation avec second membre et étude de fonction | solution particulière, condition initiale, primitive |
| 2 | Modélisation : refroidissement d'un pain | équation $y' = ay + b$, paramètre, seuil |
| 3 | QCM | primitives, équations différentielles |
| 4 | Modélisation : perfusion d'un médicament | deux phases, continuité, seuils |

## Sujet 1 — Équation différentielle et étude de fonction

On considère l'équation différentielle $(E) : y' + y = 2e^{-x}$.

**Partie A — Résolution**

1. Vérifier que la fonction $p(x) = 2xe^{-x}$ est une solution de $(E)$.
2. Résoudre l'équation $(E_0) : y' + y = 0$.
3. En déduire toutes les solutions de $(E)$.
4. Déterminer la solution $f$ de $(E)$ telle que $f(0) = 1$.

**Partie B — Étude de $f$**

On admet que $f(x) = (2x + 1)e^{-x}$.

5. Déterminer les limites de $f$ en $-\infty$ et en $+\infty$.
6. Montrer que $f'(x) = (1 - 2x)e^{-x}$ en utilisant l'équation $(E)$, puis dresser le tableau de variations de $f$.
7. Déterminer des réels $a$ et $b$ tels que $F(x) = (ax + b)e^{-x}$ soit une primitive de $f$ sur $\mathbb{R}$.

??? success "Correction"
    **1.** $p'(x) = 2e^{-x} - 2xe^{-x}$, donc $p'(x) + p(x) = 2e^{-x}$.

    **2.** $y' = -y$ : solutions $Ce^{-x}$, $C \in \mathbb{R}$.

    **3.** Solutions de $(E)$ : $x \mapsto 2xe^{-x} + Ce^{-x} = (2x + C)e^{-x}$.

    **4.** $f(0) = C = 1$, donc $f(x) = (2x + 1)e^{-x}$.

    **5.** En $-\infty$ : $2x + 1 \to -\infty$ et $e^{-x} \to +\infty$, donc $f \to -\infty$. En $+\infty$ : $f(x) = 2\frac{x}{e^x} + e^{-x} \to 0$ par croissance comparée.

    **6.** D'après $(E)$, $f'(x) = 2e^{-x} - f(x) = 2e^{-x} - (2x + 1)e^{-x} = (1 - 2x)e^{-x}$. Elle a le signe de $1 - 2x$.

    | $x$ | $-\infty$ | | $\frac{1}{2}$ | | $+\infty$ |
    |---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | |
    | $f(x)$ | $-\infty$ | $\nearrow$ | $\frac{2}{\sqrt{e}}$ | $\searrow$ | $0$ |

    **7.** $F'(x) = ae^{-x} - (ax + b)e^{-x} = (-ax + a - b)e^{-x}$. On veut $-ax + a - b = 2x + 1$ : $a = -2$ et $a - b = 1$, donc $b = -3$. $F(x) = -(2x + 3)e^{-x}$.

---

## Sujet 2 — Refroidissement d'un pain

À la sortie du four ($t = 0$), un pain est à 200 °C. On le pose dans une pièce à 25 °C. Sa température $\theta(t)$, en °C, $t$ minutes après la sortie du four, vérifie :

$$\theta'(t) = -k\big(\theta(t) - 25\big), \qquad k > 0.$$

1. Résoudre cette équation et montrer que $\theta(t) = 25 + 175e^{-kt}$.
2. Au bout de 10 minutes, la température du pain est de 100 °C. Montrer que $k = \dfrac{1}{10}\ln\dfrac{7}{3}$, et en donner une valeur approchée.
3. Déterminer la limite de $\theta$ en $+\infty$ et interpréter.
4. Le pain peut être emballé quand sa température est inférieure à 40 °C. Au bout de combien de temps, à la minute près, peut-on l'emballer ?

??? success "Correction"
    **1.** $\theta' = -k\theta + 25k$ : solution constante $25$, donc $\theta(t) = 25 + Ce^{-kt}$. $\theta(0) = 200$ donne $C = 175$.

    **2.** $25 + 175e^{-10k} = 100 \iff e^{-10k} = \frac{75}{175} = \frac{3}{7} \iff -10k = \ln\frac{3}{7} \iff k = \frac{1}{10}\ln\frac{7}{3} \approx 0{,}0847$.

    **3.** $e^{-kt} \to 0$ (car $k > 0$), donc $\theta \to 25$ : le pain finit à la température de la pièce.

    **4.** $\theta(t) < 40 \iff 175e^{-kt} < 15 \iff e^{-kt} < \frac{3}{35} \iff -kt < \ln\frac{3}{35} \iff t > \frac{1}{k}\ln\frac{35}{3}$.

    $\frac{1}{k}\ln\frac{35}{3} = \dfrac{10\ln(35/3)}{\ln(7/3)} \approx 29{,}0$. On peut l'emballer au bout d'environ **29 minutes**.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** Une primitive sur $\mathbb{R}$ de $x \mapsto 2xe^{x^2}$ est :

a) $x^2e^{x^2}$ — b) $e^{x^2}$ — c) $2e^{x^2}$ — d) $\frac{1}{2}e^{x^2}$

**Question 2.** Les solutions de $y' = -3y$ sont les fonctions :

a) $Ce^{3x}$ — b) $Ce^{-3x}$ — c) $-3e^{x} + C$ — d) $e^{-3x} + C$

**Question 3.** La solution constante de $y' = 2y - 4$ est :

a) $-2$ — b) $2$ — c) $4$ — d) $-4$

**Question 4.** Une primitive de $x \mapsto \dfrac{1}{2x + 1}$ sur $\left]-\frac{1}{2} \,;\, +\infty\right[$ est :

a) $\ln(2x + 1)$ — b) $2\ln(2x + 1)$ — c) $\frac{1}{2}\ln(2x + 1)$ — d) $-\dfrac{1}{(2x + 1)^2}$

**Question 5.** La primitive $F$ de $x \mapsto e^{2x}$ telle que $F(0) = 1$ est :

a) $e^{2x}$ — b) $\frac{1}{2}e^{2x} + \frac{1}{2}$ — c) $2e^{2x} - 1$ — d) $\frac{1}{2}e^{2x} + 1$

??? success "Correction"
    **Question 1 : b).** C'est $u'e^u$ avec $u = x^2$.

    **Question 2 : b).** Cours : solutions de $y' = ay$ avec $a = -3$.

    **Question 3 : b).** $-\frac{b}{a} = -\frac{-4}{2} = 2$. *Vérification : $y = 2$ donne $0 = 4 - 4$.*

    **Question 4 : c).** $\frac{1}{2}\frac{u'}{u}$ avec $u = 2x + 1$, $u' = 2$.

    **Question 5 : b).** $F(x) = \frac{1}{2}e^{2x} + C$ et $F(0) = \frac{1}{2} + C = 1$, donc $C = \frac{1}{2}$.

---

## Sujet 4 — Perfusion d'un médicament

On injecte un médicament par perfusion à débit constant de 4 mg par heure. L'organisme élimine le médicament à une vitesse proportionnelle à la quantité présente, avec un coefficient $0{,}2$ par heure. La quantité $Q(t)$ de médicament dans le sang (en mg), $t$ heures après le début de la perfusion, vérifie donc :

$$Q'(t) = -0{,}2\,Q(t) + 4, \qquad Q(0) = 0.$$

**Partie A — Pendant la perfusion**

1. Montrer que $Q(t) = 20\left(1 - e^{-0{,}2t}\right)$.
2. Déterminer la limite de $Q$ en $+\infty$ et interpréter.
3. Le médicament est efficace à partir de 18 mg. Au bout de combien de temps (à 0,1 h près) est-il efficace ?

**Partie B — Après l'arrêt**

On arrête la perfusion au bout de 12 heures. Pour $t \geq 12$, la quantité vérifie alors $Q' = -0{,}2\,Q$, avec $Q(12) = 20\left(1 - e^{-2{,}4}\right) \approx 18{,}19$ mg (continuité).

4. Montrer que pour $t \geq 12$, $Q(t) = Q(12)\,e^{-0{,}2(t - 12)}$.
5. À quel instant (à 0,1 h près) la quantité redescend-elle sous 5 mg ?

??? success "Correction"
    **1.** Solution constante : $-\frac{4}{-0{,}2} = 20$. Donc $Q(t) = 20 + Ce^{-0{,}2t}$, et $Q(0) = 0$ donne $C = -20$.

    **2.** $Q(t) \to 20$ : si la perfusion durait indéfiniment, la quantité se stabiliserait à 20 mg (équilibre entre l'apport et l'élimination).

    **3.** $Q(t) \geq 18 \iff 1 - e^{-0{,}2t} \geq 0{,}9 \iff e^{-0{,}2t} \leq 0{,}1 \iff t \geq \frac{\ln 10}{0{,}2} = 5\ln 10 \approx 11{,}5$ h.

    **4.** Sur $[12 \,;\, +\infty[$, les solutions de $Q' = -0{,}2Q$ sont $Ce^{-0{,}2t}$. La condition $Q(12) = Ce^{-2{,}4}$ donne $C = Q(12)e^{2{,}4}$, d'où $Q(t) = Q(12)e^{-0{,}2(t - 12)}$.

    **5.** $Q(12)e^{-0{,}2(t - 12)} < 5 \iff t - 12 > 5\ln\frac{Q(12)}{5} \approx 5\ln(3{,}637) \approx 6{,}46$. La quantité passe sous 5 mg vers $t \approx 18{,}5$ h, soit environ 6 h 30 après l'arrêt.
