#!/bin/python

import json


class JSONparser(object):

    def ext_json(self, file):
        js = ''
        t = open(file, "r")
        js = t.read()
        t.close()
        return js

    def show_first_element(self, js):
        s = js.keys()[0] + ":" + js[js.values()[0]]
        return js.keys()[0]

    def show_last_element(self, js):
        return js.keys()[len(js.keys())-1]

    def show_all(self, js):
        print 

jsparser = JSONparser()
exjs = jsparser.ext_json("el_json")
js = json.loads(exjs)

def loop_d(cont):
    for el in cont:
        if type(cont[el]) == type(dict()):
            print "json %s" %el
            loop_d(cont[el])
        elif type(cont[el]) == type(list()):
            print "list %s" %el

loop_d(js)


jsparser.show_first_element(js)
