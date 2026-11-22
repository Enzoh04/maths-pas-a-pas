# Maths Pas à Pas

Site de mathématiques construit avec MkDocs Material. Les formules sont rendues par KaTeX, inclus dans le dossier `docs/javascripts/katex` pour que le site fonctionne sans dépendre d'un service externe.

## Organisation

```
mkdocs.yml                  ← réglages du site et menu (rubrique nav)
docs/
  index.md                  ← page d'accueil
  terminale/
    index.md                ← liste des chapitres de Terminale
    suites/
      index.md              ← présentation du chapitre
      cours.md
      methodes.md
      exercices.md
  stylesheets/extra.css     ← couleurs des encadrés (définition, théorème…)
  javascripts/              ← KaTeX et son initialisation
```

Chaque page est un fichier Markdown : du texte presque brut, avec les formules entre `$...$` (dans la ligne) ou `$$...$$` (centrées).

## Voir le site sur ton ordinateur

1. Installer Python 3, puis dans un terminal ouvert dans ce dossier :
   `pip install -r requirements.txt`
2. Lancer `mkdocs serve`, puis ouvrir http://127.0.0.1:8000 dans le navigateur.
   Chaque modification d'un fichier `.md` s'affiche immédiatement.

## Générer les PDF imprimables

Chaque chapitre a 4 PDF dans son dossier `pdf/` : cours, fiches méthode, exercices (énoncés seuls) et exercices corrigés. Ils sont fabriqués automatiquement à partir des pages Markdown :

```
python3 outils/generer_pdf.py                        # tous les chapitres
python3 outils/generer_pdf.py docs/terminale/suites  # un seul chapitre
```

Il faut pandoc et une distribution LaTeX avec xelatex (TeX Live ou MiKTeX). À relancer après chaque modification d'un chapitre. Les blocs `??? success "Correction"` sont retirés de la version « énoncés ».

## Encadrés disponibles

```
!!! definition "Titre"      encadré bleu
!!! theoreme "Titre"        encadré rouge
!!! propriete "Titre"       encadré vert
!!! demo "Titre"            démonstration au programme
!!! tip / warning / note    conseil, piège, remarque
??? success "Correction"    bloc repliable (corrections)
```

Le contenu d'un encadré est décalé de 4 espaces.
