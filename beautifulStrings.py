def beautifulStrings(filename):
	f = open(filename,'r')

	for test in f:
		import re
		from collections import Counter
		allowed = '[A-Za-z]'
		test = ''.join(re.findall(allowed, test.lower()))
		count = Counter(c for c in test)

		k, total = 26, 0
		for c in sorted(count.values(), reverse = True):
			total += k*c
			k -= 1

		print(total)

	f.close()	

beautifulStrings('beautifulStrings.txt')