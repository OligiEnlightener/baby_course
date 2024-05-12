def reverse_number() -> int:
    # 12345
    # 54321 = 50000 + 4000 + 300 + 20 + 1
    print("Функция возвращает перевернутое число.")
    number = int(input("Введи 5-значное число!\n"))
    fifth = int(number % 10 * 10000)
    number = number / 10
    fourth = int(number % 10) * 1000
    number = number / 10
    third = int(number % 10) * 100
    number = number / 10
    second = int(number % 10) * 10
    first = int(number / 10)


    return fifth + fourth + third + second + first


result = reverse_number()
print(result)
