#!/bin/python

import random

vista = []
tam = random.randrange(2, 6)
ship = [random.randrange(0, tam), random.randrange(0, tam)]

for i in range(tam) :
    vista.append([])
    for j in range(tam) :
        vista[i].append("O")

def vista_usuario() :
    for i in range(len(vista)) :
        row = '            '
        for j in range(len(vista)) :
            row =  row +" "+ vista[i][j]
        print row

def play() :
    cx = int(raw_input(".:Ingresa coordenadas a atacar:.\n-> Coord x: "))
    cy = int(raw_input("-> Coord y: "))

    if cx <= tam and cy <= tam and cx > 0 and cy > 0:
        if ship[0] == cx - 1 and ship[1] == cy - 1 :
            print "NAVE DESTRUIDA!!!"
            vista[ship[1]][ship[0]] = "S"
            vista_usuario()
        else :
            print "SIGUE INTENTANDO...\n--------------------------------"
            vista[cy -1][cx -1] = "X"
            vista_usuario()
            play()
    else :
        print "VALORES FUERA DE RANGO\n------------------------------"
        vista_usuario()
        play()

vista_usuario()
play()
