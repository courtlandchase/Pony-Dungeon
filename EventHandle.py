import sys
import curses
import Help

def exit():
    curses.endwin()
    sys.exit(0)

def handleInput(globs, cmd):
    if globs.menustate == "help":
        try:
            Help.help(int(cmd))
        except:
            Help.help(0)
            
    if cmd == 'q' or cmd == 'Q':
        exit()
    if cmd == 'h':
        globs.running = not globs.running
        if globs.running:
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
    

    return "Invalid input: " + cmd + ".\nPress h for help."

def checkItems(globs, room):
    i = 0
    while i < len(room.items):
        item = room.items[i]
        if globs.player.pos.x == item.x and globs.player.pos.y == item.y:
            room.items[i].consume(globs)
            del room.items[i]
            break

        i += 1

def checkDoors(globs, room):
    nroom = room
    numdoors = len(room.doors)
    if globs.player.pos.y == 1:
        if globs.player.pos.x == 1:
            nroom = globs.dungeon[room.doors[0]]
            globs.player.pos.roomnum = room.doors[0]
            globs.player.pos.x = 2
        elif globs.player.pos.x == room.width - 2 and numdoors > 1:
            nroom = globs.dungeon[room.doors[1]]
            globs.player.pos.roomnum = room.doors[1]
            globs.player.pos.x = globs.dungeon[globs.player.pos.roomnum].width - 3

    if room != nroom:
        globs.audio.playSound("snd/door.ogg")

    return nroom
        
def handleCollisions(globs):
    room = globs.dungeon[globs.player.pos.roomnum]

    checkItems(globs, room)
    room = checkDoors(globs, room)
    checkItems(globs, room)
    
    if globs.player.pos.x < 1:
        globs.player.pos.x += 1
    elif globs.player.pos.x > room.width - 2:
        globs.player.pos.x -= 1
    elif globs.player.pos.y < 1:
        globs.player.pos.y += 1
    elif globs.player.pos.y > room.height:
        globs.player.pos.y -= 1
