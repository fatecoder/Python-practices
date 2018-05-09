#!/bin/python

import random

acierto = True
ini = 1
fin = 100

pensado = random.randrange(ini, fin)

print "Piensa en un numero entre el 1 y el 100..."
while acierto :
    res = raw_input("Piensas en el: %i ? \n(si/no): " %pensado)
    if res.lower() == "si" :
        acierto = False
    else :
        m = raw_input("Mas o menos?: ")
        if m.lower() == "mas" :
            ini = pensado
            pensado = ini + ((fin - ini)/2)
        elif m.lower() == "menos" :
            fin = pensado
            pensado = ((fin - ini)/2) + ini
