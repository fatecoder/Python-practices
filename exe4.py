#!/bin/python

a="a"
b=1
c=2.2
d="1"

array = ["a", "b", "c", "d", "f", "g", "h"]
array2 = [1, 2, 3, 4, 5, 6, "h"]
array3 = ["a", "b", "c", "d", "f", "g", "h"]

print array[6] == array2[6]
print array2[5] > array2[0]
print array2[5] < array2[0]
print array2[0] != d

print "-----------------------------"
print 1 == "1"

print "-----------------------------"
print array2[0] is d
print array2[0] is b
print array2[0] == d
print array2[0] == b

print "-----------------------------"
print array is array3
print array == array3
print array is array2
print array == array2

print "-----------------------------"
print (array[0] == "a" and array3[0] == "a") is True
print (array[0] == "b" and array3[0] == "b") is not True
print (a == array[0] or a == array2[0]) is False
