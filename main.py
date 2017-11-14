#!/usr/bin/python

#import curses
from msvcrt import getch
import time
import Audio, Graphics
import Global, Dungeon
import EventHandle, Player

globs = Global.Globals()

def init():
    global globs
    globs.dungeon = Dungeon.genDungeon()
    globs.player = Player.Player()
    globs.audio = Audio.Audio()
    
    globs.event("You have entered pony dungeon in the quest for the sword of awesomeness!")
    globs.event("Press h at anytime to view a help menu.")
    globs.event("Press q at anytime to quit the game.")


def roomstr():
    global globs
    room = globs.dungeon[globs.player.pos.roomnum]
    ret = list(room.show())
    ret[globs.player.pos.y * (room.width + 1) + globs.player.pos.x] = '@'
    return "".join(ret)

def checkDeathConditions():
    #hp, food, thirst
    pass

def gameLoop():
    global globs
    
    Graphics.draw("        Pony Dungeon:\n  [Press any key to start]")
    globs.audio.playSong("snd/title.ogg")
    c = getch()
    globs.audio.stop()
    globs.audio.playSong("snd/dungeon.ogg")
    #globs.screen.timeout(1000)
    win = roomstr()
    while True:
        Graphics.draw(win)
        #if globs.running:
        #    globs.showEvents()
            
        cmd = getch()
        win = EventHandle.handleInput(globs, cmd)
        
        #todo: update win with enemy actions if needed
        EventHandle.handleCollisions(globs)
        if globs.running:
            win = roomstr()
        globs.score -= 1

        checkDeathConditions()
        
def main():
    init()
    gameLoop()

main()
