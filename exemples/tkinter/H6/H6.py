from Tkinter import *

fenetre=Tk()
fenetre.title("Go !")
fenetre.geometry("1000x680")
Fond=Canvas(fenetre,width=1000,height=680,bg="#BBBBF9")
Fond.place(x=0,y=0)

F_Chat = PhotoImage(file="chat.gif")
F_Souris = PhotoImage(file="souris.gif")
F_Echelle = PhotoImage(file="echelle.gif")
F_Pancake=PhotoImage(file="pancake.gif")
F_Acier=PhotoImage(file="acier.gif")
F_Brique=PhotoImage(file="brique.gif")

x, y = 0, 0
fichier = open("niveau.txt")
for ligne in fichier :
    for i in range(25) :
        case = ligne[i]
        if case == 'X' :
            Fond.create_image(x,y,image=F_Acier,anchor="nw")
        if case == 'H' :
            Fond.create_image(x,y,image=F_Echelle,anchor="nw")
        if case == 'T' :
            Fond.create_image(x,y,image=F_Brique,anchor="nw")
        if case == 'C' :
            Fond.create_image(x,y,image=F_Chat,anchor="nw")
        if case == 'S' :
            Fond.create_image(x,y,image=F_Souris,anchor="nw")
        if case == 'P' :
            Fond.create_image(x,y,image=F_Pancake,anchor="nw")
        x = x + 40
    x = 0
    y = y + 40
fichier.close()

fenetre.mainloop()
