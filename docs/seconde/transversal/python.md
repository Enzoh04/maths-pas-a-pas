# Algorithmique et programmation en Python

En Seconde, on apprend les bases de la programmation en **Python** : variables, instructions conditionnelles, boucles et fonctions. Ces outils servent dans tous les chapitres (calculs répétitifs, balayage, simulations). Cette page rassemble l'essentiel et des exercices corrigés. Les **listes** sont approfondies en Première ([page dédiée](../../premiere/transversal/python-listes.md)).

---

## 1. Variables et affectation

Une **variable** est un nom associé à une valeur. L'**affectation** se note `=` : `x = 3` donne à `x` la valeur $3$ (ce n'est pas une égalité mathématique : `x = x + 1` augmente `x` de $1$).

```python
a = 5          # entier (int)
b = 2.5        # nombre décimal (float)
nom = "Lou"    # chaîne de caractères (str)
test = a > b   # booléen (bool) : True
c = a * b + 1  # 13.5
```

Opérations utiles : `+`, `-`, `*`, `/` (division décimale), `//` (quotient entier), `%` (reste), `**` (puissance). Par exemple `17 // 5` vaut `3` et `17 % 5` vaut `2`.

!!! tip "Tester la parité"
    `n % 2 == 0` est vrai si et seulement si `n` est pair ; plus généralement, `n % d == 0` teste si `d` divise `n`.

---

## 2. Instructions conditionnelles

```python
def mention(note):
    if note >= 16:
        return "très bien"
    elif note >= 14:
        return "bien"
    elif note >= 10:
        return "admis"
    else:
        return "non admis"
```

Les blocs sont délimités par l'**indentation** (quatre espaces). Comparaisons : `==` (égal), `!=` (différent), `<`, `<=`, `>`, `>=` ; on combine avec `and`, `or`, `not`.

---

## 3. Boucles

### Boucle bornée `for`

On répète un nombre de fois **connu à l'avance**. `range(n)` parcourt $0, 1, \ldots, n - 1$ ; `range(a, b)` parcourt $a, \ldots, b - 1$.

```python
somme = 0
for k in range(1, 101):
    somme = somme + k
print(somme)     # 5050 = 1 + 2 + ... + 100
```

### Boucle non bornée `while`

On répète **tant qu'une condition est vraie**, sans savoir à l'avance combien de fois.

```python
capital = 1000
annees = 0
while capital < 2000:
    capital = capital * 1.05
    annees = annees + 1
print(annees)    # 15 : le capital double en 15 ans à 5 % par an
```

!!! warning "Boucle infinie"
    Dans une boucle `while`, il faut s'assurer que la condition finira par devenir fausse, sinon le programme ne s'arrête jamais.

---

## 4. Fonctions

Une **fonction** Python reçoit des **arguments** et **renvoie** un résultat avec `return`.

```python
def f(x):
    return x**2 - 3*x + 1

def aire_rectangle(longueur, largeur):
    return longueur * largeur

print(f(2), aire_rectangle(3, 4))   # -1 12
```

---

## 5. Nombres aléatoires

```python
from random import randint, random

de = randint(1, 6)    # entier au hasard entre 1 et 6 (inclus)
x = random()          # réel au hasard dans [0 ; 1[
pile = random() < 0.5 # True avec la probabilité 0,5
```

---

## 6. Exercices corrigés

### Exercice 1 — Lire un programme <span class="etoiles">★</span>

Que valent `a` et `b` à la fin du programme ?

```python
a = 3
b = 5
a = a + b
b = a - b
a = a - b
```

??? success "Correction"
    $a = 8$, puis $b = 3$, puis $a = 5$. Les valeurs de `a` et `b` ont été **échangées**.

### Exercice 2 — Diviseurs <span class="etoiles">★</span>

Écrire une fonction `diviseurs(n)` qui affiche tous les diviseurs positifs de l'entier `n`.

??? success "Correction"
    ```python
    def diviseurs(n):
        for d in range(1, n + 1):
            if n % d == 0:
                print(d)
    ```

### Exercice 3 — Seuil <span class="etoiles">★★</span>

Une population de bactéries double toutes les heures, en partant de $500$. Écrire un programme qui détermine au bout de combien d'heures elle dépasse un million.

??? success "Correction"
    ```python
    population = 500
    heures = 0
    while population <= 1000000:
        population = population * 2
        heures = heures + 1
    print(heures)   # 11 (500 × 2^11 = 1 024 000)
    ```

### Exercice 4 — Équation du premier degré <span class="etoiles">★★</span>

Écrire une fonction `solution(a, b)` qui renvoie la solution de $ax + b = 0$ si elle est unique, et un message sinon.

??? success "Correction"
    ```python
    def solution(a, b):
        if a != 0:
            return -b / a
        elif b == 0:
            return "tous les réels sont solutions"
        else:
            return "pas de solution"
    ```

### Exercice 5 — Balayage <span class="etoiles">★★★</span>

La fonction $f(x) = x^3 + x - 1$ s'annule une seule fois sur $[0\,;\,1]$. Écrire un programme qui donne un encadrement de cette solution d'amplitude $0{,}01$ par balayage.

??? success "Correction"
    ```python
    def f(x):
        return x**3 + x - 1

    x = 0
    while f(x + 0.01) < 0:
        x = x + 0.01
    print(x, x + 0.01)   # environ 0.68 et 0.69
    ```

    On avance tant que $f$ reste négative au point suivant ($f$ est croissante sur $[0\,;\,1]$, car $x^3$ et $x$ le sont).

### Exercice 6 — Simulation <span class="etoiles">★★★</span>

On lance un dé jusqu'à obtenir un $6$. Écrire une fonction `attente()` qui renvoie le nombre de lancers nécessaires, puis estimer le nombre moyen de lancers sur $10\,000$ simulations.

??? success "Correction"
    ```python
    from random import randint

    def attente():
        n = 1
        while randint(1, 6) != 6:
            n = n + 1
        return n

    total = 0
    for k in range(10000):
        total = total + attente()
    print(total / 10000)   # environ 6
    ```

    En moyenne, il faut environ $6$ lancers : c'est l'inverse de la probabilité $\frac{1}{6}$ (résultat démontré dans le supérieur).

[Retour à la page Seconde](../index.md)
