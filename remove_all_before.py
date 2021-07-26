def remove_all_before(items, border):
    for i in range(0, len(items)):
        if (items[i] == border):
            return items[i:]
    return items


def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items


from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items


def remove_all_before(lst, num):
    if num not in lst:
        return lst
    i = lst.index(num)
    return lst[i:]