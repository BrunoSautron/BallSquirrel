import threading
import time

class MyThreading(threading.Thread):
	def __init__(self, object):
		threading.Thread.__init__(self)
		self.terminated = False
		self._object = object

	def run(self):
		i = 0
		while (not self.terminated):
			self._object.forward(0, 10)
			time.sleep(1.0)
			i += 1
			if (i >= 10):
				self.stop()
		print "Thread of a " + self._object.getType() + " stoped"
	
	def stop(self):
		self.terminated = True
