class Vignere:
    def __init__(self, message: str, key: str = "") -> None:
        self.message = message
        self.key = key

    @staticmethod
    def __shift_calc(text: str) -> list[int]:
        # Convert to uppercase, to have them all in the same case
        temp_text = text.upper()

        # Get a map object with result of ASCII codes of characters in `secret`
        # This basically runs the function `ord()` on every single character
        # of `secret`, individually, then stores their pattern (not their results
        # yet - we get that after we serialize it to a list)
        #
        # Why not use a `for` loop? Because this is more efficient, since
        # internally, it does the loop using `C` code, which is more efficient
        # than Python's looping mechanisms
        shift = map(ord, temp_text)

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

    def encrypt(self) -> str:
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
            char_position: int = ord(char) - ord("A")

            # Retrieve shift value for this iteration
            #
            # We want it to go theough `shift_list` in a cyclic manner,
            # hence we modulo our current `shift_position` with
            # the length of given key so that it the index value
            # does not overflow
            shift_current: int = shift_list[shift_position % len(self.key)]


            # Calculate ASCII value of shifted character
            #
            # We are then modulo-ing the summation with 26
            # because we don't want the characted to overflow
            # to non-alphabet regions of ASCII, so that we
            # gracefully cycle through alphabets only
            char_position: int = (char_position + shift_current) % 26

            # Convert it to a proper character
            #
            # We add the ASCII value of 'A' to it because of how
            # we originally subtracted it from `char_position`, for
            # mathematical simplicity - to balance that off, we do this
            char_cipher: str = chr(char_position + ord("A"))

            # Add this character to ciphertext
            # (as character and not ASCII code)
            cipher: str = cipher + char_cipher
            
            # Increment `shift_position` for next iteration
            shift_position: int = char_position + 1

        # After we've built ciphertext, return it
        return cipher


print(Vignere("SECRET", "KEY").encrypt())
