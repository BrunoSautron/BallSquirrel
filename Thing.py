# -*- coding: utf-8 -*-

from MyThreading import *
import ImageTk
import math

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
		self._vY = math.sin(math.radians(self._angle)) * self._v0
		self._vX = math.cos(math.radians(self._angle)) * self._v0
		self._weight = weight
		self._rebound = rebound
		self.img = ImageTk.PhotoImage(file = "images/" + img)
		self._sizeY = self.img.height()
		self._sizeX = self.img.width()
		self.__tps = 0
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

	def setX(self, X):
		self._X = X
	def setY(self, Y):
		self._Y = Y

	def __isEnoughtFast(self):
		if (self._v0 < 0.6):
			return False
		return True

	def isMovable(self):
		if (not self.__isEnoughtFast()):
			return False

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
			self._vY = math.sin(math.radians(self._angle)) * self._v0 * self._directionY
			self._vX = math.cos(math.radians(self._angle)) * self._v0 * self._directionX
			self._Y0 = 400 - self._sizeY
			self._X0 = self._X
			if (not self.__isEnoughtFast()):
				return False

		return True

	def deplace(self, dTime):
		self.__tps += dTime
		self._X = self._vX * self.__tps + self._X0
		self._Y = (self._weight * 9.81) / 2 * (self.__tps ** 2) - self._vY * self.__tps + self._Y0
		
		if (not self.isMovable()):
			self._Y = 400 - self._sizeY
			print self.name + ": stoped at " + str(self.getTps()) + "s"
			self.__tps = 0
			self.stop()

	def shoot(self, speed, angle):
		self._v0 = speed
		self._angle = angle
		self._directionX = 1
		self._directionY = 1
		self._vY = math.sin(math.radians(self._angle)) * self._v0
		self._vX = math.cos(math.radians(self._angle)) * self._v0
		self.go()
