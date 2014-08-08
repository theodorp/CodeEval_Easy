def reverseWords(filename):
	# f = open(filename, 'r')
	with open(filename, 'r') as f:
		for line in f:#open(filename, 'r'):
			if line:
				print(' '.join(line.split()[::-1]))

	# f.close()

	
print (reverseWords('reverseWords.txt'))