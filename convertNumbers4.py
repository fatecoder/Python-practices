#!/bin/python

class Convert(object):
    def toRomano(self, num):
        if num.isdigit() and int(num) <= 3999 and int(num) > 0:
            dict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"F", 1000:"C"}
            lista = []
            m = 10**len(num)
            conc = ''
            for i in range(len(num)):
                m = m / 10
                lista.append(str( int(num[i]) * m ))
            lista.reverse()
            m = 1
            for i in range(len(lista)):
                conc2 = ''
                for j in range( int(lista[i]) / m ):
                    if j == 3 or j == 8:
                        conc2 = "%s%s" %( dict[m], dict[(m*(j+1))+m] )
                    elif j == 4:
                        conc2 = dict[(m*j)+m]
                    elif j == 5:
                        conc2 = "%s%s" %(dict[m*j],dict[m])
                    else:
                        conc2 += dict[m]
                conc = conc2 + conc
                m = m * 10
            return conc
rom = Convert()
num = raw_input("Introduce un numero: ")
print "Convertido: %s" %rom.toRomano(num)
#for i in range(1, 4000):
#    print "%s - %s" %(i,rom.toRomano(str(i)))
