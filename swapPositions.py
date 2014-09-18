# SWAP ELEMENTS
# CHALLENGE DESCRIPTION:
# You are given a list of numbers which is supplemented with positions that
# have to be swapped.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Input
# example is the following

# 1 2 3 4 5 6 7 8 9 : 0-8
# 1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

# As you can see a colon separates numbers with positions. 
# Positions start with 0. 
# You have to process positions left to right. In the example above (2nd line)
# first you process 0-1, then 1-3.

# OUTPUT SAMPLE:
# Print the lists in the following way.

# 9 2 3 4 5 6 7 8 1
# 2 4 3 1 5 6 7 8 9 10

def swapPositions(test):
	list_ints, list_swaps = test.strip().split(': ')
	
	list_ints = [int(i) for i in list_ints.split()]
	
	list_swaps = list_swaps.replace('-', ' ').replace(', ', ' ').split()
	list_swaps = [int(i) for i in list_swaps]
	
	for i in range(0, len(list_swaps), 2):
		list_ints[list_swaps[i]], list_ints[list_swaps[i+1]] = list_ints[list_swaps[i+1]], list_ints[list_swaps[i]]

	return(list_ints)


test_cases = open('swapPositions.txt','r')

for test in test_cases:
	print(' '.join(list(map(str, swapPositions(test)))))

test_cases.close()