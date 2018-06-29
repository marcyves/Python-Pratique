#! /usr/bin/python
# -*- coding: utf-8 -*-

class Animal():
    def __init__(self):
        print("Nouvel animal créé")

    def queSuisJe(self):
        print("Je suis un animal")

    def mange(self):
        print("En train de manger")


class Chien(Animal):
    espece = "mammifère"
    nb = 0

    def __init__(self, race, nom, vaccin=False, taille=30):
        Animal.__init__(self)
        Chien.nb += 1
        print("Un nouveau chien est créé")
        self.race = race
        self.nom = nom
        self.vaccin = vaccin
        self.taille = taille

    def __str__(self):
        return "Je suis le chien {} de race {}".format(self.nom, self.race)

    def __del__(self):
        print("Le chien a disparu")

    def __len__(self):
        return self.taille

    @staticmethod
    def Combien():
        return Chien.nb

    def queSuisJe(self):
        print("Je suis un chien")

    def Aboyer(self):
        print("Ouah ouah !")

    def EstVacciné(self):
        return self.vaccin

    def Vaccination(self):
        self.vaccin = True


sam = Chien('Labrador','Sam')
medor = Chien('Husky', 'Medor')
print(Chien.Combien())
toutou = Chien('Caniche', 'Toutou')
print(Chien.Combien())
