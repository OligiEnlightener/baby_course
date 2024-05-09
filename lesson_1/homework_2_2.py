def reverse_number() -> int:
    print("Функция возвращает перевернутое число.")
    number = int(input("Введи 5-значное число!\n"))
    numbers = list(str(number))
    numbers.reverse()

    return int(''.join(str(digit) for digit in numbers))


result = reverse_number()
print(result)
