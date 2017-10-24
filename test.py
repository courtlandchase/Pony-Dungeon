import curses, time, Graphics

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.noecho()
curses.curs_set(0)
curses.cbreak()

screen.addstr(0, 0, "hello world", curses.color_pair(1))
screen.refresh()
time.sleep(5)
Graphics.clear(screen)
screen.refresh()

time.sleep(2)
screen.addstr(0, 0, "hello world", curses.color_pair(1))
