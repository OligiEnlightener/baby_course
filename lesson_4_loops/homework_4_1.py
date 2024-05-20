def move_zeros(lst: list) -> list:
    lst.sort(key=lambda x: x == 0)
    return lst


test_list_1 = [0, 1, 3, 5, 0, 6, 7]
test_list_2 = [1, 3, 5, 6, 3, 4]
test_list_3 = []
test_list_4 = [0, 1, 0, 4, 0, 1, 0, 6]
print(move_zeros(test_list_1))
print(move_zeros(test_list_2))
print(move_zeros(test_list_3))
print(move_zeros(test_list_4))
