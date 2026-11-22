# Méthodes — Trigonométrie

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Convertir, placer un point, trouver la mesure principale

**Les étapes**

1. Conversion : $x$ en radians $= \alpha$ en degrés $\times \dfrac{\pi}{180}$.
2. Mesure principale de $x$ : retrancher ou ajouter des multiples de $2\pi$ jusqu'à tomber dans $]-\pi\,;\,\pi]$. Avec une fraction $\frac{p\pi}{q}$, on écrit $p$ sous la forme $2qk + r$.
3. Placer le point à partir de la mesure principale.

**Exemple.** Mesure principale de $\frac{25\pi}{4}$ : $25 = 24 + 1$, donc $\frac{25\pi}{4} = 6\pi + \frac{\pi}{4} = 3 \times 2\pi + \frac{\pi}{4}$. Mesure principale : $\frac{\pi}{4}$.

**Exemple.** $150° = 150 \times \frac{\pi}{180} = \frac{5\pi}{6}$ rad.

---

## Méthode 2 — Calculer le cosinus ou le sinus d'un angle « remarquable »

**Les étapes**

1. Se ramener à la mesure principale.
2. Exprimer l'angle avec un angle du premier quadrant : $\pi - a$, $\pi + a$, $-a$, avec $a \in \left\{\frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}\right\}$.
3. Appliquer les formules des angles associés, en **vérifiant le signe** sur le cercle.

**Exemple.** $\cos\frac{11\pi}{6}$ : $\frac{11\pi}{6} = 2\pi - \frac{\pi}{6}$, mesure principale $-\frac{\pi}{6}$. Donc $\cos\frac{11\pi}{6} = \cos\left(-\frac{\pi}{6}\right) = \cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$. (Le point est en bas à droite : cosinus positif.)

---

## Méthode 3 — Calculer $\cos x$ connaissant $\sin x$ (ou l'inverse)

**Les étapes**

1. Utiliser $\cos^2 x = 1 - \sin^2 x$.
2. Prendre la racine carrée, **avec le bon signe**, que l'on lit grâce à l'intervalle où se trouve $x$.

**Exemple.** $\sin x = \frac{3}{5}$ et $x \in \left[\frac{\pi}{2}\,;\,\pi\right]$. Alors $\cos^2 x = 1 - \frac{9}{25} = \frac{16}{25}$. Sur $\left[\frac{\pi}{2}\,;\,\pi\right]$, le cosinus est négatif : $\cos x = -\frac{4}{5}$.

---

## Méthode 4 — Simplifier une expression avec des angles associés

**Les étapes**

1. Traiter chaque terme séparément avec le tableau des angles associés.
2. Pour un angle comme $x + \pi$ ou $\frac{\pi}{2} + x$, l'écrire à partir des formes du tableau : $\frac{\pi}{2} + x = \frac{\pi}{2} - (-x)$.
3. Réduire.

**Exemple.** $A = \cos(\pi - x) + \cos(\pi + x) + 2\cos(-x) = -\cos x - \cos x + 2\cos x = 0$.

**Exemple.** $\sin\left(\frac{\pi}{2} + x\right) = \sin\left(\frac{\pi}{2} - (-x)\right) = \cos(-x) = \cos x$.

---

## Méthode 5 — Résoudre une équation ou une inéquation

**Les étapes**

1. Isoler $\cos x$ ou $\sin x$.
2. Reconnaître une valeur remarquable : écrire l'équation sous la forme $\cos x = \cos a$ ou $\sin x = \sin a$.
3. Écrire les solutions dans $\mathbb{R}$, puis garder celles de l'intervalle demandé.
4. Pour une inéquation, **lire l'arc de cercle** qui convient.

**Exemple.** $2\sin x + \sqrt{3} = 0$ dans $]-\pi\,;\,\pi]$. On a $\sin x = -\frac{\sqrt{3}}{2} = \sin\left(-\frac{\pi}{3}\right)$. Solutions dans $\mathbb{R}$ : $-\frac{\pi}{3} + 2k\pi$ et $\pi + \frac{\pi}{3} + 2k\pi = \frac{4\pi}{3} + 2k\pi$. Dans $]-\pi\,;\,\pi]$ : $S = \left\{-\frac{2\pi}{3}\,;\,-\frac{\pi}{3}\right\}$ (car $\frac{4\pi}{3} - 2\pi = -\frac{2\pi}{3}$).

**Exemple.** $\cos x \geq \frac{1}{2}$ dans $]-\pi\,;\,\pi]$ : l'arc à droite de la droite $x = \frac{1}{2}$ va de $-\frac{\pi}{3}$ à $\frac{\pi}{3}$. $S = \left[-\frac{\pi}{3}\,;\,\frac{\pi}{3}\right]$.
