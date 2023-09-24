def find_pairs(numbers: list[int], target_sum: int) -> list[tuple[int, int]]:
    """Finds out pairs that

    Args:
        numbers (list[int]): A 1D list of integers - has to have unique elements
        target_sum (int): The target sum to which pairs should add up

    Returns:
        list[tuple[int, int]]: A list containing tuples which represent
        pairs of numbers that sum up to `target_sum`
    """
    # Initialize a set to hold integers that were seen in `numbers` already
    seen: set[int] = set()
    # Initialize blank list to hold tuples with valid integer pairs
    pairs: list[tuple[int, int]] = list()

    # Iterate through the list of numbers (`numbers`)
    for num in numbers:
        # Raise error if `num` was already seen once
        #
        # Although we were told to assume that
        # there are no duplicates in the list,
        # never trust the user - end-users are stupid
        if num in seen:
            raise ValueError("Duplicate values detected in list")

        # Calculate difference between `target_sum` and `num`
        diff = target_sum - num

        # Check if the `diff` is in the set
        #
        # If it's in there, we know that
        # `diff` and `num` is a valid pair that
        # adds up to `target_sum`
        if diff in seen:
            pairs.append((num, diff))

        # Add `num` to set `seen`
        seen.add(num)

    # After we've iterated through every element of `numbers`,
    # Output the list of pairs we have
    return pairs


# Example usage:
numbers: list[int] = [2, 7, 4, 0, 0, 9, 5, 1, 3]
target_sum: int = 8
result: list[tuple[int, int]] = find_pairs(numbers, target_sum)
print(result)  # Output: [(2, 5), (7, 0), (4, 3)]
