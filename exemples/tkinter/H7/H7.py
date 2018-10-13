# Créé par IANTE, le 10/12/2011
from Tkinter import *
import random

def glisse() :
    for x in range(1200) :
        Fond.coords(P,x,250)
        Fond.update()

fenetre=Tk()
fenetre.title("Bataille de boules de neige")
fenetre.geometry("800x400")
Fond=Canvas(fenetre,width=800,height=400,bg="black")
Fond.place(x=0,y=0)
#Lignes
for i in range(10) :
    Fond.create_line(0,i*10,400,i*5,fill='green')
    Fond.create_line(400,i*5,800,i*10,fill='green')
#Boules de neige
for i in range(200) :
    d=random.randint(2,20)
    x=random.randint(0,800)
    y=random.randint(50,400)
    Fond.create_oval(x,y,x+d,y+d,fill='white')

fichier = PhotoImage(file="noel.gif")
P = Fond.create_image(1200, 250, image=fichier)
Button(fenetre, text="GO",command=glisse).place(x=0,y=0)

Fond.create_text(400,200,text="Bataille de boules de neige !",font=("Arial",30), fill='yellow')

fenetre.mainloop()

