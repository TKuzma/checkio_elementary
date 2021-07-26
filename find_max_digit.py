def max_digit(number):
    number = list(str(number))
    return int(max(number))


# max_digit = lambda number: int(max(str(number)))


def max_digit(number: int) -> int:
    return int(max(str(number)))


def max_digit(number: int) -> int:
    return max([int(i) for i in str(number)])