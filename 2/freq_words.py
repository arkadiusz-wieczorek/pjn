#!/usr/bin/python
from collections import Counter
import sys
import re

words = []

while 1:
	try:
		std = re.sub('([:,.;"`"?!()])*', '', raw_input()).lower().split()
		words += std
	except:
		break
	pass

counter = Counter()

for word in words:	counter[word] += 1
for word in counter.most_common():	print word[1],"	",word[0]