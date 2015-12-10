#!/bin/bash

find /home/kurt/alchemy-workspace/Product_Information/ -iname "*.pdf" | \
	awk -F/ '{ printf "%s\t%s\n", $6, $7 }' | \
	grep -ve "PDS -" -ve "SDS -"
