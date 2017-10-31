class Item:
    def __init__(self, key):
        self.key = key
        if(key == '#'):
            key = '.'
            
        self.vkey = key #viewed key
        self.x = 0
        self.y = 0
        #todo: add other properties later

itemChance = 0.015
itemList = [ '$', #sand
             '+', #HP restore
             'w', #weapon
             'i', #item
             '?', #mystery box
             '~', #water
             'f', #food
             '#', #possible pit
             'X', #treasure
             't' #trap (instant death)
]
