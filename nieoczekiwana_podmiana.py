#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

# searching element to change
def get_value_from_dict(search_word):
	for changed_word, item in dictionary.items():
		if item == search_word: return (changed_word)
	pass

while 1:
	# inputs
	rows=open(sys.argv[1]).readlines()
	input_string = input()
	input_list = input_string.split(" ")

	# make dictionary from file
	dictionary = {}
	for row in rows:
		row = row.split("	")
		key = row[1].replace("\n", "")
		value = row[0].replace("\n", "")
		dictionary.update({key: value})

	# make output
	output = ""
	for element in input_list:
		a = get_value_from_dict(element)
		if (a != None): output += a
		else: output += element
		output += " "
	output = output[:-1]

	print (output)
	pass