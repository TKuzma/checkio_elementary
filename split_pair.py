def split_pairs(a):
    new_lst = []

    if len(a) % 2 != 0:
        a += "_"

    for i in range(0, len(a), 2):
        new_lst.append(a[i : i + 2])
    return new_lst


def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]


from textwrap import wrap


def split_pairs(a):
    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)


def split_pairs(a):
    l = len(a)
    if l == 0:
        return []
    if l == 1:
        return [a + '_']
    else:
        return [a[:2]] + split_pairs(a[2:])


    import itertools, operator


    def split_pairs(a):
        it = itertools.chain(a, '_')
        return map(operator.add, it, it)