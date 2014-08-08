def simpleSorting(filename):
	f = open(filename,'r')

	for test in f:
		# test = sorted([float(i) for i in test.strip().split()], key=int)
		# print(' '.join(map(lambda f: "%.3f" % (f,),test)))
		print (" ".join(map(lambda f: "%.3f" % (f,), sorted(map(float, test.strip().split())))))

simpleSorting('simpleSorting.txt')