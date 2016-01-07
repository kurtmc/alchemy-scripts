#!/bin/bash

# usage ./get_new old_dir new_dir out_dir

OLD_DIR=$1
NEW_DIR=$2
OUTPUT=$3

mkdir $OUTPUT

diff --brief $OLD_DIR $NEW_DIR | grep ^"Only in $NEW_DIR" | awk -F': ' '{ print $2 }' | while read f; do
cp "$NEW_DIR/$f" ./new_sds
done

diff --brief $OLD_DIR $NEW_DIR | grep ^Files | sed 's/ differ//' | awk -F' and ' '{ print $2 }' | while read f; do
cp "$f" ./new_sds
done
