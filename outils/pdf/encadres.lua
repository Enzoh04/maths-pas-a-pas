-- Transforme les blocs ::: {.type titre="..."} en encadrés LaTeX colorés.
local couleurs = {
  definition = "cdef", theoreme = "cthm", propriete = "cprop", demo = "cdemo",
  tip = "ctip", warning = "cwarn", success = "cok", note = "cinfo",
  info = "cinfo", abstract = "cinfo", consigne = "cinfo",
  demoplus = "cdemoplus", admis = "cadmis", lecture = "cinfo"
}

function Div(el)
  for _, cls in ipairs(el.classes) do
    local c = couleurs[cls]
    if c then
      local titre = el.attributes["titre"] or ""
      local debut = pandoc.RawBlock("latex",
        "\\begin{encadre}{" .. c .. "}{" .. titre .. "}")
      local fin = pandoc.RawBlock("latex", "\\end{encadre}")
      local contenu = el.content
      table.insert(contenu, 1, debut)
      table.insert(contenu, fin)
      return contenu
    end
  end
end
