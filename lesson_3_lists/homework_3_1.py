def last_to_first(lst):
    if len(lst) > 0:
        array_2 = [lst[len(lst) - 1]]
        array_2 += lst.copy()
        array_2.pop()
        print(array_2)
    else:
        print(lst)

print("1, 2, 3, 4, 5")
last_to_first([1, 2, 3, 4, 5])

print("1")
last_to_first([1])

print("empty list")
last_to_first([])
