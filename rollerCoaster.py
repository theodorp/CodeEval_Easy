# ROLLER COASTER
# CHALLENGE DESCRIPTION:


# You are given a text. Your job is to write a program to set the case of text characters based on the following:

# First letter of the line should be upper case.
# Next letter should be lower case.
# Next letter should be upper case and so on...
# Any characters, except the letters, are ignored during determination of letters case.
# INPUT SAMPLE:

# The first argument will be a path to a filename containing sentences, one per line. You can assume all characters are from the english language. E.g.:

# To be, or not to be:" that is the question.
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles,
# And by opposing end them? To die: to sleep.
# OUTPUT SAMPLE:

# Print to stdout, the RoLlErCoAsTeR case version of the string. E.g.:

# To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
# WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR
# ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE,
# Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS,
# AnD bY oPpOsInG eNd ThEm? To DiE: tO sLeEp.


def rollerCoaster(filepath):
	
	file = open(filepath, "r")

	for line in file:
		line = line.strip()
		n = 0
		new = ''
		for letter in line:
			if str.isalpha(letter) == True:
				n += 1
				if n % 2 != 0:
					new += letter.upper()
				else:
					new += letter.lower()
				
			else:
				new += letter

		print(new)

rollerCoaster("rollerCoaster.txt")