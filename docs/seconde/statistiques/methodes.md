# Méthodes — Information chiffrée et statistiques

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Calculer avec des proportions

**Les étapes**

1. Identifier la **population de référence** (le « tout ») et la **sous-population** (la « partie »).
2. Proportion $= \dfrac{\text{effectif de la partie}}{\text{effectif du tout}}$ ; effectif de la partie $=$ proportion $\times$ effectif du tout.
3. Pour une **proportion de proportion**, multiplier les proportions.

**Exemple.** Dans une entreprise de $250$ salariés, $40\,\%$ sont des cadres, et $35\,\%$ des cadres sont des femmes. Proportion de femmes cadres parmi les salariés : $0{,}4 \times 0{,}35 = 0{,}14$, soit $14\,\%$. Nombre de femmes cadres : $250 \times 0{,}14 = 35$.

---

## Méthode 2 — Calculer avec des évolutions

**Les étapes**

1. Traduire chaque évolution par un **coefficient multiplicateur** : $+t\,\% \to 1 + \frac{t}{100}$ ; $-t\,\% \to 1 - \frac{t}{100}$.
2. Pour des évolutions **successives**, **multiplier** les coefficients.
3. Revenir à un taux : $t = CM - 1$ (puis $\times 100$ pour l'exprimer en pourcentage).
4. Pour retrouver une **valeur de départ**, diviser par le coefficient : $V_D = \dfrac{V_A}{CM}$.

**Exemple.** Un prix augmente de $10\,\%$ puis baisse de $30\,\%$ : $1{,}1 \times 0{,}7 = 0{,}77$, soit une baisse globale de $23\,\%$. Pour revenir au prix initial, il faudrait multiplier par $\frac{1}{0{,}77} \approx 1{,}299$, soit une hausse d'environ $29{,}9\,\%$.

**Exemple.** Après une hausse de $25\,\%$, un article coûte $75$ € : avant, il coûtait $\frac{75}{1{,}25} = 60$ €.

---

## Méthode 3 — Calculer la médiane et les quartiles

**Les étapes**

1. **Ranger** les valeurs dans l'ordre croissant (en répétant les valeurs autant de fois que leur effectif), et compter l'effectif total $N$.
2. **Médiane** : rang $\frac{N + 1}{2}$ si $N$ est impair ; moyenne des rangs $\frac{N}{2}$ et $\frac{N}{2} + 1$ si $N$ est pair.
3. **$Q_1$** : calculer $\frac{N}{4}$ et arrondir à l'entier **supérieur** : c'est le rang de $Q_1$. **$Q_3$** : de même avec $\frac{3N}{4}$.
4. Avec un tableau d'effectifs, utiliser les **effectifs cumulés croissants** pour trouver la valeur d'un rang donné.

**Exemple.** Pointures de $25$ élèves :

| Pointure | $37$ | $38$ | $39$ | $40$ | $41$ | $42$ |
|---|---|---|---|---|---|---|
| Effectif | $3$ | $5$ | $6$ | $5$ | $4$ | $2$ |
| Effectif cumulé | $3$ | $8$ | $14$ | $19$ | $23$ | $25$ |

$N = 25$ : médiane au rang $13$, soit $39$ ; $\frac{25}{4} = 6{,}25$, $Q_1$ au rang $7$ : $38$ ; $\frac{75}{4} = 18{,}75$, $Q_3$ au rang $19$ : $40$.

---

## Méthode 4 — Calculer une moyenne et un écart type

**Les étapes**

1. Moyenne : $\bar{x} = \frac{\sum n_ix_i}{N}$ (avec les **centres** des classes pour une série en classes).
2. Variance : moyenne des carrés des écarts, $V = \frac{\sum n_i(x_i - \bar{x})^2}{N}$.
3. Écart type : $\sigma = \sqrt{V}$ (à la calculatrice ou en Python pour les séries importantes).
4. Interpréter : comparer deux séries par leurs moyennes, puis par leurs écarts types (dispersion).

**Exemple.** Série $6\,;\,8\,;\,10\,;\,12\,;\,14$ : $\bar{x} = 10$, $V = \frac{16 + 4 + 0 + 4 + 16}{5} = 8$, $\sigma = \sqrt{8} = 2\sqrt{2} \approx 2{,}83$.

---

## Méthode 5 — Exploiter un tableau croisé

**Les étapes**

1. Compléter les **totaux** de lignes et de colonnes.
2. **Fréquence marginale** : total d'une ligne (ou colonne) divisé par l'effectif total.
3. **Fréquence conditionnelle** « parmi les $B$ » : effectif de la case divisé par le **total de $B$**.
4. Comparer des fréquences conditionnelles pour savoir si deux caractères semblent liés.

**Exemple.** Avec le tableau du cours (sport selon le sexe) : la proportion de sportifs est $0{,}6$ parmi les filles et $\frac{180}{300} = 0{,}6$ parmi les garçons. Elle est la même : dans cette population, la pratique du sport ne dépend pas du sexe.
