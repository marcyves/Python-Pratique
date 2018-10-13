# -*- coding:Utf-8 -*-
class plateau():

    def __init__(self):
        self.grille = [[" ", " ", " "], ["O", " ", "X"], [" ", " ", " "]]

    def getPosition(self, x, y):
        return self.grille[x][y]

    def affiche(self):
        print("    1 | 2 | 3 ")
        for ligne in range(3):
            print(str(ligne + 1), end=": ")
            for colonne in range(3):
                print(" " + grille.getPosition(ligne, colonne), end=" ")
                if colonne < 2:
                    print("|", end="")
            print("")
            if ligne < 2:
                print("   ---|---|---")


# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tQuatrième essai\n")

grille = plateau()

grille.affiche()
