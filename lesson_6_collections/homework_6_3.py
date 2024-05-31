def get_input() -> str:
    return input("Введіть ціле число\n")


def multiply_until_single_digit(number: str) -> int:
    result = multiply(number)
    while result > 9:
        result = multiply(str(result))
    return result


def multiply(digits: str) -> int:
    result = 1
    for digit in digits:
        result *= int(digit)
    return result


inputted_number = get_input()
result = multiply_until_single_digit(inputted_number)
print(result)
