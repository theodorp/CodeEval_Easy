def bitPositions(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [bin(int(i))[2:] for i in line]

			if line[0][::-1][int(line[1],2)-1] == line[0][::-1][int(line[2],2)-1]:
				print("true")
			else:
				print("false")
			

bitPositions('bitPositions.txt')
