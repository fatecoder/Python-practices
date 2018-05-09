#!/bin/python

#even_squares = [x%2==0 for x in range(1, 11)]
even_squares = [x**2 for x in range(2, 11, 2)]

print even_squares

even_squares2 = [x**2 for x in range(1, 11) if x%2==0]

print even_squares2
