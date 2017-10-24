import random

minWidth = 20
maxWidth = 50
minHeight = 5
maxHeight = 20
RECMAX = 4

class Room:
    def __init__(self, id):
        self.id = id
        self.width = minWidth + int(random.random() * (maxWidth - minWidth))
        self.height = minHeight + int(random.random() * (maxHeight - minHeight))
        self.doors = []
        self.items = []

    def __str__(self):
        ret = "Room {id = " + str(self.id) + ", "
        ret += "width = " + str(self.width) + ", height = " + str(self.height) + "}"
        return ret

    def show(self):
        tb = '-' * self.width + "\n"
        td = '.' * self.width
        mi = '|' + '.' * (self.width - 2) + "|\n"
        mid = mi * (self.height - 2)
        ld = len(self.doors)
        if ld == 1:
            mid = '.' * (self.width - 1) + "|\n" + mid
        elif ld == 2:
            mid = '\n' + mid
            mid += mi
        elif ld == 3:
            mid = '\n' + mid
            mid += '.' * (self.width - 1) + "|\n"
        else:
            mid = '\n' + mid
            mid += '.' * self.width + '\n'

        ret = list(tb + td + mid + tb)
         
        for item in self.items:
            ret[item.y * (self.width + 1) + item.x] = item.key

        ret = "".join(ret)
            
        return ret
        

