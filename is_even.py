def is_even(num: int) -> bool:
    if num % 2 == 0 and -1000 < num < 1000:
        return True
    else:
        return False


def is_even(num: int) -> bool:
    return num & 1 == 0


def is_even(num: int) -> bool:
    return num % 2 == 0


is_even_1 = lambda n : n % 2 == 0