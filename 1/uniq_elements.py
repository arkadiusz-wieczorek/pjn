#!/usr/bin/python
def uniq_elements(sequence):
	if (type(sequence) is int or type(sequence) is float): 
		print "You have given number parameter =",sequence,"Please insert tuple, list, string or set."
	else:
		print len(set(sequence))
	pass

uniq_elements((1,2,4,3,2,1,3,2))
uniq_elements([1,2,4,3,2,1,3,2])
uniq_elements(set([1,2,4,3,2,1,3,2]))
uniq_elements("abracadabra")
uniq_elements(set("abracadabra"))
uniq_elements(12432132)
uniq_elements(1243.2132)


# # lista [2,3,5,3,2,1]
# # zbior set(2,2,3)
# # tuple/krotka (1,2,2,4,5,6)
# # lancuch "asdasaada"