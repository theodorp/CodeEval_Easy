def sumOfPrimes(n):
	primes = []
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.append(i)
			multiples.update(range(i*i, n+1, i))
	print(sum(primes))


sumOfPrimes(7920)