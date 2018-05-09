#!/bin/python
import random

#list = [random.randrange(1,5), random.randrange(1,5), random.randrange(1,5), random.randrange(1,5)]
list = [4, 1, 2, 3]
print list

def factorial(list):
    acum = list[0]*list[1]
    for i in range(2, len(list)):
        acum = acum * list[i]
    return acum

print factorial(list)
