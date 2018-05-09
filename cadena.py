#!/bin/python

str1 = raw_input("Ingresa el primer string: ")
str2 = raw_input("Ingresa el segundo string: ")
ini = 0
fin = len(str2)
acum = 0

def contar_veces (ini, fin, str1, str2, acum):
    if len(str1) >= fin :
        #print str1[ini:fin]
        if str1[ini:fin] == str2 :
            acum = acum + 1
        ini = ini + 1
        fin = fin + 1
        contar_veces(ini, fin, str1, str2, acum)
    elif len(str1) < len(str2):
        print "Error, la primera cadena debe ser la mas grande"
    else :
        print "La segunda cadena aparece %i veces dentro de la primera cadena" %acum
contar_veces(ini, fin, str1, str2, acum)
