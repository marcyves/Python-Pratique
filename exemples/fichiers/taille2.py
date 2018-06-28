#! /usr/bin/python
# -*- coding: latin-1 -*-     # permet les accents dans le script

import os.path

def sizedirectory(path):
    size = 0
    for root, dirs, files in os.walk(path):
        for fic in files:
            size += os.path.getsize(os.path.join(root, fic))
    return size

chemin=os.getcwd()
print (sizedirectory(chemin))
