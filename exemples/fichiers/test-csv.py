import csv

fichier = "test.csv"

fi = open(fichier, "w", newline='')

csv.register_dialect('test',delimiter=';')
mon_csv = csv.writer(fi, 'test')

mon_csv.writerow(('Nom','Prénom','Téléphone'))
mon_csv.writerow(('Hauchon', 'Paul', '0102030405'))
mon_csv.writerow(('Enfaillite', 'Mélusine', '0305400505'))

fi.close()

fi2 = open(fichier,"r")
"""
texte = fi2.read()
print(texte)
fi2.close()
"""

# Lecture ligne à ligne
"""
mon_csv = csv.reader(fi2)

for ligne in mon_csv:
    print(ligne)
"""
# Lecture par dictionnaire
mon_csv = csv.DictReader(fi2,dialect='test')

for ligne in mon_csv:
    print(dict(ligne))
    print(ligne['Nom'],ligne['Prénom'])
