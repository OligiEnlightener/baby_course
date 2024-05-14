def last_to_first(lst) -> list:
    if len(lst) > 0:
        lst.insert(0, lst[len(lst) - 1])
        lst.pop()
    return lst


print("1, 2, 3, 4, 5")
print(last_to_first([1, 2, 3, 4, 5]))

print("1")
print(last_to_first([1]))

print("empty list")
print(last_to_first([]))
