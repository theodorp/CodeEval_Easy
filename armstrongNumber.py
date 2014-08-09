# ARMSTRONG NUMBERS
# CHALLENGE DESCRIPTION:


# An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Each line in this file has a positive integer. E.g.

# 6
# 153
# 351
# OUTPUT SAMPLE:

# Print out True/False if the number is an Armstrong number or not. E.g.

# True
# True
# False


def armstrongNumber(filename):
	f = open(filename, 'r')

	for test in f:
		test = test.strip()
		temp = 0 
		for i in test:
			temp += int(i)**len(test)
		if temp == int(test):
			print("True")
		else:
			print("False")
		# print(test)

armstrongNumber('armstrongNumber.txt')