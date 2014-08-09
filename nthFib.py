# FIBONACCI SERIES
# CHALLENGE DESCRIPTION:


# The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1. Given a positive integer 'n', print out the F(n).

# INPUT SAMPLE:

# The first argument will be a path to a filename containing a positive integer, one per line. E.g.

# 5
# 12
# OUTPUT SAMPLE:

# Print to stdout, the fibonacci number, F(n). E.g.

# 5
# 144

	
def nthFib(filepath):

	f = open(filepath, "r")

	for line in f:
		line = line.strip('\n')
		a, i, b = 0, 0, 1
		while i < int(line):
			i = i + 1		
			a, b = b, a+b
		print(a)		
	f.close()

nthFib("nthFib.txt")
