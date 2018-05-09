#!/bin/python

k2 = {"casa1":255, "casa2":256, "casa3":257}
colors = ["red", "yellow", "blue", "orange", "pink", "black"]
k1 = {"colors":colors}
d = {"key1":k1, "key2":k2}

#print d["key1"]
print d["key2"]["casa1"]
print d["key1"]["colors"][0]
