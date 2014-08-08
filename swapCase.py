def swapCase(filename):
	f = open(filename,'r')

	for test in f:
		test = test.strip()
		t2 = ''.join([i.lower() if i.isupper() else i.upper() for i in test])
		
		print(t2)

	f.close()	

swapCase('swapCase.txt')