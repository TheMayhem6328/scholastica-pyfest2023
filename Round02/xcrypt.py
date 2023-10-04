KEY: str = "QWERTYUIOPASDFGHJKLZXCVBNM9876543210 "
SPACE: str = " "

def encrypt(plain: str) -> str:
    key_list: list[str] = list(KEY)
    cipher: str = ""
    for i in plain:
        if i == SPACE:
            cipher += SPACE
        elif i.isnumeric():
            cipher += key_list[ord(i) - 22]
        elif i.isupper():
            cipher += key_list[ord(i) - 65]
        else:
            cipher += key_list[ord(i) - 97].lower()
    return cipher


def decrypt(cipher: str) -> str:
    key_list_up: list[str] = list(KEY)
    key_list_low: list[str] = list(KEY.lower())
    decrypt_key: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    plain = ""
    for i in cipher:
        if i == SPACE:
            plain += SPACE
        elif i.islower() or i.isnumeric():
            plain += decrypt_key[key_list_low.index(i)].lower()
        else:
            plain += decrypt_key[key_list_up.index(i)].upper()
    return plain
