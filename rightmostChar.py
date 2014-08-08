def rightmostChar(filename):
	f = open(filename, 'r')
	i = 0 
	for test in f:
		t1,t2 = test.rstrip().split(',')

		print(t1.rfind(t2))


rightmostChar('rightmostChar.txt')