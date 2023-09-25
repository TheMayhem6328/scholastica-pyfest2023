class Vignere:
    """Class containing data structures and methods related to Vignere cipher"""

    def __init__(self, message: str, key: str = "") -> None:
        """Initialize data structure for manipulating `message`
        with various methods pertaining to Vignere cipher

        ### Args:
            `message` (`str`):
                The message you want to manipulate with provided cipher methods
            `key` (`str`, optional):
                The key you want to use for provided cipher methods. Defaults to `""`,
                but must be populated if you want to run `self.encode()` or `self.decode()`
        """
        # Initialize necessary class attributes
        self.message = message
        self.key = key

    @staticmethod
    def __shift_calc(text: str) -> list[int]:
        """A helper method for generating a list of shift values based
        off provided string. To be used only by methods inside this class

        ### Args:
            `text` (`str`):
                String to find shift values of

        ### Returns:
            `list[int]`:
                A list of integers containing shift values in corresponding order of `text`
        """
        # Convert to uppercase, to have them all in the same case
        temp_text: str = text.upper()

        # Get a map object with result of ASCII codes of characters in `secret`
        # This basically runs the function `ord()` on every single character
        # of `secret`, individually, then stores their pattern (not their results
        # yet - we get that after we serialize it to a list)
        #
        # Why not use a `for` loop? Because this is more efficient, since
        # internally, it does the loop using `C` code, which is more efficient
        # than Python's looping mechanisms
        shift: map[int] | list[int] = map(ord, temp_text)

        # Serialize it to a list
        shift = list(shift)

        # Use a list comprehension to subtract the ASCII value of A
        # from every element of the list
        #
        # This allows us to find how many alphabets away
        # every element of the list was from A, hence we have our shift values
        shift = [i - ord("A") for i in shift]

        # Return shift values
        return shift

    def __crypt_base(self, encrypt: bool) -> str:
        """A helper method meant to unify code for encryption and decryption
        methods. To be used only by methods in this class

        Args:
            `encrypt` (`bool`, optional):
                Indicates whether to encrypt message or not

        Raises:
            `ValueError`:
                Exception raised when key is empty

        Returns:
            `str`:
                Contains encrypted/decrypted message, depending on
                the value of paramerer `encrypt`
        """
        # Raise error if key is blank
        if len(self.key) == 0:
            raise ValueError("Key is empty - cannot encrypt")

        # Retrieve shift values
        shift_list: list[int] = self.__shift_calc(self.key)

        # Initialize variable to store current position in shift_list
        shift_position: int = 0

        # Initialize variable to store encrypted list
        cipher: str = ""

        # Initialize variable to store alphabet position
        # of character we'll be iterating through
        char_position: int = 0

        # Iterate through every character of message

        for char in self.message:
            # Calculate position of currently iterated character
            # as difference between its ASCII value and the
            # ASCII value of 'A'
            char_position = ord(char) - ord("A")

            # Retrieve shift value for this iteration
            #
            # We want it to go theough `shift_list` in a cyclic manner,
            # hence we modulo our current `shift_position` with
            # the length of given key so that it the index value
            # does not overflow
            shift_current: int = shift_list[shift_position % len(self.key)]

            # Calculate ASCII value of shifted character
            #
            # We are then retrieving the remainder we get when
            # dividing the result of the summation by 26
            # because we don't want the characted to overflow
            # to non-alphabet regions of ASCII, so that we
            # gracefully cycle through alphabets only
            #
            # If we want to encrypt, we have to add the
            # corresponding shift values, but if we want to
            # decrypt, then we have to work our way back by *subtracting*
            # the corresponding shift values
            if encrypt:
                char_position = (char_position + shift_current) % 26
            else:
                char_position = (char_position - shift_current) % 26

            # Convert it to a proper character
            #
            # We add the ASCII value of 'A' to it because of how
            # we originally subtracted it from `char_position`, for
            # mathematical simplicity - to balance that off, we do this
            char_cipher: str = chr(char_position + ord("A"))

            # Add this character to ciphertext
            # (as character and not ASCII code)
            cipher = cipher + char_cipher

            # Increment `shift_position` for next iteration
            shift_position = shift_position + 1

        # After we've built ciphertext, return it
        return cipher

    def encrypt(self) -> str:
        """Encrypts provided message.
        Key has to be provided for this to work

        Returns:
            `str`:
                Encrypted text
        """
        return self.__crypt_base(encrypt=True)

    def decrypt(self) -> str:
        """Decrypts provided message.
        Key has to be provided for this to work

        Returns:
            `str`:
                Decrypted text
        """
        return self.__crypt_base(encrypt=False)

# Task 01
print(Vignere("THISISATESTHAHAHEHEHUHUWAWA", "SECURITYISKEY").encrypt())

# Task 02
print(Vignere("WEXAHAKMNP", "CHALLENGEACCEPTED").decrypt())

# Task 03
print(Vignere("EXTRACTION", "COMPLEXITY").encrypt())

# Task 04
print(Vignere("VWHUJARZTM", "ENCRYPTIONISFUN").decrypt())
