def divide(lst) -> list:
    middle_index = int(len(lst) / 2)
    result = []
    if len(lst) % 2 == 0:
        result = [lst[0:middle_index], lst[middle_index:]]
    else:
        middle_index += 1
        result = [lst[0:middle_index], lst[middle_index:]]

    return result


print(divide([1, 2, 3]))
print(divide([1, 2, 3, 4]))
print(divide([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(divide([1]))
print(divide([]))
