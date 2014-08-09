# FILE SIZE
# CHALLENGE DESCRIPTION:


# Print the size of a file in bytes.

# INPUT:

# The first argument to your program has the path to the file you need to check the size of.

# OUTPUT SAMPLE:

# Print the size of the file in bytes. E.g.

# 55

def fileSize(filename):
	import sys
	with open(filename, 'r') as f:
		for line in f:
			print(sys.getsizeof(line))

			# print(getsize(line))

fileSize('fileSize.txt')