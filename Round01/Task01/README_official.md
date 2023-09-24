# Question 16

You are given a list of integers called `numbers`, and your task is to find all pairs of
elements in the list that sum up to a target value `target_sum`. Write a Python program
to find and print all such pairs. Each pair should be printed only once, and the order of
elements in a pair does not matter.

Your program should define a function called `find_pairs(numbers, target_sum)` that takes
in the following parameters:

- `numbers`: A 1D list of integers.
- `target_sum`: The target sum to which pairs should add up.

The function should return a list of tuples, where each tuple represents a pair of
numbers that sum up to `target_sum`.
Here is an example of how the function should work:

```py
pythonnumbers = [2, 7, 4, 0, 9, 5, 1, 3]
target_sum = 7
result = find_pairs(numbers, target_sum)
# The expected output for this example is:
# [(2, 5), (7, 0), (4, 3)]
```

In this example, the pairs (2, 5), (7, 0), and (4, 3) are the pairs of elements from the
`numbers` list that add up to the `target_sum` of 7.

Your solution should handle edge cases and be efficient in terms of time complexity.

## Note

You can assume that there are no duplicate elements in the `numbers` list, and a number
cannot be used more than once to form a pair.
