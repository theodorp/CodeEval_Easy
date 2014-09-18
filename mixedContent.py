# MIXED CONTENT
# CHALLENGE DESCRIPTION:
# You have a string of words and digits divided by comma. Write a program
# which separates words with digits. You shouldn't change the order elements.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Input
# example is the following

# 8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
# 24,13,14,43,41

# OUTPUT SAMPLE:

# melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
# 24,13,14,43,41

def mixedContent(test):

	line = test.strip().split(',')

	numbers = []
	words = []


	for i in line:
		try:
			numbers.append(int(i))
		except ValueError:
			words.append(i)
			pass

	return(words, numbers)


test_cases = open('mixedContent.txt','r')

for test in test_cases:

	words, numbers = mixedContent(test)

	if len(words) and len(numbers) > 0:
		print(','.join(words) + "|" + ','.join(map(str, numbers)))

	elif len(words) == 0:
		print(','.join(map(str, numbers)))

	elif len(numbers) == 0:
		print(','.join(words))

test_cases.close()