#!/usr/bin/python
def freq_dic(sequence):
	if (type(sequence) is int or type(sequence) is float):
		print "You have given number parameter =",sequence,"Please insert tuple, list, string or set."
	else:
		dictionary = dict.fromkeys(sequence, 0)
		for char in sequence: 
			dictionary[char] += 1
		print dictionary
	pass
		
freq_dic("abracadabra")
freq_dic("aaaaabbbcaaaaaaaccc")
freq_dic(["s","s","s",3,3])
freq_dic((2,2,3,3))
freq_dic(set([2,2,2,2,2,3]))
freq_dic((1,2,4,3,2,1,3,2))
freq_dic([1,2,4,3,2,1,3,2])
freq_dic(set([1,2,4,3,2,1,3,2]))
freq_dic(set("12432132"))
freq_dic(12432132)
freq_dic(1243.2132)
