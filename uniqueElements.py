# UNIQUE ELEMENTS
# CHALLENGE DESCRIPTION:


# You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

# INPUT SAMPLE:

# File containing a list of sorted integers, comma delimited, one per line. E.g. 
# 1,1,1,2,2,3,3,4,4
# 2,3,4,5,5
# OUTPUT SAMPLE:

# Print out the sorted list with duplicates removed, one per line. 
# E.g.

# 1,2,3,4
# 2,3,4,5

def uniqueElements(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [int(i) for i in line]
			print(','.join(map(str, list(set(line)))))

(uniqueElements('uniqueElements.txt'))