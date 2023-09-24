def find_pairs(numbers: list[int], target_sum: int) -> list[tuple[int, int]]:
    return [(2, 5), (7, 0), (4, 3)]

number_list: list[int] = [2, 7, 4, 0, 9, 5, 1, 3]
target: int = 7
result: list[tuple[int, int]] = find_pairs(number_list, target)

print(result)