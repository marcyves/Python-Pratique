#! /usr/bin/python
# -*- coding: latin-1 -*-     # permet les accents dans le script
import os
chemin=os.getcwd()            # ! il ne s'agit pas nécessairement du répertoire du script
dossier=os.listdir(chemin)
for nom in dossier:           # pour chaque chose rencontrée dans un répertoire
  element= chemin+os.sep+nom  # le chemin complet est composé
  if os.path.isfile(element): # teste si element est un fichier
    print (element)
