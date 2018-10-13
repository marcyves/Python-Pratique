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

class ferme():
    """
     La ferme
    """

    prix_terrain = 5       # Prix de l'hectare en tonne de blé
    semence = 1            # Tonnes par ha pour planter
    productivite = 2       # Production par hectare en tonnes
    taxe = 1000            # Taxe annuelle en tonne de blé

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

    def affiche_statut_ferme(self, titre):
        print ("\n\t\t%s %i" % (titre, self.an))
        print ("\t\t----------------\n")
        print ("Surface cultivable %i" % self.terrain)
        print ("Stock de blé : %i" % self.stock)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
an = 2016

def affiche_statut_ferme(an, terrain,stock):
    print("==>")
    print ("\tEn {}, notre ferme possède {} hectares et {} tonnes de stock de blé.\n".format(an,terrain, stock))

def jeu_du_fermier():
    global semence, stock, terrain

    print("* "*40)
    reponse = ""
    while(reponse.upper() not in ['O', 'N', 'OUI', 'NON']):
         reponse = input("Est-ce que vous voulez continuez à jouer ? Oui/Non => ")
    if reponse.upper() == 'O':
        decision = {'jeu':True}

        plante = -1
        while(plante < 0 or plante > stock/semence or plante > terrain):
            plante =  int(input("Combien d'hectares à semer ? ==> "))
            # On vérifie que l'on ne plante pas plus que l'on a en stock
            if (plante*semence > stock):
                print("*** Vous n'avez pas assez de stock")
                # option où le jeu force la valeur maximum
                #plante = stock/semence
            # et que notre terrain peu supporter
            if (plante > terrain):
                print ("*** Vous n'avez pas assez de terrain")
                # option où le jeu force la valeur maximum
                # plante = terrain
        decision['plante'] = plante

        # On agrandi notre propriété
        achat = -1
        while(achat < 0):
            achat = int(input("Achat de nouveau terrain (0 pour ne rien acheter) ==> "))
        decision['achat'] = achat
    else:
        decision = {'jeu':False}

    return decision

def execute_simulation(decision):
    global an, terrain, stock
    global semence, stock, terrain, taxe, prix

    if decision['jeu']:
        # Opérations de l'année
        print("- "*40)
        # Maintenant on plante et diminue le stock en conséquence
        stock = stock - decision['plante']*semence
        print("\tVous avez planté {} hectares".format(decision['plante']))
        # Comme le temps passe vite...
        an += 1
        # Moisson et calcul du stock actualisé
        recolte = decision['plante']*productivite
        stock = stock + recolte
        print("\tQui ont produit {} tonnes de blé".format(recolte))
        # Vérification de solvabilité
        achat = decision['achat']
        if achat*prix > stock:
            achat = stock/prix
            print("*** Vous avez trop demandé, limite %i" % achat)
        print("\tAchat de {} hectares pour {} tonnes de blé.".format(achat,achat*prix))
        # On paye cash
        terrain = terrain + achat
        stock = stock - achat * prix
        # On paye les impots, si on peut
        if (stock < taxe):
              print ("Vous etes en faillite")
              decision = {'jeu':False}
              stock = 0
        else:
            print("\tVous avez payé {} tonnes de blé de taxes.".format(taxe))
            stock = stock - taxe

    return decision

def verifie_jeu_en_cours(decision):
    return decision['jeu']

print("=================")
print("=== Ferme 2.0 ===")
print("=================")

jeu = True

while jeu:
    affiche_statut_ferme(an, terrain,stock)
    decision = jeu_du_fermier()
    decision = execute_simulation(decision)
    jeu = verifie_jeu_en_cours(decision)

# Affiche le dernier statut

print("Le jeu est terminé")
affiche_statut_ferme(an, terrain,stock)
