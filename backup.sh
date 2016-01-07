#!/bin/bash

DATE=$(date -u +"%Y-%m-%d_%H-%M-%S")

tar cfJ "$1_$DATE.tar.xz" $1
