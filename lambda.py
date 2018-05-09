#!/bin/python

squares = [x**2 for x in range(1, 11)]

print squares
print filter(lambda x: x >= 30 and x <= 70, squares)

squares2 = [x**2 for x in range(1, 11) if x**2 > 30 and x**2 < 70]
print squares2
