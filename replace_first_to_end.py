def replace_first(list):
    if len(list) >= 1:
        list.append(list[0])
        list.pop(0)
    return list


def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items


def replace_first(items: list) -> list:
    return items[1:] + items[:1]


from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items