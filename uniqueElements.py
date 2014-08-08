def uniqueElements(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [int(i) for i in line]
			print(','.join(map(str, list(set(line)))))

(uniqueElements('uniqueElements.txt'))