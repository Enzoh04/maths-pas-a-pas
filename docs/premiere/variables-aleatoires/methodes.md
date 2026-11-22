# Méthodes — Variables aléatoires réelles

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Déterminer la loi d'une variable aléatoire

**Les étapes**

1. Lister **toutes les valeurs** possibles de $X$.
2. Pour chaque valeur $x_i$, déterminer l'événement $\{X = x_i\}$ et calculer sa probabilité (dénombrement, arbre, tableau).
3. Présenter la loi dans un tableau et **vérifier que la somme des probabilités vaut $1$**.

**Exemple.** On lance deux pièces équilibrées ; $X$ est le nombre de « pile ». Issues équiprobables : $PP$, $PF$, $FP$, $FF$.

| $k$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $P(X = k)$ | $\frac{1}{4}$ | $\frac{1}{2}$ | $\frac{1}{4}$ |

Vérification : $\frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1$.

---

## Méthode 2 — Calculer et interpréter une espérance

**Les étapes**

1. Écrire $E(X) = \sum p_ix_i$ en suivant le tableau de la loi.
2. Mettre au même dénominateur, ou calculer en décimaux.
3. Interpréter : moyenne des valeurs sur un grand nombre de répétitions. Pour un jeu : $E(X) > 0$ favorable au joueur, $E(X) = 0$ équitable, $E(X) < 0$ défavorable.

**Exemple.** Un jeu coûte $2$ € ; on gagne $10$ € avec la probabilité $0{,}1$, $3$ € avec la probabilité $0{,}2$, rien sinon. Le gain **net** $G$ vaut $8$, $1$ ou $-2$ :
$$E(G) = 0{,}1 \times 8 + 0{,}2 \times 1 + 0{,}7 \times (-2) = 0{,}8 + 0{,}2 - 1{,}4 = -0{,}4.$$
Le jeu est défavorable : en moyenne, on perd $0{,}40$ € par partie.

!!! warning "Penser à la mise"
    Le gain net, c'est ce que l'on reçoit **moins** ce que l'on a payé.

---

## Méthode 3 — Calculer une variance et un écart-type

**Les étapes**

1. Calculer $E(X)$.
2. Calculer $E\left(X^2\right) = \sum p_ix_i^2$ (on élève les **valeurs** au carré, pas les probabilités).
3. $V(X) = E\left(X^2\right) - E(X)^2$, puis $\sigma(X) = \sqrt{V(X)}$.

**Exemple (suite).** $E\left(G^2\right) = 0{,}1 \times 64 + 0{,}2 \times 1 + 0{,}7 \times 4 = 6{,}4 + 0{,}2 + 2{,}8 = 9{,}4$, donc $V(G) = 9{,}4 - 0{,}16 = 9{,}24$ et $\sigma(G) = \sqrt{9{,}24} \approx 3{,}04$ €.

---

## Méthode 4 — Utiliser la linéarité

**Les étapes**

1. Exprimer la nouvelle variable en fonction de l'ancienne : $Y = aX + b$.
2. Appliquer $E(Y) = aE(X) + b$, $V(Y) = a^2V(X)$, $\sigma(Y) = |a|\sigma(X)$.
3. **Ne pas** ajouter $b$ à la variance ni à l'écart-type.

**Exemple.** Un commerçant vend $X$ objets par jour, avec $E(X) = 12$ et $\sigma(X) = 3$. Son bénéfice quotidien est $B = 15X - 40$ (en euros). Alors $E(B) = 15 \times 12 - 40 = 140$ € et $\sigma(B) = 15 \times 3 = 45$ €.

---

## Méthode 5 — Trouver un paramètre pour qu'un jeu soit équitable

**Les étapes**

1. Écrire la loi du gain net en fonction du paramètre inconnu (mise $m$, gain $g$, probabilité…).
2. Calculer l'espérance en fonction du paramètre.
3. Résoudre $E(X) = 0$ (ou l'inéquation demandée).

**Exemple.** On tire une carte dans un jeu de $32$ cartes. On gagne $g$ € si c'est un as, sinon on perd $1$ €. Le gain vaut $g$ avec la probabilité $\frac{4}{32} = \frac{1}{8}$ et $-1$ avec la probabilité $\frac{7}{8}$ :
$$E(X) = \frac{g}{8} - \frac{7}{8} = 0 \iff g = 7.$$
Le jeu est équitable si l'on gagne $7$ € avec un as.
