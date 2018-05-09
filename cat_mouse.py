#!/bin/python

import random

tablero = ['-','-','-','-','-','-','-','-','-']

def input_usuario():
    lugar = int(raw_input("Ingresa el lugar: "))
    if lugar >= 0 and lugar < 9 and tablero[lugar] == '-':
        tablero[lugar] = 'O'
    else :
        print "No permitido"

def input_auto():
    if '-' in tablero :
        lugar = random.randrange(0, 9)
        if tablero[lugar] == '-' :
            tablero[lugar] = 'X'
        else :
            input_auto()

def ver_tablero():
    conc = ''
    for i in range(len(tablero)) :
        conc = conc + str(tablero[i])
        if i == 2 or i == 5:
            conc = conc + '\n'
    print conc

def comprobar() :
    gane = [[0,1,2],[2,5,8],[6,7,8],[0,3,6],[0,4,8],[2,4,6],[1,4,7],[3,4,5]]
    for i in range(len(gane)):
        print gane[i][0]
        if tablero[gane[i][0]] == 'O' and tablero[gane[i][1]] == 'O' and tablero[gane[i][2]] == 'O' :
            return True

        elif tablero[gane[i][0]] == 'X' and tablero[gane[i][1]] == 'X' and tablero[gane[i][2]] == 'X':
            return False

def juego():
    if '-' in tablero :
        input_usuario()
        input_auto()
        ver_tablero()
        if comprobar() is True:
            print "Gana Jugador"
        elif comprobar() is False:
            print "Gana Maquina"
        else:
            juego()

ver_tablero()
juego()
#comprobar()
