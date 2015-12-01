#!/usr/bin/python3
import re
import json
import sys
from pprint import pprint
name = input('Podaj nazwisko\n')

with open(sys.argv[1]) as data_file:   
    ends = json.load(data_file)

with open(sys.argv[2]) as data_file:
	asset = json.load(data_file)

classes = asset[0]
codes = asset[1][0]
cases = ['mianownik', 'dopelniacz', 'celownik', 'biernik', 'nadrzednik', 'miejscownik', 'wolacz']

def getClassOfName(name):
	for number in range(0,len(classes)):
		table_of_ends = classes[number] #from current class
		
		for i in range(0,len(table_of_ends)):
			
			regex = re.escape(table_of_ends[i]) + r'$'
			check_name = re.search(regex, name)

			if(check_name != None):
				test_properties = {
					"match": [check_name.group(), {"input":name}],
					"class_number": number
				}
				return test_properties
			pass
		pass
	pass

def showVariants(name_from_user):
	record = getClassOfName(name_from_user)
	name_class = ends[record["class_number"]]
	name = record["match"][1]["input"]

	for prop in range(0,len(cases)):
		CASE = name_class[cases[prop]]
		end = record["match"][0]
		theme = codes[end]
		core_name = name[0:name.rfind(end)]+theme
		print('\n')
		print(cases[prop])
		for i in range(0,len(CASE)):
			print(core_name + CASE[i])
			pass
	pass

showVariants(name);