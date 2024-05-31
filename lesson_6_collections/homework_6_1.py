import string

# Мы прошли тему словарей и таплов, но я чет не понял, как её использовать в этом задании.
# сорян, но надеюсь это решение не совсем шляпа


def get_letters(bounds: str):
    result = string.ascii_letters
    return result[result.find(bounds[0]): result.find(bounds[2]) + 1]


def get_input() -> str:
    given = input("Введіть 2 літери у форматі 'a-a': \n")
    return given


print(get_letters(get_input()))

