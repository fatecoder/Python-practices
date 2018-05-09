#!/bin/python

import random

tablero = []
vista = []
tam = random.randrange(2, 6)

def gene_tablero():
    for i in range(tam):
        tablero.append([])
        for j in range(tam):
            tablero[i].append("O")
    #ship
    tablero[random.randrange(0,tam)][random.randrange(0,tam)] = "S"

def test_view_tablero() :
    for i in range(len(tablero)) :
        row = ''
        for j in range(len(tablero)):
            row = row +" "+ tablero[i][j]
        print row

#test_view_tablero()

def gene_view() :
    for i in range(tam) :
        vista.append([])
        for j in range(tam) :
            vista[i].append("O")

def user_view() :
    for i in range(len(vista)) :
        row = '            '
        for j in range(len(vista)) :
            row =  row +" "+ vista[i][j]
        print row

def play() :
    print ".:Ingresa coordenadas a atacar:."
    cx = int(raw_input("-> Coord x: "))
    cy = int(raw_input("-> Coord y: "))

    if cx < tam and cy < tam :
        if tablero[cy][cx] == "S" :
            print "NAVE DESTRUIDA!!!"
            vista[cy][cx] = "S"
            user_view()
        else :
            print "SIGUE INTENTANDO..."
            print "-------------------------------"
            vista[cy][cx] = "X"
            user_view()
            play()
    else :
        print "VALORES FUERA DE RANGO"
        print "-------------------------------"
        user_view()
        play()

gene_tablero()
test_view_tablero()
gene_view()
user_view()
play()
