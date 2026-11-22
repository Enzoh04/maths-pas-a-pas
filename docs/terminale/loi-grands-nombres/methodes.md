# Méthodes — Concentration, loi des grands nombres

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Appliquer l'inégalité de Bienaymé-Tchebychev

**Les étapes**

1. Calculer (ou relever) $\mu = E(X)$ et $V = V(X)$.
2. **Traduire l'événement** sous la forme $|X - \mu| \geq \delta$ ou $|X - \mu| < \delta$. Un intervalle **centré en $\mu$** est indispensable : $\mu - \delta < X < \mu + \delta \iff |X - \mu| < \delta$.
3. Appliquer $P\big(|X - \mu| \geq \delta\big) \leq \dfrac{V}{\delta^2}$, ou la forme $P\big(|X - \mu| < \delta\big) \geq 1 - \dfrac{V}{\delta^2}$.

**Exemple.** $X \sim \mathcal{B}(400\,;\,0{,}05)$. Minorer $P(10 < X < 30)$.

$\mu = 20$ et $V = 400 \times 0{,}05 \times 0{,}95 = 19$. L'intervalle $]10, 30[$ est centré en $20$ : $10 < X < 30 \iff |X - 20| < 10$. Donc
$$P(10 < X < 30) = P\big(|X - 20| < 10\big) \geq 1 - \frac{19}{100} = 0{,}81.$$

!!! warning "Strict ou large ?"
    Pour une variable à valeurs entières, $P(11 \leq X \leq 29) = P(10 < X < 30)$. Pour un intervalle fermé comme $[10, 30]$, on minore simplement : $P(10 \leq X \leq 30) \geq P(10 < X < 30) \geq 0{,}81$.

---

## Méthode 2 — Appliquer l'inégalité de concentration

**Les étapes**

1. Identifier l'**échantillon** : $n$ variables indépendantes de même loi que $X$, et la moyenne $M_n$ (ou la fréquence $F_n$).
2. Déterminer $\mu = E(X)$ et $V = V(X)$. Pour une fréquence : $V = p(1 - p)$, ou la majoration $V \leq \frac{1}{4}$ si $p$ est inconnu.
3. Appliquer $P\big(|M_n - \mu| \geq \delta\big) \leq \dfrac{V}{n\,\delta^2}$.

**Exemple.** On lance $1\,000$ fois une pièce équilibrée. Majorer la probabilité que la fréquence de Pile s'écarte de $0{,}5$ d'au moins $0{,}05$.

$F_{1000}$ est la moyenne d'un échantillon de la loi de Bernoulli de paramètre $0{,}5$, de variance $0{,}25$. Donc
$$P\big(|F_{1000} - 0{,}5| \geq 0{,}05\big) \leq \frac{0{,}25}{1\,000 \times 0{,}05^2} = 0{,}1.$$

---

## Méthode 3 — Déterminer une taille d'échantillon

**Les étapes**

1. Repérer la **précision** $\delta$ et le **risque** $\alpha$ demandés : on veut $P\big(|M_n - \mu| \geq \delta\big) \leq \alpha$.
2. Il suffit que $\dfrac{V}{n\,\delta^2} \leq \alpha$, soit $n \geq \dfrac{V}{\alpha\,\delta^2}$.
3. Conclure par le **plus petit entier** qui convient, en précisant que cette taille est **suffisante** (pas forcément nécessaire).

**Exemple.** Un dé est lancé $n$ fois. Combien de lancers suffisent pour que la moyenne des résultats soit à moins de $0{,}1$ de $3{,}5$ avec une probabilité d'au moins $0{,}95$ ?

$V = \frac{35}{12}$, $\delta = 0{,}1$, $\alpha = 0{,}05$ : $n \geq \dfrac{35/12}{0{,}05 \times 0{,}01} \approx 5\,833{,}3$. Il suffit de $5\,834$ lancers.

---

## Méthode 4 — Estimer une probabilité par simulation

**Les étapes**

1. Écrire une fonction Python qui simule **une** expérience et renvoie $1$ si l'événement est réalisé, $0$ sinon.
2. La répéter $n$ fois et calculer la fréquence $F_n$.
3. Interpréter : d'après la loi des grands nombres, $F_n$ est proche de $p$ pour $n$ grand. Pour quantifier, $P\big(|F_n - p| \geq \delta\big) \leq \dfrac{1}{4n\,\delta^2}$.

**Exemple.** Estimer la probabilité que la somme de trois dés soit au moins $15$.

```python
from random import randint

def experience():
    s = randint(1, 6) + randint(1, 6) + randint(1, 6)
    return 1 if s >= 15 else 0

n = 100000
F = sum(experience() for i in range(n)) / n
print(F)    # environ 0.093
```

La valeur exacte est $\frac{20}{216} \approx 0{,}0926$ (en dénombrant les $20$ triplets). Avec $n = 100\,000$ : $P\big(|F_n - p| \geq 0{,}005\big) \leq \frac{1}{4 \times 100\,000 \times 0{,}005^2} = 0{,}1$.
