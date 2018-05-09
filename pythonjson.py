#!/bin/python

import json
import urllib2

content = urllib2.urlopen("direccion json").read()

#print content


my_json = json.loads(content)
print my_json
