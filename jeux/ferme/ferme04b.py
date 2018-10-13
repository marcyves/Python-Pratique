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
        # On plante et diminue le stock en conséquence
        self.stock = self.stock - plante * ferme.semence

    def moissonne(self, plante):
        # Comme le temps passe vite...
        self.an += 1
        # Moisson
        recolte = plante * ferme.productivite
        self.stock = self.stock + recolte

        return recolte

    def taxes(self):
        # Et on paye les impots
        print("stock avant impot {}".format(self.stock))
        self.stock = self.stock - ferme.taxe
        if (self.stock < 0):
            self.stock = 0
            return True
        else:
            print("\tVous avez payé {} tonnes de blé de taxes.".format(ferme.taxe))
            print("Stock en fin de production : %i tonnes" % self.stock)
            return False

    def acheteTerrain(self,achat):
        # On vérifie que l'on a de quoi Acheter
        if (self.stock < achat * ferme.prix_terrain):
            print("\tVous n'avez pas assez de blé pour acheter %i hectares" % achat)
            achat = self.stock/ferme.prix_terrain
            print("\tVous ne pouvez acheter que %i hectares" % achat)
        self.stock = self.stock - achat * ferme.prix_terrain
        self.terrain = self.terrain + achat

    def affiche_statut_ferme(self, titre):
        print("==> {}".format(titre))
        print ("\tEn {}, notre ferme possède {} hectares et {} tonnes de stock de blé.\n".format(self.an,self.terrain, self.stock))

    def jeu_du_fermier(self):
        print("* "*40)
        reponse = ""
        while(reponse.upper() not in ['O', 'N', 'OUI', 'NON']):
             reponse = input("Est-ce que vous voulez continuez à jouer ? Oui/Non => ")
        if reponse.upper() == 'O':
            decision = {'jeu':True}

            plante = -1
            while(plante < 0 or plante > self.stock/ferme.semence or plante > self.terrain):
                plante =  int(input("Combien d'hectares à semer ? ==> "))
                # On vérifie que l'on ne plante pas plus que l'on a en stock
                if (plante*ferme.semence > self.stock):
                    print("*** Vous n'avez pas assez de stock")
                    # option où le jeu force la valeur maximum
                    #plante = stock/semence
                # et que notre terrain peu supporter
                if (plante > self.terrain):
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

MaFerme = ferme(1000, 3000, 2016)

print("=================")
print("=== Ferme 2.0 ===")
print("=================")

jeu = True

while jeu:
    MaFerme.affiche_statut_ferme("Bilan de l'exploitation")
    decision = MaFerme.jeu_du_fermier()

    if decision['jeu']:
        # Opérations de l'année
        print("- "*40)
        # Maintenant on plante et diminue le stock en conséquence
        MaFerme.planteSemences(decision['plante'])
        print("\tVous avez planté {} hectares".format(decision['plante']))
        # Moisson et calcul du stock actualisé
        recolte = MaFerme.moissonne(decision['plante'])
        print("\tQui ont produit {} tonnes de blé".format(recolte))
        # Vérification de solvabilité
        MaFerme.acheteTerrain(decision['achat'])
        # On paye les impots, si on peut
        if (MaFerme.taxes()):
              print ("*** Vous etes en faillite")
              decision = {'jeu':False}

    jeu = decision['jeu']

# Affiche le dernier statut
MaFerme.affiche_statut_ferme("Le jeu est terminé")
