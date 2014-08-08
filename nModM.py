def nModM(filename):
	f = open(filename, 'r')

	for test in f:
		test = test.split(',')
		t1,t2 = [int(i) for i in test]
		ans = divmod(t1, t2)
		print(ans[1])

nModM('nModM.txt')