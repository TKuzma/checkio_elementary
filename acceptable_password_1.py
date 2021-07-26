def is_acceptable_password(password):
    if len(password) > 6:
        return True
    else:
        return False


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


is_acceptable_password = lambda password: len(password) > 6