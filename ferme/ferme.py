#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Petit jeu de simulation de ferme
Garanti sans OGM

(c) Marc Augier 2018
m.augier@me.com

Règles du jeu:
--------------
Un paysan possède au départ :
 - un terrain de 100 ha.
 - un stock de 1000 tonnes de blé.

Tous les ans, il plante du blé, et son terrain lui produit 2 fois ce qu'il a planté
Avec le stock de blé, il peut :
 - Le conserver.
 - Le planter dans la limite du terrain disponible (1 t/ha).
 - Acheter plus de terrain (10 t/ha)
 - Il doit aussi payer des impots (1000 tonnes)

"""

terrain = 100
stock = 1000
productivite = 2
semence = 1
cout = 10
taxe = 1000

an = 2016

def affiche_statut_ferme(an, terrain,stock):
    print ("En {}, notre ferme possède {} hectares et {} tonnes de stock de blé.".format(an,terrain, stock))

def jeu_du_fermier():
    reponse = ""
    while(reponse.upper() not in ['O', 'N', 'OUI', 'NON']):
         reponse = input("Est-ce que vous voulez continuez à jouer ? Oui/Non => ")
    if reponse.upper() == 'O':
        decision = {'jeu':True}

    else:
        decision = {'jeu':False}

    return decision

def execute_simulation(decision):
    global an, terrain, stock
    if decision['jeu']:
        print("ça joue")
        an += 1
    return

def verifie_jeu_en_cours(decision):
    return decision['jeu']


print("===============")
print("=== Ferme 2.0 ===")
print("===============")

jeu = True

while jeu:
    affiche_statut_ferme(an, terrain,stock)
    decision = jeu_du_fermier()
    execute_simulation(decision)
    jeu = verifie_jeu_en_cours(decision)

# Affiche le dernier statut

print("Le jeu est terminé")
affiche_statut_ferme(an, terrain,stock)
