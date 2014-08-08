def longestWord(filename):
	f = open(filename,'r')

	for test in f:
		# test = test.split()
		maxLength = 0
		maxWord = []
		for word in test.split():
			if len(word) > maxLength:
				maxLength = len(word)
				maxWord = [word]
		print(''.join(maxWord))


	f.close()	

longestWord('longestWord.txt')