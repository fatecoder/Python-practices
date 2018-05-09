#!/bin/python

import xml.etree.ElementTree as ET

class XMLParser():
    l = []
    def ext_xml(self):
        tree = ET.parse("xml_arc.xml")
        root = tree.getroot()
        return root

    def show_first_element(self, xml):
        return "%s: %s" %(xml[0][0].tag, xml[0][0].text)

    def show_last_element(self, xml):
        return "%s: %s" %(xml[0][len(xml[0])-1].tag, xml[0][len(xml[0])-1].text)

    def show_ints(self, xml):
        for el in xml:
            for e in el:
                if e.text.isdigit():
                    print "%s: %s" %(e.tag, e.text)

    def show_strs(self, xml):
        for el in xml:
            for e in el:
                if not e.text.isdigit() and e.text != "true" and e.text != "false":
                    print "%s: %s" %(e.tag, e.text)

    def show_bools(self, xml):
        for el in xml:
            for e in el:
                if e.text == "false" or e.text == "true":
                    print "%s: %s" %(e.tag, e.text)

    def show_all(self, r):
        for el in r:
            if str(el.attrib) != "{}":
                print "%s -> %s" %(el.tag, el.attrib)
                for e in el.attrib:
                    print "%s: %s" %(e, el.attrib[e])
            else:
                print "%s: %s" %(el.tag, el.text)
            self.show_all(el)

    def ext_all(self, r):
        for el in r:
            if str(el.attrib) != "{}":
                for e in el.attrib:
                    self.l.append([e, el.attrib[e]])
            else:
                self.l.append([el.tag,  el.text])
            self.ext_all(el)
        return self.l

    def show_list(self):
        self.ext_all(self.ext_xml())
        for el in self.l:
            print "%s: %s" %(el[0], el[1])

    def show_only_ints(self):
        self.ext_all(self.ext_xml())
        for el in self.l:
            if el[1].isdigit():
                print "%s: %s" %(el[0],el[1])



xmlparser = XMLParser()
root = xmlparser.ext_xml()
#xmlparser.show_all(root)
#xmlparser.show_strs(root)
#xmlparser.show_list()
print xmlparser.show_first_element(root)
print xmlparser.show_last_element(root)
