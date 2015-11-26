# -*- coding: utf-8 -*-

from MyThreading import *
import ImageTk
import math
import random

class Thing(MyThreading):
	def __init__(self, type="None", weight=1, rebound=0.5, Y=0, X=0, img=''):
		MyThreading.__init__(self)
		self._type = type
		self._Y = Y
		self._X = X
		self.renderY = Y
		self.renderX = X
		self._Y0 = Y
		self._X0 = X
		self._v0 = 0
		self._directionY = 1
		self._directionX = 1
		self._angle = 45
		self.maxJump = 4
		self.currentJump = 0
		self._vY = math.sin(math.radians(self._angle)) * self._v0
		self._vX = math.cos(math.radians(self._angle)) * self._v0
		self._weight = weight
		self._rebound = rebound
		self.__img = ImageTk.PhotoImage(file = "images/" + img)
		self.__imgCan = 0
		self._sizeY = self.__img.height()
		self._sizeX = self.__img.width()
		self.__tps = 0
		self._isMoving = False
		self.beginThreading()
		print "╔= " + self._type + " =="
		print "Weight: " + str(self._weight)
		print "Rebound: " + str(self._rebound)
		print "Positions: " + str(self._Y) + "/" + str(self._X)
		print "Size: " + str(self._sizeY) + "*" + str(self._sizeX)

	def _printEnd(self):
		str = "╚="
		for i in range(len(self._type) + 2):
			str += "="
		str += "=="
		print str

	def getName(self):
		return (self._name)
	def getType(self):
		return (self._type)
	def getX(self):
		return (self._X)
	def getY(self):
		return (self._Y)
	def getX0(self):
		return (self._X0)
	def getY0(self):
		return (self._Y0)
	def getSizeX(self):
		return (self._sizeX)
	def getSizeY(self):
		return (self._sizeY)
	def getWeight(self):
		return (self._weight)
	def getRebound(self):
		return (self._rebound)
	def getImg(self):
		return (self.__img)
	def getImgCan(self):
		return (self.__imgCan)

	def setX(self, X):
		self._X = X
	def setY(self, Y):
		self._Y = Y
	def setImgCan(self, imgCan):
		self.__imgCan = imgCan

	def __isEnoughtFast(self):
		if (self._v0 < 0.6):
			print "Because not enought fast",
			return False
		return True

	def isMovable(self):

		if (self._X < 0):
			self._directionX *= -1
			self._vX = math.cos(math.radians(self._angle)) * self._v0 * self._directionX
			self._X = 0
			self._X0 = self._X - self._X0

		if (self._X + self._sizeX > 1200):
			self._directionX *= -1
			self._vX = math.cos(math.radians(self._angle)) * self._v0 * self._directionX
			self._X = 1200 - self._sizeX
			self._X0 = self._X * 2 - self._X0

		if (self._Y + self._sizeY > 400):

			self.__tps = 0
			self._v0 *= self._rebound
			if (not self.__isEnoughtFast()):
				self._Y = 400 - self._sizeY
				return False
			if (self._angle > 180):
				self._angle = self._angle - 2 *(self._angle - 180)
			elif (self._angle < 0):
				self._angle *= -1
			elif (self._angle == -90 or self._angle == 270):
				self._angle == 90

			self._vY = math.sin(math.radians(self._angle)) * self._v0 * self._directionY
			self._vX = math.cos(math.radians(self._angle)) * self._v0 * self._directionX
			self._Y0 = 400 - self._sizeY
			self._X0 = self._X

		return True

	def deplace(self, dTime):
		self.__tps += dTime
		self._X = self._vX * self.__tps + self._X0
		self._Y = (self._weight * 9.81) / 2 * (self.__tps ** 2) - self._vY * self.__tps + self._Y0
		
		if (not self.isMovable()):
			self._Y = 400 - self._sizeY
			print self.name + ": reset after at " + str(self.getTps()) + "s"
			self.__tps = 0
			self.currentJump = 0
			self._isMoving = False
			self.cancelThreading()

	def shoot(self, speed=100, angle=45):
		print "Begin Shoot"
		speed += random.randint(0, 300);
		self.currentJump += 1
		self._X0 = self._X
		self._Y0 = self._Y
		self.__tps = 0
		self._v0 = speed
		self._angle = angle
		self._directionX = 1
		self._directionY = 1
		self._vY = math.sin(math.radians(self._angle)) * self._v0
		self._vX = math.cos(math.radians(self._angle)) * self._v0
		self._v = 0
		self._isMoving = True
		self.resetThreading()

	def isIn(self, thing):
		for y in range(int(self._Y), int(self._Y + self._sizeY - 1)):
			for x in range(int(self._X), int(self._X + self._sizeX - 1)):
				if (y >= thing.getY() and y <= thing.getY() + thing.getSizeY() and x >= thing.getX() and x <= thing.getX() + thing.getSizeX()):
					return True
		return False

	def isInList(self, things):
		for i in range(len(things)):
			if (self.isIn(things[i])):
				return True
		return False
