import Help

def handleInput(globs, cmd):
    if cmd == 'q' or cmd == 'Q':
        return 'q'
    if cmd == 'h':
        globs.running = not globs.running
        return Help.help()
    #todo: wsad

    return "Invalid input: " + cmd + ".\nPress h for help."
