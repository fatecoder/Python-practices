#!/bin/python

#list = [1, 2, 5, 8, -4, -3, 7, 6, 5]
list = [1, 3, 1, 2, 1, 2, 1, 2, 3, 4, 6, 6, 7]
total = 0

for i in range(len(list)) :
    if i < len(list)-1 and (list[i] == list[i+1] +1 or list[i] == list[i+1] -1) :
        total = total +1
        list.pop(i+1)

print total

