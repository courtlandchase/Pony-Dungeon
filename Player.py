import Position

class Player:
    def __init__(self):
        self.pos = Position.Position()
        self.items = []
        self.maxhp = 10
        self.atk = 1
        self.hp = self.maxhp
        self.hunger = 0
        self.thirst = 0
