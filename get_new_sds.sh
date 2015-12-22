#!/bin/bash
OLD_DIR=SDS-copy
NEW_DIR=SDS-copy2
OUTPUT=new_sds

mkdir $OUTPUT

diff --brief $OLD_DIR $NEW_DIR | grep ^"Only in $NEW_DIR" | awk -F': ' '{ print $2 }' | while read f; do
cp "$NEW_DIR/$f" ./new_sds
done

diff --brief $OLD_DIR $NEW_DIR | grep ^Files | sed 's/ differ//' | awk -F' and ' '{ print $2 }' | while read f; do
cp "$f" ./new_sds
done
