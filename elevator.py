#!/bin/python

import random

tam = random.randrange(3, 18)
floors = []

for i in range(tam) :
    floors.append(random.randrange(1, 10))

print floors

def elevator_distance(floors) :
    total = 0
    for i in range(len(floors)) :
        if i < len(floors)-1 :
            total = total + abs(floors[i] - floors[i+1])
    return total

print "Distance: %i" %elevator_distance(floors)
