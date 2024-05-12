def number_to_digits():
    print("Функция разбивает ввееденное вами число на цифры.")
    number = int(input("Введи 4х-значное число!\n"))
    print(int(number/1000))
    number = number % 1000
    print(int(number/100))
    number = number % 100
    print(int(number/10))
    number = number % 10
    print(number)

number_to_digits()
