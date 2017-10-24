class Globals:
    def __init__(self):
        self.floor = 1
        self.score = 0
        self.eventLog = ["", "", ""]
        self.screen = None

    def event(self, msg):
        self.eventLog.pop(0)
        self.eventLog.append(msg)

    def showEvents(self):
        for event in self.eventLog:
            print(event) #todo: change to curses
