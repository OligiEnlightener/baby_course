def reverse_array(lst):
    array_2 = lst.copy()
    array_2.reverse()
    print(str(array_2))


print("1, 2, 3, 4, 5")
reverse_array([1, 2, 3, 4, 5])

print("1")
reverse_array([1])

print("empty list")
reverse_array([])
