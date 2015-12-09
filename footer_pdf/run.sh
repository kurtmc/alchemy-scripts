#!/bin/bash

FILENAME=$1
TMP_DIR=tmp_dir

rm -r $TMP_DIR
mkdir -p $TMP_DIR


cp $FILENAME $TMP_DIR/
pdfseparate $TMP_DIR/$FILENAME $TMP_DIR/tmp_%d.pdf

FIRST=$(echo $TMP_DIR/tmp_1.pdf | sed -e 's/[\/&]/\\&/g')

cat footer.tex | sed "s/%%FILENAME%%/$FIRST/" | pdflatex &>/dev/null && rm texput.log texput.aux

rm $TMP_DIR/$FILENAME
mv texput.pdf $TMP_DIR/tmp_1.pdf

pdfunite $TMP_DIR/tmp_* $TMP_DIR/$FILENAME.new

NOEXT="${FILENAME%.*}"

cp "$TMP_DIR/$FILENAME.new" "${NOEXT}_foot.pdf"
