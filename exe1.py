#!/bin/python

#Total_de_la_cuenta

costo=44.50
INT_RES=6.75/100
PROP=15.0/100
total=0

print "Costo de la comida $44.50"
print "Interes del restaurante 6.75%"
print "Propina 15%"

total=costo
INT_RES=INT_RES*costo
total=total+INT_RES
PROP=PROP*total
total=total+PROP
costo=total

print "TOTAL:"
print costo
