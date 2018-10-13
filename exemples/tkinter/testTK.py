#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def calcule(*args):
    try:
        value = float(pied.get())
        metres.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Pieds en mètres")

fenetre = ttk.Frame(root, padding="3 3 12 12")
fenetre.grid(column=0, row=0, sticky=(N, W, E, S))
fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)

pied = StringVar()
metres = StringVar()

pied_entry = ttk.Entry(fenetre, width=7, textvariable=pied)
pied_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(fenetre, textvariable=metres).grid(column=2, row=2, sticky=(W, E))
ttk.Button(fenetre, text="Calculer", command=calcule).grid(column=3, row=3, sticky=W)

ttk.Label(fenetre, text="Pieds").grid(column=3, row=1, sticky=W)
ttk.Label(fenetre, text="valent").grid(column=1, row=2, sticky=E)
ttk.Label(fenetre, text="Mètres").grid(column=3, row=2, sticky=W)

for child in fenetre.winfo_children(): child.grid_configure(padx=5, pady=5)

pied_entry.focus()
root.bind('<Return>', calcule)

root.mainloop()
