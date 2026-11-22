# Méthodes — Probabilités conditionnelles et indépendance

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Lire une probabilité conditionnelle dans un tableau croisé

**Les étapes**

1. Repérer la condition (« sachant que… », « parmi les… ») : c'est l'événement $A$ de $P_A(B)$.
2. Se placer dans la **ligne ou la colonne** de $A$ : c'est la nouvelle population de référence.
3. Diviser l'effectif de $A \cap B$ par l'effectif total de $A$.

**Exemple.** Dans un club de $200$ sportifs :

| | Fille ($F$) | Garçon ($G$) | Total |
|---|---|---|---|
| Football ($Fo$) | $30$ | $70$ | $100$ |
| Natation ($N$) | $50$ | $50$ | $100$ |
| Total | $80$ | $120$ | $200$ |

Probabilité qu'un sportif choisi au hasard fasse du football **sachant que c'est une fille** : $P_F(Fo) = \frac{30}{80} = \frac{3}{8}$. Probabilité que ce soit une fille **sachant qu'il fait du football** : $P_{Fo}(F) = \frac{30}{100} = 0{,}3$.

---

## Méthode 2 — Construire et exploiter un arbre pondéré

**Les étapes**

1. Nommer les événements et repérer l'**ordre chronologique** (ou logique) : ce qui est donné « sans condition » va au premier niveau.
2. Traduire chaque pourcentage de l'énoncé : « $15\,\%$ **des** $A$ sont $B$ » se traduit par $P_A(B) = 0{,}15$ (une probabilité conditionnelle, au second niveau).
3. Compléter les branches : la somme des branches issues d'un même nœud vaut $1$.
4. Probabilité d'un chemin : **produit** des branches. Probabilité d'un événement : **somme** des chemins qui y mènent.

**Exemple.** $60\,\%$ des clients d'un magasin paient par carte ($C$), les autres en espèces. $30\,\%$ des clients payant par carte achètent un produit en promotion ($R$), contre $20\,\%$ des autres.

Arbre : $P(C) = 0{,}6$, $P\left(\overline{C}\right) = 0{,}4$, $P_C(R) = 0{,}3$, $P_C\left(\overline{R}\right) = 0{,}7$, $P_{\overline{C}}(R) = 0{,}2$, $P_{\overline{C}}\left(\overline{R}\right) = 0{,}8$.

$P(C \cap R) = 0{,}6 \times 0{,}3 = 0{,}18$.

---

## Méthode 3 — Probabilités totales et inversion du conditionnement

**Les étapes**

1. Pour $P(B)$ : additionner les probabilités de **tous les chemins** qui mènent à $B$ (formule des probabilités totales).
2. Pour une probabilité « à l'envers » $P_B(A)$, alors que l'arbre commence par $A$ : écrire $P_B(A) = \dfrac{P(A \cap B)}{P(B)}$, où $P(A \cap B)$ se lit sur un chemin et $P(B)$ vient de l'étape 1.

**Exemple (suite).** $P(R) = 0{,}6 \times 0{,}3 + 0{,}4 \times 0{,}2 = 0{,}18 + 0{,}08 = 0{,}26$.

Probabilité qu'un client ayant acheté en promotion ait payé par carte :
$$P_R(C) = \frac{0{,}18}{0{,}26} = \frac{18}{26} = \frac{9}{13}.$$

---

## Méthode 4 — Démontrer que deux événements sont indépendants (ou non)

**Les étapes**

1. Calculer $P(A)$, $P(B)$ et $P(A \cap B)$.
2. Comparer $P(A \cap B)$ et $P(A) \times P(B)$ : égaux si et seulement si $A$ et $B$ sont indépendants.
3. *Variante* : comparer $P_A(B)$ et $P(B)$.

**Exemple (suite).** $P(C) \times P(R) = 0{,}6 \times 0{,}26 = 0{,}156 \neq 0{,}18 = P(C \cap R)$ : les événements $C$ et $R$ **ne sont pas** indépendants. On le voit aussi avec $P_C(R) = 0{,}3 \neq 0{,}26 = P(R)$.

---

## Méthode 5 — Répéter une épreuve de Bernoulli

**Les étapes**

1. Identifier l'épreuve de Bernoulli : le **succès** et sa probabilité $p$, puis le nombre $n$ de répétitions **indépendantes**.
2. Un chemin avec $k$ succès a pour probabilité $p^k q^{n-k}$, où $q = 1 - p$.
3. Compter les chemins qui conviennent (avec l'arbre, ou en listant les positions des succès), puis multiplier.
4. Pour « au moins un », passer par le contraire : $1 - q^n$.

**Exemple.** On lance $4$ fois un dé équilibré. Succès : « obtenir $6$ », $p = \frac{1}{6}$. Probabilité d'obtenir exactement un $6$ : il y a $4$ chemins (le $6$ peut arriver au 1er, 2e, 3e ou 4e lancer), donc
$$4 \times \frac{1}{6} \times \left(\frac{5}{6}\right)^3 = \frac{4 \times 125}{1\,296} = \frac{500}{1\,296} = \frac{125}{324}.$$
Probabilité d'au moins un $6$ : $1 - \left(\frac{5}{6}\right)^4 = 1 - \frac{625}{1\,296} = \frac{671}{1\,296} \approx 0{,}52$.
