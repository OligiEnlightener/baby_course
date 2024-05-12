def divide(lst):
    if len(lst) > 0:
        if len(lst) % 2 == 0:
            middle_index = int(len(lst) / 2)
            print(str(lst[0:middle_index]), str(lst[middle_index:]))
        else:
            middle_index = int((len(lst) / 2) + 1)
            print(str(lst[0:middle_index]), str(lst[middle_index:]))
    else:
        print([])


divide([1, 2, 3])
divide([1, 2, 3, 4])
divide([1, 2, 3, 4, 5, 6, 7, 8, 9])
divide([1])
divide([])
