def correct_sentence(text: str) -> str:
    text_list = [i for i in text]

    text_list[0] = text_list[0].upper()

    if text_list[-1] != '.':
        text_list.append('.')

    text = ''.join(text_list)
    return text


def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


def correct_sentence(text :str) -> str:

    if text[-1] != '.':
        text = text + '.'

    return text.replace(text[0], text[0].upper(), 1)