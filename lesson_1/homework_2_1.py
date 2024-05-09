def number_to_digits() -> list:
    print("Функция разбивает ввееденное вами число на цифры.")
    number = int(input("Введи 4х-значное число!\n"))
    return [int(digit) for digit in list(str(number))]





def print_list(given):
    for each in given:
        print(each)


list_to_print_1 = number_to_digits()
print_list(list_to_print_1)
