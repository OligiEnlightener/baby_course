import string


# def edit(text: str) -> str:
#     for char in text:
#         if char.isspace() or char in string.punctuation:
#             text = text.replace(char, "")
#     return text.lower()


def is_palindrome(text: str) -> bool:
    # text = edit(text)
    #return text == text[::-1]
    removed_punctuation = text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    return removed_punctuation == removed_punctuation[::-1]


assert is_palindrome('Ana') == True, 'Test1'
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
