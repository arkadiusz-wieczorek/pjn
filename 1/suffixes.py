# !/usr/bin/python
def suffixes(string):
	reductions = []
	for x in range(len(string)): 
		reductions.append(string[x:len(string)])
	print reductions

suffixes("banana")