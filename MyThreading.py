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
		while (1):
			if (self.threaded):
				self.deplace(self.__dTime)
			time.sleep(self.__dTime)
			self.__tps += self.__dTime

	def go(self):
		self.threaded = True

	def stop(self):
		self.threaded = False
		self.__tps = 0
