import Tkinter
import time
from Squirrel import *
from Acorn import *

class Game:
	def __init__(self, height=500, width=1200):
		self.__inited = False
		self.__height = height
		self.__width = width
		self.__initTkinter(self.__height, self.__width)
		self.player = Squirrel("Bruno", 100, 200)
		self.__acorn = [Acorn(200, 1000),
				Acorn(123, 900),
				Acorn(333, 940)
				]
		self.__createImages()

	def __initTkinter(self, height, width):
		self.win = Tkinter.Tk()
		self.can = Tkinter.Canvas(self.win, width = width, height = height, bg = 'white')
		self.can.pack()
		self.__inited = True

	def __createImages(self):
		self.cImg = self.can.create_image(self.player.getX(), self.player.getY(), image = self.player.img)
		for i in range(len(self.__acorn)):
			self.can.create_image(self.__acorn[i].getX(), self.__acorn[i].getY(), image = self.__acorn[i].img)

	def render(self):
		self.can.move(self.cImg, self.player.diffX, self.player.diffY)
		self.player.diffX = 0
		self.player.diffY = 0
		print "fps"

	def isInit(self):
		return self.__inited
