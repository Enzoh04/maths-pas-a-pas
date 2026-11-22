# Méthodes — Fonctions sinus et cosinus

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Résoudre une équation trigonométrique

**Les étapes**

1. Se ramener à $\cos x = \cos a$ ou $\sin x = \sin a$, en reconnaissant une valeur remarquable.
2. Écrire **toutes** les solutions dans $\mathbb{R}$ (avec $+ 2k\pi$).
3. Ne garder que celles de l'intervalle demandé, en testant les valeurs de $k$.

**Exemple.** $\cos x = \frac{1}{2}$ sur $[0 \,;\, 2\pi[$.

- $\frac{1}{2} = \cos\frac{\pi}{3}$, donc $x = \frac{\pi}{3} + 2k\pi$ ou $x = -\frac{\pi}{3} + 2k\pi$.
- Dans $[0 \,;\, 2\pi[$ : $x = \frac{\pi}{3}$ (avec $k = 0$) et $x = -\frac{\pi}{3} + 2\pi = \frac{5\pi}{3}$ (avec $k = 1$).

**Avec un coefficient.** Pour $\cos(2x) = 0$ : $2x = \frac{\pi}{2} + k\pi$, donc $x = \frac{\pi}{4} + \frac{k\pi}{2}$. Attention : diviser par $2$ change le « pas » des solutions.

---

## Méthode 2 — Résoudre une inéquation trigonométrique

**Les étapes**

1. Résoudre d'abord l'**équation** associée sur l'intervalle.
2. Placer les solutions sur le **cercle trigonométrique**.
3. Repérer l'arc où l'abscisse (pour $\cos$) ou l'ordonnée (pour $\sin$) vérifie l'inégalité.

**Exemple.** $\cos x \geq \frac{1}{2}$ sur $[-\pi \,;\, \pi]$. Les points d'abscisse $\frac{1}{2}$ correspondent à $\pm\frac{\pi}{3}$. Les points d'abscisse supérieure à $\frac{1}{2}$ sont « à droite » de ces points : $\mathcal{S} = \left[-\frac{\pi}{3} \,;\, \frac{\pi}{3}\right]$.

---

## Méthode 3 — Exploiter parité et périodicité

**Les étapes**

1. **Périodicité** : vérifier si $f(x + T) = f(x)$ pour un $T$ (souvent $2\pi$, ou $\frac{2\pi}{\omega}$ pour $\cos(\omega x)$).
2. **Parité** : calculer $f(-x)$. Si $f(-x) = f(x)$, $f$ est paire ; si $f(-x) = -f(x)$, $f$ est impaire.
3. Réduire l'étude : sur un intervalle de longueur $T$, puis sur sa moitié positive si $f$ est paire ou impaire.

**Exemple.** $f(x) = \cos(2x) + 2\cos x$ est $2\pi$-périodique et paire : on l'étudie sur $[0 \,;\, \pi]$, puis on complète la courbe par symétrie par rapport à l'axe des ordonnées, puis par translations de $2\pi$.

---

## Méthode 4 — Étudier le signe d'une dérivée trigonométrique

**Les étapes**

1. Dériver, puis **factoriser** au maximum (souvent par $\sin x$ ou $\cos x$, à l'aide de $\sin 2x = 2\sin x\cos x$).
2. Étudier le signe de chaque facteur **sur l'intervalle d'étude**, avec le cercle trigonométrique.
3. Dresser un tableau de signes.

**Exemple.** $f(x) = \cos(2x) + 2\cos x$ sur $[0 \,;\, \pi]$ :

$$f'(x) = -2\sin(2x) - 2\sin x = -4\sin x\cos x - 2\sin x = -2\sin x\,(2\cos x + 1).$$

Sur $[0 \,;\, \pi]$, $\sin x \geq 0$, et $2\cos x + 1 > 0 \iff \cos x > -\frac{1}{2} \iff x < \frac{2\pi}{3}$.

---

## Méthode 5 — Calculer une limite avec sinus ou cosinus

**En $0$** : faire apparaître $\dfrac{\sin X}{X}$ avec $X \to 0$.

$$\frac{\sin(3x)}{x} = 3 \times \frac{\sin(3x)}{3x} \xrightarrow[x\to 0]{} 3.$$

**En l'infini** : $\sin$ et $\cos$ n'ont pas de limite, mais elles sont **bornées**. On encadre, puis on applique les gendarmes ou la comparaison :

$$-\frac{1}{x} \leq \frac{\sin x}{x} \leq \frac{1}{x} \quad (x > 0), \qquad \text{donc } \frac{\sin x}{x} \xrightarrow[x\to+\infty]{} 0.$$

!!! warning "Ne pas confondre"
    $\dfrac{\sin x}{x} \to 1$ quand $x \to 0$, mais $\dfrac{\sin x}{x} \to 0$ quand $x \to +\infty$.
