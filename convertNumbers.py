#!/bin/pyhton

class Numbers(object):
    def convertToRomano(self, num):
        dict = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        lista = []
        for i in range(len(num)):
            lista.append(num[i])

        lista.reverse()
        mul = 1
        for i in range(len(lista)):
            lista[i] = str(int(lista[i]) * mul)
            mul = mul * 10
        print lista
        m = 1
        conc = ''
        #ejemplo 888
        for i in range(len(lista)):
            conc2 = ''
            for j in range( int(lista[i]) / m ):
                if j == 3:
                    conc2 = dict[(j*m)+m]
                elif j == 4:
                    conc2 = dict[(j*m)+m]
                elif j == 5:
                    conc2 = "%s%s" %(dict[j*m],dict[m])
                elif j == 8:
                    conc2 = dict[(j*m)+m]
                else:
                    conc2 += dict[m]
            conc = conc2 + conc
            m = m * 10
        return conc

num = raw_input("Introduce un numero: ")
rom = Numbers()

if int(num) < 3999 and int(num) > 0:
    print "Convertido: %s" %rom.convertToRomano(num)
