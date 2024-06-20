def get_args(func):
    def wrapper(*args):
        result = func(*args)
        name = func.__name__
        args_str = ', '.join(repr(arg) for arg in args)
        print(f'func: {name} ({args_str}), -> {result}')
        return result

    return wrapper

@get_args
def sum_up(a: int, b: int) -> int:
    return a + b


@get_args
def pow_of_two(power: int) -> int:
    return pow(2, power)


@get_args
def recursive_power(base: int, power: int) -> int:
    if power == 0:
        return 1
    return base * recursive_power(base, power - 1)


sum_up(1, 2)
pow_of_two(3)
recursive_power(2,7)
