def move_zeros(lst: list):

    for number in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
    return lst

test_list_1 = [0, 1, 3, 5, 0, 6, 7]
test_list_2 = [1, 3, 5, 6, 3, 4]
test_list_3 = []
print(move_zeros(test_list_1))
print(move_zeros(test_list_2))
print(move_zeros(test_list_3))