import math


def is_prime(num: int) -> bool:
    if num <= 1 or (num != 2 and num % 2 == 0):
        return False
    # if num != 2 and num % 2 == 0:
    #     return False
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True


def prime_generator(end):
    for num in range(end + 1):
        if is_prime(num):
            yield num


# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], f'Test1:{list(prime_generator(10))}'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], f'Test2 : {list(prime_generator(15))}'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], f'Test3: {list(prime_generator(29))}'
assert list(prime_generator(100)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                      41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                      89, 97], f'Test3: {list(prime_generator(100))}'
