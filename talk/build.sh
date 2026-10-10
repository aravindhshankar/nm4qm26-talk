#!/bin/bash
# Build the talk and open the PDF.   ./build.sh
# Live preview, rebuilds on save:    ./build.sh -w   (Ctrl-C to stop)
cd "$(dirname "$0")" || exit 1
if [ "$1" = "-w" ]; then
  exec latexmk -pdf -pvc -interaction=nonstopmode nm4qm_talk.tex
fi
latexmk -pdf -interaction=nonstopmode -halt-on-error nm4qm_talk.tex || {
  echo "BUILD FAILED: see nm4qm_talk.log (search for lines starting with '!')"; exit 1; }
latexmk -c >/dev/null 2>&1; rm -f nm4qm_talk.nav nm4qm_talk.snm
open nm4qm_talk.pdf
