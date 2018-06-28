#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

dossier = "C:\\Users\\Administrateur\\Desktop\\"

for rep, sous_reps, fichiers in os.walk(dossier):
    print("\Répertoire :",rep)
    print(" Liste sous répertoires : ", sous_reps)
    print(" Fichier : ", fichiers)

    for sous_rep in sous_reps:
        print("\t Sous répertoire",sous_rep)
    for fichier in fichiers:
        print("\t Fichier ", fichier)