import sys

def redact(sourceFile):
	redactedOutFile = open(sourceFile+'.redac', 'w')
	# TODO - open an audit file to append activity log per redact()
	with open(sourceFile) as inputFile:
		for line in inputFile:
			if ('CC=' not in line) and ('SSN=' not in line):
				redactedOutFile.write(line)

	redactedOutFile.close()
	inputFile.close()

if __name__ == '__main__':
	redact(sys.argv[1])
