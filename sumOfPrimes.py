# SUM OF PRIMES
# CHALLENGE DESCRIPTION:

# Write a program to determine the sum of the first 1000 prime numbers.

# INPUT SAMPLE:

# There is no input for this program.

# OUTPUT SAMPLE:

# Your program should print the sum on stdout, i.e.

# 3682913

def sumOfPrimes(n):
	primes = []
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.append(i)
			multiples.update(range(i*i, n+1, i))
	print(sum(primes))


sumOfPrimes(7920)