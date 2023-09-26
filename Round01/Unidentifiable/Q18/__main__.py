class Vignere:
    """Class containing data structures and methods related to Vignere cipher

    We decided to make it a class rather than definining it as functions in the
    global namespace because we wanted this to have a cleanly stored
    data structure and methods

    While yes, it is more hassle to type `Vignere(message="ENCRYPTED", key="SECURITYISKEY").encrypt()`
    rather than just `vignere_encrypt(message="ENCRYPTED", key="SECURITYISKEY")`,
    this allows us store not just the result of the encrypted text, but also
    allows us to retrieve given parameters on demand much later into execution

    This could be useful when let's say we want to first to run
    the method `self.guess_key_length()` to approximate the length
    of the key, then accordingly try bruteforcing the key without
    typing in the original message more than once

    What if the message was an user input? Do we prompt the user
    to give us the same input value again, word-by-word? Or if
    we're let's say retrieving something from an API - we can
    minimize calls to the API by implementing this data structure"""

    def __init__(self, message: str, key: str = "") -> None:
        """Initialize data structure for manipulating `message`
        with various methods pertaining to Vignere cipher

        ### Args:
            `message` (`str`):
                The message you want to manipulate with provided cipher methods
            `key` (`str`, optional):
                The key you want to use for provided cipher methods. Defaults to `""`,
                but must be populated if you want to run `self.encode()` or `self.decode()`

        ### Raises:
            `ValueError`:
                Exception raised when message is empty
        """
        # Initialize variable to hold error description
        error_text: str = ""

        # Implement a function to check for errors
        # common to both message and key
        #
        # TODO: Turn these limitations into supported functionality
        def common_errors(param_name: str, param_value: str) -> str:
            # Run through a chain of if statements
            # to sniff out errors within `param`
            if not param_value.isalpha():
                return f"{param_name} cannot have non-alphabetical characters"
            if not param_value.isupper():
                return f"{param_name} cannot have lowercase letters"
            return ""

        # Check error cases for `message`
        if len(message) == 0:
            error_text = "Message cannot be empty"
        else:
            error_text = common_errors(message, "Message")

        # Check error cases for `key`
        # but only if a value is given
        #
        # Non-empty strings have a `True` value
        # Blanks ones are implicitly `False`
        if key:
            error_text = common_errors(key, "Key")

        # Raise `ValueError` with appropriate description
        # if the description is not empty
        if not error_text:
            raise ValueError(error_text)

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

    @staticmethod
    def __index_of_coincidence(text: str) -> float:
        """A helper method to return the probability of any
        two randomly selected characters from given string
        being the same. To be used only by methods inside
        this class

        ### Args:
            `text` (`str`):
                Text to find IC of

        ### Returns:
            `float`:
                The IC value of the string, within range 0 to 1
        """
        # Initialize a dictionary to store the frequency of each letter
        freq: dict[str, int] = {}

        # Iterate through each letter in the text
        #
        # Here, we essentially count the frequency
        # of each letter in the text
        for letter in text:
            # Increment frequency count
            # of current letter
            freq[letter] = freq.get(letter, 0) + 1

        # Initialize a variable to store the sum of
        # the products of `freq` and (`freq`-1)
        product_sum: int = 0
        # Iterate through each letter in the frequency dictionary
        for letter in freq:
            # Add product of `freq` and (`freq`-1)
            # to sum, `freq` being the frequency
            # of the current alphabet being iterated
            product_sum += freq[letter] * (freq[letter] - 1)

        # Calculate and return the IC as the sum divided by
        # the product of `text length` and (`text length`-1)
        return product_sum / ((len(text) * (len(text) - 1)) / 1)

    def __crypt_base(self, encrypt: bool) -> str:
        """A helper method meant to unify code for encryption and decryption
        methods. To be used only by methods in this class

        ### Args:
            `encrypt` (`bool`):
                Indicates whether to encrypt message or not

        ### Raises:
            `ValueError`:
                Exception raised when key is empty

        ### Returns:
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

    def guess_key_length(self) -> int:
        """Retrieves the best guess of what the length of the key may be

        NOTE: This is just a pretty close approximation - output
        may be wrong, so please be aware of that. The longer
        the ciphertext is, the more accurate the results get

        Returns:
            int:
                The best-guess length of the key
        """
        # Initialize variable to store maximum IC
        max_ic: float = 0

        # Initialize variable to store best keyword length
        best_length: int = 0

        # Loop through possible keyword lengths from 1 to half of message length
        for length in range(1, len(self.message) // 2 + 1):
            # Initialize a variable to store the ICs sum of all segments
            total_ic: float = 0

            # Loop through each segment with step `length`
            for i in range(length):
                segment = self.message[i::length]
                total_ic += self.__index_of_coincidence(segment)

            # Calculate the average IC of all segments
            avg_ic = total_ic / length

            # If the average IC is greater than the maximum IC,
            # update the maximum IC and best keyword length
            if avg_ic > max_ic:
                max_ic = avg_ic
                best_length = length

        # Return the best keyword length
        return best_length

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
print(Vignere(message="ENCRYPTED", key="SECURITYISKEY").encrypt())

# Task 02
print(Vignere(message="WEXAHAKMNP", key="CHALLENGEACCEPTED").decrypt())

# Task 03
print(Vignere(message="EXTRACTION", key="COMPLEXITY").encrypt())

# Task 04
print(Vignere(message="VWHUJARZTM", key="ENCRYPTIONISFUN").decrypt())

# Task 05
print(Vignere(message="COUUPVCIUTHREUUTFRNUFTRROU").guess_key_length())
