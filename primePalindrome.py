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