#!/bin/python

list  = [1, 2, 5, 8, -4, -3, 7, 6, 5, 4]
total = 0

for i in range(len(list)) :
    if i == 0 or i % 2 == 0 :
        if i < len(list)-1 :
            if list[i] == list[i+1] -1 or list[i] == list[i+1] +1 :
                total = total +1

print total
