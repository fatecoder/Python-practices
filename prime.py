#!/bin/python

def isprime(num):
    if num == 2:
       return True

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True

n = raw_input("Introduce un numero: ")
if n.isdigit():
   print isprime(int(n))
else :
    print "Eso no se puede evaluar"


