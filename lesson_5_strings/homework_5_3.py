import string


def create_hashtag(tag_string: str) -> str:
    result = "#"
    words = tag_string.split()
    for word in words:
        for char in word:
            if char.isspace() or char in string.punctuation:
                word = word.replace(char, "")
        result += word[
                  0:140 - len(result + word)]  # Так оно работает, но может лучше расписать как в следующих строках?
        # if len(result + word) < 140:
        #     result += word
        # else:
        #     result += word[0:140 - len(result + word)]

    return result


create_hashtag('Python Community')
create_hashtag('i like python community!')
create_hashtag('Should, I. subscribe? Yes!')
create_hashtag('t!e@S#T e$XA%m')
create_hashtag(
    'Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community Python Community ')
