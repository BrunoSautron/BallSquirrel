import ImageTk
from Tkinter import *
from ObjetDeLaVie import *

class   Gland(ObjetDeLaVie):
    """LE gland"""

    def __init__(self, can, py, px, img):
        ObjetDeLaVie.__init__(self, can, 1, 0.1, py, px)
        self.image = self.can.create_image(self.px, self.py, image = img, anchor = NW)
