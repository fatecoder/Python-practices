#!/bin/pyhton

class Numbers(object):
    def convertToRomano(self, num):
        if int(num) <= 39999 and int(num) > 0:
            dict = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M", 4000:"MS", 5000:"S", 9000:"MW", 10000:"W"}
            lista = []
            m = 1
            conc = ''
            for i in range(len(num)):
                lista.append(num[i])

            lista.reverse()
            for i in range(len(lista)):
                lista[i] = str(int(lista[i]) * m)
                m = m * 10
            print lista
            m = 1
            for i in range(len(lista)):
                conc2 = ''
                for j in range( int(lista[i]) / m ):
                    if j == 3 or j == 4 or j == 8:
                        conc2 = dict[(j*m)+m]
                    elif j == 5:
                        conc2 = "%s%s" %(dict[j*m],dict[m])
                    else:
                        conc2 += dict[m]
                conc = conc2 + conc
                m = m * 10
            return conc

rom = Numbers()
num = raw_input("Introduce un numero: ")
print "Convertido: %s" %rom.convertToRomano(num)

#for i in range(1, 4000):
#    print "%s - %s" %(i,rom.convertToRomano(str(i)))
