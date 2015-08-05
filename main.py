# -*- coding: utf-8 -*-

from Tkinter import *
from math import *
from scipy import *
import ImageTk
import threading

from Gland import *
from Squirrel import *



def     pointeur(event):
    x,y = event.x,event.y

    print "click"
    i = 0
    vitesse = 0
    angle = 0
    while (sq[i]):
        if (sq[i].moov == 0):
            oppose = sq[i].py0 + 30 - y
            if (x < sq[i].px0 + 30):
                adjacent = (sq[i].px0 + 30 - x)
                tanj = oppose / adjacent
                angle = 180 - math.degrees(math.atan(tanj))
                h = -adjacent / cos(angle*0.0174)
            elif (x > sq[i].px0 + 30):
                adjacent = x - sq[i].px0 + 30
                tanj = oppose / adjacent
                angle = math.degrees(math.atan(tanj))
                h = adjacent / cos(angle*0.0174)
            vitesse = h * 0.2
            if (vitesse >= 90):
                vitesse = 90
            sq[i].shoot(vitesse, angle)
        i = i + 1



#----------------PROGRAMME PRINCIPALE---------------

#creation canvas
fen = Tk()
fen.title("BallSquirrel")
frame = Frame(fen)
frame.pack()
can = Canvas(fen, width = 1200, height = 500, bg = 'white')
can.bind("<Button-1>", pointeur)
can.pack(side = TOP, padx = 0, pady = 0)

#url des images
fond_image = ImageTk.PhotoImage(file = 'images/decors.png')
gland_image = ImageTk.PhotoImage(file = 'images/gland.gif')
squirrel_image = ImageTk.PhotoImage(file = 'images/ab.gif')
sol_image = ImageTk.PhotoImage(file = 'images/bg2.gif')

#implantation image de base
fond = can.create_image(0, 0, image = fond_image, anchor = NW)
sol = can.create_image(0, 351, image = sol_image, anchor = NW)

#POID, COEFF rebon, Py, Px
gl = [Gland(can, 100, 1100, gland_image),
        Gland(can, 200, 1050, gland_image),
        0]
sq = [Squirrel(can, 2, 0.3, 340, 50, squirrel_image),
        0]
#kill de la fenetre
fen.mainloop()
