import random
import math


def make_random_list() -> list:
    result = []
    for number in range(random.randint(3, 10)):
        result.append(random.randint(0, 1000))
        # В примере инты, а я не могу придумать нормальный способ закидывать целыe числа.
    return result


def get_three_values(lst: list) -> list:
    return [lst[0], lst[2], lst[-2]]


def run_and_test():
    ramdom_list_1 = make_random_list()
    ramdom_list_2 = make_random_list()
    ramdom_list_3 = make_random_list()
    assert 3 <= len(ramdom_list_1) <= 10
    assert 3 <= len(ramdom_list_2) <= 10
    assert 3 <= len(ramdom_list_3) <= 10

    short_1 = get_three_values(ramdom_list_1)
    short_2 = get_three_values(ramdom_list_2)
    short_3 = get_three_values(ramdom_list_3)
    assert short_1[0] == ramdom_list_1[0] and short_1[1] == ramdom_list_1[2] and short_1[2] == ramdom_list_1[-2]
    assert short_2[0] == ramdom_list_2[0] and short_2[1] == ramdom_list_2[2] and short_2[2] == ramdom_list_2[-2]
    assert short_3[0] == ramdom_list_3[0] and short_3[1] == ramdom_list_3[2] and short_3[2] == ramdom_list_3[-2]


run_and_test()
