def is_all_upper(text):
    if text == text.upper():
        return True
    else:
        return False


def is_all_upper(text):
    return text.upper() == text


def is_all_upper(text):
    return text.isupper() if any(i.isalpha() for i in text) else True



