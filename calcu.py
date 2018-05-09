#!/bin/python

print "Choose an option\n1.-Addition\n2.-Substraction\n3.-Multiplication\n4.-Division"
option = raw_input(": ")

if int(option) > 0 & int(option) < 5 :
  value1 = float(raw_input("First value: "))
  value2 = float(raw_input("Second value: "))

  if option == "1" :
    res = value1 + value2
  elif option == "2" :
    res = value1 - value2
  elif option == "3" :
    res = value1 * value2
  elif option == "4" :
    res = value1 / value2

  print "= %f" %res

else :
  print "Exit..."
