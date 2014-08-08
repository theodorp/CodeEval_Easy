def capitalizeWords(filename):
	with open(filename, 'r') as f:
		for test in f:
			test = test.split()
			# word = [word.capitalize() for word in test]
			print(' '.join([word[0].upper() + word[1:] for word in test]))
			# for word in test:
				# word = test.capwords(test,sep=' ')
			# print(word)
			# print(word)

capitalizeWords('capitalizeWords.txt')
