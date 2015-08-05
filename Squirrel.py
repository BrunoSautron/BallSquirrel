from ObjetDeLaVie import *
from Tkinter import *
from ObjetDeLaVie import *

class 	Squirrel(ObjetDeLaVie):
    """LE squirrel"""

    def __init__(self, can, poids, coeff, py, px, img):
        ObjetDeLaVie.__init__(self, can, poids, coeff, py, px)
        self.image = self.can.create_image(self.px, self.py, image = img, anchor = NW)

