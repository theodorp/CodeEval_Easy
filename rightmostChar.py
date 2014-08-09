# RIGHTMOST CHAR
# CHALLENGE DESCRIPTION:

# You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. The position to be printed out is zero based.

# INPUT SAMPLE:

# The first argument will ba a path to a filename, containing a string and a character, comma delimited, one per line. Ignore all empty lines in the input file. E.g. 
# Hello World,r
# Hello CodeEval,E
# OUTPUT SAMPLE:

# Print out the zero based position of the character 't' in string 'S', one per line. Do NOT print out empty lines between your output. 
# E.g.

# 8
# 10

def rightmostChar(filename):
	f = open(filename, 'r')
	i = 0 
	for test in f:
		t1,t2 = test.rstrip().split(',')

		print(t1.rfind(t2))


rightmostChar('rightmostChar.txt')