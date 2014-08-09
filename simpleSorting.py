# SIMPLE SORTING
# CHALLENGE DESCRIPTION:


# Write a program which sorts numbers.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following

# 70.920 -38.797 14.354 99.323 90.374 7.581
# -37.507 -3.263 40.079 27.999 65.213 -55.552
# OUTPUT SAMPLE:

# Print sorted numbers in the following way.

# -38.797 7.581 14.354 70.920 90.374 99.323
# -55.552 -37.507 -3.263 27.999 40.079 65.213

def simpleSorting(filename):
	f = open(filename,'r')

	for test in f:
		# test = sorted([float(i) for i in test.strip().split()], key=int)
		# print(' '.join(map(lambda f: "%.3f" % (f,),test)))
		print (" ".join(map(lambda f: "%.3f" % (f,), sorted(map(float, test.strip().split())))))

simpleSorting('simpleSorting.txt')