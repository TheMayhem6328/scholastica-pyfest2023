"""
This is best statically stored pre-calculated
as a constant, since nothing at all is really
variable, but just doing what y'all asked me to do
"""
from math import comb


def count_ways_to_divide_word() -> int:
    """Returns number of ways the word `'CROCODILE'`
    can be divided into three groups of three letters
    each, given that two `'C'`s are in separate groups

    ### Returns:
        `int`:
            Returns the number of ways this is possible
    """
    # Initialize variable to store
    # total number of ways this can
    # be combined, given no restriction
    total_ways: float = 0.0

    # Calculate total ways
    total_ways: float = comb(9, 6) * comb(6, 3)

    # Account for repetition in total
    total_ways /= 2 * 2 * 3

    # Initialize variable to store
    # number of invalid ways to combine
    wrong_ways: int = 0

    # We do it the subtractive way
    # We subtract total by number of invalid cases

    # Calculate number of ways where
    # pattern is `CC* O** O**`
    wrong_ways += comb(5, 1) * comb(4, 2)

    # Calculate number of ways where
    # pattern is `CCO O** ***`
    wrong_ways += comb(5, 2)

    # Calculate number of ways where
    # pattern is `CC* OO* ***`
    wrong_ways += comb(5, 1) * comb(4, 1)

    # Return the right amount of ways
    return int(total_ways) - wrong_ways

# Output result
print(count_ways_to_divide_word())
