import Graphics, Room, MotionPlanner

class Globals:
    def __init__(self, name):
        self.name = name
        self.floor = 0
        self.score = 0
        self.player = None
        self.enemies = []
        self.dungeon = None
        self.eventLog = ["", "", ""]
        self.screen = None
        self.running = True
        self.menustate = ""
        self.audio = None
        self.iobj = None
        self.mp = MotionPlanner.MotionPlanner()
        self.trap = None #to deal with issues externally

    def event(self, msg):
        self.eventLog.pop(0)
        self.eventLog.append(msg)

    def showEvents(self):
        for i in range(len(self.eventLog)):
            Graphics.addstr(2+i, Room.maxWidth+2, self.eventLog[i])

    def showState(self):
        self.showEvents()
        xoff = Room.maxWidth+2
        Graphics.addstr(6, xoff, self.name)
        Graphics.addstr(7, xoff, "Score:\t" + str(self.score))
        Graphics.addstr(8, xoff, "Floor:\t" + str(self.floor))
        Graphics.addstr(9, xoff, "Hit Points:\t" + str(self.player.hp) + "/" + str(self.player.maxhp))
        Graphics.addstr(10, xoff, "Attack:\t" + str(self.player.atk))
        Graphics.addstr(11, xoff, "Hunger:\t" + str(self.player.hunger))
        Graphics.addstr(12, xoff, "Thirst:\t" + str(self.player.thirst))
        Graphics.addstr(13, xoff, "Position:\t" + str(self.player.pos))


