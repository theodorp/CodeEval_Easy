# SWAP CASE
# CHALLENGE DESCRIPTION:


# Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following

# Hello world!
# JavaScript language 1.8
# A letter
# OUTPUT SAMPLE:

# Print results in the following way.

# hELLO WORLD!
# jAVAsCRIPT LANGUAGE 1.8
# a LETTER

def swapCase(filename):
	f = open(filename,'r')

	for test in f:
		test = test.strip()
		t2 = ''.join([i.lower() if i.isupper() else i.upper() for i in test])
		
		print(t2)

	f.close()	

swapCase('swapCase.txt')