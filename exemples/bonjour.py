#!/Users/marc/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
Démonstration du passage d'arguments depuis la ligne de commande
"""
def syntax():
    """
    Fonction appelée pour donner la syntaxe exacte
    """
    print("Syntax: bonjour name [-o|--obsequieux] [--output=filename]")
    print("    name : votre nom ")
    print("    -o|--obsequieux : mode obsequieux")
    print("    --output=filename : fichier en sortie")
    exit(1)

def bonjour(nom):
    """
    Fonction qui construit le texte du message standard
    """
    return "Bonjour {} !".format(nom)

def bonjour_obsequieux(nom):
    """
    Fonction qui construit le texte du message obsequieux
    """
    return "Bonjour Messire {} !".format(nom)


if __name__ == "__main__":
    import sys

    args = sys.argv
    nb_args = len(args)

    if nb_args > 3:
        syntax()

    parms = {'Nom': None, 'Obsequieux': False, 'output': None }

    for i in range(1,nb_args):
        if args[i] == '-o' or args[i] == '--obsequieux':
            parms['Obsequieux'] = True
        elif args[i][0] != '-':
            if parms['Nom'] is None:
                parms['Nom'] = args[i]
            else:
                syntax()
        else:
            output = args[i].split('=')
            if output[0] != '--output':
                syntax()
            parms['output'] = output[1]
    if parms['Nom'] is None:
        syntax()

    if parms['Obsequieux']:
        texte = bonjour_obsequieux(parms['Nom'])
    else:
        texte = bonjour(parms['Nom'])

    if parms['output'] is None:
        print(texte)
    else:
        fi = open(parms['output'], 'w')
        fi.write(texte)
        fi.close()
