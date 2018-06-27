#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re

BLACK   = 0
RED     = 1
GREEN   = 2
YELLOW  = 3
BLUE    = 4
PINK    = 5
CYAN    = 6
WHITE   = 7
B8      = 8
DEFAULT = 9

def color(code, background=False):
    if background:
        print('\033[4{}m'.format(code), end ='')
    else:
        print('\033[3{}m'.format(code), end ='')


def clearShell():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
#    sys.stdout.write("\x1b[8;32;63t")
#    sys.stdout.write("\x1b[48;5;211m")
    sys.stdout.flush()
    items = [
        'Terminer',
        'Liste des projets',
        'Liste des environnements',
        'Tâches par projet',
        'Tâches par environnement',
        'Tâches par priorité',
        'Toutes les tâches',
        'Les tâches cloturées'
    ]

    return afficheMenu(items)

def afficheMenu(items):
    for i, item in enumerate(items):
        print("{} - {}".format(i, item))

    choix = -1
    while choix < 0 or choix >= len(items):
        try:
            choix = int(input("\tVotre choix ==> "))
        except ValueError:
            continue

    return choix


class Todo():

    def __init__(self, fichier_todo = "todo.txt"):

        self.fichier_todo = fichier_todo
        self.texte = ""
        self.fichier_lu = False

    def lireFichier(self):
        try:
            print("Nous allons lire le fichier {}".format(self.fichier_todo))
            f = open(self.fichier_todo)
        except FileNotFoundError as e:
            print("Le fichier {} n'existe pas !".format(e.filename))
            try:
                f = open(self.fichier_todo, 'w+')
            except FileNotFoundError as e:
                print("Je ne peux pas créer le fichier")
                exit(2)
            except Exception as e:
                print("Erreur : {}".format(e))
            else:
                print("Le fichier a été créé")
        except Exception as e:
            print("Erreur : {}".format(e))

        self.texte = f.read()
        self.fichier_lu = True
        f.close()

    def resetFichierLu(self):
        self.texte = ""
        self.fichier_lu = False

    def fichierLu(self):
        return self.fichier_lu

    def extraireListe(self, pattern):
        #pattern = r'[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+'
        match = set(re.findall(pattern, self.texte))
        return list(match)

    def afficheListe(self, items, message):
        print(message)
        print("-"*len(message))
        for i, item in enumerate(items):
            print("\t{} - {}".format(i, item[1:]))

    def afficheListeEnvironements(self):
        if not self.fichierLu():
            self.lireFichier()
        liste = self.extraireListe(r'@[a-z0-9A-Z._-]+')
        self.afficheListe(liste ,"Liste des environnements")
        return liste

    def afficheListeProjets(self):
        if not self.fichierLu():
            self.lireFichier()
        liste = self.extraireListe(r'\+[a-z0-9A-Z._-]+')
        self.afficheListe(liste ,"Liste des projets")
        return liste

    def afficheListePriorité(self, priorité):
        print("Liste des tâches de priorité {}\n".format(priorité))
        with open(self.fichier_todo) as f:
            lines = f.readlines()
            for line in lines:
                if (line[0:3] == '('+priorité+')'):
                    print(line, end='')

    def afficheListeParClef(self, clef, msg):
        print("Liste des tâches {} {}\n".format(msg, clef))
        cherche = re.compile(clef)
        with open(self.fichier_todo) as f:
            lines = f.readlines()
            for line in lines:
                if cherche.findall(line):
                    print(line, end='')

    def afficheTachesCloturées(self):
        with open(self.fichier_todo) as f:
            lines = f.readlines()
            for line in lines:
                if (line[0].lower() == 'x'):
                    print(line, end='')

    def ajouterTache(self, tache):
        resetFichierLu()
        pass

    def cloreTache(self, tache):
        resetFichierLu()
        pass

    def augmentePrioritéTache(self, tache,):
        resetFichierLu()
        pass

    def descendPrioritéTache(self, tache):
        resetFichierLu()
        pass



if __name__ == "__main__":

    # fichier = "/Users/marc/Dropbox/Applications/pomodorotxt/todo.txt"
    ma_todo = Todo()

    while True:
        clearShell()
        choix = mainMenu()

        color(RED)
        if choix == 0:
            exit(0)
        elif choix == 1:
            # Liste des projets
            ma_todo.afficheListeProjets()
        elif choix == 2:
            # Liste des environnements
            ma_todo.afficheListeEnvironements()
        elif choix == 3:
            # Les taches par projet
            if not ma_todo.fichierLu():
                ma_todo.lireFichier()
            liste = ma_todo.extraireListe(r'\+[a-z0-9A-Z._-]+')
            choix = afficheMenu(liste)
            color(BLUE)
            ma_todo.afficheListeParClef(r'\{}'.format(liste[choix]), "du projet")
        elif choix == 4:
            # Les taches par environnement
            if not ma_todo.fichierLu():
                ma_todo.lireFichier()
            liste = ma_todo.extraireListe(r'@[a-z0-9A-Z._-]+')
            choix = afficheMenu(liste)
            color(BLUE)
            ma_todo.afficheListeParClef(liste[choix], "de l'environnement")
        elif choix == 5:
            ma_todo.afficheListePriorité('B')
        elif choix == 6:
            pass
        elif choix == 7:
            ma_todo.afficheTachesCloturées()

        color(DEFAULT)
        input("Appuyez sur <entrée> pour continuer")


#        clearShell()