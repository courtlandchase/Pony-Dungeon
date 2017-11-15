import Graphics, Room

class Globals:
    def __init__(self):
        self.floor = 1
        self.score = 0
        self.player = None
        self.dungeon = None
        self.eventLog = ["", "", ""]
        self.screen = None
        self.running = True
        self.menustate = ""
        self.audio = None
        self.iobj = None
        self.trap = None #to deal with issues externally

    def event(self, msg):
        self.eventLog.pop(0)
        self.eventLog.append(msg)

    def showEvents(self):
        for i in range(len(self.eventLog)):
            Graphics.addstr(2+i, Room.maxWidth+2, self.eventLog[i])

    def showState():
        pass


