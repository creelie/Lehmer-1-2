#!/bin/sh
# Builds the PDF and the arXiv source package of the paper.
#   sh make_arxiv.sh        ->  build/main.pdf  and  lehmer-bound-arxiv.tar.gz  (main.tex and the PNG figures it uses)
# Requires pdflatex.  The figures are exported from their TikZ sources by figures/build.sh.
set -e
cd "$(dirname "$0")"
mkdir -p build
for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex > build/pdflatex.log; done
if grep -q "undefined" build/main.log; then grep "undefined" build/main.log; exit 1; fi
rm -rf build/arxiv && mkdir -p build/arxiv/figures
cp main.tex build/arxiv/
for f in $(grep -o 'figures/[A-Za-z_0-9]*\.png' main.tex | sort -u); do cp "$f" build/arxiv/figures/; done
(cd build/arxiv && for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null; done \
  && rm -f main.aux main.log main.out main.pdf)
tar -C build/arxiv -czf lehmer-bound-arxiv.tar.gz main.tex figures
echo "build/main.pdf, lehmer-bound-arxiv.tar.gz"
