from Tkinter import *
fenetre=Tk()
fenetre.title("Coccinelle")

def haut():
    global y
    y = max (0,y-10)
    Fond.coords(coc,x,y)
    Fond.itemconfig(coc,image=F_CocH)

def bas():
    global y
    y = min (400,y+10)
    Fond.coords(coc,x,y)
    Fond.itemconfig(coc,image=F_CocB)

def gauche():
    global x
    x = max (0,x-10)
    Fond.coords(coc,x,y)
    Fond.itemconfig(coc,image=F_CocG)

def droite():
    global x
    x = min (400,x+10)
    Fond.coords(coc,x,y)
    Fond.itemconfig(coc,image=F_CocD)


Fond=Canvas(fenetre,width=400,height=400,bg="white")
Fond.grid(column=0,row=0, rowspan = 4)

Button(fenetre,text="HAUT",command=haut).grid(column=1,row=0)
Button(fenetre,text="BAS",command=bas).grid(column=1,row=1)
Button(fenetre,text="GAUCHE",command=gauche).grid(column=1,row=2)
Button(fenetre,text="DROITE",command=droite).grid(column=1,row=3)

x, y = 200, 200

F_CocH = PhotoImage(file="cocH.gif")
F_CocB = PhotoImage(file="cocB.gif")
F_CocG = PhotoImage(file="cocG.gif")
F_CocD = PhotoImage(file="cocD.gif")

coc = Fond.create_image(x,y,image=F_CocH)

fenetre.mainloop()

