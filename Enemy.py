import Player, Position
import random

ENEMY_RATE = 1

class Enemy(Player.Player):
    def __init__(self, globs):
        Player.Player.__init__(self) #super().__init__()
        self.hp = 10 + 2 * globs.floor
        self.atk = int(globs.player.atk - globs.floor / 2.0 + (globs.floor * random.random()))
        self.path = []
        self.spawn(globs)
    
    def spawn(self, globs):
        dlen = len(globs.dungeon)
        rn = int(random.random() * dlen)
        c = 2 + int(random.random() * (globs.dungeon[rn].width - 4))
        r = 2 + int(random.random() * (globs.dungeon[rn].height - 4))
        self.pos = Position.Position(rn, c, r)
        if self.pos == globs.player.pos:
            rn += 1
            if rn > dlen:
                rn = 0

            self.pos = Position.Position(rn, c, r)
        
    def update(self, globs):
        npos = globs.mp.nextStep(globs, self.pos)
        if npos == self.pos:
            globs.player.hp -= 1 #self.atk
        
        self.pos = npos

def genEnemies(globs):
    globs.enemies = []
    numEnemies = int(ENEMY_RATE * (globs.floor / 2) + 1)
    for _ in range(numEnemies):
        globs.enemies.append(Enemy(globs))

def update(globs):
    for i in range(len(globs.enemies)):
        if globs.enemies[i].hp:
            globs.enemies[i].update(globs)
        else:
            del globs.enemies[i]
