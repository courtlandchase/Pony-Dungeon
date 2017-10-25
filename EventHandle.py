import Help

def handleInput(globs, cmd):
    if globs.menustate == "help":
        try:
            Help.help(int(cmd))
        except:
            Help.help(0)
            
    if cmd == 'q' or cmd == 'Q':
        return 'q'
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
