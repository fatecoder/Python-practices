#!/bin/python

import random
import math

vista = []
tam = random.randrange(2, 6)
ship = [random.randrange(0, tam), random.randrange(0, tam)]
intentos = math.ceil((tam * tam) * 0.25)

def rellenar_vista() :
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

def play(intentos) :
    print "Tienes: %i" %intentos + " intentos"
    if intentos > 0 :
        cx = int(raw_input(".:Ingresa coordenadas a atacar:.\n-> Coord x: "))
        cy = int(raw_input("-> Coord y: "))

        if cx <= tam and cy <= tam and cx > 0 and cy > 0:
            if ship[0] == cx - 1 and ship[1] == cy - 1 :
                print "NAVE DESTRUIDA!!!"
                vista[ship[1]][ship[0]] = "S"
                vista_usuario()
            elif vista[cy -1][cx -1] == "X" :
                print "Intenta en otro lugar"
                vista_usuario()
                play(intentos)
            else :
                print "SIGUE INTENTANDO...\n--------------------------------"
                vista[cy -1][cx -1] = "X"
                vista_usuario()
                intentos = intentos - 1
                play(intentos)
        else :
            print "VALORES FUERA DE RANGO\n------------------------------"
            vista_usuario()
            play(intentos)
    else : print "Intentos Agotados"

rellenar_vista()
vista_usuario()
play(intentos)
