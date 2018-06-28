#! /usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
# Choisir la ligne en fonction de l'os - permet les accents dans le script

import sys, os
script= sys.argv[0]  # le premier element de argv est le nom du script, les suivants: parametres
chemin= os.path.abspath(script)  # chemin + nom du script
repertoire= os.path.dirname(chemin)  # retourne la partie chemin
print (repertoire)
