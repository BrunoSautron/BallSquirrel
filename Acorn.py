from Thing import *

class Acorn(Thing):
	def __init__(self, Y, X):
		Thing.__init__(self, "Acorn", Y, X, 1, 1, 0.5, 0, 'gland.gif')
		self._point = 10

		print "Point: " + str(self._point)
		self._printEnd()
