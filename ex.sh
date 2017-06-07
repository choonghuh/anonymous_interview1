#!/bin/bash

echo "tar unzipping $1"
var="$( tar -xzvf $1 )"

for a in $var; do
	python redact.py $a
done
