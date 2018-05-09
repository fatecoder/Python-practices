#!/bin/python

import urllib2
import xml.etree.ElementTree as ET

class Records(object):

    def get_xml(self):
        content = urllib2.urlopen("https://www.w3schools.com/xml/cd_catalog.xml")
        tree = ET.parse(content)
        root = tree.getroot()
        return root

    def find_indexes(self, root, string):
        indexes_cd = []
        for i in range(len(root)):
            for child in root[i]:
                if string.lower() in child.text.lower() and i not in indexes_cd:
                    indexes_cd.append(i)
        return indexes_cd

    def print_details(self, indexes_cd, root):
        print "%s Record(s) Found: " % len(indexes_cd)
        for index in indexes_cd:
            print "---"
            for child in root[index]:
                print "%s: %s" % (child.tag, child.text)

rec = Records()
input_string = raw_input("Welcome to PyCD! Find Record: ")
root = rec.get_xml()
list = rec.find_indexes(root, input_string)
rec.print_details(list, root)
