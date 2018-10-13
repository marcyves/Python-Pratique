#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Petit jeu de simulation de ferme
Garanti sans OGM

(c) Marc Augier 2016
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

an = 2000

def afficheStatutFerme(an, terrain,stock):
    print("===============")
    print("=== Ferme 2.0 ===")
    print("===============")

    print ("En {}, notre ferme possède {} hectares et {} tonnes de stock de blé.".format(an,terrain, stock))

# Affiche statut de la ferme initialement
afficheStatutFerme(an, terrain,stock)

# Calcule une année
plante = 100
stock = stock - plante*semence

an = an + 1
stock = stock + plante*productivite
stock = stock - taxe

# Affiche le nouveau statut
afficheStatutFerme(an, terrain,stock)
