"""def arif(a, b, c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
    else:
        return 'Invalid operation'


print(arif(1, 2, '-'))
print(arif(7, 30, '+'))
print(arif(8, 90, '*'))
print(arif(1, 2, 7))


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(True)
    else:
        print(False)


print(is_year_leap(2002))
print(is_year_leap(2003))
print(is_year_leap(2004))


def square(x):
    sq = (4 * x, x ** 2, x ** 0.5)
    return sq


print(square(4))


def season(s):
    if s == 12 or 1 <= s <= 2:
        print('winter')
    elif 3 <= s <= 5:
        print('spring')
    elif 6 <= s <= 8:
        print('summer')
    elif 9 <= s <= 11:
        print('autumn')
    else:
        print('Nothing')


print(season(12))
print(season(3))
print(season(19))


def bank(a, years):
    for i in range(years):
        a *= 1.1
        return a


print(bank(10, 10))


def is_prime(q):
    if type(q) == int:
        print(True)
    else:
        print(False)

    if q > 1000 or q < 0:
        print('Error')


is_prime(1)
is_prime(1001)
is_prime(5.5)"""








