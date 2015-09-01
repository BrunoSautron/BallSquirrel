from Thing import *
import random

class Acorn(Thing):
	def __init__(self, Y, X):
		Thing.__init__(self, "Acorn", 20, 0.3, Y, X, 'gland.gif')
		self._point = 10

		print "Point: " + str(self._point)
		self._printEnd()
	
	def randomShoot(self):
		speed = random.randint(150, 300)
		angle = random.randint(91, 179)
		self.shoot(speed, angle)
