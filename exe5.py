#!/bin/python

word = raw_input("Enter a word: ")

if word.isalpha() :
    print "Good!"
    print "---> %s" %word[1:] + word[0] + "ay"
else :
    print "Please, enter a valid word..."
