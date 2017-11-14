import random

class Item:
    def __init__(self, key):
        self.key = self.vkey = key
        if key == '#':
            self.vkey = '.'
            
        self.x = 0
        self.y = 0
        self.removes = True
        self.consume = itemFunction[key]

itemChance = 0.015
itemList = [ '$', #sand
             '+', #HP restore
             'w', #weapon
             '?', #mystery box
             '~', #water
             'f', #food
             '#', #pit
             'X', #treasure
             't' #trap (instant death)
]

def moneyFunc(globs):
    globs.score += 100

def healthFunc(globs):
    globs.player.hp += globs.player.maxhp / 10

def weaponFunc(globs):
    globs.player.atk += int(random.random() * (globs.floor+1)) + 1

def randomFunc(globs):
    f = int(random.random() * 8)
    if f == 0:
        moneyFunc(globs)
    elif f == 1:
        healthFunc(globs)
    elif f == 2:
        weaponFunc(globs)
    elif f == 3:
        waterFunc(globs)
    elif f == 4:
        foodFunc(globs)
    elif f == 5:
        pitFunc(globs)
    elif f == 6:
        treasureFunc(globs)
    elif f == 7:
        trapFunc(globs)
    
def waterFunc(globs):
    globs.player.thirst -= 10
    if globs.player.thirst < 0:
        globs.player.thirst = 0

def foodFunc(globs):
    globs.player.hunger -= 10
    if globs.player.hunger < 0:
        globs.player.hunger = 0

def pitFunc(globs):
    globs.floor -= 1
    if globs.floor < 1:
        globs.floor = 1
    else:
        pass #send trap to globs

def treasureFunc(globs):
    globs.score <<= 1

def trapFunc(globs):
    globs.player.hp /= 10

def stairFunc(globs):
    globs.trap = 1
    
itemFunction = {
    '$' : moneyFunc,
    '+' : healthFunc,
    'w' : weaponFunc,
    '?' : randomFunc,
    '~' : waterFunc,
    'f' : foodFunc,
    '#' : pitFunc,
    'X' : treasureFunc,
    't' : trapFunc,
    '>' : stairFunc
}
