# Méthodes — Limites de fonctions

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Traduire une limite en asymptote (et inversement)

| Limite | Interprétation graphique |
|---|---|
| $\displaystyle\lim_{x\to\pm\infty} f(x) = \ell$ | droite $y = \ell$ asymptote **horizontale** en $\pm\infty$ |
| $\displaystyle\lim_{x\to a^\pm} f(x) = \pm\infty$ | droite $x = a$ asymptote **verticale** |
| $\displaystyle\lim_{x\to\pm\infty} f(x) = \pm\infty$ | pas d'asymptote horizontale |

**Position relative.** Pour savoir si la courbe est au-dessus ou en dessous de son asymptote $y = \ell$, on étudie le **signe de $f(x) - \ell$**.

**Exemple.** $f(x) = 2 + \dfrac{3}{x^2 + 1}$. On a $\displaystyle\lim_{x\to\pm\infty} \frac{3}{x^2+1} = 0$, donc $y = 2$ est asymptote horizontale en $+\infty$ et en $-\infty$. Comme $f(x) - 2 = \frac{3}{x^2+1} > 0$, la courbe est toujours au-dessus.

---

## Méthode 2 — Polynômes et fractions rationnelles en l'infini

**Quand ?** Limite en $\pm\infty$ d'un polynôme ou d'un quotient de polynômes donnant une forme indéterminée.

**Les étapes**

1. Repérer le terme de plus haut degré du numérateur et du dénominateur.
2. Au bac, **justifier** en factorisant par ces termes (la règle du terme dominant peut être citée si le cours l'a démontrée).
3. Conclure avec les limites de référence.

**Exemple.** En $+\infty$ :

$$\frac{4x^3 - x}{2x^3 + 5} = \frac{x^3\left(4 - \frac{1}{x^2}\right)}{x^3\left(2 + \frac{5}{x^3}\right)} = \frac{4 - \frac{1}{x^2}}{2 + \frac{5}{x^3}} \longrightarrow \frac{4}{2} = 2.$$

!!! warning "Piège"
    Cette méthode ne marche **qu'en l'infini**. En un réel $a$, on remplace simplement $x$ par $a$ quand c'est possible.

---

## Méthode 3 — Limite en un réel : étudier le signe du dénominateur

**Quand ?** Le dénominateur s'annule en $a$, mais pas le numérateur : on obtient une forme « $\frac{\ell}{0}$ » avec $\ell \neq 0$.

**Les étapes**

1. Calculer la limite du numérateur (un réel $\ell \neq 0$).
2. Étudier le **signe du dénominateur** au voisinage de $a$, à gauche et à droite (tableau de signes).
3. Conclure avec la règle des signes : $\frac{\ell}{0^+}$ et $\frac{\ell}{0^-}$ valent $\pm\infty$.

**Exemple.** $f(x) = \dfrac{x + 3}{x^2 - 1}$ en $1$. Le numérateur tend vers $4 > 0$. Le dénominateur $(x - 1)(x + 1)$ est négatif entre $-1$ et $1$, positif après $1$. Donc :

$$\lim_{x\to 1^-} f(x) = \frac{4}{0^-} = -\infty, \qquad \lim_{x\to 1^+} f(x) = \frac{4}{0^+} = +\infty.$$

**Si le numérateur tend aussi vers $0$** (forme $\frac{0}{0}$) : on factorise par $(x - a)$ en haut et en bas, puis on simplifie.

---

## Méthode 4 — Fonctions avec des racines carrées

**Technique A : quantité conjuguée** pour une forme $\infty - \infty$ :

$$\sqrt{x + 1} - \sqrt{x} = \frac{(x+1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}} \xrightarrow[x\to+\infty]{} 0.$$

**Technique B : factoriser sous la racine.** Pour $x \neq 0$ :

$$\sqrt{x^2 + x} = \sqrt{x^2\left(1 + \tfrac{1}{x}\right)} = |x|\sqrt{1 + \tfrac{1}{x}}.$$

!!! warning "Attention au signe en $-\infty$"
    $\sqrt{x^2} = |x|$, et non $x$ ! En $-\infty$, $x < 0$ donc $|x| = -x$. C'est l'erreur la plus fréquente de ce chapitre (voir l'exercice 17).

---

## Méthode 5 — Utiliser la composition

**Quand ?** La fonction est de la forme $v(u(x))$ : $\sqrt{\dots}$, $e^{\dots}$, $\frac{1}{\dots}$…

**Rédaction type.** Pour $\displaystyle\lim_{x\to+\infty} e^{-x^2+1}$ :

- on pose $X = -x^2 + 1$ ; on a $\displaystyle\lim_{x\to+\infty} X = -\infty$ ;
- or $\displaystyle\lim_{X\to-\infty} e^X = 0$ ;
- donc, par composition, $\displaystyle\lim_{x\to+\infty} e^{-x^2+1} = 0$.

---

## Méthode 6 — Utiliser les croissances comparées

**Quand ?** Une forme indéterminée mêle **exponentielle** et **puissances de $x$**.

**Les étapes**

1. Repérer le terme qui « croît le plus vite » : $e^x$ en $+\infty$.
2. **Factoriser** par ce terme, pour faire apparaître des quotients $\dfrac{x^n}{e^x}$ qui tendent vers $0$.
3. Conclure par opérations.

**Exemple.** En $+\infty$, $e^x - x^2$ est une forme $\infty - \infty$. On factorise par $e^x$ :

$$e^x - x^2 = e^x\left(1 - \frac{x^2}{e^x}\right).$$

Par croissance comparée, $\frac{x^2}{e^x} \to 0$, donc la parenthèse tend vers $1$, et $e^x - x^2 \to +\infty$.

**Changement de variable.** Pour $\dfrac{e^{2x}}{x}$ en $+\infty$, on pose $X = 2x$ : $\dfrac{e^{2x}}{x} = 2 \times \dfrac{e^X}{X} \to +\infty$.

---

## Méthode 7 — Encadrer une fonction qui oscille

**Quand ?** La fonction contient $\sin x$, $\cos x$ ou $(-1)^{\dots}$, qui n'ont pas de limite en $+\infty$.

**Les étapes**

1. Encadrer : $-1 \leq \sin x \leq 1$.
2. En déduire une inégalité sur $f(x)$, en faisant attention au **signe** des facteurs quand on multiplie.
3. Conclure par comparaison (limite infinie) ou par les gendarmes (limite finie).

**Exemple.** Pour $x > 0$, $-e^{-x} \leq e^{-x}\cos x \leq e^{-x}$ (car $e^{-x} > 0$). Les deux bornes tendent vers $0$ : par les gendarmes, $\displaystyle\lim_{x\to+\infty} e^{-x}\cos x = 0$.
