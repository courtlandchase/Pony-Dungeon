import curses
import time
import Audio, Graphics
import Global, Dungeon
import EventHandle, Player

globs = Global.Globals()

def cursesInit():
    global globs
    globs.screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK) #player
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) #floor
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) #enemies
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK) #items

def roomstr():
    global globs
    room = globs.dungeon[globs.player.pos.roomnum]
    ret = list(room.show())
    ret[globs.player.pos.y * (room.width + 1) + globs.player.pos.x] = '@'
    return "".join(ret)
    
def init():
    global globs
    cursesInit()
    globs.dungeon = Dungeon.genDungeon()
    globs.player = Player.Player()
    globs.audio = Audio.Audio()
    
    globs.event("You have entered pony dungeon in the quest for the sword of awesomeness!")
    globs.event("Press h at anytime to view a help menu.")
    globs.event("Press q at anytime to quit the game.")

def gameLoop():
    global globs

    Graphics.draw(globs.screen, "        Pony Dungeon:\n  [Press any key to start]")
    globs.audio.playSong("snd/title.ogg")
    c = chr(globs.screen.getch())
    globs.audio.stop()
    globs.audio.playSong("snd/dungeon.ogg")
    globs.screen.timeout(1000)
    win = roomstr()
    while True:
        Graphics.draw(globs.screen, win)
        cmd = globs.screen.getch()
        if cmd > 0:
            win = EventHandle.handleInput(globs, chr(cmd))
        
        #todo: update win with enemy actions if needed
        EventHandle.handleCollisions(globs)
        if globs.running:
            win = roomstr()
        globs.score -= 1
        
def main():
    init()
    gameLoop()

main()
