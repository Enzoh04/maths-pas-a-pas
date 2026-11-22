# Méthodes — Droites du plan

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **les étapes** et **un exemple rédigé**, sans calculatrice.

---

## Méthode 1 — Déterminer une équation cartésienne

**Les étapes**

1. Trouver un point $A$ de la droite et un vecteur directeur $\vec{u}\begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ (par exemple $\overrightarrow{AB}$).
2. Écrire $M(x\,;\,y) \in d \iff \det\left(\overrightarrow{AM}, \vec{u}\right) = 0$ et développer.
3. *Raccourci* : l'équation est de la forme $\beta x - \alpha y + c = 0$ ; on trouve $c$ en remplaçant par les coordonnées de $A$.

**Exemple.** Droite passant par $A(2\,;\,-1)$ et $B(5\,;\,1)$. $\overrightarrow{AB}\begin{pmatrix} 3 \\ 2 \end{pmatrix}$ : équation $2x - 3y + c = 0$. Avec $A$ : $4 + 3 + c = 0$, donc $c = -7$. Équation : $2x - 3y - 7 = 0$. Vérification avec $B$ : $10 - 3 - 7 = 0$. ✓

---

## Méthode 2 — Déterminer l'équation réduite passant par deux points

**Les étapes**

1. Si $x_A = x_B$, la droite a pour équation $x = x_A$.
2. Sinon, calculer $m = \dfrac{y_B - y_A}{x_B - x_A}$.
3. Trouver $p$ en écrivant que $A$ est sur la droite : $y_A = mx_A + p$.
4. Vérifier avec $B$.

**Exemple.** $A(2\,;\,1)$ et $B(6\,;\,-1)$. $m = \frac{-1 - 1}{6 - 2} = -\frac{1}{2}$. $1 = -\frac{1}{2} \times 2 + p$, donc $p = 2$. Équation : $y = -\frac{1}{2}x + 2$. Vérification : $-3 + 2 = -1$. ✓

---

## Méthode 3 — Tracer une droite et lire son équation

**Les étapes**

1. **Tracer** $y = mx + p$ : placer le point $(0\,;\,p)$, puis à partir de ce point, avancer de $1$ (ou de $q$ si $m = \frac{r}{q}$) et monter de $m$ (ou de $r$). On peut aussi calculer deux points.
2. Pour une équation cartésienne, passer d'abord à l'équation réduite, ou chercher deux points (souvent les intersections avec les axes).
3. **Lire** une équation : repérer l'ordonnée à l'origine $p$, puis lire $m$ comme « variation verticale / variation horizontale » entre deux points à coordonnées entières.

**Exemple.** Tracer $d : 3x + 2y - 6 = 0$. Pour $x = 0$ : $y = 3$ ; pour $y = 0$ : $x = 2$. La droite passe par $(0\,;\,3)$ et $(2\,;\,0)$. Équation réduite : $y = -\frac{3}{2}x + 3$.

---

## Méthode 4 — Étudier la position relative de deux droites

**Les étapes**

1. Comparer les coefficients directeurs (équations réduites) ou calculer $ab' - a'b$ (équations cartésiennes).
2. Si les droites sont parallèles, vérifier si elles sont **confondues** (un point de l'une est-il sur l'autre ?).
3. Si elles sont sécantes, résoudre le système formé par les deux équations : la solution donne les coordonnées du point d'intersection.

**Exemple.** $d : y = 2x - 1$ et $d' : y = -x + 5$. $2 \neq -1$ : sécantes. $2x - 1 = -x + 5 \iff x = 2$, puis $y = 3$. Point d'intersection : $(2\,;\,3)$.

---

## Méthode 5 — Résoudre un problème avec un système

**Les étapes**

1. Choisir **deux inconnues** et préciser leur signification (et leur unité).
2. Traduire l'énoncé par **deux équations**.
3. Résoudre par **substitution** (si une inconnue s'isole facilement) ou par **combinaison**.
4. Vérifier dans les deux équations, puis **répondre à la question** par une phrase.

**Exemple.** Au cinéma, $3$ places adulte et $2$ places enfant coûtent $41$ € ; $2$ places adulte et $4$ places enfant coûtent $42$ €. Avec $a$ et $e$ les prix (en €) :
$$\begin{cases} 3a + 2e = 41 \\ 2a + 4e = 42 \end{cases} \quad \to \quad \begin{cases} 6a + 4e = 82 \\ 2a + 4e = 42 \end{cases} \quad \to \quad 4a = 40.$$
Donc $a = 10$, puis $2e = 41 - 30$, $e = 5{,}5$. Une place adulte coûte $10$ € et une place enfant $5{,}50$ €. Vérification : $20 + 22 = 42$. ✓
