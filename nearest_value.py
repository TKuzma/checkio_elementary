def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    n = 1
    while True:
        if (one - n) in values:
            return one - n
        elif (one + n) in values:
            return one + n
        n += 1