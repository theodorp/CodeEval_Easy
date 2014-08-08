	
def nthFib(filepath):

	f = open(filepath, "r")

	for line in f:
		line = line.strip('\n')
		a, i, b = 0, 0, 1
		while i < int(line):
			i = i + 1		
			a, b = b, a+b
		print(a)		
	f.close()

nthFib("nthFib.txt")
