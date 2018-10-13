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

terrain = 1000
stock = 1000
productivite = 2.1
semence = 1
cout = 10
taxe = 1150
prix = 5

an = 2016

def afficheStatutFerme(an, terrain,stock):
    print "==============="
    print "=== Ferme 2.0 ==="
    print "==============="

    print "En %i, notre ferme possède %i hectares et %i tonnes de stock de blé." % (an,terrain, stock)

jeu = True
while jeu:
    # Affiche statut de la ferme initialement
    afficheStatutFerme(an, terrain,stock)

    # Calcule une année
    plante =  input("Combien d'hectares à semer ? (0 pour terminer) ==> ")
    if (plante == 0):
        jeu = False
    else:
    # Opérations de l'année
        # On vérifie que l'on ne plante pas plus que l'on a en stock
        if (plante*semence > stock):
            print("Vous n'avez pas assez de stock")
            plante = stock/semence
        # et que notre terrain peu supporter
        if (plante > terrain):
            print ("Vous n'avez pas assez de terrain")
            plante = terrain
        # Maintenant on plante et diminue le stock en conséquence
        stock = stock - plante*semence
        print("En %i, vous avez planté %i hectares" % (an, plante))
        # Comme le temps passe vite...
        an = an + 1
        # Moisson et calcul du stock actualisé
        stock = stock + plante*productivite
        # On paye les impots, si on peut
        if (stock < taxe):
              print ("Vous etes en faillite")
              jeu = False
        else:
            stock = stock - taxe
            # On agrandi notre propriété
            print ("Vous avez %i tonnes de blé" % stock)
            achat = input("Achat de nouveau terrain ==> ")
            # Vérification de solvabilité
            if achat*prix > stock:
                achat = stock/prix
                print("Vous avez trop demandé, limite %i" % achat)
            # On paye cash
            terrain = terrain + achat
            stock = stock - achat * prix

# Affiche le dernier statut
print("Le jeu est terminé")
afficheStatutFerme(an, terrain,stock)
