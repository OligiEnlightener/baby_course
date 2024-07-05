import math


def generate_cube_numbers(end: int) -> list:
    sqrt_3_weight = pow(end, 1 / 3) + 0.00000000000001
    floored_idx = math.floor(sqrt_3_weight)
    for n in range(2, floored_idx + 1):
        yield pow(n, 3)


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], f'оскільки воно менше 10. {list(generate_cube_numbers(10))}'
assert list(generate_cube_numbers(100)) == [8, 27, 64], f'5 у кубі це 125, а воно вже більше 100. {list(generate_cube_numbers(100))}'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

