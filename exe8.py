#!/bin/python

st1 = raw_input("Cadena 1: ")
st2 = raw_input("Cadena 2: ")
ini = 0
estatic = len(st1)
tam_st2 = len(st2)
cont = 0

def contar() :

    
    if st1[ini:tam_st2] == st2 :


    """if ini != estatic :
        if st1[ini:tam_st2] == st2 :
            cont = cont + 1
            print st1[ini:tam_st2]
            ini = ini + 1
            tam_st2 = tam_st2 + 1
            print st1[ini:tam_st2]
            contar()
    else :
        print "Listo: %i" %cont"""

contar()
