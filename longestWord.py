# LONGEST WORD
# CHALLENGE DESCRIPTION:

# In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following


# some line with text
# another line
# Each line has one or more words. Each word is separated by space char.

# OUTPUT SAMPLE:

# Print the longest word in the following way.


# some
# another


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