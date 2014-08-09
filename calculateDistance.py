# CALCULATE DISTANCE
# CHALLENGE DESCRIPTION:


# You have coordinates of 2 points and need to find the distance between them.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following


# (25, 4) (1, -6)
# (47, 43) (-25, -11)
# All numbers in input are integers between -100 and 100.

# OUTPUT SAMPLE:

# Print results in the following way.


# 26
# 90
# You don't need to round the results you receive. 
# They must be integer numbers between -100 and 100.

def calculateDistance(filename):
	f = open(filename,'r')
	for test in f:
		from re import match
		from math import sqrt
		# test = [int(i) for i in test.strip().split()]
		x1, y1, x2, y2 = map(int, match(r"\((.*), (.*)\) \((.*), (.*)\)", test).groups())
		# print(x1, y1, x2, y2)
		print(int(sqrt((x1-x2)**2+(y1-y2)**2)))

calculateDistance('calculateDistance.txt')