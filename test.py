import re
a = "aaaaaa"
pattern = re.compile("^(a+|b)$")
word = pattern.search(a)
print word.group()