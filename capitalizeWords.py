# CAPITALIZE WORDS
# CHALLENGE DESCRIPTION:


# Write a program which capitalizes the first letter of each word in a sentence.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following


# Hello world
# javaScript language
# a letter
# 1st thing
# OUTPUT SAMPLE:

# Print capitalized words in the following way.


# Hello World
# JavaScript Language
# A Letter
# 1st Thing


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
