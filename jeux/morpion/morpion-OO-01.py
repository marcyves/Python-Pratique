# -*- coding:Utf-8 -*-
class plateau():

    def __init__(self):
        self.grille = [[" ", " ", " "], ["O", " ", "X"], [" ", " ", " "]]

    def getPosition(self, x, y):
        return self.grille[x][y]


# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tPremier essai\n")

grille = plateau()

for ligne in range(3):
    for colonne in range(3):
        print(grille.getPosition(ligne, colonne), end="")
    print()

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tDeuxième essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(grille.getPosition(ligne, colonne), end="")
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("--|---|--")
