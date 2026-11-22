# Méthodes — Suites : récurrence et limites

[📄 Télécharger les fiches méthode en PDF](pdf/methodes.pdf){ .md-button }

Chaque méthode donne **quand l'utiliser**, **les étapes** et **un exemple rédigé** comme on l'attend au bac.

---

## Méthode 1 — Rédiger une démonstration par récurrence

**Quand ?** L'énoncé demande de montrer une propriété « pour tout entier $n$ » et l'on peut passer facilement du rang $n$ au rang $n+1$ : formule explicite d'une suite définie par récurrence, inégalité, encadrement, divisibilité.

**Les étapes**

1. Écrire clairement la propriété $\mathcal{P}(n)$.
2. **Initialisation** : vérifier $\mathcal{P}(n_0)$ par un calcul.
3. **Hérédité** : « Soit $n \geq n_0$ tel que $\mathcal{P}(n)$ est vraie. Montrons $\mathcal{P}(n+1)$. » Partir de $u_{n+1}$ (ou du membre de gauche au rang $n+1$) et **utiliser l'hypothèse de récurrence**.
4. **Conclusion** : « Par récurrence, $\mathcal{P}(n)$ est vraie pour tout $n \geq n_0$. »

**Exemple.** $u_0 = 2$ et $u_{n+1} = \dfrac{1}{2}u_n + 1$. Montrer que $u_n \geq 2$ pour tout $n$.

On note $\mathcal{P}(n)$ : « $u_n \geq 2$ ».

- Initialisation : $u_0 = 2 \geq 2$.
- Hérédité : soit $n$ tel que $u_n \geq 2$. Alors $\dfrac{1}{2}u_n \geq 1$, donc $u_{n+1} = \dfrac{1}{2}u_n + 1 \geq 2$.
- Conclusion : pour tout $n \in \mathbb{N}$, $u_n \geq 2$.

!!! tip "Pour les encadrements"
    Si $u_{n+1} = f(u_n)$ avec $f$ **croissante** sur un intervalle, on applique $f$ à l'encadrement de $u_n$ : l'ordre est conservé. C'est souvent la clé de l'hérédité (voir l'exercice 24).

---

## Méthode 2 — Lever une forme indéterminée

**Quand ?** Les opérations sur les limites aboutissent à $\infty - \infty$, $0 \times \infty$, $\dfrac{\infty}{\infty}$ ou $\dfrac{0}{0}$.

**Technique A : factoriser par le terme dominant** (polynômes, quotients de polynômes)

$$\frac{2n^2 + 3n}{5n^2 - 1} = \frac{n^2\left(2 + \frac{3}{n}\right)}{n^2\left(5 - \frac{1}{n^2}\right)} = \frac{2 + \frac{3}{n}}{5 - \frac{1}{n^2}} \longrightarrow \frac{2}{5}.$$

**Technique B : multiplier par la quantité conjuguée** (différence de racines carrées)

$$\sqrt{n+1} - \sqrt{n} = \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}} \longrightarrow 0.$$

**Technique C : factoriser par la plus grande puissance** (suites géométriques)

$$4^n - 3^n = 4^n\left(1 - \left(\tfrac{3}{4}\right)^n\right) \longrightarrow +\infty \quad \text{car } \left(\tfrac{3}{4}\right)^n \to 0.$$

---

## Méthode 3 — Utiliser un théorème de comparaison

**Quand ?** La suite contient un terme qui **oscille** ($(-1)^n$, $\cos n$, $\sin n$) ou une expression difficile à calculer directement, mais **facile à encadrer**.

**Les étapes**

1. Encadrer le terme gênant : $-1 \leq \cos n \leq 1$, $-1 \leq (-1)^n \leq 1$…
2. En déduire une inégalité (ou un encadrement) sur $u_n$, en faisant attention au **signe** quand on multiplie ou divise.
3. Conclure :
    - limite infinie : **théorème de comparaison** (une seule inégalité suffit) ;
    - limite finie : **théorème des gendarmes** (il faut un encadrement dont les deux bornes ont **la même limite**).

**Exemple.** $u_n = \dfrac{\sin n}{n}$ pour $n \geq 1$. On a $-1 \leq \sin n \leq 1$ et $n > 0$, donc $-\dfrac{1}{n} \leq u_n \leq \dfrac{1}{n}$. Les deux bornes tendent vers $0$ : d'après le théorème des gendarmes, $\lim u_n = 0$.

---

## Méthode 4 — Montrer qu'une suite converge sans calculer sa limite

**Quand ?** La suite est définie par récurrence et l'on n'a pas de formule explicite.

**Les étapes**

1. Étudier le **sens de variation** : signe de $u_{n+1} - u_n$, ou récurrence sur « $u_n \leq u_{n+1}$ ».
2. Trouver un **majorant** (si croissante) ou un **minorant** (si décroissante), souvent par récurrence.
3. Conclure avec le théorème de convergence monotone : « $(u_n)$ est croissante et majorée, donc elle converge. »

!!! warning "Piège classique"
    Un majorant n'est **pas** forcément la limite. Si $u_n \leq 3$, on sait seulement que $\ell \leq 3$.

---

## Méthode 5 — Étudier une suite arithmético-géométrique

**Quand ?** $u_{n+1} = a\,u_n + b$, avec $a \neq 1$ et $b \neq 0$.

**Les étapes**

1. Chercher le réel $c$ tel que $c = ac + b$, c'est-à-dire $c = \dfrac{b}{1-a}$.
2. Poser $v_n = u_n - c$ (l'énoncé le donne en général) et montrer que $(v_n)$ est géométrique de raison $a$ :

$$v_{n+1} = u_{n+1} - c = a u_n + b - c = a u_n - ac = a(u_n - c) = a\,v_n.$$

3. En déduire $v_n = v_0 \times a^n$, puis $u_n = v_0 \times a^n + c$.
4. Calculer la limite avec le théorème sur $(q^n)$.

---

## Méthode 6 — Écrire un algorithme de seuil en Python

**Quand ?** On sait que $(u_n)$ tend vers $+\infty$ (ou vers $\ell$) et l'on cherche **le plus petit rang** $n$ à partir duquel $u_n$ dépasse une valeur donnée.

**Le modèle**

```python
def seuil(S):
    n = 0
    u = 2              # valeur de u_0
    while u <= S:      # on continue TANT QUE la condition n'est PAS atteinte
        u = 3 * u - 1  # relation de récurrence
        n = n + 1
    return n
```

!!! tip "Trois points à vérifier"
    - La condition du `while` est **le contraire** de la condition cherchée.
    - On met à jour `u` **et** `n` dans la boucle.
    - L'algorithme ne termine que si la suite atteint bien le seuil : il faut le justifier d'abord par un calcul de limite.
