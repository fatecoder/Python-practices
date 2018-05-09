#!/bin/python

concat=''
frase = raw_input("Ingresa una palabra o frase: ")

print "Contiene %s caracteres" % len(frase)
print "Aplicando lower(): %s" % frase.lower()
print "Aplicando upper(): %s" % frase.upper()

ind = raw_input("Obtener la letra en indice: ")

concat = concat + frase[int(ind)]

ind = raw_input("Obtener la letra en indice: ")

concat = concat + frase[int(ind)]

ind = raw_input("Obtener la letra en indice: ")

concat = concat + frase[int(ind)]

print concat
print frase[4:9]
