import threading
from Game import *
from MyTimer import *

g = Game()

g.player.thread.start()
t = MyTimer(0.2, g.render)
t.start()
g.win.mainloop()
