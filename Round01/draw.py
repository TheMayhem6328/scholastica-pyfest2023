import unicurses as curses

# Initialize curses UI root
stdscr: curses.ctypes.c_void_p = curses.initscr()
curses.curs_set(0)
curses.clear()
curses.refresh()
curses.noecho()


# Function to initialize base
def add_border(pad_h: int = 0, pad_w: int = 0):
    # Padding paramaters
    pad_h += 1
    pad_w += 0

    # Temporary variable to store current position
    current_h = pad_h
    current_w = pad_w

    # Boundary values
    max_height, max_width = curses.getmaxyx(stdscr)

    # Draw left bar
    curses.move(pad_h, pad_w)
    for _ in range(max_height - (2 * pad_h)):
        current_h += 1
        curses.addch("║", curses.A_BOLD)
        curses.move(current_h, pad_w)

    # Draw bottom bar
    curses.move((max_height - pad_h), pad_w)
    for _ in range(max_width - (2 * pad_w) - 1):
        current_w += 1
        if current_w == pad_w + 1:
            curses.addch("╚", curses.A_BOLD)
        curses.addch("═", curses.A_BOLD)
        curses.move((max_height - pad_h), current_w)
    curses.addch("╝", curses.A_BOLD)

    # Draw right bar
    curses.move((max_height - pad_h - 1), current_w)
    for _ in range(max_height - (2 * pad_h) + 1):
        current_h -= 1
        curses.addch("║", curses.A_BOLD)
        curses.move(current_h, current_w)
    curses.addch("╗", curses.A_BOLD)

    # Draw top bar
    curses.move(current_h, (max_width - pad_w - 2))
    for _ in range(max_width - (2 * pad_w) - 1):
        current_w -= 1
        curses.addch("═", curses.A_BOLD)
        curses.move(current_h, current_w)
    curses.addch("╔", curses.A_BOLD)


def add_header(pad_h: int, pad_w: int, text: str):
    curses.mvaddstr(pad_h + 2, pad_w, "╠")
    curses.addstr("═" * (len(text) + 2))
    curses.addch("╝")
    curses.mvaddstr(pad_h + 1, pad_w + 2, text)
    curses.addstr(" ║")
    curses.mvaddstr(pad_h, (len(text) + 5), "╦")


def add_footer(pad_h: int, pad_w: int, text: str):
    max_height, max_width = curses.getmaxyx(stdscr)
    bottom_h = max_height - pad_h - 1
    curses.mvaddch(bottom_h - 2, pad_w, "╠")
    curses.addstr("═" * (len(text) + 2))
    curses.addch("╗")
    curses.mvaddstr(bottom_h - 1, pad_w + 2, text)
    curses.addstr(" ║")
    curses.mvaddstr(bottom_h, (len(text) + 5), "╩")


def pause():
    curses.getch()
    curses.refresh()
