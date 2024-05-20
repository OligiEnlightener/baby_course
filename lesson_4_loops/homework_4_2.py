def sum_up_even_multiply(lst: list) -> list:
    # summ = 0
    # for number in lst[0::2]:
    #     summ += number
    # return summ * lst[-1] * lst[-1] if len(lst) > 0 else 0
    # return sum(lst[0::2]) * lst[-1] if len(lst) > 0 else 0

    summ = 0
    for x in lst[::2]:
        summ += x
    return summ * lst[-1]


# Code testing
assert sum_up_even_multiply([0, 1, 7, 2, 4, 8]) == 88
assert sum_up_even_multiply([1, 3, 5]) == 30
assert sum_up_even_multiply([6]) == 36
assert sum_up_even_multiply([]) == 0
assert sum_up_even_multiply([1, 1, 1, 1, 1]) == 3
