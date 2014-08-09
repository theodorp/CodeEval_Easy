# N MOD M
# CHALLENGE DESCRIPTION:


# Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

# 20,6
# 2,3
# You may assume M will never be zero.



def nModM(filename):
	f = open(filename, 'r')

	for test in f:
		test = test.split(',')
		t1,t2 = [int(i) for i in test]
		ans = divmod(t1, t2)
		print(ans[1])

nModM('nModM.txt')