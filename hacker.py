import random
import time
import curses

ASCII_RANGE = 400
DELAY_TIME = 0.01

curses.initscr()
curses.curs_set(0)

def progress():
    target = list("ACCESS GRANTED")
    output = list()
    win = curses.newwin(3, len(target)+2, 10, 32)
    win.border(0)
    for x in range(len(target)):
        y = random.randint(32, ASCII_RANGE)
        while(y in range(127, 163)):
            y = random.randint(32, ASCII_RANGE)
        output.append(chr(y))
    iterator = 0
    while(output != target):
        y = random.randint(32, ASCII_RANGE)
        while(y in range(127, 163)):
            y = random.randint(32, ASCII_RANGE)
        output[iterator] = chr(y)
        update_progress(win, output, iterator)
        time.sleep(DELAY_TIME)
        if output[iterator] == target[iterator]:
            iterator += 1
    time.sleep(1)
    for x in range(2):
        success = list("    I'm in!   ")
        for ch in range(len(success)):
            update_progress(win, success, ch)
        time.sleep(0.25)
        success = list("              ")
        for ch in range(len(success)):
            update_progress(win, success, ch)
        time.sleep(0.25)
    success = list("   I'm in!  ")
    for ch in range(len(success)):
        update_progress(win, success, ch)

def update_progress(win, output, iterator):
    display = output[iterator]
    win.addstr(1, iterator+1, "{}".format(display))
    win.refresh()


progress()

time.sleep(2)

curses.endwin()