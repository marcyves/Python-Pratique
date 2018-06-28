#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

racine = os.getcwd() + os.sep + "test"
dossier = os.listdir(racine)
print("Contenu du dossier {}".format(dossier))
for fichier in dossier:
    nom_complet = racine + os.sep + fichier
    if os.path.isfile(nom_complet):
        print(fichier)
fichier_travail = input("Quel fichier ? ==> ")
fichier_travail = racine + os.sep + fichier_travail

try:
    print("Nous allons lire le fichier {}".format(fichier_travail))
    f = open(fichier_travail)
except FileNotFoundError as e :
    print("Le fichier {} n'existe pas !".format(e.filename))
    try:
        f = open(fichier_travail, 'w+')
    except FileNotFoundError as e :
        print("Je ne peux pas créer le fichier")
        exit(2)
    except Exception as e:
        print("Erreur : {}".format(e))
    else:
        print("Le fichier a été créé")
except Exception as e:
    print("Erreur : {}".format(e))
print("On continue")
texte = f.read()
print("Contenu du fichier\n")
print(texte)