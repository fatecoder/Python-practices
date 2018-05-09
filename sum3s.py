#!/bin/python

list = [1, 2, 3, 322]
total = 0

for elem in list :
    if elem % 2 != 0 and "3" in str(elem) :
        total = total + elem
        #print elem

print total
