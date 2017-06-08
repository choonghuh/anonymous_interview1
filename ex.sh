#!/bin/bash

# ex.sh
# Author: Choong Huh
# Description:
# The program unzips user-provided gzip file, which shall contain one or more 
# text files that contain logging data.
# Redacted copies of the logs are created by redact.py, along with audit.txt
# and the resulting files are compressed back into output.tar.gz

echo "tar unzipping $1"

# Saving tar extraction stdout output to var
var="$( tar -xzvf $1 )"
var2=""
rm -f auditLog.txt
touch auditLog.txt

# Building string var2 to be used in compressing and cleanup
for a in $var; do
	python redact.py $a
	rm $a
	var2="$var2 $a.redact"
done
# echo $var2

tar -czvf output.tar.gz auditLog.txt $var2
rm auditLog.txt $var2
# TODO - Carry over metadata