# WORD TO DIGIT
# CHALLENGE DESCRIPTION:


# Having a string representation of a set of numbers you need to print this numbers.

# All numbers are separated by semicolon. There are up to 20 numbers in one line. The numbers are "zero" to "nine"

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Each line in this file is one test case. E.g.

# zero;two;five;seven;eight;four
# three;seven;eight;nine;two
# OUTPUT SAMPLE:

# Print numbers in the following way:

# 025784
# 37892

def wordToDigit(filename):
	f = open(filename, 'r')
	
	for test in f:
		new = []
		test = test.strip().split(';')
		for i in test:
			if i == "zero":
				i = "0"
				new.append(i)
			elif i == "one":
				i = "1"
				new.append(i)
			elif i == "two":
				i = "2"
				new.append(i)
			elif i == "three":
				i = "3"
				new.append(i)
			elif i == "four":
				i = "4"
				new.append(i)
			elif i == "five":
				i = "5"
				new.append(i)
			elif i == "six":
				i = "6"
				new.append(i)
			elif i == "seven":
				i = "7"
				new.append(i)
			elif i == "eight":
				i = "8"
				new.append(i)
			elif i == "nine":
				i = "9"
				new.append(i)
			
		print(''.join(new))

	f.close()

	
wordToDigit('wordToDigit.txt')