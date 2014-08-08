def happy(n):
	past = set()			
	while n != 1:
		n = sum(int(i)**2 for i in str(n))
		if n in past:
			return (0)
		past.add(n)
	return (1)

def happyNumbers(filename):

	f = open(filename, 'r')

	for test in f:
		t = test.strip()
		print(happy(int(t)))


# print(happy(7))

happyNumbers('happyNumbers.txt')
