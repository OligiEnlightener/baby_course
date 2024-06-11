def popular_words(text: str, words: list) -> dict:
    return {word: text.lower().split(" ").count(word) for word in words}
    # formatted_text = text.lower().split(" ")
    # for word in words:
    #     result_dict[word] = formatted_text.count(word)
    # return result_dict

#test section
text = 'When I was One I had just begun When I was Two I was nearly new '
words = ['i', 'was', 'three', 'near']
assert popular_words(text, words) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, \
    f"was expactred 'i': 4, 'was': 3, 'three': 0, 'near': 0 , not {popular_words(text, words)}"
