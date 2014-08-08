def sumOfIntFromFile(filepath):

	f = open(filepath, "r")
	tot = 0 
	for line in f:
		t = line.strip('\n')
		tot = tot + int(t)
	print (tot)

	f.close()

sumOfIntFromFile("sumOfIntFromFile.txt")