# MULTIPLES OF A NUMBER
# CHALLENGE DESCRIPTION:


# Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

# INPUT SAMPLE:

# The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.

# 13,8
# 17,16
# OUTPUT SAMPLE:

# Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

# 16
# 32

def multiplesOfNumber(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [int(i) for i in line]
			temp = line[1]
			while line[1] < line[0]:
				line[1] = line[1] + temp
			print(line[1])			
multiplesOfNumber('multiplesOfNumber.txt')