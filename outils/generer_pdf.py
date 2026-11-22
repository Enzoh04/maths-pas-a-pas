#!/usr/bin/env python3
"""Génère les PDF imprimables de chaque chapitre à partir des pages Markdown.

Pour chaque dossier de chapitre (docs/<niveau>/<chapitre>/) contenant
cours.md, methodes.md et/ou exercices.md, crée dans <chapitre>/pdf/ :
  - cours.pdf                (démonstrations au programme du bac seulement)
  - cours-complet.pdf        (toutes les démonstrations)
  - methodes.pdf
  - exercices-enonces.pdf    (sans les corrections)
  - exercices-corriges.pdf   (avec les corrections)
  - bac-enonces.pdf / bac-corriges.pdf (si bac.md existe)

Utilisation (depuis la racine du projet) :
  python3 outils/generer_pdf.py                 # tous les chapitres
  python3 outils/generer_pdf.py docs/terminale/suites

Nécessite pandoc et une distribution LaTeX avec xelatex.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOCS = RACINE / "docs"
OUTILS_PDF = RACINE / "outils" / "pdf"

NIVEAUX = {
    "seconde": "Seconde",
    "premiere": "Première — Spécialité mathématiques",
    "terminale": "Terminale — Spécialité mathématiques",
}

TITRES_PAR_DEFAUT = {
    "tip": "Conseil", "warning": "Attention", "note": "Remarque",
    "info": "Information", "abstract": "À retenir", "success": "Correction",
    "definition": "Définition", "theoreme": "Théorème",
    "propriete": "Propriété", "demo": "Démonstration",
}

RE_ADMONITION = re.compile(r'^(!!!|\?\?\?\+?)\s+(\w+)(?:\s+"([^"]*)")?\s*$')


def convertir_admonitions(lignes, garder_corrections, exclure=()):
    """Remplace les encadrés MkDocs (!!! / ???) par des blocs pandoc ::: ."""
    sortie, i = [], 0
    while i < len(lignes):
        m = RE_ADMONITION.match(lignes[i])
        if not m:
            sortie.append(lignes[i])
            i += 1
            continue
        _, genre, titre = m.groups()
        titre = titre or TITRES_PAR_DEFAUT.get(genre, "")
        i += 1
        bloc = []
        while i < len(lignes) and (lignes[i].strip() == "" or lignes[i].startswith("    ")):
            bloc.append(lignes[i][4:] if lignes[i].startswith("    ") else "")
            i += 1
        while bloc and bloc[-1] == "":
            bloc.pop()
        est_correction = genre == "success" and titre.lower().startswith("correction")
        if (est_correction and not garder_corrections) or genre in exclure:
            continue
        interieur = convertir_admonitions(bloc, garder_corrections, exclure)
        titre_tex = titre.replace('"', "''")
        sortie += ["", f'::: {{.{genre} titre="{titre_tex}"}}', *interieur, ":::", ""]
    return sortie


def preparer(texte, garder_corrections, saut_de_page=False, exclure=()):
    """Adapte le Markdown du site à une version imprimable."""
    lignes = []
    for ligne in texte.splitlines():
        if ".md-button" in ligne:            # boutons de téléchargement
            continue
        if ligne.lstrip().startswith(("Clique sur **Correction**", "Sur le site, ")):
            continue
        if ligne.strip() == "---":            # séparateurs horizontaux
            ligne = "\n\\newpage\n" if saut_de_page else ""
        lignes.append(ligne)
    texte = "\n".join(convertir_admonitions(lignes, garder_corrections, exclure))
    # Étoiles de difficulté (avec ou sans balise <span>)
    texte = re.sub(r'<span class="etoiles">(★+)</span>', r"\1", texte)
    texte = re.sub(r"★+", lambda m: "\\etoiles{" + m.group(0) + "}", texte)
    # Liens internes vers d'autres pages : on garde seulement le texte
    texte = re.sub(r"(?<!!)\[([^\[\]$\n]+)\]\((?!https?:)[^)\s]*\)", r"\1", texte)
    return texte


def bandeau(niveau, chapitre, document):
    return (
        "```{=latex}\n"
        "\\begin{tcolorbox}[enhanced, colback=cprimaire, colframe=cprimaire, "
        "coltext=white, arc=3pt, left=10pt, top=8pt, bottom=8pt]\n"
        f"{{\\small\\sffamily {niveau}}}\\\\[3pt]\n"
        f"{{\\raggedright\\LARGE\\bfseries {chapitre}\\par}}\\vspace{{3pt}}\n"
        f"{{\\large {document}}}\n"
        "\\end{tcolorbox}\n"
        "{\\small\\itshape\\color{cwarn!80!black} Document produit avec l'aide d'une "
        "intelligence artificielle : il peut contenir des erreurs.}\n\n"
        "\\vspace{4pt}\n"
        "```\n"
    )


def produire(source, destination, document, garder_corrections, niveau,
             saut_de_page=False, exclure=()):
    texte = source.read_text(encoding="utf-8")
    m = re.search(r"^# (.+)$", texte, flags=re.M)
    titre_h1 = m.group(1) if m else source.stem
    chapitre = titre_h1.split(" — ", 1)[1] if " — " in titre_h1 else titre_h1
    texte = re.sub(r"^# .+\n", "", texte, count=1, flags=re.M)
    corps = bandeau(niveau, chapitre, document) + preparer(texte, garder_corrections, saut_de_page, exclure)

    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "page.md"
        md.write_text(corps, encoding="utf-8")
        entete = Path(tmp) / "entete.tex"
        entete.write_text(
            (OUTILS_PDF / "entete.tex").read_text(encoding="utf-8")
            + f"\n\\fancyhead[R]{{\\small\\sffamily {chapitre} — {document}}}\n",
            encoding="utf-8")
        commande = [
            "pandoc", str(md), "-o", str(destination),
            "--from", "markdown+tex_math_dollars+pipe_tables+fenced_divs+raw_attribute",
            "--pdf-engine=xelatex",
            "--lua-filter", str(OUTILS_PDF / "encadres.lua"),
            "-H", str(entete),
            "-V", "documentclass=article", "-V", "papersize=a4",
            "-V", "fontsize=11pt", "-V", "geometry:margin=2cm",
            "-V", "geometry:top=2.2cm", "-V", "colorlinks=true",
            "--shift-heading-level-by=-1",
            "--resource-path", str(source.parent),
            "--highlight-style=tango",
        ]
        subprocess.run(commande, check=True)
    print(f"  ✓ {destination.relative_to(RACINE)}")


def traiter_chapitre(dossier):
    dossier = Path(dossier).resolve()
    niveau = NIVEAUX.get(dossier.parent.name, dossier.parent.name.capitalize())
    sortie = dossier / "pdf"
    sortie.mkdir(exist_ok=True)
    print(f"Chapitre : {dossier.relative_to(DOCS)}")
    if (dossier / "cours.md").exists():
        # Version classique : seulement les démonstrations au programme du bac
        produire(dossier / "cours.md", sortie / "cours.pdf", "Cours", True, niveau,
                 exclure=("demoplus", "admis", "lecture"))
        # Version complète : toutes les démonstrations
        produire(dossier / "cours.md", sortie / "cours-complet.pdf",
                 "Cours complet avec démonstrations", True, niveau)
    if (dossier / "methodes.md").exists():
        produire(dossier / "methodes.md", sortie / "methodes.pdf", "Fiches méthode", True, niveau)
    if (dossier / "exercices.md").exists():
        produire(dossier / "exercices.md", sortie / "exercices-enonces.pdf",
                 "Exercices — énoncés", False, niveau)
        produire(dossier / "exercices.md", sortie / "exercices-corriges.pdf",
                 "Exercices — énoncés et corrections", True, niveau)
    if (dossier / "bac.md").exists():
        # En Première, l'examen est l'épreuve anticipée de mathématiques
        examen = {"premiere": "Sujets type épreuve anticipée",
                  "seconde": "Évaluations type"}.get(dossier.parent.name, "Sujets type bac")
        produire(dossier / "bac.md", sortie / "bac-enonces.pdf",
                 f"{examen} — énoncés", False, niveau, saut_de_page=True)
        produire(dossier / "bac.md", sortie / "bac-corriges.pdf",
                 f"{examen} — énoncés et corrections", True, niveau, saut_de_page=True)


if __name__ == "__main__":
    dossiers = sys.argv[1:] or sorted({p.parent for p in DOCS.glob("*/*/cours.md")})
    for d in dossiers:
        traiter_chapitre(d)
