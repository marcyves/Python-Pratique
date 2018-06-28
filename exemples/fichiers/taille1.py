#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

dossier = "C:\\Users\\Administrateur\\Desktop\\"

taille = 0
for rep, sous_reps, fichiers in os.walk(dossier):
    for fichier in fichiers:
        taille += os.path.getsize(os.path.join(rep,fichier))

print(taille)