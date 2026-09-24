#!/bin/bash
set -euo pipefail

curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz -o lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz

MY_FILE=$(tar -tzf lab3-bundle.tar.gz | grep '\.tsv$')

awk '!/^[[:space:]]*$/' "$MY_FILE" > cleaned.tsv

#use tr to convert tabs to commas
tr '\t' ',' < cleaned.tsv > cleaned.csv

#tail -n +3 to skip the first line (header)
#wc -l to count the number of lines
LINES=$(tail -n +3 cleaned.csv | wc -l)
echo "Remaining data lines: $LINES"

tar -czf converted-archive.tar.gz cleaned.csv