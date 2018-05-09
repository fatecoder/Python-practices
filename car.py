#!/bin/python

class Car(object) :
    condition = "new"

    def __init__(self, model, color, kpl):
        self.model = model
        self.color = color
        self.kpl = kpl

    def display_car(self):
        print "Model: %s" %self.model
        print "Color: %s" %self.color
        print "KPL: %i" %self.kpl

    def drive_car(self):
        self.condition = "used"

my_car = Car("Mustang", "Red", 16)
my_car.display_car()
print "Condition: %s" %my_car.condition + "\n-----------"

print "Driving car"
my_car.drive_car()
print "-----------"
print "Condition: %s" %my_car.condition
