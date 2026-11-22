# Méthodes — Combinatoire et dénombrement

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Choisir le bon modèle

**Les deux questions à se poser**

1. **L'ordre compte-t-il ?** Échanger deux éléments donne-t-il un résultat différent ? (Oui pour un code ou un podium, non pour une main de cartes ou un comité.)
2. **Les répétitions sont-elles possibles ?** Peut-on choisir deux fois le même élément ? (Oui pour un code, non pour des personnes.)

| | Répétitions | Pas de répétition |
|---|---|---|
| **Ordre** | $n^k$ | $\dfrac{n!}{(n - k)!}$ |
| **Pas d'ordre** | (hors programme) | $\dbinom{n}{k}$ |

**Rédaction.** On écrit toujours la phrase de modélisation : « Un tirage correspond à une partie à 5 éléments d'un ensemble à 32 éléments, donc il y en a $\binom{32}{5}$. »

---

## Méthode 2 — Utiliser le principe multiplicatif

**Les étapes**

1. Décomposer le choix en **étapes successives**.
2. Compter le nombre de possibilités **à chaque étape** (il peut dépendre des choix précédents, mais pas son **nombre**).
3. Multiplier.

**Exemple.** Nombres de 4 chiffres distincts (le premier n'étant pas $0$) : $9$ choix pour le premier chiffre (pas $0$), puis $9$ pour le deuxième ($0$ est permis, mais pas le premier chiffre), puis $8$, puis $7$ : $9 \times 9 \times 8 \times 7 = 4\,536$.

!!! tip "Traiter d'abord les contraintes"
    On commence par l'étape la plus **contrainte** (ici le premier chiffre). Sinon, le nombre de choix aux étapes suivantes dépend des cas.

---

## Méthode 3 — Passer par le complémentaire

**Quand ?** L'énoncé dit « **au moins un** » : il est souvent plus simple de compter le contraire, « **aucun** ».

$$\operatorname{Card}(\text{au moins un}) = \operatorname{Card}(\text{total}) - \operatorname{Card}(\text{aucun}).$$

**Exemple.** Mains de 5 cartes parmi 32 contenant au moins un cœur : il y a $\binom{24}{5}$ mains sans cœur (on choisit parmi les 24 autres cartes), donc $\binom{32}{5} - \binom{24}{5} = 201\,376 - 42\,504 = 158\,872$ mains.

---

## Méthode 4 — Combinaisons avec conditions

**Quand ?** On choisit des éléments dans **plusieurs groupes** avec des contraintes : « exactement 2 femmes et 2 hommes », « exactement 2 as »…

**Les étapes**

1. Choisir dans **chaque groupe** le nombre d'éléments imposé : $\binom{n_1}{k_1}$, $\binom{n_2}{k_2}$…
2. **Multiplier** (principe multiplicatif).
3. Pour « au moins » ou « au plus », **additionner** les cas disjoints, ou passer par le complémentaire.

**Exemple.** Comité de 4 personnes choisies parmi 6 femmes et 5 hommes, avec exactement 2 femmes : $\binom{6}{2} \times \binom{5}{2} = 15 \times 10 = 150$.

!!! warning "Erreur fréquente"
    Pour « au moins une femme », compter « une femme, puis 3 personnes quelconques » donne $6 \times \binom{10}{3}$, ce qui est **faux** : un comité avec deux femmes serait compté deux fois. Il faut passer par le complémentaire.

---

## Méthode 5 — Démontrer une identité par double dénombrement

**Principe.** Pour montrer que deux expressions sont égales, on montre qu'elles **comptent le même ensemble** de deux façons différentes.

**Exemple.** $k\binom{n}{k} = n\binom{n - 1}{k - 1}$. On compte les comités de $k$ personnes parmi $n$, avec un président choisi dans le comité.

- On choisit le comité ($\binom{n}{k}$), puis le président parmi ses membres ($k$) : $k\binom{n}{k}$.
- On choisit le président ($n$), puis les $k - 1$ autres membres parmi les $n - 1$ restants : $n\binom{n - 1}{k - 1}$.

---

## Méthode 6 — Calculer et vérifier avec Python

```python
from math import factorial, comb, perm
from itertools import permutations, combinations, product

comb(32, 5)       # nombre de combinaisons : 201376
perm(10, 3)       # nombre d'arrangements : 720
factorial(5)      # 5! = 120

# Vérification par énumération : anagrammes de "ANANAS"
len(set(permutations("ANANAS")))   # 60
```

L'énumération par ordinateur est un excellent moyen de **vérifier** un dénombrement, sur des petits cas.
