# -*- coding:Utf-8 -*-

grille = [[" ", " ", " "], ["O", " ", "X"], [" ", " ", " "]]

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tPremier essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(grille[ligne][colonne], end="")
    print()

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tDeuxième essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(grille[ligne][colonne], end="")
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("--|---|--")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tTroisième essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(" " + grille[ligne][colonne], end=" ")
        if colonne < 2:
            print("|", end="")
    print("")
    if ligne < 2:
        print("---|---|---")
# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tQuatrième essai\n")

print("    1 | 2 | 3 ")
for ligne in range(3):
    print(str(ligne + 1), end=": ")
    for colonne in range(3):
        print(" " + grille[ligne][colonne], end=" ")
        if colonne < 2:
            print("|", end="")
    print("")
    if ligne < 2:
        print("   ---|---|---")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tCinquième essai\n")


def affiche(une_grille):
    print("    1 | 2 | 3 ")
    for ligne in range(3):
        print(str(ligne + 1), end=": ")
        for colonne in range(3):
            print(" " + une_grille[ligne][colonne], end=" ")
            if colonne < 2:
                print("|", end="")
        print("")
        if ligne < 2:
            print("   ---|---|---")


affiche(grille)
