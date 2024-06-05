from collections import Counter


def find_unique_value(some_list: list) -> int:
    counted_values = Counter(some_list)
    return min(counted_values, key=counted_values.get)


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
