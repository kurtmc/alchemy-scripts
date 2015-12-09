#!/bin/bash

DATE=$(date -u +"%Y-%m-%d_%H-%M-%S")

tar czf "$1_$DATE.tar.gz" $1
