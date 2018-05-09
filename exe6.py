#!/bin/python

from random import randrange, choice

ini = 1
fin = 101
veces = 0
frases = ["Es el numero ", "Acaso es el ", "Podria ser el ", "Piensas en el ", "Probablemente es el ", "Tu numero es el "]

pensado = randrange(ini, fin)
print "Piensa en un numero entero entre el 1 y el 100..."

def adivina(ini, fin, pensado, veces) :
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - -"
    res = raw_input(choice(frases) + "%i ? \n(si/no): " %pensado)
    if res.lower() != "no" :
        print "Lo sabia!!!"
    else :
        m = raw_input("Mas o menos?: ")
        if m.lower() == "mas" :
            ini = pensado
        elif m.lower() == "menos" :
            fin = pensado
        pensado = ini + ((fin - ini)/2)
        veces = veces + 1
        if veces == 7 :
            print "Deberia ser el %i" %pensado
        elif veces > 7 :
            print "Estas mintiendo..."
        adivina(ini, fin, pensado, veces)

adivina(ini, fin, pensado, veces)

# 100
# 50
# 25
# 12
# 6
# 3
# 1
