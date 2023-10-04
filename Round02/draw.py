import unicurses as curses

# Initialize curses UI root
stdscr: curses.ctypes.c_void_p = curses.initscr()
curses.curs_set(0)
curses.clear()
curses.refresh()
curses.noecho()

curses.init_pair(  # Initialize a pair of fg and bg colors
    1,  # Number for reference
    curses.COLOR_CYAN,  # Foreground color
    curses.COLOR_BLUE,  # Background color
)

# Function to initialize base
def add_border(pad_h: int = 1, pad_w: int = 2):
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


def add_header(pad_h: int = 1, pad_w: int = 2, text: str = "Head", animate: int = 0):
    curses.mvaddch(pad_h + 2, pad_w, "╠")
    for _ in range(len(text) + 2):
        curses.addch("═")
    curses.addch("╝")
    curses.mvaddch(pad_h, (len(text) + 5), "╦")
    curses.move(pad_h + 1, pad_w + 2)
    for char in text + " ║":
        curses.addch(char)
        if animate != 0:
            curses.refresh()
            curses.napms(animate)


def add_footer(pad_h: int = 1, pad_w: int = 2, text: str = "Footer",animate: int = 0):
    max_height, max_width = curses.getmaxyx(stdscr)
    bottom_h = max_height - pad_h - 1
    curses.mvaddch(bottom_h - 2, pad_w, "╠")
    for _ in range(len(text) + 2):
        curses.addch("═")
    curses.addch("╗")
    curses.mvaddch(bottom_h, (len(text) + 5), "╩")
    curses.move(bottom_h - 1, pad_w + 2)
    for char in text + " ║":
        curses.addch(char)
        if animate != 0:
            curses.refresh()
            curses.napms(animate)


def pause():
    curses.refresh()
    curses.getch()


def add_input(
    pos_y: int,
    pos_x: int,
    accept_numbers: bool = True,
    accept_alphabet: bool = True,
    accept_space: bool = True,
) -> str:
    user_input = ""
    char_input = 0
    while True:
        # Turn on cursor - because fancy :D
        curses.curs_set(1)

        # Get character input
        char_input = curses.getch()

        # If input is Enter, erase input echo
        # and break out of loop
        if char_input in [10, 12]:
            curses.mvaddstr(pos_y, pos_x, " " * len(user_input))
            curses.move(pos_y, pos_x)
            curses.refresh()
            break

        # If input is within normal character set,
        # echo back input
        elif (
            # If input is a number
            (char_input in range(48, 58) and accept_numbers)
            or (
                # If input is an alphabet
                char_input in range(65, 91)
                or char_input in range(97, 123)
                and accept_alphabet
            )
            or (char_input == 32 and accept_space)
        ):
            user_input += chr(char_input)
            curses.addch(chr(char_input))
            curses.refresh()

        # If input is backspace
        elif char_input == 8:
            curses.mvaddstr(pos_y, pos_x, " " * (len(user_input) + 1))
            curses.move(pos_y, pos_x)
            user_input = ""
            curses.refresh()

    # Now that we're done taking input, turn off cursor
    curses.curs_set(0)

    # Return input
    return user_input


def recreate_window(
    pad_y: int = 1,
    pad_x: int = 2,
    header: str = "",
    footer: str = "",
    border: bool = True,
    animate: int = 0
):
    curses.clear()
    if border:
        add_border(pad_y, pad_x)
    if header:
        add_header(pad_y, pad_x, header, animate)
    if footer:
        add_footer(pad_y, pad_x, footer, animate)
    curses.refresh()

def addstr_anim(
    text: str,
    animate: int,
):
    for char in text:
        curses.addch(char)
        if animate != 0:
            curses.refresh()
            curses.napms(animate)

def mvaddstr_anim(
    pos_y: int,
    pos_x: int,
    text: str,
    animate: int,
):
    curses.move(pos_y, pos_x)
    addstr_anim(text, animate)