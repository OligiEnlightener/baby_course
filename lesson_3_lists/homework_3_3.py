def divide(lst):
    middle_index = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        result = [lst[0:middle_index], lst[middle_index:]]
        print(result)
    else:
        middle_index += 1
        result = [lst[0:middle_index], lst[middle_index:]]
        print(result)


divide([1, 2, 3])
divide([1, 2, 3, 4])
divide([1, 2, 3, 4, 5, 6, 7, 8, 9])
divide([1])
divide([])
