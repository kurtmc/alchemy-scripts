#!/bin/bash

FILENAME=$1
TMP_DIR=tmp_dir
OUTPUT_DIR=output
BASENAME=$(basename "$FILENAME")

rm -rf $TMP_DIR
mkdir -p $TMP_DIR
mkdir -p $OUTPUT_DIR


cp "$FILENAME" "$TMP_DIR/"

pdfseparate "$TMP_DIR/$BASENAME" "$TMP_DIR/tmp_%d.pdf"

FIRST=$(echo $TMP_DIR/tmp_1.pdf | sed -e 's/[\/&]/\\&/g')

cat footer.tex | sed "s/%%FILENAME%%/$FIRST/" | pdflatex &>/dev/null && rm texput.log texput.aux

rm "$TMP_DIR/$BASENAME"
mv texput.pdf $TMP_DIR/tmp_1.pdf

pdfunite $TMP_DIR/tmp_* "$TMP_DIR/$BASENAME.new"

NOEXT="${FILENAME%.*}"

mv "$TMP_DIR/$BASENAME.new" "${OUTPUT_DIR}/${BASENAME}"
