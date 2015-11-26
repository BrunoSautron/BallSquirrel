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
		self.player = [
				Squirrel(name="Bruno", Y=20, X=100),
				]
		self.acorn = [Acorn(250, 600),
				]
		bgTkImg = ImageTk.PhotoImage(file = 'images/decors.png')
		self.bgImg = self.can.create_image(0, 0, image = bgTkImg);
		self.__listDoAction(self.player, self.__createImageThing)
		self.__listDoAction(self.acorn, self.__createImageThing)

	def __initTkinter(self, height, width):
		self.win = Tkinter.Tk()
		self.can = Tkinter.Canvas(self.win, width = width, height = height)
		self.can.bind("<Button-1>", self.__pointer)
		self.can.pack()
		self.can.create_line(0, 400, 1200, 400)
		self.__inited = True

	def __pointer(self, event):
		x,y = event.x, event.y
		for i in range(len(self.player)):
			oppose = self.player[i].getY() - y
			if (x < self.player[i].getX()):
				adjacent = self.player[i].getX() - x
				tanj = oppose / adjacent
				angle = 180 - math.degrees(math.atan(tanj))
				h = adjacent / math.cos(math.radians(angle)) * -1

			elif x > self.player[i].getX():
				adjacent = x - self.player[i].getX()
				tanj = oppose / adjacent
				angle = math.degrees(math.atan(tanj))
				h = adjacent / math.cos(math.radians(angle))
	
			speed = h * 2
			if (self.player[i].currentJump < self.player[i].maxJump):
				print "click to shoot", self.player[i].getName(), self.player[i].getType()
				self.player[i].shoot(speed, angle)

	def __createImageThing(self, thing):
		thing.setImgCan(self.can.create_image(thing.getX() + thing.getSizeX() / 2, thing.getY() + thing.getSizeY() / 2, image=thing.getImg()))

	def __putThing(self, thing):
		diffX = thing._X - thing.renderX
		diffY = thing._Y - thing.renderY
		thing.renderX = thing._X
		thing.renderY = thing._Y
		self.can.move(thing.getImgCan(), diffX, diffY)

	def __render(self):
		self.__listDoAction(self.player, self.__putThing)
		self.__listDoAction(self.acorn, self.__putThing)

	def __hitPlayer(self, thing):
		thing.eat(self.acorn)

	def isInit(self):
		return self.__inited

	def run(self, time=0.001):
		for i in range(len(self.player)):
			self.player[i].start()
			self.player[i].shoot(200, 90)
		for i in range(len(self.acorn)):
			self.acorn[i].start()
			self.acorn[i].randomShoot()
		self.__timer = MyTimer(time, self.__render)
		self.__timer.start()
		self.win.mainloop() 

	def __stopThing(self, thing):
		thing.stopThreading()

	def stop(self):
		print "Game Stoped"
		self.__listDoAction(self.player, self.__stopThing)
		self.__listDoAction(self.acorn, self.__stopThing)
		self.__timer.stop()

	def __doAction(self, thing, fn):
		fn(thing)

	def __listDoAction(self, list, fn):
		for i in range(len(list)):
			self.__doAction(list[i], fn)
