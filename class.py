#!/bin/python

class Animal :

    no_privado = "variable no privada"
    __privado = "variable privada"

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.accion = []

    def __fun_priv(self):
        return "funcion privada"

    def incluir_accion(self, nombre_accion):
        self.accion.append(nombre_accion)

    def calcular_cuadrados(self, limite):
        cubes_by_four = [x**3 for x in range(1, limite) if x**3 % 4 == 0]
        return cubes_by_four

animal = Animal("Perro", "Cafe")
animal.incluir_accion("Ladra")
animal.incluir_accion("Corre")

animal2 = Animal("Oso", "Negro")
animal2.incluir_accion("Ruge")

class Insecto(Animal):

    def insec_accion(self):
        return "Picar"

print animal.nombre
print animal.color
print animal.accion
print animal.calcular_cuadrados(20)
print animal.no_privado

print "------------------------------"
insecto = Insecto("Abeja", "Amarillo")
insecto.incluir_accion("Vuela")

print insecto.nombre
print insecto.insec_accion()
print insecto.color
print insecto.accion

print "------------------------------"
print animal2.nombre
print animal2.accion
