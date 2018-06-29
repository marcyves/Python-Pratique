#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programmation Orienté Objet
# Les classes

class contact():
    """
    Classe permettant de représenter un contact
    """
    def __init__(self, nom, prenom, telephone):
        self.nom       = nom
        self.prenom    = prenom
        self.telephone = telephone

    def quelNumero(self):
        return self.telephone
    
    def modifierNumero(self, tel):
        self.telephone = tel

    def quelNom(self):
        return self.nom

    def quelPrenom(self):
        return self.prenom

class contactP():

    def __init__(self, nom, prenom, telephone):
        self._nom_       = nom
        self._prenom_    = prenom
        self._telephone_ = telephone

    def quelNumero(self):
        return self.telephone

    def quelNom(self):
        return self.nom

    def quelPrenom(self):
        return self.prenom

Marc = contact("Marc","Augier","0102030405")
Sophie = contact("Sophie","Telle","0611111111")

# Accès direct aux variables
print "Le numéro du contact %s est : %s" % (Marc.nom, Marc.telephone)

Marc.modifierNumero("1111111111")

# En utilisant une methode
print "Le numéro du contact %s est : %s" % (Marc.quelNom(), Marc.quelNumero())

Paul = contactP("paul","hauchon","1")

print "Le numéro du contact %s est : %s" % (Paul._nom_, Paul._telephone_)
