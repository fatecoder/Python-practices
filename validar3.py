#!/bin/python

class Check(object):
    def op_clo(self, st):
        dict = {"(":")","{":"}","[":"]"}
        for c in dict:
            if c in st or dict[c] in st:
                if st.count(c) != st.count(dict[c]):
                    return False
        for c in dict:
            if c in st or dict[c] in st:
                print c
                if st.index(c) > st.index(dict[c]):
                    return False
        print st.index(")")
        print st.index("(")
        if st.isalpha() or st.isalnum():
            return False
        return True

check = Check()
str = raw_input("Input: ")
print check.op_clo(str)
