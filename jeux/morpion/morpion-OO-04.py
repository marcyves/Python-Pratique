# -*- coding:Utf-8 -*-
class plateau():

    def __init__(self):
        self.grille = [[" ", " ", " "], ["O", " ", "X"], [" ", " ", " "]]

    def getPosition(self, x, y):
        return self.grille[x][y]

    def __str__(self):
        tmp = "    1 | 2 | 3 \n"
        for ligne in range(3):
            tmp += " " * 2 + str(ligne + 1)
            for colonne in range(3):
                tmp += " " + grille.getPosition(ligne, colonne) + " "
                if colonne < 2:
                    tmp += "|"
            tmp += "\n"
            if ligne < 2:
                tmp += "   ---|---|---\n"
        return tmp


# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tCinquième essai\n")

grille = plateau()

print(grille)
