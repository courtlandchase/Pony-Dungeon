import threading, time
from msvcrt import getch

class AsyncInput:
    def __init__(self):
        self.hasKey = False
        self.key = 0
        self.locked = False
        self.die = False
        threading.Thread(target = keyFunc, args = (self,)).start()

    def getKey(self):
        self.locked = False
        self.hasKey = False
        return self.key

def keyFunc(iobj):
    lock = threading.Lock()
    while True:
        with lock:
            if iobj.die:
                return
            iobj.key = getch()
            iobj.hasKey = True
            iobj.locked = True
            while iobj.locked:
                time.sleep(0.01667)
