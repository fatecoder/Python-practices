#!/bin/python

import random

p = ''
letras = ['a','b','c']
tablero = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def input_usuario():
    if espacios() is True:
        coor = raw_input("Ingresa posicion: {Ejemplo: %s," %random.choice(letras) + "%i}: " %random.randrange(1,4))
        if len(coor) == 3 and coor[1] == ',' and coor[0].isalpha() is True and coor[0] in letras and coor[2].isdigit() is True:
            cx = letras.index(coor[0])
            cy = int(coor[2]) - 1
            if cx >= 0 and cx < 3 and cy >= 0 and cy < 3 and tablero[cx][cy] == ' ' :
                tablero[cx][cy] = 'O'
                print "______________\nTurno de Jugador (O)"
                ver_tablero()
            else:
                print "No permitido"
                input_usuario()
        else :
            print "Formato incorrecto. Formato: {letra(a,b,c)}{,}{digito(1,2,3)}"
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
            print "____________\nTurno de Maquina (X)"
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

def comprobar(p):
    gane = [ [[0,0],[0,1],[0,2]], #h1 ->
             [[1,0],[1,1],[1,2]], #h2 ->
             [[2,0],[2,1],[2,2]], #h3 ->
             [[0,0],[1,0],[2,0]], #v izq
             [[0,1],[1,1],[2,1]], #v med
             [[0,2],[1,2],[2,2]], #v der
             [[0,0],[1,1],[2,2]], #diag izq
             [[0,2],[1,1],[2,0]] ] #diag der
    for i in range(len(gane)):
        if tablero[gane[i][0][0]][gane[i][0][1]] == p and tablero[gane[i][1][0]][gane[i][1][1]] == p and tablero[gane[i][2][0]][gane[i][2][1]] == p:
            return True

def juego():
    if espacios() is True :
        input_usuario()
        if comprobar("O") is True:
            print "Gana Jugador"
        else:
            input_auto()
            if comprobar("X") is True:
                print "Gana Maquina"
            else :
                juego()
    else:
        print "Empate..."

ver_tablero()
juego()
