#!/usr/bin/python3
import re

name = input('Podaj nazwisko\n')

classes = [["ski", "cki", "dzki"],	["ak", "ik", "yk"],	["ek"],	["ny"],	["ka"],	["owicz", "ewicz", "ach", "ól", "arz"],	["ur"],	["el"],	["ra"],	["an", "ąb"], ["oł", "eł", "ieł"], ["ia"], ["ień"], ["leń"]]

codes = {	"ski": "s",	"cki": "c",	"dzki": "dz", "ak": "ak", "ik": "ik", "yk": "yk", "ek": "",
	"ny": "n", "ka": "", "owicz": "owicz", "ewicz": "ewicz", "ach": "ach", "ól": "ól",
	"arz": "arz", "ur": "ur", "el": "", "ra": "r", "an": "an", "ąb": "ąb", "oł": "o",
	"eł": "", "ieł": "ie", "ia": "i", "ień": "", "leń": "le"	}
cases = ['mianownik', 'dopelniacz', 'celownik', 'biernik', 'nadrzednik', 'miejscownik', 'wolacz']

ends = [
	{ #klasa 1
		"mianownik": ['ki', 'cy', 'ka', 'kie'],
		"dopelniacz": ['kiego', 'kich', 'kiej', 'kich'],
		"celownik": ['kiemu', 'kim', 'kiej', 'kim'],
		"biernik": ['kiego', 'kich', 'ką', 'kich'],
		"nadrzednik": ['kim', 'kimi', 'ką', 'kimi'],
		"miejscownik": ['kim', 'kich', 'kiej', 'kich'],
		"wolacz": ['ki', 'cy', 'ka', 'kie']
	},
	{ #klasa 2
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['iem', 'ami', ''],
		"miejscownik": ['u', 'ach', ''],
		"wolacz": ['u', 'owie', '']
	},
	{ #klasa 3
		"mianownik": ['ek', 'kowie', 'ek'],
		"dopelniacz": ['ka', 'ków', 'ek'],
		"celownik": ['kowi', 'kom', 'ek'],
		"biernik": ['ka', 'ków', 'ek'],
		"nadrzednik": ['kiem', 'kami', 'ek'],
		"miejscownik": ['ku', 'kach', 'ek'],
		"wolacz": ['ku', 'kowie', 'ek']
	},
	{ #klasa 4
		"mianownik": ['y', 'i', 'a'],
		"dopelniacz": ['ego', 'ych', 'ej'],
		"celownik": ['emu', 'ym', 'ej'],
		"biernik": ['ego', 'ych', 'ą'],
		"nadrzednik": ['ym', 'ymi', 'ą'],
		"miejscownik": ['ym', 'ych', 'ej'],
		"wolacz": ['y', 'i', 'a']
	},
	{ #klasa 5
		"mianownik": ['ka', 'kowie', 'ka'],
		"dopelniacz": ['ki', 'ków', 'ki'],
		"celownik": ['ce', 'kom', 'ce'],
		"biernik": ['kę', 'ków', 'kę'],
		"nadrzednik": ['ką', 'kami', 'ką'],
		"miejscownik": ['ce', 'kach', 'ce'],
		"wolacz": ['ka', 'kowie', 'ka']
	},
	{ #klasa 6
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['u', 'ach', ''],
		"wolacz": ['u', 'owie', '']
	},
	{ #klasa 7
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['ze', 'ach', ''],
		"wolacz": ['ze', 'owie', '']
	},
	{ #klasa 8
		"mianownik": ['el', 'lowie', 'el'],
		"dopelniacz": ['la', 'lów', 'el'],
		"celownik": ['owi', 'lom', 'el'],
		"biernik": ['a', 'lów', 'el'],
		"nadrzednik": ['em', 'lami', 'el'],
		"miejscownik": ['lu', 'lach', 'el'],
		"wolacz": ['lu', 'lowie', 'el']
	},
	{ #klasa 9
		"mianownik": ['a', 'owie', 'a'],
		"dopelniacz": ['y', 'ów', 'y'],
		"celownik": ['ze', 'om', 'ze'],
		"biernik": ['ę', 'ów', 'ę'],
		"nadrzednik": ['ą', 'ami', 'ą'],
		"miejscownik": ['ze', 'ach', 'ze'],
		"wolacz": ['o', 'owie', 'o']
	},
	{ #klasa 10
		"mianownik": ['', 'owie', ''],
		"dopelniacz": ['a', 'ów', ''],
		"celownik": ['owi', 'om', ''],
		"biernik": ['a', 'ów', ''],
		"nadrzednik": ['em', 'ami', ''],
		"miejscownik": ['ie', 'ach', ''],
		"wolacz": ['ie', 'owie', '']
	},
	{ #klasa 11
		"mianownik": ['ł', 'łowie', 'ł'],
		"dopelniacz": ['ła', 'łów', 'ł'],
		"celownik": ['łowi', 'łom', 'ł'],
		"biernik": ['ła', 'łów', 'ł'],
		"nadrzednik": ['łem', 'łami', 'ł'],
		"miejscownik": ['le', 'łach', 'ł'],
		"wolacz": ['le', 'łowie', 'ł']
	},
	{ #klasa 12
		"mianownik": ['a', 'owie', 'a'],
		"dopelniacz": ['', 'ów', ''],
		"celownik": ['', 'om', ''],
		"biernik": ['ę', 'ów', 'ę'],
		"nadrzednik": ['ą', 'ami', 'ą'],
		"miejscownik": ['', 'ach', ''],
		"wolacz": ['o', 'owie', 'o']
	},
	{ #klasa 13
		"mianownik": ['ień', 'iowie', 'ień'],
		"dopelniacz": ['nia', 'niów', 'ień'],
		"celownik": ['niowi', 'niom', 'ień'],
		"biernik": ['nia', 'niów', 'ień'],
		"nadrzednik": ['niem', 'niami', 'ień'],
		"miejscownik": ['niu', 'niach', 'ień'],
		"wolacz": ['niu', 'niowie', 'ień']	
	},
	{ #klasa 14
		"mianownik": ['ń', 'niowie', 'ń'],
		"dopelniacz": ['nia', 'niów', 'ń'],
		"celownik": ['niowi', 'niom', 'ń'],
		"biernik": ['nia', 'niów', 'ń'],
		"nadrzednik": ['niem', 'niami', 'ń'],
		"miejscownik": ['niu', 'niach', 'ń'],
		"wolacz": ['niu', 'niowie', 'ń']	
	}
]

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