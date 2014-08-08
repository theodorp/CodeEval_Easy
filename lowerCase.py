def lowerCase(filepath):
	
	f = open(filepath, "r")

	for line in f:
		print(line.lower().strip())

	f.close()

lowerCase("lowerCase.txt")