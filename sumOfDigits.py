# SUM OF DIGITS
# CHALLENGE DESCRIPTION:


# Given a positive integer, find the sum of its constituent digits.

# INPUT SAMPLE:

# The first argument will be a path to a filename containing positive integers, one per line. E.g.

# 23
# 496
# OUTPUT SAMPLE:

# Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

# 5
# 19


def sumOfDigits(filepath):
	
	f = open(filepath, "r")

	for line in f:
		t = line.strip('\n')
		tot = [int(t[i]) for i in range(0,len(t))]
		print (sum(tot))

	f.close()

sumOfDigits("sumOfDigits.txt")