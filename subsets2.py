#!/bin/python

class Check(object):
    def subsets(self, lista):
        rlista = [[]]
        for el in lista:
            nlista = []
            for elr in rlista:
                #print elr
                nel = elr[0:len(elr)]
                nel.append(el)
                nlista.append(nel)
            rlista = rlista + nlista
        return rlista

lista = [4, 5, 6, 7]
check = Check()
print check.subsets(lista)
