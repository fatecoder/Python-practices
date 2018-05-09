#!/bin/python

cubes_by_four = [x**3 for x in range(2, 10, 2)]

print cubes_by_four

cubes_by_four2 = [x**3 for x in range(1, 10) if x**3 % 4 == 0]

print cubes_by_four2
