from Thing import *

class Squirrel(Thing):
	def __init__(self, name="Patrick", Y=0, X=0):
		Thing.__init__(self, type="Squirrel", weight=100, rebound=0.4, Y=Y, X=X, img='ab.gif')
		self._name = name

		print "Name: " + self._name
		self._printEnd()

	def eat(self, acorn):
		if (self.isInList(acorn)):
			print self.name + " eat one"
