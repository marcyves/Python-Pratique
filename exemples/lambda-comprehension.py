#!/Users/marc/anaconda3/bin/python3
# -*- coding: utf-8 -*-

"""
Déclinaisons autour des lambda et des compréhension de liste
"""

print("- "*20)
print("Déclinaisons autour des lambda et des compréhension de liste")
print("- "*20)

n=4

c1 = [x*2 for x in range(n)]
print("c1 = {}".format(c1))

def ff(nb):
    return nb*2

c2 = [ff(x) for x in range(n)]
print("c2 = {}".format(c2))

c3 = list(map(ff, range(n)))
print("c3 = {}".format(c3))

l = lambda x: x*2
c4 = [l(x) for x in range(n)]
print("c4 = {}".format(c4))

c5 = [(lambda x: x*2)(x) for x in range(n)]
print("c5 = {}".format(c5))

c6 = [(lambda y: (lambda x: x**y))(i) for i in range(n)]
print("c6 = {}".format(c6))
print("c6[2](3) = {}".format(c6[2](3)))
