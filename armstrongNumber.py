def armstrongNumber(filename):
	f = open(filename, 'r')

	for test in f:
		test = test.strip()
		temp = 0 
		for i in test:
			temp += int(i)**len(test)
		if temp == int(test):
			print("True")
		else:
			print("False")
		# print(test)

armstrongNumber('armstrongNumber.txt')