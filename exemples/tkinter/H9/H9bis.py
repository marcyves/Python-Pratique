from Tkinter import *
import math
fenetre=Tk()
fenetre.title("Bonneteau")

def echange():
    global t,pos
    if pos == 0 :
        Fond.tag_raise(GB)
        pos = 1
    else :
        Fond.tag_raise(GA)
        pos = 0

    for i in range(10000) :
        t = t - math.pi/10000
        xA = 100+100*math.cos(t)
        yA = 50-50*math.sin(t)
        xB = 100+100*math.cos(t+math.pi)
        yB = 50-50*math.sin(t+math.pi)
        Fond.coords(GA,xA,yA)
        Fond.coords(GB,xB,yB)
        Fond.update()

Fond=Canvas(fenetre,width=350,height=300,bg="white")
Fond.grid(column=0,row=0)

Button(fenetre,text="ECHANGER",command=echange).grid(column=0,row=1)

t, pos = -math.pi, 0

F_GobA = PhotoImage(file="gobeletA.gif")
F_GobB = PhotoImage(file="gobeletB.gif")

GA = Fond.create_image(0,50,image=F_GobA,anchor='nw')
GB = Fond.create_image(200,50,image=F_GobB,anchor='nw')

fenetre.mainloop()

