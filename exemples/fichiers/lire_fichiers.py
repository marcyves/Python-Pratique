#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

dossier = "/Users/marc/Google Drive/Cours/M2I - Python/Exercices pratiques/Scripts Online/"

for repertoire, sous_repertoires, fichiers in os.walk(dossier):
    print("* - "*10)
    print ("\nRépertoire :", repertoire)
    print ("  Sous-répertoire :", sous_repertoires)
    print ("  Fichier :", fichiers)

    for sous_repertoire in sous_repertoires:
        print('\t- sous_repertoire ' + sous_repertoire)

    print("\t- Les fichiers du sous repertoire")
    for fichier in fichiers:
        file_path = os.path.join(repertoire, fichier)
        print(file_path)
