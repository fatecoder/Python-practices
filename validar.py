#!/bin/python

class Check(object):
    def op_clo(self, st):
        dict = { "(":")", "{":"}", "[":"]"}
        com = []
        for c in st:
            if c in dict:
                if st.count(c) == st.count(dict[c]) and st.index(c) < st.index(dict[c]):
                    com.append(True)
                else:
                    com.append(False)
        print com

check = Check()
str = raw_input("Input: ")
print check.op_clo(str)
