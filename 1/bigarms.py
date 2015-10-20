#!/usr/bin/python
def bigrams(sequence):

	if (type(sequence) is str): generate_bigrams(sequence)
	else: 
		for element in sequence: generate_bigrams(element)


def generate_bigrams(instance):

	reductions = []
	for x in range(len(instance)):

		inst = instance[x:x+2]
		if (len(inst)==2): reductions.append(inst)

	print reductions

a = ("qwertya ","asdfghju","zxcvbnm")
b = ["qwertyu","asdfghju","zxcvbnm"]
c = set(["qwertyu","asdfghju","zxcvbnm"])


bigrams("banana")
bigrams(a)
bigrams(b)
bigrams(c)