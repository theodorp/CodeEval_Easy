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