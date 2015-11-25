#!/usr/bin/python3
import re

def search_word(word, string):

	# pattern = "[^a-zA-Z]*" + word + "[^a-zA-Z]*"
	pattern = word
	match = re.finditer(pattern, string)
	print match.start()

	# for i in match.finditer():
	# 	print i
	# 	pass


	
	pass


std = "ala ma ala kota"
word = "ala"

search_word(word, std)

