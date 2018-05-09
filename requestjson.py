#!/bin/python

import urllib2
import json

content = urllib2.urlopen("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json").read()

my_json = json.loads(content)

for key in my_json:
    if key != "members":
        print "%s: %s" %(key, my_json[key])

for i in range(len(my_json["members"])):
    print "----------------"
    print "name: %s" %my_json["members"][i]["name"]
    print "age: %s" %my_json["members"][i]["age"]
    print "secretIdentity: %s" %my_json["members"][i]["secretIdentity"]
    print "powers:"
    for val in my_json["members"][i]["powers"]:
        print "    %s" %val

print "_______________"
my_json2 = json.loads('{ "book": [{ "id":"01", "language": "Java", "edition": "third", "author": "Herbert Schildt" },{ "id":"07", "language": "C++", "edition": "second", "author": "E.Balagurusamy"}]}')

for el in my_json2["book"]:
    for ne in el:
        print "%s: %s" %(ne,el[ne])
    print "---"
