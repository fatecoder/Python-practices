#!/bin/python

class Check(object):
    def op_clo(self, st):
        dict = {"(":")","{":"}","[":"]"}
        for c in st:
            if c in dict:
                

