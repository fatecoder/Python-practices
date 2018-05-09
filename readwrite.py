#!/bin/python

class Doc(object):
    def myWrite(self, s, s1, s2, c):
        f = open('pruebas.txt', 'w')
        for i in range(c):
            f.write(s+"\n"+s1+"\n"+s2+"\n"+s+"\n"+s1+"\n"+s2+"\n"+s1+"\n"+s+"\n")
        f.close()

    def myRead(self):
        f = open('pruebas.txt', 'r')
        for li in f:
            print li,
        f.close()

    def myAppend(self, s, c):
        f = open('pruebas.txt', 'a')
        for i in range(c):
            f.write(s+"\n")
        f.close()

#f = open('pruebas.txt', 'r+')
#for i in range(15):
#    f.write("|--------|\n|        |\n|        |\n|--------|\n")
#for i in f:
#    print i,
#f.close()

s = raw_input("Input a string: ")
s1 = raw_input("Input a new string: ")
s2 = raw_input("Input another string: ")
c = raw_input("Input times to repeat: ")

doc = Doc()
doc.myWrite(s, s1, s2, int(c))
doc.myRead()

a = raw_input("Input a string: ")
b = raw_input("Input times to repeat: ")
doc.myAppend(a, int(b))
doc.myRead()
