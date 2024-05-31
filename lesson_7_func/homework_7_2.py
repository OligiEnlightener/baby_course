def correct_sentence(text: str) -> str:
    words = text.split(" ")
    words[0] = words[0].capitalize()

    for i in range(1, len(words)):
        if words[i - 1].endswith("."):
            words[i] = words[i].capitalize()

    result = " ".join(words).strip()
    if not result.endswith("."):
        result += "."

    return result



assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings. friends.") == "Greetings. Friends.", 'Test5'