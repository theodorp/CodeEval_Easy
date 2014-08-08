def hexToDecimal(filepath):
	
	f = open(filepath, "r")

	for line in f:
		t = line.strip('\n')
		print(int(t,16))

	f.close()

hexToDecimal("hexToDec.txt")