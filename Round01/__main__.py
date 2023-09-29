import draw
from draw import curses
import Intermediate.Q16.__main__ as Q16
import Intermediate.Q17.__main__ as Q17
import Unidentifiable.Q18.__main__ as Q18

# Store padding
pad_y, pad_x = 1, 2

# Team member names
team = ["Zahiruzzaman Chowdhury", "Fatema Jahan Akhter"]

# Root
char_input = 0
while True:
    draw.add_border(pad_y, pad_x)
    draw.add_header(
        pad_y, pad_x, "What do you want to open?"
    )
    draw.add_footer(
        pad_y, pad_x, "Press ESC to exit"
    )
    curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter a number to continue:")
    curses.mvaddstr(
        pad_y + 6,
        pad_x + 4,
        "[1] (  Intermediate  || Question 16 ) Find pairs of numbers from list that add up a target number",
    )
    curses.mvaddstr(
        pad_y + 7,
        pad_x + 4,
        "[2] (  Intermediate  || Question 17 ) CROCODILE Division",
    )
    curses.mvaddstr(
        pad_y + 8,
        pad_x + 4,
        "[3] ( Unidentifiable || Question 18 ) Vignere Cipher",
    )
    curses.refresh()
    char_input = curses.getch()
    if char_input == 27:  # If ESC
        curses.clear()
        draw.add_footer(
            pad_y, pad_x, f"Collaborative work of {team[0]} and {team[1]}"
        )
        draw.pause()
        break
    elif char_input == 49:  # If 1
        char_input_depth_01 = 0
        while True:
            curses.clear()
            draw.add_border(
                pad_y, pad_x
            )
            draw.add_header(
                pad_y,
                pad_x,
                "Find pairs of numbers from list that add up a target number",
            )
            curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter numbers to add to the list")
            draw.add_footer(
                pad_y,
                pad_x,
                "Press ENTER to finalize input - leave input empty to proceed to next step",
            )
            curses.mvaddstr(pad_y + 6, pad_x + 2, "Answer: ")
            curses.refresh()
            num_list = []
            num = ""
            char_input_depth_02 = 0
            while True:
                char_input_depth_02 = curses.getch()
                if char_input_depth_02 in [10, 12]:
                    if num == "":
                        curses.refresh()
                        break
                    if num:
                        num_list.append(int(num))
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "Answer:                        "
                        )
                        curses.mvaddstr(pad_y + 6, pad_x + 2, "Answer: ")
                        num = ""
                        curses.refresh()
                elif char_input_depth_02 == 8:
                    curses.mvaddstr(
                        pad_y + 6, pad_x + 2, "Answer:                        "
                    )
                    curses.mvaddstr(pad_y + 6, pad_x + 2, "Answer: ")
                    num = ""
                    curses.refresh()
                elif char_input_depth_02 in range(48, 58):
                    num += chr(char_input_depth_02)
                    curses.addch(chr(char_input_depth_02))
                    curses.refresh()
            curses.mvaddstr(
                pad_y + 4, pad_x + 2, "                                    "
            )
            curses.mvaddstr(
                pad_y + 6, pad_x + 2, "                                    "
            )
            curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter targer sum: ")
            curses.refresh()
            target = 0
            num = ""
            char_input_depth_02 = 0
            while True:
                char_input_depth_02 = curses.getch()
                if char_input_depth_02 in [10, 12]:
                    target = int(num)
                    curses.mvaddstr(
                        pad_y + 6, pad_x + 2, "                                    "
                    )
                    curses.refresh()
                    break
                elif char_input_depth_02 in range(48, 58):
                    num += chr(char_input_depth_02)
                    curses.addch(chr(char_input_depth_02))
                    curses.refresh()
                elif char_input_depth_02 == 8:
                    curses.mvaddstr(
                        pad_y + 4, pad_x + 2, "Answer:                        "
                    )
                    curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter targer sum: ")
                    num = ""
            curses.mvaddstr(
                pad_y + 6, pad_x + 2, "                                       "
            )
            curses.refresh()

            # After ans:
            my_list = Q16.find_pairs(
                num_list, target
            )
            curses.clear()
            draw.add_border(
                pad_y, pad_x
            )
            draw.add_header(
                pad_y,
                pad_x,
                "Find pairs of numbers from list that add up a target number",
            )
            draw.add_footer(
                pad_y, pad_x, "Press ESC to go back"
            )
            curses.mvaddstr(pad_y + 4, pad_x + 2, "Your result is as follows:")
            curses.mvaddstr(pad_y + 6, pad_x + 2, str(my_list))
            curses.refresh()

            char_input_depth_01 = curses.getch()
            if char_input_depth_01 == 27:  # If ESC
                curses.clear()
                break
    elif char_input == 50:  # If 2
        char_input_depth_01 = 0
        while True:
            my_ans = (
                Q17.count_ways_to_divide_word()
            )
            curses.clear()
            draw.add_border(
                pad_y, pad_x
            )
            draw.add_header(
                pad_y, pad_x, "CROCODILE Division"
            )
            draw.add_footer(
                pad_y, pad_x, "Press ESC to go back"
            )
            curses.mvaddstr(
                pad_y + 4, pad_x + 2, "Given the condition, the result is as follows:"
            )
            curses.mvaddstr(pad_y + 6, pad_x + 2, f"{my_ans} combinations are possible")
            curses.refresh()
            char_input_depth_01 = curses.getch()
            if char_input_depth_01 == 27:  # If ESC
                curses.clear()
                break
    elif char_input == 51:  # If 3
        char_input_depth_01 = 0
        while True:
            my_ans = (
                Q17.count_ways_to_divide_word()
            )
            curses.clear()
            draw.add_border(
                pad_y, pad_x
            )
            draw.add_header(
                pad_y, pad_x, "Vignere Cipher"
            )
            draw.add_footer(
                pad_y, pad_x, "Press ESC to go back"
            )
            curses.mvaddstr(pad_y + 4, pad_x + 2, "Choose an option:")
            curses.refresh()
            curses.mvaddstr(
                pad_y + 6,
                pad_x + 4,
                "[1] Execute preset task",
            )
            curses.mvaddstr(
                pad_y + 7,
                pad_x + 4,
                "[2] Encrypt",
            )
            curses.mvaddstr(
                pad_y + 8,
                pad_x + 4,
                "[3] Decrypt",
            )
            curses.mvaddstr(
                pad_y + 9,
                pad_x + 4,
                "[4] Guess key length",
            )
            char_input_depth_01 = curses.getch()
            if char_input_depth_01 == 27:  # If ESC
                curses.clear()
                break
            elif char_input_depth_01 == 49:  # If 1
                char_input_depth_01 = 0
                while True:
                    my_ans = (
                        Q17.count_ways_to_divide_word()
                    )
                    curses.clear()
                    draw.add_border(
                        pad_y, pad_x
                    )
                    draw.add_header(
                        pad_y, pad_x, "Vignere Cipher -> Execute preset task"
                    )
                    draw.add_footer(
                        pad_y, pad_x, "Press ESC to go back"
                    )
                    curses.mvaddstr(
                        pad_y + 4,
                        pad_x + 2,
                        "Given the task, the result is as follows:",
                    )
                    curses.mvaddstr(
                        pad_y + 6,
                        pad_x + 2,
                        "Plaintext: ENCRYPTED || Key: 'SECURITYISKEY'",
                    )
                    curses.mvaddstr(
                        pad_y + 7,
                        pad_x + 2,
                        f"Ciphertext: {Q18.Vignere(message='ENCRYPTED', key='SECURITYISKEY').encrypt()}",
                    )
                    curses.mvaddstr(
                        pad_y + 9,
                        pad_x + 2,
                        "Ciphertext: 'WEXAHAKMNP' || Key: 'CHALLENGEACCEPTED'",
                    )
                    curses.mvaddstr(
                        pad_y + 10,
                        pad_x + 2,
                        f"Plaintext: {Q18.Vignere(message='WEXAHAKMNP', key='CHALLENGEACCEPTED').decrypt()}",
                    )
                    curses.mvaddstr(
                        pad_y + 12,
                        pad_x + 2,
                        "Plaintext: 'EXTRACTION' || Key: 'COMPLEXITY'",
                    )
                    curses.mvaddstr(
                        pad_y + 13,
                        pad_x + 2,
                        f"Ciphertext: {Q18.Vignere(message='EXTRACTION', key='COMPLEXITY').encrypt()}",
                    )
                    curses.mvaddstr(
                        pad_y + 15,
                        pad_x + 2,
                        "Ciphertext: 'VWHUJARZTM' || Key: 'ENCRYPTIONISFUN'",
                    )
                    curses.mvaddstr(
                        pad_y + 16,
                        pad_x + 2,
                        f"Plaintext: {Q18.Vignere(message='VWHUJARZTM', key='ENCRYPTIONISFUN').decrypt()}",
                    )
                    curses.mvaddstr(
                        pad_y + 18,
                        pad_x + 2,
                        "Plaintext: 'JTOHYZSFOCQXQY' || Key: *!!!Unknown!!!*",
                    )
                    curses.mvaddstr(
                        pad_y + 19,
                        pad_x + 2,
                        f"Key length (approximate): {Q18.Vignere(message='JTOHYZSFOCQXQY').guess_key_length()}",
                    )
                    curses.refresh()
                    char_input_depth_01 = curses.getch()
                    if char_input_depth_01 == 27:  # If ESC
                        curses.clear()
                        break
            elif char_input_depth_01 == 50:  # If 2
                curses.clear()
                draw.add_border(
                    pad_y, pad_x
                )
                draw.add_header(
                    pad_y, pad_x, "Vignere Cipher -> Encrypt"
                )
                draw.add_footer(
                    pad_y,
                    pad_x,
                    "Press ENTER to finalize input - leave input empty to proceed to next step",
                )
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                    "
                )
                curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter plaintext: ")
                curses.refresh()
                plain = ""
                inp = ""
                char_input_depth_02 = 0
                while True:
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 in [10, 12]:
                        plain = inp
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "                                    "
                        )
                        curses.refresh()
                        break
                    elif char_input_depth_02 in range(
                        65, 91
                    ) or char_input_depth_02 in range(97, 123):
                        inp += chr(char_input_depth_02).upper()
                        curses.addch(chr(char_input_depth_02))
                        curses.refresh()
                    elif char_input_depth_02 == 8:
                        curses.mvaddstr(
                            pad_y + 4, pad_x + 2, "Answer:                        "
                        )
                        curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter plaintext: ")
                        inp = ""
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                       "
                )
                curses.refresh()
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                    "
                )
                curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter key: ")
                curses.refresh()
                keytext = ""
                inp = ""
                char_input_depth_02 = 0
                while True:
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 in [10, 12]:
                        keytext = inp
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "                                    "
                        )
                        curses.refresh()
                        break
                    elif char_input_depth_02 in range(
                        65, 91
                    ) or char_input_depth_02 in range(97, 123):
                        inp += chr(char_input_depth_02).upper()
                        curses.addch(chr(char_input_depth_02))
                        curses.refresh()
                    elif char_input_depth_02 == 8:
                        curses.mvaddstr(
                            pad_y + 4, pad_x + 2, "Answer:                        "
                        )
                        curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter key: ")
                        inp = ""
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                       "
                )
                curses.refresh()

                # After ans:
                while True:
                    cipher = Q18.Vignere(
                        plain, keytext
                    ).encrypt()
                    curses.clear()
                    draw.add_border(
                        pad_y, pad_x
                    )
                    draw.add_header(
                        pad_y, pad_x, "Vignere Cipher -> Encrypt"
                    )
                    draw.add_footer(
                        pad_y, pad_x, "Press ESC to go back"
                    )
                    curses.mvaddstr(pad_y + 4, pad_x + 2, "Your result is as follows:")
                    curses.mvaddstr(pad_y + 6, pad_x + 2, str(cipher))
                    curses.refresh()
                    char_input_depth_02 = 0
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 == 27:  # If ESC
                        curses.clear()
                        break
            elif char_input_depth_01 == 51:  # If 3
                curses.clear()
                draw.add_border(
                    pad_y, pad_x
                )
                draw.add_header(
                    pad_y, pad_x, "Vignere Cipher -> Decrypt"
                )
                draw.add_footer(
                    pad_y,
                    pad_x,
                    "Press ENTER to finalize input - leave input empty to proceed to next step",
                )
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                    "
                )
                curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter ciphertext: ")
                curses.refresh()
                plain = ""
                inp = ""
                char_input_depth_02 = 0
                while True:
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 in [10, 12]:
                        plain = inp
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "                                    "
                        )
                        curses.refresh()
                        break
                    elif char_input_depth_02 in range(
                        65, 91
                    ) or char_input_depth_02 in range(97, 123):
                        inp += chr(char_input_depth_02).upper()
                        curses.addch(chr(char_input_depth_02))
                        curses.refresh()
                    elif char_input_depth_02 == 8:
                        curses.mvaddstr(
                            pad_y + 4, pad_x + 2, "Answer:                        "
                        )
                        curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter ciphertext: ")
                        inp = ""
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                       "
                )
                curses.refresh()
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                    "
                )
                curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter key: ")
                curses.refresh()
                keytext = ""
                inp = ""
                char_input_depth_02 = 0
                while True:
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 in [10, 12]:
                        keytext = inp
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "                                    "
                        )
                        curses.refresh()
                        break
                    elif char_input_depth_02 in range(
                        65, 91
                    ) or char_input_depth_02 in range(97, 123):
                        inp += chr(char_input_depth_02).upper()
                        curses.addch(chr(char_input_depth_02))
                        curses.refresh()
                    elif char_input_depth_02 == 8:
                        curses.mvaddstr(
                            pad_y + 4, pad_x + 2, "Answer:                        "
                        )
                        curses.mvaddstr(pad_y + 4, pad_x + 2, "Enter key: ")
                        inp = ""
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                       "
                )
                curses.refresh()

                # After ans:
                while True:
                    cipher = Q18.Vignere(
                        plain, keytext
                    ).decrypt()
                    curses.clear()
                    draw.add_border(
                        pad_y, pad_x
                    )
                    draw.add_header(
                        pad_y, pad_x, "Vignere Cipher -> Decrypt"
                    )
                    draw.add_footer(
                        pad_y, pad_x, "Press ESC to go back"
                    )
                    curses.mvaddstr(pad_y + 4, pad_x + 2, "Your result is as follows:")
                    curses.mvaddstr(pad_y + 6, pad_x + 2, str(cipher))
                    curses.refresh()
                    char_input_depth_02 = 0
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 == 27:  # If ESC
                        curses.clear()
                        break
            elif char_input_depth_01 == 52:  # If 4
                curses.clear()
                draw.add_border(
                    pad_y, pad_x
                )
                draw.add_header(
                    pad_y, pad_x, "Vignere Cipher -> Guess key length"
                )
                draw.add_footer(
                    pad_y,
                    pad_x,
                    "Press ENTER to finalize input - leave input empty to proceed to next step",
                )
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 6, pad_x + 2, "                                    "
                )
                curses.mvaddstr(
                    pad_y + 4, pad_x + 2, "Enter ciphertext to guess key length of: "
                )
                curses.refresh()
                plain = ""
                inp = ""
                char_input_depth_02 = 0
                while True:
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 in [10, 12]:
                        plain = inp
                        curses.mvaddstr(
                            pad_y + 6, pad_x + 2, "                                    "
                        )
                        curses.refresh()
                        break
                    elif char_input_depth_02 in range(
                        65, 91
                    ) or char_input_depth_02 in range(97, 123):
                        inp += chr(char_input_depth_02).upper()
                        curses.addch(chr(char_input_depth_02))
                        curses.refresh()
                    elif char_input_depth_02 == 8:
                        curses.mvaddstr(pad_y + 4, pad_x + 2, f"Answer:{''*70}")
                        curses.mvaddstr(
                            pad_y + 4,
                            pad_x + 2,
                            "Enter ciphertext to guess key length of: ",
                        )

                # After ans:
                while True:
                    cipher = Q18.Vignere(
                        plain
                    ).guess_key_length()
                    curses.clear()
                    draw.add_border(
                        pad_y, pad_x
                    )
                    draw.add_header(
                        pad_y, pad_x, "Vignere Cipher -> Guess key length"
                    )
                    draw.add_footer(
                        pad_y, pad_x, "Press ESC to go back"
                    )
                    curses.mvaddstr(pad_y + 4, pad_x + 2, "Your result is as follows:")
                    curses.mvaddstr(pad_y + 6, pad_x + 2, str(cipher))
                    curses.refresh()
                    char_input_depth_02 = 0
                    char_input_depth_02 = curses.getch()
                    if char_input_depth_02 == 27:  # If ESC
                        curses.clear()
                        break

curses.endwin()
