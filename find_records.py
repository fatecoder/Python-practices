#!/bin/python

import urllib2
import xml.etree.ElementTree as ET

class Records(object):

    def ext_xml(self):
        content = urllib2.urlopen("https://www.w3schools.com/xml/cd_catalog.xml")
        tree = ET.parse(content)
        root = tree.getroot()
        return root

    def get_data(self, root):
        dictio = {}
        for i in range(len(root)):
            l = []
            ltags = []
            for j in range(len(root[i])):
                if root[i][j].tag not in ltags:
                    ltags.append(root[i][j].tag)
                l.append("%s" %root[i][j].text)
            dictio["%s-%s" %(root[i].tag, i)] = l
        return [dictio, ltags]

    def find(self, s, dictio):
        lista = []
        for el in dictio:
            for e in dictio[el]:
                if s in e:
                    if el not in lista:
                        lista.append(el)
        return [len(lista),lista]

    def show(self, lista, dictio, ltags):
        for el in dictio:
            if el in lista:
                print "---"
                for i in range(len(dictio[el])):
                    print "%s: %s" %(ltags[i], dictio[el][i])

    def empezar(self,s):
        print "%s Record(s) found:" %self.find(s, self.get_data(self.ext_xml())[0])[0]
        self.show(self.find(s, self.get_data(self.ext_xml())[0])[1], self.get_data(self.ext_xml())[0], self.get_data(self.ext_xml())[1])

rec = Records()

inp = raw_input("Welcome to PyCD. Find Record: ")
rec.empezar(inp)
