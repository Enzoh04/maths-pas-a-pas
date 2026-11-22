# Sujets type bac — Fonctions sinus et cosinus

[📄 Sujets seuls (PDF)](pdf/bac-enonces.pdf){ .md-button }
[📄 Sujets + corrections (PDF)](pdf/bac-corriges.pdf){ .md-button }

Quatre sujets au format de l'épreuve du bac. Chaque sujet correspond à **un exercice** de l'épreuve, à traiter en **45 minutes à 1 heure**, sans regarder le cours.

| Sujet | Thème | Ce qui est évalué |
|---|---|---|
| 1 | Oscillation amortie $e^{-x}\sin x$ | dérivée, signe trigonométrique, encadrement |
| 2 | Tension électrique sinusoïdale | période, équations, interprétation |
| 3 | QCM | valeurs, dérivées, équations, limites |
| 4 | Encadrements polynomiaux de $\sin$ et $\cos$ | études de fonctions en cascade, limite |

## Sujet 1 — Oscillation amortie

Soit $f$ la fonction définie sur $[0 \,;\, 2\pi]$ par $f(x) = e^{-x}\sin x$.

1. Résoudre $f(x) = 0$ sur $[0 \,;\, 2\pi]$.
2. Montrer que pour tout $x \in [0 \,;\, 2\pi]$ : $-e^{-x} \leq f(x) \leq e^{-x}$.
3. Montrer que $f'(x) = e^{-x}(\cos x - \sin x)$.
4. Résoudre $\cos x = \sin x$ sur $[0 \,;\, 2\pi]$, puis étudier le signe de $\cos x - \sin x$ sur cet intervalle à l'aide du cercle trigonométrique.
5. Dresser le tableau de variations de $f$ sur $[0 \,;\, 2\pi]$, avec les valeurs exactes des extremums.
6. Déterminer une équation de la tangente à la courbe de $f$ au point d'abscisse $0$.

??? success "Correction"
    **1.** $e^{-x} > 0$, donc $f(x) = 0 \iff \sin x = 0 \iff x \in \{0 \,;\, \pi \,;\, 2\pi\}$.

    **2.** $-1 \leq \sin x \leq 1$ et $e^{-x} > 0$.

    **3.** $f'(x) = -e^{-x}\sin x + e^{-x}\cos x = e^{-x}(\cos x - \sin x)$.

    **4.** $\cos x = \sin x$ pour les points du cercle situés sur la droite $y = x$ : $x = \frac{\pi}{4}$ et $x = \frac{5\pi}{4}$. L'abscisse est plus grande que l'ordonnée sur l'arc situé « sous » cette droite : $\cos x - \sin x > 0$ sur $\left[0 \,;\, \frac{\pi}{4}\right[ \cup \left]\frac{5\pi}{4} \,;\, 2\pi\right]$ et $< 0$ sur $\left]\frac{\pi}{4} \,;\, \frac{5\pi}{4}\right[$.

    **5.** $f'(x)$ a le signe de $\cos x - \sin x$. Valeurs : $f\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2}e^{-\pi/4} \approx 0{,}32$ et $f\left(\frac{5\pi}{4}\right) = -\frac{\sqrt{2}}{2}e^{-5\pi/4} \approx -0{,}014$.

    | $x$ | $0$ | | $\frac{\pi}{4}$ | | $\frac{5\pi}{4}$ | | $2\pi$ |
    |---|---|---|---|---|---|---|---|
    | $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
    | $f(x)$ | $0$ | $\nearrow$ | $\frac{\sqrt{2}}{2}e^{-\pi/4}$ | $\searrow$ | $-\frac{\sqrt{2}}{2}e^{-5\pi/4}$ | $\nearrow$ | $0$ |

    **6.** $f(0) = 0$ et $f'(0) = 1$ : la tangente a pour équation $y = x$.

---

## Sujet 2 — Tension électrique sinusoïdale

La tension (en volts) d'une prise électrique est modélisée par $u(t) = 325\cos(100\pi t)$, où $t$ est en secondes.

1. Montrer que $u$ est périodique de période $T = 0{,}02$ s. Quelle est la fréquence $\frac{1}{T}$ en hertz ?
2. Quelles sont les valeurs maximale et minimale de la tension ? Pour quelles valeurs de $t \in [0 \,;\, T]$ sont-elles atteintes ?
3. Calculer $u'(t)$. Que vaut $u'$ aux instants où la tension est maximale ? Interpréter graphiquement.
4. Résoudre $u(t) = 162{,}5$ sur $[0 \,;\, T]$.
5. Pendant quelle durée, sur une période, la tension dépasse-t-elle $162{,}5$ V ?

??? success "Correction"
    **1.** $u(t + 0{,}02) = 325\cos(100\pi t + 2\pi) = u(t)$. Fréquence : $\frac{1}{0{,}02} = 50$ Hz.

    **2.** $\cos$ varie entre $-1$ et $1$ : $u$ varie entre $-325$ V et $325$ V. $u(t) = 325 \iff 100\pi t = 2k\pi \iff t = \frac{k}{50}$, soit $t = 0$ ou $t = 0{,}02$ dans $[0 \,;\, T]$. $u(t) = -325 \iff 100\pi t = \pi + 2k\pi$, soit $t = 0{,}01$.

    **3.** $u'(t) = -32\,500\pi\sin(100\pi t)$. Aux instants où la tension est maximale, $\sin(100\pi t) = 0$ donc $u'(t) = 0$ : la tangente à la courbe est horizontale.

    **4.** $162{,}5 = \frac{325}{2}$, donc $\cos(100\pi t) = \frac{1}{2}$, soit $100\pi t = \pm\frac{\pi}{3} + 2k\pi$, c'est-à-dire $t = \pm\frac{1}{300} + \frac{k}{50}$. Dans $[0 \,;\, 0{,}02]$ : $t = \frac{1}{300} \approx 0{,}0033$ s et $t = -\frac{1}{300} + \frac{1}{50} = \frac{5}{300} = \frac{1}{60} \approx 0{,}0167$ s.

    **5.** $u(t) > 162{,}5 \iff \cos(100\pi t) > \frac{1}{2}$, ce qui sur $[0 \,;\, T]$ correspond à $t \in \left[0 \,;\, \frac{1}{300}\right[ \cup \left]\frac{1}{60} \,;\, 0{,}02\right]$. Durée totale : $\frac{1}{300} + \left(\frac{1}{50} - \frac{1}{60}\right) = \frac{1}{300} + \frac{1}{300} = \frac{1}{150} \approx 0{,}0067$ s, soit un tiers de la période.

---

## Sujet 3 — QCM

Pour chaque question, une seule réponse est exacte. Indiquer laquelle **en justifiant**.

**Question 1.** $\cos\frac{5\pi}{3}$ est égal à :

a) $-\frac{1}{2}$ — b) $\frac{1}{2}$ — c) $\frac{\sqrt{3}}{2}$ — d) $-\frac{\sqrt{3}}{2}$

**Question 2.** La dérivée de $x \mapsto \sin(3x)$ est :

a) $\cos(3x)$ — b) $3\cos(3x)$ — c) $-3\cos(3x)$ — d) $3\sin(3x)$

**Question 3.** L'ensemble des solutions de $\sin x = \frac{1}{2}$ dans $[0 \,;\, 2\pi]$ est :

a) $\left\{\frac{\pi}{6}\right\}$ — b) $\left\{\frac{\pi}{6} \,;\, \frac{5\pi}{6}\right\}$ — c) $\left\{\frac{\pi}{3} \,;\, \frac{2\pi}{3}\right\}$ — d) $\left\{\frac{\pi}{6} \,;\, \frac{7\pi}{6}\right\}$

**Question 4.** $\displaystyle\lim_{x\to 0} \frac{\sin(2x)}{x}$ vaut :

a) $0$ — b) $\frac{1}{2}$ — c) $1$ — d) $2$

**Question 5.** La fonction $x \mapsto x\cos x$ est :

a) paire — b) impaire — c) périodique de période $2\pi$ — d) croissante sur $\mathbb{R}$

??? success "Correction"
    **Question 1 : b).** $\frac{5\pi}{3} = 2\pi - \frac{\pi}{3}$, donc $\cos\frac{5\pi}{3} = \cos\left(-\frac{\pi}{3}\right) = \frac{1}{2}$.

    **Question 2 : b).** $(\sin(ax + b))' = a\cos(ax + b)$.

    **Question 3 : b).** $\sin x = \sin\frac{\pi}{6} \iff x = \frac{\pi}{6} + 2k\pi$ ou $x = \frac{5\pi}{6} + 2k\pi$.

    **Question 4 : d).** $\frac{\sin(2x)}{x} = 2 \times \frac{\sin(2x)}{2x} \to 2$.

    **Question 5 : b).** $(-x)\cos(-x) = -x\cos x$. Elle n'est pas $2\pi$-périodique, car $f(2\pi) = 2\pi \neq f(0) = 0$, ni croissante, car elle vaut $0$ en $\frac{\pi}{2}$ et $-\pi$ en $\pi$.

---

## Sujet 4 — Encadrements polynomiaux

**Partie A**

1. Montrer que pour tout $x \geq 0$ : $\sin x \leq x$. *(Étudier $x - \sin x$.)*
2. Montrer que pour tout $x \geq 0$ : $\cos x \geq 1 - \dfrac{x^2}{2}$.
3. Montrer que pour tout $x \geq 0$ : $\sin x \geq x - \dfrac{x^3}{6}$.

**Partie B**

4. Montrer que pour tout $x \geq 0$ : $\cos x \leq 1 - \dfrac{x^2}{2} + \dfrac{x^4}{24}$.
5. En déduire que pour tout $x \geq 0$ : $\sin x \leq x - \dfrac{x^3}{6} + \dfrac{x^5}{120}$.
6. En déduire un encadrement de $\sin(0{,}1)$, et la limite $\displaystyle\lim_{x\to 0^+} \frac{x - \sin x}{x^3}$.

??? success "Correction"
    Dans chaque question, on étudie la différence $d$ entre les deux membres : on montre que $d' \geq 0$ grâce à la question précédente, et comme $d(0) = 0$, on obtient $d \geq 0$ sur $[0 \,;\, +\infty[$.

    **1.** $d_1(x) = x - \sin x$ : $d_1'(x) = 1 - \cos x \geq 0$ et $d_1(0) = 0$.

    **2.** $d_2(x) = \cos x - 1 + \frac{x^2}{2}$ : $d_2'(x) = -\sin x + x = d_1(x) \geq 0$ et $d_2(0) = 0$.

    **3.** $d_3(x) = \sin x - x + \frac{x^3}{6}$ : $d_3'(x) = \cos x - 1 + \frac{x^2}{2} = d_2(x) \geq 0$ et $d_3(0) = 0$.

    **4.** $d_4(x) = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cos x$ : $d_4'(x) = -x + \frac{x^3}{6} + \sin x = d_3(x) \geq 0$ et $d_4(0) = 0$.

    **5.** $d_5(x) = x - \frac{x^3}{6} + \frac{x^5}{120} - \sin x$ : $d_5'(x) = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cos x = d_4(x) \geq 0$ et $d_5(0) = 0$.

    **6.** Pour $x = 0{,}1$ : $0{,}1 - \frac{0{,}001}{6} \leq \sin(0{,}1) \leq 0{,}1 - \frac{0{,}001}{6} + \frac{0{,}00001}{120}$, soit

    $$0{,}0998333 \leq \sin(0{,}1) \leq 0{,}0998334.$$

    Pour la limite : d'après les questions 3 et 5, pour $x > 0$, $\frac{x^3}{6} - \frac{x^5}{120} \leq x - \sin x \leq \frac{x^3}{6}$. En divisant par $x^3 > 0$ :

    $$\frac{1}{6} - \frac{x^2}{120} \leq \frac{x - \sin x}{x^3} \leq \frac{1}{6}.$$

    Par les gendarmes, la limite vaut $\frac{1}{6}$.

    *En continuant, on obtient $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$ : c'est le développement en série du sinus, étudié dans le supérieur.*
