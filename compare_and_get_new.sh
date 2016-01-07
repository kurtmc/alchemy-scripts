#!/bin/bash

# usage: ./compare_and_get_new.sh old_dir new_dir out_dir
function useage {
	echo "usage: ./compare_and_get_new.sh old_dir new_dir out_dir"
	exit 1
}

OLD_DIR=$1
NEW_DIR=$2
OUTPUT=$3

if [ -z "$OLD_DIR" ]; then
	useage
fi
if [ -z "$NEW_DIR" ]; then
	useage
fi
if [ -z "$OUTPUT" ]; then
	useage
fi


mkdir $OUTPUT

diff --brief $OLD_DIR $NEW_DIR | grep ^"Only in $NEW_DIR" | awk -F': ' '{ print $2 }' | while read f; do
cp "$NEW_DIR/$f" $OUTPUT
done

diff --brief $OLD_DIR $NEW_DIR | grep ^Files | sed 's/ differ//' | awk -F' and ' '{ print $2 }' | while read f; do
cp "$f" $OUTPUT
done
