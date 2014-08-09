# SUM OF INTEGERS FROM FILE
# CHALLENGE DESCRIPTION:

# Print out the sum of integers read from a file.

# INPUT SAMPLE:

# The first argument to the program will be a path to a filename containing a positive integer, one per line. E.g.

# 5
# 12
# OUTPUT SAMPLE:

# Print out the sum of all the integers read from the file. E.g.

# 17

def sumOfIntFromFile(filepath):

	f = open(filepath, "r")
	tot = 0 
	for line in f:
		t = line.strip('\n')
		tot = tot + int(t)
	print (tot)

	f.close()

sumOfIntFromFile("sumOfIntFromFile.txt")