# Exercices corrigés — Primitives et équations différentielles

[📄 Énoncés seuls (PDF)](pdf/exercices-enonces.pdf){ .md-button }
[📄 Énoncés + corrections (PDF)](pdf/exercices-corriges.pdf){ .md-button }

28 exercices classés par thème. Difficulté : <span class="etoiles">★</span> application directe — <span class="etoiles">★★</span> entraînement — <span class="etoiles">★★★</span> approfondissement.

Pour t'entraîner dans les conditions de l'examen, va voir les [sujets type bac](bac.md).

Clique sur **Correction** seulement après avoir vraiment cherché.

| Thème | Exercices |
|---|---|
| 1. Vérifier une solution | 1 à 3 |
| 2. Calculs de primitives | 4 à 12 |
| 3. Équations $y' = ay$ et $y' = ay + b$ | 13 à 18 |
| 4. Équations avec second membre | 19 à 22 |
| 5. Modélisation | 23 à 26 |
| 6. Approfondissement | 27 et 28 |

---

## Thème 1 — Vérifier une solution

*Méthode associée : [Méthode 1](methodes.md#methode-1-verifier-quune-fonction-est-solution).*

### Exercice 1 — Vérifications directes <span class="etoiles">★</span>

1. Vérifier que $f(x) = 3e^{2x}$ est solution de $y' = 2y$.
2. Vérifier que $g(x) = e^x - x - 1$ est solution de $y' = y + x$.

??? success "Correction"
    1. $f'(x) = 6e^{2x} = 2 \times 3e^{2x} = 2f(x)$.
    2. $g'(x) = e^x - 1$ et $g(x) + x = e^x - 1$ : les deux membres sont égaux.

### Exercice 2 — Trouver un paramètre <span class="etoiles">★★</span>

Déterminer les réels $a$ pour lesquels $f(x) = e^{ax}$ est solution de $y'' - 3y' + 2y = 0$.

??? success "Correction"
    $f'(x) = ae^{ax}$ et $f''(x) = a^2e^{ax}$. L'équation devient $(a^2 - 3a + 2)e^{ax} = 0$. Comme $e^{ax} > 0$, il faut $a^2 - 3a + 2 = 0$, soit $(a - 1)(a - 2) = 0$ : $a = 1$ ou $a = 2$.

### Exercice 3 — La fonction logistique <span class="etoiles">★★</span>

Montrer que $f(x) = \dfrac{1}{1 + e^{-x}}$ est solution de l'équation $y' = y(1 - y)$.

??? success "Correction"
    $f'(x) = \dfrac{e^{-x}}{(1 + e^{-x})^2}$ (chapitre 3, exercice 16). D'autre part, $1 - f(x) = \dfrac{e^{-x}}{1 + e^{-x}}$, donc

    $$f(x)\big(1 - f(x)\big) = \frac{1}{1 + e^{-x}} \times \frac{e^{-x}}{1 + e^{-x}} = \frac{e^{-x}}{(1 + e^{-x})^2} = f'(x).$$

---

## Thème 2 — Calculs de primitives

*Méthodes associées : [Méthode 2](methodes.md#methode-2-trouver-une-primitive) et [Méthode 3](methodes.md#methode-3-primitive-verifiant-une-condition).*

### Exercice 4 — Primitives usuelles <span class="etoiles">★</span>

Donner une primitive de chaque fonction sur l'intervalle indiqué.

1. $f(x) = x^3 - 2x + 5$ sur $\mathbb{R}$
2. $g(x) = \dfrac{1}{x^2}$ sur $]0 \,;\, +\infty[$
3. $h(x) = e^{3x}$ sur $\mathbb{R}$
4. $k(x) = \dfrac{1}{\sqrt{x}}$ sur $]0 \,;\, +\infty[$
5. $m(x) = \cos(2x)$ sur $\mathbb{R}$

??? success "Correction"
    1. $F(x) = \dfrac{x^4}{4} - x^2 + 5x$.
    2. $G(x) = -\dfrac{1}{x}$.
    3. $H(x) = \dfrac{1}{3}e^{3x}$.
    4. $K(x) = 2\sqrt{x}$.
    5. $M(x) = \dfrac{1}{2}\sin(2x)$.

### Exercice 5 — Forme $u'e^u$ <span class="etoiles">★</span>

Donner une primitive sur $\mathbb{R}$ de $f(x) = 2x\,e^{x^2}$ et de $g(x) = x\,e^{-x^2}$.

??? success "Correction"
    $f = u'e^u$ avec $u = x^2$ : $F(x) = e^{x^2}$.

    Avec $u = -x^2$, $u' = -2x$ : $g = -\frac{1}{2}u'e^u$, donc $G(x) = -\dfrac{1}{2}e^{-x^2}$.

### Exercice 6 — Forme $u'u^n$ <span class="etoiles">★★</span>

Donner une primitive sur $\mathbb{R}$ de :

1. $f(x) = (2x + 1)(x^2 + x)^3$
2. $g(x) = \cos x\,\sin^2 x$
3. $h(x) = (3x - 1)^5$

??? success "Correction"
    1. $u = x^2 + x$, $u' = 2x + 1$ : $F(x) = \dfrac{(x^2 + x)^4}{4}$.
    2. $u = \sin x$, $u' = \cos x$ : $G(x) = \dfrac{\sin^3 x}{3}$.
    3. $u = 3x - 1$, $u' = 3$ : $h = \frac{1}{3}u'u^5$, donc $H(x) = \dfrac{1}{3} \times \dfrac{(3x - 1)^6}{6} = \dfrac{(3x - 1)^6}{18}$.

### Exercice 7 — Forme $\frac{u'}{u}$ <span class="etoiles">★★</span>

Donner une primitive de :

1. $f(x) = \dfrac{2x}{x^2 + 1}$ sur $\mathbb{R}$
2. $g(x) = \dfrac{1}{2x + 3}$ sur $\left]-\frac{3}{2} \,;\, +\infty\right[$
3. $h(x) = \dfrac{e^x}{e^x + 1}$ sur $\mathbb{R}$
4. $k(x) = \tan x = \dfrac{\sin x}{\cos x}$ sur $\left]-\frac{\pi}{2} \,;\, \frac{\pi}{2}\right[$

??? success "Correction"
    1. $u = x^2 + 1 > 0$ : $F(x) = \ln(x^2 + 1)$.
    2. $u = 2x + 3 > 0$, $u' = 2$ : $G(x) = \dfrac{1}{2}\ln(2x + 3)$.
    3. $u = e^x + 1 > 0$ : $H(x) = \ln(e^x + 1)$.
    4. $u = \cos x > 0$ sur cet intervalle, $u' = -\sin x$ : $k = -\frac{u'}{u}$, donc $K(x) = -\ln(\cos x)$.

### Exercice 8 — Forme $\frac{u'}{u^2}$ <span class="etoiles">★★</span>

Donner une primitive sur $\mathbb{R}$ de $f(x) = \dfrac{x}{(x^2 + 1)^2}$ et de $g(x) = \dfrac{e^x}{(1 + e^x)^2}$.

??? success "Correction"
    $f = \frac{1}{2}\frac{u'}{u^2}$ avec $u = x^2 + 1$ : $F(x) = -\dfrac{1}{2(x^2 + 1)}$.

    $g = \frac{u'}{u^2}$ avec $u = 1 + e^x$ : $G(x) = -\dfrac{1}{1 + e^x}$.

### Exercice 9 — Forme $\frac{u'}{\sqrt{u}}$ <span class="etoiles">★★</span>

Donner une primitive sur $\mathbb{R}$ de $f(x) = \dfrac{x}{\sqrt{x^2 + 4}}$.

??? success "Correction"
    $u = x^2 + 4 > 0$, $u' = 2x$ : $f = \frac{1}{2}\frac{u'}{\sqrt{u}}$, donc $F(x) = \frac{1}{2} \times 2\sqrt{u} = \sqrt{x^2 + 4}$.

### Exercice 10 — Avec une condition <span class="etoiles">★★</span>

Déterminer la primitive $F$ de $f(x) = 3x^2 - 4x$ sur $\mathbb{R}$ telle que $F(1) = 2$.

??? success "Correction"
    $F(x) = x^3 - 2x^2 + C$ et $F(1) = 1 - 2 + C = 2$, donc $C = 3$ : $F(x) = x^3 - 2x^2 + 3$.

### Exercice 11 — Une primitive du logarithme <span class="etoiles">★★</span>

1. Calculer la dérivée de $x \mapsto x\ln x - x$ sur $]0 \,;\, +\infty[$.
2. En déduire la primitive de $\ln$ qui s'annule en $1$.

??? success "Correction"
    **1.** $(x\ln x - x)' = \ln x + x \times \frac{1}{x} - 1 = \ln x$.

    **2.** Les primitives de $\ln$ sont $x\ln x - x + C$. En $1$ : $0 - 1 + C = 0$, donc $C = 1$. La primitive cherchée est $F(x) = x\ln x - x + 1$.

### Exercice 12 — Chercher une primitive d'une forme donnée <span class="etoiles">★★★</span>

1. Déterminer des réels $a$ et $b$ tels que $F(x) = (ax + b)e^x$ soit une primitive de $f(x) = xe^x$.
2. Déterminer de même une primitive de $g(x) = x^2e^x$ de la forme $(ax^2 + bx + c)e^x$.

??? success "Correction"
    **1.** $F'(x) = ae^x + (ax + b)e^x = (ax + a + b)e^x$. On veut $ax + a + b = x$ pour tout $x$ : $a = 1$ et $a + b = 0$, donc $b = -1$. $F(x) = (x - 1)e^x$.

    **2.** $G'(x) = (2ax + b)e^x + (ax^2 + bx + c)e^x = \big(ax^2 + (2a + b)x + (b + c)\big)e^x$. On identifie avec $x^2$ : $a = 1$, $2a + b = 0$, $b + c = 0$, donc $b = -2$ et $c = 2$. $G(x) = (x^2 - 2x + 2)e^x$.

    *Au chapitre 8, l'intégration par parties permet de trouver ces primitives sans deviner leur forme.*

---

## Thème 3 — Équations $y' = ay$ et $y' = ay + b$

*Méthode associée : [Méthode 4](methodes.md#methode-4-resoudre-y-ay-b-avec-une-condition-initiale).*

### Exercice 13 — Équation homogène <span class="etoiles">★</span>

Résoudre $y' = -2y$, puis déterminer la solution $f$ telle que $f(0) = 5$.

??? success "Correction"
    Solutions : $x \mapsto Ce^{-2x}$. Avec $f(0) = C = 5$ : $f(x) = 5e^{-2x}$.

### Exercice 14 — Avec une constante <span class="etoiles">★</span>

Résoudre $y' = 3y + 6$, puis déterminer la solution $f$ telle que $f(0) = 1$.

??? success "Correction"
    Solution constante : $-\frac{6}{3} = -2$. Solutions : $Ce^{3x} - 2$. $f(0) = C - 2 = 1$, donc $C = 3$ : $f(x) = 3e^{3x} - 2$.

### Exercice 15 — Mettre sous la bonne forme <span class="etoiles">★★</span>

Résoudre $2y' + y = 4$ avec $y(0) = 0$, puis déterminer la limite de la solution en $+\infty$.

??? success "Correction"
    $y' = -\frac{1}{2}y + 2$. Solution constante : $-\frac{2}{-1/2} = 4$. Solutions : $Ce^{-x/2} + 4$. Avec $y(0) = 0$ : $C = -4$, donc $f(x) = 4 - 4e^{-x/2}$.

    En $+\infty$, $e^{-x/2} \to 0$ et $f(x) \to 4$.

### Exercice 16 — Condition initiale ailleurs qu'en 0 <span class="etoiles">★★</span>

Déterminer la solution de $y' = y$ telle que $y(1) = e^2$.

??? success "Correction"
    Solutions : $Ce^x$. $Ce^1 = e^2$ donne $C = e$. La solution est $f(x) = e \times e^x = e^{x + 1}$.

### Exercice 17 — Comportement des solutions <span class="etoiles">★★</span>

On considère l'équation $y' = -y + 1$.

1. Résoudre l'équation.
2. Montrer que toutes les solutions ont la même limite en $+\infty$.
3. Selon la valeur de $f(0)$, la solution $f$ est-elle croissante ou décroissante ?

??? success "Correction"
    **1.** Solutions : $f(x) = Ce^{-x} + 1$.

    **2.** $Ce^{-x} \to 0$, donc toutes les solutions tendent vers $1$.

    **3.** $f(0) = C + 1$, donc $C = f(0) - 1$, et $f'(x) = -Ce^{-x}$ a le signe de $-C$. Si $f(0) > 1$, alors $C > 0$ et $f$ est décroissante ; si $f(0) < 1$, $f$ est croissante ; si $f(0) = 1$, $f$ est constante. Dans tous les cas, $f$ « se rapproche » de $1$.

### Exercice 18 — Unicité de l'exponentielle <span class="etoiles">★★★</span>

Soit $f$ une fonction dérivable sur $\mathbb{R}$ telle que $f' = f$ et $f(0) = 1$.

1. Démontrer que $f(x) = e^x$ pour tout $x$, en étudiant $g(x) = f(x)e^{-x}$.
2. Pourquoi ce raisonnement ne démontre-t-il pas l'**existence** de l'exponentielle ?

??? success "Correction"
    **1.** $g'(x) = f'(x)e^{-x} - f(x)e^{-x} = 0$, donc $g$ est constante, égale à $g(0) = 1$. D'où $f(x) = e^x$.

    **2.** On a utilisé la fonction $e^{-x}$ dans le raisonnement : on suppose donc déjà que l'exponentielle existe. Ce raisonnement montre seulement qu'il ne peut pas y avoir **deux** fonctions différentes vérifiant $f' = f$ et $f(0) = 1$ (unicité). L'existence est admise (chapitre 2).

---

## Thème 4 — Équations avec second membre

*Méthode associée : [Méthode 5](methodes.md#methode-5-resoudre-y-ay-f).*

### Exercice 19 — Second membre polynomial <span class="etoiles">★★</span>

1. Déterminer une solution particulière de $y' = 2y + x$ de la forme $p(x) = \alpha x + \beta$.
2. En déduire toutes les solutions.

??? success "Correction"
    **1.** $p'(x) = \alpha$ et $2p(x) + x = (2\alpha + 1)x + 2\beta$. Pour tout $x$ : $2\alpha + 1 = 0$ et $2\beta = \alpha$. Donc $\alpha = -\frac{1}{2}$ et $\beta = -\frac{1}{4}$.

    **2.** Solutions : $f(x) = -\dfrac{x}{2} - \dfrac{1}{4} + Ce^{2x}$.

### Exercice 20 — Second membre exponentiel <span class="etoiles">★★</span>

1. Vérifier que $p(x) = xe^{-x}$ est solution de $y' + y = e^{-x}$.
2. En déduire la solution $f$ telle que $f(0) = 2$.

??? success "Correction"
    **1.** $p'(x) = e^{-x} - xe^{-x}$, donc $p'(x) + p(x) = e^{-x}$.

    **2.** L'équation s'écrit $y' = -y + e^{-x}$. Solutions : $f(x) = xe^{-x} + Ce^{-x} = (x + C)e^{-x}$. $f(0) = C = 2$ : $f(x) = (x + 2)e^{-x}$.

### Exercice 21 — Second membre trigonométrique <span class="etoiles">★★</span>

Déterminer une solution particulière de $y' - y = \cos x$ de la forme $p(x) = a\cos x + b\sin x$, puis toutes les solutions.

??? success "Correction"
    $p'(x) - p(x) = -a\sin x + b\cos x - a\cos x - b\sin x = (b - a)\cos x - (a + b)\sin x$. On veut que ce soit $\cos x$ pour tout $x$ : $b - a = 1$ et $a + b = 0$, donc $a = -\frac{1}{2}$ et $b = \frac{1}{2}$.

    Solutions : $f(x) = \dfrac{\sin x - \cos x}{2} + Ce^x$.

### Exercice 22 — Un polynôme de degré 2 <span class="etoiles">★★★</span>

Résoudre $y' + y = x^2$ avec $y(0) = 0$.

??? success "Correction"
    On cherche $p(x) = ax^2 + bx + c$ : $p'(x) + p(x) = ax^2 + (2a + b)x + (b + c)$. On identifie avec $x^2$ : $a = 1$, $2a + b = 0$, $b + c = 0$, donc $b = -2$ et $c = 2$. $p(x) = x^2 - 2x + 2$.

    Solutions : $f(x) = x^2 - 2x + 2 + Ce^{-x}$. $f(0) = 2 + C = 0$ donne $C = -2$ :

    $$f(x) = x^2 - 2x + 2 - 2e^{-x}.$$

---

## Thème 5 — Modélisation

*Méthode associée : [Méthode 6](methodes.md#methode-6-modeliser-une-situation).*

### Exercice 23 — Iode radioactif <span class="etoiles">★★</span>

L'iode 131, utilisé en médecine, a une demi-vie de 8 jours. Le nombre de noyaux vérifie $N' = -\lambda N$.

1. Exprimer $N(t)$ en fonction de $N_0 = N(0)$, de $\lambda$ et de $t$ (en jours).
2. Montrer que $\lambda = \dfrac{\ln 2}{8}$.
3. Quelle proportion des noyaux reste-t-il au bout de 30 jours ?

??? success "Correction"
    **1.** $N(t) = N_0e^{-\lambda t}$.

    **2.** $N(8) = \frac{N_0}{2} \iff e^{-8\lambda} = \frac{1}{2} \iff \lambda = \frac{\ln 2}{8}$.

    **3.** $\dfrac{N(30)}{N_0} = e^{-30\ln 2/8} = 2^{-30/8} = 2^{-3{,}75} \approx 0{,}074$ : il reste environ 7,4 % des noyaux.

### Exercice 24 — Refroidissement d'un plat <span class="etoiles">★★</span>

Un plat sort du four à 80 °C dans une pièce à 20 °C. Sa température vérifie $\theta' = -k(\theta - 20)$ avec $k > 0$, $t$ en minutes. Au bout de 5 minutes, le plat est à 60 °C.

1. Montrer que $\theta(t) = 20 + 60e^{-kt}$.
2. Déterminer $k$.
3. Au bout de combien de temps le plat sera-t-il à 30 °C ?

??? success "Correction"
    **1.** $\theta' = -k\theta + 20k$ : solution constante $20$, donc $\theta(t) = 20 + Ce^{-kt}$. $\theta(0) = 80$ donne $C = 60$.

    **2.** $20 + 60e^{-5k} = 60 \iff e^{-5k} = \frac{2}{3} \iff k = \frac{1}{5}\ln\frac{3}{2} \approx 0{,}081$.

    **3.** $20 + 60e^{-kt} = 30 \iff e^{-kt} = \frac{1}{6} \iff t = \frac{\ln 6}{k} = \frac{5\ln 6}{\ln 1{,}5} \approx 22{,}1$ minutes.

### Exercice 25 — Charge d'un condensateur <span class="etoiles">★★</span>

Dans un circuit RC branché sur une tension $E$, la tension $u$ aux bornes du condensateur vérifie $RC\,u' + u = E$, avec $u(0) = 0$.

1. Résoudre cette équation.
2. On appelle $\tau = RC$ la constante de temps. Au bout de combien de temps le condensateur est-il chargé à 99 % ?

??? success "Correction"
    **1.** $u' = -\frac{1}{RC}u + \frac{E}{RC}$. Solution constante : $E$. Donc $u(t) = E + Ce^{-t/(RC)}$, et $u(0) = 0$ donne $C = -E$ : $u(t) = E\left(1 - e^{-t/\tau}\right)$.

    **2.** $u(t) = 0{,}99E \iff e^{-t/\tau} = 0{,}01 \iff t = \tau\ln 100 \approx 4{,}6\,\tau$.

    *Les physiciens retiennent qu'un condensateur est chargé « à 99 % » au bout d'environ $5\tau$.*

### Exercice 26 — Vitesse limite d'un parachutiste <span class="etoiles">★★</span>

Un parachutiste de masse $m = 80$ kg chute, parachute ouvert. Sa vitesse $v$ (en m/s) vérifie $v' = g - \frac{k}{m}v$, avec $g = 9{,}81$ m/s² et $k = 16$ kg/s. À l'ouverture, on prend $v(0) = 0$ pour simplifier.

1. Résoudre l'équation.
2. Montrer que la vitesse tend vers une **vitesse limite** et la calculer.

??? success "Correction"
    **1.** $v' = -\frac{k}{m}v + g$. Solution constante : $\frac{mg}{k}$. Donc $v(t) = \frac{mg}{k} + Ce^{-kt/m}$, et $v(0) = 0$ donne $v(t) = \frac{mg}{k}\left(1 - e^{-kt/m}\right)$.

    **2.** $e^{-kt/m} \to 0$, donc $v(t) \to \frac{mg}{k} = \frac{80 \times 9{,}81}{16} \approx 49$ m/s, soit environ 177 km/h. *(Avec les vraies valeurs d'un parachute ouvert, $k$ est bien plus grand et la vitesse limite vaut environ 5 m/s.)*

---

## Thème 6 — Approfondissement

### Exercice 27 — Résoudre l'équation logistique <span class="etoiles">★★★</span>

On cherche les solutions $y$ **strictement positives** sur $\mathbb{R}$ de $y' = y(1 - y)$, avec $y(0) = 0{,}1$.

1. On pose $z = \frac{1}{y}$. Montrer que $z' = -z + 1$.
2. Résoudre cette équation et en déduire $y$.
3. Déterminer la limite de $y$ en $+\infty$ et interpréter.

??? success "Correction"
    **1.** $z' = -\dfrac{y'}{y^2} = -\dfrac{y(1 - y)}{y^2} = -\dfrac{1 - y}{y} = -\dfrac{1}{y} + 1 = -z + 1$.

    **2.** $z(x) = 1 + Ce^{-x}$, et $z(0) = \frac{1}{0{,}1} = 10$ donne $C = 9$. Donc $y(x) = \dfrac{1}{1 + 9e^{-x}}$.

    **3.** $y \to 1$ : la population tend vers sa capacité maximale $1$ (ici, normalisée). On reconnaît la forme du modèle de population du chapitre 2.

### Exercice 28 — Méthode d'Euler et nombre $e$ <span class="etoiles">★★★</span>

On approche la solution de $y' = y$, $y(0) = 1$ sur $[0 \,;\, 1]$ par la méthode d'Euler avec $n$ pas de longueur $h = \frac{1}{n}$ : on pose $y_0 = 1$ et $y_{k+1} = y_k + h\,y_k$.

1. Justifier l'approximation $y(x + h) \approx y(x) + h\,y'(x)$, et l'utiliser pour retrouver la relation de récurrence.
2. Montrer que $y_n = \left(1 + \frac{1}{n}\right)^n$. Que doit valoir la limite de $y_n$ ?
3. Écrire une fonction Python `euler(n)` qui renvoie $y_n$.

??? success "Correction"
    **1.** C'est l'approximation par la tangente : $y(x + h) \approx y(x) + h\,y'(x)$ pour $h$ petit. Comme $y' = y$, on obtient $y_{k+1} = y_k + h\,y_k$.

    **2.** $y_{k+1} = (1 + h)y_k$ : la suite est géométrique de raison $1 + h$, donc $y_n = (1 + h)^n = \left(1 + \frac{1}{n}\right)^n$. C'est une approximation de $y(1) = e$, et l'on a bien démontré que $\left(1 + \frac{1}{n}\right)^n \to e$ (chapitre 3, exercice 22).

    **3.**

    ```python
    def euler(n):
        h = 1 / n
        y = 1
        for k in range(n):
            y = y + h * y
        return y
    ```

    `euler(1000)` renvoie environ $2{,}7169$, pour $e \approx 2{,}7183$. La méthode converge, mais lentement : l'erreur est de l'ordre de $\frac{1}{n}$.
