def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))


def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())


def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0

    return 1 + end_zeros(number[:-1])


def end_zeros(number):
    if not number:
        return 1
    if not number % 10:
        return 1 + end_zeros(number // 10)
    return 0


def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result


def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')


def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))