# redact.py
# Author: Choong Huh
# Description:
# The program will read each line of the file given by ex.sh script.
# If sensitive information is found, the occurence is recorded in the audit file
# and the offending line is removed.
# Otherwise, the line is written to a new file which serves as the redacted copy.

import sys

def redact(sourceFile):
	redactedOutFile = open(sourceFile+'.redact', 'w')
	auditOutFile = open('auditLog.txt', 'a')
	# TODO - open an audit file to append activity log per redact()
	with open(sourceFile) as inputFile:
		ssi_counter = 0
		for line in inputFile:
			if ('CC=' not in line) and ('SSN=' not in line):
				redactedOutFile.write(line)
			else:
				ssi_counter += 1
		auditOutFile.write('SSI Occurences in {0} : {1}\n'.format(sourceFile, str(ssi_counter)))

	redactedOutFile.close()
	inputFile.close()
	auditOutFile.close()

if __name__ == '__main__':
	# Depends on ex.sh to always give one argument
	redact(sys.argv[1])
