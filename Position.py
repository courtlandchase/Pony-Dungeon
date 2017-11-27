class Position:
    def __init__(self, roomnum = 0, x = 0, y = 0):
        self.roomnum = roomnum
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.roomnum) + " (" + str(self.x) + ", " + str(self.y) + ")"
