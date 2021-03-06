from Tkinter import *
fenetre=Tk()
fenetre.title("Bonneteau")

def echange():
    global xA, xB
    if xA == 0 :
        Fond.tag_raise(GB)
        sens = 1
    else :
        Fond.tag_raise(GA)
        sens = -1
    for i in range(200) :
        xA = xA + sens
        xB = xB - sens
        for j in range(30) :
            Fond.coords(GA,xA,50)
            Fond.coords(GB,xB,50)
            Fond.update()

Fond=Canvas(fenetre,width=350,height=300,bg="white",cursor="@aero_move.cur")
Fond.grid(column=0,row=0)

Button(fenetre,text="ECHANGER",command=echange).grid(column=0,row=1)

xA, xB = 0, 200

F_GobA = PhotoImage(file="gobeletA.gif")
F_GobB = PhotoImage(file="gobeletB.gif")

GA = Fond.create_image(xA,50,image=F_GobA,anchor='nw')
GB = Fond.create_image(xB,50,image=F_GobB,anchor='nw')

fenetre.mainloop()

