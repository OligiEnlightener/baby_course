def calculate():
    first = input("Введите первое число:\n")
    second = input("Введите второе число\n")
    operation = input("Введите операцию, которую нужно сделать: +, - /, * \n")

    if operation == '+':
        addition = int(first) + int(second)
        print(str(addition))
    elif operation == '-':
        subtrahtion = int(first) - int(second)
        print(str(subtrahtion))
    elif operation == '*':
        multiplication = int(first) * int(second)
        print(str(multiplication))
    else:
        if second != 0:
            division = int(first) / int(second)
            print(str(division))


calculate()

