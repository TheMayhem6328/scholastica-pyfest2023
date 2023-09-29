## deBUGGED

import sys
import traceback
import time


class InvalidKeyError(Exception):
    pass


RED: str = "\033[91m"
RESET: str = "\033[0m"


def main() -> None:
    KEY: str = "QWERTYUIOPASDFGHJKLZXCVBNM9876543210 "
    key_checker(KEY)
    choices(KEY)


def key_checker(key: str) -> None:
    key_set: set[str] = set()
    TOTAL_CHARACTERS: int = 37
    for i in key:
        key_set.add(i)
    if len(key_set) != TOTAL_CHARACTERS:
        raise InvalidKeyError(r"InvalidKeyError: Key provided is invalid.")


def encrypter(key: str) -> None:
    SPACE: str = " "
    key_list: list[str] = list(key)
    plaintext: str = input(f"\n\n══════════════╗\n\033[1mPlain text    : {RESET}")
    cipher_text: str = ""
    for i in plaintext:
        if i == SPACE:
            cipher_text += SPACE
        elif i.isnumeric():
            cipher_text += key_list[ord(i) - 22]
        elif i.isupper():
            cipher_text += key_list[ord(i) - 65]
        else:
            cipher_text += key_list[ord(i) - 97].lower()
    print(f"\033[1mCiphered text : {RED+cipher_text+RESET}\n══════════════╝\n\n")
    choices(key)


def decrypter(key: str) -> None:
    SPACE: str = " "
    key_list_up: list[str] = list(key)
    key_list_low: list[str] = list(key.lower())
    decrypt_key: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
    encrypt_key: list[str] = list("QWERTYUIOPASDFGHJKLZXCVBNM9876543210 ") # type: ignore[reportUnusedVariable]
    cipher_text = input(f"\n\n═══════════════╗\n\033[1mCiphered text  : {RESET}")
    plaintext = ""
    for i in cipher_text:
        if i == SPACE:
            plaintext += SPACE
        elif i.islower() or i.isnumeric():
            plaintext += decrypt_key[key_list_low.index(i)].lower()
        else:
            plaintext += decrypt_key[key_list_up.index(i)].upper()
    print(f"\033[1mDecrypted text : {RED+plaintext+RESET}\n═══════════════╝\n\n")
    choices(key)


def choices(key: str) -> None:
    choice = input(f"\033[30;47;1mChoose an option:{RESET}\n═════════════════\n[1] Encrypt Text\n[2] Decrypt Text\n\nEnter anything else to exit\nEnter an option: ")
    match choice:
        case "1": encrypter(key)
        case "2": decrypter(key)
        case _: sys.exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"""{RED}011101000110100001100101\n001000000110110101101111011011100110111101101100011010010111010001101000
{RESET}""")
        traceback.print_exc(limit=None, file=sys.stdout)
        time.sleep(0.5)
        sys.exit("You are still not good enough")
