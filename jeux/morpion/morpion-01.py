# -*- coding:Utf-8 -*-

grille = [" ", " ", " ", "O", " ", "X", " ", " ", " "]

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tPremier essai\n")

for position in range(9):
    print(str(position) + ": " + grille[position], end=" ")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tDeuxième essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(
            str(ligne + 2 * ligne + colonne)
            + ": "
            + grille[ligne + 2 * colonne + colonne],
            end="",
        )
    print("")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tTroisième essai\n")

for ligne in range(3):
    for colonne in range(3):
        print(
            str(ligne + 2 * ligne + colonne)
            + ": "
            + grille[ligne + 2 * colonne + colonne],
            end="",
        )
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("-----|------|-----")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tQuatrième essai\n")


def coordonnees(x, y):
    return x + 2 * x + y


for ligne in range(3):
    for colonne in range(3):
        print(
            str(coordonnees(ligne, colonne))
            + ": "
            + grille[coordonnees(ligne, colonne)],
            end="",
        )
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("-----|------|-----")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tCinquième essai\n")


def coordonnees(x, y):
    return x + 2 * x + y


print("   1 | 2 | 3 ")
for ligne in range(3):
    print(str(ligne + 1), end=": ")
    for colonne in range(3):
        print(grille[coordonnees(ligne, colonne)], end="")
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("  ---|---|----")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tSixième essai\n")


def plateau(une_grille, x, y):
    return une_grille[x + 2 * x + y]


print("   1 | 2 | 3 ")
for ligne in range(3):
    print(str(ligne + 1), end=": ")
    for colonne in range(3):
        print(plateau(grille, ligne, colonne), end="")
        if colonne < 2:
            print(" | ", end="")
    print("")
    if ligne < 2:
        print("  ---|---|----")

# - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n\tSeptième essai\n")


def plateau(une_grille, x, y):
    return une_grille[x + 2 * x + y]


def affiche(une_grille):
    print("   1 | 2 | 3 ")
    for ligne in range(3):
        print(str(ligne + 1), end=": ")
        for colonne in range(3):
            print(plateau(une_grille, ligne, colonne), end="")
            if colonne < 2:
                print(" | ", end="")
        print("")
        if ligne < 2:
            print("  ---|---|----")


affiche(grille)
