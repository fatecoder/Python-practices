#!/bin/python

import urllib2
content = urllib2.urlopen("https://www.script-tutorials.com/demos/181/index.html")
#print content.read()

lista_nombres = []
lista_precios = []

for line in content:
    if 'class="title"' in line:
        lista_nombres.append(line[line.index(">")+1:line.index("</a")])
    if 'class="st"' in line:
        lista_precios.append(line[line.index("$")+1:line.index(".")+3])

for i in range(len(lista_precios)):
    print "%s : $%s" %(lista_nombres[i],lista_precios[i])
