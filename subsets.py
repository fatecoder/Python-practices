#!/bin/python

class Check(object):
    def subsets(self, lista):
        list = []
	for item in lista:
 	    for j in range(len(lista)):
                if item != lista[j] and lista[j] > lista[lista.index(item)]:
                    list.append([item, lista[j]])
	return list

lista = [1,2,3]
check = Check()
print check.subsets(lista)
