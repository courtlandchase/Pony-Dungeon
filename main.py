import curses
import time
import Global, Dungeon, Help, Graphics

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

def init():
    global globs
    cursesInit()
    globs.event("You have entered pony dungeon in the quest for the sword of awesomeness!")
    globs.event("Press h at anytime to view a help menu.")
    globs.event("Press q at anytime to quit the game.")

def gameLoop():
    global globs

    Graphics.draw(globs.screen, "        Pony Dungeon:\n  [Press any key to start]")
    c = chr(globs.screen.getch())
    while c != 'q' and c != 'Q':
        Graphics.draw(globs.screen, "test: " + c)
        c = chr(globs.screen.getch())
        
def main():
    print("loading...")
    init()
    gameLoop()

main()