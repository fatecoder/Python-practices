#!/bin/python

import json

class JSONParser(object):

    def json_loader(self):
        my_json = self.ext_json("json_heroes")
        return json.loads(my_json)

    def ext_json(self, p):
        ex = open(p, "r")
        js = ex.read()
        ex.close()
        return js

    def show_first_element(self, js):
        return "%s: %s" %(js.keys()[0], js.values()[0])

    def show_last_element(self, js):
        return "%s: %s" %(js.keys()[len(js.keys())-1], js.values()[len(js.values())-1])

    def show_all(self, js):
        return js

    def show_ints(self, js):
        d = {}
        for k in js:
            if type(js[k]) == type(int()):
                d[str(k)] = js[k]
        return d

    def show_strings(self, js):
        d = {}
        for k in js:
            if type(js[k]) == type(unicode()):
                d[str(k)] = str(js[k])
        return d

    def show_bools(self, js):
        d = {}
        for k in js:
            if type(js[k]) == type(bool()):
                d[str(k)] = js[k]
        return d

    def show_element(self, n, js):
        if len(js.keys()) >= n and n >= 0:
            return "%s: %s" %(js.keys()[n], js.values()[n])

    def show_w_format(self, js):
        for el in js:
            if type(js[el]) == type(list()):
                print el
                for eli in js[el]:
                    for elj in eli:
                        if type(eli[elj]) == type(list()):
                            print "  %s:" %elj
                            for elk in eli[elj]:
                                print "    %s" %elk
                        else:
                            print "  %s: %s" %(elj, eli[elj])
                    print
            else:
                print "%s: %s" %(el, js[el])

jsparser = JSONParser()
js = jsparser.json_loader()
"""print jsparser.show_first_element(js)
print jsparser.show_last_element(js)
print jsparser.show_all(js)
print jsparser.show_ints(js)
print jsparser.show_strings(js)
print jsparser.show_bools(js)
print jsparser.show_element(2, js)"""
jsparser.show_w_format(js)
