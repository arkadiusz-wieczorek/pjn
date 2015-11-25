#!/usr/bin/python3
import re

# dict = {
# 	"ą": "a",
# 	"ć" : "c",
# 	"ę" : "e",
# 	"ł" : "l",
# 	"ń" : "n",
# 	"ó" : "o",
# 	"ś" : "s",
# 	"ź" : "z",
# 	"ż" : "z",
# 	"Ą" : "A",
# 	"Ć" : "C",
# 	"Ę" : "E",
# 	"Ł" : "L",
# 	"Ń" : "N",
# 	"Ó" : "O",
# 	"Ś" : "S",
# 	"Ź" : "Z",
# 	"Ż" : "Z"
# }
pattern = re.compile("([ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+)")

while 1:
	try:
		line = input().split()
		polish_words = []
		for word in line:
			reg = pattern.search(word)
			if reg != None: 
				polish_words.append(re.sub('([»<>«*:,.;"`"?!()])*', '', word))
		
		a = " ".join(polish_words)
		if a != "":
			print (a)
			pass
	except:
		break
	pass
