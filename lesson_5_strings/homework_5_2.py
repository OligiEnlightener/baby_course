from lesson_3_lists.homework_3_2 import calculate


def extend_calculate():
    # calculate()
    answer = input("Якщо хочете продовжити введіть Yes or y\n")
    while answer.lower() == 'yes' or answer.lower() == 'y':
        calculate()
        answer = input("Якщо хочете продовжити введіть Yes or y\n")


extend_calculate()
