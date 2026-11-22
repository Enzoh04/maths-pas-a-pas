// Rendu des formules (KaTeX) au chargement de chaque page,
// y compris avec la navigation instantanée de Material.
function renderMaths() {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    throwOnError: false
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(renderMaths);
} else {
  document.addEventListener("DOMContentLoaded", renderMaths);
}
