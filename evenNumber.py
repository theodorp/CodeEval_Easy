# EVEN NUMBERS
# CHALLENGE DESCRIPTION:


# Write a program which checks input numbers and determines whether a number is even or not.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following

# 701
# 4123
# 2936
# OUTPUT SAMPLE:

# Print 1 if the number is even or 0 if the number is odd.

# 0
# 0
# 1

def evenNumber(filepath):
	
	f = open(filepath, "r")

	for line in f:
		if int(line) % 2 == 0:
			print (1)
		else:
			print(0)

	f.close()

evenNumber("evenNumber.txt")