#!/usr/bin/env bash

set -eu

HERE=$(dirname $0)
BASEDIR=basefigs
FIG=figures
BASE=$BASEDIR/workflow.svg

$HERE/make-layered.py $BASE

for f in $FIG/*.svg; do
    OUT=${f%.svg}.pdf
    echo "converting $f to $OUT"
    inkscape --without-gui --export-pdf=$OUT $f
done

