from Thing import *

class Squirrel(Thing):
	def __init__(self, name, Y=0, X=0):
		Thing.__init__(self, "Squirrel", 100, 0.4, Y, X, 'ab.gif')
		self._name = name

		print "Name: " + self._name
		self._printEnd()
