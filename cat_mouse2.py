#!/bin/python

import random

tablero = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def input_usuario():
    cx = int(raw_input("Ingresa coordenada X: "))
    cy = int(raw_input("Ingresa coordenada Y: "))
    if cx >= 0 and cx < 3 and cy >= 0 and cy < 3 and tablero[cy][cx] == ' ' :
        tablero[cy][cx] = 'O'
        print "______________\nTurno de Jugador"
        ver_tablero()
    else :
        print "No permitido"
        input_usuario()

def espacios():
    for i in tablero :
        for j in i:
            if j == ' ':
                return True

def input_auto():
    if espacios() is True:
        cx = random.randrange(0, 3)
        cy = random.randrange(0, 3)
        if tablero[cy][cx] == ' ':
            tablero[cy][cx] = 'X'
            print "____________\nTurno de Maquina"
            ver_tablero()
        else :
            input_auto()

def ver_tablero():
    conc = ''
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if j == 2 and i != 2:
                conc = conc + " "+str(tablero[i][j])+" " + "\n-----------"
            elif  i == 2 and j == 2:
                conc = conc +" "+str(tablero[i][j])
            else:
                conc = conc +" "+ str(tablero[i][j])+" " + "|"
        conc = conc + '\n'
    print conc

def comprobar():
    gane = [ [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]], [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]] ]

    for i in range(len(gane)):
       if tablero[gane[i][0][0]][gane[i][0][1]] == 'O' and tablero[gane[i][1][0]][gane[i][1][1]] == 'O' and tablero[gane[i][2][0]][gane[i][2][1]] == 'O':
           return True
       if tablero[gane[i][0][0]][gane[i][0][1]] == 'X' and tablero[gane[i][1][0]][gane[i][1][1]] == 'X' and tablero[gane[i][2][0]][gane[i][2][1]] == 'X':
           return False

def juego():
    if espacios() is True :
        input_usuario()
        if comprobar() is True:
            print "Gana Jugador"
        else:
            input_auto()
            if comprobar() is False:
                print "Gana Maquina"
            else :
                juego()
    else:
        print "Empate..."

ver_tablero()
juego()

#print "   |   |   "
#print "-----------"
#print "   |   |   "
#print "-----------"
#print "   |   |   "
