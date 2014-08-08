def sumOfDigits(filepath):
	
	f = open(filepath, "r")

	for line in f:
		t = line.strip('\n')
		tot = [int(t[i]) for i in range(0,len(t))]
		print (sum(tot))

	f.close()

sumOfDigits("sumOfDigits.txt")