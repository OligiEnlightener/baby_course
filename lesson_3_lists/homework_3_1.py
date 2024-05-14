def last_to_first(lst):
    if len(lst) > 0:
        lst.insert(0,lst[len(lst) - 1])
        lst.pop()
    print(lst)

print("1, 2, 3, 4, 5")
last_to_first([1, 2, 3, 4, 5])

print("1")
last_to_first([1])

print("empty list")
last_to_first([])
