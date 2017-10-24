import Room

def clear(screen):
    rect = ' ' * Room.maxWidth + '\n'
    rect *= Room.maxHeight
    #todo: add lines for event log
    screen.addstr(0, 0, rect)

def draw(screen, win):
    clear(screen)
    screen.refresh()
    #todo: loop through screen when adding color
    screen.addstr(0, 0, win)
    screen.refresh()
    