#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
# XML
# overpass-api.de/api/interpreter?data=node[name="Cannes"];out;

url = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    ville = input("Quelle ville ? => ")
    if len(ville) < 1:
        break
    url_gm = url + urllib.parse.urlencode({'address': ville,'sensor':'false'})
    # print(url_gm)
    page = urllib.request.urlopen(url_gm)
    data = page.read()
    print("Nous avons lu {} caractères.".format(len(data)))

    js = json.loads(data)

    if js['status'] == "OVER_QUERY_LIMIT":
        print("Google nous refuse")
    elif js['status'] == 'OK':
        continue
    else:
        print(json.dumps(js, indent=4))