# Méthodes — Calcul numérique et algébrique

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Calculer avec des puissances

**Les étapes**

1. Regrouper les nombres « ordinaires » d'un côté et les puissances de même base de l'autre.
2. Décomposer si besoin les bases en facteurs premiers : $4 = 2^2$, $8 = 2^3$, $9 = 3^2$, $10 = 2 \times 5$…
3. Appliquer les règles $a^m a^n = a^{m+n}$, $\frac{a^m}{a^n} = a^{m-n}$, $(a^m)^n = a^{mn}$.
4. En notation scientifique, ajuster pour que le nombre devant la puissance de $10$ soit entre $1$ et $10$.

**Exemple.** $A = \dfrac{8^3 \times 3^{-2}}{4^2 \times 6^{-1}} = \dfrac{2^9 \times 3^{-2}}{2^4 \times 2^{-1} \times 3^{-1}} = 2^{9 - 4 + 1} \times 3^{-2 + 1} = 2^6 \times 3^{-1} = \dfrac{64}{3}$.

**Exemple.** $\dfrac{0{,}003 \times 4 \times 10^{5}}{6 \times 10^{-2}} = \dfrac{3 \times 4}{6} \times 10^{-3 + 5 + 2} = 2 \times 10^{4}$.

---

## Méthode 2 — Simplifier une expression avec des racines

**Les étapes**

1. Faire apparaître le **plus grand carré parfait** sous chaque racine : $\sqrt{a^2b} = a\sqrt{b}$ ($a \geq 0$).
2. Regrouper les termes en $\sqrt{b}$ comme des termes semblables : $3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}$.
3. Utiliser $\left(\sqrt{a}\right)^2 = a$ et les identités remarquables.
4. Pour un dénominateur $\sqrt{b}$, multiplier en haut et en bas par $\sqrt{b}$ ; pour un dénominateur $a + \sqrt{b}$, multiplier par $a - \sqrt{b}$ (l'expression **conjuguée**).

**Exemple.** $\sqrt{50} - 2\sqrt{18} + \sqrt{8} = 5\sqrt{2} - 6\sqrt{2} + 2\sqrt{2} = \sqrt{2}$.

**Exemple.** $\dfrac{1}{\sqrt{3} - 1} = \dfrac{\sqrt{3} + 1}{\left(\sqrt{3} - 1\right)\left(\sqrt{3} + 1\right)} = \dfrac{\sqrt{3} + 1}{3 - 1} = \dfrac{\sqrt{3} + 1}{2}$.

---

## Méthode 3 — Développer et factoriser

**Les étapes**

1. **Développer** : distributivité, puis identités remarquables ; réduire en regroupant les termes de même degré. Attention au signe $-$ devant une parenthèse.
2. **Factoriser** :
    - chercher un **facteur commun** (il peut être une parenthèse entière) ;
    - sinon, reconnaître une identité : $a^2 - b^2$, $a^2 \pm 2ab + b^2$ ;
    - faire apparaître un facteur commun caché : $(x - 2) - 3(2 - x) = (x - 2) + 3(x - 2) = 4(x - 2)$.
3. Vérifier en redéveloppant (ou en testant une valeur de $x$).

**Exemple.** Factoriser $A = (2x + 1)^2 - 16$ : c'est $a^2 - b^2$ avec $a = 2x + 1$ et $b = 4$ : $A = (2x + 1 - 4)(2x + 1 + 4) = (2x - 3)(2x + 5)$. Vérification avec $x = 0$ : $1 - 16 = -15$ et $(-3) \times 5 = -15$. ✓

---

## Méthode 4 — Comparer deux nombres

**Les étapes**

1. Calculer la **différence** $A - B$, la simplifier (réduire au même dénominateur, factoriser).
2. Étudier son **signe**.
3. Conclure : si $A - B > 0$, alors $A > B$.
4. *Variante* pour deux nombres **positifs** : comparer leur quotient à $1$, ou comparer leurs **carrés**.

**Exemple.** Comparer $3\sqrt{5}$ et $2\sqrt{11}$ : ils sont positifs, et $\left(3\sqrt{5}\right)^2 = 45 > 44 = \left(2\sqrt{11}\right)^2$. Donc $3\sqrt{5} > 2\sqrt{11}$.

**Exemple.** Pour tous réels $a$ et $b$, comparer $a^2 + b^2$ et $2ab$ : $a^2 + b^2 - 2ab = (a - b)^2 \geq 0$, donc $a^2 + b^2 \geq 2ab$.

---

## Méthode 5 — Encadrer une expression

**Les étapes**

1. Partir de l'encadrement de $x$.
2. Construire l'expression **étape par étape**, en appliquant à chaque étape une seule opération.
3. Quand on multiplie par un nombre **négatif**, **changer le sens** des inégalités (et remettre l'encadrement dans l'ordre).
4. Pour un **inverse**, utiliser : si $0 < a \leq x \leq b$, alors $\frac{1}{b} \leq \frac{1}{x} \leq \frac{1}{a}$.

**Exemple.** On sait que $1 \leq x \leq 4$. Encadrer $A = 5 - 3x$ et $B = \dfrac{2}{x}$.

$3 \leq 3x \leq 12$, donc $-12 \leq -3x \leq -3$, donc $-7 \leq 5 - 3x \leq 2$.

$\frac{1}{4} \leq \frac{1}{x} \leq 1$, donc $\frac{1}{2} \leq \frac{2}{x} \leq 2$.
