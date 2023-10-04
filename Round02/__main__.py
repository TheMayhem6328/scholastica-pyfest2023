from analysis import Unidentified  # type: ignore[reportUnusedImports]
import xcrypt
import draw
from draw import curses
from os import chdir
from os.path import dirname
from io import open

# Initialization for Part 2
FILENAME: str = "Anomalous - Anomalous.csv"
path: str = dirname(__file__)
chdir(path)
with open(FILENAME, newline="") as file:
    data = Unidentified(file)
    artist_dict = data.artist_songs()
artist_top = data.top_artist(artist_dict)
# Initialization for Part 2, Task 3
# Initialize a dictionary to store word occurrence count
song_word_count_dict: dict[str, int] = {}
# Get a tuple of all names
song_names_list_tuple: tuple[list[str], ...] = tuple(artist_dict.values())
# Iterate through lists in the tuple
for song_names_list in song_names_list_tuple:
    # Iterate through the names in the list
    for song_names in song_names_list:
        # Iterate through the words in the name
        for word in song_names.split(" "):
            # Initialize counter for word if not already initialized
            if word.capitalize() not in song_word_count_dict:
                song_word_count_dict[word.capitalize()] = 0
            # Increment counter for word
            song_word_count_dict[word.capitalize()] += 1
# Convert dict to list for ease of processing
song_word_count_list: list[tuple[str, int]] = list(song_word_count_dict.items())
# Sort them in descending order
song_word_count_list.sort(
    key=lambda item: item[1],  # So that we sort in order of count and not word
    reverse=True,  # We want it to be descending, hence reverse order
)


# Store constants
PAD_Y = 1
PAD_X = 2
TEAM = ["Zahiruzzaman Chowdhury", "Fatema Jahan Akhter"]
ANIMATE = 20
ANIMATE_LONG = 500

# UniCurses setup
curses.bkgdset(curses.COLOR_PAIR(1))

# Root
char_input_0 = 0
while True:
    # Draw UI
    draw.recreate_window(PAD_Y, PAD_X, "What do you want to open?", "Press ESC to exit"    )
    curses.napms(ANIMATE_LONG)
    draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, "Enter a number to continue:", ANIMATE)
    curses.napms(ANIMATE_LONG)
    draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, "[1] (Part 01) XCrypt", ANIMATE)
    draw.mvaddstr_anim(
        PAD_Y + 7, PAD_X + 4, "[2] (Part 02) Unidentified's CSV Explorer", ANIMATE
    )
    curses.bkgd(curses.COLOR_PAIR(1))
    curses.refresh()
    curses.bkgdset(curses.COLOR_PAIR(1))

    char_input_0 = curses.getch()

    ## Conditions for exiting loop

    # If input is ESC
    if char_input_0 == 27:
        curses.clear()
        draw.add_footer(
            PAD_Y, PAD_X, f"Collaborative work of {TEAM[0]} and {TEAM[1]}", ANIMATE
        )

        draw.pause()
        break

    # If input is 1
    elif char_input_0 == 49:
        curses.clear()
        char_input_1 = 0
        while True:
            # Draw UI
            draw.recreate_window(PAD_Y, PAD_X, "XCrypt", "Press ESC to go back")
            curses.napms(ANIMATE_LONG)
            draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, "What do you want to do?", ANIMATE)
            curses.napms(ANIMATE_LONG)
            draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, "[1] Encrypt", ANIMATE)
            draw.mvaddstr_anim(PAD_Y + 7, PAD_X + 4, "[2] Decrypt", ANIMATE)
            curses.refresh()

            char_input_1 = curses.getch()
            # If input is ESC
            if char_input_1 == 27:
                curses.clear()
                break

            # If input is 1
            elif char_input_1 == 49:
                curses.clear()
                char_input_2 = 0
                while True:
                    # Draw UI
                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "XCrypt > Encrypt",
                        "Press ENTER to proceed to output",
                    )
                    curses.napms(ANIMATE_LONG)
                    prompt_text: str = "Enter text to encrypt: "
                    draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, prompt_text, ANIMATE)
                    text_decode = draw.add_input(
                        PAD_Y + 4, PAD_X + 2 + len(prompt_text)
                    )

                    # Process input
                    text_encode = xcrypt.encrypt(text_decode)

                    # Output result
                    draw.recreate_window(
                        PAD_Y, PAD_X, "XCrypt > Encrypt", "Press ESC to go back"
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 4, PAD_X + 2, "You wanted to encrypt:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 5, PAD_X + 2, text_decode, ANIMATE)
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 7, PAD_X + 2, "Here's the ciphered output:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 8, PAD_X + 2, text_encode, ANIMATE)
                    curses.napms(ANIMATE_LONG)
                    curses.refresh()

                    char_input_2 = curses.getch()
                    # If input is ESC
                    if char_input_2 == 27:
                        curses.clear()
                        break

            # If input is 2
            elif char_input_1 == 50:
                curses.clear()
                char_input_2 = 0
                while True:
                    # Draw UI
                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "XCrypt > Decrypt",
                        "Press ENTER to proceed to output",
                    )
                    curses.napms(ANIMATE_LONG)
                    prompt_text: str = "Enter text to decrypt: "
                    draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, prompt_text, ANIMATE)
                    text_encode = draw.add_input(
                        PAD_Y + 4, PAD_X + 2 + len(prompt_text)
                    )

                    # Process input
                    text_decode = xcrypt.decrypt(text_encode)

                    # Output result
                    draw.recreate_window(
                        PAD_Y, PAD_X, "XCrypt > Decrypt", "Press ESC to go back"
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 4, PAD_X + 2, "You wanted to decrypt:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 5, PAD_X + 2, text_encode, ANIMATE)
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 7, PAD_X + 2, "Here's the decrypted output:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 8, PAD_X + 2, text_decode, ANIMATE)
                    curses.refresh()

                    char_input_2 = curses.getch()
                    # If input is ESC
                    if char_input_2 == 27:
                        curses.clear()
                        break

    # If input is 2
    elif char_input_0 == 50:
        curses.clear()
        char_input_1 = 0
        while True:
            # Draw UI
            draw.recreate_window(
                PAD_Y, PAD_X, "Unidentified's CSV Explorer", "Press ESC to go back"
            )
            curses.napms(ANIMATE_LONG)
            draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, "What do you want to do?", ANIMATE)
            curses.napms(ANIMATE_LONG)
            draw.mvaddstr_anim(
                PAD_Y + 6, PAD_X + 4, "[1] Execute Task Sequence", ANIMATE
            )
            draw.mvaddstr_anim(
                PAD_Y + 7, PAD_X + 4, "[2] Find songs of artist", ANIMATE
            )
            draw.mvaddstr_anim(
                PAD_Y + 8,
                PAD_X + 4,
                "[3] Find occurrence of word in song names",
                ANIMATE,
            )
            curses.refresh()

            char_input_1 = curses.getch()
            # If input is ESC
            if char_input_1 == 27:
                curses.clear()
                break

            # If input is 1
            elif char_input_1 == 49:
                curses.clear()
                char_input_2 = 0
                while True:
                    # Draw UI
                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "Unidentified's CSV Explorer > Execute Task Sequence",
                        "Press ESC to go back",
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 4,
                        PAD_X + 2,
                        "Which task do you want to execute?",
                        ANIMATE,
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 6,
                        PAD_X + 4,
                        "[1] (Task 01) Find artist with most songs",
                        ANIMATE,
                    )
                    draw.mvaddstr_anim(
                        PAD_Y + 7,
                        PAD_X + 4,
                        "[2] (Task 02) Find songs by 'Sophia Hall'",
                        ANIMATE,
                    )
                    draw.mvaddstr_anim(
                        PAD_Y + 8,
                        PAD_X + 4,
                        "[3] (Task 03) Find words in song names that were used at least 15 times",
                        ANIMATE,
                    )
                    draw.mvaddstr_anim(
                        PAD_Y + 9,
                        PAD_X + 4,
                        "[4] (Task 04) Find songs by 'The unidentified'",
                        ANIMATE,
                    )
                    curses.refresh()

                    char_input_2 = curses.getch()
                    # If input is ESC
                    if char_input_2 == 27:
                        curses.clear()
                        break

                    # If input is 1
                    elif char_input_2 == 49:
                        curses.clear()
                        char_input_2 = 0
                        while True:
                            # Draw UI
                            draw.recreate_window(
                                PAD_Y,
                                PAD_X,
                                "Unidentified's CSV Explorer > Execute Task Sequence > Task 01",
                                "Press ESC to go back",
                                animate=ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 4,
                                PAD_X + 2,
                                "The artist with the most amount of songs in the dataset is:",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 6, PAD_X + 4, artist_top[0], ANIMATE
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 8,
                                PAD_X + 2,
                                "His songs are as follows: (If the output breaks, please enlarge and reload terminal and script)",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            for index, element in enumerate(artist_top[1]):
                                draw.mvaddstr_anim(
                                    PAD_Y + 10 + index,
                                    PAD_X + 4,
                                    f"{str(index + 1).zfill(2)}] {element}",
                                    ANIMATE,
                                )

                            char_input_2 = curses.getch()
                            # If input is ESC
                            if char_input_2 == 27:
                                curses.clear()
                                break

                    # If input is 2
                    elif char_input_2 == 50:
                        curses.clear()
                        char_input_3 = 0
                        while True:
                            # Initialize artist name
                            name = "Sophia Hall"

                            # Draw UI
                            draw.recreate_window(
                                PAD_Y,
                                PAD_X,
                                "Unidentified's CSV Explorer > Execute Task Sequence > Task 02",
                                "Press ESC to go back",
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 4,
                                PAD_X + 2,
                                "The artist we're looking for is:",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, name, ANIMATE)
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 8,
                                PAD_X + 2,
                                "Her songs are as follows: (If the output breaks, please enlarge and reload terminal and script)",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            for index, element in enumerate(artist_dict[name]):
                                draw.mvaddstr_anim(
                                    PAD_Y + 10 + index,
                                    PAD_X + 4,
                                    f"{str(index + 1).zfill(2)}] {element}",
                                    ANIMATE,
                                )

                            char_input_3 = curses.getch()
                            # If input is ESC
                            if char_input_3 == 27:
                                curses.clear()
                                break

                    # If input is 3
                    elif char_input_2 == 51:
                        curses.clear()
                        char_input_3 = 0
                        while True:
                            # Draw UI
                            draw.recreate_window(
                                PAD_Y,
                                PAD_X,
                                "Unidentified's CSV Explorer > Execute Task Sequence > Task 03",
                                "Press ESC to go back",
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 4,
                                PAD_X + 2,
                                "The words are as follows: (If the output breaks, please enlarge and reload terminal and script)",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            for index, word in enumerate(song_word_count_list):
                                if word[1] < 15:
                                    break
                                draw.mvaddstr_anim(
                                    PAD_Y + 6 + index,
                                    PAD_X + 4,
                                    f"{str(index + 1).zfill(2)}] ({str(word[1]).zfill(2)} occurrences) {word[0]}",
                                    ANIMATE,
                                )
                                curses.napms(ANIMATE_LONG // 2)

                            char_input_3 = curses.getch()
                            # If input is ESC
                            if char_input_3 == 27:
                                curses.clear()
                                break

                    # If input is 4
                    elif char_input_2 == 52:
                        curses.clear()
                        char_input_3 = 0
                        while True:
                            # Initialize artist name
                            name = "The unidentified"

                            # Draw UI
                            draw.recreate_window(
                                PAD_Y,
                                PAD_X,
                                "Unidentified's CSV Explorer > Execute Task Sequence > Task 04",
                                "Press ESC to go back",
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 4,
                                PAD_X + 2,
                                "The artist we're looking for is:",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, name, ANIMATE)
                            curses.napms(ANIMATE_LONG)
                            draw.mvaddstr_anim(
                                PAD_Y + 8,
                                PAD_X + 2,
                                "His songs are as follows:",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                            for index, element in enumerate(artist_dict[name]):
                                draw.mvaddstr_anim(
                                    PAD_Y + 10 + index,
                                    PAD_X + 4,
                                    f"{str(index + 1).zfill(2)}] {element}",
                                    ANIMATE,
                                )
                                curses.napms(ANIMATE_LONG)

                            char_input_3 = curses.getch()
                            # If input is ESC
                            if char_input_3 == 27:
                                curses.clear()
                                break

            # If input is 2
            elif char_input_1 == 50:
                curses.clear()
                char_input_2 = 0
                while True:
                    # Draw UI
                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "Unidentified's CSV Explorer > Find songs of artist",
                        "Press ENTER to proceed to output",
                    )
                    curses.napms(ANIMATE_LONG)
                    # Input word
                    prompt_text: str = "Enter artist to find: "
                    draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, prompt_text, ANIMATE)
                    name = draw.add_input(PAD_Y + 4, PAD_X + 2 + len(prompt_text))

                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "Unidentified's CSV Explorer > Find songs of artist",
                        "Press ESC to go back",
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 4, PAD_X + 2, "The artist we're looking for is:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, name, ANIMATE)
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 8,
                        PAD_X + 2,
                        "Their songs are as follows: (If the output breaks, please enlarge and reload terminal and script)",
                        ANIMATE,
                    )
                    curses.napms(ANIMATE_LONG)
                    try:
                        for index, element in enumerate(artist_dict[name]):
                            draw.mvaddstr_anim(
                                PAD_Y + 10 + index,
                                PAD_X + 4,
                                f"{str(index + 1).zfill(2)}] {element}",
                                ANIMATE,
                            )
                            curses.napms(ANIMATE_LONG)
                    except KeyError:
                        draw.mvaddstr_anim(
                            PAD_Y + 10, PAD_X + 4, "No songs found", ANIMATE
                        )

                    char_input_3 = curses.getch()
                    # If input is ESC
                    if char_input_3 == 27:
                        curses.clear()
                        break

            # If input is 3
            elif char_input_1 == 51:
                curses.clear()
                char_input_2 = 0
                while True:
                    # Draw UI
                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "Unidentified's CSV Explorer > Find occurrence of word in song names",
                        "Press ENTER to proceed to output",
                    )
                    curses.napms(ANIMATE_LONG)
                    # Input word
                    prompt_text: str = "Enter word to find: "
                    draw.mvaddstr_anim(PAD_Y + 4, PAD_X + 2, prompt_text, ANIMATE)
                    word = draw.add_input(PAD_Y + 4, PAD_X + 2 + len(prompt_text))

                    try:
                        count = str(song_word_count_dict[word.capitalize()]).zfill(2)
                    except KeyError:
                        count = "No"

                    draw.recreate_window(
                        PAD_Y,
                        PAD_X,
                        "Unidentified's CSV Explorer > Find occurrence of word in song names",
                        "Press ESC to go back",
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 4, PAD_X + 2, "The word we're looking for is:", ANIMATE
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(PAD_Y + 6, PAD_X + 4, word, ANIMATE)
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 8,
                        PAD_X + 2,
                        "The occurrences of this word is as follows:",
                        ANIMATE,
                    )
                    curses.napms(ANIMATE_LONG)
                    draw.mvaddstr_anim(
                        PAD_Y + 10, PAD_X + 4, f"{count} occurrences", ANIMATE
                    )

                    char_input_3 = curses.getch()
                    # If input is ESC
                    if char_input_3 == 27:
                        curses.clear()
                        break


curses.endwin()
