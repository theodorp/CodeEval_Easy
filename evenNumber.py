def evenNumber(filepath):
	
	f = open(filepath, "r")

	for line in f:
		if int(line) % 2 == 0:
			print (1)
		else:
			print(0)

	f.close()

evenNumber("evenNumber.txt")