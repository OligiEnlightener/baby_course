def calculate():
    first = int(input("Введите первое число:\n"))
    second = int(input("Введите второе число\n"))
    operation = input("Введите операцию, которую нужно сделать: +, - /, * \n")

    if operation == '+':
        addition = first + second
        print(addition)
    elif operation == '-':
        subtraction = first - second
        print(subtraction)
    elif operation == '/':
        if second != 0:
            division = first / second
            print(division)
        else:
            print("Делить на ноль нельзя! ")
    else:
        multiplication = first * second
        print(multiplication)


calculate()
