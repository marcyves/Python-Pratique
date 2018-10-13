#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def Calcule(*var):
    try:
        valeur = float(pied.get())
        metre.set((0.3048*valeur*10000 + 0.5)/10000)
    except ValueError:
        pass

root = Tk()
root.title("Ma fenêtre")

fen = ttk.Frame(root, padding="3 3 12 12")
fen.grid(column=0, row=0, sticky=(N,W,E,S))
fen.columnconfigure(0,weight=1)
fen.rowconfigure(0,weight=1)

pied = StringVar()
metre = StringVar()

pied_fen = ttk.Entry(fen, width=3, textvariable=pied)
pied_fen.grid(column=2, row=1, sticky=(W,E))

ttk.Label(fen, textvariable=metre).grid(column=2, row=2,sticky=W)
ttk.Label(fen, text="Pieds").grid(column=3, row=1, sticky=W)
ttk.Label(fen, text="Mètres").grid(column=3, row=2, sticky=W)
ttk.Label(fen, text="Calculateur produit par Python").grid(column=2, row=10, sticky=S)

ttk.Button(fen, text="Calcule", command=Calcule).grid(column=3, row=3,sticky=E)

pied_fen.focus()

root.mainloop()