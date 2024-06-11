import string


def format_text(text: str) -> str:
    not_in_word = string.punctuation.replace("'", "")
    return text.translate(str.maketrans(not_in_word, " " * len(not_in_word))).strip()


def first_word(text: str) -> str:
    text = format_text(text)
    text = text.split(" ")
    return text[0]


assert first_word("Hello world") == "Hello", "1 " + f'{first_word("Hello world")}'
assert first_word("greetings, friends") == "greetings", "2 " + f'{first_word("greetings, friends")}'
assert first_word("don't touch it") == "don't", "3 " + f'{first_word("don't touch it")}'
assert first_word(".., and so on ...") == "and", "4 " + f'{first_word(".., and so on ...")}'
assert first_word("hi") == "hi", "5 " + f'{first_word("hi")}'
assert first_word("Hello.World") == "Hello", "6 " + f'{first_word("Hello.World")}'
