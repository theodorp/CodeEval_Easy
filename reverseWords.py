# REVERSE WORDS
# CHALLENGE DESCRIPTION:


# Write a program to reverse the words of an input sentence.

# INPUT SAMPLE:

# The first argument will be a path to a filename containing multiple sentences, one per line. Possibly empty lines too. E.g.

# Hello World
# Hello CodeEval
# OUTPUT SAMPLE:

# Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print. E.g.

# World Hello
# CodeEval Hello

def reverseWords(filename):
	# f = open(filename, 'r')
	with open(filename, 'r') as f:
		for line in f:#open(filename, 'r'):
			if line:
				print(' '.join(line.split()[::-1]))

	# f.close()

	
print (reverseWords('reverseWords.txt'))