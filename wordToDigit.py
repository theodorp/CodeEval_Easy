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