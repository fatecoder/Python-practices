#!/bin/python

class First_class :

    def __init__(self, name_class):
        self.name_class = name_class
        self.actions_class = []

    def add_action(self, action_class):
        self.actions_class.append(action_class)

    def my_function(self):
        print "I'm a function"

instance = First_class("primera instancia")
instance2 = First_class("segunda instancia")

instance.add_action("Borrar")
instance.add_action("Cortar")
instance2.add_action("Borrar tambien")
print instance.name_class
print instance.actions_class

print instance2.name_class
print instance2.actions_class
