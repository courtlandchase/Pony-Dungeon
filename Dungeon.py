import random
import Room, Position, Item

maxRooms = 20
minRooms = 13

def genRandItems(room):
    i = 3
    while i < room.width - 2:
        j = 2
        while j < room.height - 2:
            if i == 4 and j == 2:
                j += 1
                continue
            
            if(random.random() <= Item.itemChance):
                item = Item.Item(random.choice(Item.itemList))
                item.x, item.y = i, j
                room.items.append(item)
            j += 1
        i += 1

def genDungeon():
    numrooms = minRooms + int(random.random() * (maxRooms - minRooms))
    stairsloc = Position.Position(int(random.random() * numrooms), 4, 2)
    roomIDs = list(range(numrooms))
    
    rooms = []
    for i in roomIDs:
        room = Room.Room(i)
        if i > 0:
            room.doors.append(i - 1)

        if i < len(roomIDs) - 1:
            room.doors.append(i + 1)
        
        rooms.append(room)

    extra = int(random.random() * 4) + 2
    extra += extra & 1
    extraConns = random.sample(roomIDs, extra)
    
    i = 0
    while i+1 < len(extraConns):
        n = extraConns[i]
        m = extraConns[i+1]

        if(m in rooms[n].doors or n in rooms[m].doors):
            i += 1
            continue
        
        rooms[n].doors.append(m)
        rooms[m].doors.append(n)
        i += 1

    for room in rooms:
        genRandItems(room)

    stairs = Item.Item('>')
    stairs.x = stairsloc.x
    stairs.y = stairsloc.y
    rooms[stairsloc.roomnum].items.append(stairs)
        
    return rooms
