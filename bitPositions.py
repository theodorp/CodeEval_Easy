# BIT POSITIONS
# CHALLENGE DESCRIPTION:


# Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

# INPUT SAMPLE:

# The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.


# 1
# 2
# 86,2,3
# 125,1,2
# OUTPUT SAMPLE:

# Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.


# 1
# 2
# true
# false



def bitPositions(filename):
	with open(filename, 'r') as f:
		for line in f:
			line = line.split(',')
			line = [bin(int(i))[2:] for i in line]

			if line[0][::-1][int(line[1],2)-1] == line[0][::-1][int(line[2],2)-1]:
				print("true")
			else:
				print("false")
			

bitPositions('bitPositions.txt')
