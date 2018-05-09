#!/bin/python

import math
from random import randrange

numero = randrange(-100,100)

#print dir(math)
#print dir(randrange)

print "################################################"
print "Numero: %i" %numero
if numero < 0 :
    numero = abs(numero)
print "La raiz es: %f" %math.sqrt(numero)
print "Potencia al cuadrado: %s" %math.pow(numero,2)
print "Raiz %s" %type(math.sqrt(numero))
print "Numero %s" %type(numero)

def rec() :
    palabra = raw_input("Ingresa una palabra: ")
    if palabra.isalpha() :
        print "Palabra %s" %type(palabra)
        print "Max: %s" %max(palabra)
        print "Min: %s" %min(palabra)
        print "steps %s" %palabra[::2]
        print min(palabra) + palabra[1:len(palabra)-1] + max(palabra)
        return True
    else :
       print "Tienes que ingresar una palabra valida"
       return False

print rec()

