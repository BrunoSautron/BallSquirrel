import threading
from Game import *

def main():
	g = Game()
	g.run()
	g.win.mainloop()
	g.stop()
	

if __name__ == "__main__":
	main()
