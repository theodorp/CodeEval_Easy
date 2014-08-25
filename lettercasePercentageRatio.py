# LETTERCASE PERCENTAGE RATIO
# CHALLENGE DESCRIPTION:


# Your goal is to find the percentage ratio of lowercase and uppercase letters in line below.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Each line of input contains a string with uppercase and lowercase letters E.g.:

# thisTHIS
# AAbbCCDDEE
# N
# UkJ

# OUTPUT SAMPLE:

# For each line from input, print the percentage ratio of uppercase and lowercase letters rounded to the second digit after the dot. E.g.:

# lowercase: 50.00 uppercase: 50.00
# lowercase: 20.00 uppercase: 80.00
# lowercase: 0.00 uppercase: 100.00
# lowercase: 33.33 uppercase: 66.67

# def lettercasePercentageRatio(filepath):
# 	file = open(filepath, "r")

# 	for test in file:
# 		line = test.strip()

# 		countL = 0
# 		countU = 0
# 		for char in line:
# 			if char.isupper() == True:
# 				countU += 1
# 			else:
# 				countL += 1

# 		print("lowercase:", "%.2f" % (countL/len(line)*100), "uppercase:", "%.2f" % (countU/len(line)*100))

# lettercasePercentageRatio("lettercasePercentageRatio.txt")

# def tester(filepath):
def lettercasePercentageRatio(test):
	line = test.strip()
	countL = 0
	countU = 0
	for char in line:
		if char.isupper() == True:
			countU += 1
		else:
			countL += 1

	return("lowercase:", "%.2f" % (countL/len(line)*100), "uppercase:", "%.2f" % (countU/len(line)*100))

file = open("lettercasePercentageRatio.txt", "r")

for test in file:
	print(' '.join(lettercasePercentageRatio(test)))

# lettercasePercentageRatio("lettercasePercentageRatio.txt")