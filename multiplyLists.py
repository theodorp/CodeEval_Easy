def multiplyLists(filename):
	f = open(filename, 'r')
	for test in f:
		t1,t2 = test.strip().split(' | ')
		t1 = [int(i) for i in t1.split()]
		t2 = [int(j) for j in t2.split()]
		print(' '.join([str(a*b) for a,b in zip(t1,t2)]))
		# test = [int(i) for i in test]
		# for i in len(test):
			# print(i)


multiplyLists('multiplyLists.txt')