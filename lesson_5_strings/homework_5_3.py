import string


def create_hashtag(tag_string: str) -> str:
    result = "#"
    words = tag_string.split()
    for word in words:
        for char in word:
            if char.isspace() or char in string.punctuation:
                word = word.replace(char, "")
        word = word.lower()
        word = word.title()
        result += word[0:140 - len(result + word)]  # Так оно работает, но может лучше расписать
                                                    # как в следующих строках?
        # if len(result + word) < 140:
        #     result += word
        # else:
        #     result += word[0:140 - len(result + word)]

    return result


print(create_hashtag('Python Community'))
print(create_hashtag('i like python community!'))
print(create_hashtag('Should, I. subscribe? Yes!'))
print(create_hashtag('t!e@S#T e$XA%m'))

