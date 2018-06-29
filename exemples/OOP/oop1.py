#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programmation Orienté Objet
# Les classes

class contact():
    """
    Classe qui représente un contact
    
    """
    def __init__(self, prenom, nom, telephone):
        self.nom    = nom
        self.prenom = prenom
        self.telephone = telephone
    
    def quelNumero(self):
        return self.telephone
    
    def quelNom(self):
        return self.nom
    
    def changeNumero(self, tel):
        self.telephone = tel


Marc = contact("Marc","Augier","0102030405")
Sophie = contact("Sophia", "Antipolis", "0606060606")


print "Le numero du contact %s est : %s" % (Sophie.quelNom(), Sophie.quelNumero())

Marc.changeNumero("1111111111")

print "Le numero du contact %s est : %s" % (Marc.quelNom(), Marc.quelNumero())
