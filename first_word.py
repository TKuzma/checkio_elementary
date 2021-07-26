def first_word(text):
    text = text.split()
    return text[0]


def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text