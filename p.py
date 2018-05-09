#!/bin/python

i = raw_input("Ingresa: ")

if len(i) == 3 and i[1] == ',' and i[0].isdigit() is True and i[2].isdigit() is True:
    print "cierto"

