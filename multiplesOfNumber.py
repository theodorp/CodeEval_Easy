def multiplesOfNumber(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [int(i) for i in line]
			temp = line[1]
			while line[1] < line[0]:
				line[1] = line[1] + temp
			print(line[1])			
multiplesOfNumber('multiplesOfNumber.txt')