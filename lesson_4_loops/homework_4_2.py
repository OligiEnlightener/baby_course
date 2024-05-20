def sum_up_even_multiply(lst: list):
    # summ = 0
    # for number in lst[0::2]:
    #     summ += number
    # return summ * lst[-1] * lst[-1] if len(lst) > 0 else 0
    # return sum(lst[0::2]) * lst[-1] if len(lst) > 0 else 0
    sum = 0

    for x in lst[::2]:
        sum += x
    return sum * lst[-1]


# Code testing
assert sum_up_even_multiply([0, 1, 7, 2, 4, 8]) == 88, ("(0 + 7 + 4) * 8 should be 88,"
                                                        " not ") + str(sum_up_even_multiply([0, 1, 7, 2, 4, 8]))
assert sum_up_even_multiply([1, 3, 5]) == 30, (" (1 + 5) * 5 should be 30,"
                                               " not ") + str(sum_up_even_multiply([1, 3, 5]))
assert sum_up_even_multiply([6]) == 36, (" 6 * 6 should be 36"
                                         ", not ") + str(sum_up_even_multiply([6]))
assert sum_up_even_multiply([]) == 0, ("zero is zero,"
                                       " not ") + str(sum_up_even_multiply([0]))
assert sum_up_even_multiply([1, 1, 1, 1, 1]) == 3, (
        "(1 + 1 + 1) * 1 should be 3, not " + str(sum_up_even_multiply([1, 1, 1, 1, 1])))
