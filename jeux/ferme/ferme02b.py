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


    else:
        decision = {'jeu':False}

    return decision

def execute_simulation(decision):
    global an, terrain, stock
    global semence, stock, terrain, taxe

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
        # On paye les impots, si on peut
        if (stock < taxe):
              print ("Vous etes en faillite")
              stock = 0
        else:
            print("\tVous avez payé {} euros de taxes.".format(taxe))
            stock = stock - taxe

    return

def verifie_jeu_en_cours(decision):
    return decision['jeu']

print("=================")
print("=== Ferme 2.0 ===")
print("=================")

jeu = True

while jeu:
    affiche_statut_ferme(an, terrain,stock)
    decision = jeu_du_fermier()
    execute_simulation(decision)
    jeu = verifie_jeu_en_cours(decision)

# Affiche le dernier statut

print("Le jeu est terminé")
affiche_statut_ferme(an, terrain,stock)
