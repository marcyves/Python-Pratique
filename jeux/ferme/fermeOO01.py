#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Petit jeu de simulation de ferme
Garanti sans OGM

(c) Marc Augier 2016
m.augier@me.com

Règles du jeu:
--------------
Un paysan possède un terrain de 100h au départ.
Tous les ans, il plante du blé, et son terrain lui produit 2 fois ce qu'il a planté
Avec le stock de blé, il peut :
 - Le conserver
 - Le planter dans la limite du terrain
 - Acheter plus de terrain

"""

#

class ferme():
    """
     La ferme
    """
    prix_terrain = 5       # Prix de l'hectare en tonne de blé
    semence = 1           # Tonnes par ha pour planter
    productivite = 2.1    # Production par hectare en tonnes
    taxe = 1150             # Taxe annuelle en tonne de blé

    def __init__(self,t = 1000,s = 500, a=1900):
        self.terrain = t
        self.stock   = s
        self.an      = a

    def planteSemences(self,plante):
        # On vérifie que l'on ne plante pas plus que l'on a en stock
        if (plante * ferme.semence > self.stock):
            print("\t-- Vous n'avez pas assez de stock pour planter %i hectares" % plante)
            plante = self.stock/ferme.semence
        # et que notre terrain peu supporter
        if (plante > self.terrain):
            print("\t-- Vous n'avez pas assez de terrain pour planter %i hectares" % plante)
            plante = self.terrain
        # Maintenant on plante et diminue le stock en conséquence
        self.stock = self.stock - plante * ferme.semence
        print("En %i, vous avez planté %i hectares." % (self.an, plante))
        return plante

    def moissonne(self, plante):
        # Moisson
        self.stock = self.stock + plante * ferme.productivite

    def taxes(self):
        # Et on paye les impots
        self.stock = self.stock - ferme.taxe
        if (self.stock < 0):
            self.stock = 0
            return False
        else:
            print("Stock en fin de production : %i tonnes" % self.stock)
            self.an += 1
            return True

    def acheteTerrain(self,achat):
        # On vérifie que l'on a de quoi Acheter
        if (self.stock < achat * ferme.prix_terrain):
            print("\tVous n'avez pas assez de blé pour acheter %i hectares" % achat)
            achat = self.stock/ferme.prix_terrain
            print("\tVous ne pouvez acheter que %i hectares" % achat)
        self.stock = self.stock - achat * ferme.prix_terrain
        self.terrain = self.terrain + achat

    def AfficheBilan(self, titre):
        print ("\n\t\t%s %i" % (titre, self.an))
        print ("\t\t----------------\n")
        print ("Surface cultivable %i" % self.terrain)
        print ("Trésorerie : %i" % self.stock)

jeu = True

MaFerme = ferme(1000, 3000, 2016)
MaFerme.AfficheBilan("Mon exploitation au lancement en ")

while (jeu):
    plante = input("Combien vous plantez d'hectares cette année ? (0 = stop) --> ")
    if (plante == 0):
        jeu = False
    else:
    # Opérations de l'année
        MaFerme.moissonne(MaFerme.planteSemences(plante))
        jeu = MaFerme.taxes()
        if (jeu):
            achat = input("Agrandir le terrain de --> ")
            MaFerme.acheteTerrain(achat)
            MaFerme.AfficheBilan("Le bilan de mon exploitation en ")

MaFerme.AfficheBilan("C'est terminé --> ")
