def fileSize(filename):
	import sys
	with open(filename, 'r') as f:
		for line in f:
			print(sys.getsizeof(line))

			# print(getsize(line))

fileSize('fileSize.txt')