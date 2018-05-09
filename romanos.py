#!/bin/python

#I 1
#V 5
#X 10
#L 50
#C 100
#D 500
#M 1000

dict = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
num = int(raw_input("Input a number: "))

#determinar si es decena, centena o mil

#print len(str(num))
#1 es menor que 10
#2 son decenas
#3 son centenas
#4 son miles

#if num in dict:
#    print dict[num]

mod = num % 10
nuevo = num - mod
#print mod
#print nuevo

if num in dict:
    print dict[num]

elif len(str(num)) is 2:
    divisible = nuevo / 10
    conc = ''
    if divisible < 4:
        for i in range(divisible):
            conc = conc + dict[10]
        #print divisible
        print "%s%s" %(conc, dict[mod])
    elif divisible == 4:
        conc = dict[40]
        print "%s%s" %(conc, dict[mod])

else:
    print "Nothing"
