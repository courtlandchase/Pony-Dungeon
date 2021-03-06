import sys
import Help, Dungeon, Position, Save, Enemy

def exit(globs):
    Save.save(globs)
    sys.exit(0)

def handleInput(globs, cmd):
    if globs.menustate == "help":
        if cmd == 'h':
            globs.menustate = ""
            globs.running = True
            return
            
        try:
            return Help.help(int(cmd))
        except:
            return Help.help(0)

    globs.running = True
            
    if cmd == 'q' or cmd == 'Q':
        globs.iobj.die = True
        exit(globs)
    if cmd == 'h':
        globs.running = not globs.running
        if not globs.running:
            globs.menustate = "help"
            return Help.help()
        else:
            globs.menustate = ""
            return
    if cmd == 'w':
        globs.player.pos.y -= 1
        return
    if cmd == 's':
        globs.player.pos.y += 1
        return
    if cmd == 'a':
        globs.player.pos.x -= 1
        return
    if cmd == 'd':
        globs.player.pos.x += 1
        return
    
    globs.running = False
    return "Invalid input: " + str(cmd) + ".\nPress h for help."

def checkItems(globs, room):
    i = 0
    while i < len(room.items):
        item = room.items[i]
        if globs.player.pos.x == item.x and globs.player.pos.y == item.y:
            room.items[i].consume(globs)
            if room.items[i].removes:
                del room.items[i]
            break

        i += 1

def checkDoors(globs, room):
    nroom = room
    numdoors = len(room.doors)
    if globs.player.pos.y == 1:
        if globs.player.pos.x == 1:
            nroom = globs.dungeon[room.doors[0]]
        elif globs.player.pos.x == room.width - 2 and numdoors > 1:
            nroom = globs.dungeon[room.doors[1]]
    elif globs.player.pos.y == room.height:
        if globs.player.pos.x == 1 and numdoors > 2:
            nroom = globs.dungeon[room.doors[2]]
        elif globs.player.pos.x == room.width - 2 and numdoors > 3:
            nroom = globs.dungeon[room.doors[3]]
            
    if room != nroom:
        globs.player.pos.roomnum = nroom.id
        
        for i in range(len(nroom.doors)):
            if room.id == nroom.doors[i]:
                break

        if i == 0 or i == 2:
            globs.player.pos.x = 2
        else:
            globs.player.pos.x = nroom.width - 3

        if i == 0 or i == 1:
            globs.player.pos.y = 1
        else:
            globs.player.pos.y = nroom.height
            
        globs.audio.playSound("snd/door.ogg")

    return nroom
        
def handleCollisions(globs):
    room = globs.dungeon[globs.player.pos.roomnum]

    checkItems(globs, room)
    rt = False
    if globs.trap == 1:
        globs.floor += 1
        rt = True
    elif globs.trap == 2:
        globs.floor -= 1
        rt = True

    if rt:
        globs.dungeon = Dungeon.genDungeon()
        globs.player.pos = Position.Position(0, 2, 1)
        globs.trap = 0
        Enemy.genEnemies(globs)
        return
        
    room = checkDoors(globs, room)

    if globs.player.pos.x < 1:
        globs.player.pos.x += 1
    elif globs.player.pos.x > room.width - 2:
        globs.player.pos.x -= 1
    elif globs.player.pos.y < 1:
        globs.player.pos.y += 1
    elif globs.player.pos.y > room.height:
        globs.player.pos.y -= 1
