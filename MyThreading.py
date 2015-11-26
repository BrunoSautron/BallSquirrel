import threading
import time
from MyTimer import *

class MyThreading(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.threaded = False
		self.__tps = 0
		self.__dTime = 0.001

	def getTps(self):
		return self.__tps

	def run(self):
		i = 0
		while (1):
			if (self._isMoving):
				self.deplace(self.__dTime)
				#print self._isMoving
			time.sleep(self.__dTime)
			self.__tps += self.__dTime
			i += 1

	def beginThreading(self):
		self.threaded = True

	def resetThreading(self):
		self.beginThreading()
		self.__tps = 0

	def cancelThreading(self):
		self.__tps = 0;

	def stopThreading(self):
		self.threaded = False
		self.__tps = 0
