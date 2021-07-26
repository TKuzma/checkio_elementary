def beginning_zeros(number):
    from itertools import takewhile
    number = str(number)[::1]
    return len(list(takewhile(lambda x: x == '0', number)))


def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


eginning_zeros = lambda number: len(number) - len(number.lstrip('0'))