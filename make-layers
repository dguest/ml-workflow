#!/usr/bin/env bash

set -eu

cd $(dirname $0)
BASEDIR=basefigs
FIG=figures
BASE=$BASEDIR/workflow.svg

./make-layered.py $BASE

for f in $PWD/$FIG/*.svg; do
    OUT=${f%.svg}.pdf
    echo "converting $f to $OUT"
    inkscape --without-gui --export-pdf=$OUT $f
done

