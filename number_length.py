def number_length(a):
    return len(str(a))


def number_length(number: int) -> int:
    base, result = 10, 1
    while base <= number:
        base = (base << 3) + (base << 1)
        result += 1
    return result


def number_length(a: int) -> int:
    return 1 + ((b := a // 10) and number_length(b))


def number_length(a: int) -> int:
    digits = 0
    while a:
        digits += 1
        a //= 10
    return digits + (not digits)