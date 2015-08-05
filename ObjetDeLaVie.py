from Tkinter import *
from math import *
from scipy import *
import ImageTk
import threading

from MyTimer import *

class   ObjetDeLaVie:
    """Unobjet avec les propriete Newton"""

    def __init__(self, can, poids, coeff, py0, px0):
        self.can = can;
        self.poids = poids
        self.py0 = py0
        self.px0 = px0
        self.py = py0
        self.px = px0
        self.coeff = coeff
        self.moov = 0
        self.timer = MyTimer(0.001, self.deplace)

    def shoot(self, vitesse, angle):
        self.angle = angle
        self.vitesse = vitesse
        self.vx = cos(self.angle * 0.0174) * vitesse
        self.vy = sin(self.angle * 0.0174) * vitesse
        self.tps = 0
        self.timer.start()

    def deplace(self):
        self.moov = 1
        if (self.vitesse > 2):
            if (self.py > 340):
                self.timer.stop()
                self.px0 = self.px
                self.py0 = 340
                self.vitesse *= self.coeff
                self.shoot(self.vitesse, self.angle)

            if (self.px < -20):
                self.vx = -self.vx
                self.px = -20
                self.angle = self.angle - 2*(self.angle - 90)
                self.px0 = -20 - self.px0
            elif (self.px > 1000):
                self.vx = -self.vx
                self.px = 1000
                self.angle = self.angle - 2*(self.angle - 90)
                self.px0 = 2*1000 - self.px0

            if (self.px >= -20 and self.px <= 1000):
                self.px = self.vx*self.tps + self.px0
                self.py = ((self.poids*9.81)/2)*self.tps*self.tps - self.vy*self.tps + self.py0
                self.can.coords(self.image, self.px, self.py)
                self.tps += 0.018
        else:
            self.moov = 0
            self.timer.stop()

