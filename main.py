from msvcrt import getch
import time, os, sys
import Audio, Graphics
import Global, Dungeon, Player
import EventHandle, Input, Enemy

if sys.version_info[0] == 2:
    globs = Global.Globals(raw_input("Enter username: "))
else:
    globs = Global.Globals(input("Enter username: "))


def init():
    global globs
    os.system("mode 200,60")
    os.system("color 5E")
    globs.dungeon = Dungeon.genDungeon()
    globs.player = Player.Player()
    globs.audio = Audio.Audio()
    
    globs.event("You have entered pony dungeon in the quest for the sword of awesomeness!")
    globs.event("Press h at anytime to view a help menu.")
    globs.event("Press q at anytime to quit the game.")

def roomstr():
    global globs
    prn = globs.player.pos.roomnum
    room = globs.dungeon[prn]
    ret = list(room.show())
    ret[globs.player.pos.y * (room.width + 1) + globs.player.pos.x] = '@'
    for e in globs.enemies:
        if e.pos.roomnum == prn:
            #todo: fix (main.py)
            ret[e.pos.y * (room.width + 1) + e.pos.x] = 'E'
    
    return "".join(ret)

def checkDeathConditions():
    global globs
    globs.player.hunger += 1
    globs.player.thirst += 1
    Graphics.draw("You ded!")
    if globs.player.hp <= 0 or globs.player.thirst >= 5000 or globs.player.hunger >= 5000:
        EventHandle.exit(globs)
    
def checkStoryConditions():
    global globs
    f = globs.floor
    if f == 0:
        s = "After being promised pizza, you've found that you've been tricked!\n"
        s += "Trapped in a dungeon full of math majors, your only chance out is\n"
        s += "finding the Sword of Awesomeness and defeating Mr. Dice, the ultimate\n"
        s += "liar.\n"
        Graphics.draw(s)
        getch()
        globs.floor += 1
    elif f == 5:
        s = "You've come far. Ahead of you is none other than Duke Shoot'em himself.\n"
        s += 'He says, "Ahead of you lies some powerful nerds. When I tried to tell them\n'
        s += "about the path to elightenment, Excel, they told me they loved graphs. But\n"
        s += "instead of linear regression, perceptrons, or k-means, they spoke of vertex\n"
        s += 'and edge sets."\n'
        s += "Tears start to form around Duke Shoot'em's eyes.\n"
        s += '"Take the sword. With it I managed to kill the Dice\'s cake that also lied."\n'
        s += "\nYou kneel before Shoot'em and equip the sword. Rainbows fly everywhere!\n"
        #todo: draw this first then make colors fly
        
        s += '"NEEEEEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIIIIIIIIIIIGGGHHHH", you roar.\n'
        Graphics.draw(s)
        getch()
        globs.player.atk += 1000
        globs.floor += 1
    elif f == 8:
        Boss.start()
        
def gameLoop():
    global globs

    Graphics.clear()
    Graphics.addstr(29, 90, "Pony Dungeon:")
    Graphics.addstr(30, 84, "[Press any key to start]")
    
    globs.audio.playSong("snd/title.ogg")
    c = getch()
    globs.audio.stop()
    globs.audio.playSong("snd/dungeon.ogg")
    win = roomstr()
    globs.iobj = Input.AsyncInput()
    
    while True:
        checkStoryConditions()
        t0 = time.time()
        Graphics.draw(win)
        if globs.running:
            globs.showState()

        while time.time() - t0 < 1:
            if globs.iobj.hasKey:
                cmd = globs.iobj.getKey()
                win = EventHandle.handleInput(globs, cmd)
                break
            
        EventHandle.handleCollisions(globs)
        if globs.running:
            win = roomstr()
            globs.score -= 1

        Enemy.update(globs)
        checkDeathConditions()
        
def main():
    init()
    gameLoop()

main()
