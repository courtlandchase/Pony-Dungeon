import random, math

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
             't' #trap
]

def moneyFunc(globs):
    globs.score += 100
    globs.event("Picked up some sand!")

def healthFunc(globs):
    if globs.player.hp == globs.player.maxhp:
        globs.player.maxhp += int(math.log(globs.floor)/math.log(2)) + 1
        globs.event("All this walking has improved your health.")
    else:
        globs.player.hp += int(globs.player.maxhp / 4)
        if globs.player.hp > globs.player.maxhp:
            globs.player.hp = globs.player.maxhp
        globs.event("Recovered some of your health.")

def weaponFunc(globs):
    globs.player.atk += int(random.random() * math.log(globs.floor+1)) + 1
    globs.event("Found a bland sword, but it's slightly better than what you have now.")

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
    globs.player.thirst -= 500
    if globs.player.thirst < 0:
        globs.player.thirst = 0
    globs.event("Drank some spilled Mnt Dew.")

def foodFunc(globs):
    globs.player.hunger -= 1000
    if globs.player.hunger < 0:
        globs.player.hunger = 0
    globs.event("Found some cheetos on the ground. Yummy!")

def pitFunc(globs):
    if globs.floor > 1:
        globs.trap = 2
        globs.event("You fell through a trap door D:")

def treasureFunc(globs):
    globs.score += 500
    globs.event("Picked up a dropped wallet.")

def trapFunc(globs):
    globs.player.hp = int(globs.player.hp/10)
    globs.event("You've fallen into a trap.")

def stairFunc(globs):
    globs.trap = 1
    globs.event("You've ventured farther into the dungeon.")

def battleFunc(globs):
    pass #maybe make it like boss fight later

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
    '>' : stairFunc,
    'E' : battleFunc
}
