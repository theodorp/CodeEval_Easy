# Write a program to determine the biggest prime palindrome under 1000.

# INPUT SAMPLE:

# There is no input for this program.

# OUTPUT SAMPLE:

# Your program should print the largest palindrome on stdout, i.e.

# 929

def primePalindrome():
	n = 1000
	multiples = set()
	max = 0
	for i in range(2, n+1):
		if i not in multiples:
			multiples.update(range(i*i, n+1, i))
			if str(i) == str(i)[::-1] and i > max:
				max = i
	print(max)

				 

primePalindrome()