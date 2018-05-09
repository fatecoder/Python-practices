#!/bin/python

list = [0, 0, 0, 0]

st = raw_input("Input any number of characters: ")

for c in st :
    if c.isupper() :
        list[0] = list[0] + 1
    elif c.islower() :
        list[1] = list[1] + 1
    elif c.isdigit() :
        list[2] = list[2] + 1
    else :
        list[3] = list[3] + 1

print list
