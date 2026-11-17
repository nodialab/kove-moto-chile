#!/bin/bash
# Build + commit + push main + publica site/ en GitHub Pages (rama gh-pages).
# Uso: ./deploy.sh "mensaje del commit"
set -e
cd "$(dirname "$0")"
python3 -I build/build.py
touch site/.nojekyll
git add -A
git diff --cached --quiet || git commit -qm "${1:-Actualización del sitio}"
git push -q origin main
git branch -D gh-pages 2>/dev/null || true
git subtree split --prefix=site -b gh-pages >/dev/null
git push -q -f origin gh-pages
echo "Publicado: https://nodialab.github.io/kove-moto-chile/ (tarda 1-2 min)"
