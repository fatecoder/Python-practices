#!/bin/python

num = float(raw_input("Input a number: "))
#print "%.2f" %num

def red(num) :
    ent = num - (num % 1)
    dec = (num % 1) * 100
    dec = (dec - (dec % 1)) / 100
    return (ent +  dec)

print red(num)
