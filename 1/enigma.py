#!/usr/bin/python
from collections import OrderedDict
import re
def enigma(string):

	splited = re.sub('( {2,})+', ' ', string).split(" ")
	
	ordered_list = list(OrderedDict.fromkeys(splited))
	output = []

	for element in splited: 
		output.append(ordered_list.index(element))
	print output

while 1: enigma(raw_input())