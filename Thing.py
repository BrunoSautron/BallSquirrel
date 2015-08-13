# -*- coding: utf-8 -*-

from MyThreading import *
import ImageTk

class Thing:
	def __init__(self, type="None", Y=0, X=0, sizeY=1, sizeX=1, weight=0, rebound=0.5, img=''):
		self._type = type
		self._Y = Y
		self._X = X
		self._sizeY = sizeY
		self._sizeX = sizeX
		self._weight = weight
		self._rebound = rebound
		self.diffY = 0
		self.diffX = 0
		self.img = ImageTk.PhotoImage(file = "images/" + img)
		self.thread = MyThreading(self)
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
	def getWeight(self):
		return (self._weight)
	def getRebound(self):
		return (self._rebound)

	def setX(self, X):
		self._X = X
	def setY(self, Y):
		self._Y = Y

	def forward(self, Y, X):
		self.diffX = X
		self.diffY = Y
		self._Y += Y
		self._X += X
	def moveTo(self, Y, X):
		self._Y = Y
		self._X = X
