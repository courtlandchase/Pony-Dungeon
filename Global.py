class Globals:
    def __init__(self):
        self.floor = 1
        self.score = 0
        self.eventLog = ["", "", ""]
        self.screen = None
        self.running = True

    def event(self, msg):
        self.eventLog.pop(0)
        self.eventLog.append(msg)

    def showEvents(self):
        ret = ""
        for event in self.eventLog:
            ret += event + "\n"

        return ret
