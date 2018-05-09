#!/bin/python

import random
import math

vista = []
tam = random.randrange(2, 8)
intentos = math.ceil((tam*tam) * 0.33 )
num_ships = math.floor((tam*tam) * 0.25)
ship_cont = []

"""def ships() :
    for i in range(int(num_ships)) :
        ship_cont.append([random.randrange(0, tam), random.randrange(0, tam)])
        while ship_cont.count(ship_cont[i]) > 1 :
            print "dentro del while %s" %ship_cont[i]
            ship_cont.pop()
            ship_cont.append([random.randrange(0, tam), random.randrange(0, tam)])"""

def ships() :
    for i in range(int(num_ships)) :
        new_ship = [random.randrange(0, tam), random.randrange(0, tam)]
        if new_ship not in ship_cont :
            ship_cont.append(new_ship)
        else :
          i = i - 1

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

def play(intentos, num_ships) :
    print "Intentos: %i" %intentos + " restantes"
    print "Naves: %i" %num_ships + " restantes"
    if num_ships > 0 :
        if intentos > 0 :
            cx = int(raw_input(".:Ingresa coordenadas a atacar:.\n-> Coord x: "))
            cy = int(raw_input("-> Coord y: "))
            if cx <= tam and cy <= tam and cx > 0 and cy > 0:
                if ship_cont.count([cx-1, cy-1]) == 1 and vista[cy -1][cx -1] != "S":
                    print "NAVE DESTRUIDA!!!\n--------------------------------"
                    vista[cy -1][cx -1] = "S"
                    num_ships = num_ships - 1
                    vista_usuario()
                    play(intentos, num_ships)
                elif vista[cy -1][cx -1] == "X" or vista[cy -1][cx -1] == "S" :
                    print "INTENTA EN OTRO LUGAR\n--------------------------------"
                    vista_usuario()
                    play(intentos, num_ships)
                else :
                    print "SIGUE INTENTANDO...\n--------------------------------"
                    vista[cy -1][cx -1] = "X"
                    vista_usuario()
                    intentos = intentos - 1
                    play(intentos, num_ships)
            else :
                print "VALORES FUERA DE RANGO\n------------------------------"
                vista_usuario()
                play(intentos, num_ships)
        else : print "INTENTOS AGOTADOS..."
    else : print "TODAS LAS NAVES DESTRUIDAS!"

ships()
print intentos
print num_ships
print ship_cont
rellenar_vista()
vista_usuario()
play(intentos, num_ships)

