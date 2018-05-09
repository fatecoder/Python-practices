#!/bin/python

class Check(object):
    def op_clo(self, st):
        dict = {"(":")","{":"}","[":"]"}
        for c in dict:
            if c in st or dict[c] in st:
                if st.count(c) != st.count(dict[c]) or st.index(dict[c]) < st.index(c):
                    return False
        return True

check = Check()
str = raw_input("Input: ")
print check.op_clo(str)
