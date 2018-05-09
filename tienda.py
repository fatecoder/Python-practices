#!/bin/python

#diccionario

arts = [
         'USB 32 Gb',
         'Mouse Logitech',
         'Teclado Logitech',
         'Laptop Lenovo',
         'Cargador Lenovo',
         'Cable HDMI'
       ]

precios = {
            arts[0]: 480,
            arts[1]: 220,
            arts[2]: 380,
            arts[3]: 12000,
            arts[4]: 1500,
            arts[5]: 450
           }

stock = {
          arts[0]: 50,
          arts[1]: 30,
          arts[2]: 15,
          arts[3]: 80,
          arts[4]: 51,
          arts[5]: 60
        }

empty = []
ins_nom = ''
ins_precio = 0
ins_stock = 0


def ver_todo_empty() :
    for item in empty :
        print item

def llenar_vacio() :
    for item in arts :
        cadena = "%s " %arts.index(item) + "Articulo: %s " %item + "Precio: $%i " %precios[item] + "Stock: %i" %stock[item]
        empty.append(cadena)

    ver_todo_empty()

llenar_vacio()


print "-------------------------------------------------------------"

def consultar () :
    ans = raw_input("Quieres consultar un articulo?(si/no): ")

    if ans.lower() == "si" :
        look = raw_input("Ingresa el nombre del articulo: ")
        for item in arts :
            if look.lower() == item.lower() :
                print "Articulo: %s" %item + "\nPrecio: $%i" %precios[item] + "\nStock: %i" %stock[item]
    elif ans.lower() == "no" :
        print "Vuelva pronto..."

consultar()

print "------------------------------------------------------------"

total = 0
def vender_todo (total) :
    for item in arts :
        total = total + (precios[item] * stock[item])
    return total

print "Vendiendo todo: %i" %vender_todo(total)

print "------------------------------------------------------------"

def ver_todo_arts() :
    for item in arts :
        print "%i " %arts.index(item) + "Articulo: %s " %item + "Precios: %i " %precios[item] + "Stock: %i " %stock[item]

def quitar (ins_nom) :
    arts.remove(ins_nom)
    del precios[ins_nom]
    del stock[ins_nom]

def insertar(ins_nom, ins_precio, ins_stock):
    arts.append(ins_nom)
    precios[ins_nom] = int(ins_precio)
    stock[ins_nom] = int(ins_stock)

def seleccion () :
    sel = raw_input("Insertar(i), Borrar(b) o Salir(s)?")
    if sel == "i" :
        ins_nom = raw_input("Nombre de Articulo: ")
        ins_precio = raw_input("Precio de Articulo: ")
        ins_stock = raw_input("Cantidad de Articulos: ")
        insertar(ins_nom, ins_precio, ins_stock)
        ver_todo_arts()
        print "~~~~~~~~"
        seleccion()
    elif sel == "b" :
        ins_nom = raw_input("Nombre de Articulo a Borrar: ")
        quitar(ins_nom)
        ver_todo_arts()
        print "~~~~~~~~"
        seleccion()
    elif sel == "s" :
        print "Saliendo..."
    else :
        seleccion()

seleccion()
