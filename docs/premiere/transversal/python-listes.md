# Algorithmique et programmation — les listes en Python

En Première, la nouveauté en programmation est la notion de **liste**. Elle sert dans presque tous les chapitres : termes d'une suite, valeurs d'une fonction, simulations en probabilités, coordonnées de vecteurs. Cette page rassemble l'essentiel et des exercices corrigés.

---

## 1. Créer et lire une liste

Une **liste** est une suite ordonnée de valeurs, écrite entre crochets.

```python
L = [3, 7, -1, 12]
print(L[0])       # 3 : le premier élément a l'indice 0
print(L[3])       # 12 : le dernier, d'indice len(L) - 1
print(L[-1])      # 12 : indice négatif = en partant de la fin
print(len(L))     # 4 : longueur de la liste
```

!!! warning "Les indices commencent à 0"
    Une liste de longueur $n$ a pour indices $0, 1, \ldots, n - 1$. Écrire `L[len(L)]` provoque une erreur `IndexError`.

**Modifier un élément** : `L[1] = 5` remplace $7$ par $5$.

---

## 2. Construire une liste

### Par ajouts successifs avec `append`

```python
carres = []
for k in range(1, 6):
    carres.append(k**2)
print(carres)     # [1, 4, 9, 16, 25]
```

### En compréhension

```python
carres = [k**2 for k in range(1, 6)]          # même résultat
pairs = [k for k in range(20) if k % 2 == 0]  # [0, 2, 4, ..., 18]
```

### Avec `range`

`list(range(a, b))` donne les entiers de $a$ à $b - 1$ ; `range(a, b, p)` avance de $p$ en $p$.

---

## 3. Parcourir une liste

```python
notes = [12, 15, 8, 17, 10]

# parcours des valeurs
somme = 0
for x in notes:
    somme = somme + x
moyenne = somme / len(notes)      # 12.4

# parcours des indices
for i in range(len(notes)):
    print("élève", i, ":", notes[i])
```

Fonctions utiles : `sum(L)`, `max(L)`, `min(L)`, `sorted(L)` (copie triée), `L.count(x)` (nombre d'occurrences de `x`), `x in L` (test d'appartenance).

---

## 4. Listes et mathématiques de Première

### Termes d'une suite

```python
def termes(n):
    """Renvoie la liste [u_0, ..., u_n] pour u_0 = 2 et u_{k+1} = 0.5 u_k + 3."""
    u = 2
    L = [u]
    for k in range(n):
        u = 0.5 * u + 3
        L.append(u)
    return L

print(termes(5))   # [2, 4.0, 5.0, 5.5, 5.75, 5.875] : la suite semble tendre vers 6
```

### Tableau de valeurs d'une fonction

```python
def f(x):
    return x**2 - 4*x + 3

X = [k / 2 for k in range(0, 9)]      # 0 ; 0,5 ; ... ; 4
Y = [f(x) for x in X]
```

### Simulation et fréquences

```python
from random import randint

lancers = [randint(1, 6) for i in range(1000)]
print(lancers.count(6) / 1000)        # proche de 1/6
```

### Moyenne et écart-type d'une série

```python
from math import sqrt

def moyenne(L):
    return sum(L) / len(L)

def ecart_type(L):
    m = moyenne(L)
    return sqrt(sum((x - m)**2 for x in L) / len(L))
```

---

## 5. Exercices corrigés

### Exercice 1 — Lire du code <span class="etoiles">★</span>

Que contient la liste `L` après l'exécution de ce programme ?

```python
L = [1]
for i in range(4):
    L.append(2 * L[-1])
```

??? success "Correction"
    `[1, 2, 4, 8, 16]` : chaque nouvel élément est le double du dernier. Ce sont les termes de la suite géométrique $2^n$.

### Exercice 2 — Suite arithmétique <span class="etoiles">★</span>

Écrire une fonction `arithmetique(u0, r, n)` qui renvoie la liste des termes $u_0, \ldots, u_n$ d'une suite arithmétique de premier terme `u0` et de raison `r`.

??? success "Correction"
    ```python
    def arithmetique(u0, r, n):
        return [u0 + k * r for k in range(n + 1)]
    ```

### Exercice 3 — Seuil <span class="etoiles">★★</span>

Écrire une fonction `au_dessus(L, s)` qui renvoie la liste des éléments de `L` strictement supérieurs à `s`, puis une fonction `premier_indice(L, s)` qui renvoie le premier indice `i` tel que `L[i] > s` (ou `None` s'il n'y en a pas).

??? success "Correction"
    ```python
    def au_dessus(L, s):
        return [x for x in L if x > s]

    def premier_indice(L, s):
        for i in range(len(L)):
            if L[i] > s:
                return i
        return None
    ```

### Exercice 4 — Maximum sans `max` <span class="etoiles">★★</span>

Écrire une fonction `maximum(L)` qui renvoie le plus grand élément d'une liste non vide, sans utiliser `max`.

??? success "Correction"
    ```python
    def maximum(L):
        m = L[0]
        for x in L:
            if x > m:
                m = x
        return m
    ```

### Exercice 5 — Loi empirique d'un dé <span class="etoiles">★★★</span>

Écrire une fonction `frequences(N)` qui simule $N$ lancers d'un dé équilibré et renvoie la liste `[f1, f2, ..., f6]` des fréquences d'apparition de chaque face. Que constate-t-on pour $N$ grand ?

??? success "Correction"
    ```python
    from random import randint

    def frequences(N):
        effectifs = [0] * 6               # [0, 0, 0, 0, 0, 0]
        for i in range(N):
            face = randint(1, 6)
            effectifs[face - 1] = effectifs[face - 1] + 1
        return [e / N for e in effectifs]

    print(frequences(100000))
    ```

    Pour $N$ grand, chaque fréquence est proche de $\frac{1}{6} \approx 0{,}167$.

[Retour à la page Première](../index.md)
