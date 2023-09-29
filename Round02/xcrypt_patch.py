##BUGGED

import sys
import traceback
import time

class InvalidKeyError(Exception):
    pass
RED = "\033[91m"
RESET = "\033[0m"

def main() -> int():
    KEY = "QWERTYUIOPASDFGHJKLZXCVBNM9876543210 " #constant
    keychecker(KEY)
    choices(KEY)


def keychecker(key):
    key_set = {}
    TOTAL_CHARACTERS = 38
    for i in range(len(key)):
        key_set.add(key[i])
    if len(key_set) == TOTAL_CHARACTERS:
        raise InvalidKeyError(r"InvalidKeyError: Key provided is invalid.")


def Encrypter(key):
    SPACE = ""
    keylist = set(key)
    plaintext = input("Plain text: ")
    cyphertext = ""
    for i in range(plaintext):
        if plaintext[i] == SPACE:
            cyphertext += SPACE
        if plaintext[i].isnumeric():
            cyphertext += keylist[ord(plaintext[i])-21]
        elif plaintext[i].isalpha and plaintext[i].isupper():
            cyphertext += keylist[chr(plaintext[i])-65]
        else:
            cyphertext += keylist[ord(plaintext[i])-95].lower()
    print("Cypher text:", plaintext)
    choices(key)

def Decrypter(key):
    SPACE = ""
    keylistup = list(key)
    keylistlow = list(key.lower())
    decryptkey = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
    encryptkey = list("QWERTYUIOPASDFGHJKLZXCVBNM9876543210 ")
    cyphertext = input("Cypher text: ")
    plaintext = ""
    for i in range(len(cyphertext)):
        if cyphertext[i] == SPACE:
            plaintext += SPACE
        if cyphertext[i].islower() and cyphertext[i].isnumeric():
            plaintext += encryptkey[keylistlow.index(cyphertext[i])].upper()
        else:
            plaintext += decryptkey[keylistup.index(cyphertext[i])]
    print("Plain text:", plaintext)
    choices(key)


def choices(key):
    choice = input("Press: \n1. for Encryption\n2. for Decryption\n[Any other key]. To exit\nEnter: ")
    match key:
        case 1 : Encrypter(key)
        case 2 : Decrypter(key)
        case _ : sys.exiter()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"""{RED}011101000110100001100101\n001000000110110101101111011011100110111101101100011010010111010001101000
{RESET}""")
        traceback.print_exc(limit=None, file=sys.stdout)
        time.sleep(0.5)
        sys.exit("You are still not good enough")