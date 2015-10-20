#!/usr/bin/python
import sys
import re

if (len(sys.argv) >= 2): n = int(sys.argv[1])
else: n = 3

while 1:
	try:
		line = raw_input().split()
		m = n
		ngram = []
		for word in range(len(line)):
			if len(line[word:m]) == n:
				ngram.append(line[word:m])
			m = m+1
		if ngram != []: print ngram
	except:
		break
	pass