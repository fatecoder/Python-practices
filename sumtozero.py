#!/bin/python

class Check(object):
    def sum_to_zero(self, lista):
        cont = 0
        list = []
        for i in range(len(lista)):
            for j in range(len(lista)):
                for k in range(len(lista)):
                    if lista[i] + lista[j] + lista[k] is 0 and j > i and k > j:
                        list.append([lista[i], lista[j], lista[k]])
        return list


lista = [-25, -10, -7, -3, 2, 4, 8, 10]
#lista = [-3, -25, 6, 10, 23, 28, 24, 2, 1]
#lista =  [1, 2, 3, 4, 5, 6, 7, -10, -11, -8]
check = Check()
print check.sum_to_zero(lista)
