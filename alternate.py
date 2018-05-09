#!/bin/python

chain = raw_input("Introduce una cadena: ")
new = ''

def alter (chain, new) :
    print chain
    for character in chain :
        if character == character.lower() :
            new = new + character.upper()
        elif character == character.upper() :
            new = new + character.lower()
    return new

print alter(chain, new)
