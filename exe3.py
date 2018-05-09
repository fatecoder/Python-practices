#!/bin/python
#mostrar datetime solamente

from datetime import datetime

current = datetime.now();

print "Complete: %s" %current
print "Year: %s" %current.year

if int(current.month) < 10 :
  print "Month 0%s" %current.month
else :
  print "Month: %s" %current.month

if int(current.day) < 10 :
  print "Day: 0%s" %current.day
else :
  print "Day: %s" %current.day

if int(current.hour) < 10 :
  print "Hour: 0%s" %current.hour
else :
  print "Hour: %s" %current.hour

if int(current.minute) < 10 :
  print "Minutes: 0%s" %current.minute
else :
  print "Minutes: %s" %current.minute

if int(current.second) < 10 :
  print "Seconds: 0%s" %current.second
else :
  print "Seconds: %s" %current.second

print "Microsecond: %s" %current.microsecond
