def setIntersection(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip().split(';')
			line = [i.split(',') for i in line]
			inter = list(set(line[0]).intersection(set(line[1])))
			inter.sort()
			print (','.join(inter))

setIntersection('setIntersection.txt')