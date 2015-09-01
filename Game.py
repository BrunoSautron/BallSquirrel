import Tkinter
import time
from MyTimer import *
from Squirrel import *
from Acorn import *

class Game:
	def __init__(self, height=500, width=1200):
		self.__inited = False
		self.__height = height
		self.__width = width
		self.__initTkinter(self.__height, self.__width)
		self.player = Squirrel("Bruno", 20, 100)
		self.acorn = [Acorn(250, 600),
				Acorn(123, 910),
				Acorn(30, 940)
				]
		self.__createImages()

	def __initTkinter(self, height, width):
		self.win = Tkinter.Tk()
		self.can = Tkinter.Canvas(self.win, width = width, height = height, bg = '#777777')
		self.can.bind("<Button-1>", self.__pointer)
		self.can.pack()
		self.can.create_line(0, 400, 1200, 400)
		self.__inited = True

	def __pointer(self, event):
		x,y = event.x, event.y
		oppose = self.player.getY() - y
		if (x < self.player.getX()):
			adjacent = self.player.getX() - x
			tanj = oppose / adjacent
			angle = 180 - math.degrees(math.atan(tanj))
			h = adjacent / math.cos(math.radians(angle)) * -1

		elif x > self.player.getX():
			adjacent = x - self.player.getX()
			tanj = oppose / adjacent
			angle = math.degrees(math.atan(tanj))
			h = adjacent / math.cos(math.radians(angle))

		speed = h * 2
		print "shoot: " + str(speed)
		if (not self.player.threaded):
			self.player.shoot(speed, angle)

	def __createImages(self):
		self.playerImg = self.can.create_image(self.player.getX() + self.player.getSizeX() / 2, self.player.getY() + self.player.getSizeY() / 2, image = self.player.img)
		print self.player.img.height()
		self.acornImg = []
		for i in range(len(self.acorn)):
			self.acornImg.append(self.can.create_image(self.acorn[i].getX() + self.acorn[i].getSizeX() / 2, self.acorn[i].getY() + self.acorn[i].getSizeY() / 2, image = self.acorn[i].img))

	def __render(self):
		diffX = self.player._X - self.player.renderX
		diffY = self.player._Y - self.player.renderY
		self.player.renderX = self.player._X
		self.player.renderY = self.player._Y
		self.can.move(self.playerImg, diffX, diffY)
		for i in range(len(self.acorn)):
			diffX = self.acorn[i]._X - self.acorn[i].renderX
			diffY = self.acorn[i]._Y - self.acorn[i].renderY
			self.acorn[i].renderX = self.acorn[i]._X
			self.acorn[i].renderY = self.acorn[i]._Y
			self.can.move(self.acornImg[i], diffX, diffY)

	def isInit(self):
		return self.__inited

	def run(self, time=0.01):
		self.player.start()
		self.player.shoot(1,270)
		for i in range(len(self.acorn)):
			self.acorn[i].start()
			self.acorn[i].randomShoot()
		self.__timer = MyTimer(time, self.__render)
		self.__timer.start()

	def stop(self):
		print "Game Stoped"
		self.player.stop()
		for i in range(len(self.acorn)):
			self.acorn[i].stop()
		self.__timer.stop()
